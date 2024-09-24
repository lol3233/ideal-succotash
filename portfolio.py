# ⚠️ USE AT YOUR OWN RISK
# first: pip install pysqlite3-binary
# then in settings.py:

# these three lines swap the stdlib sqlite3 lib with the pysqlite3 package
__import__('pysqlite3')
import sys
import os
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')





import pandas as pd
import chromadb
import uuid

class Portfolio:
    def __init__(self , file_path="https://raw.githubusercontent.com/codebasics/project-genai-cold-email-generator/main/my_portfolio.csv"):
        self.file_path=file_path
        self.data=pd.read_csv(file_path)
        self.chroma_client=chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection("portfolio")

    def load_portfolio(self):
        if not self.collection.count():
           for _, row in self.data.iterrows():
              self.collection.add(documents=row["Techstack"],
                       metadatas = {"links":row["Links"]}, 
                       ids= [str(uuid.uuid4())])    
              
    def query_links(self,skills):
        return self.collection.query(query_texts=skills, n_results=2).get('metadatas',[])


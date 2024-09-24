from chains import Chain
from portfolio import Portfolio
from utils import clean_text
import os
import streamlit as st
from langchain_community.document_loaders import WebBaseLoader



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join('/workspaces/codespaces-jupyter/', 'db.sqlite3'),
    }
}





def create_streamlit_app(llm, portfolio, clean_text):
    st.title("🐦 Thandi Patrika")
    url_input = st.text_input("Enter a URL:", value="https://jobs.nike.com/job/R-33460")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Thandi Patrika", page_icon="🐦")
    create_streamlit_app(chain, portfolio, clean_text)

    
     
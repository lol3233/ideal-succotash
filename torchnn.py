#import dependencies
from torch import nn
from torch.optim import Adam
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor


train = datasets.MNIST(root="/workspaces/codespaces-jupyter/",download=True , train=True, transform=ToTensor())
datasets = DataLoader(train , 32 )

class ImageClassifier(nn.Module):
    def __init__(self):
        self.model = nn.Sequential(
            nn.Conv2d(1,32,(3,3)),
            nn.ReLU(),
            nn.Conv2d(32,64,(3,3)),
            nn.ReLU(),
            nn.Conv2d(64,64,(3,3)),
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(64*(28-6)*(28-6),10)


        )
    

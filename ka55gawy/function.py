import numpy as np 
from ipywidgets import interact, fixed
from PIL import Image

def imshow(X, resize=None):
    """
    Pass an PIL Image class, 
    pass resize as tuple
    """
    if resize:
        X = X.resize(resize)
    X.show()
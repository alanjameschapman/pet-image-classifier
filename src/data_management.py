# import numpy as np
# import pandas as pd
# import os
# import base64
# from datetime import datetime
import joblib


def load_pkl_file(file_path):
    '''
    Loads pickle file
    '''
    
    return joblib.load(filename=file_path)

import os
import streamlit as st
from src.data_management import load_pkl_file


def load_test_evaluation(version):
    '''
    Loads pickle file using function imported from data management
    '''

    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    outputs = os.path.join(base_dir, f'outputs/{version}')

    return load_pkl_file(f'{outputs}/evaluation.pkl')

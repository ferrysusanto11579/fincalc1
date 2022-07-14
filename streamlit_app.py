import streamlit as st
import pandas as pd
import numpy as np
import pickle
import xgboost as xgb
import datetime as dt
import matplotlib.pyplot as plt
import altair as alt
from sklearn.utils import shuffle


#####################################################################
## Global variables
SIM_INPUT_MAXDATE = dt.date.today() + dt.timedelta(days=365*2)
SIM_INPUT_NUMERIC_LINSPACE = 4


#####################################################################
st.write('# Melbourne Housing Market')

st.write('## Introduction')

if st.checkbox('Objective'):
	st.write('''
			* Perform exploratory data analysis using [Jupyter notebook](https://jupyter.org/)
			* Data cleaning, feature engineering, and modelling
			* Build an app using [Streamlit](https://docs.streamlit.io/en/stable/)
			* Allow user to do exploratory analysis of a pre-selected suburb
			* Using the pre-trained model, allow user to estimate/forecast Housing price
		''')

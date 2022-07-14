import streamlit as st
import pandas as pd
import numpy as np



##################################################################### CONFIG

config = {}



##################################################################### SIDEBAR

with st.sidebar:
	
	sb_baserev = st.text_input('Base revenue')

	sb_revunit = st.radio(
		'',
		('million','billion')
	)



##################################################################### MAIN PAGE
st.write('# Financial Modelling')

st.write('## Introduction')

if st.checkbox('Objective'):
	st.write('''
			* Perform exploratory data analysis using [Jupyter notebook](https://jupyter.org/)
			* Data cleaning, feature engineering, and modelling
			* Build an app using [Streamlit](https://docs.streamlit.io/en/stable/)
			* Allow user to do exploratory analysis of a pre-selected suburb
			* Using the pre-trained model, allow user to estimate/forecast Housing price
		''')

if st.checkbox('Technical overview'):
	st.write('''
			* Data source: [Melbourne Housing Market](https://www.kaggle.com/anthonypino/melbourne-housing-market)
			* Exploratory data analysis notebook: [link](https://github.com/ferrysusanto11579/melb-housing/blob/main/notebook/Melbourne%20Housing%20Market%20-%20EDA.ipynb)
			* Import raw data
			* Data cleaning, missing data imputations, feature engineering
			* ML modelling (xgboost)
			* Model analysis (feature importance, explain the model using [SHAP](https://shap.readthedocs.io/en/latest/))
			* Save the data & trained model (used as an input to this app)
			* Build interactive visualisations (using altair package) to allow exploratory data analysis for a particular Suburb
			* Predict the House Price using the ML model
			* Display output for analysis
		''')

	


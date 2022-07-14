import streamlit as st
import pandas as pd
import numpy as np



##################################################################### CONFIG

config = {}



##################################################################### SIDEBAR

with st.sidebar:
	
	sb_baserevenue = st.text_input('Base Revenue')

	sb_revenueunit = st.radio('unit', ('million','billion'))
	
	sb_revenuegrowth1 = st.text_input('Revenue growth (next year)', value=0.05)
	sb_revenuegrowthN = st.text_input('Revenue growth (terminal year)', value=0.02)
	
	sb_sharesout = st.text_input('Shares outstanding', value=100)
	sb_sharesoutunit = st.radio('unit2', ('million','billion'))
	
	sb_netmargin = st.text_input('Net margin (%)', value=0.10)
	sb_fcfmargin = st.text_input('FCF margin (%)', value=0.10)
	
	sb_numofyears = st.text_input('Number of years', value=10)
	sb_terminalyearmultiple = st.text_input('Terminal year multiple', value=12)
	sb_discountrate = st.text_input('Discount rate (%)', value=0.125)



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

	


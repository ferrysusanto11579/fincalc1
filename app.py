import streamlit as st
import pandas as pd
import numpy as np



##################################################################### CONFIG

config = {}



##################################################################### SIDEBAR

with st.sidebar:
	
	sb_baserevenue = st.number_input('Base Revenue')

	sb_revenueunit = st.radio('Rev. unit', ('million','billion'))
	
	sb_revenuegrowth1 = st.number_input('Revenue Growth (next year)', value=0.05)
	sb_revenuegrowthN = st.number_input('Revenue Growth (terminal year)', value=0.02)
	
	sb_sharesout = st.number_input('Shares Outstanding', value=100)
	sb_sharesoutunit = st.radio('Shares Out. unit', ('million','billion'))
	
	sb_netmargin = st.number_input('Net Margin (%)', value=0.15)
	sb_fcfmargin = st.number_input('FCF Margin (%)', value=0.15)
	
	sb_numofyears = st.number_input('Number of Years', value=10)
	sb_terminalyearmultiple = st.number_input('Terminal Year Multiple', value=12)
	sb_discountrate = st.number_input('Discount Rate (%)', value=0.125)



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

	


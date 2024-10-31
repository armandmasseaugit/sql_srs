import pandas as pd
import streamlit as st
import duckdb as db

st.write(
    '''# SQL Space Repetition System'''
)

st.selectbox(
    label='What would you like to review ?',
    options=('Join','Group by',
           'Window functions'),
    index=None,
    placeholder='Select a theme...'
)


st.write('Le tableau tableau_df est défini comme tel :')

tableau_df = pd.DataFrame(
    {'Name': ['John', 'Alice', 'Bob'],
       'Age': [25, 30, 35],
       'City': ['New York', 'London', 'Paris']}
)#.set_index('Name')

st.dataframe(tableau_df)

tab1, tab2, tab3 = st.tabs(['Select','f','t'])

with tab1:
    query = st.text_area(label='Entrez votre requête SQL')
    st.dataframe(db.sql(query))
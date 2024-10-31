import pandas as pd
import streamlit as st
import duckdb as db

st.write(
    '''# SQL Space Repetition System'''
)

st.selectbox(
    label=('Join','Group by',
           'Window functions'),
    index=None,
    placeholder='Select a theme...'
)


st.write('Le tableau tableau_df est défini comme tel :')

tableau_df = pd.DataFrame(
    {'name': ['John', 'Alice', 'Bob'],
       'age': [25, 30, 35],
       'city': ['New York', 'London', 'Paris']}
)#.set_index('Name')

st.write(
    '''Write an SQL query to only display 
    the lines of people aged>27yo'''
)

query = st.text_area(label='Enter your SQL query')
st.dataframe(db.sql(query))

tables, solution, tab3 = st.tabs(['Tables', 'Solutions'])

with tables:
    st.dataframe(tableau_df)

with solution:
    st.dataframe(
        tableau_df
        .query('age>=27')
    )
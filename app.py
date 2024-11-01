# pylint: disable=missing-module-docstring.
import pandas as pd
import streamlit as st
import duckdb as db

tableau_df = pd.DataFrame(
    {
        "name": ["John", "Alice", "Bob"],
        "age": [25, 30, 35],
        "city": ["New York", "London", "Paris"],
    }
)  # .set_index('Name')

solution_df = db.sql(
    """SELECT * FROM
        tableau_df
        WHERE age>27"""
).df()

st.write("""# SQL Space Repetition System""")

st.selectbox(
    label="What would you like to review ?",
    options=("Join", "Group by", "Window functions"),
    index=None,
    placeholder="Select a theme...",
)

st.write("tableau_df is defined as follow :")
st.dataframe(tableau_df)
st.write(
    """Write an SQL query to only display 
    the lines of people aged>27yo"""
)

query = st.text_area(label="Enter your SQL query")

result, solution = st.tabs(["Result", "Solution"])

with result:
    if query:
        result_df = db.sql(query).df()
        st.dataframe(result_df)
        try:
            if result_df.compare(solution_df):
                st.write("Good job !")
            else:
                st.write("Wrong ! Try again")
        except ValueError as e:
            st.write("Problem")


with solution:
    st.dataframe(solution_df)

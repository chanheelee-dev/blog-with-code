import streamlit as st
import pandas as pd

import db_util as db


st.title("SQL Demo")

# show tables
db_name = st.selectbox(label="Select a database", options=db.get_database_names())
st.write("Tables in the selected database:")
st.table(db.get_table_names(db_name))

# query editor
query = st.text_area(label="Enter your SQL query here", value="SELECT * FROM data")

# show result
if st.button("Run query"):
    result = db.execute_query(db_name, query)
    st.text("Query result:")
    st.write(pd.DataFrame(result))
else:
    st.text("Query result:")

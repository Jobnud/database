
from sqlalchemy import create_engine
import streamlit as st
import pandas as pd

st.title("📈 AI Analizator Dochodów")

# Połączenie z bazą przez SQLAlchemy + pymssql
server = 'oleksiidb.database.windows.net'
database = 'alexdb'  # poprawna nazwa bazy (nie 'aalexdb')
username = 'alex'
password = 'qwertyQWERTY228'

engine = create_engine(f"mssql+pymssql://{username}:{password}@{server}:1433/{database}")

# Wczytaj dane do DataFrame
df = pd.read_sql("SELECT * FROM history", engine)

st.subheader("📊 Dane historyczne z bazy danych")
st.dataframe(df)

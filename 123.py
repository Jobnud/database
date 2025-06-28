import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.title("📈 AI Analizator Dochodów")

# Parametry połączenia (najlepiej pobierać z env zmiennych - zobacz dalej)
server = 'oleksiidb.database.windows.net'
database = 'alexdb'
username = 'alex'
password = 'qwertyQWERTY228'

# Tworzymy silnik SQLAlchemy z pymssql (bez portu 1433 - domyślny)
engine = create_engine(f"mssql+pymssql://{username}:{password}@{server}/{database}")

# Zapytanie i załadowanie danych do DataFrame
@st.cache_data  # cache, żeby nie przeładowywać za każdym razem
def load_data():
    query = "SELECT * FROM history"
    return pd.read_sql(query, engine)

df = load_data()

st.subheader("📊 Dane historyczne z bazy danych")
st.dataframe(df)
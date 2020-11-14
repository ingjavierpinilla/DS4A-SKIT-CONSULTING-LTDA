from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("postgresql+psycopg2://postgres:7$col&ds0@ds4a-70-db.cgxzuy7k08ix.us-east-2.rds.amazonaws.com/")
df_model = pd.read_sql_table('df_model',engine)
original = pd.read_sql_table('skit_final',engine)
SKIT_FINAL = pd.read_sql_table('skit_final',engine)
Table_Stage = pd.read_sql_table('table_stage',engine)
new_variables = pd.read_sql_table('new_variables',engine)
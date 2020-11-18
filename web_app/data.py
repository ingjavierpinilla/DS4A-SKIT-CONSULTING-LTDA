from sqlalchemy import create_engine
import pandas as pd
from keys import pass, ip

engine = create_engine("postgresql+psycopg2://postgres:" + pass + "@" + ip + "/")
df_model = pd.read_sql_table('df_model',engine)
original = pd.read_sql_table('skit_final',engine)
SKIT_FINAL = pd.read_sql_table('skit_final',engine)
Table_Stage = pd.read_sql_table('table_stage',engine)
new_variables = pd.read_sql_table('new_variables',engine)

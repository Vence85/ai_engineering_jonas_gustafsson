from pathlib import Path
import duckdb

DATA_PATH = Path(__file__).parent / "data_restaurants"
DATA_PATH.mkdir(exist_ok=True)

def query_duckdb(sql_code, parameters=None):
    with duckdb.connect(DATA_PATH / "restaurants.duckdb") as conn:
        cursor = conn.execute(sql_code, parameters)

        sql_code = sql_code.strip().casefold()
        if sql_code.startswith(("select", "desc", "pragma")):
            return cursor.df()

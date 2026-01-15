from utils import query_duckdb

if __name__ == "__main__":

    query_duckdb("""
        CREATE TABLE IF NOT EXISTS restaurant(
                name TEXT,
                food TEXT,
                price_level INTEGER,
                rating DOUBLE,
                description TEXT,
                opening_hours TEXT,
                location TEXT
            );
                
    """)

    print(query_duckdb("desc;"))
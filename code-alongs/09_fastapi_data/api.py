from fastapi import FastAPI, Query
from data_processing import DataExplorer

app = FastAPI()

explorer = DataExplorer(limit=100)

@app.get("/sales")
async def read_sales():
    return explorer.df.to_dict(orient="records")

@app.get("/summary")
async def read_summary_data():
    """
    Return some basic KPIs (Key Performance Indicators)
    from the Sales.csv data.
    """
    df = explorer.df  # de första 100 raderna som Dataexplorer läste in

    return {
        
        # how many different countries appear
        "unique_countries": df["Country"].nunique(),
        # total revenue (assuming there is a column named "Revenue" or "Sales")
        "total_revenue": float(df["Revenue"].sum()),

        # average revenue per transaction
        "avg_revenue_per_transaction": float(df["Revenue"].mean()),

        # best-selling product (if there is a "Product" column)
        "top_product": df["Product"].value_counts().idxmax(),

        # total quantity sold (if there is a "Quantity" column)
        "total_quantity_sold": int(df["Quantity"].sum()) if "Quantity" in df.columns else None
    }

  
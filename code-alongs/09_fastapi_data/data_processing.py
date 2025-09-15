import pandas as pd 
from constatns import DATA_PATH
from pprint import pprint

df = pd.read_csv(DATA_PATH / "Sales.csv")

class DataExplorer:
    def __init__(self):
        self._df = df.head()

    @property
    def df(self):
        return self._df
    
    def kpis(self, country):
        """Filter out kpis based on country"""
        df_by_country = self._df.query("Country.str.casefold() == @country.casefold()")
        return {
            "total_profit": df_by_country["Profit"].sum()
        }
    
    
    def json_response(self):
        json_data = self._df.to_json(orient= "records")
        return json_data

if __name__ == "__main__":
    data_exporer = DataExplorer()

    pprint(data_exporer.json_response())
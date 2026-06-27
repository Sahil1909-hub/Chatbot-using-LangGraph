from langchain_core.tools import tool
import requests

@tool
def predict_stock_price(symbol: str):

    """
    Fetch latest stock price.
    """

    url = (
        f"https://www.alphavantage.co/query"
        f"?function=GLOBAL_QUOTE"
        f"&symbol={symbol}"
        f"&apikey=YOUR_API_KEY"
    )

    response = requests.get(url)

    return response.json()
import yfinance as yf

from utils.database import get_all_stocks


def get_current_price(ticker):
    stock = yf.Ticker(ticker)

    data = stock.history(period="1d")

    if data.empty:
        return None

    return round(data["Close"].iloc[-1], 2)


def calculate_portfolio():

    stocks = get_all_stocks()

    portfolio = []

    total_investment = 0
    total_current_value = 0

    for stock in stocks:

        current_price = get_current_price(stock["ticker"])

        if current_price is None:
            continue

        investment = stock["shares"] * stock["buy_price"]

        current_value = stock["shares"] * current_price

        profit = current_value - investment

        portfolio.append({

            "id": stock["id"],
            "ticker": stock["ticker"],
            "shares": stock["shares"],
            "buy_price": stock["buy_price"],

            "current_price": current_price,

            "current_value": round(current_value,2),

            "profit": round(profit,2)

        })

        total_investment += investment
        total_current_value += current_value

    total_profit = total_current_value - total_investment

    if total_investment == 0:
        total_return = 0
    else:
        total_return = round(
            (total_profit / total_investment) * 100,
            2
        )

    return {

    "stocks": portfolio,

    "invested_amount": round(total_investment,2),

    "current_value": round(total_current_value,2),

    "gain": round(total_profit,2),

    "return_percent": total_return
}
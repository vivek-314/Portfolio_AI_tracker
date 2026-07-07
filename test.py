from utils.ai import analyze_portfolio

stocks = [
    {"ticker":"AAPL","shares":10},
    {"ticker":"NVDA","shares":34}
]

print(analyze_portfolio(stocks))
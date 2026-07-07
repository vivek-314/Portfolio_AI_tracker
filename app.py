from flask import Flask, render_template, request , redirect
from utils.finance import calculate_portfolio
from utils.ai import analyze_portfolio
from utils.database import (
    initialize_database,
    add_stock,
    get_all_stocks,
    delete_stock
)



app = Flask(__name__)

@app.route("/")
def home():
    portfolio = calculate_portfolio()

    return render_template("index.html",stocks=portfolio["stocks"],portfolio=portfolio)

@app.route("/add", methods=["POST"])
def add():

    ticker = request.form["ticker"].upper()
    shares = int(request.form["shares"])
    buy_price = float(request.form["buy_price"])

    add_stock(ticker, shares, buy_price)

    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):

    delete_stock(id)

    return redirect("/")

@app.route("/analyze")
def analyze():

    portfolio = calculate_portfolio()

    report = analyze_portfolio(portfolio["stocks"])

    return render_template(
        "analysis.html",
        report=report
    )


if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)


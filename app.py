import streamlit as st
import yfinance as yf
import pandas as pd

st.title("📈 Stock Portfolio Tracker")

portfolio = []

st.header("Add Stock")

stock_name = st.text_input("Enter Stock Symbol")

quantity = st.number_input("Quantity", min_value=1)

buy_price = st.number_input("Buy Price", min_value=0.0)

if st.button("Add Stock"):

    stock = yf.Ticker(stock_name)

    data = stock.history(period="1d")

    if not data.empty:

        current_price = data['Close'].iloc[-1]

        investment = quantity * buy_price

        current_value = quantity * current_price

        profit_loss = current_value - investment

        portfolio.append({
            "Stock": stock_name,
            "Quantity": quantity,
            "Buy Price": buy_price,
            "Current Price": round(current_price, 2),
            "Profit/Loss": round(profit_loss, 2)
        })

        df = pd.DataFrame(portfolio)

        st.subheader("📊 Portfolio Summary")

        st.dataframe(df)

    else:
        st.error("Invalid Stock Symbol")
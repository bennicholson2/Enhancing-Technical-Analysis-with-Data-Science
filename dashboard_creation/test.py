import dash
from dash import dcc, html
import plotly.express as px

# Initialize the Dash app
app = dash.Dash(__name__)

import yfinance as yf
import pandas as pd

# Fetch stock data for Apple (AAPL)
stock_data = yf.download('AAPL', start='2020-01-01', end='2023-01-01')

# Sample data for plot
fig = px.line(stock_data, x=stock_data.index, y="Close", title="AAPL Stock Price")

# Define the layout
app.layout = html.Div([
html.H1("AAPL Stock Dashboard"),
dcc.Graph(figure=fig)
])

app.layout = html.Div([
html.H1("AAPL Stock Dashboard"),
dcc.DatePickerRange(id='date-picker',
start_date='2020-01-01',
end_date='2023-01-01'),
dcc.Graph(id='stock-graph')
])

@app.callback(
dash.dependencies.Output('stock-graph', 'figure'),
[dash.dependencies.Input('date-picker', 'start_date'),
dash.dependencies.Input('date-picker', 'end_date')]
)
def update_graph(start_date, end_date):
    filtered_data = stock_data.loc[start_date:end_date]
    return px.line(filtered_data, x=filtered_data.index, y="Close", title="AAPL Stock Price")

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)


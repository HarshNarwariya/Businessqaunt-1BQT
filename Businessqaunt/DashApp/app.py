from dash import Dash, dcc, html, dash_table
from dash.dependencies import Output, Input
import plotly.graph_objects as go
import pandas as pd

data_path = "../Data/Results/1. AssignmentBusinessQuant.csv"
data = pd.read_csv(data_path)
checkbox_options = data.Item.unique()

app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.Div([
            html.P(children="Items"),
            dcc.Checklist(
                id="pick-item",
                value=["Brocolli"],
                className="pick-item",
            ),
        ], className="check-list-container"),
        html.Div([
            # dcc.Graph(id="data-table"),
            dash_table.DataTable(
                id="data-table",
            ),
        ], className="table-container"),
    ], className="container"),
])

@app.callback(
    Output(component_id="data-table", component_property="data"),
    Output(component_id="data-table", component_property="columns"),
    Output(component_id="pick-item", component_property="options"),
    [Input(component_id="pick-item", component_property="value")]
)
def update_graph(option_chosen):
    options = [{"label": "Select all", "value": "Select all", "disabled": False}]
    if "Select all" in option_chosen:
        options += [
            {"label": label, "value": label, "disabled": True}
            for label in checkbox_options
        ]
        df = data
    else:
        df = data[data['Item'].isin(option_chosen)]
        options += [
            {"label": label, "value": label, "disabled": False}
            for label in checkbox_options
        ]
    columns = [{"name": i, "id": i} for i in df.columns]
    return df.to_dict("records"), columns, options

if __name__ == "__main__":
    app.run_server()

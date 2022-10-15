import os
import pathlib

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table
import plotly.graph_objs as go
import dash_daq as daq

import pandas as pd
import plotly.express as px
from IPython.display import display


app = dash.Dash(__name__)
app.title = "F1 analyze"
server = app.server

circuits = pd.read_csv('data/circuits.csv')
constructor_results = pd.read_csv('data/constructor_results.csv')
constructor_standings = pd.read_csv('data/constructor_standings.csv')
constructors = pd.read_csv('data/constructors.csv')
drivers = pd.read_csv('data/drivers.csv')
lap_times = pd.read_csv('data/lap_times.csv')
pit_stops = pd.read_csv('data/pit_stops.csv')
qualifying = pd.read_csv('data/qualifying.csv')
races = pd.read_csv('data/races.csv')
seasons = pd.read_csv('data/seasons.csv')
sprint_results = pd.read_csv('data/sprint_results.csv')
status = pd.read_csv('data/status.csv')


df1 = drivers[drivers.columns[1:2]]
dictionary = df1.to_dict()
dict = dictionary['driverRef']
zxc = [{'label': x, 'value': y} for x,y in dict.items()]
driver_list = zxc


def build_banner():
    return html.Div(
            id="banner",
            className="banner",
            children=[
                html.Div(
                    id="banner-text",
                    children=[
                        html.H4("F1 analysis"),
                        html.H5("F1 analysis but smaller"),
                    ],
                ),
                html.Div(
                    id="banner-logo",
                    children=[
                        html.Button(id="about-dashboard-button", children="ABOUT DASHBOARD", n_clicks=0
                                    ),
                    ],
                ),
            ],
    )


def build_tabs():
    return html.Div(
        id="tabs",
        className="tabs",
        children=[
            dcc.Tabs(
                id="app-tabs",
                value="tab2",
                className="custom-tabs",
                children=[
                    dcc.Tab(
                        id="Specs-tab",
                        label="Constructor stats",
                        value="tab1",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    dcc.Tab(
                        id="Control-chart-tab",
                        label="Drivers stats",
                        value="tab2",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                ],
            )
        ],
    )

# func to generate info about dashboard


def generate_modal():
    return html.Div(
        id="markdown",
        className="modal",
        children=(
            html.Div(
                id="markdown-container",
                children=[
                    html.Div(
                        className="close-container",
                        children=html.Button(
                            "Close",
                            id="markdown_close",
                            n_clicks=0,
                            className="closeButton"
                        ),
                    ),
                    html.Div(
                        className="markdown-text",
                        children=dcc.Markdown(
                            children=("Here you will find more info about this dashboard. Soon...")
                            )
                        ),
                    ],
                )
            ),
        )


def build_quick_stats_panel():
    return html.Div(
        id="quick-stats",
        className="row",
        children=[
            html.Div(
                id="card-1",
                children=[
                    html.P("Horizontal barchart with GP/Driver")
                ],
            ),
        ],
    )


def build_drivers_status_panel():
    # as build_quick_stats_panel
    pass


def build_constructor_stats():
    # as build_tab_1
    pass


def build_driver_stats():
    # as build_tab_2 constructed in app-content callback
    return (
        html.Div(
            id="status-container",
            children=[
                build_drivers_status_panel(),
                html.Div(
                    id="graphs-container",
                    children=[build_top_panel(), build_bubble_chart_panel()],
                ),
            ],
        ),
    )


def generate_section_banner(title):
    return html.Div(className="section-banner", children=title)


def build_top_panel():
    return html.Div(
        id="top-section-container",
        className="row",
        children=[
            # Metrics summary
            html.Div(
                id="metric-summary-session",
                className="eight columns",
                children=[
                    generate_section_banner("Positions gained"),
                    html.Div(
                        id="metric-div",
                        children=[
                            html.Div(
                                id="metric-rows",
                                children=[html.H6("Position vs grid")],
                            ),
                        ],
                    ),
                ],
            ),
            # Violinplot
            html.Div(
                id="pitstops-violin-outer",
                className="four columns",
                children=[
                    generate_section_banner("Pitstops time"),
                    generate_violin_plot(),
                ],
            ),
        ],
    )


# ======================== Setting the margins
# layout = go.Layout(
#     margin=go.layout.Margin(
#         l=40,  # left margin
#         r=40,  # right margin
#         b=10,  # bottom margin
#         t=35  # top margin
#     )
# )


def generate_violin_plot():
    layout = html.Div(
        children=[
            dcc.Dropdown(id="pitstops_dropdown", options=driver_list)],
    )

    fig = dcc.Graph(id="violinplot", figure=go.Figure(layout=layout).add_trace(go.Violin(x=pit_stops['driverId'], y=pit_stops['duration'])).update_layout())
    return fig


def build_bubble_chart_panel():
    pass
    #     html.Div(
    #     id="control-chart-container",
    #     className="twelve columns",
    #     children=[
    #         generate_section_banner("Drivers with most won GP"),
    #         dcc.Graph(
    #             id="control-chart-live",
    #             figure=go.Figure(
    #                 {
    #                     "data": [constructor_results['constructorId']
    #                     ],
    #                     "layout": {
    #                         "paper_bgcolor": "rgba(0,0,0,0)",
    #                         "plot_bgcolor": "rgba(0,0,0,0)",
    #                         "xaxis": dict(
    #                             showline=False, showgrid=False, zeroline=False
    #                         ),
    #                         "yaxis": dict(
    #                             showgrid=False, showline=False, zeroline=False
    #                         ),
    #                         "autosize": True,
    #                     },
    #                 }
    #             ),
    #         ),
    #     ],
    # )


# ====================== Layout section ======================

app.layout = html.Div(
    id="big-app-container",
    children=[
        build_banner(),
        html.Div(
            id="app-container",
            children=[
                build_tabs(),
                # Main app
                html.Div(id="app-content"),
            ],
        ),
        # dcc.Store(id="value-setter-store", data=init_value_setter_store()),
        # dcc.Store(id="n-interval-stage", data=50),
        generate_modal(),
    ],
)


# ====================== Callbacks section ======================

# callback for about-dashboard button

@app.callback(
    Output("markdown", "style"),
    [Input("about-dashboard-button", "n_clicks"), Input("markdown_close", "n_clicks")],
)
def update_click_output(button_click, close_click):
    ctx = dash.callback_context

    if ctx.triggered:
        prop_id = ctx.triggered[0]["prop_id"].split(".")[0]
        if prop_id == "about-dashboard-button":
            return {"display": "block"}

    return {"display": "none"}


# Content callback
@app.callback(
    [Output("app-content", "children")],
    [Input("app-tabs", "value")],
)
def render_tab_content(tab_switch):
    if tab_switch == "tab1":
        return build_constructor_stats()
    return build_driver_stats()


# Running the server
if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
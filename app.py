from datetime import datetime
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import dash_daq as daq
import plotly.express as px
import numpy as np


# load datasets

constructors = pd.read_csv('data/constructors.csv')
drivers = pd.read_csv('data/drivers.csv')
races = pd.read_csv('data/races.csv')
results = pd.read_csv('data/results.csv')

# merge datasets
df = pd.merge(results, races[['raceId', 'year', 'name', 'round']], on='raceId', how='left')
df = pd.merge(df, drivers[['driverId', 'driverRef', 'nationality']], on='driverId', how='left')
df = pd.merge(df, constructors[['constructorId', 'name', 'nationality']], on='constructorId', how='left')

# drop columns
df.drop(['number', 'position', 'positionText', 'laps', 'fastestLap', 'statusId', 'resultId', 'raceId', 'driverId', 'constructorId'], axis=1, inplace=True)

# rename columns
df = df.rename(columns={'rank': 'fastest_lap_rank', 'name_x': 'gp_name',
                    'nationality_x': 'driver_nationality', 'name_y': 'constructor_name', 'nationality_y': 'constructor_nationality',
                   'fastestLapTime': 'fastest_lap_time', 'fastestLapSpeed': 'fastest_lap_speed', 'driverRef': 'driver', 'positionOrder': 'position_order'})

# rearrange columns
df = df[['year', 'gp_name', 'round', 'driver', 'constructor_name', 'grid', 'position_order', 'points', 'time', 'milliseconds', 'fastest_lap_rank', 'fastest_lap_time', 'fastest_lap_speed', 'driver_nationality', 'constructor_nationality']]

# drop 2019 and results newer than 2000
df = df[df['year'] >= 2000]

# sort values
df = df.sort_values(by=['year', 'round', 'position_order'], ascending=[False, True, True])

# replace \N values in time col
df.time.replace('\\N', np.nan, inplace=True)
df.milliseconds.replace('\\N', np.nan, inplace=True)
df.fastest_lap_time.replace('\\N', np.nan, inplace=True)
df.fastest_lap_speed.replace('\\N', np.nan, inplace=True)
df.fastest_lap_rank.replace('\\N', np.nan, inplace=True)

# change datatypes
df.fastest_lap_speed = df.fastest_lap_speed.astype(float)
df.fastest_lap_rank = df.fastest_lap_rank.astype(float)
df.milliseconds = df.milliseconds.astype(float)

# format string values
df.gp_name = df.gp_name.apply(lambda x: x.title().replace("_", " "))
df.driver = df.driver.apply(lambda x: x.title().replace("_", " "))
df.constructor_name = df.constructor_name.apply(lambda x: x.title().replace("_", " "))
df.constructor_nationality = df.constructor_nationality.apply(lambda x: x.title().replace("_", " "))
df.driver_nationality = df.driver_nationality.apply(lambda x: x.title().replace("_", " "))

constructors_colors = {'Ferrari': '#DC0000', 'Mercedes': '#00D2BE', 'Haas F1 Team': '#FFFFFF', 'Alfa Romeo': '#900000', 'Alpine F1 Team': '#0090FF',
 'Alphatauri': '#2B4562', 'Aston Martin': '#006F62', 'Williams': '#005AFF', 'Mclaren': '#FF8700', 'Red Bull': '#0600EF',
 'Racing Point': '#F596C8', 'Renault': '#FFF500', 'Toro Rosso': '#E60F46', 'Force India': '#ff5f0f', 'Sauber': '#006eff',
 'Manor Marussia': '#323232', 'Lotus F1': '#86995B', 'Marussia': '#6E0000', 'Caterham': '#005030', 'Hrt': '#A6904F', 'Lotus': '#FFB800', 'Virgin': '#cc0000',
 'Brawn': '#B8FD6E', 'Toyota': '#cc242c', 'Bmw Sauber': '#1a32d7',  'Super Aguri': '#bb7174', 'Honda': '#49b7a9', 'Spyker': '#f29153', 'Mf1': '#a2abb2',
 'Spyker Mf1': '#f94f41', 'Bar': '#49b7a9', 'Jordan': '#ebc432', 'Minardi': '#feff59', 'Jaguar': '#436e5b', 'Arrows': '#febb62', 'Prost': '#04086a',
 'Benetton': '#00b2ec'}

df['constructor_colors'] = df['constructor_name'].map(constructors_colors)

# reset index
df.reset_index(drop=True, inplace=True)


app = Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
app.title = "F1 analyze"
server = app.server



app_color = {"graph_bg": "#061E44", "graph_line": "#007ACE", "graph_text": "#FFFFFF", "graph_colors": px.colors.qualitative.Vivid, "constructors_colors": constructors_colors}



app.layout = html.Div(
    [
        # header
        html.Div(
            [
                html.Div(
                    [
                        html.Img(src="assets/logo.png", width="300px", height="200px", className="app_header_title"),
                        html.H2("seasons 2000-2022 analysis", className="app_header_paragraph"),
                    ],
                ),
                html.Div(
                    [
                        html.Div(
                            [html.H3("Time to next race", className="graph_title", style={"textAlign": "center"}), html.Br()]
                        ),
                        html.Div(
                            [
                                daq.LEDDisplay(
                                    id='my-LED-display',
                                    label="DAYS:HOURS:MINUTES:SECONDS",
                                    labelPosition="bottom",
                                    value=0,
                                    backgroundColor="#061E44"
                                ),
                                dcc.Interval(
                                    id="update_timer",
                                    interval=1000,
                                    n_intervals=0
                                )
                            ]
                        )
                    ],
                )

            ],
            className="app_header_desc"
        ),
        html.Div(
            [
                html.Div(
                    [html.H3("Constructor wins and their teams", className="graph_title")]
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                dcc.Graph(
                                id="constructor_wins_graph"
                                ),
                            ],
                            id = "constructor_wins_bar"

                        ),
                        html.Div(
                            [
                                dcc.Graph(
                                id="sun"
                                ),
                            ],
                            id="team_sunburst_graph"
                        ),
                    ],
                    className="graph_container_flex_top"
                ),
                html.Div(
                    [
                        dcc.Slider(
                            min=df["year"].min(),
                            max=df["year"].max(),
                            step=1,
                            id="constructor_wins_slider",
                            value=df["year"].min(),
                            marks=None,
                            tooltip={"placement": "bottom", "always_visible": True}
                        ),
                    ],
                    id="slider_container"
                )
            ],
            className="graph_container_top"
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [html.H3("Speed on GP", className="graph_title")]
                        ),
                        html.Div(
                            [
                                dcc.Graph(
                                    id="gp_speed_line"
                                ),
                            ]
                        ),
                        html.Div(
                            [
                                dcc.Dropdown(
                                    options=df['gp_name'].unique(),
                                    id='gp_speed_dropdown',
                                    multi=True,
                                    value=["Monaco Grand Prix", "Spanish Grand Prix"],
                                )
                            ]
                        ),
                    ],
                ),
            ],
            className="graph_container bottom"
        ),
    ],
    className="app_container"
)


# =============================== Callbacks ===============================

# Constructor wins callback
@app.callback(
    Output("constructor_wins_graph", "figure"),
    Input("constructor_wins_slider", "value"))
def update_bar_chart(year):
    data = df.loc[df['position_order'] == 1]
    mask = data["year"] == year
    fig = px.bar(data[mask], x="position_order", y="constructor_name",  orientation='h', labels={'position_order': "Number of GP wins", 'constructor_name': "Constructor name"},
                 color='constructor_name', color_discrete_map=constructors_colors)
    fig.update_layout(
        plot_bgcolor=app_color["graph_bg"],
        paper_bgcolor=app_color["graph_bg"],
        font_color=app_color["graph_text"],
        showlegend=False,
        hovermode=False,
        yaxis={'categoryorder': 'total ascending'}
    )

    return fig


# GP Speed callback
@app.callback(
    Output("gp_speed_line", "figure"),
    Input("gp_speed_dropdown", "value"))
def update_line(gp):
    df_speed = df.groupby(['gp_name', 'year'])['fastest_lap_speed'].mean().to_frame().reset_index()
    mask = df_speed.gp_name.isin(gp)
    fig = px.line(df_speed[mask], x='year', y="fastest_lap_speed", labels={'year': "Year", 'fastest_lap_speed': "Fastest Lap Speed (kmh)"}, color='gp_name',
                  color_discrete_map=constructors_colors)
    fig.update_layout(
        plot_bgcolor=app_color["graph_bg"],
        paper_bgcolor=app_color["graph_bg"],
        font_color=app_color["graph_text"],
        xaxis=dict(showgrid=False),
        showlegend=False,
        hoverlabel=dict(
            font_size=16,
            font_color=app_color['graph_text']
        )
    )
    fig.update_traces(mode='markers+lines', marker=dict(size=10))
    return fig


# Team-constructor callback
@app.callback(
    Output("sun", "figure"),
    Input("constructor_wins_slider", "value"))
def update_sunburst(year):
    mask = df['year'] == year
    fig = px.sunburst(df[mask], path=['constructor_name', 'driver'], values="points", color='constructor_name', color_discrete_map=constructors_colors)
    fig.update_layout(
        plot_bgcolor=app_color["graph_bg"],
        paper_bgcolor=app_color["graph_bg"],
        font_color=app_color["graph_text"],
        margin=dict(t=0, l=0, r=0, b=0)
    )
    return fig


# LED callback
@app.callback(
    Output("my-LED-display", "value"),
    Input("update_timer", "n_intervals"))
def update_timer(value):
    now = datetime.now()
    gp_time = datetime(2023, 3, 5, 16, 0, 0)
    diff = gp_time-now
    days = diff.days
    hours = diff.seconds // 3600
    totalHours, minutes = divmod(diff.seconds, 3600)
    totalMinutes, seconds = divmod(diff.seconds, 60)

    return f"{days}:{hours}:{minutes//60}:{seconds}"



if __name__ == "__main__":
    #app.run_server(debug=True)
    app.run(host='0.0.0.0')

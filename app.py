import os
import json
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_colorscales as dcs
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from data import create_mesh_data, toggle_mesh_data


app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

server = app.server

GITHUB_LINK = os.environ.get(
    "GITHUB_LINK",
    "https://github.com/plotly/dash-sample-apps/tree/master/apps/dash-brain-viewer",
)


plot_layout = {
    "title": "",
    "margin": {"t": 0, "b": 100, "l": 20, "r": 20},
    "font": {"size": 12, "color": "white"},
    "showlegend": False,
    "plot_bgcolor": "#141414",
    "paper_bgcolor": "#141414",
    "scene": {
        "xaxis":  {
            "title" : '',
            "tickmode" : 'array',
            "tickvals" : [0, 1, 2, 3],
            "ticktext" : ['Government','Industry','Professional',''],
            },
        "yaxis":  {
            "title" : '',
            "tickmode" : 'array',
            "tickvals" : [0, 1, 2, 3,4,5,6,7],
            "ticktext" : ['Mobility','Cohesion','Deomcracy','Health','Employment','Housing',''],
            },
        "zaxis":  {
            "title" : '',
            "tickmode" : 'array',
            "tickvals" : [0, 1, 2, 3, 4, 5, 6, 7],
            "ticktext" : ['', 'Privacy','Content','Transparency','Bias','Accountability','Safety'],
            } ,
        "aspectratio": {"x": 1, "y": 1.2, "z": 1},
        "camera": {"eye": {"x": 1.25, "y": 1.25, "z": 1.25}},
        "annotations": [],
        #TODO turn off auto hover annotations
    },
}

app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H2("Ethics Cube"),
                                    ],
                                    className="header__title",
                                ),
                                html.Div(
                                    [
                                       html.H5("This is an example demo for the interactive ethics cube")
                                    ],
                                    className="header__info pb-20",
                                ),
                                html.Div(
                                    [
                                       #Add github link here
                                    ],
                                    className="header__button",
                                ),
                            ],
                            className="header pb-20",
                        ),
                        html.Div(
                            [
                                dcc.Graph(
                                    id="cube-graph",
                                    figure={
                                        "data": create_mesh_data("main"),
                                        "layout": plot_layout,
                                    },
                                    config={"editable": True, "scrollZoom": False},
                                )
                            ],
                            className="graph__container",
                        ),
                    ],
                    className="container",
                )
            ],
            className="two-thirds column app__left__section",
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                
                            ]
                        )
                    ],
                    className="colorscale pb-20",
                ),
                html.Div(
                    [
                        html.P("Select View Option", className="subheader"),
                        dcc.RadioItems(
                            options=[
                                {"label": "Solutions", "value": "main"},
                                {"label": "Risks", "value": "view1"},
                                {"label": "Opportunities", "value": "view2"},
                            ],
                            value="main",
                            id="radio-options",
                            labelClassName="label__option",
                            inputClassName="input__option",
                        ),
                    ],
                    className="pb-20",
                ),
                html.Div(
                   #Add click data here
                ),
                html.Div(
                    #add relayout data here
                ),
                html.Div(
                    [
                        html.A(
                                            "Code developed using the example Dash App Repositiory on Github",
                                            href=GITHUB_LINK,
                                            target="_blank",
                                )
                    ]
                ),
            ],
            className="one-third column app__right__section",
        ),
        dcc.Store(id="annotation_storage"),
    ]
)


@app.callback(
    Output("cube-graph", "figure"),
    [
        Input("cube-graph", "clickData"),
        Input("radio-options", "value"),
    ],
    [State("cube-graph", "figure")],
)



def cube_graph_handler(click_data, val,figure):

    if figure["data"][0]["name"] != val:
        figure["data"] = create_mesh_data(val)
        figure["layout"] = plot_layout
        return figure

  
    if click_data is not None and "points" in click_data:
        #TODO Develop interactive functionlity for clicking and toggling individual cube visibility
        y_value = click_data["points"][0]["y"]
        x_value = click_data["points"][0]["x"]
        z_value = click_data["points"][0]["z"]

    

        


        
    return figure






if __name__ == "__main__":
    app.run_server(debug=True)
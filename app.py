import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# Create the Dash application
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#Styling sidebar
SIDEBAR_STYLE= {
    "position": "fixed",
    "top":0,
    "left":0,
    "bottom":0,
    "width": "12rem",
    "padding":"2rem 1rem",
    "background-color": "#F8F9FA",
}
# location of tab information
CONTENT_STYLE = {
    "margin-left": "16rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",}
# Create the Sidebar
sidebar = html.Div(
    [
        html.H2("PfH", className="display-1"),
        html.Hr(),
        html.P ('Home Page'),
        dbc.Nav([
                dbc.NavLink("Background", href="/", active = "exact"),
        ],
            vertical = True,
            pills = True
        ),
        html.Hr(),
        html.P(
            'Partners for Healing', className='lead'
        ),
        dbc.Nav(
            [
                dbc.NavLink("Clinic Usage", href="/clinic_usage", active = "exact"),
                dbc.NavLink("Demographics", href="/demographics", active="exact"),
                dbc.NavLink("Conditions", href="/conditions", active="exact"),
            ],
            vertical = True,
            pills = True,
        ),
        html.Hr(),
        html.P('County', className='lead'),
        dbc.Nav(
            [
                dbc.NavLink("Eligibility", href="/county", active = "exact"),
            ],
            vertical = True,
            pills = True,
        ),
        html.Hr(),
        html.P('Hospital Insights', className='lead'),
        dbc.Nav(
            [
                dbc.NavLink("ER Usage", href="/ER", active = "exact"),
                dbc.NavLink("Rural vs Urban", href="/rural_urban", active="exact"),
                dbc.NavLink("Test 8", href="/test-8", active="exact"),
            ],
            vertical = True,
            pills = True,
        ),
    ],
    style= SIDEBAR_STYLE,
)
content = html.Div(id="page-content", children =[], style=CONTENT_STYLE)
# Define the layout
app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content ])
@app.callback(
    Output("page-content", "children"),
    [Input("url","pathname")]
    )
def render_page_content(pathname):
    if pathname == "/":
        return [
            html.H1('Bridging The Health Care Coverage Gap',
                   style={'textAlign':'center'}),
            html.P("Problem Statement")
                ]
    elif pathname == "/clinic_usage":
        return [
            html.H1("PfH Clinic Usage Throughout Years",
                   style={'textAlign':'center'}),
            ## use dcc.Graph(id='bargraph', then put the code in )
            dcc.Graph(id='bargraph',
                      figure = px.bar(filtered_counties, x='county', y='percent uninsured',
                                hover_data=['population'], title='Uninsured Status')
                     )]
    elif pathname == "/demographics":
        return [
            html.H1("PfH Clinic Demographics",
                   style={'textAlign':'center'})
            #dcc.Graph(id='bargraph',
                      #figure = px.bar(filtered_counties, x='county', y='percent uninsured',
                                #hover_data=['population'], title='Uninsured Status')
                     #)
                        ]
    elif pathname == "/conditions":
        return [
            html.H1("Patient Conditions",
                   style={'textAlign':'center'}),
            dcc.Graph(id='bargraph',
                      figure = px.bar(filtered_counties, x='county', y='percent uninsured',
                             hover_data=['population'], title='Uninsured Status')
                     )
                        ]
    elif pathname == "/county":
        return [
            html.H1("Population of Eligible Patients in Local Counties",
                   style={'textAlign':'center'})
            #dcc.Graph(id='bargraph',
                     #add graph code
                        ]
    elif pathname == "/ER":
        return [
            html.H1("Preventable ER Visits",
                   style={'textAlign':'center'})
            #dcc.Graph(id='bargraph',
                     #add graph code
                        ]
    elif pathname == "/rural_urban":
        return [
            html.H1("Rural vs Urban Healthcare",
                   style={'textAlign':'center'})
           #dcc.Graph(id='bargraph',
                     #add graph code
                        ]
# Define callbacks to update the content based on the selected sub-tabs
# Run the application
if __name__=='__main__':
    app.run_server(debug=True, port=8000)
#http://127.0.0.1:8000/county
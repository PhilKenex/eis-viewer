import dash
from dash import dcc, html, dash_table
from dash.dependencies import Output, Input, State

external_stylesheets = ['https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css',
                        'https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap',
                        'https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;700&display=swap']
                        
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.title = 'EIS Viewer'

app.layout = html.Div([
    # Header section with logo and main title
    html.Div([
        html.A([
            html.Img(src='/assets/logo_white.svg', style={'maxHeight': '100px'})  # Adjust the size as needed
        ], href='http://www.kenex.co.nz', target='_blank'),
        html.H1('EIS Target Management Dashboard', style={'margin': '0 10%'})  # Adjust margin as needed
    ], style={'display': 'flex', 'alignItems': 'center', 'justifyContent': 'space-between', 'padding': '20px'}),

   html.Div([
    html.P([
        "As part of Kenex’s Mineral Potential Mapping service, we have developed a dashboard to help better visualise and assess the resulting targets. Below is an example of the dashboard built using targets developed from the ",
        html.A("Eastern Lachlan Orogen Mineral Potential Data Package", href="https://search.geoscience.nsw.gov.au/product/9253"),
        "."
    ]),
    html.Div([
        html.P("To use the dashboard, you can toggle layers on and off using this button", style={'display': 'inline-block', 'margin': '0', 'verticalAlign': 'middle'}),
        html.Img(src='/assets/layers.png', style={'height': '40px', 'width': 'auto', 'verticalAlign': 'middle', 'marginLeft': '10px'})
    ],),
    html.P([
        "The tables at the bottom of the dashboard are linked to the corresponding layers:",
    html.Ul([
        html.Li([html.Strong("All Targets – "), "All targets defined within the study area."]),
        html.Li([html.Strong("Undrilled Targets – "), "All targets that don’t have any drillholes inside them. Assessing the rank and location of these targets could guide the location of the next drill program."]),
        html.Li([html.Strong("Untested Targets – "), "All targets that don’t have any drilling, rock chip sampling, soil and stream sediment sampling inside them. Assessing these targets could guide the next sampling program."]),
        html.Li([html.Strong("Free Targets – "), "Targets that are not currently held within a tenement, as of 03/07/2023. These targets could be an opportunity to apply for a new exploration area."])
    ], style={'textAlign': 'left', 'paddingLeft': '20px'}) 
    ])
    ], style={
        'padding-top': '20px',
        'padding-bottom': '20px',
        'width': '50%',
        'margin': '15px auto',
        'fontSize': '18px',
        'color': 'white',
        'fontFamily': 'Roboto, sans-serif',
        'textAlign': 'center'
    }),

    # Section for embedding the ArcGIS dashboard within an iframe
    html.Div([
        html.Iframe(
            src="https://www.arcgis.com/apps/dashboards/b3bb082de0e64c84a1cec9be182b9707",
            style={"height": "calc(100vh - 120px)", "width": "100%"}  # Adjusting for header height
        )
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
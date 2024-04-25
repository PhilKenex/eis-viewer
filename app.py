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
        html.H1('EIS Target Management Dashboard', style={'margin': '0 20px'})  # Adjust margin as needed
    ], style={'display': 'flex', 'alignItems': 'center', 'justifyContent': 'space-between', 'padding': '10px'}),

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

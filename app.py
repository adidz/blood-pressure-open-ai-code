import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the dataset from the provided link
data_url = 'https://raw.githubusercontent.com/plotly/datasets/master/diabetes-vid.csv'
df = pd.read_csv(data_url)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H1("Diabetes Data Analysis"),
    
    # Dropdown for filtering by 'Outcome' column
    dcc.Dropdown(
        id='outcome-dropdown',
        options=[
            {'label': str(outcome), 'value': outcome}
            for outcome in df['Outcome'].unique()
        ],
        value=df['Outcome'].unique()[0],  # Default value
        multi=False
    ),
    
    # Scatter plot for blood pressure vs BMI
    dcc.Graph(id='scatter-plot'),
])

# Define callback to update the scatter plot based on the selected 'Outcome' value
@app.callback(
    Output('scatter-plot', 'figure'),
    Input('outcome-dropdown', 'value')
)
def update_scatter_plot(selected_outcome):
    # Filter the DataFrame based on the selected 'Outcome' value
    filtered_df = df[df['Outcome'] == selected_outcome]
    
    # Create the scatter plot
    fig = px.scatter(
        filtered_df,
        x='BloodPressure',
        y='BMI',
        color='Age',
        title=f'Scatter Plot - Blood Pressure vs BMI (Outcome: {selected_outcome})'
    )
    
    return fig

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)

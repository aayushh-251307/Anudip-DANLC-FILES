import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output

# Load dataset
file_path = "eci-2024.csv"
df = pd.read_csv(file_path)

# Clean column names
df.columns = df.columns.str.strip()

# Convert "Total Votes" to numeric
df["Total Votes"] = pd.to_numeric(df["Total Votes"], errors="coerce")

# Drop rows with missing votes
df.dropna(subset=["Total Votes"], inplace=True)

# Sort to get the highest voted candidate per seat
df = df.sort_values(["State", "PC No", "Total Votes"], ascending=[True, True, False])

# Get winners for each constituency
winners_df = df.drop_duplicates(subset=["State", "PC No"], keep="first")

# Ensure all states are captured
unique_states = sorted(df["State"].dropna().unique())

# Initialize Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div(style={'backgroundColor': '#f4f4f4', 'padding': '20px'}, children=[
    html.H1("Lok Sabha Elections 2024 - Data Visualization", style={'text-align': 'center', 'color': '#333'}),

    # Dropdowns (Same as before)
    html.Div([
        html.Label("Select a State:", style={'font-weight': 'bold'}),
        dcc.Dropdown(
            id="state-dropdown",
            options=[{"label": state, "value": state} for state in unique_states],
            placeholder="Select State",
            clearable=True
        ),

        html.Label("Select a Constituency:", style={'font-weight': 'bold'}),
        dcc.Dropdown(
            id="seat-dropdown",
            placeholder="Select Constituency",
            clearable=True
        ),
    ], style={'text-align': 'center', 'margin-bottom': '20px'}),

    # Pie charts side by side
    html.Div([
        dcc.Graph(id="state-pie-chart", style={'width': '48%', 'display': 'inline-block'}),
        dcc.Graph(id="seat-pie-chart", style={'width': '48%', 'display': 'inline-block'}),
    ]),

    # Table: State-wise seats won
    html.Div([
        html.H3("Seats Won by Each Party in Selected State",
                style={'text-align': 'center', 'margin-top': '30px', 'color': '#333'}),
        dash_table.DataTable(
            id="state-party-table",
            columns=[
                {"name": "Party", "id": "Party"},
                {"name": "Seats Won", "id": "Seats Won"}
            ],
            style_table={'margin': 'auto', 'width': '60%', 'border': '1px solid black', 'backgroundColor': '#fff'},
            style_header={'fontWeight': 'bold', 'textAlign': 'center', 'backgroundColor': '#007BFF', 'color': 'white'},
            style_cell={'textAlign': 'center', 'padding': '8px', 'border': '1px solid black'},
        ),
    ]),

    # Table: Candidate-wise vote share
    html.Div([
        html.H3("Candidate Votes Breakdown", style={'text-align': 'center', 'margin-top': '30px', 'color': '#333'}),
        dash_table.DataTable(
            id="candidate-table",
            columns=[
                {"name": "S. No", "id": "Sl no"},
                {"name": "Candidate", "id": "Candidate"},
                {"name": "Party", "id": "Party"},
                {"name": "Total Votes", "id": "Total Votes"}
            ],
            style_table={'margin': 'auto', 'width': '80%', 'border': '1px solid black', 'backgroundColor': '#fff'},
            style_header={'fontWeight': 'bold', 'textAlign': 'center', 'backgroundColor': '#007BFF', 'color': 'white'},
            style_cell={'textAlign': 'center', 'padding': '8px', 'border': '1px solid black'},
            page_size=10
        ),
    ]),
])


# Update constituency dropdown based on selected state
@app.callback(
    Output("seat-dropdown", "options"),
    Input("state-dropdown", "value")
)
def update_seat_dropdown(selected_state):
    if selected_state:
        filtered_df = df[df["State"] == selected_state]
        return [{"label": seat, "value": seat} for seat in sorted(filtered_df["PC Name"].unique())]
    return []


# Update state-wise pie chart
@app.callback(
    Output("state-pie-chart", "figure"),
    Input("state-dropdown", "value")
)
def update_state_chart(selected_state):
    if not selected_state:
        return px.pie(title="Select a State to View Party Wins")

    state_data = winners_df[winners_df["State"] == selected_state]
    party_counts = state_data["Party"].value_counts()

    fig = px.pie(
        names=party_counts.index,
        values=party_counts.values,
        title=f"Seats Won by Each Party in {selected_state}",
        hole=0.3
    )

    fig.update_traces(
        textinfo="label+value",
        marker=dict(line=dict(color='black', width=1))
    )

    return fig


# Update seat-wise pie chart
@app.callback(
    Output("seat-pie-chart", "figure"),
    Input("seat-dropdown", "value"),
    Input("state-dropdown", "value")
)
def update_seat_chart(selected_seat, selected_state):
    if not selected_seat or not selected_state:
        return px.pie(title="Select a Constituency to View Vote Share")

    seat_data = df[(df["State"] == selected_state) & (df["PC Name"] == selected_seat)]

    fig = px.pie(
        seat_data,
        names="Candidate",
        values="Total Votes",
        title=f"Vote Share in {selected_seat} ({selected_state})",
        hole=0.3
    )

    fig.update_traces(
        textinfo="label+value",
        marker=dict(line=dict(color='black', width=1))
    )

    return fig


# Update state-wise party table with total seats
@app.callback(
    Output("state-party-table", "data"),
    Input("state-dropdown", "value")
)
def update_state_party_table(selected_state):
    if not selected_state:
        return []

    state_data = winners_df[winners_df["State"] == selected_state]
    party_counts = state_data["Party"].value_counts().reset_index()
    party_counts.columns = ["Party", "Seats Won"]

    total_seats = state_data.shape[0]

    # Append total row
    total_row = pd.DataFrame({"Party": ["Total Seats"], "Seats Won": [total_seats]})
    party_counts = pd.concat([party_counts, total_row], ignore_index=True)

    return party_counts.to_dict("records")


# Update candidate table
@app.callback(
    Output("candidate-table", "data"),
    Input("seat-dropdown", "value"),
    Input("state-dropdown", "value")
)
def update_candidate_table(selected_seat, selected_state):
    if not selected_seat or not selected_state:
        return []

    seat_data = df[(df["State"] == selected_state) & (df["PC Name"] == selected_seat)]

    return seat_data[["Sl no", "Candidate", "Party", "Total Votes"]].to_dict("records")


# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)

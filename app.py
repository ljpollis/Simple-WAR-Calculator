from dash import callback, Dash, dcc, html, Input, Output

app = Dash()

app.config.suppress_callback_exceptions = True

app.layout = [
  html.H1('Simple WAR Calculator'),
  html.Div(children=[
    html.Label('Home Runs'),
    html.Br(),
    dcc.Input(id = 'home-runs', value = '16', type = 'number'),
    html.Br(),
    html.Br(),
    html.Label('Walks'),
    html.Br(),
    dcc.Input(id = 'walks', value = '50', type = 'number'),
    html.Br(),
    html.Br(),
    html.Label('Strikeouts'),
    html.Br(),
    dcc.Input(id = 'strikeouts', value = '75', type = 'number'),
    html.Br(),
    html.Br(),
    html.Label('Stolen Bases'),
    html.Br(),
    dcc.Input(id = 'stolen-bases', value = '8', type = 'number'),
    html.Br(),
    html.Br(),
    html.Label('BABIP'),
    html.Br(),
    dcc.Input(id = 'babip', value = '.300', type = 'number', step = 0.001),
    html.Br(),
    html.Br(),
    html.Label('Plate Appearances'),
    html.Br(),
    dcc.Input(id = 'plate-appearances', value = '600', type = 'number'),
    html.Br(),
    html.Br(),
    html.Label('Games'),
    html.Br(),
    dcc.Input(id = 'games', value = '150', type = 'number'),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Label('Primary Position'),
    dcc.Dropdown(['C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'DH'], 'LF', id = 'position'),
    html.Br(),
    html.Label('Defensive Performance'),
    dcc.Slider(
      id = 'defense',
      min = 20,
      max = 80,
      step = 10,
      value = 50,
        ),
    html.Br(),
    html.Label('Baserunning Performance'),
    dcc.Slider(
      id = 'baserunning', 
      min = 20,
      max = 80,
      step = 10,
      value = 50,
        )
  ]),
  html.Div(children=[
    html.Div(id='xwrc'),
    html.Div(id='batting-runs'),
    html.Div(id='defense-runs'),
    html.Div(id='baserunning-runs'),
    html.Div(id='replacement-runs'),
    html.Div(id='runs-above-replacement'),
    html.Div(id='xwrc-display'),
    html.Br(),
    html.Br(),
    html.Div(id='batting-runs-display'),
    html.Br(),
    html.Br(),
    html.Div(id='defense-runs-display'),
    html.Br(),
    html.Br(),
    html.Div(id='baserunning-runs-display'),
    html.Br(),
    html.Br(),
    html.Div(id='replacement-runs-display'),
    html.Br(),
    html.Br(),
    html.Div(id='runs-above-replacement-display')
  ])
]


## Calculation callbacks

@callback(
    Output(component_id = 'xwrc', component_property = 'data'),
    Input(component_id = 'home-runs', component_property = 'value'),
    Input(component_id = 'walks', component_property = 'value'),
    Input(component_id = 'strikeouts', component_property = 'value'),
    Input(component_id = 'stolen-bases', component_property = 'value'),
    Input(component_id = 'babip', component_property = 'value'),
    Input(component_id = 'plate-appearances', component_property = 'value')
    )
def update_xwrc(hr, bb, k, sb, babip, pa):
    return (1184.34 * float(hr) / float(pa) + 275.21 * float(bb) / float(pa) - 180.52 * float(k) / float(pa) + 422.14 * float(babip) + 151.75 * float(sb) / float(pa) - 51.57)

@callback(
    Output('batting-runs', 'data'),
    Input('xwrc', 'data'),
    Input('plate-appearances', 'value')
    )
def update_batting_runs(xwrc, pa):
    return float(xwrc - 100) * 0.1123 * float(pa) / 100

@callback(
    Output('defense-runs', 'data'),
    Input('defense', 'value'),
    Input('games', 'value')
    )
def update_defense_runs(defense, games):
    return (float(defense) - 50) * float(games) / 150

@callback(
    Output('baserunning-runs', 'data'),
    Input('baserunning', 'value'),
    Input('plate-appearances', 'value')
    )
def update_baserunning_runs(baserunning, pa):
    return (float(baserunning) - 50) / 2 * float(pa) / 600

@callback(
    Output('replacement-runs', 'data'),
    Input('plate-appearances', 'value')
    )
def update_replacement_runs(pa):
    return float(pa) / 30

@callback(
    Output('runs-above-replacement', 'data'),
    Input('batting-runs', 'data'),
    Input('defense-runs', 'data'),
    Input('baserunning-runs', 'data'),
    Input('replacement-runs', 'data')
    )
def update_runs_above_replacement(battingruns, defenseruns, baserunningruns, replacementruns):
    return battingruns + defenseruns + baserunningruns + replacementruns


## Display callbacks

@callback(
    Output(component_id = 'xwrc-display', component_property = 'children'),
    Input(component_id = 'xwrc', component_property = 'data')
    )
def update_xwrc_display(xwrc):
    return f'xwRC+: ' + str(int(xwrc))

@callback(
    Output('batting-runs-display', 'children'),
    Input('batting-runs', 'data')
    )
def update_batting_runs_display(battingruns):
    return f'Batting Runs: ' + str(round(battingruns, 1))

@callback(
    Output('defense-runs-display', 'children'),
    Input('defense-runs', 'data')
    )
def update_defense_runs_display(defenseruns):
    return f'Defensive Runs: ' + str(round(defenseruns, 1))

@callback(
    Output('baserunning-runs-display', 'children'),
    Input('baserunning-runs', 'data')
    )
def update_baserunning_runs_display(baserunningruns):
    return f'Baserunning Runs: ' + str(round(baserunningruns, 1))

@callback(
    Output('replacement-runs-display', 'children'),
    Input('replacement-runs', 'data')
    )
def update_replacement_runs_display(replacementruns):
    return f'Replacement Runs: ' + str(round(replacementruns, 1))

@callback(
    Output('runs-above-replacement-display', 'children'),
    Input('runs-above-replacement', 'data')
    )
def update_replacement_runs_display(runsabovereplacement):
    return f'Runs Above Replacement: ' + str(round(runsabovereplacement, 1))

if __name__ == '__main__':
    app.run(debug=True)


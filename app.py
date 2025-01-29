from dash import callback, Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets = [dbc.themes.BOOTSTRAP])

app.config.suppress_callback_exceptions = True

roundbutton = {
    "border": None,
    "border-radius": "50%",
    "padding": 0,
    "backgroundColor": "blue",
    "color": "white",
    "textAlign": "center",
    "fontSize": 10,
    "height": 20,
    "width": 20,
    "margin": 2,
}

outputs = [
  html.Div(children=[
    html.Div(id='xwrc'),
    html.Div(id='batting-runs'),
    html.Div(id='defense-runs'),
    html.Div(id='baserunning-runs'),
    html.Div(id='positional-runs'),
    html.Div(id='replacement-runs'),
    html.Div(id='runs-above-replacement'),
    html.Div(id='wins-above-replacement'),
    html.H6(id='xwrc-display'),
    html.Br(),
    html.Br(),
    html.H6(id='batting-runs-display'),
    html.Br(),
    html.H6(id='defense-runs-display'),
    html.Br(),
    html.H6(id='baserunning-runs-display'),
    html.Br(),
    html.H6(id='positional-runs-display'),
    html.Br(),
    html.H6(id='replacement-runs-display'),
    html.Br(),
    html.H6(id='runs-above-replacement-display'),
    html.Br(),
    html.Br(),
    html.Br(),
    html.H4(id='wins-above-replacement-display')
    ]
  )
]

nontextselections = [
  html.Label('Primary Position'),
  dcc.Dropdown(['C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'DH'], 'LF', id = 'position'),
  html.Br(),
  html.Label('Defensive Performance'),
  dcc.Slider(
    id = 'defense',
    min = 20,
    max = 80,
    step = 5,
    value = 50
    ),
  html.Br(),
  html.Label('Baserunning Performance'),
  dcc.Slider(
    id = 'baserunning', 
    min = 20,
    max = 80,
    step = 5,
    value = 50
    )
]

home_runs_row = dbc.Row([
  dbc.Col(html.Label('Home Runs:'), width = 4),
  dbc.Col(dcc.Input(id = 'home-runs', value = '16', type = 'number'), width = 1)
])

walks_row = dbc.Row([
  dbc.Col(html.Label('Walks:'), width = 4),
  dbc.Col(dcc.Input(id = 'walks', value = '50', type = 'number'), width = 1)
])

strikeouts_row = dbc.Row([
  dbc.Col(html.Label('Strikeouts:'), width = 4),
  dbc.Col(dcc.Input(id = 'strikeouts', value = '75', type = 'number'), width = 1)
])

stolen_bases_row = dbc.Row([
  dbc.Col(html.Label('Stolen Bases:'), width = 4),
  dbc.Col(dcc.Input(id = 'stolen-bases', value = '8', type = 'number'), width = 1)
])

babip_row = dbc.Row([
  dbc.Col(
    html.Div(
      [
        html.Label('BABIP:'),
        dbc.Button('?', id = 'babip-?',style=roundbutton),
        dbc.Tooltip(
            "Batting Average on Balls in Play: The proportion of batted balls within the field of play that fall for hits. Essentially batting average that doesn't count home runs or strikeouts.",
            target="babip-?")
      ]
    ), width = 4, style={"verticalAlign": "center"}),
  dbc.Col(dcc.Input(id = 'babip', value = '.300', type = 'number', step = 0.001), width = 1)
])

plate_appearances_row = dbc.Row([
  dbc.Col(html.Label('PA:'), width = 4),
  dbc.Col(dcc.Input(id = 'plate-appearances', value = '600', type = 'number'), width = 1)
])

games_row = dbc.Row([
  dbc.Col(html.Label('Games:'), width = 4),
  dbc.Col(dcc.Input(id = 'games', value = '150', type = 'number'), width = 1)
])

park_factor_row = dbc.Row([
  dbc.Col(html.Label('Park Factor:'), width = 4),
  dbc.Col(dcc.Input(id = 'park-factor', value = '100', type = 'number'), width = 1)
])

runs_per_pa_row = dbc.Row([
  dbc.Col(html.Label('League Runs per PA:'), width = 4),
  dbc.Col(dcc.Input(id = 'runs-per-pa', value = '.117', type = 'number', step = 0.001), width = 1)
])

replacement_level_row = dbc.Row([
  dbc.Col(html.Label('Replacement Level (Runs per 600 PA):'), width = 4),
  dbc.Col(dcc.Input(id = 'replacement-level', value = '-20', type = 'number', step = 0.1), width = 1)
])

runs_per_win_row = dbc.Row([
  dbc.Col(html.Label('Runs per Win Conversion:'), width = 4),
  dbc.Col(dcc.Input(id = 'runs-per-win', value = '9.683', type = 'number', step = 0.001), width = 1)
])


app.layout = [
  html.H1('Simple WAR Calculator'),
  html.Br(),
  dbc.Row(
    [
      dbc.Col([
        home_runs_row,
        html.Br(),
        walks_row,
        html.Br(),
        strikeouts_row,
        html.Br(),
        stolen_bases_row,
        html.Br(),
        babip_row,
        html.Br(),
        plate_appearances_row,
        html.Br(),
        games_row,
        html.Br(),
        park_factor_row,
        html.Br(),
        dbc.Row([
          dbc.Col(nontextselections, width = 10)
        ]),
        html.Br(),
        dbc.Button(outline = True, color = 'primary', id = 'toggle-button', n_clicks = 0),
        html.Br(),
        html.Br(),
        html.Div([runs_per_pa_row,
        html.Br(),
        replacement_level_row,
        html.Br(),
        runs_per_win_row], id = 'advanced-selection')
      ], style = {"margin-left": "10px"}, width = 3),
      dbc.Col(outputs, width = 3)
    ], justify = "start"
  )
]


## Calculation callbacks

@callback(
  Output(component_id = 'xwrc', component_property = 'data'),
  Input(component_id = 'home-runs', component_property = 'value'),
  Input(component_id = 'walks', component_property = 'value'),
  Input(component_id = 'strikeouts', component_property = 'value'),
  Input(component_id = 'stolen-bases', component_property = 'value'),
  Input(component_id = 'babip', component_property = 'value'),
  Input(component_id = 'plate-appearances', component_property = 'value'),
  Input(component_id = 'park-factor', component_property = 'value')
  )
def update_xwrc(hr, bb, k, sb, babip, pa, pf):
  return (1184.34 * float(hr) / float(pa) + 275.21 * float(bb) / float(pa) - 180.52 * float(k) / float(pa) + 422.14 * float(babip) + 151.75 * float(sb) / float(pa) - 51.57) * 100 / float(pf)

@callback(
  Output('batting-runs', 'data'),
  Input('xwrc', 'data'),
  Input('plate-appearances', 'value'),
  Input('park-factor', 'value'),
  Input('runs-per-pa', 'value')
  )
def update_batting_runs(xwrc, pa, pf, rppa):
  return (xwrc + float(pf) - 200) * float(rppa) * float(pa) / 100

@callback(
  Output('defense-runs', 'data'),
  Input('position', 'value'),
  Input('defense', 'value'),
  Input('games', 'value')
  )
def update_defense_runs(position, defense, games):
  if position == 'DH':
    defense = 0
  else:
    defense = (float(defense) - 50) * float(games) / 150
  return defense

@callback(
  Output('baserunning-runs', 'data'),
  Input('baserunning', 'value'),
  Input('plate-appearances', 'value')
  )
def update_baserunning_runs(baserunning, pa):
  return (float(baserunning) - 50) / 2 * float(pa) / 600

@callback(
  Output('positional-runs', 'data'),
  Input('position', 'value'),
  Input('games', 'value')
  )
def update_positional_runs(position, games):
  if position == 'C':
    value = 12.5
  elif position == '1B':
    value = -12.5
  elif position in ['2B', '3B', 'CF']:
    value = 2.5
  elif position == 'SS':
    value = 7.5
  elif position in ['LF', 'RF']:
    value = -7.5
  else:
    value = -17.5
  return float(value) * float(games) / 162

@callback(
  Output('replacement-runs', 'data'),
  Input('plate-appearances', 'value'),
  Input('replacement-level', 'value')
  )
def update_replacement_runs(pa, replacementlevel):
  return float(pa) * -float(replacementlevel) / 600

@callback(
  Output('runs-above-replacement', 'data'),
  Input('batting-runs', 'data'),
  Input('defense-runs', 'data'),
  Input('baserunning-runs', 'data'),
  Input('positional-runs', 'data'),
  Input('replacement-runs', 'data')
  )
def update_runs_above_replacement(battingruns, defenseruns, baserunningruns, positionalruns, replacementruns):
  return battingruns + defenseruns + baserunningruns + positionalruns + replacementruns

@callback(
  Output('wins-above-replacement', 'data'),
  Input('runs-above-replacement', 'data'),
  Input('runs-per-win', 'value')
  )
def update_wins_above_replacement(runsabovereplacement, runsperwin):
  return runsabovereplacement / float(runsperwin)


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
  Input('position', 'value'),
  Input('defense-runs', 'data')
  )
def update_defense_runs_display(position, defenseruns):
  if position == 'DH':
    dh_caveat = ' (DH, does not play defense)'
  else:
    dh_caveat = ''
  return f'Defensive Runs: ' + str(round(defenseruns, 1)) + dh_caveat

@callback(
  Output('baserunning-runs-display', 'children'),
  Input('baserunning-runs', 'data')
  )
def update_baserunning_runs_display(baserunningruns):
  return f'Baserunning Runs: ' + str(round(baserunningruns, 1))

@callback(
  Output('positional-runs-display', 'children'),
  Input('positional-runs', 'data')
  )
def update_replacement_runs_display(positionalruns):
  return f'Positional Runs: ' + str(round(positionalruns, 1))

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
def update_runs_above_replacement_display(runsabovereplacement):
  return f'Runs Above Replacement: ' + str(round(runsabovereplacement, 1))

@callback(
  Output('wins-above-replacement-display', 'children'),
  Input('wins-above-replacement', 'data')
  )
def update_wins_above_replacement_display(winsabovereplacement):
  return f'Wins Above Replacement: ' + str(round(winsabovereplacement, 1))

@callback(
  Output('advanced-selection', 'hidden'),
  Input('toggle-button', 'n_clicks')
  )
def toggle_advanced(nclicks):
  return (int(nclicks) % 2 == 0)

@callback(
  Output('toggle-button', 'children'),
  Input('toggle-button', 'n_clicks')
  )
def toggle_advanced(nclicks):
  if int(nclicks) % 2 == 1:
    label = 'Hide Advanced Inputs'
  else:
    label = 'Show Advanced Inputs'
  return label

if __name__ == '__main__':
    app.run(debug=True)


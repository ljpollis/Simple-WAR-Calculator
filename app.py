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
    html.Div(id='ops-plus'),
    html.H6(id='rate-stat-display'),
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
  html.Div(
      [
        html.Label('Defensive Performance'),
        dbc.Button('?', id = 'defense-20-80-?',style=roundbutton),
        dbc.Tooltip(
            "Baseball scouts grade tools on the 20-80 scale. For defense, 50 is the MLB average, 80 is Ozzie Smith, and 20 is Adam Dunn.",
            target="defense-20-80-?")
      ]
    ),
  dcc.Slider(
    id = 'defense',
    min = 20,
    max = 80,
    step = 5,
    value = 50
    ),
  html.Br(),
  html.Div(
      [
        html.Label('Baserunning Performance'),
        dbc.Button('?', id = 'baserunning-20-80-?',style=roundbutton),
        dbc.Tooltip(
            "Baseball scouts grade tools on the 20-80 scale. For speed, 50 is the MLB average, 80 is Billy Hamilton, and 20 is Billy Butler.",
            target="baserunning-20-80-?")
      ]
    ),
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
            "The proportion of batted balls within the field of play that fall for hits. Essentially batting average that doesn't count home runs or strikeouts.",
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
  dbc.Col(
    html.Div(
      [
        html.Label('Park Factor:'),
        dbc.Button('?', id = 'park-factor-?',style=roundbutton),
        dbc.Tooltip(
            "An adjustment for how favorable the run environment was in the parks where the player hit, due to field size, weather, etc. Usually ranges from around 90 (lower scoring) to 110 (more offense).",
            target="park-factor-?")
      ]
    ), width = 4, style={"verticalAlign": "center"}),
  dbc.Col(dcc.Input(id = 'park-factor', value = '100', type = 'number'), width = 1)
])

runs_per_pa_row = dbc.Row([
  dbc.Col(
    html.Div(
      [
        html.Label('League Runs per PA:'),
        dbc.Button('?', id = 'league-rppa-?',style=roundbutton),
        dbc.Tooltip(
            "The baseline runs created per plate appearance across the league.",
            target="league-rppa-?")
      ]
    ), width = 4, style={"verticalAlign": "center"}),
  dbc.Col(dcc.Input(id = 'runs-per-pa', value = '.117', type = 'number', step = 0.001), width = 1)
])

replacement_level_row = dbc.Row([
  dbc.Col(
    html.Div(
      [
        html.Label('Replacement Level (Runs per 600 PA):'),
        dbc.Button('?', id = 'replacement-level-?',style=roundbutton),
        dbc.Tooltip(
            "The difference in batting performance between an average player and a hitter you could easily call up or sign on short notice, extrapolated over a full season. (This gap is probably smaller in your beer league than it is in the big leagues.)",
            target="replacement-level-?")
      ]
    ), width = 4, style={"verticalAlign": "center"}),
  dbc.Col(dcc.Input(id = 'replacement-level', value = '-20', type = 'number', step = 0.1), width = 1)
])

runs_per_win_row = dbc.Row([
  dbc.Col(
    html.Div(
      [
        html.Label('Runs per Win Conversion:'),
        dbc.Button('?', id = 'runs-per-win-?',style=roundbutton),
        dbc.Tooltip(
            "The number of marginal runs scored (or prevented) it takes to increase a team's expected win total by one. Usually around 10 and correlated with R/PA.",
            target="runs-per-win-?")
      ]
    ), width = 4, style={"verticalAlign": "center"}),
  dbc.Col(dcc.Input(id = 'runs-per-win', value = '9.683', type = 'number', step = 0.001), width = 1)
])

obp_row = dbc.Row([
  dbc.Col(html.Label('OBP:'), width = 4),
  dbc.Col(dcc.Input(id = 'obp', value = '.400', type = 'number', step = 0.001), width = 1)
])

slg_row = dbc.Row([
  dbc.Col(html.Label('SLG:'), width = 4),
  dbc.Col(dcc.Input(id = 'slg', value = '.500', type = 'number', step = 0.001), width = 1)
])

lg_obp_row = dbc.Row([
  dbc.Col(
    html.Div(
      [
        html.Label('League OBP:'),
        dbc.Button('?', id = 'league-obp-?',style=roundbutton),
        dbc.Tooltip(
            "The average OBP for the league environment. If you have a park-adjusted version handy, you can put it here and league the park factor at 100.",
            target="league-obp-?")
      ]
    ), width = 4, style={"verticalAlign": "center"}),
  dbc.Col(dcc.Input(id = 'league-obp', value = '.312', type = 'number', step = 0.001), width = 1)
])

lg_slg_row = dbc.Row([
  dbc.Col(
    html.Div(
      [
        html.Label('League SLG:'),
        dbc.Button('?', id = 'league-slg-?',style=roundbutton),
        dbc.Tooltip(
            "The average SLG for the league environment. If you have a park-adjusted version handy, you can put it here and league the park factor at 100.",
            target="league-obp-?")
      ]
    ), width = 4, style={"verticalAlign": "center"}),
  dbc.Col(dcc.Input(id = 'league-slg', value = '.399', type = 'number', step = 0.001), width = 1)
])

batting_type = html.Div(
  [
    html.H5(
      [
        "Version: ",
        dbc.RadioItems(
          id="radios",
          className="btn-group",
          inputClassName="btn-check",
          labelClassName="btn btn-outline-primary",
          labelCheckedClassName="active",
          options=
            [
              {"label": "Original", "value": 1},
              {"label": "OPS+", "value": 2},
            ],
          value=1,
        ),
        html.Div(id="output"),
      ],
    className="radio-group",
    )
  ],
  style = {"margin-left": "10px"}
)

xwrcplus_inputs = dbc.Col(
  [
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
    dbc.Row(
      [
        dbc.Col(nontextselections, width = 10)
      ]
    ),
    html.Br(),
    dbc.Button(outline = True, color = 'primary', id = 'toggle-button', n_clicks = 0),
    html.Br(),
    html.Br(),
    html.Div(
      [
        runs_per_pa_row,
        html.Br(),
        replacement_level_row,
        html.Br(),
        runs_per_win_row], id = 'advanced-selection')
      ]
    )
    
opsplus_inputs = dbc.Col(
  [
    obp_row,
    html.Br(),
    slg_row,
    html.Br(),
    lg_obp_row,
    html.Br(),
    lg_slg_row,
    html.Br(),
    plate_appearances_row,
    html.Br(),
    games_row,
    html.Br(),
    park_factor_row,
    html.Br(),
    dbc.Row(
      [
        dbc.Col(nontextselections, width = 10)
      ]
    ),
    html.Br(),
    dbc.Button(outline = True, color = 'primary', id = 'toggle-button', n_clicks = 0),
    html.Br(),
    html.Br(),
    html.Div(
      [
        runs_per_pa_row,
        html.Br(),
        replacement_level_row,
        html.Br(),
        runs_per_win_row], id = 'advanced-selection')
      ]
    )


app.layout = [
  html.H1('Simple WAR Calculator'),
  html.Br(),
  batting_type,
  html.Br(),
  dbc.Row(
    [
      dbc.Col(id = "inputs", style = {"margin-left": "10px"}, width = 3),
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
  Input('ops-plus', 'data'),
  Input('plate-appearances', 'value'),
  Input('park-factor', 'value'),
  Input('runs-per-pa', 'value'),
  Input(component_id = 'radios', component_property = 'value')
  )
def update_batting_runs(xwrc, opsplus, pa, pf, rppa, selection):
  if selection == 1:
    inputtype = xwrc
  else:
    inputtype = opsplus
  return (inputtype + float(pf) - 200) * float(rppa) * float(pa) / 100

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

@callback(
  Output('ops-plus', 'data'),
  Input('obp', 'value'),
  Input('slg', 'value'),
  Input('league-obp', 'value'),
  Input('league-slg', 'value')
  )
def update_ops_plus(obp, slg, leagueobp, leagueslg):
  return 100 * (float(obp) / float(leagueobp) + float(slg) / float(leagueslg) - 1)


## Display callbacks

@callback(
  Output(component_id = 'rate-stat-display', component_property = 'children'),
  Input(component_id = 'xwrc', component_property = 'data'),
  Input(component_id = 'ops-plus', component_property = 'data'),
  Input(component_id = 'radios', component_property = 'value')
  )
def update_rate_stat(xwrc, opsplus, selection):
  if selection == 1:
    stat = xwrc
    label = 'xwRC+: '
  else:
    stat = opsplus
    label = 'OPS+: '
  return label + str(int(stat))

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

@callback(
  Output(component_id = 'ops-plus-display', component_property = 'children'),
  Input(component_id = 'ops-plus', component_property = 'data')
  )
def update_xwrc_display(opsplus):
  return f'OPS+: ' + str(int(opsplus))

@callback(
  Output(component_id = 'inputs', component_property = 'children'),
  Input(component_id = 'radios', component_property = 'value')
  )
def update_input_selections(selection):
  if selection == 1:
    inputtype = xwrcplus_inputs
  else:
    inputtype = opsplus_inputs
  return inputtype


if __name__ == '__main__':
    app.run(debug=True)


from dash import callback, Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets = [dbc.themes.BOOTSTRAP])

app.config.suppress_callback_exceptions = True

roundbutton = {
    'border' : None,
    'border-radius' : '50%',
    'padding' : 0,
    'backgroundColor' : 'blue',
    'color' : 'white',
    'textAlign' : 'center',
    'fontSize' : 10,
    'height' : 20,
    'width' : 20,
    'margin' : 2,
}

outputs = [
  html.Div(
    [
      html.H6(id = 'rate-stat-display'),
      html.Br(),
      html.Br(),
      html.H6(id = 'batting-runs-display'),
      html.Br(),
      html.H6(id = 'defense-runs-display'),
      html.Br(),
      html.H6(id = 'baserunning-runs-display'),
      html.Br(),
      html.H6(id = 'positional-runs-display'),
      html.Br(),
      html.H6(id = 'replacement-runs-display'),
      html.Br(),
      html.H6(id = 'runs-above-replacement-display'),
      html.Br(),
      html.Br(),
      html.Br(),
      html.H4(id = 'wins-above-replacement-display')
    ]
  )
]

outoftheway = [
    html.Div(id = 'xwrc'),
    html.Div(id = 'batting-runs'),
    html.Div(id = 'defense-runs'),
    html.Div(id = 'baserunning-runs'),
    html.Div(id = 'positional-runs'),
    html.Div(id = 'replacement-runs'),
    html.Div(id = 'runs-above-replacement'),
    html.Div(id = 'wins-above-replacement'),
    html.Div(id = 'ops-plus'),
    html.Div(id = 'pitching-runs'),
    html.Div(id = 'replacement-runs-p'),
    html.Div(id = 'runs-above-replacement-p'),
    html.Div(id = 'wins-above-replacement-p'),
    html.Div(id = 'leverage-runs'),
    html.Div(id = 'kwera'),
    html.Div(id = 'fip'),
]

home_runs_row = dbc.Row(
  [
    dbc.Col(html.Label('Home Runs:'), width = 4),
    dbc.Col(dcc.Input(id = 'home-runs', value = '16', type = 'number'), width = 1)
  ]
)

walks_row = dbc.Row(
  [
    dbc.Col(html.Label('Walks:'), width = 4),
    dbc.Col(dcc.Input(id = 'walks', value = '50', type = 'number'), width = 1)
  ]
)

strikeouts_row = dbc.Row(
  [
    dbc.Col(html.Label('Strikeouts:'), width = 4),
    dbc.Col(dcc.Input(id = 'strikeouts', value = '75', type = 'number'), width = 1)
  ]
)

stolen_bases_row = dbc.Row(
  [
    dbc.Col(html.Label('Stolen Bases:'), width = 4),
    dbc.Col(dcc.Input(id = 'stolen-bases', value = '8', type = 'number'), width = 1)
  ]
)

babip_row = dbc.Row(
  [
    dbc.Col(
      html.Div(
        [
          html.Label('BABIP:'),
          dbc.Button('?', id = 'babip-?', style = roundbutton),
          dbc.Tooltip(
            "The proportion of batted balls within the field of play that fall for hits. Essentially batting average that doesn't count home runs or strikeouts.",
            target = 'babip-?'
          )
         ]
      ), width = 4, style = {'verticalAlign' : 'center'}
    ),
    dbc.Col(dcc.Input(id = 'babip', value = '.300', type = 'number', step = 0.001), width = 1)
  ]
)

obp_row = dbc.Row(
  [
    dbc.Col(html.Label('OBP:'), width = 4),
    dbc.Col(dcc.Input(id = 'obp', value = '.400', type = 'number', step = 0.001), width = 1)
  ]
)

slg_row = dbc.Row(
  [
    dbc.Col(html.Label('SLG:'), width = 4),
    dbc.Col(dcc.Input(id = 'slg', value = '.500', type = 'number', step = 0.001), width = 1)
  ]
)

lg_obp_row = dbc.Row(
  [
    dbc.Col(
      html.Div(
        [
          html.Label('League OBP:'),
          dbc.Button('?', id = 'league-obp-?', style = roundbutton),
          dbc.Tooltip(
            'The average OBP for the league environment. If you have a park-adjusted version handy, you can put it here and league the park factor at 100.',
            target = 'league-obp-?'
          )
        ]
      ), width = 4, style = {'verticalAlign' : 'center'}
    ),
    dbc.Col(dcc.Input(id = 'league-obp', value = '.312', type = 'number', step = 0.001), width = 1)
  ]
)

lg_slg_row = dbc.Row(
  [
    dbc.Col(
      html.Div(
        [
          html.Label('League SLG:'),
          dbc.Button('?', id = 'league-slg-?', style = roundbutton),
          dbc.Tooltip(
            'The average SLG for the league environment. If you have a park-adjusted version handy, you can put it here and league the park factor at 100.',
            target = 'league-slg-?'
          )
        ]
      ), width = 4, style = {'verticalAlign' : 'center'}
    ),
    dbc.Col(dcc.Input(id = 'league-slg', value = '.399', type = 'number', step = 0.001), width = 1)
  ]
)

plate_appearances_row = dbc.Row(
  [
    dbc.Col(html.Label('Plate Appearances:'), width = 4),
    dbc.Col(dcc.Input(id = 'plate-appearances', value = '600', type = 'number'), width = 1)
  ]
)

games_row = dbc.Row(
  [
    dbc.Col(html.Label('Games:'), width = 4),
    dbc.Col(dcc.Input(id = 'games', value = '150', type = 'number'), width = 1)
  ]
)

nontextselections = [
  html.Label('Primary Position'),
  dcc.Dropdown(['C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'DH'], 'LF', id = 'position'),
  html.Br(),
  html.Div(
    [
      html.Label('Defensive Performance'),
      dbc.Button('?', id = 'defense-20-80-?', style = roundbutton),
      dbc.Tooltip(
        'Baseball scouts grade tools on the 20-80 scale. For defense, 50 is the MLB average, 80 is Ozzie Smith, and 20 is Adam Dunn.',
        target = 'defense-20-80-?'
      )
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
      dbc.Button('?', id = 'baserunning-20-80-?', style = roundbutton),
      dbc.Tooltip(
        'Baseball scouts grade tools on the 20-80 scale. For speed, 50 is the MLB average, 80 is Billy Hamilton, and 20 is Billy Butler.',
        target = 'baserunning-20-80-?'
      )
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

park_factor_row = dbc.Row(
  [
    dbc.Col(
      html.Div(
        [
          html.Label('Park Factor:'),
          dbc.Button('?', id = 'park-factor-?', style = roundbutton),
          dbc.Tooltip(
            target = 'park-factor-?',
            id = 'park-factor-info'
          )
        ]
      ), width = 4, style = {'verticalAlign' : 'center'}
    ),
    dbc.Col(dcc.Input(id = 'park-factor', value = '100', type = 'number'), width = 1)
  ]
)

runs_per_pa_row = dbc.Row(
  [
    dbc.Col(
      html.Div(
        [
          html.Label('League Runs per PA:'),
          dbc.Button('?', id = 'league-rppa-?', style = roundbutton),
          dbc.Tooltip(
            'The baseline runs created per plate appearance across the league.',
            target = 'league-rppa-?'
          )
        ]
      ), width = 4, style = {'verticalAlign' : 'center'}
    ),
    dbc.Col(dcc.Input(id = 'runs-per-pa', value = '.117', type = 'number', step = 0.001), width = 1)
  ]
)

replacement_level_row = dbc.Row(
  [
    dbc.Col(
      html.Div(
        [
          html.Label('Replacement Level (Runs per 600 PA):'),
          dbc.Button('?', id = 'replacement-level-?', style = roundbutton),
          dbc.Tooltip(
            'The difference in batting performance between an average player and a hitter you could easily call up or sign on short notice, extrapolated over a full season. (This gap is probably smaller in your beer league than it is in the big leagues.)',
            target = 'replacement-level-?'
          )
        ]
      ), width = 4, style = {'verticalAlign' : 'center'}
    ),
    dbc.Col(dcc.Input(id = 'replacement-level', value = '-20', type = 'number', step = 0.1), width = 1)
  ]
)

runs_per_win_row = dbc.Row(
  [
    dbc.Col(
      html.Div(
        [
          html.Label('Runs per Win Conversion:'),
          dbc.Button('?', id = 'runs-per-win-?', style = roundbutton),
          dbc.Tooltip(
            "The number of marginal runs scored (or prevented) it takes to increase a team's expected win total by one. Usually around 10 and correlated with R/PA.",
            target = 'runs-per-win-?'
          )
        ]
      ), width = 4, style = {'verticalAlign' : 'center'}
    ),
    dbc.Col(dcc.Input(id = 'runs-per-win', value = '9.683', type = 'number', step = 0.001), width = 1)
  ]
)

era_row = dbc.Row(
  [
    dbc.Col(html.Label(id = 'era-label'), width = 4),
    dbc.Col(dcc.Input(id = 'era', type = 'number', step = 0.01), width = 1),
  ]
)

k_row = dbc.Row(
  [
    dbc.Col(html.Label('Strikeouts'), width = 4),
    dbc.Col(dcc.Input(id = 'k', type = 'number', step = 1), width = 1),
  ]
)

bb_row = dbc.Row(
  [
    dbc.Col(html.Label('Walks'), width = 4),
    dbc.Col(dcc.Input(id = 'bb', type = 'number', step = 1), width = 1),
  ]
)

hr_row = dbc.Row(
  [
    dbc.Col(html.Label('Home Runs'), width = 4),
    dbc.Col(dcc.Input(id = 'hr', type = 'number', step = 1), width = 1),
  ]
)

ip_row = dbc.Row(
  [
    dbc.Col(html.Label('IP'), width = 4),
    dbc.Col(dcc.Input(id = 'ip', type = 'number', step = 1), width = 1),
  ]
)

lg_era_row = dbc.Row(
  [
    dbc.Col(html.Label(id = 'league-era-label'), width = 4),
    dbc.Col(dcc.Input(id = 'league-era', type = 'number', step = 0.01), width = 1),
  ]
)

leverage_row = dbc.Row(
  [
    dbc.Col(html.Label('Entrance Leverage Index:'), width = 4),
    dbc.Col(dcc.Input(id = 'gmli', value = 1.00, type = 'number', step = 0.01), width = 1)
  ]
)

pitching_role_row = dbc.Row(
  [
    html.Label('Primary Position'),
    dcc.Dropdown(['Starter', 'Reliever'], 'Starter', id = 'position-p')
  ]
)

replacement_level_p_row = dbc.Row(
  [
    dbc.Col(
      html.Div(
        [
          html.Label('Replacement Level (Runs per 200 IP):'),
          dbc.Button('?', id = 'replacement-level-p-?', style = roundbutton),
          dbc.Tooltip(
            'The difference in performance between an average player and a pitcher you could easily call up or sign on short notice, extrapolated over a full season. (This gap is probably smaller in your beer league than it is in the big leagues.)',
            target = 'replacement-level-p-?'
          )
        ]
      ), width = 4, style = {'verticalAlign' : 'center'}
    ),
    dbc.Col(dcc.Input(id = 'replacement-level-p', value = '-18.5', type = 'number', step = 0.1), width = 1)
  ]
)

positional_adjustment_row = dbc.Row(
  [
    dbc.Col(html.Label('Positional Adjustment:'), width = 4),
    dbc.Col(dcc.Input(id = 'positional-adjustment', type = 'number', step = 0.01), width = 1)
  ]
)

player_type_select = html.Div(
  [
    html.H5(
      [
        'Player Type: ',
        dbc.RadioItems(
          id = 'player-type',
          className = 'btn-group',
          inputClassName = 'btn-check',
          labelClassName = 'btn btn-outline-primary',
          labelCheckedClassName = 'active',
          options =
            [
              {'label' : 'Batters', 'value' : 1},
              {'label' : 'Pitchers', 'value' : 2}
            ],
          value = 1,
        ),
        html.Div(id = 'output2'),
      ],
    className = 'radio-group',
    )
  ],
  style = {'margin-left' : '10px'}
)

version_select = html.Div(
  [
    html.H5(
      [
        'Version: ',
        dbc.RadioItems(
          id = 'radios',
          className = 'btn-group',
          inputClassName = 'btn-check',
          labelClassName = 'btn btn-outline-primary',
          labelCheckedClassName = 'active'
        ),
        html.Div(id = 'output'),
      ],
    className = 'radio-group',
    )
  ],
  style = {'margin-left' : '10px'}
)


hitting_inputs = dbc.Col(
  [
    html.Div(home_runs_row, id = 'home-runs-row-display'),
    html.Br(id = 'home-runs-break-display'),
    html.Div(walks_row, id = 'walks-row-display'),
    html.Br(id = 'walks-break-display'),
    html.Div(strikeouts_row, id = 'strikeouts-row-display'),
    html.Br(id = 'strikeouts-break-display'),
    html.Div(stolen_bases_row, id = 'stolen-bases-row-display'),
    html.Br(id = 'stolen-bases-break-display'),
    html.Div(babip_row, id = 'babip-row-display'),
    html.Br(id = 'babip-break-display'),
    html.Div(obp_row, id = 'obp-row-display'),
    html.Br(id = 'obp-break-display'),
    html.Div(slg_row, id = 'slg-row-display'),
    html.Br(id = 'slg-break-display'),
    html.Div(lg_obp_row, id = 'lg-obp-row-display'),
    html.Br(id = 'lg-obp-break-display'),
    html.Div(lg_slg_row, id = 'lg-slg-row-display'),
    html.Br(id = 'lg-slg-break-display'),
    html.Div(plate_appearances_row, id = 'plate-appearances-row-display'),
    html.Br(id = 'plate-appearances-break-display'),
    html.Div(games_row, id = 'games-row-display'),
    html.Br(id = 'games-break-display'),
    html.Div(park_factor_row, id = 'park-factor-row-display'),
    html.Br(id = 'park-factor-break-display'),
    dbc.Row(dbc.Col(nontextselections, width = 10)),
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
    
era_inputs = dbc.Col(
  [
    html.Div(era_row, id = 'era-row-display'),
    html.Br(id = 'era-break-display'),
    html.Div(k_row, id = 'k-row-display'),
    html.Br(id = 'k-break-display'),
    html.Div(bb_row, id = 'bb-row-display'),
    html.Br(id = 'bb-break-display'),
    html.Div(hr_row, id = 'hr-row-display'),
    html.Br(id = 'hr-break-display'),
    html.Div(ip_row, id = 'ip-row-display'),
    html.Br(id = 'ip-break-display'),
    html.Div(lg_era_row, id = 'lg-era-row-display'),
    html.Br(id = 'lg-era-break-display'),
    html.Div(park_factor_row, id = 'park_factor-row-display'),
    html.Br(id = 'park_factor-break-display'),
    html.Div(leverage_row, id = 'leverage-row-display'),
    html.Br(id = 'leverage-break-display'),
    html.Div(pitching_role_row, id = 'pitching-role-display'),
    html.Br(id = 'pitching-break-display'),
    dbc.Button(outline = True, color = 'primary', id = 'toggle-button', n_clicks = 0),
    html.Br(),
    html.Br(),
    html.Div(
      [
        positional_adjustment_row,
        html.Br(),
        replacement_level_p_row,
        html.Br(),
        runs_per_win_row
      ], id = 'advanced-selection'
    )
  ]
)

outputs_era = [
  html.Div(
    [
      html.H6(id = 'kwera-display'),
      html.H6(id = 'fip-display'),
      html.Br(id = 'pitching-post-rate-stat-break-display-1'),
      html.Br(id = 'pitching-post-rate-stat-break-display-2'),
      html.H6(id = 'pitching-runs-display'),
      html.Br(),
      html.H6(id = 'leverage-runs-display'),
      html.Br(id = 'leverage-runs-break-display'),
      html.H6(id = 'replacement-runs-p-display'),
      html.Br(),
      html.H6(id = 'runs-above-replacement-p-display'),
      html.Br(),
      html.Br(),
      html.Br(),
      html.H4(id = 'wins-above-replacement-p-display')
    ]
  )
]


app.layout = [
  html.H1('Simple WAR Calculator'),
  html.Br(),
  player_type_select,
  html.Br(),
  version_select,
  html.Br(),
  dbc.Row(
    [
      dbc.Col(id = 'inputs', style = {'margin-left' : '10px'}, width = 3),
      dbc.Col(id = 'outputs', width = 3)
    ], justify = 'start'
  ),
  dbc.Row(outoftheway)
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

@callback(
  Output('pitching-runs', 'data'),
  Input('era', 'value'),
  Input('league-era', 'value'),
  Input('ip', 'value'),
  Input('positional-adjustment', 'value'),
  Input('kwera', 'data'),
  Input('fip', 'data'),
  Input('park-factor', 'value'),
  Input(component_id = 'radios', component_property = 'value')
  )
def update_pitching_runs(era, leagueera, ip, positionaladjustment, kwera, fip, pf, selection):
  if selection == 4:
    adjustment = 1
  else:
    adjustment = 1.094
  if selection < 5:
    erainput = era
  elif selection == 5:
    erainput = kwera
  else:
    erainput = fip
  return (float(leagueera) - float(erainput) * 100 / int(pf) + float(positionaladjustment)) * int(ip) / 9 * adjustment

@callback(
  Output('replacement-runs-p', 'data'),
  Input('ip', 'value'),
  Input('replacement-level-p', 'value')
  )
def update_replacement_runs_p(ip, replacementlevel):
  return float(ip) * - float(replacementlevel) / 200

@callback(
  Output('runs-above-replacement-p', 'data'),
  Input('pitching-runs', 'data'),
  Input('leverage-runs', 'data'),
  Input('replacement-runs-p', 'data')
  )
def update_runs_above_replacement(pitchingruns, leverageruns, replacementruns):
  return pitchingruns + leverageruns + replacementruns

@callback(
  Output('wins-above-replacement-p', 'data'),
  Input('runs-above-replacement-p', 'data'),
  Input('runs-per-win', 'value')
  )
def update_wins_above_replacement(runsabovereplacement, runsperwin):
  return float(runsabovereplacement) / float(runsperwin)

@callback(
  Output('leverage-runs', 'data'),
  Input('pitching-runs', 'data'),
  Input('gmli', 'value'),
  Input(component_id = 'position-p', component_property = 'value')
  )
def update_leverage_runs(pitchingruns, gmli, position):
  if position == 'Starter':
    leverage = 1
  else:
    leverage = gmli
  return pitchingruns * (leverage - 1) / 2

@callback(
  Output('kwera', 'data'),
  Input('k', 'value'),
  Input('bb', 'value'),
  Input('ip', 'value'),
  Input('league-era', 'value')
  )
def update_kwera(k, bb, ip, era):
  return float(era) + 1.73 - 12 * (float(k) - float(bb)) / float(ip) / 4.23

@callback(
  Output('fip', 'data'),
  Input('k', 'value'),
  Input('bb', 'value'),
  Input('hr', 'value'),
  Input('ip', 'value'),
  Input('league-era', 'value')
  )
def update_kwera(k, bb, hr, ip, era):
  return float(era) - .91 + (13 * float(hr) + 3 * float(bb) - 2 * float(k)) / float(ip)


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
    inputtype = hitting_inputs
  elif selection == 2:
    inputtype = hitting_inputs
  else:
    inputtype = era_inputs
  return inputtype

@callback(
  Output(component_id = 'positional-adjustment', component_property = 'value'),
  Input(component_id = 'position-p', component_property = 'value')
  )
def update_positional_adjustment(position):
  if position == 'Starter':
    era = 0.07
  else:
    era = -0.11
  return era

@callback(
  Output('pitching-runs-display', 'children'),
  Input('pitching-runs', 'data')
  )
def update_pitching_runs_display(pitchingruns):
  return f'Pitching Runs: ' + str(round(pitchingruns, 1))

@callback(
  Output('replacement-runs-p-display', 'children'),
  Input('replacement-runs-p', 'data')
  )
def update_replacement_runs_display(replacementruns):
  return f'Replacement Runs: ' + str(round(replacementruns, 1))

@callback(
  Output('runs-above-replacement-p-display', 'children'),
  Input('runs-above-replacement-p', 'data')
  )
def update_runs_above_replacement_p_display(runsabovereplacement):
  return f'Runs Above Replacement: ' + str(round(runsabovereplacement, 1))

@callback(
  Output('wins-above-replacement-p-display', 'children'),
  Input('wins-above-replacement-p', 'data')
  )
def update_wins_above_replacement_p_display(winsabovereplacement):
  return f'Wins Above Replacement: ' + str(round(winsabovereplacement, 1))

@callback(
  Output(component_id = 'outputs', component_property = 'children'),
  Input(component_id = 'radios', component_property = 'value')
  )
def update_input_selections(selection):
  if selection < 3:
    inputtype = outputs
  else:
    inputtype = outputs_era
  return inputtype

@callback(
  Output('leverage-runs-display', 'children'),
  Input('leverage-runs', 'data')
  )
def update_leverage_runs_display(leverageruns):
  return f'Leverage Runs: ' + str(round(leverageruns, 1))

@callback(
  Output('era-label', 'children'),
  Input(component_id = 'radios', component_property = 'value')
  )
def update_era_label(selection):
  if selection == 4:
    label = 'RA9: '
  else:
    label = 'ERA: '
  return label

@callback(
  Output('era', 'value'),
  Input(component_id = 'radios', component_property = 'value')
  )
def update_era_default(selection):
  if selection == 4:
    default = 4.39
  else:
    default = 3.99
  return default

@callback(
  Output('league-era-label', 'children'),
  Input(component_id = 'radios', component_property = 'value')
  )
def update_league_era_label(selection):
  if selection == 4:
    label = 'League RA9: '
  else:
    label = 'League ERA: '
  return label

@callback(
  Output('league-era', 'value'),
  Input(component_id = 'radios', component_property = 'value')
  )
def update_era_default(selection):
  if selection == 4:
    default = 4.46
  else:
    default = 4.08
  return default

@callback(
  Output(component_id = 'kwera-display', component_property = 'children'),
  Input(component_id = 'kwera', component_property = 'data')
  )
def update_kwera_display(kwera):
  return f'kwERA: ' + str(round(kwera, 2))

@callback(
  Output(component_id = 'fip-display', component_property = 'children'),
  Input(component_id = 'fip', component_property = 'data')
  )
def update_fip_display(fip):
  return f'FIP: ' + str(round(fip, 2))

@callback(
  Output('ip', 'value'),
  Output('k', 'value'),
  Output('bb', 'value'),
  Output('hr', 'value'),
  Input(component_id = 'position-p', component_property = 'value')
  )
def update_ip_default(selection):
  if selection == 'Starter':
    defaultip = 200
    defaultk = 200
    defaultbb = 50
    defaulthr = 20
  else:
    defaultip = 70
    defaultk = 70
    defaultbb = 20
    defaulthr = 10
  return defaultip, defaultk, defaultbb, defaulthr

@callback(
  Output('radios', 'options'),
  Output('radios', 'value'),
  Input(component_id = 'player-type', component_property = 'value')
  )
def update_options(selection):
  if selection == 1:
    choices = [
      {'label' : 'Original (xwRC+)', 'value' : 1},
      {'label' : 'OPS+', 'value' : 2}
    ]
    default = 1
  else:
    choices = [
      {'label' : 'Original (ERA)', 'value' : 3},
      {'label' : 'RA9', 'value' : 4},
      {'label' : 'kwERA', 'value' : 5},
      {'label' : 'FIP', 'value' : 6}
    ]
    default = 3
  return choices, default

@callback(
  Output('home-runs-row-display', 'hidden'),
  Output('home-runs-break-display', 'hidden'),
  Output('walks-row-display', 'hidden'),
  Output('walks-break-display', 'hidden'),
  Output('strikeouts-row-display', 'hidden'),
  Output('strikeouts-break-display', 'hidden'),
  Output('stolen-bases-row-display', 'hidden'),
  Output('stolen-bases-break-display', 'hidden'),
  Output('babip-row-display', 'hidden'),
  Output('babip-break-display', 'hidden'),
  Output('obp-row-display', 'hidden'),
  Output('obp-break-display', 'hidden'),
  Output('slg-row-display', 'hidden'),
  Output('slg-break-display', 'hidden'),
  Output('lg-obp-row-display', 'hidden'),
  Output('lg-obp-break-display', 'hidden'),
  Output('lg-slg-row-display', 'hidden'),
  Output('lg-slg-break-display', 'hidden'),
  Input(component_id = 'radios', component_property = 'value')
  )
def update_options(selection):
  if selection == 1:
    wrcplus = False
    opsplus = True
  else:
    wrcplus = True
    opsplus = False
  return wrcplus, wrcplus, wrcplus, wrcplus, wrcplus, wrcplus, wrcplus, wrcplus, wrcplus, wrcplus, opsplus, opsplus, opsplus, opsplus, opsplus, opsplus, opsplus, opsplus

@callback(
  Output('era-row-display', 'hidden'),
  Output('era-break-display', 'hidden'),
  Output('k-row-display', 'hidden'),
  Output('k-break-display', 'hidden'),
  Output('bb-row-display', 'hidden'),
  Output('bb-break-display', 'hidden'),
  Output('hr-row-display', 'hidden'),
  Output('hr-break-display', 'hidden'),
  Output('kwera-display', 'hidden'),
  Output('fip-display', 'hidden'),
  Output('pitching-post-rate-stat-break-display-1', 'hidden'),
  Output('pitching-post-rate-stat-break-display-2', 'hidden'),
  Input(component_id = 'radios', component_property = 'value')
  )
def update_options(selection):
  if selection < 5:
    era = False
    k = True
    bb = True
    hr = True
    kwera = True
    fip = True
    estimator = True
  elif selection == 5:
    era = True
    k = False
    bb = False
    hr = True
    kwera = False
    fip = True
    estimator = False
  else:
    era = True
    k = False
    bb = False
    hr = False
    kwera = True
    fip = False
    estimator = False
  return era, era, k, k, bb, bb, hr, hr, kwera, fip, estimator, estimator

@callback(
  Output('leverage-row-display', 'hidden'),
  Output('leverage-break-display', 'hidden'),
  Output('leverage-runs-break-display', 'hidden'),
  Output('leverage-runs-display', 'hidden'),
  Input('position-p', 'value')
  )
def update_options(selection):
  if selection == 'Starter':
    leverage = True
  else:
    leverage = False
  return leverage, leverage, leverage, leverage

@callback(
  Output('park-factor-info', 'children'),
  Input(component_id = 'radios', component_property = 'value')
  )
def update_options(selection):
  if selection == 1:
    info = 'An adjustment for how favorable the run environment was in the parks where the player hit, due to field size, weather, etc. Usually ranges from around 90 (lower scoring) to 110 (more offense).'
  elif selection == 2:
    info = 'An adjustment for how favorable the run environment was in the parks where the player hit, due to field size, weather, etc. Usually ranges from around 90 (lower scoring) to 110 (more offense). If you are factoring park into the league OBP and SLG, leave this at 100.'
  elif selection == 4:
    info = 'An adjustment for how favorable the run environment was in the parks where the player hit, due to field size, weather, etc. Usually ranges from around 90 (lower scoring) to 110 (more offense). If you are factoring park into the league RA9, leave this at 100.'
  else:
    info = 'An adjustment for how favorable the run environment was in the parks where the player hit, due to field size, weather, etc. Usually ranges from around 90 (lower scoring) to 110 (more offense). If you are factoring park into the league ERA, leave this at 100.'
  return info


if __name__ == '__main__':
    app.run(debug=True)


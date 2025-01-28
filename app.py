from dash import callback, Dash, dcc, html, Input, Output

app = Dash()

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
    html.Div(id='xwrc')
  ])
]

@callback(
    Output(component_id = 'xwrc', component_property='children'),
    Input(component_id = 'home-runs', component_property = 'value'),
    Input(component_id = 'walks', component_property = 'value'),
    Input(component_id = 'strikeouts', component_property = 'value'),
    Input(component_id = 'stolen-bases', component_property = 'value'),
    Input(component_id = 'babip', component_property = 'value'),
    Input(component_id = 'plate-appearances', component_property = 'value')
)
def update_output_div(hr, bb, k, sb, babip, pa):
    return f'xwRC+: ' + str(int(1184.34 * float(hr) / float(pa) + 275.21 * float(bb) / float(pa) - 180.52 * float(k) / float(pa) + 422.14 * float(babip) + 151.75 * float(sb) / float(pa) - 51.57))

if __name__ == '__main__':
    app.run(debug=True)


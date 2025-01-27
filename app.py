from dash import Dash, dcc, html

app = Dash()

app.layout = [
  html.H1('Simple WAR Calculator'),
  html.Div(children=[
    html.Label('Home Runs'),
    html.Br(),
    dcc.Input(value = '16', type = 'number'),
    html.Br(),
    html.Br(),
    html.Label('Walks'),
    html.Br(),
    dcc.Input(value = '50', type = 'number'),
    html.Br(),
    html.Br(),
    html.Label('Strikeouts'),
    html.Br(),
    dcc.Input(value = '75', type = 'number'),
    html.Br(),
    html.Br(),
    html.Label('Stolen Bases'),
    html.Br(),
    dcc.Input(value = '8', type = 'number'),
    html.Br(),
    html.Br(),
    html.Label('BABIP'),
    html.Br(),
    dcc.Input(value = '.300', type = 'number', step = 0.001),
    html.Br(),
    html.Br(),
    html.Label('Plate Appearances'),
    html.Br(),
    dcc.Input(value = '600', type = 'number'),
    html.Br(),
    html.Br(),
    html.Label('Games'),
    html.Br(),
    dcc.Input(value = '150', type = 'number'),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Label('Primary Position'),
    dcc.Dropdown(['C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'DH'], 'LF'),
    html.Br(),
    html.Label('Defensive Performance'),
    dcc.Slider(
      min = 20,
      max = 80,
      step = 10,
      value = 50,
        ),
    html.Br(),
    html.Label('Baserunning Performance'),
    dcc.Slider(
      min = 20,
      max = 80,
      step = 10,
      value = 50,
        )
  ])
]

if __name__ == '__main__':
    app.run(debug=True)


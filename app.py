import dash
import dash_core_components as dcc 
import dash_html_components as html 
import plotly.graph_objs as go
import pandas as pd
import numpy as np

from dash.dependencies import Input, Output

# Step 1. Launch the application
app = dash.Dash()

# Step 2. Import the dataset
k = pd.DataFrame(list(np.arange(0,5,0.01)))

d = 0.2
n = 0.02
s = 0.3
a = 0.5

index = pd.DataFrame(list(range(0,101)))

equal = ((d + n)/s)**(1/(a-1))

# Step 3. Create a plotly figure
trace_1 = go.Scatter(x = k[0], y = k[0] ** a,
                    name = 'f(x)',
                    line = dict(width = 2,
                                color = 'rgb(229, 151, 50)'))


layout = go.Layout(title = 'Produto, poupança, depreciação e crescimento populacional',
                    hovermode = 'closest',
                    updatemenus=[dict(type="buttons",
                                    buttons=[dict(label="Play",
                                            method="animate",
                                            args=[None])])
                                            ]                   )


fig = go.Figure(data = [trace_1], layout = layout)

fig.add_trace(go.Scatter(x=k[0], y=s*(k[0]**a),
                        mode='lines',
                        name='sf(x)'))

fig.add_trace(go.Scatter(x=k[0], y=(d+n)*(k[0]),
                        mode='lines',
                        name='df(x)'))

fig.layout.update(
    showlegend=False,
    annotations=[
        go.layout.Annotation(
            x=equal,
            y=0,
            xref="x",
            yref="y",
            text="Eq. inicial",
            arrowwidth=1,
            arrowhead=7,
            showarrow=True,
            ax=0,
            ay=-200
        )
    ]
)


trace_2 = go.Scatter(x = [0], y = [0],
                        name = 'gx',
                        line = dict(width = 2,
                                    color = 'rgb(229, 151, 50)'))


fig2 = go.Figure(data = [trace_2], layout = layout)

#fig3.add_trace(go.Scatter(x=k[0], y=(s*(k[0]**a))/k[0],
#                        mode='lines',
#                        name='sf(x)'))


trace_3 = go.Scatter(x=k[0], y=(s*(k[0]**a))/k[0],
                        name = 'gx',
                        line = dict(width = 2,
                                    color = 'rgb(229, 151, 50)'))

fig3 = go.Figure(data = [trace_3], layout = layout)


fig3.add_trace(go.Scatter(x=k[0], y=[d+n]*len(k[0]),
                        mode='lines',
                        name='df(x)'))



    # Step 4. Create a Dash layout
app.layout = html.Div([
                # a header and a paragraph
                html.Div([
                    html.H1("Solow-Swan Model")
                        ]),
                    html.Div([
                        html.Div(
                            html.P('d:'),
                            style={'display': 'inline-block'}),
                        html.Div(
                            dcc.Input(id='d', type='number', value = d, step=0.05),
                            style={'display': 'inline-block'})],
                        style={'width': '12.5%', 'display': 'inline-block'}),
                    html.Div([
                        html.Div(
                            html.P('n:'),
                            style={'display': 'inline-block'}),
                        html.Div(
                            dcc.Input(id='n', type='number', value = n, step=0.01),
                            style={'display': 'inline-block'})],
                        style={'width': '12.5%', 'display': 'inline-block'}),
                    html.Div([
                        html.Div(
                            html.P('s:'),
                            style={'display': 'inline-block'}),
                        html.Div(
                            dcc.Input(id='s', type='number', value = s, step=0.05),
                            style={'display': 'inline-block'})],
                        style={'width': '12.5%', 'display': 'inline-block'}),                                                
                    html.Div([
                        html.Div(
                            html.P('a:'),
                            style={'display': 'inline-block'}),
                        html.Div(
                            dcc.Input(id='a', type='number', value = a, step=0.05),
                            style={'display': 'inline-block'})],
                        style={'width': '12.5%', 'display': 'inline-block'}),                    
                #html.P(':'),
                #dcc.Input(id='n', type='number', value = n, step=0.01),
                #dcc.Input(id='s', type='number', value = s, step=0.05),
                #dcc.Input(id='a', type='number', value = a, step=0.05),
                # adding a plot
                html.Div([
                    html.Div([
                        dcc.Graph(id = 'plot', figure = fig)
                            ], style={'width': '48%', 'display': 'inline-block'}),
                    html.Div([dcc.Graph(id = 'plot2', figure = fig2)],
                        style={'width': '48%', 'float':'right', 'display': 'inline-block'})
                            ]),
                html.Div([
                    html.Div([
                        dcc.Graph(id = 'plot3', figure = fig3)
                            ], style={'width': '48%', 'display': 'inline-block'}),
                    html.Div([dcc.Graph(id = 'plot4', figure = fig2)],
                        style={'width': '48%', 'float':'right', 'display': 'inline-block'})
                            ])
                            
                        ])

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

    # Step 5. Add callback functions
@app.callback([Output('plot', 'figure'),
                Output('plot2', 'figure'),
                Output('plot3', 'figure'),
                Output('plot4', 'figure')],
                [Input('d', 'value'), 
                Input('n', 'value'),
                Input('s', 'value'),
                Input('a', 'value')])

def update_figure(input1,input2,input3,input4):
        # updating the plot
    d = input1
    n = input2
    s = input3
    a = input4

    new_equal = ((d + n)/s)**(1/(a-1))
            
    trace_1 = go.Scatter(x = k[0], y = k[0] ** a,
                        name = 'f(x)',
                        line = dict(width = 2,
                                    color = 'rgb(229, 151, 50)'))
        
    layout1 = go.Layout(title = 'Produto, poupança, depreciação e crescimento populacional',
                    hovermode = 'closest',
                    updatemenus=[
                            dict(type="buttons",
                            buttons=[dict(label="Play",
                                        method="animate",
                                        args=[None])])
                                        ])
    layout2 = go.Layout(title = 'gy, gk',
                    hovermode = 'closest',
                    updatemenus=[
                            dict(type="buttons",
                            buttons=[dict(label="Play",
                                        method="animate",
                                        args=[None])])
                                        ])
        
    layout3 = go.Layout(title = 'Taxas de crescimento',
                    hovermode = 'closest',
                    updatemenus=[
                            dict(type="buttons",
                            buttons=[dict(label="Play",
                                        method="animate",
                                        args=[None])])
                                        ])

    layout4 = go.Layout(title = 'log(Y/L)',
                    hovermode = 'closest',
                    updatemenus=[
                            dict(type="buttons",
                            buttons=[dict(label="Play",
                                        method="animate",
                                        args=[None])])
                                        ])

    kz = equal
    yz = kz**a
    gk = (s*(kz**(a-1)))-d-n
    gy = 0

    i = 0

    time = pd.DataFrame(np.matrix([0,kz,yz,gk]))

    for i in range(0,201):
        gk = round(s*(time.iloc[i,1]**(a-1))-d-n,5)
        kz = time.iloc[i,1] + gk
        yz = time.iloc[i,1]**a
        gy = round(yz - time.iloc[i-1,2],5)
        #print(gy)
        print(np.log(yz))
        time = time.append(pd.DataFrame(np.matrix([i,kz,yz,gk,gy])))

    time.columns = ['idx','kz','yz','gk','gy']

    fig = go.Figure(data = [trace_1],
        layout = layout1
        )
                
    trace_2 = go.Scatter(x = time.iloc[1:,0], y = time.iloc[1:,3],
                        name = 'gk',
                        line = dict(width = 2,
                                    color = 'rgb(229, 151, 50)'))


    fig2 = go.Figure(data = [trace_2],
        layout = layout2
        )    

    fig2.add_trace(go.Scatter(x=time.iloc[1:,0], y=time.iloc[3:,4],
                    mode='lines',
                    name='gy',
                    line = dict(color = 'blue')))    

    trace_3 = go.Scatter(x=k[0], y=(s*(k[0]**a))/k[0],
                            name = 'sf(k)/k',
                            line = dict(width = 2,
                                        color = 'rgb(229, 151, 50)'))

    fig3 = go.Figure(data = [trace_3], layout = layout3)


    fig3.add_trace(go.Scatter(x=k[0], y=[d+n]*len(k[0]),
                            mode='lines',
                            name='d + n',
                            line = dict(color = 'blue')                            ))
    
    trace_4 = go.Scatter(x=time.iloc[1:,0], y=np.log(time.iloc[3:,2]),
                            name = 'gx',
                            line = dict(width = 2,
                                        color = 'rgb(229, 151, 50)'))

    fig4 = go.Figure(data = [trace_4], layout = layout4)


    fig.add_trace(go.Scatter(x=k[0], y=s*(k[0]**a),
                    mode='lines',
                    name='sf(x)'))
        
    fig.add_trace(go.Scatter(x=k[0], y=(d+n)*(k[0]),
                    mode='lines',
                    name='df(x)'))

    fig.layout.update(
        showlegend=False,
        annotations=[
            go.layout.Annotation(
                x=equal,
                y=0,
                xref="x",
                yref="y",
                text="Eq. inicial",
                arrowwidth=1,
                arrowhead=7,
                showarrow=True,
                ax=0,
                ay=-200
            ),
            go.layout.Annotation(
                x=new_equal,
                y=0,
                xref="x",
                yref="y",
                text="Novo eq.",
                showarrow=True,
                arrowwidth=1,
                arrowhead=7,
                ax=0,
                ay=-230
            )
        ]
    )
    
    return fig, fig2, fig3, fig4
    
server = app.server

    # Step 6. Add the server clause
if __name__ == '__main__':
    app.run_server()

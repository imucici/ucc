import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
app = dash.Dash()
df = pd.read_csv(r'C:\Users\USER\Desktop\tt.csv',encoding='utf-8')

x_name = df['time'].unique()
r1,r2 = [],[]
time_0 = df[df['time']=='馬上']
time_1 = df[df['time']=='一周內']


t0_r1 = time_0[time_0['risk']==1]
t0r1 = t0_r1['money'].sum()
r1.append(t0r1)

t0_r2 = time_0[time_0['risk']==2]   
t0r2 = t0_r2['money'].sum()
r2.append(t0r2)

t1_r1 = time_1[time_1['risk']==1]
t1r1 = t1_r1['money'].sum()
r1.append(t1r1)

t1_r2 = time_1[time_1['risk']==2]
t1r2 = t1_r2['money'].sum()
r2.append(t1r2)




trace1 = go.Bar(
    x=x_name,
    y=r1,
    name='R1'
)
trace2 = go.Bar(
    x=x_name,
    y=r2,
    name='R2'
)

app.layout = html.Div([
    dcc.Graph(id='bar_plot',
              figure=go.Figure(data=[trace1, trace2],
                               layout=go.Layout(barmode='stack'))
              )
    ])

if __name__ == '__main__':
    app.run_server(debug=False,port=8050)
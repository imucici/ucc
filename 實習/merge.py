import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_table
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import math
import dash_daq as daq

# external_stylesheets = ['http://myweb.scu.edu.tw/~06170211/assets/typography.css']

app = dash.Dash(__name__)

colors = {
    'background': '#16243f',
    'background_colheader' : '#1d3267',
    'text': '#3785f2'
}

# fig1
text_1=''' 長條圖 '''

# fig2
df_1 = pd.read_csv('D:/大學資料/大三資料/大三下/福銘/所須csv/table.csv')
text_2 = ''' 表格 '''

# fig3
df_3 = pd.read_csv('D:\大學資料\大三資料\大三下\福銘\所須csv\circle_slider.csv')
text_3 = ''' 泡泡圖 '''
bubble_size = [math.sqrt(p / math.pi) for p in df_3["pop"].values]
df_3['size'] = bubble_size
sizeref = 2*max(df_3['size'])/(100**2)
unique_continents = list(df_3["continent"].unique())

@app.callback(
    Output('fig_3', 'figure'),
    [Input('year-slider', 'value'),
    Input('continent-checklist','value')])

def update_figure(selected_year,selected_continent):
    year_filtered_df = df_3[df_3.year == selected_year]
    filtered_df = year_filtered_df[df_3.continent.isin(selected_continent)]
    traces = []

    for i in filtered_df.continent.unique():
        df_by_continent = filtered_df[filtered_df['continent'] == i]
        traces.append(go.Scatter(
            x=df_by_continent['gdpPercap'],
            y=df_by_continent['lifeExp'],
            text=df_by_continent['country'],
            mode='markers',
            opacity=0.7,
            marker={
                'size': df_3[df_3['continent'] == i]['size'],
                'line': {'width': 1.0, 'color': 'white'},
                'sizeref': sizeref,
                'symbol': 'circle',
                'sizemode': 'area'
            },
            name=i
        ))

    return {
            'data': traces,
            'layout' : go.Layout(
                xaxis={
                    'title':'GDP Per Capita',
                    'gridcolor':'rgb(255, 255, 255)',
                    'gridwidth':1,
                    'type':'log',
                    'color' : 'rgb(55, 133, 242)'
                },
                yaxis={
                    'title':'Life Expectancy',
                    'gridcolor':'rgb(255, 255, 255)',
                    'gridwidth':1,
                    'range':[20, 90],
                    'color' : 'rgb(55, 133, 242)'
                },
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1,'font':{'color':'rgb(55, 133, 242)'}},
                hovermode='closest',
                paper_bgcolor= '#16243f',
                plot_bgcolor='#16243f'
            )
            
    }



# fig4
df_4 = pd.read_csv('D:/大學資料/大三資料/大三下/福銘/所須csv/country_indicators.csv')
text_4 = ''' 散點圖'''
available_indicators = df_4['Indicator Name'].unique()

@app.callback(
    Output('indicator-graphic', 'figure'),
    [Input('xaxis-column', 'value'),
     Input('yaxis-column', 'value'),
     Input('xaxis-type', 'value'),
     Input('yaxis-type', 'value'),
     Input('year--slider', 'value')])
def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type,
                 year_value):
    dff = df_4[df_4['Year'] == year_value]

    fig_4 = px.scatter(x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
                     y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
                     hover_name=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name']
                     ,height = 404)

    fig_4.update_layout(margin={'l': 40, 'b': 40, 't': 15, 'r': 0}, hovermode='closest')

    fig_4.update_xaxes(title=xaxis_column_name, 
                     type='linear' if xaxis_type == 'Linear' else 'log') 

    fig_4.update_yaxes(title=yaxis_column_name, 
                     type='linear' if yaxis_type == 'Linear' else 'log') 
    
    fig_4.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'])

    return fig_4

# fig5
text_5 = '圓餅圖'
df_5 = px.data.gapminder()
available_continent = df_5['continent'].unique()

### 裝飾器和func的參數 之間的順序必須一致!!!!!!!!
@app.callback(
    Output('pie-graphic', 'figure'),
    [Input('continent_type', 'value'),
     Input('year_slider', 'value')])
def update_graph(continent_type,year_slider):
    
    dff = df_5[df_5['year'] == year_slider]
    dff = dff[dff['continent']==continent_type]
    fig = px.pie(dff, values='pop', names='country')## names -> 側邊提示列
    
    #### fig.update_traces()參數 ####

    ## 1. textinfo='' ->  設定pie內顯示的內容(label/percent/value)

    ## 2. hoverinfo='' -> 設定hover時顯示的內容(label/percent/value)

    ## 3. insidetextorientation='' -> 設定pie內顯示內容的排列方向(horizontal/radial/tangential)

    ############
    fig.update_traces(hoverinfo='label+value', textfont_size=12,
                        textposition='inside',textinfo='label+percent',
                        insidetextorientation = 'horizontal',
                        marker=dict(line=dict(color='white', width=2)))
    ############
    
    #### fig.update_layout()參數 ####
    ## 1. uniformtext_minsize -> 設定pie內顯示內容的文字大小統一為xx
    ## 2. uniformtext_mode='hide' -> 若pie空間不夠，textinfo則不顯示
    #######################
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide',
                    margin={'l': 40, 'b': 40, 't': 15, 'r': 0},
                    plot_bgcolor=colors['background'],paper_bgcolor=colors['background'],font_color=colors['text'],
                    height=300,width=630)
    ########################

    return fig
###########################################################################################################

app.layout = html.Div([
    html.Div(
        [
            dcc.Markdown(
                text_1,
                style={
                    'textAlign': 'center',
                    'color': colors['text'],
                    'fontSize' : '21.5px',
                    'fontWeight' : 700,
                }
            ),


            dcc.Tabs([
                dcc.Tab(label='長條圖1',style={'background-color': 'lightblue','font-weight':'bold','height':'50%'}, 
                children=[
                    dcc.Graph(
                        figure={
                            'data': [
                                {'x': [1, 2, 3], 'y': [4, 1, 2],
                                    'type': 'bar', 'name': 'type1','opacity':0.95},
                                {'x': [1, 2, 3], 'y': [2, 4, 5],
                                'type': 'bar', 'name': 'type2','opacity':0.95},
                                
                            ],
                            'layout': go.Layout(

                                xaxis={
                                    'title':'x',
                                    'gridcolor':'rgb(255, 255, 255)',
                                    'gridwidth':1,
                                    'color' : 'rgb(55, 133, 242)'
                                },
                                yaxis={
                                    'title':'y',
                                    'gridcolor':'rgb(255, 255, 255)',
                                    'gridwidth':1,
                                    'color' : 'rgb(55, 133, 242)'
                                },

                                legend={
                                    'x': 1.1, 'y': 1, #坐標軸的位置
                                    'yanchor':"top",
                                    'xanchor' : 'right',
                                    'font':{'color':colors['background_colheader']},
                                    'bgcolor':"LightSteelBlue",
        
                                    'bordercolor':"#1d3267",
                                    'borderwidth':2},

                                hovermode='closest',
                                paper_bgcolor= '#16243f',
                                plot_bgcolor='#16243f',
                                # barmode='stack'

                            )
                        }
                    )
                ]),
                dcc.Tab(label='長條圖2',style={'background-color': 'lightblue','font-weight':'bold'}, children=[
                    dcc.Graph(
                        figure={
                            'data': [
                                {'x': [1, 2, 3], 'y': [1, 4, 1],
                                    'type': 'bar', 'name': 'type1','opacity':0.95},
                                {'x': [1, 2, 3], 'y': [1, 2, 3],
                                'type': 'bar', 'name': 'type2','opacity':0.95},
                            ],
                            'layout': go.Layout(

                                xaxis={
                                    'title':'x',
                                    'gridcolor':'rgb(255, 255, 255)',
                                    'gridwidth':1,
                                    'color' : 'rgb(55, 133, 242)'
                                },
                                yaxis={
                                    'title':'y',
                                    'gridcolor':'rgb(255, 255, 255)',
                                    'gridwidth':1,
                                    'color' : 'rgb(55, 133, 242)'
                                },

                                legend={
                                    'x': 1.1, 'y': 1, #坐標軸的位置
                                    'yanchor':"top",
                                    'xanchor' : 'right',
                                    'font':{'color':colors['background_colheader']},
                                    'bgcolor':"LightSteelBlue",
                                    'bordercolor':"#1d3267",
                                    'borderwidth':2},

                                hovermode='closest',
                                paper_bgcolor= '#16243f',
                                plot_bgcolor='#16243f',
                                # barmode='stack'

                            )
                        }
                    )
                ]),
                dcc.Tab(label='長條圖3',style={'background-color': 'lightblue','font-weight':'bold'}, children=[
                    dcc.Graph(
                        figure={
                            'data': [
                                {'x': [1, 2, 3], 'y': [2, 4, 3],
                                    'type': 'bar', 'name': 'type1','opacity':0.95},
                                {'x': [1, 2, 3], 'y': [5, 4, 3],
                                'type': 'bar', 'name': 'type2','opacity':0.95},
                            ],
                            'layout': go.Layout(

                                xaxis={
                                    'title':'x',
                                    'gridcolor':'rgb(255, 255, 255)',
                                    'gridwidth':1,
                                    'color' : 'rgb(55, 133, 242)'
                                },
                                yaxis={
                                    'title':'y',
                                    'gridcolor':'rgb(255, 255, 255)',
                                    'gridwidth':1,
                                    'color' : 'rgb(55, 133, 242)'
                                },

                                legend={
                                    'x': 1.1, 'y': 1, #坐標軸的位置
                                    'yanchor':"top",
                                    'xanchor' : 'right',
                                    'font':{'color':colors['background_colheader']},
                                    'bgcolor':"LightSteelBlue",
                                    'bordercolor':"#1d3267",
                                    'borderwidth':2},

                                hovermode='closest',
                                paper_bgcolor= '#16243f',
                                plot_bgcolor='#16243f',
                                # barmode='stack'

                            )
                        }
                    )
                ]),
            ])
            
        ],
        style={
            'backgroundColor': colors['background'],
            'height': '540px',
            'width':'800px',
            'display': 'inline-block',
            'position' : 'absolute',
            'top': '0px',
            
            }
    ),

    #################################################
    html.Div([

        dcc.Markdown(
                text_2,
                style={
                    'textAlign': 'center',
                    'color': colors['text'],
                    'fontSize' : '21.5px',
                    'fontWeight' : 700,
                    'backgroundColor': colors['background'],
                    'width':'450px',
                    'top':'0px',
                    'display': 'inline-block'
                }
            ),


        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in df_1.columns],
            data=df_1.to_dict('records'),
            fixed_rows={'headers': True},
            fixed_columns={'headers': True,'data':1},
            # page_size=5, next_page
            style_table={'width':'450px','height': '200px', 'overflowX': 'auto','overflowY': 'auto'},
            style_header={'textAlign':'center','fontWeight': 'bold','backgroundColor': colors['background_colheader']},
            style_cell={
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
                'maxWidth': 0,
                'textAlign':'center',
                'backgroundColor': colors['background'],
                'color': 'white'
            },
            tooltip_data=[
                {
                    column: {'value': str(value), 'type': 'markdown'}
                    for column, value in row.items()
                } for row in df_1.to_dict('rows')
            ],
            tooltip_duration=2000, # 出現多久時間
            # style_cell_conditional=[
            #     {
            #         'if': {'column_id': 'id'},
            #         'textAlign': 'left'
            #     } 
            # ],
            # style_data_conditional=[
            #     {
            #         'if': {'row_index': 'odd'},
            #         'backgroundColor': 'rgb(248, 248, 248)'
            #     }
            # ],
           

        )
    ],
    style={
        'backgroundColor': colors['background'],
        'display': 'inline-block',
        'position' : 'absolute',
        'top': '0px',
        'left' : '800px',
        'margin-left':'8px',
        'overflow': 'hidden',
    }

    
    ),


    #################################################
    html.Div([

        dcc.Markdown(
                text_2,
                style={
                    'textAlign': 'center',
                    'color': colors['text'],
                    'fontSize' : '21.5px',
                    'fontWeight' : '700',
                    'backgroundColor': colors['background'],
                    'width':'450px',
                    'display': 'inline-block'
                }
            ),

        ########## 如果要有篩選功能 就不能加fixed_rows={'headers': True} ########
        dash_table.DataTable(
            id='table_2',
            # columns=[{"name": i, "id": i} for i in df_1.columns],
            data=df_1.to_dict('records'),
            sort_action='native',
            filter_action='native',
            # fixed_rows={'headers': True},
            fixed_columns={'headers': True,'data':1},
            # page_size=5, next_page
            style_table={'width':'450px','height': '200px', 'overflowX': 'auto','overflowY': 'auto'},
            style_header={'textAlign':'center','fontWeight': 'bold','backgroundColor': colors['background_colheader']},

            columns=[
                {'name': 'id', 'id': 'id', 'type': 'text'},
                {'name': 'value', 'id': 'value', 'type': 'numeric'},
                {'name': 'week', 'id': 'week', 'type': 'text'},
                {'name': 'num', 'id': 'num', 'type': 'numeric'},
                {'name': 'bala', 'id': 'bala', 'type': 'text'}
            ],

            style_cell={
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
                'maxWidth': 0,
                'textAlign':'center',
                'backgroundColor': colors['background'],
                'color': 'white',
                
            },
            style_data={
                'width': '80px', 'minWidth': '80px', 'maxWidth': '80px',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
            },
            tooltip_data=[
                {
                    column: {'value': str(value), 'type': 'markdown'}
                    for column, value in row.items()
                } for row in df_1.to_dict('rows')
            ],
            tooltip_duration=2000, # 出現多久時間
            
            style_data_conditional=[
                {
                    'if': {
                        'filter_query': '{value} > 100 && {value} < 400',
                        'column_id': 'value'
                    },
                    'color':'lightgreen',
                    'fontWeight': 'bold'
                    
                },

                {
                    'if': {
                        'filter_query': '{{num}} = {}'.format(df_1['num'].max()),
                        'column_id' : 'num'
                    },
                    'backgroundColor' : '#FF4136',
                    'color' : 'white'

                }
            ],
           

        )
    ],
    style={
        'backgroundColor': colors['background'],
        'display': 'inline-block',
        'position' : 'absolute',
        'left' : '800px',
        'top':'270px',
        'margin-left':'8px',
        'overflow': 'hidden',
    }

    
    ),


    #################################################
    html.Div([

        dcc.Markdown(
            text_3,
                style={
                    'textAlign': 'center',
                    'color': colors['text'],
                    'fontSize' : '21.5px',
                    'fontWeight' : 700
                }
        ),
        dcc.Checklist(
            id="continent-checklist",
            options=[
                {'label': i, 'value': i} for i in unique_continents
            ],
            value=unique_continents,
            style={
            'display': 'flex',
            'align-items' : 'center',
            'color' : 'white'
        },
        ),
        dcc.Graph(
            id='fig_3',
            animate=True
        ),
        dcc.Slider(
            id='year-slider',
            min=df_3['year'].min(),
            max=df_3['year'].max(),
            value=df_3['year'].min(),
            marks={str(year): str(year) for year in df_3['year'].unique()},
            step=None,
            #### daq.Slider
            # handleLabel={"showCurrentValue": True,"label": "YEAR"},
            # size=615, 
        ),
        
    ],
    style={
        'backgroundColor': colors['background'],
        # 'height': '500px',
        'width':'630px',
        'display': 'inline-block',
        'position' : 'absolute',
        'top': '535px'
        }
    
    ),


    #################################################
    html.Div([

        dcc.Markdown(
            text_4,
                style={
                    'textAlign': 'center',
                    'color': colors['text'],
                    'fontSize' : '23px',
                    'fontWeight' : 700
                }
        ),

        html.Div([

            html.Div([
                dcc.Dropdown(
                    id='xaxis-column',
                    options=[{'label': i, 'value': i} for i in available_indicators],
                    value='Fertility rate, total (births per woman)'
                ),
                dcc.RadioItems(
                    id='xaxis-type',
                    options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                    value='Linear',
                    labelStyle={'display': 'inline-block','color':'white'}
                )
            ],
            style={'width': '48%', 'display': 'inline-block'}),

            html.Div([
                dcc.Dropdown(
                    id='yaxis-column',
                    options=[{'label': i, 'value': i} for i in available_indicators],
                    value='Life expectancy at birth, total (years)'
                ),
                dcc.RadioItems(
                    id='yaxis-type',
                    options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                    value='Linear',
                    labelStyle={'display': 'inline-block','color':'white'}
                )
            ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
        ]),

        dcc.Graph(id='indicator-graphic'),

        dcc.Slider(
            id='year--slider',
            min=df_4['Year'].min(),
            max=df_4['Year'].max(),
            value=df_4['Year'].max(),
            marks={str(year): str(year) for year in df_4['Year'].unique()},
            step=None,
            
        ),

    ],

    style={
        'backgroundColor': colors['background'],
        'width':'624px',
        'display': 'inline-block',
        'position' : 'absolute',
        'top': '540px',
        'left': '635px'
        }


    ),

    #################################################
    html.Div([

        dcc.Markdown(
            text_5,
                style={
                    'textAlign': 'center',
                    'color': colors['text'],
                    'fontSize' : '23px',
                    'fontWeight' : 700
                }
        ),

        html.Div([

            html.Div([
                dcc.Dropdown(   
                    id='continent_type',
                    options=[{'label': i, 'value': i} for i in available_continent],
                    value='Asia',
                )
            ],
            style={'width':'200px','display': 'inline-block'}
            ),

            html.Div([
                dcc.Graph(id='pie-graphic'),
            ]), 

            html.Div([
                dcc.Slider(
                    id='year_slider',
                    min=df_5['year'].min(),
                    max=df_5['year'].max(),
                    value=df_5['year'].max(),
                    marks={str(year): str(year) for year in df_5['year'].unique()},
                    step=None,
                    
                ),
            ]),
        
        ],
        style={
                'backgroundColor': colors['background'],
                'width':'630px',
                'display': 'inline-block',
                'position' : 'absolute',
                'position' : 'absolute',
                'top': '1110px'
                }
        )


    ])

    

],

)

if __name__ == '__main__':
    app.run_server(debug=False,port=8050)
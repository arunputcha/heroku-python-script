#!/Users/arunputcha/opt/anaconda3/bin/python3
# coding: utf-8

# In[ ]:


import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
from dash.dependencies import Input, Output

#read data
all_sites_df = pd.read_csv('Alaska_North_Slope_Site_Names_Data.csv')

#Creat a template for the website

def clean_chart_format(fig):
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        annotations=[go.layout.Annotation(
                x=0.9,
                y=1.02,
                showarrow=False,
                #text="Twitter: @_jphwang",
                xref="paper",
                yref="paper",
                textangle=0
            ),
        ],
        font=dict(
            family="Arial, Tahoma, Helvetica",
            size=10,
            color="#404040"
        ),
        margin=dict(
            t=20
        )
    )
    fig.update_traces(marker=dict(line=dict(width=1, color='Navy')), selector=dict(mode='markers'))
    fig.update_coloraxes(colorbar=dict(
            thicknessmode="pixels", thickness=15,
            outlinewidth=1,
            outlinecolor='#909090',
            lenmode="pixels", len=300,
            yanchor="top",
            y=1,
        ))
    fig.update_yaxes(showgrid=True, gridwidth=1, tickson='boundaries', gridcolor='LightGray', fixedrange=True)
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray', fixedrange=True)
    return True


#feeding in data to a function for bar plot

def make_alt_dist_chart(input_df, color_continuous_scale=None,col_col='Alt_in_cm', range_color=None):

    max_bubble_size = 15
    if color_continuous_scale is None:
        color_continuous_scale = px.colors.diverging.RdYlBu_r
    #if range_color is None:
     #   range_color = [min(input_df[col_col]), max(input_df[col_col])]

    fig = px.bar(
        input_df, x='Date', y='Alt_in_cm',
        color=col_col,
        color_continuous_scale=color_continuous_scale,
        #range_color=range_color,
        range_x=[0, len(input_df.Date)],
        range_y=[0, max(input_df.Alt_in_cm)+4],
        #hover_name='Tsur_in_deg_cent', hover_data=['min_start', 'min_end', 'shots_count', 'shots_made', 'shots_freq', 'shots_acc', ],
        #render_mode='svg'
    )
    fig.update_coloraxes(colorbar=dict(title='Range of ALT'))
    #fig.update_traces(marker=dict(sizeref=2. * 10 / (max_bubble_size ** 2)))
    fig.update_yaxes(title="Active Layer Thickness")
    fig.update_xaxes(title='Date', tickvals=list(range(0, 140, 2)))

    return fig

#webapp deployment

app = dash.Dash(__name__)
app.title = 'Permafrost'
server = app.server

team_names = all_sites_df.Site_Name.unique()
team_names.sort()

app.layout = html.Div([html.Div([dcc.Markdown(
    """
    #### Active Layer Thickness across different sites in Alaska from 1995 - 2018
    
    This page contains active layer thickness values in 'cm' for 8 sites in North_Alaska
    from 1995 - 2018.
    
    Use the pulldown to select a site of interest.
    
    """),html.P([html.Small("See more data/Permafrost content, find me on"), html.A(html.Small("Hello"), 
                                                                                    href =  "https://youtube.com/"), 
                                                                                    html.Small("!")])]),
    html.Div([dcc.Dropdown(id = 'group-select',options = [{'label':i, 'value':i} for i in team_names], 
                                  value = 'U32',style = {'width':'140px'})]), 
                      dcc.Graph('shot-dist-graph', config={'displayModeBar': False})])

@app.callback(
    Output('shot-dist-graph', 'figure'),
    [Input('group-select','value')]
)
                       

def update_graph(grpname):
    fig = make_alt_dist_chart(all_sites_df[all_sites_df.Site_Name == grpname], col_col = 'Alt_in_cm')
    clean_chart_format(fig)
    
    if len(grpname) > 3:
        fig.update_layout(height = 850, width = 1250)
    else:
        fig.update_layout(height = 500, width = 1250)
        
    return fig



if __name__ == '__main__':
    app.run_server(debug = False)


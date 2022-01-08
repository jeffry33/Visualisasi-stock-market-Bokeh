# -*- coding: utf-8 -*-
"""Visdat_DataInteraktif_.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XyPXFFdlRblAufH5vJoUVWsxzfhxyOiT

# Preparasi data
"""

import pandas as pd
import bokeh.io
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, NumeralTickFormatter
from bokeh.models import HoverTool
from bokeh.models.widgets import Tabs, Panel
from bokeh.models import ColumnDataSource, CDSView, GroupFilter
from bokeh.layouts import row

df= pd.read_csv("stock_market after edit.csv")
# df

df['Name'].unique()

df['Adj_Close'] = df['Adj Close'].astype(float)
df['Volume'] = df['Volume'].astype(float)
df['Day_Perc_Change'] = df['Day_Perc_Change'].astype(float)
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
# df.dtypes

# df = df[pd.DatetimeIndex(df['Date']).year != 2019]
# df = df[pd.DatetimeIndex(df['Date']).year != 2018]

# df

# Output to file
output_file('visualization-Level-3.html')

df_cds = ColumnDataSource(df)


Hang_view = CDSView(source=df_cds,
                      filters=[GroupFilter(column_name='Name', 
                                          group='NIFTY 50')])

Nikkei_view = CDSView(source=df_cds,
                      filters=[GroupFilter(column_name='Name', 
                                           group='NIKKEI 225')])

Nasdaq_view = CDSView(source=df_cds,
                      filters=[GroupFilter(column_name='Name', 
                                           group='S&P 500')])


common_figure_kwargs = {
    'plot_width': 750,
    'plot_height' : 750,
    'toolbar_location': 'right',
}
common_circle_kwargs = {
    'source': df_cds,
    'size': 7,
    'alpha': 0.7,
}
common_hang_kwargs = {
    'view': Hang_view,
    'color': '#002859',
    'legend': 'Hang Seng'
}
common_nikkei_kwargs = {
    'view': Nikkei_view,
    'color': '#FFC324',
    'legend': 'Nikkei'
}
common_nasdaq_kwargs = {
    'view': Nasdaq_view,
    'color': '#85F781',
    'legend': 'Nasdaq'
}

select_tools = ['box_select', 'lasso_select', 'poly_select', 'tap', 'reset']
fig1 = figure(**common_figure_kwargs,
             x_axis_type='datetime',
             x_axis_label='Tanggal',
             y_axis_label='Adj_Close',
             title='Visualisasi Pasar Saham Berdasar Adj Close',
             tools=select_tools
              )
fig2 = figure(**common_figure_kwargs,
             x_axis_type='datetime',
             x_axis_label='Tanggal',
             y_axis_label='Volume',
             title='Visualisasi Pasar Saham Berdasar Volume ',
             tools=select_tools
              )
fig3 = figure(**common_figure_kwargs,
             x_axis_type='datetime',
             x_axis_label='Tanggal',
             y_axis_label='Presentase perubahan harga',
             title='Visualisasi Pasar Saham Berdasar Presentase Perubahan Harga',
             tools=select_tools
              )

fig1.circle(**common_circle_kwargs, 
           **common_hang_kwargs,
          #  muted_alpha=0.1, 
           x='Date',
           y='Adj_Close',
           nonselection_alpha=0.3
            )
fig1.circle(**common_circle_kwargs, 
           **common_nikkei_kwargs,
          #  muted_alpha=0.1,
           x='Date',
           y='Adj_Close',
           nonselection_alpha=0.3
            )
fig1.circle(**common_circle_kwargs, 
           **common_nasdaq_kwargs,
          #  muted_alpha=0.1,
           x='Date',
           y='Adj_Close',
           nonselection_alpha=0.3
            )
fig1.legend_label.click_policy = 'hide'

fig2.circle(**common_circle_kwargs, 
           **common_hang_kwargs,
          #  muted_alpha=0.1,
           x='Date',
           y='Volume',
           nonselection_alpha=0.3
            )
fig2.circle(**common_circle_kwargs, 
           **common_nikkei_kwargs,
          #  muted_alpha=0.1,
           x='Date',
           y='Volume',
           nonselection_alpha=0.3
            )
fig2.circle(**common_circle_kwargs, 
           **common_nasdaq_kwargs,
          #  muted_alpha=0.1,
           x='Date',
           y='Volume',
           nonselection_alpha=0.3
            )
fig2.legend_label.click_policy = 'hide'

fig3.circle(**common_circle_kwargs, 
           **common_hang_kwargs,
          #  muted_alpha=0.1,
           x='Date',
           y='Day_Perc_Change',
           nonselection_alpha=0.3
            )
fig3.circle(**common_circle_kwargs, 
           **common_nikkei_kwargs,
          #  muted_alpha=0.1,
           x='Date',
           y='Day_Perc_Change',
           nonselection_alpha=0.3
            )
fig3.circle(**common_circle_kwargs, 
           **common_nasdaq_kwargs,
          #  muted_alpha=0.1,
           x='Date',
           y='Day_Perc_Change',
           nonselection_alpha=0.3
            )
fig3.legend_label.click_policy = 'hide'

hover_glyph1 = fig1.circle(x='Date', y='Adj_Close', source=df_cds,
                         size=7, alpha=0,
                         hover_fill_color='black', hover_alpha=0.5)

hover_glyph2 = fig2.circle(x='Date', y='Volume', source=df_cds,
                         size=7, alpha=0,
                         hover_fill_color='green', hover_alpha=0.5)

hover_glyph3 = fig3.circle(x='Date', y='Day_Perc_Change', source=df_cds,
                         size=7, alpha=0,
                         hover_fill_color='black', hover_alpha=0.5)

tooltips =[('Date ','@Date'),
           ('Adj Close ','@Adj_Close'),
           ('Volume ','@Volume'),
           ('Day_Perc_Change ','@Day_Perc_Change'),
           ('Name ','@Name'),   
]
fig1.add_tools(HoverTool(tooltips=tooltips, renderers=[hover_glyph1]))
fig2.add_tools(HoverTool(tooltips=tooltips, renderers=[hover_glyph2]))
fig3.add_tools(HoverTool(tooltips=tooltips, renderers=[hover_glyph3]))

panel1 = Panel(child=fig1, title='Adj Close')
panel2 = Panel(child=fig2, title='Volume')
panel3 = Panel(child=fig3, title='Day Per Change')

tabs = Tabs(tabs=[panel1,panel2,panel3])

show(row(tabs))
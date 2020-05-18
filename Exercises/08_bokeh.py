
import bokeh
import bokeh.io
from bokeh.plotting import figure as bkfig
import pandas as pd
import numpy as np

#######
plot_obj = bkfig(plot_width=400, plot_height=400)
plot_obj.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=15, line_color="navy", fill_color="orange", fill_alpha=0.5)

bokeh.io.show(plot_obj)


#######
datetime_df = pd.DataFrame({'value': np.random.randn(100).cumsum()},
                           index=pd.date_range('2020', freq='D', periods=100))
datetime_df = datetime_df.reset_index()

plot_obj2 = bkfig(x_axis_type="datetime", title="Value as of this year", plot_height=350, plot_width=800)
plot_obj2.xgrid.grid_line_color=None
plot_obj2.ygrid.grid_line_alpha=0.5
plot_obj2.xaxis.axis_label = 'Time'
plot_obj2.yaxis.axis_label = 'Value'

plot_obj2.line(datetime_df.index, datetime_df.value)
bokeh.io.show(plot_obj2)

########
import pandas_bokeh

df_energy = pd.read_csv(r"https://raw.githubusercontent.com/PatrikHlobil/Pandas-Bokeh/master/docs/Testdata/energy/energy.csv", 
parse_dates=["Year"])

df_energy.plot_bokeh.area(
    x="Year",
    stacked=True,
    colormap=["brown", "orange", "black", "grey", "blue", "green"],
    title="Worldwide energy consumption split by energy source",
    ylabel="Million tonnes oil equivalent",
    ylim=(0, 16000)
)

########
import holoviews as hv
hv.extension('bokeh')

scatter = hv.Scatter(df_energy, 'Oil', 'Gas')
scatter + hv.Curve(df_energy, 'Oil', 'Hydroelectricity')

scatter * hv.Curve(df_energy, 'Oil', 'Hydroelectricity')

hv.HoloMap({y: hv.Bars(df_energy.loc[df_energy["Year"] == y, "Coal"]) for y in df_energy["Year"]}, kdims=['Year'])
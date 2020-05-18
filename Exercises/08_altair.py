# https://altair-viz.github.io/
import altair as alt
from vega_datasets import data

cars = data.cars
cars()

cars_url = data.cars.url

brush = alt.selection_interval()  # selection of type 'interval'

alt.Chart(cars_url).mark_point().encode(
    x='Miles_per_Gallon:Q', # qualitative
    y='Horsepower:Q',
    color=alt.condition(brush, 'Origin:N', alt.value('lightgray')) # N: nominal
).add_selection(
    brush
)
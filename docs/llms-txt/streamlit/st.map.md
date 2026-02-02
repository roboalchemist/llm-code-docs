# st.map

Display a map with a scatterplot overlaid onto it.

This is a wrapper around `st.pydeck_chart` to quickly create scatterplot charts on top of a map, with auto-centering and auto-zoom.

When using this command, a service called [Carto](https://carto.com/) provides the map tiles to render map content. If you're using advanced PyDeck features you may need to obtain an API key from Carto first. You can do that as `pydeck.Deck(api_keys={&quot;carto&quot;: YOUR_KEY})` or by setting the CARTO_API_KEY environment variable. See [PyDeck's documentation](https://deckgl.readthedocs.io/en/latest/deck.html) for more information.

Another common provider for map tiles is [Mapbox](https://mapbox.com/). If you prefer to use that, you'll need to create an account at [https://mapbox.com](https://mapbox.com/) and specify your Mapbox key when creating the `pydeck.Deck` object. You can do that as `pydeck.Deck(api_keys={&quot;mapbox&quot;: YOUR_KEY})` or by setting the MAPBOX_API_KEY environment variable.

Carto and Mapbox are third-party products and Streamlit accepts no responsibility or liability of any kind for Carto or Mapbox, or for any content or information made available by Carto or Mapbox. The use of Carto or Mapbox is governed by their respective Terms of Use.

## Example

```python
import time
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(
    rng(0).standard_normal(size=(50, 20)), columns=['col %d' % i for i in range(20)]
)

st.map(df)
```

You can also customize the size and color of the datapoints:

```python
st.map(df, size=20, color="#0044ff")
```

And finally, you can choose different columns to use for the latitude and longitude components, as well as set size and color of each datapoint dynamically based on other columns:

```python
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(
    {
        "col1": rng(0).standard_normal(1000) / 50 + 37.76,
        "col2": rng(1).standard_normal(1000) / 50 + -122.4,
        "col3": rng(2).standard_normal(1000) * 100,
        "col4": rng(3).standard_normal((1000, 4)).tolist(),
    }
)

st.map(df, latitude="col1", longitude="col2", size="col3", color="col4")
```

## Concatenate a dataframe to the bottom of the current one.

```python
import time
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df1 = pd.DataFrame(
    rng(0).standard_normal(size=(50, 20)), columns=['col %d' % i for i in range(20)]
)

df2 = pd.DataFrame(
    rng(1).standard_normal(size=(50, 20)), columns=['col %d' % i for i in range(20)]
)

my_table = st.table(df1)
time.sleep(1)
my_table.add_rows(df2)
```

You can do the same thing with plots. For example, if you want to add more data to a line chart:

```python
# Assuming df1 and df2 from the example above still exist...
my_chart = st.line_chart(df1)
time.sleep(1)
my_chart.add_rows(df2)
```

And for plots whose datasets are named, you can pass the data with a keyword argument where the key is the name:

```python
my_chart = st.vega_lite_chart(
    {
        "mark": "line",
        "encoding": {"x": "a", "y": "b"},
        "datasets": {"some_fancy_name": df1,  # <-- named dataset
        },
        "data": {"name": "some_fancy_name"},
    }
)
my_chart.add_rows(some_fancy_name=df2)  # <-- name used as keyword
```
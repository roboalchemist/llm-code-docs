# st.vega_lite_chart

Display a chart using the Vega-Lite library.

[Vega-Lite](https://vega.github.io/vega-lite/) is a high-level grammar for defining interactive graphics.

## Parameters

- **data**: (Anything supported by st.dataframe)
- **spec**: (dict or None)
- **width**: ("stretch", "content", int, or None)
- **height**: ("content", "stretch", or int)
- **use_container_width**: (bool or None)
- **theme**: ("streamlit" or None)
- **key**: (str)
- **on_select**: ("ignore", "rerun", or callable)
- **selection_mode**: (str or Iterable of str)
- ****kwargs**: any

## Example

```python
import time
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df1 = pd.DataFrame(rng(0).standard_normal(size=(50, 20)), columns=["col %d" % i for i in range(20)])
df2 = pd.DataFrame(rng(1).standard_normal(size=(50, 20)), columns=["col %d" % i for i in range(20)])

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
        "datasets": {
            "some_fancy_name": df1,  # <-- named dataset
        },
        "data": {"name": "some_fancy_name"},
    }
)
my_chart.add_rows(some_fancy_name=df2)  # <-- name used as keyword
```

Try selecting points in this interactive example. When you click a point, the selection will appear under the attribute, "point_selection", which is the name given to the point selection parameter. Similarly, when you make an interval selection, it will appear under the attribute "interval_selection". You can give your selection parameters other names if desired.

If you hold Shift while selecting points, existing point selections will be preserved. Interval selections are not preserved when making additional selections.

## Theming

The Vega-Lite chart is displayed using the Streamlit theme by default. This theme is sleek, user-friendly, and incorporates Streamlit's color palette. The added benefit is that your charts better integrate with the rest of your app's design.

The Streamlit theme is available from Streamlit 1.16.0 through the `theme="streamlit"` keyword argument. To disable it, and use Vega-Lite's native theme, use `theme=None` instead.

Let's look at an example of charts with the Streamlit theme and the native Vega-Lite theme:

```python
import altair as alt
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df1 = pd.DataFrame(rng(0).standard_normal(size=(50, 20)), columns=["col %d" % i for i in range(20)])

df2 = pd.DataFrame(rng(1).standard_normal(size=(50, 20)), columns=["col %d" % i for i in range(20)])

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
        "datasets": {
            "some_fancy_name": df1,  # <-- named dataset
        },
        "data": {"name": "some_fancy_name"},
    }
)
my_chart.add_rows(some_fancy_name=df2)  # <-- name used as keyword
```

Try selecting points in this interactive example. When you click a point, the selection will appear under the attribute, "point_selection", which is the name given to the point selection parameter. Similarly, when you make an interval selection, it will appear under the attribute "interval_selection". You can give your selection parameters other names if desired.

If you hold Shift while selecting points, existing point selections will be preserved. Interval selections are not preserved when making additional selections.

## Theming

The schema for the Vega-Lite event state.

The event state is stored in a dictionary-like object that supports both key and attribute notation. Event states cannot be programmatically changed or set through Session State.

Only selection events are supported at this time.

The Vega-Lite spec for the chart as keywords. This is an alternative to `spec`.

## Example

```python
import time
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df1 = pd.DataFrame(rng(0).standard_normal(size=(50, 20)), columns=["col %d" % i for i in range(20)])

df2 = pd.DataFrame(rng(1).standard_normal(size=(50, 20)), columns=["col %d" % i for i in range(20)])

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
        "datasets": {
            "some_fancy_name": df1,  # <-- named dataset
        },
        "data": {"name": "some_fancy_name"},
    }
)
my_chart.add_rows(some_fancy_name=df2)  # <-- name used as keyword
```

## Theming

The schema for the Vega-Lite event state.

The event state is stored in a dictionary-like object that supports both key and attribute notation. Event states cannot be programmatically changed or set through Session State.

Only selection events are supported at this time.

The Vega-Lite spec for the chart as keywords. This is an alternative to `spec`.

## Example

```python
import time
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df1 = pd.DataFrame(rng(0).standard_normal(size=(50, 20)), columns=["col %d" % i for i in range(20)])

df2 = pd.DataFrame(rng(1).standard_normal(size=(50, 20)), columns=["col %d" % i for i in range(20)])

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
        "datasets": {
            "some_fancy_name": df1,  # <-- named dataset
        },
        "data": {"name": "some_fancy_name"},
    }
)
my_chart.add_rows(some_fancy_name=df2)  # <-- name used as keyword
```
# Source: https://docs.streamlit.io/develop/api-reference/charts/st.scatter_chart

# st.scatter_chart

Display a scatterplot chart.

This is syntax-sugar around `st.altair_chart`. The main difference is this command uses the data's own column and indices to figure out the chart's Altair spec. As a result this is easier to use for many "just plot this" scenarios, while being less customizable.

## Function signature

```jsx
st.scatter_chart(data=None, *, x=None, y=None, x_label=None, y_label=None, color=None, size=None, width="stretch", height="content", use_container_width=None)
```

### Parameters

- **data**: (Anything supported by st.dataframe)
- **x**: (str or None)
- **y**: (str, Sequence of str, or None)
- **x_label**: (str or None)
- **y_label**: (str or None)
- **color**: (str, tuple, Sequence of str, Sequence of tuple, or None)
- **size**: (str, float, int, or None)
- **width**: ("stretch", "content", or int)
- **height**: ("stretch", "content", or int)
- **use_container_width**: (bool or None)

### Example

```jsx
import time
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df1 = pd.DataFrame(rng(0).standard_normal(size=(50, 20)), columns=['col %d' % i for i in range(20)])
df2 = pd.DataFrame(rng(1).standard_normal(size=(50, 20)), columns=['col %d' % i for i in range(20)])

my_table = st.table(df1)
time.sleep(1)
my_table.add_rows(df2)
```

You can do the same thing with plots. For example, if you want to add more data to a line chart:

```jsx
# Assuming df1 and df2 from the example above still exist...
my_chart = st.line_chart(df1)
time.sleep(1)
my_chart.add_rows(df2)
```

And for plots whose datasets are named, you can pass the data with a keyword argument where the key is the name:

```jsx
my_chart = st.vega_lite_chart({
    "mark": "line",
    "encoding": {"x": "a", "y": "b"},
    "datasets": {"some_fancy_name": df1,  # <-- named dataset
    },
    "data": {"name": "some_fancy_name"},
})
my_chart.add_rows(some_fancy_name=df2)  # <-- name used as keyword
```

## Deprecation notice

We plan to deprecate `add_rows()`. Please leave [feedback](https://github.com/streamlit/streamlit/issues/13063).

## Concatenate a dataframe to the bottom of the current one.

```jsx
import time
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df1 = pd.DataFrame(rng(0).standard_normal(size=(50, 20)), columns=['col %d' % i for i in range(20)])
df2 = pd.DataFrame(rng(1).standard_normal(size=(50, 20)), columns=['col %d' % i for i in range(20)])

my_table = st.table(df1)
time.sleep(1)
my_table.add_rows(df2)
```

You can do the same thing with plots. For example, if you want to add more data to a line chart:

```jsx
# Assuming df1 and df2 from the example above still exist...
my_chart = st.line_chart(df1)
time.sleep(1)
my_chart.add_rows(df2)
```

And for plots whose datasets are named, you can pass the data with a keyword argument where the key is the name:

```jsx
my_chart = st.vega_lite_chart({
    "mark": "line",
    "encoding": {"x": "a", "y": "b"},
    "datasets": {"some_fancy_name": df1,  # <-- named dataset
    },
    "data": {"name": "some_fancy_name"},
})
my_chart.add_rows(some_fancy_name=df2)  # <-- name used as keyword
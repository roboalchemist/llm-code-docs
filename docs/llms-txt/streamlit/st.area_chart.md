# st.area_chart

Display an area chart.

This is syntax-sugar around `st.altair_chart`. The main difference is this command uses the data's own column and indices to figure out the chart's Altair spec. As a result this is easier to use for many "just plot this" scenarios, while being less customizable.

## Function signature

```jsx
st.area_chart(data=None, *, x=None, y=None, x_label=None, y_label=None, color=None, stack=None, width="stretch", height="content", use_container_width=None)
```

## Parameters

- **data**: (Anything supported by st.dataframe)
- **x**: (str or None)
- **y**: (str, Sequence of str, or None)
- **x_label**: (str or None)
- **y_label**: (str or None)
- **color**: (str, tuple, Sequence of str, Sequence of tuple, or None)
- **stack**: (bool, "normalize", "center", or None)
- **width**: ("stretch", "content", or int)
- **height**: ("stretch", "content", or int)
- **use_container_width**: (bool or None)

## Example

### Example 1: Basic area chart from a dataframe

If you don't use any of the optional parameters, Streamlit plots each column as a separate area, uses the index as the x values, and labels each series with the column name:

```jsx
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(rng(0).standard_normal((50, 3)), columns=["col1", "col2", "col3"])

st.area_chart(df)
```

### Example 2: Area chart from specific dataframe columns

You can choose different columns to use for the x and y values. If your dataframe is in long format (all y-values in one column), you can set the area colors from another column.

If the column contains color strings, the colors will be applied directly and the series will be unlabeled. If the column contains other values, those values will label each area, and the area colors will be selected from the default color palette. You can configure this color palette in the `theme.chartCategoryColors` configuration option.

```jsx
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(
    {
        "col1": list(range(20)) * 3,
        "col2": rng(0).standard_normal(60),
        "col3": ["a"] * 20 + ["b"] * 20 + ["c"] * 20,
    }
)

st.area_chart(df, x="col1", y="col2", color="col3")
```

### Example 3: Area chart from wide-format dataframe

If your dataframe is in wide format (y-values are in multiple columns), you can pass a list of columns to the `y` parameter. Each column name becomes a series label. To override the default colors, pass a list of colors to the `color` parameter, one for each series. If your areas are overlapping, use colors with some transparency (alpha channel) for the best results.

```jsx
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(
    {
        "col1": list(range(20)),
        "col2": rng(0).standard_normal(20),
        "col3": rng(1).standard_normal(20),
    }
)

st.area_chart(
    df,
    x="col1",
    y=["col2", "col3"],
    color=["#FF000080", "#0000FF80"],
)
```

### Example 4: Area chart with different stacking

You can adjust the stacking behavior by setting `stack`. You can create a streamgraph by setting `stack="center"`:

```jsx
import streamlit as st
from vega_datasets import data

df = data.unemployment_across_industries()

st.area_chart(df, x="date", y="count", color="series", stack="center")
```

## Deprecation notice

We plan to deprecate `add_rows()`. Please leave [feedback](https://github.com/streamlit/streamlit/issues/13063).

## Concatenate a dataframe to the bottom of the current one.

```jsx
import time
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df1 = pd.DataFrame(
    rng(0).standard_normal(size=(50, 20)), columns=["col %d" % i for i in range(20)]
)

df2 = pd.DataFrame(
    rng(1).standard_normal(size=(50, 20)), columns=["col %d" % i for i in range(20)]
)

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
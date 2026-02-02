# st.bar_chart

Display a bar chart.

This is syntax-sugar around `st.altair_chart`. The main difference is this command uses the data's own column and indices to figure out the chart's Altair spec. As a result this is easier to use for many "just plot this" scenarios, while being less customizable.

## Function signature

```jsx
st.bar_chart(data=None, *, x=None, y=None, x_label=None, y_label=None, color=None, horizontal=False, sort=True, stack=None, width="stretch", height="content", use_container_width=None)
```

## Parameters

- **data**: (Anything supported by st.dataframe)
- **x**: (str or None)
- **y**: (str, Sequence of str, or None)
- **x_label**: (str or None)
- **y_label**: (str or None)
- **color**: (str, tuple, Sequence of str, Sequence of tuple, or None)
- **horizontal**: (bool or str)
- **sort**: (bool or str)
- **stack**: (bool, "normalize", "center", "layered", or None)
- **width**: ("stretch", "content", or int)
- **height**: ("stretch", "content", or int)
- **use_container_width**: (bool or None)

## Example

### Example 1: Basic bar chart from a dataframe

If you don't use any of the optional parameters, Streamlit plots each column as a series of bars, uses the index as the x values, and labels each series with the column name:

```jsx
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["col %d" % i for i in range(20)])

st.bar_chart(df)
```

### Example 2: Bar chart from specific dataframe columns

You can choose different columns to use for the x and y values. If your dataframe is in long format (all y-values in one column), you can set the bar colors from another column.

If the column contains color strings, the colors will be applied directly and the series will be unlabeled. If the column contains other values, those values will label each series, and the bar colors will be selected from the default color palette. You can configure this color palette in the `theme.chartCategoryColors` configuration option.

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

st.bar_chart(df, x="col1", y="col2", color="col3")
```

### Example 3: Bar chart from wide-format dataframe

If your dataframe is in wide format (y-values are in multiple columns), you can pass a list of columns to the `y` parameter. Each column name becomes a series label. To override the default colors, pass a list of colors to the `color` parameter, one for each series:

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

st.bar_chart(
    df,
    x="col1",
    y=["col2", "col3"],
    color=["#FF0000", "#0000FF"],
)
```

### Example 4: Horizontal bar chart

You can use the `horizontal` parameter to display horizontal bars instead of vertical bars. This is useful when you have long labels on the x-axis, or when you want to display a large number of categories. This example requires `vega_datasets` to be installed.

```jsx
import streamlit as st
from vega_datasets import data

source = data.barley()

st.bar_chart(source, x="variety", y="yield", color="site", horizontal=True)
```

### Example 5: Unstacked bar chart

You can configure the stacking behavior of the bars by setting the `stack` parameter. Set it to `False` to display bars side by side. This example requires `vega_datasets` to be installed.

```jsx
import streamlit as st
from vega_datasets import data

source = data.barley()

st.bar_chart(source, x="year", y="yield", color="site", stack=False)
```

## Notes

- `add_rows` is deprecated and might be removed in a future version. If you have a specific use-case that requires the `add_rows` functionality, please tell us via this [issue on Github](https://github.com/streamlit/streamlit/issues/13063).

## Version from slug

- `streamlit.bar_chart` is version 1.52.0
- `st.area_chart` is version 1.52.0
- `st.line_chart` is version 1.52.0
- `st.map` is version 1.52.0
- `st.scatter_chart` is version 1.52.0
- `st.altair_chart` is version 1.52.0
- `st.bokeh_chart` is version 1.52.0
- `st.graphviz_chart` is version 1.52.0
- `st.plotly_chart` is version 1.52.0
- `st.pydeck_chart` is version 1.52.0
- `st.pyplot` is version 1.52.0
- `st.vega_lite_chart` is version 1.52.0
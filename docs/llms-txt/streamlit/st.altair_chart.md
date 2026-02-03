# Source: https://docs.streamlit.io/develop/api-reference/charts/st.altair_chart

# st.altair_chart

Display a chart using the Vega-Altair library.

[Vega-Altair](https://altair-viz.github.io/) is a declarative statistical visualization library for Python, based on Vega and Vega-Lite.

## Parameters

- **altair_chart**: (altair.Chart)
  - The Altair chart object to display. See [https://altair-viz.github.io/gallery/](https://altair-viz.github.io/gallery/) for examples of graph descriptions.
- **width**: ("stretch", "content", int, or None)
  - The width of the chart element. This can be one of the following:
    - "stretch": The width of the element matches the width of the parent container.
    - "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
    - An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.
    - None (default): Streamlit uses "stretch" for most charts, and uses "content" for the following multi-view charts:
      - Facet charts: the spec contains "facet" or encodings for "row", "column", or "facet".
      - Horizontal concatenation charts: the spec contains "hconcat".
      - Repeat charts: the spec contains "repeat".
- **height**: ("content", "stretch", or int)
  - The height of the chart element. This can be one of the following:
    - "content" (default): The height of the element matches the height of its content.
    - "stretch": The height of the element matches the height of its content or the height of the parent container, whichever is larger. If the element is not in a parent container, the height of the element matches the height of its content.
    - An integer specifying the height in pixels: The element has a fixed height. If the content is larger than the specified height, scrolling is enabled.
- **use_container_width**: bool or None
  - Whether to override the chart's native width with the width of the parent container. This can be one of the following:
    - None (default): Streamlit will use the parent container's width for all charts except those with known incompatibility (altair.Facet, altair.HConcatChart, and altair.RepeatChart).
    - True: Streamlit sets the width of the chart to match the width of the parent container.
    - False: Streamlit sets the width of the chart to fit its contents according to the plotting library, up to the width of the parent container.
- **theme**: "streamlit" or None
  - The theme of the chart. If theme is "streamlit" (default), Streamlit uses its own design default. If theme is None, Streamlit falls back to the default behavior of the library.
  - The "streamlit" theme can be partially customized through the configuration options theme.chartCategoricalColors and theme.chartSequentialColors. Font configuration options are also applied.
- **key**: str
  - An optional string to use for giving this element a stable identity. If key is None (default), this element's identity will be determined based on the values of the other parameters.
  - Additionally, if selections are activated and key is provided, Streamlit will register the key in Session State to store the selection state. The selection state is read-only.
- **on_select**: "ignore", "rerun", or callable
  - How the figure should respond to user selection events. This controls whether or not the figure behaves like an input widget.
  - If on_select is "ignore" (default), Streamlit will not react to any selection events in the chart. The figure will not behave like an input widget.
  - If on_select is "rerun": Streamlit will rerun the app when the user selects data in the chart. In this case, st.altair_chart will return the selection data as a dictionary.
  - If on_select is a callable: Streamlit will rerun the app and execute the callable as a callback function before the rest of the app. In this case, st.altair_chart will return the selection data as a dictionary.
  - To use selection events, the object passed to altair_chart must include selection parameters. To learn about defining interactions in Altair and how to declare selection-type parameters, see [Interactive Charts](https://altair-viz.github.io/user_guide/interactions.html) in Altair's documentation.
- **selection_mode**: str or Iterable of str
  - The selection parameters Streamlit should use. If selection_mode is None (default), Streamlit will use all selection parameters defined in the chart's Altair spec.
  - When Streamlit uses a selection parameter, selections from that parameter will trigger a rerun and be included in the selection state. When Streamlit does not use a selection parameter, selections from that parameter will not trigger a rerun and not be included in the selection state.
  - Selection parameters are identified by their name property.

## Returns

- If on_select is "ignore" (default), this command returns an internal placeholder for the chart element that can be used with the add_rows() method. Otherwise, this command returns a dictionary-like object that supports both key and attribute notation. The attributes are described by the VegaLiteState dictionary schema.

## Example

```python
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

Try selecting points in this interactive example. When you click a point, the selection will appear under the attribute, "point_selection", which is the name given to the point selection parameter. Similarly, when you make an interval selection, it will appear under the attribute "interval_selection". You can give your selection parameters other names if desired.

If you hold Shift while selecting points, existing point selections will be preserved. Interval selections are not preserved when making additional selections.

## Theming

Altair charts are displayed using the Streamlit theme by default. This theme is sleek, user-friendly, and incorporates Streamlit's color palette. The added benefit is that your charts better integrate with the rest of your app's design.

The Streamlit theme is available from Streamlit 1.16.0 through the `theme="streamlit"` keyword argument. To disable it, and use Altair's native theme, use `theme=None` instead.

Let's look at an example of charts with the Streamlit theme and the native Altair theme:

```python
import altair as alt
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

Try selecting points in this interactive example. When you click a point, the selection will appear under the attribute, "point_selection", which is the name given to the point selection parameter. Similarly, when you make an interval selection, it will appear under the attribute "interval_selection". You can give your selection parameters other names if desired.

If you hold Shift while selecting points, existing point selections will be preserved. Interval selections are not preserved when making additional selections.

## Important

`add_rows` is deprecated and might be removed in a future version. If you have a specific use-case that requires the `add_rows` functionality, please tell us via this [issue on Github](https://github.com/streamlit/streamlit/issues/13063).

## Example

```python
import altair as alt
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
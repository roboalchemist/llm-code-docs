# Source: https://docs.streamlit.io/develop/api-reference/data/st.column_config/st.column_config.barchartcolumn

# st.column_config.BarChartColumn

Configure a bar chart column in `st.dataframe` or `st.data_editor`.

Cells need to contain a list of numbers. Chart columns are not editable at the moment. This command needs to be used in the `column_config` parameter of `st.dataframe` or `st.data_editor`.

## Parameters

- **label**: (str or None)
  - The label shown at the top of the column. If this is `None` (default), the column name is used.

- **width**: ("small", "medium", "large", int, or None)
  - The display width of the column. If this is `None` (default), the column will be sized to fit the cell contents. Otherwise, this can be one of the following:
    - `"small"`: 75px wide
    - `"medium"`: 200px wide
    - `"large"`: 400px wide
    - An integer specifying the width in pixels

  If the total width of all columns is less than the width of the dataframe, the remaining space will be distributed evenly among all columns.

- **help**: (str or None)
  - A tooltip that gets displayed when hovering over the column label. If this is `None` (default), no tooltip is displayed.

  The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the `body` parameter of `st.markdown`.

- **pinned**: (bool or None)
  - Whether the column is pinned. A pinned column will stay visible on the left side no matter where the user scrolls. If this is `None` (default), Streamlit will decide: index columns are pinned, and data columns are not pinned.

- **y_min**: (int, float, or None)
  - The minimum value on the y-axis for all cells in the column. If this is `None` (default), every cell will use the minimum of its data.

- **y_max**: (int, float, or None)
  - The maximum value on the y-axis for all cells in the column. If this is `None` (default), every cell will use the maximum of its data.

- **color**: ("auto", "auto-inverse", str, or None)
  - The color to use for the chart. This can be one of the following:
    - `None` (default): The primary color is used.
    - `"auto"`: If the data is increasing, the chart is green; if the data is decreasing, the chart is red.
    - `"auto-inverse"`: If the data is increasing, the chart is red; if the data is decreasing, the chart is green.
    - A single color value that is applied to all charts in the column. In addition to the basic color palette (red, orange, yellow, green, blue, violet, gray/grey, and primary), this supports hex codes like `#483d8b`.

## Examples

```python
import pandas as pd
import streamlit as st

data_df = pd.DataFrame(
    {
        "sales": [
            [0, 4, 26, 80, 100, 40],
            [80, 20, 80, 35, 40, 100],
            [10, 20, 80, 80, 70, 0],
            [10, 100, 20, 100, 30, 100],
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "sales": st.column_config.BarChartColumn(
            "Sales (last 6 months)",
            help="The sales volume in the last 6 months",
            y_min=0,
            y_max=100,
        ),
    },
    hide_index=True,
)
```

## Additional Information

- [Forum](https://discuss.streamlit.io)
- [Still have questions?](https://docs.streamlit.io/get-started/fundamentals/summary)
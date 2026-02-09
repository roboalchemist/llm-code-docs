# Source: https://docs.streamlit.io/develop/api-reference/data/st.column_config/st.column_config.progresscolumn

# st.column_config.ProgressColumn

Configure a progress column in `st.dataframe` or `st.data_editor`.

Cells need to contain a number. Progress columns are not editable at the moment. This command needs to be used in the `column_config` parameter of `st.dataframe` or `st.data_editor`.

## Parameters

| Parameter | Description |
| --- | --- |
| `label` | The label shown at the top of the column. If this is `None` (default), the column name is used. |
| `width` | The display width of the column. If this is `None` (default), the column will be sized to fit the cell contents. Otherwise, this can be one of the following: <br> - `"small"`: 75px wide <br> - `"medium"`: 200px wide <br> - `"large"`: 400px wide <br> - An integer specifying the width in pixels <br> If the total width of all columns is less than the width of the dataframe, the remaining space will be distributed evenly among all columns. |
| `help` | A tooltip that gets displayed when hovering over the column label. If this is `None` (default), no tooltip is displayed. <br> The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the `body` parameter of `st.markdown`. |
| `format` | A format string controlling how the numbers are displayed. This can be one of the following values: <br> - `None` (default): Streamlit infers the formatting from the data. <br> - `"plain"`: Show the full number without any formatting (e.g. `"1234.567"`). <br> - `"localized"`: Show the number in the default locale format (e.g. `"1,234.567"`). <br> - `"percent"`: Show the number as a percentage (e.g. `"123456.70%"`). <br> - `"dollar"`: Show the number as a dollar amount (e.g. `"$1,234.57"`). <br> - `"euro"`: Show the number as a euro amount (e.g. `"€1,234.57"`). <br> - `"yen"`: Show the number as a yen amount (e.g. `"¥1,235"`). <br> - `"accounting"`: Show the number in an accounting format (e.g. `"1,234.00"`). <br> - `"bytes"`: Show the number in a byte format (e.g. `"1.2KB"`). <br> - `"compact"`: Show the number in a compact format (e.g. `"1.2K"`). <br> - `"scientific"`: Show the number in scientific notation (e.g. `"1.235E3"`). <br> - `"engineering"`: Show the number in engineering notation (e.g. `"1.235E3"`). <br> - printf-style format string: Format the number with a printf specifier, like `"%d"` to show a signed integer (e.g. `"1234"`), or `"%X"` to show an unsigned hexadecimal integer (e.g. `"4D2"`). You can also add prefixes and suffixes. To show British pounds, use `"$ %.2f"` (e.g. `"£ 1234.57"`). For more information, see [sprint-js](https://github.com/alexei/sprintf.js?tab=readme-ov-file#format-specification). |
| `pinned` | Whether the column is pinned. A pinned column will stay visible on the left side no matter where the user scrolls. If this is `None` (default), Streamlit will decide: index columns are pinned, and data columns are not pinned. |
| `min_value` | The minimum value of the progress bar. If this is `None` (default), the minimum will be 0. |
| `max_value` | The maximum value of the progress bar. If this is `None` (default), the maximum will be 100 for integer values and 1.0 for float values. |
| `step` | The precision of numbers. If this is `None` (default), integer columns will have a step of 1 and float columns will have a step of 0.01. Setting `step` for float columns will ensure a consistent number of digits after the decimal are displayed. |
| `color` | The color to use for the chart. This can be one of the following: <br> - `None` (default): The primary color is used. <br> - `"auto"`: If the value is more than half, the bar is green; if the value is less than half, the bar is red. <br> - `"auto-inverse"`: If the value is more than half, the bar is red; if the value is less than half, the bar is green. <br> - A single color value that is applied to all charts in the column. In addition to the basic color palette (red, orange, yellow, green, blue, violet, gray/grey, and primary), this supports hex codes like `"#483d8b"`.

## Examples

```python
import pandas as pd
import streamlit as st

data_df = pd.DataFrame(
    {
        "sales": [200, 550, 1000, 80],
    }
)

st.data_editor(
    data_df,
    column_config={
        "sales": st.column_config.ProgressColumn(
            "Sales volume",
            help="The sales volume in USD",
            format="$%f",
            min_value=0,
            max_value=1000,
        ),
    },
    hide_index=True,
)
```
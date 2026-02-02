# st.column_config.TimeColumn

Configure a time column in `st.dataframe` or `st.data_editor`.

This is the default column type for time values. This command needs to be used in the `column_config` parameter of `st.dataframe` or `st.data_editor`. When used with `st.data_editor`, editing will be enabled with a time picker widget.

## Parameters

| Parameter | Description |
| --- | --- |
| `label` | The label shown at the top of the column. If this is `None` (default), the column name is used. |
| `width` | The display width of the column. If this is `None` (default), the column will be sized to fit the cell contents. Otherwise, this can be one of the following: <br> - `"small"`: 75px wide <br> - `"medium"`: 200px wide <br> - `"large"`: 400px wide <br> - An integer specifying the width in pixels <br> If the total width of all columns is less than the width of the dataframe, the remaining space will be distributed evenly among all columns. |
| `help` | A tooltip that gets displayed when hovering over the column label. If this is `None` (default), no tooltip is displayed. <br> The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the `body` parameter of `st.markdown`. |
| `disabled` | Whether editing should be disabled for this column. If this is `None` (default), Streamlit will enable editing wherever possible. <br> If a column has mixed types, it may become uneditable regardless of `disabled`. |
| `required` | Whether edited cells in the column need to have a value. If this is `False` (default), the user can submit empty values for this column. If this is `True`, an edited cell in this column can only be submitted if its value is not `None`, and a new row will only be submitted after the user fills in this column. |
| `pinned` | Whether the column is pinned. A pinned column will stay visible on the left side no matter where the user scrolls. If this is `None` (default), Streamlit will decide: index columns are pinned, and data columns are not pinned. |
| `default` | Specifies the default value in this column when a new row is added by the user. This defaults to `None`. |
| `format` | A format string controlling how times are displayed. This can be one of the following values: <br> - `None` (default): Show the time in `HH:mm:ss` format (e.g. "20:00:00"). <br> - `"localized"`: Show the time in the default locale format (e.g. "12:00:00 PM" in the America/Los_Angeles timezone). <br> - `"iso8601"`: Show the time in ISO 8601 format (e.g. "20:00:00.000Z"). <br> - A momentJS format string: Format the time with a string, like `"ha"` to show "8pm". For available formats, see [momentJS](https://momentjs.com/docs/#/displaying/format/). <br> Formatting from `column_config` always takes precedence over formatting from `pandas.Styler`. The formatting does not impact the return value when used in `st.data_editor`. |
| `min_value` | The minimum time that can be entered. If this is `None` (default), there will be no minimum. |
| `max_value` | The maximum time that can be entered. If this is `None` (default), there will be no maximum. |
| `step` | The stepping interval in seconds. If this is `None` (default), the step will be 1 second. |

## Examples

```python
from datetime import time
import pandas as pd
import streamlit as st

data_df = pd.DataFrame(
    {
        "appointment": [
            time(12, 30),
            time(18, 0),
            time(9, 10),
            time(16, 25),
        ]
    }
)

st.data_editor(
    data_df,
    column_config={
        "appointment": st.column_config.TimeColumn(
            "Appointment",
            min_value=time(8, 0, 0),
            max_value=time(19, 0, 0),
            format="hh:mm a",
            step=60,
        ),
    },
    hide_index=True,
)
```

## Related Links

- [Previous: Date column](/develop/api-reference/data/st.column_config/st.column_config.datecolumn)
- [Next: JSON column](/develop/api-reference/data/st.column_config/st.column_config.jsoncolumn)

## Forum

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.
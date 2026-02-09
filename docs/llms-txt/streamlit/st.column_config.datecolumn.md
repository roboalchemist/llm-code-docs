# Source: https://docs.streamlit.io/develop/api-reference/data/st.column_config/st.column_config.datecolumn

# st.column_config.DateColumn

Configure a date column in `st.dataframe` or `st.data_editor`.

This is the default column type for date values. This command needs to be used in the `column_config` parameter of `st.dataframe` or `st.data_editor`. When used with `st.data_editor`, editing will be enabled with a date picker widget.

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
| `format` | A format string controlling how dates are displayed. This can be one of the following values: <br> - `None` (default): Show the date in `YYYY-MM-DD` format (e.g. "2025-03-04"). <br> - `"localized"`: Show the date in the default locale format (e.g. "Mar 4, 2025" in the America/Los_Angeles timezone). <br> - `"distance"`: Show the date in a relative format (e.g. "a few seconds ago"). <br> - `"iso8601"`: Show the date in ISO 8601 format (e.g. "2025-03-04"). <br> - A momentJS format string: Format the date with a string, like `ddd, MMM Do` to show "Tue, Mar 4th". For available formats, see [momentJS](https://momentjs.com/docs/#/displaying/format/). <br> Formatting from `column_config` always takes precedence over formatting from `pandas.Styler`. The formatting does not impact the return value when used in `st.data_editor`. |
| `min_value` | The minimum date that can be entered. If this is `None` (default), there will be no minimum. |
| `max_value` | The maximum date that can be entered. If this is `None` (default), there will be no maximum. |
| `step` | The stepping interval in days. If this is `None` (default), the step will be 1 day. |

## Examples

```python
from datetime import date
import pandas as pd
import streamlit as st

data_df = pd.DataFrame(
    {
        "birthday": [
            date(1980, 1, 1),
            date(1990, 5, 3),
            date(1974, 5, 19),
            date(2001, 8, 17),
        ]
    }
)

st.data_editor(
    data_df,
    column_config={
        "birthday": st.column_config.DateColumn(
            "Birthday",
            min_value=date(1900, 1, 1),
            max_value=date(2005, 1, 1),
            format="DD.MM.YYYY",
            step=1,
        ),
    },
    hide_index=True,
)
```

## Related Links

- [Previous: Datetime column](/develop/api-reference/data/st.column_config/st.column_config.datetimecolumn)
- [Next: Time column](/develop/api-reference/data/st.column_config/st.column_config.timecolumn)

## Forum

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.
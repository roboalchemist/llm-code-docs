# st.column_config.JsonColumn

Configure a JSON column in `st.dataframe` or `st.data_editor`.

Cells need to contain JSON strings or JSON-compatible objects. JSON columns are not editable at the moment. This command needs to be used in the `column_config` parameter of `st.dataframe` or `st.data_editor`.

## Function signature

```markdown
st.column_config.JsonColumn(label=None, *, width=None, help=None, pinned=None)
```

## Parameters

- **label** (str or None)
  - The label shown at the top of the column. If this is `None` (default), the column name is used.

- **width** ("small", "medium", "large", int, or None)
  - The display width of the column. If this is `None` (default), the column will be sized to fit the cell contents. Otherwise, this can be one of the following:
    - "small": 75px wide
    - "medium": 200px wide
    - "large": 400px wide
    - An integer specifying the width in pixels

  If the total width of all columns is less than the width of the dataframe, the remaining space will be distributed evenly among all columns.

- **help** (str or None)
  - A tooltip that gets displayed when hovering over the column label. If this is `None` (default), no tooltip is displayed.

  The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the `body` parameter of `st.markdown`.

- **pinned** (bool or None)
  - Whether the column is pinned. A pinned column will stay visible on the left side no matter where the user scrolls. If this is `None` (default), Streamlit will decide: index columns are pinned, and data columns are not pinned.

## Examples

```python
import pandas as pd
import streamlit as st

data_df = pd.DataFrame(
    {
        "json": [
            {"foo": "bar", "bar": "baz"},
            {"foo": "baz", "bar": "qux"},
            {"foo": "qux", "bar": "foo"},
            None,
        ],
    }
)

st.dataframe(
    data_df,
    column_config={
        "json": st.column_config.JsonColumn(
            "JSON Data",
            help="JSON strings or objects",
            width="large",
        ),
    },
    hide_index=True,
)
```

## Additional Information

- [Forum](https://discuss.streamlit.io)
- [Fullscreen open_in_new](https://doc-json-column.streamlit.app//?utm_medium=oembed&)
# Source: https://docs.streamlit.io/develop/api-reference/data/st.table

# st.table

Display a static table.

While `st.dataframe` is geared towards large datasets and interactive data exploration, `st.table` is useful for displaying small, styled tables without sorting or scrolling. For example, `st.table` may be the preferred way to display a confusion matrix or leaderboard. Additionally, `st.table` supports Markdown.

## Function signature

```python
st.table(data=None, *, border=True)
```

### Parameters

- **data**: (Anything supported by st.dataframe)
  - The table data.
  - All cells including the index and column headers can optionally contain GitHub-flavored Markdown. Syntax information can be found at: [https://github.github.com/gfm](https://github.github.com/gfm).
  - See the `body` parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.

- **border**: (bool or "horizontal")
  - Whether to show borders around the table and between cells. This can be one of the following:
    - `True` (default): Show borders around the table and between cells.
    - `False`: Don't show any borders.
    - `"horizontal"`: Show only horizontal borders between rows.

## Examples

### Example 1: Display a confusion matrix as a static table

```python
import pandas as pd
import streamlit as st

confusion_matrix = pd.DataFrame(
    {
        "Predicted Cat": [85, 3, 2, 1],
        "Predicted Dog": [2, 78, 4, 0],
        "Predicted Bird": [1, 5, 72, 3],
        "Predicted Fish": [0, 2, 1, 89],
    },
    index=["Actual Cat", "Actual Dog", "Actual Bird", "Actual Fish"],
)
st.table(confusion_matrix)
```

### Example 2: Display a product leaderboard with Markdown and horizontal borders

```python
import streamlit as st

product_data = {
    "Product": [
        ":material/devices: Widget Pro",
        ":material/smart_toy: Smart Device",
        ":material/inventory: Premium Kit",
    ],
    "Category": [":blue[Electronics]", ":green[IoT]", ":violet[Bundle]"],
    "Stock": ["🟢 Full", "🟡 Low", "🔴 Empty"],
    "Units sold": [1247, 892, 654],
    "Revenue": [125000, 89000, 98000],
}
st.table(product_data, border="horizontal")
```

## Additional Information

- **Deprecated notice**: We plan to deprecate `add_rows()`. Please leave [feedback](https://github.com/streamlit/streamlit/issues/13063).

## Notes

- `add_rows` is deprecated and might be removed in a future version. If you have a specific use-case that requires the `add_rows` functionality, please tell us via this [issue on Github](https://github.com/streamlit/streamlit/issues/13063).

## Version from slug

- `streamlit.table`: Version 1.52.0
- `DeltaGenerator.add_rows`: Version 1.52.0
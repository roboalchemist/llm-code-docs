# Source: https://docs.streamlit.io/develop/api-reference/data/st.column_config/st.column_config.column

# st.column_config.Column

Configure a generic column in `st.dataframe` or `st.data_editor`.

The type of the column will be automatically inferred from the data type. This command needs to be used in the `column_config` parameter of `st.dataframe` or `st.data_editor`.

To change the type of the column and enable type-specific configuration options, use one of the column types in the `st.column_config` namespace, e.g., `st.column_config.NumberColumn`.

## Examples

```python
import pandas as pd
import streamlit as st

data_df = pd.DataFrame(
    {
        "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
    }
)

st.data_editor(
    data_df,
    column_config={
        "widgets": st.column_config.Column(
            "Streamlit Widgets",
            help="Streamlit **widget** commands 🎈",
            width="medium",
            required=True,
        )
    },
    hide_index=True,
    num_rows="dynamic",
)
```

## Attributes

- **label**: The label shown at the top of the column. If this is `None` (default), the column name is used.
- **width**: The display width of the column. If this is `None` (default), the column will be sized to fit the cell contents. Otherwise, this can be one of the following:
  - `"small"`: 75px wide
  - `"medium"`: 200px wide
  - `"large"`: 400px wide
  - An integer specifying the width in pixels
- **help**: A tooltip that gets displayed when hovering over the column label. If this is `None` (default), no tooltip is displayed.
  - The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the `body` parameter of `st.markdown`.
- **disabled**: Whether editing should be disabled for this column. If this is `None` (default), Streamlit will enable editing wherever possible.
  - If a column has mixed types, it may become uneditable regardless of `disabled`.
- **required**: Whether edited cells in the column need to have a value. If this is `False` (default), the user can submit empty values for this column. If this is `True`, an edited cell in this column can only be submitted if its value is not `None`, and a new row will only be submitted after the user fills in this column.
- **pinned**: Whether the column is pinned. A pinned column will stay visible on the left side no matter where the user scrolls. If this is `None` (default), Streamlit will decide: index columns are pinned, and data columns are not pinned.

## Example Usage

```python
import pandas as pd
import streamlit as st

data_df = pd.DataFrame(
    {
        "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
    }
)

st.data_editor(
    data_df,
    column_config={
        "widgets": st.column_config.Column(
            "Streamlit Widgets",
            help="Streamlit **widget** commands 🎈",
            width="medium",
            required=True,
        )
    },
    hide_index=True,
    num_rows="dynamic",
)
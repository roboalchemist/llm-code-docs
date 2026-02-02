# Dataframes

Dataframes are a great way to display and edit data in a tabular format. Working with Pandas DataFrames and other tabular data structures is key to data science workflows. If developers and data scientists want to display this data in Streamlit, they have multiple options: `st.dataframe` and `st.data_editor`. If you want to solely display data in a table-like UI, `st.dataframe` is the way to go. If you want to interactively edit data, use `st.data_editor`.

## Display dataframes with `st.dataframe`

Streamlit can display dataframes in a table-like UI via `st.dataframe`:

```python
import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)

st.dataframe(df, use_container_width=True)
```

## `st.data_editor` UI features

`st.data_editor` provides additional functionality by using `glide-data-grid` under the hood:

- **Column sorting**: To sort columns, select their headers, or select "Sort ascending" or "Sort descending" from the header menu (more_vert).
- **Column resizing**: To resize columns, drag and drop column header borders, or select "Autosize" from the header menu.
- **Column hiding**: To hide columns, select "Hide column" from the header menu.
- **Reorder and pin columns**: To reorder columns or pin them on the left, drag and drop column headers or select "Pin column" from the header menu, respectively.
- **Format numbers, dates, and times**: To change the format of numeric columns, select an option under "Format" in the header menu.
- **Dataframe resizing**: To resize dataframes, drag and drop the bottom right corner.
- **Fullscreen view**: To enlarge dataframes to fullscreen, select the fullscreen icon (fullscreen) in the toolbar.
- **Search**: To search through the data, select the search icon (search) in the toolbar or use hotkeys (⌘+F or Ctrl+F).
- **Download**: To download the data as a CSV file, select the download icon (download) in the toolbar.

## `st.data_editor` UI features

`st.data_editor` also supports a few additional things:

- **Add and delete rows**: You can do this by setting `num_rows="dynamic"` when calling `st.data_editor`. This will allow users to add and delete rows as needed.
- **Copy and paste support**: Copy and paste both between `st.data_editor` and spreadsheet software like Google Sheets and Excel.
- **Access edited data**: Access only the individual edits instead of the entire edited data structure via Session State.
- **Bulk edits**: Similar to Excel, just drag a handle to edit neighboring cells.
- **Automatic input validation**: Column Configuration provides strong data type support and other configurable options. For example, there's no way to enter letters into a number cell. Number cells can have a designated min and max.
- **Edit common data structures**: `st.data_editor` supports lists, dicts, NumPy ndarray, and more!

## `st.data_editor` UI features

### Add and delete rows

With `st.data_editor`, viewers can add or delete rows via the table UI. This mode can be activated by setting `num_rows="dynamic"` when calling `st.data_editor`. This will allow users to add and delete rows as needed.

- To add new rows, click the plus icon (add) in the toolbar. Alternatively, click inside a shaded cell below the bottom row of the table.
- To delete rows, select one or more rows using the checkboxes on the left. Click the delete icon (delete) or press the delete key on your keyboard.

### Copy and paste support

The data editor supports pasting in tabular data from Google Sheets, Excel, Notion, and many other similar tools. You can also copy-paste data between `st.data_editor` instances. This functionality, powered by the `Clipboard API`, can be a huge time saver for users who need to work with data across multiple platforms. To try it out:

- Copy data from this Google Sheets document to your clipboard.
- Single click any cell in the name column in the app above. Paste it in using hotkeys (⌘+V or Ctrl+V).

Every cell of the pasted data will be evaluated individually and inserted into the cells if the data is compatible with the column type. For example, pasting in non-numerical text data into a number column will be ignored.

If you embed your apps with iframes, you'll need to allow the iframe to access the clipboard if you want to use the copy-paste functionality. To do so, give the iframe `allow="clipboard-write;clipboard-read;" ... src="https://your-app-url">` in the iframe.

As developers, ensure the app is served with a valid, trusted certificate when using TLS. If users encounter issues with copying and pasting data, direct them to check if their browser has activated clipboard access permissions for the Streamlit application, either when prompted or through the browser's site settings.

### Access edited data

Sometimes, it is more convenient to know which cells have been changed rather than getting the entire edited dataframe back. Streamlit makes this easy through the use of `Session State`. If a `key` parameter is set, Streamlit will store any changes made to the dataframe in Session State.

This snippet shows how you can access changed data using Session State:

```python
st.data_editor(df, key="my_key", num_rows="dynamic")  # 👈 Set a key
st.write("Here's the value in Session State:")
st.write(st.session_state["my_key"])  # 👈 Show the value in Session State
```

In this code snippet, the `key` parameter is set to `my_key`. After the data editor is created, the value associated to `my_key` in Session State is displayed in the app using `st.write`. This shows the additions, edits, and deletions that were made.

This can be useful when working with large dataframes and you only need to know which cells have changed, rather than access the entire edited dataframe.

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `st.data_editor` UI features

### `
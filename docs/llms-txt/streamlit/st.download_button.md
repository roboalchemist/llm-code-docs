# st.download_button

Display a download button widget.

This is useful when you would like to provide a way for your users to download a file directly from your app.

If you pass the data directly to the `data` parameter, then the data is stored in-memory while the user is connected. It's a good idea to keep file sizes under a couple hundred megabytes to conserve memory or use deferred data generation by passing a callable to the `data` parameter.

If you want to prevent your app from rerunning when a user clicks the download button, wrap the download button in a [fragment](https://docs.streamlit.io/develop/concepts/architecture/fragments).

## Example 1: Download a dataframe as a CSV file

When working with a large dataframe, it's recommended to fetch your data with a cached function. When working with a download button, it's similarly recommended to convert your data into a downloadable format with a cached function. Caching ensures that the app reruns efficiently.

```python
import streamlit as st
import pandas as pd
import numpy as np

# st.cache_data
def get_data():
    df = pd.DataFrame(
        np.random.randn(50, 20), columns=('col %d' % i for i in range(20)))
    return df

# st.cache_data
def convert_for_download(df):
    return df.to_csv().encode("utf-8")

df = get_data()
csv = convert_for_download(df)

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="data.csv",
    mime="text/csv",
    icon=":material/download:",
)
```

## Example 2: Download a string as a text file

If you pass a string to the `data` argument, Streamlit will automatically use the "text/plain" MIME type.

When you have a widget (like a text area) affecting the value of your download, it's recommended to use another button to prepare the download. In this case, use `on_click="ignore"` in your download button to prevent the download button from rerunning your app. This turns the download button into a frontend-only element that can be nested in another button.

Without a preparation button, a user can type something into the text area and immediately click the download button. Because a download is initiated concurrently with the app rerun, this can create a race-like condition where the user doesn't see the updated data in their download.

```python
import streamlit as st

message = st.text_area("Message", value="Lorem ipsum.\\nStreamlit is cool.")

if st.button("Prepare download"):
    st.download_button(
        label="Download text",
        data=message,
        file_name="message.txt",
        on_click="ignore",
        type="primary",
        icon=":material/download:",
    )
```

## Example 3: Download a file

Use a context manager to open and read a local file on your Streamlit server. Pass the `io.BufferedReader` object directly to `data`. Remember to specify the MIME type if you don't want the default type of `application/octet-stream` for generic binary data. In the example below, the MIME type is set to "image/png" for a PNG file.

```python
import streamlit as st

with open("flower.png", "rb") as file:
    st.download_button(
        label="Download image",
        data=file,
        file_name="flower.png",
        mime="image/png",
    )
```

## Example 4: Generate the data on-click with a callable

Pass a callable to `data` to generate the bytes lazily when the user clicks the button. Streamlit commands inside this callable are ignored. The callable can't accept any arguments and must return a file-like object.

```python
import streamlit as st
import time

def make_report():
    time.sleep(1)
    return "col1,col2\\n1,2\\n3,4".encode("utf-8")

st.download_button(
    label="Download report",
    data=make_report,
    file_name="report.csv",
    mime="text/csv",
)
```

## Parameters

| Parameter | Description |
| --- | --- |
| `label` | A short label explaining to the user what this button is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. See the `body` parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives. |
| `data` | The contents of the file to be downloaded or a callable that returns the contents of the file. File contents can be a string, bytes, or file-like object. File-like objects include `io.BytesIO`, `io.StringIO`, or any class that implements the abstract base class `io.RawIOBase`. If a callable is passed, it is executed when the user clicks the download button and runs on a separate thread from the resulting script rerun. This deferred generation is helpful for large files to avoid blocking the page script. The callable can't accept any arguments. If any Streamlit commands are executed inside the callable, they will be ignored. To prevent unnecessary recomputation, use caching when converting your data for download. For more information, see the Example 1 below. |
| `file_name` | An optional string to use as the name of the file to be downloaded, such as "my_file.csv". If not specified, the name will be automatically generated. |
| `mime` | The MIME type of the data. If this is `None` (default), Streamlit sets the MIME type depending on the value of `data` as follows: - If `data` is a string or textual file (i.e. `str` or `io.TextIOWrapper` object), Streamlit uses the "text/plain" MIME type. - If `data` is a binary file or bytes (i.e. `bytes`, `io.BytesIO`, `io.BufferedReader`, or `io.RawIOBase` object), Streamlit uses the "application/octet-stream" MIME type. For more information about MIME types, see [https://www.iana.org/assignments/media-types/media-types.xhtml](https://www.iana.org/assignments/media-types/media-types.xhtml). |
| `key` | An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key. |
| `help` | A tooltip that gets displayed when the button is hovered over. If this is `None` (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the `body` parameter of `st.markdown`. |
| `on_click` | How the button should respond to user interaction. This controls whether or not the button triggers a rerun and if a callback function is called. This can be one of the following values: - `rerun` (default): The user downloads the file and the app reruns. No callback function is called. - `ignore`: The user downloads the file and the app doesn't rerun. No callback function is called. - A `callable`: The user downloads the file and app reruns. The callable is called before the rest of the app. - `None`: This is same as `on_click="rerun"`. This value exists for backwards compatibility and shouldn't be used. |
| `args` | An optional list or tuple of args to pass to the callback. |
| `kwargs` | An optional dict of kwargs to pass to the callback. |
| `type` | An optional string that specifies the button type. This can be one of the following: - `primary`: The button's background is the app's primary color for additional emphasis. - `secondary` (default): The button's background coordinates with the app's background color for normal emphasis. - `tertiary`: The button is plain text without a border or background for subtlety. |
| `icon` | An optional emoji or icon to display next to the button label. If `icon` is `None` (default), no icon is displayed. If `icon` is a string, the following options are valid: - A single-character emoji. For example, you can set `icon="🚨"` or `icon="🔥"`. Emoji short codes are not supported. - An icon from the Material Symbols library (rounded style) in the format `:material/icon_name:` where "icon_name" is the name of the icon in snake case. For example, `icon=":material/thumb_up:"` will display the Thumb Up icon. Find additional icons in the [Material Symbols font library](https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded). - `spinner`: Displays a spinner as an icon. |
| `disabled` | An optional boolean that disables the download button if set to `True`. The default is `False`. |
| `use_container_width` | Whether to expand the button's width to fill its parent container. If `use_container_width` is `False` (default), Streamlit sizes the button to fit its contents. If `use_container_width` is `True`, the width of the button matches its parent container. In both cases, if the contents of the button are wider than the parent container, the contents will line wrap. |
| `width` | The width of the download button. This can be one of the following: - `content`: The width of the button matches the width of its content, but doesn't exceed the width of the parent container. - `stretch`: The width of the button matches the width of the parent container. - An integer specifying the width in pixels: The button has a fixed width. If the specified width is greater than the width of the parent container, the width of the button matches the width of the parent container. |
| `shortcut` | An optional keyboard shortcut that triggers the button. This can be one of the following strings: - A single alphanumeric key like "K" or "4". - A function key like "F11". - A special key like "Enter", "Esc", or "Tab". - Any of the above combined with modifiers. For example, you can use "Ctrl+K" or "Cmd+Shift+O". |

## Returns

| Return | Description |
| --- | --- |
| `bool` | True if the button was clicked on the last run of the app, False otherwise. |

## Examples

### Example 1: Download a dataframe as a CSV file

When working with a large dataframe, it's recommended to fetch your data with a cached function. When working with a download button, it's similarly recommended to convert your data into a downloadable format with a cached function. Caching ensures that the app reruns efficiently.

```python
import streamlit as st
import pandas as pd
import numpy as np

# st.cache_data
def get_data():
    df = pd.DataFrame(
        np.random.randn(50, 20), columns=('col %d' % i for i in range(20)))
    return df

# st.cache_data
def convert_for_download(df):
    return df.to_csv().encode("utf-8")

df = get_data()
csv = convert_for_download(df)

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="data.csv",
    mime="text/csv",
    icon=":material/download:",
)
```

### Example 2: Download a string as a text file

If you pass a string to the `data` argument, Streamlit will automatically use the "text/plain" MIME type.

When you have a widget (like a text area) affecting the value of your download, it's recommended to use another button to prepare the download. In this case, use `on_click="ignore"` in your download button to prevent the download button from rerunning your app. This turns the download button into a frontend-only element that can be nested in another button.

Without a preparation button, a user can type something into the text area and immediately click the download button. Because a download is initiated concurrently with the app rerun, this can create a race-like condition where the user doesn't see the updated data in their download.

```python
import streamlit as st

message = st.text_area("Message", value="Lorem ipsum.\\nStreamlit is cool.")

if st.button("Prepare download"):
    st.download_button(
        label="Download text",
        data=message,
        file_name="message.txt",
        on_click="ignore",
        type="primary",
        icon=":material/download:",
    )
```

### Example 3: Download a file

Use a context manager to open and read a local file on your Streamlit server. Pass the `io.BufferedReader` object directly to `data`. Remember to specify the MIME type if you don't want the default type of `application/octet-stream` for generic binary data. In the example below, the MIME type is set to "image/png" for a PNG file.

```python
import streamlit as st

with open("flower.png", "rb") as file:
    st.download_button(
        label="Download image",
        data=file,
        file_name="flower.png",
        mime="image/png",
    )
```

### Example 4: Generate the data on-click with a callable

Pass a callable to `data` to generate the bytes lazily when the user clicks the button. Streamlit commands inside this callable are ignored. The callable can't accept any arguments and must return a file-like object.

```python
import streamlit as st
import time

def make_report():
    time.sleep(1)
    return "col1,col2\\n1,2\\n3,4".encode("utf-8")

st.download_button(
    label="Download report",
    data=make_report,
    file_name="report.csv",
    mime="text/csv",
)
```
# st.file_uploader

Display a file uploader widget.

By default, uploaded files are limited to 200 MB each. You can configure this using the `server.maxUploadSize` config option. For more information on how to set config options, see [config.toml](https://docs.streamlit.io/develop/api-reference/configuration/config.toml).

## Examples

### Example 1: Accept a single file at a time

```python
import streamlit as st
import pandas as pd
from io import StringIO

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
```

### Example 2: Accept multiple files at a time

```python
import pandas as pd
import streamlit as st

uploaded_files = st.file_uploader(
    "Upload data", accept_multiple_files=True, type="csv"
)
for uploaded_file in uploaded_files:
    df = pd.read_csv(uploaded_file)
    st.write(df)
```

### Example 3: Accept an entire directory

```python
import streamlit as st

uploaded_files = st.file_uploader(
    "Upload images", accept_multiple_files="directory", type=["jpg", "png"]
)
for uploaded_file in uploaded_files:
    st.image(uploaded_file)
```

## Returns

- If `accept_multiple_files` is `False`, returns either `None` or an `UploadedFile` object.
- If `accept_multiple_files` is `True` or `"directory"`, returns a list with the uploaded files as `UploadedFile` objects. If no files were uploaded, returns an empty list.

The `UploadedFile` class is a subclass of `BytesIO`, and therefore is "file-like". This means you can pass an instance of it anywhere a file is expected.

## Notes

This is a best-effort check, but doesn't provide a security guarantee against users uploading files of other types or type extensions. The correct handling of uploaded files is part of the app developer's responsibility.

## Version

Streamlit Version: 1.52.0

## Category

- **Get started**
  - [Installation](/get-started/installation)
  - [Fundamentals](/get-started/fundamentals)
  - [First steps](/get-started/tutorials)

## Subcategories

- **API reference**
  - [Page elements](/develop/api-reference/widgets/st.file_uploader)
  - [Text elements](/develop/api-reference/text)
  - [Data elements](/develop/api-reference/data)
  - [Chart elements](/develop/api-reference/charts)
  - [Input widgets](/develop/api-reference/widgets)
  - [Media elements](/develop/api-reference/media)
  - [Layouts and containers](/develop/api-reference/layout)
  - [Chat elements](/develop/api-reference/chat)
  - [Status elements](/develop/api-reference/status)
  - [Third-party components](https://streamlit.io/components)
  - [Application logic](/develop/api-reference/concepts)
  - [Authentication and user info](/develop/api-reference/user)
  - [Navigation and pages](/develop/api-reference/navigation)
  - [Execution flow](/develop/api-reference/execution-flow)
  - [Caching and state](/develop/api-reference/caching-and-state)
  - [Connections and secrets](/develop/api-reference/connections)
  - [Custom components](/develop/api-reference/custom-components)
  - [Configuration](/develop/api-reference/configuration)
  - [App testing](/develop/api-reference/app-testing)
  - [Command line](/develop/api-reference/cli)

## Additional Resources

- [Forum](https://discuss.streamlit.io)
- [Documentation](https://docs.streamlit.io)
- [GitHub](https://github.com/streamlit/streamlit)
- [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q)
- [Twitter](https://twitter.com/streamlit)
- [LinkedIn](https://www.linkedin.com/company/streamlit)
- [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

## Copyright

© 2025 Snowflake Inc.
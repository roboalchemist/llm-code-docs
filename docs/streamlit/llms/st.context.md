# Source: https://docs.streamlit.io/develop/api-reference/caching-and-state/st.context

# st.context

## Overview

An interface to access user session context.

st.context provides a read-only interface to access headers and cookies for the current user session.

Each property (`st.context.cookies` and `st.context.headers`) returns a dictionary of named values.

## Examples

### Example 1: Access all available cookies

Show a dictionary of cookies:

```python
import streamlit as st

st.context.cookies
```

### Example 2: Access a specific cookie

Show the value of a specific cookie:

```python
import streamlit as st

st.context.cookies["_ga"]
```

## Attributes

- **cookies**: A read-only, dict-like object containing cookies sent in the initial request.
- **headers**: A read-only, dict-like object containing headers (with only the last instance of any repeated key).
- **ip_address**: The read-only IP address of the user's connection.
- **is_embedded**: Whether the app is embedded.
- **locale**: The read-only locale of the user's browser.
- **theme**: A read-only, dictionary-like object containing theme information.
- **timezone**: The read-only timezone of the user's browser.
- **timezone_offset**: The read-only timezone offset of the user's browser.

## Example

Conditionally show content when you access your app through `localhost`:

```python
import streamlit as st

if st.context.url.startswith("http://localhost"):
    st.write("You are running the app locally.")
```

## Notes

Changes made to the background color through CSS are not included. Additionally, the theme type may be incorrect during a change in theme, like in the following situations:

- When the app is first loaded within a session
- When the user changes the theme in the settings menu

For more information and to upvote an improvement, see GitHub issue [#11920](https://github.com/streamlit/streamlit/issues/11920).

## Version

- **Version 1.52.0**
- **Version 1.51.0**
- **Version 1.50.0**
- **Version 1.49.0**
- **Version 1.48.0**
- **Version 1.47.0**
- **Version 1.46.0**
- **Version 1.45.0**
- **Version 1.44.0**
- **Version 1.43.0**
- **Version 1.42.0**
- **Version 1.41.0**
- **Version 1.40.0**
- **Version 1.39.0**
- **Version 1.38.0**
- **Version 1.37.0**
- **Version 1.36.0**
- **Version 1.35.0**
- **Version 1.34.0**
- **Version 1.33.0**
- **Version 1.32.0**
- **Version 1.31.0**
- **Version 1.30.0**
- **Version 1.29.0**
- **Version 1.28.0**
- **Version 1.27.0**
- **Version 1.26.0**
- **Version 1.25.0**
- **Version 1.24.0**
- **Version 1.23.0**
- **Version 1.22.0**

## Additional Resources

- [forum](https://discuss.streamlit.io)
- [Get started](/get-started)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)
- [API reference](/develop/api-reference)
- [Deploy](/deploy)
- [Knowledge base](/knowledge-base)
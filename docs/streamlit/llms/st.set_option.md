# Source: https://docs.streamlit.io/develop/api-reference/configuration/st.set_option

# st.set_option

Set a configuration option.

Currently, only `client` configuration options can be set within the script itself:

> * `client.showErrorDetails`
> * `client.showSidebarNavigation`
> * `client.toolbarMode`

Calling `st.set_option` with any other option will raise a `StreamlitAPIException`. When changing a configuration option in a running app, you may need to trigger a rerun after changing the option to see the effects.

Run `streamlit config show` in a terminal to see all available options.

## Example

```python
import streamlit as st

st.set_option("client.showErrorDetails", True)
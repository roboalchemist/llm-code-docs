# Source: https://docs.streamlit.io/develop/api-reference/configuration/st.get_option

# st.get_option

Return the current value of a given Streamlit configuration option.

Run `streamlit config show` in a terminal to see all available options.

## Function signature

```jsx
st.get_option(key)
```

### Parameters

- **key** (str): The config option key of the form "section.optionName". To see all available options, run `streamlit config show` in a terminal.

## Example

```jsx
import streamlit as st

color = st.get_option("theme.primaryColor")
```

## Version

Streamlit Version

- Version 1.52.0
- Version 1.51.0
- Version 1.50.0
- Version 1.49.0
- Version 1.48.0
- Version 1.47.0
- Version 1.46.0
- Version 1.45.0
- Version 1.44.0
- Version 1.43.0
- Version 1.42.0
- Version 1.41.0
- Version 1.40.0
- Version 1.39.0
- Version 1.38.0
- Version 1.37.0
- Version 1.36.0
- Version 1.35.0
- Version 1.34.0
- Version 1.33.0
- Version 1.32.0
- Version 1.31.0
- Version 1.30.0
- Version 1.29.0
- Version 1.28.0
- Version 1.27.0
- Version 1.26.0
- Version 1.25.0
- Version 1.24.0
- Version 1.23.0
- Version 1.22.0

## Related Links

- [Previous: config.toml](/develop/api-reference/configuration/config.toml)
- [Next: st.set_option](/develop/api-reference/configuration/st.set_option)

## Forum

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

## Copyright

© 2025 Snowflake Inc.
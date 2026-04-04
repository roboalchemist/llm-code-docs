# Source: https://docs.streamlit.io/develop/api-reference/cli

# Command-line options

When you install Streamlit, a command-line (CLI) tool gets installed as well. The purpose of this tool is to run Streamlit apps, change Streamlit configuration options, and help you diagnose and fix issues.

## Available commands

- `streamlit cache clear`: Clear the on-disk cache.
- `streamlit config show`: Show all configuration options.
- `streamlit docs`: Open the Streamlit docs.
- `streamlit hello`: Run an example Streamlit app.
- `streamlit help`: Show the available CLI commands.
- `streamlit init`: Create the files for a new Streamlit app.
- `streamlit run`: Run your Streamlit app.
- `streamlit version`: Show the version of Streamlit.

### Run your app

The most important command is `streamlit run`, which is summarized for convenience here:

```bash
streamlit run your_script.py
```

At any time, in your terminal, you can stop the server with **Ctrl+C**.
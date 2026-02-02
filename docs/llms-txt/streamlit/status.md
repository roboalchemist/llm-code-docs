# Display progress and status

Streamlit provides a few methods that allow you to add animation to your apps. These animations include progress bars, status messages (like warnings), and celebratory balloons.

## Animated status elements

### Progress bar
Display a progress bar.
```python
for i in range(101):
  st.progress(i)
  do_something_slow()
```

### Spinner
Temporarily displays a message while executing a block of code.
```python
with st.spinner("Please wait..."):
  do_something_slow()
```

### Status container
Display output of long-running tasks in a container.
```python
with st.status("Running"):
  do_something_slow()
```

### Toast
Briefly displays a toast message in the bottom-right corner.
```python
st.toast("Butter!", icon='🧈')
```

### Balloons
Display celebratory balloons!
```python
st.balloons()
```

### Snowflakes
Display celebratory snowflakes!
```python
st.snow()
```

## Simple callout messages

### Success box
Display a success message.
```python
st.success("Match found!")
```

### Info box
Display an informational message.
```python
st.info("Dataset is updated every day at midnight.")
```

### Warning box
Display warning message.
```python
st.warning("Unable to fetch image. Skipping...")
```

### Error box
Display error message.
```python
st.error("We encountered an error")
```

### Exception output
Display an exception.
```python
e = RuntimeError("This is an exception of type RuntimeError")
st.exception(e)
```

## Third-party components

### Stqdm
The simplest way to handle a progress bar in streamlit app. Created by @Wirg.
```python
from stqdm import stqdm

for _ in stqdm(range(50)):
    sleep(0.5)
```

### Custom notification box
A custom notification box with the ability to close it out. Created by @Socvest.
```python
from streamlit_custom_notification_box import custom_notification_box

styles = {'material-icons':{'color': 'red'}, 'text-icon-link-close-container': {'box-shadow': '#3896de 0px 4px'}, 'notification-text': {'':''}, 'close-button':{'':''}, 'link':{'':''}}
custom_notification_box(icon='info', textDisplay='We are almost done with your registration...', externalLink='more info', url='#', styles=styles, key='foo')
```

### Streamlit Extras
A library with useful Streamlit extras. Created by @arnaudmiribel.
```python
from streamlit_extras.let_it_rain import rain

rain(emoji='🎈', font_size=54,
  falling_speed=5, animation_length='infinite')
```

## Status elements

### Success box
Display a success message.
```python
st.success("Match found!")
```

### Info box
Display an informational message.
```python
st.info("Dataset is updated every day at midnight.")
```

### Warning box
Display warning message.
```python
st.warning("Unable to fetch image. Skipping...")
```

### Error box
Display error message.
```python
st.error("We encountered an error")
```

### Exception output
Display an exception.
```python
e = RuntimeError("This is an exception of type RuntimeError")
st.exception(e)
```

## Caching and state

### Server
Server configuration.
```python
st.cache_data
st.cache_resource
st.experimental_memo
st.experimental_singleton
st.session_state
st.context
st.query_params
st.experimental_get_query_params
st.experimental_set_query_params
```

## Connections and secrets

### Secrets
Secrets management.
```python
st.secrets
```

### Connections
Connections and secrets management.
```python
st.connection
st.connection
st.experimental_connection
st.experimental_connection
st.experimental_connection
```

## Custom components

### V2 Backend (Python)
V2 Backend (Python) configuration.
```python
st.components.v2.types.bidicomponentcallable
st.components.v2.component
st.components.v2.componentargs
st.components.v2.componentstate
st.components.v2.OptionalComponentCleanupFunction
st.components.v2.st.components.v2.declare_component
st.components.v2.st.components.v2.html
st.components.v2.st.components.v2.iframe
```

### V2 Frontend (TypeScript)
V2 Frontend (TypeScript) configuration.
```python
st.components.st.components.v2.declare_component
st.components.st.components.v2.html
st.components.st.components.v2.iframe
```

### V1 Components
V1 Components configuration.
```python
st.components.st.components.v1.declare_component
st.components.st.components.v1.html
st.components.st.components.v1.iframe
```

## Configuration

### Config.toml
Config.toml configuration.
```python
st.get_option
st.set_option
st.set_page_config
```

## Tools

## App testing

### AppTest
AppTest configuration.
```python
st.testing.v1.apptest
```

## Command line

### Streamlit cache
Streamlit cache command.
```python
st.get_option
st.set_option
st.set_page_config
```

## Tutorials

### Authentication and personalization
Authentication and personalization tutorials.
```python
st.login
st.logout
st.user
```

### Chat and LLM apps
Chat and LLM apps tutorials.
```python
build-conversational-apps
build-an-llm-app-using-langchain
get-chat-response-feedback
validate-and-edit-chat-responses
```

### Configuration and theming
Configuration and theming tutorials.
```python
use-external-font-files
use-external-font-files-streamlit1500
use-static-font-files
use-variable-font-files
```

### Connect to data sources
Connect to data sources tutorials.
```python
aws-s3
bigquery
firestore
google-cloud-storage
microsoft-sql-server
mongodb
mysql
neon
postgresql
private-google-sheet
public-google-sheet
snowflake
supabase
tidb
tigergraph
```

### Elements
Elements tutorials.
```python
annotate-an-altair-chart
dataframe-row-selections
get-dataframe-row-selections
```

### Execution flow
Execution flow tutorials.
```python
trigger-a-full-script-rerun-from-a-fragment
create-a-multiple-container-fragment
start-and-stop-a-streaming-fragment
```

### Multipage apps
Multipage apps tutorials.
```python
dynamic-navigation
build-navigation-with-st.page_link
```

## Quick reference

### Cheat sheet
Cheat sheet.
```python
cheat-sheet
```

### Release notes
Release notes.
```python
2025
2024
2023
2022
2021
2020
2019
```

### Pre-release features
Pre-release features.
```python
prerelease
```

### Roadmap
Roadmap.
```python
https://roadmap.streamlit.app
```
# Source: https://docs.streamlit.io/develop/tutorials/execution-flow

# Source: https://docs.streamlit.io/develop/api-reference/execution-flow

# Execution flow

## Change execution

By default, Streamlit apps execute the script entirely, but we allow some functionality to handle control flow in your applications.

### Modal dialog
Insert a modal dialog that can rerun independently from the rest of the script.

```python
@st.dialog("Sign up")
def email_form():
    name = st.text_input("Name")
    email = st.text_input("Email")
    st.form_submit_button("Sign up")
```

### Fragment
Define a fragment to rerun independently from the rest of the script.

```python
@st.fragment(run_every="10s")
def fragment():
    df = get_data()
    st.line_chart(df)
```

### Rerun script
Rerun the script immediately.

```python
st.rerun()
```

### Stop execution
Stops execution immediately.

```python
st.stop()
```

## Group multiple widgets

By default, Streamlit reruns your script everytime a user interacts with your app. However, sometimes it's a better user experience to wait until a group of related widgets is filled before actually rerunning the script. That's what `st.form` is for!

### Forms
Create a form that batches elements together with a “Submit” button.

```python
with st.form(key='my_form'):
    name = st.text_input("Name")
    email = st.text_input("Email")
    st.form_submit_button("Sign up")
```

### Form submit button
Display a form submit button.

```python
with st.form(key='my_form'):
    name = st.text_input("Name")
    email = st.text_input("Email")
    st.form_submit_button("Sign up")
```

## Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app/)!

### Autorefresh
Force a refresh without tying up a script. Created by [@kmcgrady](https://github.com/kmcgrady).

```python
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=2000, limit=100,
  key="fizzbuzzcounter")
```

### Pydantic
Auto-generate Streamlit UI from Pydantic Models and Dataclasses. Created by [@lukasmasuch](https://github.com/lukasmasuch).

```python
import streamlit_pydantic as sp

sp.pydantic_form(key="my_form",
  model=ExampleModel)
```

### Streamlit Pages
An experimental version of Streamlit Multi-Page Apps. Created by [@blackary](https://github.com/blackary).

```python
from st_pages import Page, show_pages, add_page_title

show_pages([ Page("streamlit_app.py", "Home", "🏠"),
  Page("other_pages/page2.py", "Page 2", ":books:"), ])
```

### Custom components
[![Image 1: screenshot](https://docs.streamlit.io/images/api/components/autorefresh.jpg)](https://github.com/kmcgrady/streamlit-autorefresh)

#### Autorefresh
Force a refresh without tying up a script. Created by [@kmcgrady](https://github.com/kmcgrady).

```python
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=2000, limit=100,
  key="fizzbuzzcounter")
```

### Pydantic
Auto-generate Streamlit UI from Pydantic Models and Dataclasses. Created by [@lukasmasuch](https://github.com/lukasmasuch).

```python
import streamlit_pydantic as sp

sp.pydantic_form(key="my_form",
  model=ExampleModel)
```

### Streamlit Pages
An experimental version of Streamlit Multi-Page Apps. Created by [@blackary](https://github.com/blackary).

```python
from st_pages import Page, show_pages, add_page_title

show_pages([ Page("streamlit_app.py", "Home", "🏠"),
  Page("other_pages/page2.py", "Page 2", ":books:"), ])
```

### Custom components
[![Image 2: screenshot](https://docs.streamlit.io/images/api/components/pages.jpg)](https://github.com/blackary/st_pages)

#### Streamlit Pages
An experimental version of Streamlit Multi-Page Apps. Created by [@blackary](https://github.com/blackary).

```python
from st_pages import Page, show_pages, add_page_title

show_pages([ Page("streamlit_app.py", "Home", "🏠"),
  Page("other_pages/page2.py", "Page 2", ":books:"), ])
```

## App testing

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

### Ask AI

### Release notes

- 2025
- 2024
- 2023
- 2022
- 2021
- 2020
- 2019

### Deployment issues

- How can I deploy multiple Streamlit apps on different subdomains?
- How do I deploy Streamlit on a domain so it appears to run on a regular port (i.e. port 80)?
- Does Streamlit support the WSGI Protocol? (aka Can I deploy Streamlit with gunicorn?)
- How do I increase the upload limit of st.file_uploader on Streamlit Community Cloud?
- How do I share apps with viewers outside my organization?
- How can I make Streamlit watch for changes in other modules I'm importing in my app?
- What browsers does Streamlit support?
- Where does st.file_uploader store uploaded files and when do they get deleted?
- Widget updating for every second input when using session state
- Why does Streamlit restrict nested st.columns?
- What is serializable session state?

### Knowledge base

- How do I create an anchor link?
- Enabling camera access in your browser
- How to download a file in Streamlit?
- How to download a Pandas DataFrame as a CSV?
- How do I upgrade to the latest version of Streamlit?
- How do I insert elements out of order?
- How can I make st.pydeck_chart use custom Mapbox styles?
- How to remove “· Streamlit” from the app title?
- How do you retrieve the filename of a file uploaded with st.file_uploader?
- Sanity checks
- How can I make Streamlit watch for changes in other modules I'm importing in my app?
- What is serializable session state?

### Quick reference

- Cheat sheet
- Release notes
- Pre-release features
- Roadmap

### Deploy

- Concepts
- Streamlit Community Cloud
- Snowflake
- Other platforms

### Knowledge base

- FAQ
- Installing dependencies
- Deployment issues

### Quick reference

- Cheat sheet
- Release notes
- Pre-release features
- Roadmap
# Layouts and Containers

Streamlit provides several options for controlling how different elements are laid out on the screen.

## Complex layouts

Streamlit provides several options for controlling how different elements are laid out on the screen.

### Columns

Insert containers laid out as side-by-side columns.

```python
col1, col2 = st.columns(2)
col1.write("this is column 1")
col2.write("this is column 2")
```

### Container

Insert a multi-element container.

```python
c = st.container()
st.write("This will show last")
c.write("This will show first")
c.write("This will show second")
```

### Modal dialog

Insert a modal dialog that can rerun independently from the rest of the script.

```python
@st.dialog("Sign up")
def email_form():
    name = st.text_input("Name")
    email = st.text_input("Email")
```

### Empty

Insert a single-element container.

```python
c = st.empty()
st.write("This will show last")
c.write("This will be replaced")
c.write("This will show first")
```

### Expander

Insert a multi-element container that can be expanded/collapsed.

```python
with st.expander("Open to see more"):
  st.write("This is more content")
```

### Popover

Insert a multi-element popover container that can be opened/closed.

```python
with st.popover("Settings"):
  st.checkbox("Show completed")
```

### Sidebar

Display items in a sidebar.

```python
st.sidebar.write("This lives in the sidebar")
st.sidebar.button("Click me!")
```

### Space

Add vertical or horizontal space.

```python
st.space("small")
```

### Tabs

Insert containers separated into tabs.

```python
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")
```

## Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app/)!

### Streamlit Elements

Create a draggable and resizable dashboard in Streamlit. Created by [@okls](https://github.com/okls).

```python
from streamlit_elements import elements, mui, html

with elements("new_element"):
  mui.Typography("Hello world")
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

- [Intro to custom components](https://github.com/okld/streamlit-elements)
- [Create a Component](https://github.com/okld/streamlit-elements)
- [Publish a Component](https://github.com/okld/streamlit-elements)
- [Limitations](https://github.com/okld/streamlit-elements)
- [Component gallery](https://github.com/okld/streamlit-elements)

### Configuration and theming

- [Configuration options](https://github.com/okld/streamlit-elements)
- [HTTPS support](https://github.com/okld/streamlit-elements)
- [Serving static files](https://github.com/okld/streamlit-elements)
- [THEMING](https://github.com/okld/streamlit-elements)
- [Customize your theme](https://github.com/okld/streamlit-elements)
- [Customize colors and borders](https://github.com/okld/streamlit-elements)
- [Customize fonts](https://github.com/okld/streamlit-elements)

### App testing

- [Get started](https://github.com/okld/streamlit-elements)
- [Beyond the basics](https://github.com/okld/streamlit-elements)
- [Automate your tests](https://github.com/okld/streamlit-elements)
- [Example](https://github.com/okld/streamlit-elements)
- [Cheat sheet](https://github.com/okld/streamlit-elements)

## Quick reference

### Cheat sheet

- [Cheat sheet](https://docs.streamlit.io/develop/quick-reference/cheat-sheet)

### Release notes

- [2025](https://docs.streamlit.io/develop/quick-reference/release-notes/2025)
- [2024](https://docs.streamlit.io/develop/quick-reference/release-notes/2024)
- [2023](https://docs.streamlit.io/develop/quick-reference/release-notes/2023)
- [2022](https://docs.streamlit.io/develop/quick-reference/release-notes/2022)
- [2021](https://docs.streamlit.io/develop/quick-reference/release-notes/2021)
- [2020](https://docs.streamlit.io/develop/quick-reference/release-notes/2020)
- [2019](https://docs.streamlit.io/develop/quick-reference/release-notes/2019)

### Pre-release features

- [Pre-release features](https://docs.streamlit.io/develop/quick-reference/prerelease)

### Roadmap

- [Roadmap](https://roadmap.streamlit.app/)

## Deployment

### Concepts

- [Concepts](https://docs.streamlit.io/develop/concepts)
- [Architecture and execution](https://docs.streamlit.io/develop/concepts/architecture)
- [Multipage apps](https://docs.streamlit.io/develop/concepts/multipage-apps)
- [App design](https://docs.streamlit.io/develop/concepts/design)
- [ADDITIONAL](https://docs.streamlit.io/develop/concepts/additional-features)
- [Connections, secrets, and authentication](https://docs.streamlit.io/develop/concepts/connections)
- [Custom components](https://docs.streamlit.io/develop/concepts/custom-components)
- [Configuration and theming](https://docs.streamlit.io/develop/concepts/configuration)
- [App testing](https://docs.streamlit.io/develop/concepts/app-testing)

### API reference

- [PAGE ELEMENTS](https://docs.streamlit.io/develop/api-reference/write-magic)
- [Write and magic](https://docs.streamlit.io/develop/api-reference/write-magic)
- [Text elements](https://docs.streamlit.io/develop/api-reference/text)
- [Data elements](https://docs.streamlit.io/develop/api-reference/data)
- [Chart elements](https://docs.streamlit.io/develop/api-reference/charts)
- [Input widgets](https://docs.streamlit.io/develop/api-reference/widgets)
- [Media elements](https://docs.streamlit.io/develop/api-reference/media)
- [Layouts and containers](https://docs.streamlit.io/develop/api-reference/layout)
- [Chat elements](https://docs.streamlit.io/develop/api-reference/chat)
- [Status elements](https://docs.streamlit.io/develop/api-reference/status)
- [Third-party components](https://docs.streamlit.io/develop/api-reference/components)
- [Application logic](https://docs.streamlit.io/develop/api-reference/execution-flow)
- [Authentication and user info](https://docs.streamlit.io/develop/api-reference/user)
- [Navigation and pages](https://docs.streamlit.io/develop/api-reference/navigation)
- [Execution flow](https://docs.streamlit.io/develop/api-reference/execution-flow)
- [Caching and state](https://docs.streamlit.io/develop/api-reference/caching-and-state)
- [Connections and secrets](https://docs.streamlit.io/develop/api-reference/connections)
- [Custom components](https://docs.streamlit.io/develop/api-reference/custom-components)
- [Configuration and theming](https://docs.streamlit.io/develop/api-reference/configuration)
- [App testing](https://docs.streamlit.io/develop/api-reference/app-testing)
- [Command line](https://docs.streamlit.io/develop/api-reference/cli)

## Tutorials

- [Authentication and personalization](https://docs.streamlit.io/develop/tutorials/authentication)
- [Chat and LLM apps](https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps)
- [Configuration and theming](https://docs.streamlit.io/develop/tutorials/configuration-and-theming)
- [Connect to data sources](https://docs.streamlit.io/develop/tutorials/databases)
- [Elements](https://docs.streamlit.io/develop/tutorials/elements)
- [Execution flow](https://docs.streamlit.io/develop/tutorials/execution-flow)
- [Multipage apps](https://docs.streamlit.io/develop/tutorials/multipage)

## Quick reference

- [Cheat sheet](https://docs.streamlit.io/develop/quick-reference/cheat-sheet)
- [Release notes](https://docs.streamlit.io/develop/quick-reference/release-notes)
- [Pre-release features](https://docs.streamlit.io/develop/quick-reference/prerelease)
- [Roadmap](https://docs.streamlit.io/develop/quick-reference/roadmap)
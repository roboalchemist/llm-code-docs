# Source: https://docs.streamlit.io/develop/api-reference/layout/st.tabs

# st.tabs

Insert containers separated into tabs.

Inserts a number of multi-element containers as tabs. Tabs are a navigational element that allows users to easily move between groups of related content.

To add elements to the returned containers, you can use the `with` notation (preferred) or just call methods directly on the returned object. See the examples below.

## Example 1: Use context management

You can use `with` notation to insert any element into a tab:

```python
import streamlit as st

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
```

## Example 2: Call methods directly

You can call methods directly on the returned objects:

```python
import streamlit as st
from numpy.random import default_rng as rng

df = rng(0).standard_normal((10, 1))

tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])

tab1.subheader("A tab with a chart")
tab1.line_chart(df)

tab2.subheader("A tab with the data")
tab2.write(df)
```

## Example 3: Set the default tab and style the tab labels

Use the `default` parameter to set the default tab. You can also use Markdown in the tab labels.

```python
import streamlit as st

tab1, tab2, tab3 = st.tabs(
    [":cat: Cat", ":dog: Dog", ":rainbow[Owl]"], default=":rainbow[Owl]"
)

with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
```
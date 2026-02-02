# st.columns

Insert containers laid out as side-by-side columns.

Inserts a number of multi-element containers laid out side-by-side and returns a list of container objects.

To add elements to the returned containers, you can use the `with` notation (preferred) or just call methods directly on the returned object. See examples below.

## Example 1: Use context management

You can use the `with` statement to insert any element into a column:

```python
import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
```

## Example 2: Use commands as container methods

You can just call methods directly on the returned objects:

```python
import streamlit as st
from numpy.random import default_rng as rng

df = rng(0).standard_normal((10, 1))
col1, col2 = st.columns([3, 1])

col1.subheader("A wide column with a chart")
col1.line_chart(df)

col2.subheader("A narrow column with the data")
col2.write(df)
```

## Example 3: Align widgets

Use `vertical_alignment="bottom"` to align widgets.

```python
import streamlit as st

left, middle, right = st.columns(3, vertical_alignment="bottom")

left.text_input("Write something")
middle.button("Click me", use_container_width=True)
right.checkbox("Check me")
```

## Example 4: Use vertical alignment to create grids

Adjust vertical alignment to customize your grid layouts.

```python
import streamlit as st

vertical_alignment = st.selectbox(
    "Vertical alignment", ["top", "center", "bottom"], index=2
)

left, middle, right = st.columns(3, vertical_alignment=vertical_alignment)
left.image("https://static.streamlit.io/examples/cat.jpg")
middle.image("https://static.streamlit.io/examples/dog.jpg")
right.image("https://static.streamlit.io/examples/owl.jpg")
```

## Example 5: Add borders

Add borders to your columns instead of nested containers for consistent heights.

```python
import streamlit as st

left, middle, right = st.columns(3, border=True)

left.markdown("Lorem ipsum " * 10)
middle.markdown("Lorem ipsum " * 5)
right.markdown("Lorem ipsum ")
```

## Notes

To follow best design practices and maintain a good appearance on all screen sizes, don't nest columns more than once.
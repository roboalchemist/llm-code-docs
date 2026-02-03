# Source: https://docs.streamlit.io/develop/api-reference/layout/st.container

# st.container

Insert a multi-element container.

Inserts an invisible container into your app that can be used to hold multiple elements. This allows you to, for example, insert multiple elements into your app out of order.

To add elements to the returned container, you can use the `with` notation (preferred) or just call commands directly on the returned object. See examples below.

## Example 1: Inserting elements using `with` notation

You can use the `with` statement to insert any element into a container.

```python
import streamlit as st

with st.container():
    st.write("This is inside the container")

    # You can call any Streamlit command, including custom components:
    st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")
```

## Example 2: Inserting elements out of order

When you create a container, its position in the app remains fixed and you can add elements to it at any time. This allows you to insert elements out of order in your app. You can also write to the container by calling commands directly on the container object.

```python
import streamlit as st

container = st.container(border=True)
container.write("This is inside the container")
st.write("This is outside the container")

container.write("This is inside too")
```

## Example 3: Grid layout with columns and containers

You can create a grid with a fixed number of elements per row by using columns and containers.

```python
import streamlit as st

row1 = st.columns(3)
row2 = st.columns(3)

for col in row1 + row2:
    tile = col.container(height=120)
    tile.title(":balloon:")
```

## Example 4: Vertically scrolling container

You can create a vertically scrolling container by setting a fixed height.

```python
import streamlit as st

long_text = "Lorem ipsum. " * 1000

with st.container(height=300):
    st.markdown(long_text)
```

## Example 5: Horizontal container

You can create a row of widgets using a horizontal container. Use `horizontal_alignment` to specify the alignment of the elements inside the container.

```python
import streamlit as st

flex = st.container(horizontal=True, horizontal_alignment="right")

for card in range(3):
    flex.button(f"Button {card + 1}")
```

## Forum

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.
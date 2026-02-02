# st.empty

Insert a single-element container.

Inserts a container into your app that can be used to hold a single element. This allows you to, for example, remove elements at any point, or replace several elements at once (using a child multi-element container).

To insert/replace/clear an element on the returned container, you can use `with` notation or just call methods directly on the returned object. See examples below.

## Examples

Inside a `with st.empty():` block, each displayed element will replace the previous one.

```python
import streamlit as st
import time

with st.empty():
    for seconds in range(10):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.write(":material/check: 10 seconds over!")
st.button("Rerun")
```

You can use an `st.empty` to replace multiple elements in succession. Use `st.container` inside `st.empty` to display (and later replace) a group of elements.

```python
import streamlit as st
import time

st.button("Start over")

placeholder = st.empty()
placeholder.markdown("Hello")
time.sleep(1)

placeholder.progress(0, "Wait for it...")
time.sleep(1)
placeholder.progress(50, "Wait for it...")
time.sleep(1)
placeholder.progress(100, "Wait for it...")
time.sleep(1)

with placeholder.container():
    st.line_chart({"data": [1, 5, 2, 6]})
    time.sleep(1)
    st.markdown("3...")
    time.sleep(1)
    st.markdown("2...")
    time.sleep(1)
    st.markdown("1...")
    time.sleep(1)

placeholder.markdown("Poof!")
time.sleep(1)

placeholder.empty()
```

## Version

Streamlit Version: Version 1.52.0

## Category

PAGE ELEMENTS

## Example

Inside a `with st.empty():` block, each displayed element will replace the previous one.

```python
import streamlit as st
import time

with st.empty():
    for seconds in range(10):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.write(":material/check: 10 seconds over!")
st.button("Rerun")
```

You can use an `st.empty` to replace multiple elements in succession. Use `st.container` inside `st.empty` to display (and later replace) a group of elements.

```python
import streamlit as st
import time

st.button("Start over")

placeholder = st.empty()
placeholder.markdown("Hello")
time.sleep(1)

placeholder.progress(0, "Wait for it...")
time.sleep(1)
placeholder.progress(50, "Wait for it...")
time.sleep(1)
placeholder.progress(100, "Wait for it...")
time.sleep(1)

with placeholder.container():
    st.line_chart({"data": [1, 5, 2, 6]})
    time.sleep(1)
    st.markdown("3...")
    time.sleep(1)
    st.markdown("2...")
    time.sleep(1)
    st.markdown("1...")
    time.sleep(1)

placeholder.markdown("Poof!")
time.sleep(1)

placeholder.empty()
# Source: https://docs.streamlit.io/develop/api-reference/text/st.latex

# st.latex

Display mathematical expressions formatted as LaTeX.

Supported LaTeX functions are listed at [https://katex.org/docs/supported.html](https://katex.org/docs/supported.html).

## Example

```python
import streamlit as st

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k = 
    a \left(\\frac{1-r^{n}}{1-r}\\right)
    ''')
```

## Navigation

- [Previous: st.echo](/develop/api-reference/text/st.echo)
- [Next: st.text](/develop/api-reference/text/st.text)

## Forum

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.
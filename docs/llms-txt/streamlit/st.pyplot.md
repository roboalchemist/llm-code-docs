# st.pyplot

Display a matplotlib.pyplot figure.

## Important

You must install `matplotlib>=3.0.0` to use this command. You can install all charting dependencies (except Bokeh) as an extra with Streamlit:

```bash
pip install streamlit[charts]
```

## Warning

Matplotlib doesn't work well with threads. So if you're using Matplotlib you should wrap your code with locks. This Matplotlib bug is more prominent when you deploy and share your apps because you're more likely to get concurrent users than. The following example uses `TkAgg`:

```python
echo "backend: TkAgg" > ~/.matplotlib/matplotlibrc
```

For more information, see [https://matplotlib.org/faq/usage_faq.html](https://matplotlib.org/faq/usage_faq.html).

## Example

```python
import matplotlib.pyplot as plt
import streamlit as st
from numpy.random import default_rng as rng

arr = rng(0).normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
```

Matplotlib supports several types of "backends". If you're getting an error using Matplotlib with Streamlit, try setting your backend to "TkAgg":

```bash
echo "backend: TkAgg" > ~/.matplotlib/matplotlibrc
```

For more information, see [https://matplotlib.org/faq/usage_faq.html](https://matplotlib.org/faq/usage_faq.html).

## Related Links

- [Previous: st.pydeck_chart](/develop/api-reference/charts/st.pydeck_chart)
- [Next: st.vega_lite_chart](/develop/api-reference/charts/st.vega_lite_chart)

## Forum

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.
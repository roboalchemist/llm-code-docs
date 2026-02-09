# Source: https://docs.streamlit.io/develop/api-reference/charts/st.bokeh_chart

# st.bokeh_chart

Display an interactive Bokeh chart.

Bokeh is a charting library for Python. You can find more about Bokeh at [https://bokeh.pydata.org](https://bokeh.pydata.org).

## Important

This command has been deprecated and removed. Please use our custom component, [streamlit-bokeh](https://github.com/streamlit/streamlit-bokeh), instead. Calling `st.bokeh_chart` will do nothing.

## Function signature

```jsx
st.bokeh_chart(figure, use_container_width=True)
```

## Parameters

- **figure** (bokeh.plotting.figure.Figure)
  - A Bokeh figure to plot.
- **use_container_width** (bool)
  - Whether to override the figure's native width with the width of the parent container. If `use_container_width` is `True` (default), Streamlit sets the width of the figure to match the width of the parent container. If `use_container_width` is `False`, Streamlit sets the width of the chart to fit its contents according to the plotting library, up to the width of the parent container.

## Example

```jsx
import st
import bokeh.plotting as bp

st.bokeh_chart(bp.figure(x='time', y='value'))
```

## Related Links

- [Previous: st.altair_chart](/develop/api-reference/charts/st.altair_chart)
- [Next: st.graphviz_chart](/develop/api-reference/charts/st.graphviz_chart)

## Forum

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.
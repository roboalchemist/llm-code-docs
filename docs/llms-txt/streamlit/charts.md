# Chart elements

Streamlit supports several different charting libraries, and our goal is to continually add support for more. Right now, the most basic library in our arsenal is [Matplotlib](https://matplotlib.org/). Then there are also interactive charting libraries like [Vega Lite](https://vega.github.io/vega-lite/) (2D charts) and [deck.gl](https://github.com/uber/deck.gl) (maps and 3D charts). And finally we also provide a few chart types that are "native" to Streamlit, like `st.line_chart` and `st.area_chart`.

## Simple chart elements

### Simple area charts
Display an area chart.
```python
st.area_chart(my_data_frame)
```

### Simple bar charts
Display a bar chart.
```python
st.bar_chart(my_data_frame)
```

### Simple line charts
Display a line chart.
```python
st.line_chart(my_data_frame)
```

### Simple scatter charts
Display a line chart.
```python
st.scatter_chart(my_data_frame)
```

### Scatterplots on maps
Display a map with points on it.
```python
st.map(my_data_frame)
```

## Advanced chart elements

### Matplotlib
Display a matplotlib.pyplot figure.
```python
st.pyplot(my_mpl_figure)
```

### Altair
Display a chart using the Altair library.
```python
st.altair_chart(my_altair_chart)
```

### Vega-Lite
Display a chart using the Vega-Lite library.
```python
st.vega_lite_chart(my_vega_lite_chart)
```

### Plotly
Display an interactive Plotly chart.
```python
st.plotly_chart(my_plotly_chart)
```

### Bokeh
Display an interactive Bokeh chart.
```python
st.bokeh_chart(my_bokeh_chart)
```

### PyDeck
Display a chart using the PyDeck library.
```python
st.pydeck_chart(my_pydeck_chart)
```

### GraphViz
Display a graph using the dagre-d3 library.
```python
st.graphviz_chart(my_graphviz_spec)
```

### Third-party components
These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app/)!

### Streamlit Lottie
Integrate [Lottie](https://lottiefiles.com/) animations inside your Streamlit app. Created by [@andfanilo](https://github.com/andfanilo).
```python
import plost
plost.line_chart(my_dataframe, x='time', y='stock_value', color='stock_name')
```

### Plotly Events
Make Plotly charts interactive!. Created by [@null-jones](https://github.com/null-jones/).
```python
fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)
```

### Streamlit Folium
Streamlit Component for rendering Folium maps. Created by [@randyzwitch](https://github.com/randyzwitch/).
```python
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
st_data = st_folium(m, width=725)
```

### Spacy-Streamlit
spaCy building blocks and visualizers for Streamlit apps. Created by [@explosion](https://github.com/explosion/).
```python
models = ['en_core_web_sm', 'en_core_web_md']
spacy_streamlit.visualize(models, 'Sundar Pichai is the CEO of Google.')
```

### Streamlit Agraph
A Streamlit Graph Vis, based on [react-grah-vis](https://github.com/crubier/react-graph-vis). Created by [@ChrisDelClea](https://github.com/ChrisDelClea/).
```python
from streamlit_agraph import agraph, Node, Edge, Config
agraph(nodes=nodes, edges=edges, config=config)
```

### Streamlit Lottie
Integrate [Lottie](https://lottiefiles.com/) animations inside your Streamlit app. Created by [@andfanilo](https://github.com/andfanilo/).
```python
lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
st_lottie(lottie_hello, key="hello")
```

### Plotly Events
Make Plotly charts interactive!. Created by [@null-jones](https://github.com/null-jones/).
```python
fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)
```

### Streamlit Folium
Streamlit Component for rendering Folium maps. Created by [@randyzwitch](https://github.com/randyzwitch/).
```python
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
st_data = st_folium(m, width=725)
```

### Spacy-Streamlit
spaCy building blocks and visualizers for Streamlit apps. Created by [@explosion](https://github.com/explosion/).
```python
models = ['en_core_web_sm', 'en_core_web_md']
spacy_streamlit.visualize(models, 'Sundar Pichai is the CEO of Google.')
```

### Streamlit Agraph
A Streamlit Graph Vis, based on [react-grah-vis](https://github.com/crubier/react-graph-vis). Created by [@ChrisDelClea](https://github.com/ChrisDelClea/).
```python
from streamlit_agraph import agraph, Node, Edge, Config
agraph(nodes=nodes, edges=edges, config=config)
```

### Streamlit Lottie
Integrate [Lottie](https://lottiefiles.com/) animations inside your Streamlit app. Created by [@andfanilo](https://github.com/andfanilo/).
```python
lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
st_lottie(lottie_hello, key="hello")
```

## App Testing
Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

## Previous: Data elements
[Previous: Data elements](/develop/api-reference/data)

## Next: st.area_chart
[Next: st.area_chart](/develop/api-reference/charts/st.area_chart)
# Source: https://docs.streamlit.io/develop/api-reference/charts/st.plotly_chart

# st.plotly_chart

Display an interactive Plotly chart.

[Plotly](https://plot.ly/python) is a charting library for Python. The arguments to this function closely follow the ones for Plotly's `plot()` function.

To show Plotly charts in Streamlit, call `st.plotly_chart` wherever you would call Plotly's `py.plot` or `py.iplot`.

## Example 1: Basic Plotly chart

The example below comes from the examples at [https://plot.ly/python](https://plot.ly/python/). Note that `plotly.figure_factory` requires `scipy` to run.

```python
import plotly.figure_factory as ff
import streamlit as st

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length")

event = st.plotly_chart(fig, key="iris", on_select="rerun")

event
```

## Example 2: Plotly Chart with configuration

By default, Plotly charts have scroll zoom enabled. If you have a longer page and want to avoid conflicts between page scrolling and zooming, you can use Plotly's configuration options to disable scroll zoom. In the following example, scroll zoom is disabled, but the zoom buttons are still enabled in the modebar.

```python
import plotly.graph_objects as go
import streamlit as st

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=[1, 2, 3, 4, 5],
        y=[1, 3, 2, 5, 4]
    )
)

st.plotly_chart(fig, config = {'scrollZoom': False})
```

## Theming

Plotly charts are displayed using the Streamlit theme by default. This theme is sleek, user-friendly, and incorporates Streamlit's color palette. The added benefit is that your charts better integrate with the rest of your app's design.

The Streamlit theme is available from Streamlit 1.16.0 through the `theme="streamlit"` keyword argument. To disable it, and use Plotly's native theme, use `theme=None` instead.

Let's look at an example of charts with the Streamlit theme and the native Plotly theme:

```python
import plotly.express as px
import streamlit as st

df = px.data.gapminder()

fig = px.scatter(
    df.query("year==2007"),
    x="sepal_width",
    y="sepal_length",
    color="species",
    size="petal_length",
    hover_data=["petal_width"],
)

event = st.plotly_chart(fig, key="iris", on_select="rerun")

event.selection
```

This is an example of the selection state when selecting a single point:

```json
{
  "points": [
    {
      "curve_number": 2,
      "point_number": 9,
      "point_index": 9,
      "x": 3.6,
      "y": 7.2,
      "customdata": [
        2.5
      ],
      "marker_size": 6.1,
      "legendgroup": "virginica"
    }
  ],
  "point_indices": [
    9
  ],
  "box": [],
  "lasso": []
}
```

The schema for the Plotly chart event state.

The event state is stored in a dictionary-like object that supports both key and attribute notation. Event states cannot be programmatically changed or set through Session State.

Only selection events are supported at this time.

## Notes

## Version From Slug

## Platform From Slug

## Menu

- **Get started**
  - **Installation**
    - LOCAL DEVELOPMENT
    - Use Streamlit Playground
    - Install via command line
    - Install via Anaconda Distribution
    - CLOUD DEVELOPMENT
    - Use GitHub Codespaces
  - **Fundamentals**
    - Basic concepts
    - Advanced concepts
    - Additional features
    - Summary
  - **First steps**
    - Create an app
    - Create a multipage app

- **Develop**
  - **Concepts**
    - CORE
    - Architecture and execution
    - Multipage apps
    - App design
    - ADDITIONAL
    - Connections, secrets, and authentication
    - Custom components
    - Configuration and theming
    - App testing
  - **API reference**
    - PAGE ELEMENTS
    - Write and magic
    - Text elements
    - Data elements
    - Chart elements
    - Input widgets
    - Media elements
    - Layouts and containers
    - Chat elements
    - Status elements
    - Third-party components
    - Application LOGIC
    - Authentication and user info
    - Navigation and pages
    - Execution flow
    - Caching and state
    - Connections and secrets
    - Custom components
    - Configuration
    - TOOLS
    - App testing
    - Command line
  - **Tutorials**
    - Authentication and personalization
    - Chat and LLM apps
    - Configuration and theming
    - Connect to data sources
    - Elements
    - Execution flow
    - Multipage apps
  - **Quick reference**
    - Cheat sheet
    - Release notes
    - Pre-release features
    - Roadmap

## Examples

### Example 1: Basic Plotly chart

The example below comes from the examples at [https://plot.ly/python](https://plot.ly/python/). Note that `plotly.figure_factory` requires `scipy` to run.

```python
import plotly.figure_factory as ff
import streamlit as st

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length")

event = st.plotly_chart(fig, key="iris", on_select="rerun")

event
```

### Example 2: Plotly Chart with configuration

By default, Plotly charts have scroll zoom enabled. If you have a longer page and want to avoid conflicts between page scrolling and zooming, you can use Plotly's configuration options to disable scroll zoom. In the following example, scroll zoom is disabled, but the zoom buttons are still enabled in the modebar.

```python
import plotly.graph_objects as go
import streamlit as st

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=[1, 2, 3, 4, 5],
        y=[1, 3, 2, 5, 4]
    )
)

st.plotly_chart(fig, config = {'scrollZoom': False})
```

### Theming

Plotly charts are displayed using the Streamlit theme by default. This theme is sleek, user-friendly, and incorporates Streamlit's color palette. The added benefit is that your charts better integrate with the rest of your app's design.

The Streamlit theme is available from Streamlit 1.16.0 through the `theme="streamlit"` keyword argument. To disable it, and use Plotly's native theme, use `theme=None` instead.

Let's look at an example of charts with the Streamlit theme and the native Plotly theme:

```python
import plotly.express as px
import streamlit as st

df = px.data.gapminder()

fig = px.scatter(
    df.query("year==2007"),
    x="sepal_width",
    y="sepal_length",
    color="species",
    size="petal_length",
    hover_data=["petal_width"],
)

event = st.plotly_chart(fig, key="iris", on_select="rerun")

event.selection
```

This is an example of the selection state when selecting a single point:

```json
{
  "points": [
    {
      "curve_number": 2,
      "point_number": 9,
      "point_index": 9,
      "x": 3.6,
      "y": 7.2,
      "customdata": [
        2.5
      ],
      "marker_size": 6.1,
      "legendgroup": "virginica"
    }
  ],
  "point_indices": [
    9
  ],
  "box": [],
  "lasso": []
}
```

The schema for the Plotly chart selection state.

The selection state is stored in a dictionary-like object that supports both key and attribute notation. Selection states cannot be programmatically changed or set through Session State.

Only selection events are supported at this time.

## Notes

## Version From Slug

## Platform From Slug

## Menu

- **Get started**
  - **Installation**
    - LOCAL DEVELOPMENT
    - Use Streamlit Playground
    - Install via command line
    - Install via Anaconda Distribution
    - CLOUD DEVELOPMENT
    - Use GitHub Codespaces
  - **Fundamentals**
    - Basic concepts
    - Advanced concepts
    - Additional features
    - Summary
  - **First steps**
    - Create an app
    - Create a multipage app

- **Develop**
  - **Concepts**
    - CORE
    - Architecture and execution
    - Multipage apps
    - App design
    - ADDITIONAL
    - Connections, secrets, and authentication
    - Custom components
    - Configuration and theming
    - App testing
  - **API reference**
    - PAGE ELEMENTS
    - Write and magic
    - Text elements
    - Data elements
    - Chart elements
    - Input widgets
    - Media elements
    - Layouts and containers
    - Chat elements
    - Status elements
    - Third-party components
    - Application LOGIC
    - Authentication and user info
    - Navigation and pages
    - Execution flow
    - Caching and state
    - Connections and secrets
    - Custom components
    - Configuration
    - TOOLS
    - App testing
    - Command line
  - **Tutorials**
    - Authentication and personalization
    - Chat and LLM apps
    - Configuration and theming
    - Connect to data sources
    - Elements
    - Execution flow
    - Multipage apps
  - **Quick reference**
    - Cheat sheet
    - Release notes
    - Pre-release features
    - Roadmap

## Examples

### Example 1: Basic Plotly chart

The example below comes from the examples at [https://plot.ly/python](https://plot.ly/python/). Note that `plotly.figure_factory` requires `scipy` to run.

```python
import plotly.figure_factory as ff
import streamlit as st

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length")

event = st.plotly_chart(fig, key="iris", on_select="rerun")

event
```

### Example 2: Plotly Chart with configuration

By default, Plotly charts have scroll zoom enabled. If you have a longer page and want to avoid conflicts between page scrolling and zooming, you can use Plotly's configuration options to disable scroll zoom. In the following example, scroll zoom is disabled, but the zoom buttons are still enabled in the modebar.

```python
import plotly.graph_objects as go
import streamlit as st

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=[1, 2, 3, 4, 5],
        y=[1, 3, 2, 5, 4]
    )
)

st.plotly_chart(fig, config = {'scrollZoom': False})
```

### Theming

Plotly charts are displayed using the Streamlit theme by default. This theme is sleek, user-friendly, and incorporates Streamlit's color palette. The added benefit is that your charts better integrate with the rest of your app's design.

The Streamlit theme is available from Streamlit 1.16.0 through the `theme="streamlit"` keyword argument. To disable it, and use Plotly's native theme, use `theme=None` instead.

Let's look at an example of charts with the Streamlit theme and the native Plotly theme:

```python
import plotly.express as px
import streamlit as st

df = px.data.gapminder()

fig = px.scatter(
    df.query("year==2007"),
    x="sepal_width",
    y="sepal_length",
    color="species",
    size="petal_length",
    hover_data=["petal_width"],
)

event = st.plotly_chart(fig, key="iris", on_select="rerun")

event.selection
```

This is an example of the selection state when selecting a single point:

```json
{
  "points": [
    {
      "curve_number": 2,
      "point_number": 9,
      "point_index": 9,
      "x": 3.6,
      "y": 7.2,
      "customdata": [
        2.5
      ],
      "marker_size": 6.1,
      "legendgroup": "virginica"
    }
  ],
  "point_indices": [
    9
  ],
  "box": [],
  "lasso": []
}
```

The schema for the Plotly chart selection state.

The selection state is stored in a dictionary-like object that supports both key and attribute notation. Selection states cannot be programmatically changed or set through Session State.

Only selection events are supported at this time.

## Notes

## Version From Slug

## Platform From Slug

## Menu

- **Get started**
  - **Installation**
    - LOCAL DEVELOPMENT
    - Use Streamlit Playground
    - Install via command line
    - Install via Anaconda Distribution
    - CLOUD DEVELOPMENT
    - Use GitHub Codespaces
  - **Fundamentals**
    - Basic concepts
    - Advanced concepts
    - Additional features
    - Summary
  - **First steps**
    - Create an app
    - Create a multipage app

- **Develop**
  - **Concepts**
    - CORE
    - Architecture and execution
    - Multipage apps
    - App design
    - ADDITIONAL
    - Connections, secrets, and authentication
    - Custom components
    - Configuration and theming
    - App testing
  - **API reference**
    - PAGE ELEMENTS
    - Write and magic
    - Text elements
    - Data elements
    - Chart elements
    - Input widgets
    - Media elements
    - Layouts and containers
    - Chat elements
    - Status elements
    - Third-party components
    - Application LOGIC
    - Authentication and user info
    - Navigation and pages
    - Execution flow
    - Caching and state
    - Connections and secrets
    - Custom components
    - Configuration
    - TOOLS
    - App testing
    - Command line
  - **Tutorials**
    - Authentication and personalization
    - Chat and LLM apps
    - Configuration and theming
    - Connect to data sources
    - Elements
    - Execution flow
    - Multipage apps
  - **Quick reference**
    - Cheat sheet
    - Release notes
    - Pre-release features
    - Roadmap

## Examples

### Example 1: Basic Plotly chart

The example below comes from the examples at [https://plot.ly/python](https://plot.ly/python/). Note that `plotly.figure_factory` requires `scipy` to run.

```python
import plotly.figure_factory as ff
import streamlit as st

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length")

event = st.plotly_chart(fig, key="iris", on_select="rerun")

event
```

### Example 2: Plotly Chart with configuration

By default, Plotly charts have scroll zoom enabled. If you have a longer page and want to avoid conflicts between page scrolling and zooming, you can use Plotly's configuration options to disable scroll zoom. In the following example, scroll zoom is disabled, but the zoom buttons are still enabled in the modebar.

```python
import plotly.graph_objects as go
import streamlit as st

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=[1, 2, 3, 4, 5],
        y=[1, 3, 2, 5, 4]
    )
)

st.plotly_chart(fig, config = {'scrollZoom': False})
```

### Theming

Plotly charts are displayed using the Streamlit theme by default. This theme is sleek, user-friendly, and incorporates Streamlit's color palette. The added benefit is that your charts better integrate with the rest of your app's design.

The Streamlit theme is available from Streamlit 1.16.0 through the `theme="streamlit"` keyword argument. To disable it, and use Plotly's native theme, use `theme=None` instead.

Let's look at an example of charts with the Streamlit theme and the native Plotly theme:

```python
import plotly.express as px
import streamlit as st

df = px.data.gapminder()

fig = px.scatter(
    df.query("year==2007"),
    x="sepal_width",
    y="sepal_length",
    color="species",
    size="petal_length",
    hover_data=["petal_width"],
)

event = st.plotly_chart(fig, key="iris", on_select="rerun")

event.selection
```

This is an example of the selection state when selecting a single point:

```json
{
  "points": [
    {
      "curve_number": 2,
      "point_number": 9,
      "point_index": 9,
      "x": 3.6,
      "y": 7.2,
      "customdata": [
        2.5
      ],
      "marker_size": 6.1,
      "legendgroup": "virginica"
    }
  ],
  "point_indices": [
    9
  ],
  "box": [],
  "lasso": []
}
```

The schema for the Plotly chart selection state.

The selection state is stored in a dictionary-like object that supports both key and attribute notation. Selection states cannot be programmatically changed or set through Session State.

Only selection events are supported at this time.

## Notes

## Version From Slug

## Platform From Slug

## Menu

- **Get started**
  - **Installation**
    - LOCAL DEVELOPMENT
    - Use Streamlit Playground
    - Install via command line
    - Install via Anaconda Distribution
    - CLOUD DEVELOPMENT
    - Use GitHub Codespaces
  - **Fundamentals**
    - Basic concepts
    - Advanced concepts
    - Additional features
    - Summary
  - **First steps**
    - Create an app
    - Create a multipage app

- **Develop**
  - **Concepts**
    - CORE
    - Architecture and execution
    - Multipage apps
    - App design
    - ADDITIONAL
    - Connections, secrets, and authentication
    - Custom components
    - Configuration and theming
    - App testing
  - **API reference**
    - PAGE ELEMENTS
    - Write and magic
    - Text elements
    - Data elements
    - Chart elements
    - Input widgets
    - Media elements
    - Layouts and containers
    - Chat elements
    - Status elements
    - Third-party components
    - Application LOGIC
    - Authentication and user info
    - Navigation and pages
    - Execution flow
    - Caching and state
    - Connections and secrets
    - Custom components
    - Configuration
    - TOOLS
    - App testing
    - Command line
  - **Tutorials**
    - Authentication and personalization
    - Chat and LLM apps
    - Configuration and theming
    - Connect to data sources
    - Elements
    - Execution flow
    - Multipage apps
  - **Quick reference**
    - Cheat sheet
    - Release notes
    - Pre-release features
    - Roadmap

## Examples

### Example 1: Basic Plotly chart

The example below comes from the examples at [https://plot.ly/python](https://plot.ly/python/). Note that `plotly.figure_factory` requires `scipy` to run.

```python
import plotly.figure_factory as ff
import streamlit as st

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length")

event = st.plotly_chart(fig, key="iris", on_select="rerun")

event
```

### Example 2: Plotly Chart with configuration

By default, Plotly charts have scroll zoom enabled. If you have a longer page and want to avoid conflicts between page scrolling and zooming, you can use Plotly's configuration options to disable scroll zoom. In the following example, scroll zoom is disabled, but the zoom buttons are still enabled in the modebar.

```python
import plotly.graph_objects as go
import streamlit as st

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=[1, 2, 3, 4, 5],
        y=[1, 3, 2, 5, 4]
    )
)

st.plotly_chart(fig, config = {'scrollZoom': False})
```

### Theming

Plotly charts are displayed using the Streamlit theme by default. This theme is sleek, user-friendly, and incorporates Streamlit's color palette. The added benefit is that your charts better integrate with the rest of your app's design.

The Streamlit theme is available from Streamlit 1.16.0 through the `theme="streamlit"` keyword argument. To disable it, and use Plotly's native theme, use `theme=None` instead.

Let's look at an example of charts with the Streamlit theme and the native Plotly theme:

```python
import plotly.express as px
import streamlit as st

df = px.data.gapminder()

fig = px.scatter(
    df.query("year==2007"),
    x="sepal_width",
    y="sepal_length",
    color="species",
    size="petal_length",
    hover_data=["petal_width"],
)

event = st.plotly_chart(fig, key="iris", on_select="rerun")

event.selection
```

This is an example of the selection state when selecting a single point:

```json
{
  "points": [
    {
      "curve_number": 2,
      "point_number": 9,
      "point_index": 9,
      "x": 3.6,
      "y": 7.2,
      "customdata": [
        2.5
      ],
      "marker_size": 6.1,
      "legendgroup": "virginica"
    }
  ],
  "point_indices": [
    9
  ],
  "box": [],
  "lasso": []
}
```

The schema for the Plotly chart selection state.

The selection state is stored in a dictionary-like object that supports both key and attribute notation. Selection states cannot be programmatically changed or set through Session State.

Only selection events are supported at this time.

## Notes

## Version From Slug

## Platform From Slug

## Menu

- **Get started**
  - **Installation**
    - LOCAL DEVELOPMENT
    - Use Streamlit Playground
    - Install via command line
    - Install via Anaconda Distribution
    - CLOUD DEVELOPMENT
    - Use GitHub Codespaces
  - **Fundamentals**
    - Basic concepts
    - Advanced concepts
    - Additional features
    - Summary
  - **First steps**
    - Create an app
    - Create a multipage app

- **Develop**
  - **Concepts**
    - CORE
    - Architecture and execution
    - Multipage apps
    - App design
    - ADDITIONAL
    - Connections, secrets, and authentication
    - Custom components
    - Configuration and theming
    - App testing
  - **API reference**
    - PAGE ELEMENTS
    - Write and magic
    - Text elements
    - Data elements
    - Chart elements
    - Input widgets
    - Media elements
    - Layouts and containers
    - Chat elements
    - Status elements
    - Third-party components
    - Application LOGIC
    - Authentication and user info
    - Navigation and pages
    - Execution flow
    - Caching and state
    - Connections and secrets
    - Custom components
    - Configuration
    - TOOLS
    - App testing
    - Command line
  - **Tutorials**
    - Authentication and personalization
    - Chat and LLM apps
    - Configuration and theming
    - Connect to data sources
    - Elements
    - Execution flow
    - Multipage apps
  - **Quick reference**
    - Cheat sheet
    - Release notes
    - Pre-release features
    - Roadmap

## Examples

### Example 1: Basic Plotly chart

The example below comes from the examples at [https://plot.ly/python](https://plot.ly/python/). Note that `plotly.figure_factory` requires `scipy` to run.

```python
import plotly.figure_factory as ff
import streamlit as st

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length")

event = st.plotly_chart(fig, key="iris", on_select="rerun")

event
```

### Example 2: Plotly Chart with configuration

By default, Plotly charts have scroll zoom enabled. If you have a longer page and want to avoid conflicts between page scrolling and zooming, you can use Plotly's configuration options to disable scroll zoom. In the following example, scroll zoom is disabled, but the zoom buttons are still enabled in the modebar.

```python
import plotly.graph_objects as go
import streamlit as st

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=[1, 2, 3, 4, 5],
        y=[1, 3, 2, 5, 4]
    )
)

st.plotly_chart(fig, config = {'scrollZoom': False})
```

### Theming

Plotly charts are displayed using the Streamlit theme by default. This theme is sleek, user-friendly, and incorporates Streamlit's color palette. The added benefit is that your charts better integrate with the rest of your app's design.

The Streamlit theme is available from Streamlit 1.16.0 through the `theme="streamlit"` keyword argument. To disable it, and use Plotly's native theme, use `theme=None` instead.

Let's look at an example of charts with the Streamlit theme and the native Plotly theme:

```python
import plotly.express as px
import streamlit as st

df = px.data.gapminder()

fig = px.scatter(
    df.query("year==2007"),
    x="sepal_width",
    y="sepal_length",
    color="species",
    size="petal_length",
    hover_data=["petal_width"],
)

event = st.plotly_chart(fig, key="iris", on_select="rerun")

event.selection
```

This is an example of the selection state when selecting a single point:

```json
{
  "points": [
    {
      "curve_number": 2,
      "point_number": 9,
      "point_index": 9,
      "x": 3.6,
      "y": 7.2,
      "customdata": [
        2.5
      ],
      "marker_size": 6.1,
      "legendgroup": "virginica"
    }
  ],
  "point_indices": [
    9
  ],
  "box": [],
  "lasso": []
}
```

The schema for the Plotly chart selection state.

The selection state is stored in a dictionary-like object that supports both key and attribute notation. Selection states cannot be programmatically changed or set through Session State.

Only selection events are supported at this time.

## Notes

## Version From Slug

## Platform From Slug

## Menu

- **Get started**
  - **Installation**
    - LOCAL DEVELOPMENT
    - Use Streamlit Playground
    - Install via command line
    - Install via Anaconda Distribution
    - CLOUD DEVELOPMENT
    - Use GitHub Codespaces
  - **Fundamentals**
    - Basic concepts
    - Advanced concepts
    - Additional features
    - Summary
  - **First steps**
    - Create an app
    - Create a multipage app

- **Develop**
  - **Concepts**
    - CORE
    - Architecture and execution
    - Multipage apps
    - App design
    - ADDITIONAL
    - Connections, secrets, and authentication
    - Custom components
    - Configuration and theming
    - App testing
  - **API reference**
    - PAGE ELEMENTS
    - Write and magic
    - Text elements
    - Data elements
    - Chart elements
    - Input widgets
    - Media elements
    - Layouts and containers
    - Chat elements
    - Status elements
    - Third-party components
    - Application LOGIC
    - Authentication and user info
    - Navigation and pages
    - Execution flow
    - Caching and state
    - Connections and secrets
    - Custom components
    - Configuration
    - TOOLS
    - App testing
    - Command line
  - **Tutorials**
    - Authentication and personalization
    - Chat and LLM apps
    - Configuration and theming
    - Connect to data sources
    - Elements
    - Execution flow
    - Multipage apps
  - **Quick reference**
    - Cheat sheet
    - Release notes
    - Pre-release features
    - Roadmap

## Examples

### Example 1: Basic Plotly chart

The example below comes from the examples at [https://plot.ly/python](https://plot.ly/python/). Note that `plotly.figure_factory` requires `scipy` to run.

```python
import plotly.figure_factory as ff
import streamlit as st

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length")

event = st.plotly_chart(fig, key="iris", on_select="rerun")

event
```

### Example 2: Plotly Chart with configuration

By default, Plotly charts have scroll zoom enabled. If you have a longer page and want to avoid conflicts between page scrolling and zooming, you can use Plotly's configuration options to disable scroll zoom. In the following example, scroll zoom is disabled, but the zoom buttons are still enabled in the modebar.

```python
import plotly.graph_objects as go
import streamlit as st

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=[1, 2, 3, 4, 5],
        y=[1, 3, 2, 5, 4]
    )
)

st.plotly_chart(fig, config = {'scrollZoom': False})
```

### Theming

Plotly charts are displayed using the Streamlit theme by default. This theme is sleek, user-friendly, and incorporates Streamlit's color palette. The added benefit is that your charts better integrate with the rest of your app's design.

The Streamlit theme is available from Streamlit 1.16.0 through the `theme="streamlit"` keyword argument. To disable it, and use Plotly's native theme, use `theme=None` instead.

Let's look at an example of charts with the Streamlit theme and the native Plotly theme:

```python
import plotly.express as px
import streamlit as st

df = px.data.gapminder()

fig = px.scatter(
    df.query("year==2007"),
    x="sepal_width",
    y="sepal_length",
    color="species",
    size="petal_length",
    hover_data=["petal_width"],
)

event = st.plotly_chart(fig, key="iris", on_select="rerun")

event.selection
```

This is an example of the selection state when selecting a single point:

```json
{
  "points": [
    {
      "curve_number": 2,
      "point_number": 9,
      "point_index": 9,
      "x": 3.6,
      "y": 7.2,
      "customdata": [
        2.5
      ],
      "marker_size": 6.1,
      "legendgroup": "virginica"
    }
  ],
  "point_indices": [
    9
  ],
  "box": [],
  "lasso": []
}
```

The schema for the Plotly chart selection state.

The selection state is stored in a dictionary-like object that supports both key and attribute notation. Selection states cannot be programmatically changed or set through Session State.

Only selection events are supported at this time.

## Notes

## Version From Slug

## Platform From Slug

## Menu

- **Get started**
  - **Installation**
    - LOCAL DEVELOPMENT
    - Use Streamlit Playground
    - Install via command line
    - Install via Anaconda Distribution
    - CLOUD DEVELOPMENT
    - Use GitHub Codespaces
  - **Fundamentals**
    - Basic concepts
    - Advanced concepts
    - Additional features
    - Summary
  - **First steps**
    - Create an app
    - Create a multipage app

- **Develop**
  - **Concepts**
    - CORE
    - Architecture and execution
    - Multipage apps
    - App design
    - ADDITIONAL
    - Connections, secrets, and authentication
    - Custom components
    - Configuration and theming
    - App testing
  - **API reference**
    - PAGE ELEMENTS
    - Write and magic
    - Text elements
    - Data elements
    - Chart elements
    - Input widgets
    - Media elements
    - Layouts and containers
    - Chat elements
    - Status elements
    - Third-party components
    - Application LOGIC
    - Authentication and user info
    - Navigation and pages
    - Execution flow
    - Caching and state
    - Connections and secrets
    - Custom components
    - Configuration
    - TOOLS
    - App testing
    - Command line
  - **Tutorials**
    - Authentication and personalization
    - Chat and LLM apps
    - Configuration and theming
    - Connect to data sources
    - Elements
    - Execution flow
    - Multipage apps
  - **Quick reference**
    - Cheat sheet
    - Release notes
    - Pre-release features
    - Roadmap

## Examples

### Example 1: Basic Plotly chart

The example below comes from the examples at [https://plot.ly/python](https://plot.ly/python/). Note that `plotly.figure_factory` requires `scipy` to run.

```python
import plotly.figure_factory as ff
import streamlit as st

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length")

event = st.plotly_chart(fig, key="iris", on_select="rerun")

event
```

### Example 2: Plotly Chart with configuration

By default, Plotly charts have scroll zoom enabled. If you have a longer page and want to avoid conflicts between page scrolling and zooming, you can use Plotly's configuration options to disable scroll zoom. In the following example, scroll zoom is disabled, but the zoom buttons are still enabled in the modebar.

```python
import plotly.graph_objects as go
import streamlit as st

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=[1, 2, 3, 4, 5],
        y=[1, 3, 2, 5, 4]
    )
)

st.plotly_chart(fig, config = {'scrollZoom': False})
```

### Theming

Plotly charts are displayed using the Streamlit theme by default. This theme is sleek, user-friendly, and incorporates Streamlit's color palette. The added benefit is that your charts better integrate with the rest of your app's design.

The Streamlit theme is available from Streamlit 1.16.0 through the `theme="streamlit"` keyword argument. To disable it, and use Plotly's native theme, use `theme=None` instead.

Let's look at an example of charts with the Streamlit theme and the native Plotly theme:

```python
import plotly.express as px
import streamlit as st

df = px.data.gapminder()

fig = px.scatter(
    df.query("year==2007"),
    x="sepal_width",
    y="sepal_length",
    color="species",
    size="petal_length",
    hover_data=["petal_width"],
)

event = st.plotly_chart(fig, key="iris", on_select="rerun")

event.selection
```

This is an example of the selection state when selecting a single point:

```json
{
  "points": [
    {
      "curve_number": 2,
      "point_number": 9,
      "point_index": 9,
      "x": 3.6,
      "y": 7.2,
      "customdata": [
        2.5
      ],
      "marker_size": 6.1,
      "legendgroup": "virginica"
    }
  ],
  "point_indices": [
    9
  ],
  "box": [],
  "lasso": []
}
```

The schema for the Plotly chart selection state.

The selection state is stored in a dictionary-like object that supports both key and attribute notation. Selection states cannot be programmatically changed or set through Session State.

Only selection events are supported at this time.

## Notes

## Version From Slug

## Platform From Slug

## Menu

- **Get started**
  - **Installation**
    - LOCAL DEVELOPMENT
    - Use Streamlit Playground
    - Install via command line
    - Install via Anaconda Distribution
    - CLOUD DEVELOPMENT
    - Use GitHub Codespaces
  - **Fundamentals
# Source: https://docs.streamlit.io/develop/api-reference/write-magic/st.write

# st.write

Displays arguments in the app.

This is the Swiss Army knife of Streamlit commands: it does different things depending on what you throw at it. Unlike other Streamlit commands, `st.write()` has some unique properties:

- You can pass in multiple arguments, all of which will be displayed.
- Its behavior depends on the input type(s).

## Examples

Its basic use case is to draw Markdown-formatted text, whenever the input is a string:

```python
import streamlit as st

st.write("Hello, *World!* :sunglasses:")
```

As mentioned earlier, `st.write()` also accepts other data formats, such as numbers, data frames, styled data frames, and assorted objects:

```python
import streamlit as st
import pandas as pd

st.write(1234)
st.write(
    pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        }
    )
)
```

Finally, you can pass in multiple arguments to do things like:

```python
import streamlit as st

st.write("1 + 1 = ", 2)
st.write("Below is a DataFrame:", data_frame, "Above is a dataframe.")
```

Oh, one more thing: `st.write` accepts chart objects too! For example:

```python
import altair as alt
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(rng(0).standard_normal((200, 3)), columns=["a", "b", "c"])
chart = (
    alt.Chart(df)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.write(chart)
```

## Featured video

Learn what the `st.write` and `magic` commands are and how to use them.

## Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

- [Concepts](/deploy/concepts)
- [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
- [Snowflake](/deploy/snowflake)
- [Other platforms](/deploy/tutorials)

## Knowledge base

- [FAQ](/knowledge-base/using-streamlit)
- [Installing dependencies](/knowledge-base/dependencies)
- [Deployment issues](/knowledge-base/deploy)

## Get started

- [Installation](/get-started/installation)
- [Fundamentals](/get-started/fundamentals)
- [First steps](/get-started/tutorials)

## Develop

- [Concepts](/develop/concepts)
- [API reference](/develop/api-reference)
- [Tutorials](/develop/tutorials)
- [Quick reference](/develop/quick-reference)

## Deploy

-
# st.pydeck_chart

Draw a chart using the PyDeck library.

This supports 3D maps, point clouds, and more! More info about PyDeck at [https://deckgl.readthedocs.io/en/latest/](https://deckgl.readthedocs.io/en/latest/).

These docs are also quite useful:

- DeckGL docs: [https://github.com/uber/deck.gl/tree/master/docs](https://github.com/uber/deck.gl/tree/master/docs)
- DeckGL JSON docs: [https://github.com/uber/deck.gl/tree/master/modules/json](https://github.com/uber/deck.gl/tree/master/modules/json)

When using this command, a service called [Carto](https://carto.com/) provides the map tiles to render map content. If you're using advanced PyDeck features you may need to obtain an API key from Carto first. You can do that as `pydeck.Deck(api_keys={"carto": YOUR_KEY})` or by setting the CARTO_API_KEY environment variable. See [PyDeck's documentation](https://deckgl.readthedocs.io/en/latest/deck.html) for more information.

Another common provider for map tiles is [Mapbox](https://mapbox.com/). If you prefer to use that, you'll need to create an account at [https://mapbox.com/](https://mapbox.com/) and specify your Mapbox key when creating the `pydeck.Deck` object. You can do that as `pydeck.Deck(api_keys={"mapbox": YOUR_KEY})` or by setting the MAPBOX_API_KEY environment variable.

Carto and Mapbox are third-party products and Streamlit accepts no responsibility or liability of any kind for Carto or Mapbox, or for any content or information made available by Carto or Mapbox. The use of Carto or Mapbox is governed by their respective Terms of Use.

## Notes

Pydeck uses two WebGL contexts per chart, and different browsers have different limits on the number of WebGL contexts per page. If you exceed this limit, the oldest contexts will be dropped to make room for the new ones. To avoid this limitation in most browsers, don't display more than eight Pydeck charts on a single page.

## Example

Here's a chart using a HexagonLayer and a ScatterplotLayer. It uses either the light or dark map style, based on which Streamlit theme is currently active:

```python
import pandas as pd
import pydeck as pdk
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(
    rng(0).standard_normal((1000, 2)) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"],
)

st.pydeck_chart(
    pdk.Deck(
        map_style=None,  # Use Streamlit theme to pick map style
        initial_view_state=pdk.ViewState(
            latitude=37.76,
            longitude=-122.4,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=df,
                get_position="[lon, lat]",
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
            pdk.Layer(
                "ScatterplotLayer",
                data=df,
                get_position="[lon, lat]",
                get_color="[200, 30, 0, 160]",
                get_radius=200,
            ),
        ],
    )
)
```

This is an example of the selection state when selecting a single object from a layer with id, `capital-cities`:

```json
{
  "indices": {
    "capital-cities": [
      2
    ]
  },
  "objects": {
    "capital-cities": [
      {
        "Abbreviation": "AZ",
        "Capital": "Phoenix",
        "Latitude": 33.448457,
        "Longitude": -112.073844,
        "Population": 1650070,
        "State": "Arizona",
        "size": 165007.0
      }
    ]
  }
}
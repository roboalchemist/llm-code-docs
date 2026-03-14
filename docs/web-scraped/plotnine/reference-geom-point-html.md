# Source: https://plotnine.org/reference/geom_point.html

Title: plotnine 0.15.3

URL Source: https://plotnine.org/reference/geom_point.html

Markdown Content:
Plot points (Scatter plot)

```
geom_point(
    mapping=None,
    data=None,
    *,
    stat="identity",
    position="identity",
    na_rm=False,
    inherit_aes=True,
    show_legend=None,
    raster=False,
    **kwargs
)
```

Parameters
----------

`mapping : aes = None`
Aesthetic mappings created with [aes](https://plotnine.org/reference/aes.html#plotnine.aes). If specified and `inherit_aes=True`, it is combined with the default mapping for the plot. You must supply mapping if there is no plot mapping.

| Aesthetic | Default value |
| --- | --- |
| **x** |  |
| **y** |  |
| alpha | `1` |
| color | `'black'` |
| fill | `None` |
| group |  |
| shape | `'o'` |
| size | `1.5` |
| stroke | `0.5` |

The **bold** aesthetics are required.

`data : DataFrame = None`
The data to be displayed in this layer. If `None`, the data from from the `ggplot()` call is used. If specified, it overrides the data from the `ggplot()` call.

`stat : str | stat = "identity"`
The statistical transformation to use on the data for this layer. If it is a string, it must be the registered and known to Plotnine.

`position : str | position = "identity"`
Position adjustment. If it is a string, it must be registered and known to Plotnine.

`na_rm : bool = False`
If `False`, removes missing values with a warning. If `True` silently removes missing values.

`inherit_aes : bool = True`
If `False`, overrides the default aesthetics.

`show_legend : bool | dict = None`
Whether this layer should be included in the legends. `None` the default, includes any aesthetics that are mapped. If a [`bool`](https://docs.python.org/3/library/functions.html#bool), `False` never includes and `True` always includes. A [`dict`](https://docs.python.org/3/library/stdtypes.html#dict) can be used to _exclude_ specific aesthetis of the layer from showing in the legend. e.g `show_legend={'color': False}`, any other aesthetic are included by default.

`raster : bool = False`
If `True`, draw onto this layer a raster (bitmap) object even ifthe final image is in vector format.

`**kwargs : Any`
Aesthetics or parameters used by the `stat`.

Examples
--------

```
import numpy as np
import pandas as pd
from plotnine import (
    ggplot,
    aes,
    geom_point,
    theme_matplotlib,
    theme_set,
)

# Set default theme for all the plots
theme_set(theme_matplotlib())
```

```
np.random.seed(123)
n = 150

df = pd.DataFrame({
    "x": np.random.randint(0, 101, n),
    "y": np.random.randint(0, 101, n),
    "var1": np.random.randint(1, 6, n),
    "var2": np.random.randint(0, 11, n)
})
```

### Basic Scatter Plot

```
# Gallery, points
(
    ggplot(df, aes("x", "y"))
    + geom_point()
)
```

![Image 1](https://plotnine.org/reference/geom_point_files/figure-html/examples-geom_point-cell-4-output-1.png)

### Coloured Point Bubbles

```
(
    ggplot(df, aes("x", "y", size="var1"))
    + geom_point(aes(color="var2"))
)
```

![Image 2](https://plotnine.org/reference/geom_point_files/figure-html/examples-geom_point-cell-5-output-1.png)

```
# Gallery, points
(
    ggplot(df, aes("x", "y", size="var1"))
    + geom_point(aes(fill="var2"), stroke=0, alpha=0.5)
    + geom_point(aes(color="var2"), fill="none")
)
```

![Image 3](https://plotnine.org/reference/geom_point_files/figure-html/examples-geom_point-cell-6-output-1.png)

[Source: Set default theme for all the plots](https://plotnine.org/reference/examples/geom_point-preview.html#cell-0)

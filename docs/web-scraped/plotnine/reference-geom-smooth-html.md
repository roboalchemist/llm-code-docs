# Source: https://plotnine.org/reference/geom_smooth.html

Title: plotnine 0.15.3

URL Source: https://plotnine.org/reference/geom_smooth.html

Markdown Content:
A smoothed conditional mean

```
geom_smooth(
    mapping=None,
    data=None,
    *,
    stat="smooth",
    position="identity",
    na_rm=False,
    inherit_aes=True,
    show_legend=None,
    raster=False,
    legend_fill_ratio=0.5,
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
| alpha | `0.4` |
| color | `'black'` |
| fill | `'#999999'` |
| group |  |
| linetype | `'solid'` |
| size | `1` |
| ymax | `None` |
| ymin | `None` |

The **bold** aesthetics are required.

`data : DataFrame = None`
The data to be displayed in this layer. If `None`, the data from from the `ggplot()` call is used. If specified, it overrides the data from the `ggplot()` call.

`stat : str | stat = "smooth"`
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

`legend_fill_ratio : float = 0.5`
How much (vertically) of the legend box should be filled by the color that indicates the confidence intervals. Should be in the range [0, 1].

`**kwargs : Any`
Aesthetics or parameters used by the `stat`.

See Also
--------

[`stat_smooth`](https://plotnine.org/reference/stat_smooth.html#plotnine.stat_smooth)
The default `stat` for this `geom`.

Examples
--------

```
from plotnine import ggplot, aes, geom_point, geom_smooth, labs, theme_matplotlib, theme_set
from plotnine.data import mpg

theme_set(theme_matplotlib())
```

### Smoothed conditional means

_Aids the eye in seeing patterns in the presence of overplotting._

`mpg.head()`

|  | manufacturer | model | displ | year | cyl | trans | drv | cty | hwy | fl | class |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | audi | a4 | 1.8 | 1999 | 4 | auto(l5) | f | 18 | 29 | p | compact |
| 1 | audi | a4 | 1.8 | 1999 | 4 | manual(m5) | f | 21 | 29 | p | compact |
| 2 | audi | a4 | 2.0 | 2008 | 4 | manual(m6) | f | 20 | 31 | p | compact |
| 3 | audi | a4 | 2.0 | 2008 | 4 | auto(av) | f | 21 | 30 | p | compact |
| 4 | audi | a4 | 2.8 | 1999 | 6 | auto(l5) | f | 16 | 26 | p | compact |

```
(
    ggplot(mpg, aes(x="displ", y="hwy"))
    + geom_point()
    + geom_smooth()
    + labs(x="displacement", y="horsepower")
)
```

![Image 1](https://plotnine.org/reference/geom_smooth_files/figure-html/examples-geom_smooth-cell-4-output-1.png)

Use `span` to control the “wiggliness” of the default loess smoother. The span is the fraction of points used to fit each local regression: small numbers make a wigglier curve, larger numbers make a smoother curve.

```
(
    ggplot(mpg, aes(x="displ", y="hwy"))
    + geom_point()
    + geom_smooth(span=0.3)
    + labs(x="displacement", y="horsepower")
)
```

![Image 2](https://plotnine.org/reference/geom_smooth_files/figure-html/examples-geom_smooth-cell-5-output-1.png)

You can remove confidence interval around smooth with `se=False`:

```
(
    ggplot(mpg, aes(x="displ", y="hwy"))
    + geom_point()
    + geom_smooth(span=0.3, se=False)
    + labs(x="displacement", y="horsepower")
)
```

![Image 3](https://plotnine.org/reference/geom_smooth_files/figure-html/examples-geom_smooth-cell-6-output-1.png)

Instead of a loess smooth, you can use any other modelling function:

```
(
    ggplot(mpg, aes(x="displ", y="hwy"))
    + geom_point()
    + geom_smooth(method="lm")
    + labs(x="displacement", y="horsepower")
)
```

![Image 4](https://plotnine.org/reference/geom_smooth_files/figure-html/examples-geom_smooth-cell-7-output-1.png)

### Points & Linear Models

```
# Gallery, points

(
    ggplot(mpg, aes(x="displ", y="hwy", color="factor(drv)"))
    + geom_point()
    + geom_smooth(method="lm")
    + labs(x="displacement", y="horsepower")
)
```

![Image 5](https://plotnine.org/reference/geom_smooth_files/figure-html/examples-geom_smooth-cell-8-output-1.png)

[Source: Smoothed conditional means](https://plotnine.org/reference/examples/geom_smooth-preview.html#cell-0)

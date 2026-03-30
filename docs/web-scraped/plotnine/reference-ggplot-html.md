# Source: https://plotnine.org/reference/ggplot.html

Title: plotnine 0.15.3

URL Source: https://plotnine.org/reference/ggplot.html

Markdown Content:
`ggplot(data=None, mapping=None)`

Create a new ggplot object

Parameters
----------

`data : Optional[DataLike] = None`
Default data for plot. Every layer that does not have data of its own will use this one.

`mapping : Optional[aes] = None`
Default aesthetics mapping for the plot. These will be used by all layers unless specifically overridden.

Notes
-----

ggplot object only have partial support for pickling. The mappings used by pickled objects should not reference variables in the namespace.

Methods
-------

| Name | Description |
| --- | --- |
| [__add__](https://plotnine.org/reference/ggplot.html#plotnine.ggplot.__add__) | Add to ggplot |
| [__iadd__](https://plotnine.org/reference/ggplot.html#plotnine.ggplot.__iadd__) | Add other to ggplot object |
| [show](https://plotnine.org/reference/ggplot.html#plotnine.ggplot.show) | Show plot using the matplotlib backend set by the user |
| [draw](https://plotnine.org/reference/ggplot.html#plotnine.ggplot.draw) | Render the complete plot |
| [save](https://plotnine.org/reference/ggplot.html#plotnine.ggplot.save) | Save a ggplot object as an image file |
| [save_helper](https://plotnine.org/reference/ggplot.html#plotnine.ggplot.save_helper) | Create MPL figure that will be saved |

### __add__

`__add__(rhs)`

Add to ggplot

#### Parameters

`other`
Either an object that knows how to “radd” itself to a ggplot, or a list of such objects.

### __iadd__

`__iadd__(other)`

Add other to ggplot object

#### Parameters

`other : PlotAddable | list[PlotAddable] | None`
Either an object that knows how to “radd” itself to a ggplot, or a list of such objects.

### show

`show()`

Show plot using the matplotlib backend set by the user

This function is called for its side-effects.

### draw

`draw(*, show=False)`

Render the complete plot

#### Parameters

`show : bool = False`
Whether to show the plot.

#### Returns

### save

```
save(
    filename=None,
    format=None,
    path="",
    width=None,
    height=None,
    units="in",
    dpi=None,
    limitsize=None,
    verbose=True,
    **kwargs
)
```

Save a ggplot object as an image file

#### Parameters

`filename : Optional[str | Path | BytesIO] = None`
File name to write the plot to. If not specified, a name like “plotnine-save-.” is used.

`format : Optional[str] = None`
Image format to use, automatically extract from file name extension.

`path : str = ""`
Path to save plot to (if you just want to set path and not filename).

`width : Optional[float] = None`
Width (defaults to value set by the theme). If specified the `height` must also be given.

`height : Optional[float] = None`
Height (defaults to value set by the theme). If specified the `width` must also be given.

`units : str = "in"`
Units for width and height when either one is explicitly specified (in, cm, or mm).

`dpi : Optional[int] = None`
DPI to use for raster graphics. If None, defaults to using the `dpi` of theme, if none is set then a `dpi` of 100.

`limitsize : bool | None = None`
If `True` (the default), save will not save images larger than 25x25 inches, to prevent the common error of specifying dimensions in pixels. The default value is from the option `plotine.options.limitsize`.

`verbose : bool = True`
If `True`, print the saving information.

`kwargs : Any`
Additional arguments to pass to matplotlib `savefig()`.

### save_helper

```
save_helper(
    filename=None,
    format=None,
    path=None,
    width=None,
    height=None,
    units="in",
    dpi=None,
    limitsize=None,
    verbose=True,
    **kwargs
)
```

Create MPL figure that will be saved

#### Notes

This method has the same arguments as [`save`](https://plotnine.org/reference/ggplot.html#plotnine.ggplot.save). Use it to get access to the figure that will be saved.

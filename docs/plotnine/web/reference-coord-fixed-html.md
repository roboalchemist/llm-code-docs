# Source: https://plotnine.org/reference/coord_fixed.html

Title: plotnine 0.15.3

URL Source: https://plotnine.org/reference/coord_fixed.html

Markdown Content:
`coord_fixed(ratio=1, xlim=None, ylim=None, expand=True)`

Cartesian coordinates with fixed relationship between x and y scales

Parameters[](https://plotnine.org/reference/coord_fixed.html#parameters)
------------------------------------------------------------------------

`ratio : float = 1`
Desired aspect_ratio (:math:`y/x`) of the panel(s).

`xlim : tuple[float, float] = None`
Limits for x axis. If None, then they are automatically computed.

`ylim : tuple[float, float] = None`
Limits for y axis. If None, then they are automatically computed.

`expand : bool = True`
If `True`, expand the coordinate axes by some factor. If `False`, use the limits from the data.

Notes[](https://plotnine.org/reference/coord_fixed.html#notes)
--------------------------------------------------------------

To specify aspect ratio of the visual size for the axes use the [`aspect_ratio`](https://plotnine.org/reference/aspect_ratio.html#plotnine.themes.themeable.aspect_ratio) themeable.

`ggplot(data, aes('x', 'y')) + theme(aspect_ratio=0.5)`

When changing the `aspect_ratio` in either way, the `width` of the panel remains constant (as derived from the [`plotnine.themes.themeable.figure_size`](https://plotnine.org/reference/figure_size.html#plotnine.themes.themeable.figure_size) themeable) and the `height` is altered to achieve desired ratio.

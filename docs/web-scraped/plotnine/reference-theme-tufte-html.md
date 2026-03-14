# Source: https://plotnine.org/reference/theme_tufte.html

Title: plotnine 0.15.3

URL Source: https://plotnine.org/reference/theme_tufte.html

Markdown Content:
`theme_tufte(base_size=11, base_family=None, ticks=True)`

Tufte Maximal Data, Minimal Ink Theme

Theme based on Chapter 6 Data-Ink Maximization and Graphical Design of Edward Tufte _The Visual Display of Quantitative Information_. No border, no axis lines, no grids. This theme works best in combination with [`geom_rug`](https://plotnine.org/reference/geom_rug.html#plotnine.geom_rug).

The default font family is set to “serif” as he uses serif fonts for labels in _The Visual Display of Quantitative Information_. The serif font used by Tufte in his books is a variant of Bembo, while the sans serif font is Gill Sans. If these fonts are installed on your system, consider setting them explicitly via the argument `base_family`.

Parameters[](https://plotnine.org/reference/theme_tufte.html#parameters)
------------------------------------------------------------------------

`base_size : int = 11`
Base font size. All text sizes are a scaled versions of the base font size.

`base_family : str = None`
Base font family. If `None`, use [`plotnine.options.base_family`](https://plotnine.org/reference/options.base_family.html#plotnine.options.base_family).

`ticks = True`
Whether to show axis ticks.

References[](https://plotnine.org/reference/theme_tufte.html#references)
------------------------------------------------------------------------

Tufte, Edward R. (2001) The Visual Display of Quantitative Information, Chapter 6.

Translated from the R ggthemes package by hyiltiz [hyiltiz@gmail.com](mailto:hyiltiz@gmail.com). Released under GNU GPL v2 license or later.

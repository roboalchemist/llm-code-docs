# Source: https://plotnine.org/reference/element_line.html

Title: plotnine 0.15.3

URL Source: https://plotnine.org/reference/element_line.html

Markdown Content:
```
element_line(
    *,
    color=None,
    size=None,
    linetype=None,
    lineend=None,
    colour=None,
    alpha=None,
    **kwargs
)
```

theme element: line

used for backgrounds and borders

Parameters
----------

`color : str | tuple = None`
line color

`colour : str | tuple = None`
alias of color

`linetype : str | tuple = None`
line style. if a string, it should be one of _solid_, _dashed_, _dashdot_ or _dotted_. you can create interesting dashed patterns using tuples, see `set_linestyle`.

`size : float = None`
line thickness

`alpha : float = None`
Opacity value

`kwargs : dict`
Parameters recognised by `line2d`.

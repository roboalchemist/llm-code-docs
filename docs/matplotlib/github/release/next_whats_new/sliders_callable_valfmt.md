# Callable *valfmt* for `Slider` and `RangeSlider`

In addition to the existing %-format string, the *valfmt* parameter of
[\~.matplotlib.widgets.Slider]{.title-ref} and
[\~.matplotlib.widgets.RangeSlider]{.title-ref} now also accepts a
callable of the form `valfmt(val: float) -> str`.

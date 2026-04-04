# Glossary

This glossary defines concepts and terminology specific to Matplotlib.

::: glossary

Figure

:   The outermost container for a Matplotlib graphic. Think of this as
    the canvas to draw on.

    This is implemented in the class [.Figure]{.title-ref}. For more
    details see `figure-intro`{.interpreted-text role="ref"}.

Axes

:   This is a container for what is often colloquially called a
    plot/chart/graph. It\'s a data area with `Axis`{.interpreted-text
    role="term"}es, i.e. coordinate directions, and includes data
    artists like lines, bars etc. as well as decorations like title,
    axis labels, legend.

    Since most \"plotting operations\" are realized as methods on
    [\~.axes.Axes]{.title-ref} this is the object users will mostly
    interact with.

    Note: The term *Axes* was taken over from MATLAB. Think of this as a
    container spanned by the *x*- and *y*-axis, including decoration and
    data.

Axis

:   A direction with a scale. The scale defines the mapping from data
    coordinates to screen coordinates. The Axis also includes the ticks
    and axis label.

Artist

:   The base class for all graphical element that can be drawn. Examples
    are Lines, Rectangles, Text, Ticks, Legend, Axes, \...
:::

# Standard getters/setters for axis inversion state

Whether an axis is inverted can now be queried and set using the
[.axes.Axes]{.title-ref} getters
[\~.Axes.get_xinverted]{.title-ref}/[\~.Axes.get_yinverted]{.title-ref}
and setters
[\~.Axes.set_xinverted]{.title-ref}/[\~.Axes.set_yinverted]{.title-ref}.

The previously existing methods ([.Axes.xaxis_inverted]{.title-ref},
[.Axes.invert_xaxis]{.title-ref}) are now discouraged (but not
deprecated) due to their non-standard naming and behavior.

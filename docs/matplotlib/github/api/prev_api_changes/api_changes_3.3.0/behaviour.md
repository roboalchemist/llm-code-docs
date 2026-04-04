# Behaviour changes

## `Formatter.fix_minus`

[.Formatter.fix_minus]{.title-ref} now performs hyphen-to-unicode-minus
replacement whenever `axes.unicode_minus`{.interpreted-text role="rc"}
is True; i.e. its behavior matches the one of
`ScalarFormatter.fix_minus` ([.ScalarFormatter]{.title-ref} now just
inherits that implementation).

This replacement is now used by the `format_data_short` method of the
various builtin formatter classes, which affects the cursor value in the
GUI toolbars.

## `FigureCanvasBase` now always has a `manager` attribute, which may be None

Previously, it did not necessarily have such an attribute. A check for
`hasattr(figure.canvas, "manager")` should now be replaced by
`figure.canvas.manager is not None` (or
`getattr(figure.canvas, "manager", None) is not None` for
back-compatibility).

## [.cbook.CallbackRegistry]{.title-ref} now propagates exceptions when no GUI event loop is running

[.cbook.CallbackRegistry]{.title-ref} now defaults to propagating
exceptions thrown by callbacks when no interactive GUI event loop is
running. If a GUI event loop *is* running,
[.cbook.CallbackRegistry]{.title-ref} still defaults to just printing a
traceback, as unhandled exceptions can make the program completely
`abort()` in that case.

## `Axes.locator_params()` validates `axis` parameter

[.axes.Axes.locator_params]{.title-ref} used to accept any value for
`axis` and silently did nothing, when passed an unsupported value. It
now raises a `ValueError`.

## `Axis.set_tick_params()` validates `which` parameter

[.Axis.set_tick_params]{.title-ref} (and the higher level
[.axes.Axes.tick_params]{.title-ref} and
[.pyplot.tick_params]{.title-ref}) used to accept any value for `which`
and silently did nothing, when passed an unsupported value. It now
raises a `ValueError`.

## `Axis.set_ticklabels()` must match `FixedLocator.locs`

If an axis is using a [.ticker.FixedLocator]{.title-ref}, typically set
by a call to [.Axis.set_ticks]{.title-ref}, then the number of
ticklabels supplied must match the number of locations available
(`FixedFormattor.locs`). If not, a `ValueError` is raised.

## `backend_pgf.LatexManager.latex`

`backend_pgf.LatexManager.latex` is now created with `encoding="utf-8"`,
so its `stdin`, `stdout`, and `stderr` attributes are utf8-encoded.

## `pyplot.xticks()` and `pyplot.yticks()`

Previously, passing labels without passing the ticks to either
[.pyplot.xticks]{.title-ref} and [.pyplot.yticks]{.title-ref} would
result in:

    TypeError: object of type 'NoneType' has no len()

It now raises a `TypeError` with a proper description of the error.

## Setting the same property under multiple aliases now raises a TypeError

Previously, calling e.g. `plot(..., color=somecolor, c=othercolor)`
would emit a warning because `color` and `c` actually map to the same
Artist property. This now raises a TypeError.

## [.FileMovieWriter]{.title-ref} temporary frames directory

[.FileMovieWriter]{.title-ref} now defaults to writing temporary frames
in a temporary directory, which is always cleared at exit. In order to
keep the individual frames saved on the filesystem, pass an explicit
*frame_prefix*.

## [.Axes.plot]{.title-ref} no longer accepts *x* and *y* being both 2D and with different numbers of columns

Previously, calling [.Axes.plot]{.title-ref} e.g. with *x* of shape
`(n, 3)` and *y* of shape `(n, 2)` would plot the first column of *x*
against the first column of *y*, the second column of *x* against the
second column of *y*, **and** the first column of *x* against the third
column of *y*. This now raises an error instead.

## [.Text.update_from]{.title-ref} now copies usetex state from the source Text

## [\~.Axes.stem]{.title-ref} now defaults to `use_line_collection=True`

This creates the stem plot as a [.LineCollection]{.title-ref} rather
than individual [.Line2D]{.title-ref} objects, greatly improving
performance.

## rcParams color validator is now stricter

Previously, rcParams entries whose values were color-like accepted
\"spurious\" extra letters or characters in the \"middle\" of the
string, e.g. `"(0, 1a, '0.5')"` would be interpreted as `(0, 1, 0.5)`.
These extra characters (including the internal quotes) now cause a
ValueError to be raised.

## [.SymLogNorm]{.title-ref} now has a *base* parameter

Previously, [.SymLogNorm]{.title-ref} had no *base* keyword argument,
and defaulted to `base=np.e` whereas the documentation said it was
`base=10`. In preparation to make the default 10, calling
[.SymLogNorm]{.title-ref} without the new *base* keyword argument emits
a deprecation warning.

## [\~.Axes.errorbar]{.title-ref} now color cycles when only errorbar color is set

Previously setting the *ecolor* would turn off automatic color cycling
for the plot, leading to the the lines and markers defaulting to
whatever the first color in the color cycle was in the case of multiple
plot calls.

## [.rcsetup.validate_color_for_prop_cycle]{.title-ref} now always raises TypeError for bytes input

It previously raised [TypeError]{.title-ref}, **except** when the input
was of the form `b"C[number]"` in which case it raised a ValueError.

## [.FigureCanvasPS.print_ps]{.title-ref} and [.FigureCanvasPS.print_eps]{.title-ref} no longer apply edgecolor and facecolor

These methods now assume that the figure edge and facecolor have been
correctly applied by [.FigureCanvasBase.print_figure]{.title-ref}, as
they are normally called through it.

This behavior is consistent with other figure saving methods
([.FigureCanvasAgg.print_png]{.title-ref},
[.FigureCanvasPdf.print_pdf]{.title-ref},
[.FigureCanvasSVG.print_svg]{.title-ref}).

## [.pyplot.subplot()]{.title-ref} now raises TypeError when given an incorrect number of arguments

This is consistent with other signature mismatch errors. Previously a
ValueError was raised.

## Shortcut for closing all figures

Shortcuts for closing all figures now also work for the classic toolbar.
There is no default shortcut any more because unintentionally closing
all figures by a key press might happen too easily. You can configure
the shortcut yourself using `keymap.quit_all`{.interpreted-text
role="rc"}.

## Autoscale for arrow

Calling ax.arrow() will now autoscale the axes.

## `set_tick_params(label1On=False)` now also makes the offset text (if any) invisible

\... because the offset text can rarely be interpreted without tick
labels anyways.

## [.Axes.annotate]{.title-ref} and [.pyplot.annotate]{.title-ref} parameter name changed

The parameter `s` to [.Axes.annotate]{.title-ref} and
[.pyplot.annotate]{.title-ref} is renamed to `text`, matching
[.Annotation]{.title-ref}.

The old parameter name remains supported, but support for it will be
dropped in a future Matplotlib release.

## [.font_manager.json_dump]{.title-ref} now locks the font manager dump file

\... to prevent multiple processes from writing to it at the same time.

## [.pyplot.rgrids]{.title-ref} and [.pyplot.thetagrids]{.title-ref} now act as setters also when called with only kwargs

Previously, keyword arguments were silently ignored when no positional
arguments were given.

## [.Axis.get_minorticklabels]{.title-ref} and [.Axis.get_majorticklabels]{.title-ref} now returns plain list

Previously, [.Axis.get_minorticklabels]{.title-ref} and
[.Axis.get_majorticklabels]{.title-ref} returns silent_list. Their
return type is now changed to normal list.
[.get_xminorticklabels]{.title-ref},
[.get_yminorticklabels]{.title-ref},
[.get_zminorticklabels]{.title-ref}, [.Axis.get_ticklabels]{.title-ref},
[.get_xmajorticklabels]{.title-ref}, [.get_ymajorticklabels]{.title-ref}
and [.get_zmajorticklabels]{.title-ref} methods will be affected by this
change.

## Default slider formatter

The default method used to format [.Slider]{.title-ref} values has been
changed to use a [.ScalarFormatter]{.title-ref} adapted the slider
values limits. This should ensure that values are displayed with an
appropriate number of significant digits even if they are much smaller
or much bigger than 1. To restore the old behavior, explicitly pass a
\"%1.2f\" as the *valfmt* parameter to [.Slider]{.title-ref}.

## Add *normalize* keyword argument to `Axes.pie`

`pie()` used to draw a partial pie if the sum of the values was \< 1.
This behavior is deprecated and will change to always normalizing the
values to a full pie by default. If you want to draw a partial pie,
please pass `normalize=False` explicitly.

## `table.CustomCell` is now an alias for [.table.Cell]{.title-ref}

All the functionality of `CustomCell` has been moved to its base class
[\~.table.Cell]{.title-ref}.

## wx Timer interval

Setting the timer interval on a not-yet-started `TimerWx` won\'t start
it anymore.

## \"step\"-type histograms default to the zorder of [.Line2D]{.title-ref}

This ensures that they go above gridlines by default. The old `zorder`
can be kept by passing it as a keyword argument to
[.Axes.hist]{.title-ref}.

## [.Legend]{.title-ref} and [.OffsetBox]{.title-ref} visibility

[.Legend]{.title-ref} and [.OffsetBox]{.title-ref} subclasses
([.PaddedBox]{.title-ref}, [.AnchoredOffsetbox]{.title-ref}, and
[.AnnotationBbox]{.title-ref}) no longer directly keep track of the
visibility of their underlying [.Patch]{.title-ref} artist, but instead
pass that flag down to the [.Patch]{.title-ref}.

## [.Legend]{.title-ref} and [.Table]{.title-ref} no longer allow invalid locations

This affects legends produced on an Axes ([.Axes.legend]{.title-ref} and
[.pyplot.legend]{.title-ref}) and on a Figure
([.Figure.legend]{.title-ref} and [.pyplot.figlegend]{.title-ref}).
Figure legends also no longer accept the unsupported `'best'` location.
Previously, invalid Axes locations would use `'best'` and invalid Figure
locations would used `'upper right'`.

## Passing Line2D\'s *drawstyle* together with *linestyle* is removed

Instead of `plt.plot(..., linestyle="steps--")`, use
`plt.plot(..., linestyle="--", drawstyle="steps")`. `ds` is also an
alias for `drawstyle`.

## Upper case color strings

Support for passing single-letter colors (one of \"rgbcmykw\") as
UPPERCASE characters is removed; these colors are now case-sensitive
(lowercase).

## tight/constrained_layout no longer worry about titles that are too wide

*tight_layout* and *constrained_layout* shrink axes to accommodate
\"decorations\" on the axes. However, if an xlabel or title is too long
in the x direction, making the axes smaller in the x-direction doesn\'t
help. The behavior of both has been changed to ignore the width of the
title and xlabel and the height of the ylabel in the layout logic.

This also means there is a new keyword argument for
[.axes.Axes.get_tightbbox]{.title-ref} and \`.axis.Axis.get_tightbbox\`:
`for_layout_only`, which defaults to *False*, but if *True* returns a
bounding box using the rules above.

## `savefig.facecolor`{.interpreted-text role="rc"} and `savefig.edgecolor`{.interpreted-text role="rc"} now default to \"auto\"

This newly allowed value for `savefig.facecolor`{.interpreted-text
role="rc"} and `savefig.edgecolor`{.interpreted-text role="rc"}, as well
as the *facecolor* and *edgecolor* parameters to
[.Figure.savefig]{.title-ref}, means \"use whatever facecolor and
edgecolor the figure current has\".

## When using a single dataset, [.Axes.hist]{.title-ref} no longer wraps the added artist in a [.silent_list]{.title-ref}

When [.Axes.hist]{.title-ref} is called with a single dataset, it adds
to the axes either a [.BarContainer]{.title-ref} object (when
`histtype="bar"` or `"barstacked"`), or a [.Polygon]{.title-ref} object
(when `histype="step"` or `"stepfilled"`) \-- the latter being wrapped
in a list-of-one-element. Previously, either artist would be wrapped in
a [.silent_list]{.title-ref}. This is no longer the case: the
[.BarContainer]{.title-ref} is now returned as is (this is an API
breaking change if you were directly relying on the concrete
[list]{.title-ref} API; however, [.BarContainer]{.title-ref} inherits
from [tuple]{.title-ref} so most common operations remain available),
and the list-of-one [.Polygon]{.title-ref} is returned as is. This makes
the [repr]{.title-ref} of the returned artist more accurate: it is now :

    <BarContainer object of 10 artists>  # "bar", "barstacked"
    [<matplotlib.patches.Polygon object at 0xdeadbeef>]  # "step", "stepfilled"

instead of :

    <a list of 10 Patch objects>  # "bar", "barstacked"
    <a list of 1 Patch objects>  # "step", "stepfilled"

When [.Axes.hist]{.title-ref} is called with multiple artists, it still
wraps its return value in a [.silent_list]{.title-ref}, but uses more
accurate type information :

    <a list of 3 BarContainer objects>  # "bar", "barstacked"
    <a list of 3 List[Polygon] objects>  # "step", "stepfilled"

instead of :

    <a list of 3 Lists of Patches objects>  # "bar", "barstacked"
    <a list of 3 Lists of Patches objects>  # "step", "stepfilled"

## Qt and wx backends no longer create a status bar by default

The coordinates information is now displayed in the toolbar,
consistently with the other backends. This is intended to simplify
embedding of Matplotlib in larger GUIs, where Matplotlib may control the
toolbar but not the status bar.

## `text.hinting`{.interpreted-text role="rc"} now supports names mapping to FreeType flags

`text.hinting`{.interpreted-text role="rc"} now supports the values
\"default\", \"no_autohint\", \"force_autohint\", and \"no_hinting\",
which directly map to the FreeType flags FT_LOAD_DEFAULT, etc. The old
synonyms (respectively \"either\", \"native\", \"auto\", and \"none\")
are still supported, but their use is discouraged. To get normalized
values, use [.backend_agg.get_hinting_flag]{.title-ref}, which returns
integer flag values.

## [.cbook.get_sample_data]{.title-ref} auto-loads numpy arrays

When [.cbook.get_sample_data]{.title-ref} is used to load a npy or npz
file and the keyword-only parameter `np_load` is True, the file is
automatically loaded using [numpy.load]{.title-ref}. `np_load` defaults
to False for backwards compatibility, but will become True in a later
release.

## `get_text_width_height_descent` now checks `ismath` rather than `text.usetex`{.interpreted-text role="rc"}

\... to determine whether a string should be passed to the usetex
machinery or not. This allows single strings to be marked as not-usetex
even when the rcParam is True.

## [.Axes.vlines]{.title-ref}, [.Axes.hlines]{.title-ref}, [.pyplot.vlines]{.title-ref} and [.pyplot.hlines]{.title-ref} *colors* parameter default change

The *colors* parameter will now default to
`lines.color`{.interpreted-text role="rc"}, while previously it
defaulted to \'k\'.

## Aggressively autoscale clim in `ScalerMappable` classes

Previously some plotting methods would defer autoscaling until the first
draw if only one of the *vmin* or *vmax* keyword arguments were passed
([.Axes.scatter]{.title-ref}, [.Axes.hexbin]{.title-ref},
[.Axes.imshow]{.title-ref}, [.Axes.pcolorfast]{.title-ref}) but would
scale based on the passed data if neither was passed (independent of the
*norm* keyword arguments). Other methods ([.Axes.pcolor]{.title-ref},
[.Axes.pcolormesh]{.title-ref}) always autoscaled base on the initial
data.

All of the plotting methods now resolve the unset *vmin* or *vmax* at
the initial call time using the data passed in.

If you were relying on exactly one of the *vmin* or *vmax* remaining
unset between the time when the method is called and the first time the
figure is rendered you get back the old behavior by manually setting the
relevant limit back to [None]{.title-ref} :

    cm_obj.norm.vmin = None
    # or
    cm_obj.norm.vmax = None

which will be resolved during the draw process.

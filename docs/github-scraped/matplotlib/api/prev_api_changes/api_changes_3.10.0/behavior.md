# Behavior Changes

## onselect argument to selector widgets made optional

The *onselect* argument to [.EllipseSelector]{.title-ref},
[.LassoSelector]{.title-ref}, [.PolygonSelector]{.title-ref}, and
[.RectangleSelector]{.title-ref} is no longer required.

## `NavigationToolbar2.save_figure` now returns filepath of saved figure

`NavigationToolbar2.save_figure` function may return the filename of the
saved figure.

If a backend implements this functionality it should return
[None]{.title-ref} in the case where no figure is actually saved
(because the user closed the dialog without saving).

If the backend does not or can not implement this functionality
(currently the Gtk4 backends and webagg backends do not) this method
will return `NavigationToolbar2.UNKNOWN_SAVED_STATUS`.

## SVG output: improved reproducibility

Some SVG-format plots [produced different output on each
render](https://github.com/matplotlib/matplotlib/issues/27831), even
with a static `svg.hashsalt` value configured.

The problem was a non-deterministic ID-generation scheme for clip paths;
the fix introduces a repeatable, monotonically increasing integer ID
scheme as a replacement.

Provided that plots add clip paths themselves in deterministic order,
this enables repeatable (a.k.a. reproducible, deterministic) SVG output.

## ft2font classes are now final

The ft2font classes [.ft2font.FT2Font]{.title-ref}, and
[.ft2font.FT2Image]{.title-ref} are now final and can no longer be
subclassed.

## `InsetIndicator` artist

[\~.Axes.indicate_inset]{.title-ref} and
[\~.Axes.indicate_inset_zoom]{.title-ref} now return an instance of
[\~matplotlib.inset.InsetIndicator]{.title-ref}. Use the
[\~matplotlib.inset.InsetIndicator.rectangle]{.title-ref} and
[\~matplotlib.inset.InsetIndicator.connectors]{.title-ref} properties of
this artist to access the objects that were previously returned
directly.

## `imshow` *interpolation_stage* default changed to \'auto\'

The *interpolation_stage* parameter of [\~.Axes.imshow]{.title-ref} has
a new default value \'auto\'. For images that are up-sampled less than a
factor of three or down-sampled, image interpolation will occur in
\'rgba\' space. For images that are up-sampled by a factor of 3 or more,
then image interpolation occurs in \'data\' space.

The previous default was \'data\', so down-sampled images may change
subtly with the new default. However, the new default also avoids
floating point artifacts at sharp boundaries in a colormap when
down-sampling.

The previous behavior can achieved by setting the *interpolation_stage*
parameter or `image.interpolation_stage`{.interpreted-text role="rc"} to
\'data\'.

## imshow default *interpolation* changed to \'auto\'

The *interpolation* parameter of [\~.Axes.imshow]{.title-ref} has a new
default value \'auto\', changed from \'antialiased\', for consistency
with *interpolation_stage* and because the interpolation is only
anti-aliasing during down-sampling. Passing \'antialiased\' still works,
and behaves exactly the same as \'auto\', but is discouraged.

## dark_background and fivethirtyeight styles no longer set `savefig.facecolor` and `savefig.edgecolor`

When using these styles, `savefig.facecolor`{.interpreted-text
role="rc"} and `savefig.edgecolor`{.interpreted-text role="rc"} now
inherit the global default value of \"auto\", which means that the
actual figure colors will be used. Previously, these rcParams were set
to the same values as `figure.facecolor`{.interpreted-text role="rc"}
and `figure.edgecolor`{.interpreted-text role="rc"}, i.e. a saved figure
would always use the theme colors even if the user manually overrode
them; this is no longer the case.

This change should have no impact for users that do not manually set the
figure face and edge colors.

## Add zorder option in QuiverKey

`zorder` can be used as a keyword argument to [.QuiverKey]{.title-ref}.
Previously, that parameter did not have any effect because the zorder
was hard coded.

## Subfigures

[.Figure.subfigures]{.title-ref} are now added in row-major order to be
consistent with [.Figure.subplots]{.title-ref}. The return value of
[\~.Figure.subfigures]{.title-ref} is not changed, but the order of
`fig.subfigs` is.

## (Sub)Figure.get_figure

\...in future will by default return the direct parent figure, which may
be a SubFigure. This will make the default behavior consistent with the
[\~matplotlib.artist.Artist.get_figure]{.title-ref} method of other
artists. To control the behavior, use the newly introduced *root*
parameter.

## `transforms.AffineDeltaTransform` updates correctly on axis limit changes

Before this change, transform sub-graphs with `AffineDeltaTransform` did
not update correctly. This PR ensures that changes to the child
transform are passed through correctly.

## The offset string associated with ConciseDateFormatter will now invert when the axis is inverted

Previously, when the axis was inverted, the offset string associated
with ConciseDateFormatter would not change, so the offset string
indicated the axis was oriented in the wrong direction. Now, when the
axis is inverted, the offset string is oriented correctly.

## `suptitle` in compressed layout

Compressed layout now automatically positions the
[\~.Figure.suptitle]{.title-ref} just above the top row of axes. To keep
this title in its previous position, either pass `in_layout=False` or
explicitly set `y=0.98` in the [\~.Figure.suptitle]{.title-ref} call.

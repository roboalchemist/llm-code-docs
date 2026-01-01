# Changes for 0.98.0

-   `matplotlib.image.imread`{.interpreted-text role="func"} now no
    longer always returns RGBA data\-\--if the image is luminance or
    RGB, it will return a MxN or MxNx3 array if possible. Also uint8 is
    no longer always forced to float.
-   Rewrote the `matplotlib.cm.ScalarMappable`{.interpreted-text
    role="class"} callback infrastructure to use
    `matplotlib.cbook.CallbackRegistry`{.interpreted-text role="class"}
    rather than custom callback handling. Any users of
    `matplotlib.cm.ScalarMappable.add_observer` of the
    `~matplotlib.cm.ScalarMappable`{.interpreted-text role="class"}
    should use the `matplotlib.cm.ScalarMappable.callbacksSM`
    `~matplotlib.cbook.CallbackRegistry`{.interpreted-text role="class"}
    instead.
-   New axes function and Axes method provide control over the plot
    color cycle: `matplotlib.axes.set_default_color_cycle` and
    `matplotlib.axes.Axes.set_color_cycle`.
-   Matplotlib now requires Python 2.4, so
    `matplotlib.cbook`{.interpreted-text role="mod"} will no longer
    provide `set`{.interpreted-text role="class"},
    `enumerate`{.interpreted-text role="func"},
    `reversed`{.interpreted-text role="func"} or `izip` compatibility
    functions.
-   In Numpy 1.0, bins are specified by the left edges only. The axes
    method `matplotlib.axes.Axes.hist`{.interpreted-text role="meth"}
    now uses future Numpy 1.3 semantics for histograms. Providing
    `binedges`, the last value gives the upper-right edge now, which was
    implicitly set to +infinity in Numpy 1.0. This also means that the
    last bin doesn\'t contain upper outliers any more by default.
-   New axes method and pyplot function,
    `~matplotlib.pyplot.hexbin`{.interpreted-text role="func"}, is an
    alternative to `~matplotlib.pyplot.scatter`{.interpreted-text
    role="func"} for large datasets. It makes something like a
    `~matplotlib.pyplot.pcolor`{.interpreted-text role="func"} of a 2-D
    histogram, but uses hexagonal bins.
-   New kwarg, `symmetric`, in
    `matplotlib.ticker.MaxNLocator`{.interpreted-text role="class"}
    allows one require an axis to be centered around zero.
-   Toolkits must now be imported from `mpl_toolkits` (not
    `matplotlib.toolkits`)

## Notes about the transforms refactoring

A major new feature of the 0.98 series is a more flexible and extensible
transformation infrastructure, written in Python/Numpy rather than a
custom C extension.

The primary goal of this refactoring was to make it easier to extend
matplotlib to support new kinds of projections. This is mostly an
internal improvement, and the possible user-visible changes it allows
are yet to come.

See `matplotlib.transforms`{.interpreted-text role="mod"} for a
description of the design of the new transformation framework.

For efficiency, many of these functions return views into Numpy arrays.
This means that if you hold on to a reference to them, their contents
may change. If you want to store a snapshot of their current values, use
the Numpy array method copy().

The view intervals are now stored only in one place \-- in the
`matplotlib.axes.Axes`{.interpreted-text role="class"} instance, not in
the locator instances as well. This means locators must get their limits
from their `matplotlib.axis.Axis`{.interpreted-text role="class"}, which
in turn looks up its limits from the
`~matplotlib.axes.Axes`{.interpreted-text role="class"}. If a locator is
used temporarily and not assigned to an Axis or Axes, (e.g., in
`matplotlib.contour`{.interpreted-text role="mod"}), a dummy axis must
be created to store its bounds. Call
`matplotlib.ticker.TickHelper.create_dummy_axis`{.interpreted-text
role="meth"} to do so.

The functionality of `Pbox` has been merged with
`~matplotlib.transforms.Bbox`{.interpreted-text role="class"}. Its
methods now all return copies rather than modifying in place.

The following lists many of the simple changes necessary to update code
from the old transformation framework to the new one. In particular,
methods that return a copy are named with a verb in the past tense,
whereas methods that alter an object in place are named with a verb in
the present tense.

### `matplotlib.transforms`{.interpreted-text role="mod"}

  ---------------------------------------------------------------------------------------------------
  Old method                                 New method
  ------------------------------------------ --------------------------------------------------------
  `Bbox.get_bounds`                          `.transforms.Bbox.bounds`{.interpreted-text role="attr"}

  `Bbox.width`                               `transforms.Bbox.width
                                             <.transforms.BboxBase.width>`{.interpreted-text
                                             role="attr"}

  `Bbox.height`                              `transforms.Bbox.height
                                             <.transforms.BboxBase.height>`{.interpreted-text
                                             role="attr"}

  `Bbox.intervalx().get_bounds()`            `.transforms.Bbox.intervalx`{.interpreted-text
  `Bbox.intervalx().set_bounds()`            role="attr"} \[It is now a property.\]

  `Bbox.intervaly().get_bounds()`            `.transforms.Bbox.intervaly`{.interpreted-text
  `Bbox.intervaly().set_bounds()`            role="attr"} \[It is now a property.\]

  `Bbox.xmin`                                `.transforms.Bbox.x0`{.interpreted-text role="attr"} or
                                             `transforms.Bbox.xmin
                                             <.transforms.BboxBase.xmin>`{.interpreted-text
                                             role="attr"}[^1]

  `Bbox.ymin`                                `.transforms.Bbox.y0`{.interpreted-text role="attr"} or
                                             `transforms.Bbox.ymin
                                             <.transforms.BboxBase.ymin>`{.interpreted-text
                                             role="attr"}[^2]

  `Bbox.xmax`                                `.transforms.Bbox.x1`{.interpreted-text role="attr"} or
                                             `transforms.Bbox.xmax
                                             <.transforms.BboxBase.xmax>`{.interpreted-text
                                             role="attr"}[^3]

  `Bbox.ymax`                                `.transforms.Bbox.y1`{.interpreted-text role="attr"} or
                                             `transforms.Bbox.ymax
                                             <.transforms.BboxBase.ymax>`{.interpreted-text
                                             role="attr"}[^4]

  `Bbox.overlaps(bboxes)`                    [Bbox.count_overlaps(bboxes)
                                             \<.BboxBase.count_overlaps\>]{.title-ref}

  `bbox_all(bboxes)`                         [Bbox.union(bboxes) \<.BboxBase.union\>]{.title-ref}
                                             \[It is a staticmethod.\]

  `lbwh_to_bbox(l, b, w, h)`                 [Bbox.from_bounds(x0, y0, w, h)
                                             \<.Bbox.from_bounds\>]{.title-ref} \[It is a
                                             staticmethod.\]

  `inverse_transform_bbox(trans, bbox)`      `bbox.inverse_transformed(trans)`

  `Interval.contains_open(v)`                [interval_contains_open(tuple, v)
                                             \<.interval_contains_open\>]{.title-ref}

  `Interval.contains(v)`                     [interval_contains(tuple, v)
                                             \<.interval_contains\>]{.title-ref}

  `identity_transform()`                     `.transforms.IdentityTransform`{.interpreted-text
                                             role="class"}

  `blend_xy_sep_transform(xtrans, ytrans)`   [blended_transform_factory(xtrans, ytrans)
                                             \<.blended_transform_factory\>]{.title-ref}

  `scale_transform(xs, ys)`                  [Affine2D().scale(xs\[, ys\])
                                             \<.Affine2D.scale\>]{.title-ref}

  `get_bbox_transform(boxin, boxout)`        [BboxTransform(boxin, boxout)
                                             \<.BboxTransform\>]{.title-ref} or
                                             [BboxTransformFrom(boxin)
                                             \<.BboxTransformFrom\>]{.title-ref} or
                                             [BboxTransformTo(boxout)
                                             \<.BboxTransformTo\>]{.title-ref}

  `Transform.seq_xy_tup(points)`             [Transform.transform(points)
                                             \<.Transform.transform\>]{.title-ref}

  `Transform.inverse_xy_tup(points)`         [Transform.inverted()
                                             \<.Transform.inverted\>]{.title-ref}.transform(points)
  ---------------------------------------------------------------------------------------------------

### `matplotlib.axes`{.interpreted-text role="mod"}

  Old method                                                  New method
  ----------------------------------------------------------- ---------------------------------------------------------------------------------------------
  `Axes.get_position()`                                       `matplotlib.axes.Axes.get_position`{.interpreted-text role="meth"}[^5]
  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--
  `Axes.set_position()`                                       `matplotlib.axes.Axes.set_position`{.interpreted-text role="meth"}[^6]
  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--
  `Axes.toggle_log_lineary()`                                 `matplotlib.axes.Axes.set_yscale`{.interpreted-text role="meth"}[^7]
  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--
  `Subplot` class                                             removed

The `Polar` class has moved to
`matplotlib.projections.polar`{.interpreted-text role="mod"}.

### `matplotlib.artist`{.interpreted-text role="mod"}

  Old method                     New method
  ------------------------------ ---------------------------------------------
  `Artist.set_clip_path(path)`   `Artist.set_clip_path(path, transform)`[^8]

### `matplotlib.collections`{.interpreted-text role="mod"}

  Old method    New method
  ------------- ------------------
  *linestyle*   *linestyles*[^9]

### `matplotlib.colors`{.interpreted-text role="mod"}

  Old method                         New method
  ---------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------
  `ColorConvertor.to_rgba_list(c)`   `colors.to_rgba_array(c)` \[`matplotlib.colors.to_rgba_array`{.interpreted-text role="meth"} returns an Nx4 NumPy array of RGBA color quadruples.\]

### `matplotlib.contour`{.interpreted-text role="mod"}

  Old method            New method
  --------------------- --------------------------------------------------------------------------------------------------------------------------------
  `Contour._segments`   `matplotlib.contour.Contour.get_paths` \[Returns a list of `matplotlib.path.Path`{.interpreted-text role="class"} instances.\]

### `matplotlib.figure`{.interpreted-text role="mod"}

  -------------------------------------------------------------------------
  Old method             New method
  ---------------------- --------------------------------------------------
  `Figure.dpi.get()`     `matplotlib.figure.Figure.dpi`{.interpreted-text
  `Figure.dpi.set()`     role="attr"} *(a property)*

  -------------------------------------------------------------------------

### `matplotlib.patches`{.interpreted-text role="mod"}

  Old method            New method
  --------------------- --------------------------------------------------------------------------------------------------------------------------------------------------
  `Patch.get_verts()`   `matplotlib.patches.Patch.get_path`{.interpreted-text role="meth"} \[Returns a `matplotlib.path.Path`{.interpreted-text role="class"} instance\]

### `matplotlib.backend_bases`{.interpreted-text role="mod"}

  Old method                                                                                  New method
  ------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------
  `GraphicsContext.set_clip_rectangle(tuple)`                                                 [GraphicsContext.set_clip_rectangle(bbox) \<.GraphicsContextBase.set_clip_rectangle\>]{.title-ref}
  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--
  `GraphicsContext.get_clip_path()`                                                           [GraphicsContext.get_clip_path() \<.GraphicsContextBase.get_clip_path\>]{.title-ref}[^10]
  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--
  `GraphicsContext.set_clip_path()`                                                           [GraphicsContext.set_clip_path() \<.GraphicsContextBase.set_clip_path\>]{.title-ref}[^11]

### `~matplotlib.backend_bases.RendererBase`{.interpreted-text role="class"}

New methods:

-   `draw_path(self, gc, path, transform, rgbFace)
    <matplotlib.backend_bases.RendererBase.draw_path>`{.interpreted-text
    role="meth"}
-   `draw_markers(self, gc, marker_path, marker_trans, path,
    trans, rgbFace)
    <matplotlib.backend_bases.RendererBase.draw_markers>`{.interpreted-text
    role="meth"}
-   `draw_path_collection(self, master_transform, cliprect,
    clippath, clippath_trans, paths, all_transforms, offsets,
    offsetTrans, facecolors, edgecolors, linewidths, linestyles,
    antialiaseds)
    <matplotlib.backend_bases.RendererBase.draw_path_collection>`{.interpreted-text
    role="meth"} *\[optional\]*

Changed methods:

-   `draw_image(self, x, y, im, bbox)` is now
    `draw_image(self, x, y, im, bbox, clippath, clippath_trans)
    <matplotlib.backend_bases.RendererBase.draw_image>`{.interpreted-text
    role="meth"}

Removed methods:

-   `draw_arc`
-   `draw_line_collection`
-   `draw_line`
-   `draw_lines`
-   `draw_point`
-   `draw_quad_mesh`
-   `draw_poly_collection`
-   `draw_polygon`
-   `draw_rectangle`
-   `draw_regpoly_collection`

[^1]: The `~matplotlib.transforms.Bbox`{.interpreted-text role="class"}
    is bound by the points (x0, y0) to (x1, y1) and there is no defined
    order to these points, that is, x0 is not necessarily the left edge
    of the box. To get the left edge of the `.Bbox`{.interpreted-text
    role="class"}, use the read-only property
    `xmin <matplotlib.transforms.BboxBase.xmin>`{.interpreted-text
    role="attr"}.

[^2]: The `~matplotlib.transforms.Bbox`{.interpreted-text role="class"}
    is bound by the points (x0, y0) to (x1, y1) and there is no defined
    order to these points, that is, x0 is not necessarily the left edge
    of the box. To get the left edge of the `.Bbox`{.interpreted-text
    role="class"}, use the read-only property
    `xmin <matplotlib.transforms.BboxBase.xmin>`{.interpreted-text
    role="attr"}.

[^3]: The `~matplotlib.transforms.Bbox`{.interpreted-text role="class"}
    is bound by the points (x0, y0) to (x1, y1) and there is no defined
    order to these points, that is, x0 is not necessarily the left edge
    of the box. To get the left edge of the `.Bbox`{.interpreted-text
    role="class"}, use the read-only property
    `xmin <matplotlib.transforms.BboxBase.xmin>`{.interpreted-text
    role="attr"}.

[^4]: The `~matplotlib.transforms.Bbox`{.interpreted-text role="class"}
    is bound by the points (x0, y0) to (x1, y1) and there is no defined
    order to these points, that is, x0 is not necessarily the left edge
    of the box. To get the left edge of the `.Bbox`{.interpreted-text
    role="class"}, use the read-only property
    `xmin <matplotlib.transforms.BboxBase.xmin>`{.interpreted-text
    role="attr"}.

[^5]: `matplotlib.axes.Axes.get_position`{.interpreted-text role="meth"}
    used to return a list of points, now it returns a
    `matplotlib.transforms.Bbox`{.interpreted-text role="class"}
    instance.

[^6]: `matplotlib.axes.Axes.set_position`{.interpreted-text role="meth"}
    now accepts either four scalars or a
    `matplotlib.transforms.Bbox`{.interpreted-text role="class"}
    instance.

[^7]: Since the refactoring allows for more than two scale types
    (\'log\' or \'linear\'), it no longer makes sense to have a toggle.
    `Axes.toggle_log_lineary()` has been removed.

[^8]: `matplotlib.artist.Artist.set_clip_path`{.interpreted-text
    role="meth"} now accepts a `matplotlib.path.Path`{.interpreted-text
    role="class"} instance and a
    `matplotlib.transforms.Transform`{.interpreted-text role="class"}
    that will be applied to the path immediately before clipping.

[^9]: Linestyles are now treated like all other collection attributes,
    i.e. a single value or multiple values may be provided.

[^10]: `matplotlib.backend_bases.GraphicsContextBase.get_clip_path`{.interpreted-text
    role="meth"} returns a tuple of the form (*path*,
    *affine_transform*), where *path* is a
    `matplotlib.path.Path`{.interpreted-text role="class"} instance and
    *affine_transform* is a
    `matplotlib.transforms.Affine2D`{.interpreted-text role="class"}
    instance.

[^11]: `matplotlib.backend_bases.GraphicsContextBase.set_clip_path`{.interpreted-text
    role="meth"} now only accepts a
    `matplotlib.transforms.TransformedPath`{.interpreted-text
    role="class"} instance.

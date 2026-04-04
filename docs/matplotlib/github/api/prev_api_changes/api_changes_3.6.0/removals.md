# Removals

The following deprecated APIs have been removed:

## Removed behaviour

### Stricter validation of function parameters

-   Unknown keyword arguments to [.Figure.savefig]{.title-ref},
    [.pyplot.savefig]{.title-ref}, and the `FigureCanvas.print_*`
    methods now raise a [TypeError]{.title-ref}, instead of being
    ignored.
-   Extra parameters to the [\~.axes.Axes]{.title-ref} constructor,
    i.e., those other than *fig* and *rect*, are now keyword only.
-   Passing arguments not specifically listed in the signatures of
    [.Axes3D.plot_surface]{.title-ref} and
    [.Axes3D.plot_wireframe]{.title-ref} is no longer supported; pass
    any extra arguments as keyword arguments instead.
-   Passing positional arguments to [.LineCollection]{.title-ref} has
    been removed; use specific keyword argument names now.

### `imread` no longer accepts URLs

Passing a URL to [\~.pyplot.imread()]{.title-ref} has been removed.
Please open the URL for reading and directly use the Pillow API (e.g.,
`PIL.Image.open(urllib.request.urlopen(url))`, or
`PIL.Image.open(io.BytesIO(requests.get(url).content))`) instead.

### MarkerStyle is immutable

The methods `MarkerStyle.set_fillstyle` and `MarkerStyle.set_marker`
have been removed. Create a new [.MarkerStyle]{.title-ref} with the
respective parameters instead.

### Passing bytes to `FT2Font.set_text`

\... is no longer supported. Pass [str]{.title-ref} instead.

### Support for passing tool names to `ToolManager.add_tool`

\... has been removed. The second parameter to
[.ToolManager.add_tool]{.title-ref} must now always be a tool class.

### `backend_tools.ToolFullScreen` now inherits from `ToolBase`, not from `ToolToggleBase`

[.ToolFullScreen]{.title-ref} can only switch between the non-fullscreen
and fullscreen states, but not unconditionally put the window in a given
state; hence the `enable` and `disable` methods were misleadingly named.
Thus, the [.ToolToggleBase]{.title-ref}-related API (`enable`,
`disable`, etc.) was removed.

### `BoxStyle._Base` and `transmute` method of box styles

\... have been removed. Box styles implemented as classes no longer need
to inherit from a base class.

### Loaded modules logging

The list of currently loaded modules is no longer logged at the DEBUG
level at Matplotlib import time, because it can produce extensive output
and make other valuable DEBUG statements difficult to find. If you were
relying on this output, please arrange for your own logging (the
built-in [sys.modules]{.title-ref} can be used to get the currently
loaded modules).

## Modules

-   The `cbook.deprecation` module has been removed from the public API
    as it is considered internal.
-   The `mpl_toolkits.axes_grid` module has been removed. All
    functionality from `mpl_toolkits.axes_grid` can be found in either
    [mpl_toolkits.axes_grid1]{.title-ref} or
    [mpl_toolkits.axisartist]{.title-ref}. Axes classes from
    `mpl_toolkits.axes_grid` based on `Axis` from
    [mpl_toolkits.axisartist]{.title-ref} can be found in
    [mpl_toolkits.axisartist]{.title-ref}.

## Classes, methods and attributes

The following module-level classes/variables have been removed:

-   `cm.cmap_d`
-   `colorbar.colorbar_doc`, `colorbar.colorbar_kw_doc`
-   `ColorbarPatch`
-   `mathtext.Fonts` and all its subclasses
-   `mathtext.FontConstantsBase` and all its subclasses
-   `mathtext.latex_to_bakoma`, `mathtext.latex_to_cmex`,
    `mathtext.latex_to_standard`
-   `mathtext.MathtextBackendPdf`, `mathtext.MathtextBackendPs`,
    `mathtext.MathtextBackendSvg`, `mathtext.MathtextBackendCairo`; use
    `.MathtextBackendPath` instead.
-   `mathtext.Node` and all its subclasses
-   `mathtext.NUM_SIZE_LEVELS`
-   `mathtext.Parser`
-   `mathtext.Ship`
-   `mathtext.SHRINK_FACTOR` and `mathtext.GROW_FACTOR`
-   `mathtext.stix_virtual_fonts`,
-   `mathtext.tex2uni`
-   `backend_pgf.TmpDirCleaner`
-   `backend_ps.GraphicsContextPS`; use `GraphicsContextBase` instead.
-   `backend_wx.IDLE_DELAY`
-   `axes_grid1.parasite_axes.ParasiteAxesAuxTransBase`; use
    [.ParasiteAxesBase]{.title-ref} instead.
-   `axes_grid1.parasite_axes.ParasiteAxesAuxTrans`; use
    [.ParasiteAxes]{.title-ref} instead.

The following class attributes have been removed:

-   `Line2D.validCap` and `Line2D.validJoin`; validation is centralized
    in `rcsetup`.
-   `Patch.validCap` and `Patch.validJoin`; validation is centralized in
    `rcsetup`.
-   `renderer.M`, `renderer.eye`, `renderer.vvec`,
    `renderer.get_axis_position` placed on the Renderer during 3D Axes
    draw; these attributes are all available via [.Axes3D]{.title-ref},
    which can be accessed via `self.axes` on all [.Artist]{.title-ref}s.
-   `RendererPdf.mathtext_parser`, `RendererPS.mathtext_parser`,
    `RendererSVG.mathtext_parser`, `RendererCairo.mathtext_parser`
-   `StandardPsFonts.pswriter`
-   `Subplot.figbox`; use [.Axes.get_position]{.title-ref} instead.
-   `Subplot.numRows`; `ax.get_gridspec().nrows` instead.
-   `Subplot.numCols`; `ax.get_gridspec().ncols` instead.
-   `SubplotDivider.figbox`
-   `cids`, `cnt`, `observers`, `change_observers`, and
    `submit_observers` on all [.Widget]{.title-ref}s

The following class methods have been removed:

-   `Axis.cla()`; use [.Axis.clear]{.title-ref} instead.
-   `RadialAxis.cla()` and `ThetaAxis.cla()`; use
    [.RadialAxis.clear]{.title-ref} or [.ThetaAxis.clear]{.title-ref}
    instead.
-   `Spine.cla()`; use [.Spine.clear]{.title-ref} instead.
-   `ContourLabeler.get_label_coords()`; there is no replacement as it
    was considered an internal helper.
-   `FancyArrowPatch.get_dpi_cor` and `FancyArrowPatch.set_dpi_cor`
-   `FigureCanvas.get_window_title()` and
    `FigureCanvas.set_window_title()`; use
    [.FigureManagerBase.get_window_title]{.title-ref} or
    [.FigureManagerBase.set_window_title]{.title-ref} if using pyplot,
    or use GUI-specific methods if embedding.
-   `FigureManager.key_press()` and `FigureManager.button_press()`;
    trigger the events directly on the canvas using
    `canvas.callbacks.process(event.name, event)` for key and button
    events.
-   `RendererAgg.get_content_extents()` and
    `RendererAgg.tostring_rgba_minimized()`
-   `NavigationToolbar2Wx.get_canvas()`
-   `ParasiteAxesBase.update_viewlim()`; use
    `ParasiteAxesBase.apply_aspect` instead.
-   `Subplot.get_geometry()`; use `SubplotBase.get_subplotspec` instead.
-   `Subplot.change_geometry()`; use `SubplotBase.set_subplotspec`
    instead.
-   `Subplot.update_params()`; this method did nothing.
-   `Subplot.is_first_row()`; use `ax.get_subplotspec().is_first_row`
    instead.
-   `Subplot.is_first_col()`; use `ax.get_subplotspec().is_first_col`
    instead.
-   `Subplot.is_last_row()`; use `ax.get_subplotspec().is_last_row`
    instead.
-   `Subplot.is_last_col()`; use `ax.get_subplotspec().is_last_col`
    instead.
-   `SubplotDivider.change_geometry()`; use
    [.SubplotDivider.set_subplotspec]{.title-ref} instead.
-   `SubplotDivider.get_geometry()`; use
    [.SubplotDivider.get_subplotspec]{.title-ref} instead.
-   `SubplotDivider.update_params()`
-   `get_depth`, `parse`, `to_mask`, `to_rgba`, and `to_png` of
    [.MathTextParser]{.title-ref}; use
    [.mathtext.math_to_image]{.title-ref} instead.
-   `MovieWriter.cleanup()`; the cleanup logic is instead fully
    implemented in [.MovieWriter.finish]{.title-ref} and `cleanup` is no
    longer called.

## Functions

The following functions have been removed;

-   `backend_template.new_figure_manager()`,
    `backend_template.new_figure_manager_given_figure()`, and
    `backend_template.draw_if_interactive()` have been removed, as part
    of the introduction of the simplified backend API.
-   Deprecation-related re-imports `cbook.deprecated()`, and
    `cbook.warn_deprecated()`.
-   `colorbar.colorbar_factory()`; use [.Colorbar]{.title-ref} instead.
    `colorbar.make_axes_kw_doc()`
-   `mathtext.Error()`
-   `mathtext.ship()`
-   `mathtext.tex2uni()`
-   `axes_grid1.parasite_axes.parasite_axes_auxtrans_class_factory()`;
    use [.parasite_axes_class_factory]{.title-ref} instead.
-   `sphinext.plot_directive.align()`; use
    `docutils.parsers.rst.directives.images.Image.align` instead.

## Arguments

The following arguments have been removed:

-   *dpi* from `print_ps()` in the PS backend and `print_pdf()` in the
    PDF backend. Instead, the methods will obtain the DPI from the
    `savefig` machinery.
-   *dpi_cor* from [\~.FancyArrowPatch]{.title-ref}
-   *minimum_descent* from `TextArea`; it is now effectively always True
-   *origin* from `FigureCanvasWx.gui_repaint()`
-   *project* from `Line3DCollection.draw()`
-   *renderer* from [.Line3DCollection.do_3d_projection]{.title-ref},
    [.Patch3D.do_3d_projection]{.title-ref},
    [.PathPatch3D.do_3d_projection]{.title-ref},
    [.Path3DCollection.do_3d_projection]{.title-ref},
    [.Patch3DCollection.do_3d_projection]{.title-ref},
    [.Poly3DCollection.do_3d_projection]{.title-ref}
-   *resize_callback* from the Tk backend; use
    `get_tk_widget().bind('<Configure>', ..., True)` instead.
-   *return_all* from `gridspec.get_position()`
-   Keyword arguments to `gca()`; there is no replacement.

## rcParams

The setting `ps.useafm`{.interpreted-text role="rc"} no longer has any
effect on [matplotlib.mathtext]{.title-ref}.

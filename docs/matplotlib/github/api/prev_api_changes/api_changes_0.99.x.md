# Changes beyond 0.99.x

-   The default behavior of
    `matplotlib.axes.Axes.set_xlim`{.interpreted-text role="meth"},
    `matplotlib.axes.Axes.set_ylim`{.interpreted-text role="meth"}, and
    `matplotlib.axes.Axes.axis`{.interpreted-text role="meth"}, and
    their corresponding pyplot functions, has been changed: when view
    limits are set explicitly with one of these methods, autoscaling is
    turned off for the matching axis. A new *auto* kwarg is available to
    control this behavior. The limit kwargs have been renamed to *left*
    and *right* instead of *xmin* and *xmax*, and *bottom* and *top*
    instead of *ymin* and *ymax*. The old names may still be used,
    however.

-   There are five new Axes methods with corresponding pyplot functions
    to facilitate autoscaling, tick location, and tick label formatting,
    and the general appearance of ticks and tick labels:

    -   `matplotlib.axes.Axes.autoscale`{.interpreted-text role="meth"}
        turns autoscaling on or off, and applies it.
    -   `matplotlib.axes.Axes.margins`{.interpreted-text role="meth"}
        sets margins used to autoscale the
        `matplotlib.axes.Axes.viewLim` based on the
        `matplotlib.axes.Axes.dataLim`.
    -   `matplotlib.axes.Axes.locator_params`{.interpreted-text
        role="meth"} allows one to adjust axes locator parameters such
        as *nbins*.
    -   `matplotlib.axes.Axes.ticklabel_format`{.interpreted-text
        role="meth"} is a convenience method for controlling the
        `matplotlib.ticker.ScalarFormatter`{.interpreted-text
        role="class"} that is used by default with linear axes.
    -   `matplotlib.axes.Axes.tick_params`{.interpreted-text
        role="meth"} controls direction, size, visibility, and color of
        ticks and their labels.

-   The `matplotlib.axes.Axes.bar`{.interpreted-text role="meth"} method
    accepts a *error_kw* kwarg; it is a dictionary of kwargs to be
    passed to the errorbar function.

-   The `matplotlib.axes.Axes.hist`{.interpreted-text role="meth"}
    *color* kwarg now accepts a sequence of color specs to match a
    sequence of datasets.

-   The `~matplotlib.collections.EllipseCollection`{.interpreted-text
    role="class"} has been changed in two ways:

    -   There is a new *units* option, \'xy\', that scales the ellipse
        with the data units. This matches the
        :class:\'\~matplotlib.patches.Ellipse\` scaling.
    -   The *height* and *width* kwargs have been changed to specify the
        height and width, again for consistency with
        `~matplotlib.patches.Ellipse`{.interpreted-text role="class"},
        and to better match their names; previously they specified the
        half-height and half-width.

-   There is a new rc parameter `axes.color_cycle`, and the color cycle
    is now independent of the rc parameter `lines.color`.
    `matplotlib.Axes.set_default_color_cycle` is deprecated.

-   You can now print several figures to one pdf file and modify the
    document information dictionary of a pdf file. See the docstrings of
    the class
    `matplotlib.backends.backend_pdf.PdfPages`{.interpreted-text
    role="class"} for more information.

-   Removed
    [configobj](http://www.voidspace.org.uk/python/configobj.html) and
    [enthought.traits](http://code.enthought.com/pages/traits.html)
    packages, which are only required by the experimental traited config
    and are somewhat out of date. If needed, install them independently.

-   The new rc parameter `savefig.extension` sets the filename extension
    that is used by `matplotlib.figure.Figure.savefig`{.interpreted-text
    role="meth"} if its *fname* argument lacks an extension.

-   In an effort to simplify the backend API, all clipping rectangles
    and paths are now passed in using GraphicsContext objects, even on
    collections and images. Therefore:

        draw_path_collection(self, master_transform, cliprect, clippath,
                             clippath_trans, paths, all_transforms, offsets,
                             offsetTrans, facecolors, edgecolors, linewidths,
                             linestyles, antialiaseds, urls)

        # is now

        draw_path_collection(self, gc, master_transform, paths, all_transforms,
                             offsets, offsetTrans, facecolors, edgecolors,
                             linewidths, linestyles, antialiaseds, urls)


        draw_quad_mesh(self, master_transform, cliprect, clippath,
                       clippath_trans, meshWidth, meshHeight, coordinates,
                       offsets, offsetTrans, facecolors, antialiased,
                       showedges)

        # is now

        draw_quad_mesh(self, gc, master_transform, meshWidth, meshHeight,
                       coordinates, offsets, offsetTrans, facecolors,
                       antialiased, showedges)


        draw_image(self, x, y, im, bbox, clippath=None, clippath_trans=None)

        # is now

        draw_image(self, gc, x, y, im)

-   There are four new Axes methods with corresponding pyplot functions
    that deal with unstructured triangular grids:

    -   `matplotlib.axes.Axes.tricontour`{.interpreted-text role="meth"}
        draws contour lines on a triangular grid.
    -   `matplotlib.axes.Axes.tricontourf`{.interpreted-text
        role="meth"} draws filled contours on a triangular grid.
    -   `matplotlib.axes.Axes.tripcolor`{.interpreted-text role="meth"}
        draws a pseudocolor plot on a triangular grid.
    -   `matplotlib.axes.Axes.triplot`{.interpreted-text role="meth"}
        draws a triangular grid as lines and/or markers.

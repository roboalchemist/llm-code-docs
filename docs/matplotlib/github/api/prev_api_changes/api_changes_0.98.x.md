# Changes for 0.98.x

-   `psd()`, `csd()`, and `cohere()` will now automatically wrap
    negative frequency components to the beginning of the returned
    arrays. This is much more sensible behavior and makes them
    consistent with `specgram()`. The previous behavior was more of an
    oversight than a design decision.

-   Added new keyword parameters *nonposx*, *nonposy* to
    `matplotlib.axes.Axes`{.interpreted-text role="class"} methods that
    set log scale parameters. The default is still to mask out
    non-positive values, but the kwargs accept \'clip\', which causes
    non-positive values to be replaced with a very small positive value.

-   Added new `matplotlib.pyplot.fignum_exists`{.interpreted-text
    role="func"} and `matplotlib.pyplot.get_fignums`{.interpreted-text
    role="func"}; they merely expose information that had been hidden in
    `matplotlib._pylab_helpers`.

-   Deprecated numerix package.

-   Added new `matplotlib.image.imsave`{.interpreted-text role="func"}
    and exposed it to the `matplotlib.pyplot`{.interpreted-text
    role="mod"} interface.

-   Remove support for pyExcelerator in exceltools \-- use xlwt instead

-   Changed the defaults of acorr and xcorr to use usevlines=True,
    maxlags=10 and normed=True since these are the best defaults

-   Following keyword parameters for
    `matplotlib.legend.Legend`{.interpreted-text role="class"} are now
    deprecated and new set of parameters are introduced. The new
    parameters are given as a fraction of the font-size. Also,
    *scatteryoffsets*, *fancybox* and *columnspacing* are added as
    keyword parameters.

      Deprecated       New
      ---------------- ---------------
      pad              borderpad
      labelsep         labelspacing
      handlelen        handlelength
      handlestextsep   handletextpad
      axespad          borderaxespad

-   Removed the configobj and experimental traits rc support

-   Modified `matplotlib.mlab.psd`{.interpreted-text role="func"},
    `matplotlib.mlab.csd`{.interpreted-text role="func"},
    `matplotlib.mlab.cohere`{.interpreted-text role="func"}, and
    `matplotlib.mlab.specgram`{.interpreted-text role="func"} to scale
    one-sided densities by a factor of 2. Also, optionally scale the
    densities by the sampling frequency, which gives true values of
    densities that can be integrated by the returned frequency values.
    This also gives better MATLAB compatibility. The corresponding
    `matplotlib.axes.Axes`{.interpreted-text role="class"} methods and
    `matplotlib.pyplot`{.interpreted-text role="mod"} functions were
    updated as well.

-   Font lookup now uses a nearest-neighbor approach rather than an
    exact match. Some fonts may be different in plots, but should be
    closer to what was requested.

-   `matplotlib.axes.Axes.set_xlim`{.interpreted-text role="meth"},
    `matplotlib.axes.Axes.set_ylim`{.interpreted-text role="meth"} now
    return a copy of the `viewlim` array to avoid modify-in-place
    surprises.

-   `matplotlib.afm.AFM.get_fullname` and
    `matplotlib.afm.AFM.get_familyname` no longer raise an exception if
    the AFM file does not specify these optional attributes, but returns
    a guess based on the required FontName attribute.

-   Changed precision kwarg in `matplotlib.pyplot.spy`{.interpreted-text
    role="func"}; default is 0, and the string value \'present\' is used
    for sparse arrays only to show filled locations.

-   `matplotlib.collections.EllipseCollection`{.interpreted-text
    role="class"} added.

-   Added `angles` kwarg to `matplotlib.pyplot.quiver`{.interpreted-text
    role="func"} for more flexible specification of the arrow angles.

-   Deprecated (raise NotImplementedError) all the mlab2 functions from
    `matplotlib.mlab`{.interpreted-text role="mod"} out of concern that
    some of them were not clean room implementations.

-   Methods
    `matplotlib.collections.Collection.get_offsets`{.interpreted-text
    role="meth"} and
    `matplotlib.collections.Collection.set_offsets`{.interpreted-text
    role="meth"} added to
    `~matplotlib.collections.Collection`{.interpreted-text role="class"}
    base class.

-   `matplotlib.figure.Figure.figurePatch` renamed
    `matplotlib.figure.Figure.patch`; `matplotlib.axes.Axes.axesPatch`
    renamed `matplotlib.axes.Axes.patch`;
    `matplotlib.axes.Axes.axesFrame` renamed
    `matplotlib.axes.Axes.frame`. `matplotlib.axes.Axes.get_frame`,
    which returns `matplotlib.axes.Axes.patch`, is deprecated.

-   Changes in the `matplotlib.contour.ContourLabeler`{.interpreted-text
    role="class"} attributes
    (`matplotlib.pyplot.clabel`{.interpreted-text role="func"} function)
    so that they all have a form like `.labelAttribute`. The three
    attributes that are most likely to be used by end users, `.cl`,
    `.cl_xy` and `.cl_cvalues` have been maintained for the moment (in
    addition to their renamed versions), but they are deprecated and
    will eventually be removed.

-   Moved several functions in `matplotlib.mlab`{.interpreted-text
    role="mod"} and `matplotlib.cbook`{.interpreted-text role="mod"}
    into a separate module `matplotlib.numerical_methods` because they
    were unrelated to the initial purpose of mlab or cbook and appeared
    more coherent elsewhere.

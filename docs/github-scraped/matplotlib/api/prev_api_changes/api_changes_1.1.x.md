# API Changes in 1.1.x

-   Added new `matplotlib.sankey.Sankey`{.interpreted-text role="class"}
    for generating Sankey diagrams.
-   In `~matplotlib.pyplot.imshow`{.interpreted-text role="meth"},
    setting *interpolation* to \'nearest\' will now always mean that the
    nearest-neighbor interpolation is performed. If you want the no-op
    interpolation to be performed, choose \'none\'.
-   There were errors in how the tri-functions were handling input
    parameters that had to be fixed. If your tri-plots are not working
    correctly anymore, or you were working around apparent mistakes,
    please see issue #203 in the github tracker. When in doubt, use
    kwargs.
-   The \'symlog\' scale had some bad behavior in previous versions.
    This has now been fixed and users should now be able to use it
    without frustrations. The fixes did result in some minor changes in
    appearance for some users who may have been depending on the bad
    behavior.
-   There is now a common set of markers for all plotting functions.
    Previously, some markers existed only for
    `~matplotlib.pyplot.scatter`{.interpreted-text role="meth"} or just
    for `~matplotlib.pyplot.plot`{.interpreted-text role="meth"}. This
    is now no longer the case. This merge did result in a conflict. The
    string \'d\' now means \"thin diamond\" while \'D\' will mean
    \"regular diamond\".

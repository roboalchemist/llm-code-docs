::: module
mpl_toolkits.axisartist
:::

# `mpl_toolkits.axisartist`

The *axisartist* namespace provides a derived Axes implementation
(`~mpl_toolkits.axisartist.axislines.Axes`{.interpreted-text
role="class"}), designed to support curvilinear grids. The biggest
difference is that the artists that are responsible for drawing axis
lines, ticks, ticklabels, and axis labels are separated out from
Matplotlib\'s Axis class.

You can find a tutorial describing usage of axisartist at the
`axisartist_users-guide-index`{.interpreted-text role="ref"} user guide.

![](../../gallery/axisartist/images/sphx_glr_demo_curvelinear_grid_001.png){.align-center}

::: note
::: title
Note
:::

This module contains classes and function that were formerly part of the
`mpl_toolkits.axes_grid` module that was removed in 3.6. Additional
classes from that older module may also be found in
[mpl_toolkits.axes_grid1]{.title-ref}.
:::

::: currentmodule
mpl_toolkits
:::

**The submodules of the axisartist API are:**

::: {.autosummary toctree="../_as_gen" template="automodule.rst"}
axisartist.angle_helper axisartist.axes_divider axisartist.axis_artist
axisartist.axisline_style axisartist.axislines axisartist.floating_axes
axisartist.grid_finder axisartist.grid_helper_curvelinear
axisartist.parasite_axes
:::

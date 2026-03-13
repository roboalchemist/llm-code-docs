# Source: https://seaborn.pydata.org/tutorial/objects_interface.html

Title: The seaborn.objects interface — seaborn 0.13.2 documentation

URL Source: https://seaborn.pydata.org/tutorial/objects_interface.html

Published Time: Thu, 25 Jan 2024 13:24:12 GMT

Markdown Content:
The seaborn.objects interface — seaborn 0.13.2 documentation
===============
- [x] - [x] 

Ctrl+K

[![Image 1: Logo image](https://seaborn.pydata.org/_static/logo-wide-lightbg.svg)![Image 2: Logo image](https://seaborn.pydata.org/_static/logo-wide-lightbg.svg)](https://seaborn.pydata.org/index.html)

*   [Installing](https://seaborn.pydata.org/installing.html)
*   [Gallery](https://seaborn.pydata.org/examples/index.html)
*   [Tutorial](https://seaborn.pydata.org/tutorial.html)
*   [API](https://seaborn.pydata.org/api.html)
*   [Releases](https://seaborn.pydata.org/whatsnew/index.html)
*   [Citing](https://seaborn.pydata.org/citing.html)
*   [FAQ](https://seaborn.pydata.org/faq.html)

*   [GitHub](https://github.com/mwaskom/seaborn "GitHub")
*   [StackOverflow](https://stackoverflow.com/tags/seaborn "StackOverflow")
*   [Twitter](https://twitter.com/michaelwaskom "Twitter")

Site Navigation

*   [Installing](https://seaborn.pydata.org/installing.html)
*   [Gallery](https://seaborn.pydata.org/examples/index.html)
*   [Tutorial](https://seaborn.pydata.org/tutorial.html)
*   [API](https://seaborn.pydata.org/api.html)
*   [Releases](https://seaborn.pydata.org/whatsnew/index.html)
*   [Citing](https://seaborn.pydata.org/citing.html)
*   [FAQ](https://seaborn.pydata.org/faq.html)

*   [GitHub](https://github.com/mwaskom/seaborn "GitHub")
*   [StackOverflow](https://stackoverflow.com/tags/seaborn "StackOverflow")
*   [Twitter](https://twitter.com/michaelwaskom "Twitter")

*   [An introduction to seaborn](https://seaborn.pydata.org/tutorial/introduction.html)

*   [Overview of seaborn plotting functions](https://seaborn.pydata.org/tutorial/function_overview.html)

*   [Data structures accepted by seaborn](https://seaborn.pydata.org/tutorial/data_structure.html)

*   [The seaborn.objects interface](https://seaborn.pydata.org/tutorial/objects_interface.html#)

*   [Properties of Mark objects](https://seaborn.pydata.org/tutorial/properties.html)

*   [Visualizing statistical relationships](https://seaborn.pydata.org/tutorial/relational.html)

*   [Visualizing distributions of data](https://seaborn.pydata.org/tutorial/distributions.html)

*   [Visualizing categorical data](https://seaborn.pydata.org/tutorial/categorical.html)

*   [Statistical estimation and error bars](https://seaborn.pydata.org/tutorial/error_bars.html)

*   [Estimating regression fits](https://seaborn.pydata.org/tutorial/regression.html)

*   [Building structured multi-plot grids](https://seaborn.pydata.org/tutorial/axis_grids.html)

*   [Controlling figure aesthetics](https://seaborn.pydata.org/tutorial/aesthetics.html)

*   [Choosing color palettes](https://seaborn.pydata.org/tutorial/color_palettes.html)

 On this page 

*   [Specifying a plot and mapping data](https://seaborn.pydata.org/tutorial/objects_interface.html#specifying-a-plot-and-mapping-data)
    *   [Setting properties](https://seaborn.pydata.org/tutorial/objects_interface.html#setting-properties)
    *   [Mapping properties](https://seaborn.pydata.org/tutorial/objects_interface.html#mapping-properties)
    *   [Defining groups](https://seaborn.pydata.org/tutorial/objects_interface.html#defining-groups)

*   [Transforming data before plotting](https://seaborn.pydata.org/tutorial/objects_interface.html#transforming-data-before-plotting)
    *   [Statistical transformation](https://seaborn.pydata.org/tutorial/objects_interface.html#statistical-transformation)
    *   [Resolving overplotting](https://seaborn.pydata.org/tutorial/objects_interface.html#resolving-overplotting)
    *   [Creating variables through transformation](https://seaborn.pydata.org/tutorial/objects_interface.html#creating-variables-through-transformation)
    *   [Orienting marks and transforms](https://seaborn.pydata.org/tutorial/objects_interface.html#orienting-marks-and-transforms)

*   [Building and displaying the plot](https://seaborn.pydata.org/tutorial/objects_interface.html#building-and-displaying-the-plot)
    *   [Adding multiple layers](https://seaborn.pydata.org/tutorial/objects_interface.html#adding-multiple-layers)
    *   [Layer-specific mappings](https://seaborn.pydata.org/tutorial/objects_interface.html#layer-specific-mappings)
    *   [Faceting and pairing subplots](https://seaborn.pydata.org/tutorial/objects_interface.html#faceting-and-pairing-subplots)
    *   [Integrating with matplotlib](https://seaborn.pydata.org/tutorial/objects_interface.html#integrating-with-matplotlib)
    *   [Building and displaying the plot](https://seaborn.pydata.org/tutorial/objects_interface.html#id1)

*   [Customizing the appearance](https://seaborn.pydata.org/tutorial/objects_interface.html#customizing-the-appearance)
    *   [Parameterizing scales](https://seaborn.pydata.org/tutorial/objects_interface.html#parameterizing-scales)
    *   [Customizing legends and ticks](https://seaborn.pydata.org/tutorial/objects_interface.html#customizing-legends-and-ticks)
    *   [Customizing limits, labels, and titles](https://seaborn.pydata.org/tutorial/objects_interface.html#customizing-limits-labels-and-titles)
    *   [Theme customization](https://seaborn.pydata.org/tutorial/objects_interface.html#theme-customization)

The seaborn.objects interface[#](https://seaborn.pydata.org/tutorial/objects_interface.html#the-seaborn-objects-interface "Permalink to this heading")
======================================================================================================================================================

The `seaborn.objects` namespace was introduced in version 0.12 as a completely new interface for making seaborn plots. It offers a more consistent and flexible API, comprising a collection of composable classes for transforming and plotting data. In contrast to the existing `seaborn` functions, the new interface aims to support end-to-end plot specification and customization without dropping down to matplotlib (although it will remain possible to do so if necessary).

Note

The objects interface is currently experimental and incomplete. It is stable enough for serious use, but there certainly are some rough edges and missing features.

Specifying a plot and mapping data[#](https://seaborn.pydata.org/tutorial/objects_interface.html#specifying-a-plot-and-mapping-data "Permalink to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------

The objects interface should be imported with the following convention:

import seaborn.objects as so

The `seaborn.objects` namespace will provide access to all of the relevant classes. The most important is [`Plot`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn.objects.Plot "seaborn.objects.Plot"). You specify plots by instantiating a [`Plot`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn.objects.Plot "seaborn.objects.Plot") object and calling its methods. Let’s see a simple example:

(
    so.Plot(penguins, x="bill_length_mm", y="bill_depth_mm")
    .add(so.Dot())
)

[![Image 3: ../_images/objects_interface_4_0.png](https://seaborn.pydata.org/_images/objects_interface_4_0.png)](https://seaborn.pydata.org/_images/objects_interface_4_0.png)
This code, which produces a scatter plot, should look reasonably familiar. Just as when using [`seaborn.scatterplot()`](https://seaborn.pydata.org/generated/seaborn.scatterplot.html#seaborn.scatterplot "seaborn.scatterplot"), we passed a tidy dataframe (`penguins`) and assigned two of its columns to the `x` and `y` coordinates of the plot. But instead of starting with the type of chart and then adding some data assignments, here we started with the data assignments and then added a graphical element.

### Setting properties[#](https://seaborn.pydata.org/tutorial/objects_interface.html#setting-properties "Permalink to this heading")

The [`Dot`](https://seaborn.pydata.org/generated/seaborn.objects.Dot.html#seaborn.objects.Dot "seaborn.objects.Dot") class is an example of a [`Mark`](https://seaborn.pydata.org/generated/seaborn.objects.Mark.html#seaborn.objects.Mark "seaborn.objects.Mark"): an object that graphically represents data values. Each mark will have a number of properties that can be set to change its appearance:

(
    so.Plot(penguins, x="bill_length_mm", y="bill_depth_mm")
    .add(so.Dot(color="g", pointsize=4))
)

[![Image 4: ../_images/objects_interface_6_0.png](https://seaborn.pydata.org/_images/objects_interface_6_0.png)](https://seaborn.pydata.org/_images/objects_interface_6_0.png)
### Mapping properties[#](https://seaborn.pydata.org/tutorial/objects_interface.html#mapping-properties "Permalink to this heading")

As with seaborn’s functions, it is also possible to _map_ data values to various graphical properties:

(
    so.Plot(
        penguins, x="bill_length_mm", y="bill_depth_mm",
        color="species", pointsize="body_mass_g",
    )
    .add(so.Dot())
)

[![Image 5: ../_images/objects_interface_8_0.png](https://seaborn.pydata.org/_images/objects_interface_8_0.png)](https://seaborn.pydata.org/_images/objects_interface_8_0.png)
While this basic functionality is not novel, an important difference from the function API is that properties are mapped using the same parameter names that would set them directly (instead of having `hue` vs. `color`, etc.). What matters is _where_ the property is defined: passing a value when you initialize [`Dot`](https://seaborn.pydata.org/generated/seaborn.objects.Dot.html#seaborn.objects.Dot "seaborn.objects.Dot") will set it directly, whereas assigning a variable when you set up the [`Plot`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn.objects.Plot "seaborn.objects.Plot") will _map_ the corresponding data.

Beyond this difference, the objects interface also allows a much wider range of mark properties to be mapped:

(
    so.Plot(
        penguins, x="bill_length_mm", y="bill_depth_mm",
        edgecolor="sex", edgewidth="body_mass_g",
    )
    .add(so.Dot(color=".8"))
)

[![Image 6: ../_images/objects_interface_10_0.png](https://seaborn.pydata.org/_images/objects_interface_10_0.png)](https://seaborn.pydata.org/_images/objects_interface_10_0.png)
### Defining groups[#](https://seaborn.pydata.org/tutorial/objects_interface.html#defining-groups "Permalink to this heading")

The [`Dot`](https://seaborn.pydata.org/generated/seaborn.objects.Dot.html#seaborn.objects.Dot "seaborn.objects.Dot") mark represents each data point independently, so the assignment of a variable to a property only has the effect of changing each dot’s appearance. For marks that group or connect observations, such as [`Line`](https://seaborn.pydata.org/generated/seaborn.objects.Line.html#seaborn.objects.Line "seaborn.objects.Line"), it also determines the number of distinct graphical elements:

(
    so.Plot(healthexp, x="Year", y="Life_Expectancy", color="Country")
    .add(so.Line())
)

[![Image 7: ../_images/objects_interface_12_0.png](https://seaborn.pydata.org/_images/objects_interface_12_0.png)](https://seaborn.pydata.org/_images/objects_interface_12_0.png)
It is also possible to define a grouping without changing any visual properties, by using `group`:

(
    so.Plot(healthexp, x="Year", y="Life_Expectancy", group="Country")
    .add(so.Line())
)

[![Image 8: ../_images/objects_interface_14_0.png](https://seaborn.pydata.org/_images/objects_interface_14_0.png)](https://seaborn.pydata.org/_images/objects_interface_14_0.png)
Transforming data before plotting[#](https://seaborn.pydata.org/tutorial/objects_interface.html#transforming-data-before-plotting "Permalink to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------

### Statistical transformation[#](https://seaborn.pydata.org/tutorial/objects_interface.html#statistical-transformation "Permalink to this heading")

As with many seaborn functions, the objects interface supports statistical transformations. These are performed by [`Stat`](https://seaborn.pydata.org/generated/seaborn.objects.Stat.html#seaborn.objects.Stat "seaborn.objects.Stat") objects, such as [`Agg`](https://seaborn.pydata.org/generated/seaborn.objects.Agg.html#seaborn.objects.Agg "seaborn.objects.Agg"):

(
    so.Plot(penguins, x="species", y="body_mass_g")
    .add(so.Bar(), so.Agg())
)

[![Image 9: ../_images/objects_interface_16_0.png](https://seaborn.pydata.org/_images/objects_interface_16_0.png)](https://seaborn.pydata.org/_images/objects_interface_16_0.png)
In the function interface, statistical transformations are possible with some visual representations (e.g. [`seaborn.barplot()`](https://seaborn.pydata.org/generated/seaborn.barplot.html#seaborn.barplot "seaborn.barplot")) but not others (e.g. [`seaborn.scatterplot()`](https://seaborn.pydata.org/generated/seaborn.scatterplot.html#seaborn.scatterplot "seaborn.scatterplot")). The objects interface more cleanly separates representation and transformation, allowing you to compose [`Mark`](https://seaborn.pydata.org/generated/seaborn.objects.Mark.html#seaborn.objects.Mark "seaborn.objects.Mark") and [`Stat`](https://seaborn.pydata.org/generated/seaborn.objects.Stat.html#seaborn.objects.Stat "seaborn.objects.Stat") objects:

(
    so.Plot(penguins, x="species", y="body_mass_g")
    .add(so.Dot(pointsize=10), so.Agg())
)

[![Image 10: ../_images/objects_interface_18_0.png](https://seaborn.pydata.org/_images/objects_interface_18_0.png)](https://seaborn.pydata.org/_images/objects_interface_18_0.png)
When forming groups by mapping properties, the [`Stat`](https://seaborn.pydata.org/generated/seaborn.objects.Stat.html#seaborn.objects.Stat "seaborn.objects.Stat") transformation is applied to each group separately:

(
    so.Plot(penguins, x="species", y="body_mass_g", color="sex")
    .add(so.Dot(pointsize=10), so.Agg())
)

[![Image 11: ../_images/objects_interface_20_0.png](https://seaborn.pydata.org/_images/objects_interface_20_0.png)](https://seaborn.pydata.org/_images/objects_interface_20_0.png)
### Resolving overplotting[#](https://seaborn.pydata.org/tutorial/objects_interface.html#resolving-overplotting "Permalink to this heading")

Some seaborn functions also have mechanisms that automatically resolve overplotting, as when [`seaborn.barplot()`](https://seaborn.pydata.org/generated/seaborn.barplot.html#seaborn.barplot "seaborn.barplot") “dodges” bars once `hue` is assigned. The objects interface has less complex default behavior. Bars representing multiple groups will overlap by default:

(
    so.Plot(penguins, x="species", y="body_mass_g", color="sex")
    .add(so.Bar(), so.Agg())
)

[![Image 12: ../_images/objects_interface_22_0.png](https://seaborn.pydata.org/_images/objects_interface_22_0.png)](https://seaborn.pydata.org/_images/objects_interface_22_0.png)
Nevertheless, it is possible to compose the [`Bar`](https://seaborn.pydata.org/generated/seaborn.objects.Bar.html#seaborn.objects.Bar "seaborn.objects.Bar") mark with the [`Agg`](https://seaborn.pydata.org/generated/seaborn.objects.Agg.html#seaborn.objects.Agg "seaborn.objects.Agg") stat and a second transformation, implemented by [`Dodge`](https://seaborn.pydata.org/generated/seaborn.objects.Dodge.html#seaborn.objects.Dodge "seaborn.objects.Dodge"):

(
    so.Plot(penguins, x="species", y="body_mass_g", color="sex")
    .add(so.Bar(), so.Agg(), so.Dodge())
)

[![Image 13: ../_images/objects_interface_24_0.png](https://seaborn.pydata.org/_images/objects_interface_24_0.png)](https://seaborn.pydata.org/_images/objects_interface_24_0.png)
The [`Dodge`](https://seaborn.pydata.org/generated/seaborn.objects.Dodge.html#seaborn.objects.Dodge "seaborn.objects.Dodge") class is an example of a [`Move`](https://seaborn.pydata.org/generated/seaborn.objects.Move.html#seaborn.objects.Move "seaborn.objects.Move") transformation, which is like a [`Stat`](https://seaborn.pydata.org/generated/seaborn.objects.Stat.html#seaborn.objects.Stat "seaborn.objects.Stat") but only adjusts `x` and `y` coordinates. The [`Move`](https://seaborn.pydata.org/generated/seaborn.objects.Move.html#seaborn.objects.Move "seaborn.objects.Move") classes can be applied with any mark, and it’s not necessary to use a [`Stat`](https://seaborn.pydata.org/generated/seaborn.objects.Stat.html#seaborn.objects.Stat "seaborn.objects.Stat") first:

(
    so.Plot(penguins, x="species", y="body_mass_g", color="sex")
    .add(so.Dot(), so.Dodge())
)

[![Image 14: ../_images/objects_interface_26_0.png](https://seaborn.pydata.org/_images/objects_interface_26_0.png)](https://seaborn.pydata.org/_images/objects_interface_26_0.png)
It’s also possible to apply multiple [`Move`](https://seaborn.pydata.org/generated/seaborn.objects.Move.html#seaborn.objects.Move "seaborn.objects.Move") operations in sequence:

(
    so.Plot(penguins, x="species", y="body_mass_g", color="sex")
    .add(so.Dot(), so.Dodge(), so.Jitter(.3))
)

[![Image 15: ../_images/objects_interface_28_0.png](https://seaborn.pydata.org/_images/objects_interface_28_0.png)](https://seaborn.pydata.org/_images/objects_interface_28_0.png)
### Creating variables through transformation[#](https://seaborn.pydata.org/tutorial/objects_interface.html#creating-variables-through-transformation "Permalink to this heading")

The [`Agg`](https://seaborn.pydata.org/generated/seaborn.objects.Agg.html#seaborn.objects.Agg "seaborn.objects.Agg") stat requires both `x` and `y` to already be defined, but variables can also be _created_ through statistical transformation. For example, the [`Hist`](https://seaborn.pydata.org/generated/seaborn.objects.Hist.html#seaborn.objects.Hist "seaborn.objects.Hist") stat requires only one of `x`_or_`y` to be defined, and it will create the other by counting observations:

(
    so.Plot(penguins, x="species")
    .add(so.Bar(), so.Hist())
)

[![Image 16: ../_images/objects_interface_30_0.png](https://seaborn.pydata.org/_images/objects_interface_30_0.png)](https://seaborn.pydata.org/_images/objects_interface_30_0.png)
The [`Hist`](https://seaborn.pydata.org/generated/seaborn.objects.Hist.html#seaborn.objects.Hist "seaborn.objects.Hist") stat will also create new `x` values (by binning) when given numeric data:

(
    so.Plot(penguins, x="flipper_length_mm")
    .add(so.Bars(), so.Hist())
)

[![Image 17: ../_images/objects_interface_32_0.png](https://seaborn.pydata.org/_images/objects_interface_32_0.png)](https://seaborn.pydata.org/_images/objects_interface_32_0.png)
Notice how we used [`Bars`](https://seaborn.pydata.org/generated/seaborn.objects.Bars.html#seaborn.objects.Bars "seaborn.objects.Bars"), rather than [`Bar`](https://seaborn.pydata.org/generated/seaborn.objects.Bar.html#seaborn.objects.Bar "seaborn.objects.Bar") for the plot with the continuous `x` axis. These two marks are related, but [`Bars`](https://seaborn.pydata.org/generated/seaborn.objects.Bars.html#seaborn.objects.Bars "seaborn.objects.Bars") has different defaults and works better for continuous histograms. It also produces a different, more efficient matplotlib artist. You will find the pattern of singular/plural marks elsewhere. The plural version is typically optimized for cases with larger numbers of marks.

Some transforms accept both `x` and `y`, but add _interval_ data for each coordinate. This is particularly relevant for plotting error bars after aggregating:

(
    so.Plot(penguins, x="body_mass_g", y="species", color="sex")
    .add(so.Range(), so.Est(errorbar="sd"), so.Dodge())
    .add(so.Dot(), so.Agg(), so.Dodge())
)

[![Image 18: ../_images/objects_interface_34_0.png](https://seaborn.pydata.org/_images/objects_interface_34_0.png)](https://seaborn.pydata.org/_images/objects_interface_34_0.png)
### Orienting marks and transforms[#](https://seaborn.pydata.org/tutorial/objects_interface.html#orienting-marks-and-transforms "Permalink to this heading")

When aggregating, dodging, and drawing a bar, the `x` and `y` variables are treated differently. Each operation has the concept of an _orientation_. The [`Plot`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn.objects.Plot "seaborn.objects.Plot") tries to determine the orientation automatically based on the data types of the variables. For instance, if we flip the assignment of `species` and `body_mass_g`, we’ll get the same plot, but oriented horizontally:

(
    so.Plot(penguins, x="body_mass_g", y="species", color="sex")
    .add(so.Bar(), so.Agg(), so.Dodge())
)

[![Image 19: ../_images/objects_interface_36_0.png](https://seaborn.pydata.org/_images/objects_interface_36_0.png)](https://seaborn.pydata.org/_images/objects_interface_36_0.png)
Sometimes, the correct orientation is ambiguous, as when both the `x` and `y` variables are numeric. In these cases, you can be explicit by passing the `orient` parameter to [`Plot.add()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.add.html#seaborn.objects.Plot.add "seaborn.objects.Plot.add"):

(
    so.Plot(tips, x="total_bill", y="size", color="time")
    .add(so.Bar(), so.Agg(), so.Dodge(), orient="y")
)

[![Image 20: ../_images/objects_interface_38_0.png](https://seaborn.pydata.org/_images/objects_interface_38_0.png)](https://seaborn.pydata.org/_images/objects_interface_38_0.png)
Building and displaying the plot[#](https://seaborn.pydata.org/tutorial/objects_interface.html#building-and-displaying-the-plot "Permalink to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------

Most examples this far have produced a single subplot with just one kind of mark on it. But [`Plot`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn.objects.Plot "seaborn.objects.Plot") does not limit you to this.

### Adding multiple layers[#](https://seaborn.pydata.org/tutorial/objects_interface.html#adding-multiple-layers "Permalink to this heading")

More complex single-subplot graphics can be created by calling [`Plot.add()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.add.html#seaborn.objects.Plot.add "seaborn.objects.Plot.add") repeatedly. Each time it is called, it defines a _layer_ in the plot. For example, we may want to add a scatterplot (now using [`Dots`](https://seaborn.pydata.org/generated/seaborn.objects.Dots.html#seaborn.objects.Dots "seaborn.objects.Dots")) and then a regression fit:

(
    so.Plot(tips, x="total_bill", y="tip")
    .add(so.Dots())
    .add(so.Line(), so.PolyFit())
)

[![Image 21: ../_images/objects_interface_40_0.png](https://seaborn.pydata.org/_images/objects_interface_40_0.png)](https://seaborn.pydata.org/_images/objects_interface_40_0.png)
Variable mappings that are defined in the [`Plot`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn.objects.Plot "seaborn.objects.Plot") constructor will be used for all layers:

(
    so.Plot(tips, x="total_bill", y="tip", color="time")
    .add(so.Dots())
    .add(so.Line(), so.PolyFit())
)

[![Image 22: ../_images/objects_interface_42_0.png](https://seaborn.pydata.org/_images/objects_interface_42_0.png)](https://seaborn.pydata.org/_images/objects_interface_42_0.png)
### Layer-specific mappings[#](https://seaborn.pydata.org/tutorial/objects_interface.html#layer-specific-mappings "Permalink to this heading")

You can also define a mapping such that it is used only in a specific layer. This is accomplished by defining the mapping within the call to [`Plot.add`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.add.html#seaborn.objects.Plot.add "seaborn.objects.Plot.add") for the relevant layer:

(
    so.Plot(tips, x="total_bill", y="tip")
    .add(so.Dots(), color="time")
    .add(so.Line(color=".2"), so.PolyFit())
)

[![Image 23: ../_images/objects_interface_44_0.png](https://seaborn.pydata.org/_images/objects_interface_44_0.png)](https://seaborn.pydata.org/_images/objects_interface_44_0.png)
Alternatively, define the layer for the entire plot, but _remove_ it from a specific layer by setting the variable to `None`:

(
    so.Plot(tips, x="total_bill", y="tip", color="time")
    .add(so.Dots())
    .add(so.Line(color=".2"), so.PolyFit(), color=None)
)

[![Image 24: ../_images/objects_interface_46_0.png](https://seaborn.pydata.org/_images/objects_interface_46_0.png)](https://seaborn.pydata.org/_images/objects_interface_46_0.png)
To recap, there are three ways to specify the value of a mark property: (1) by mapping a variable in all layers, (2) by mapping a variable in a specific layer, and (3) by setting the property directly:

![Image 25: ../_images/objects_interface_48_0.svg](https://seaborn.pydata.org/_images/objects_interface_48_0.svg)
### Faceting and pairing subplots[#](https://seaborn.pydata.org/tutorial/objects_interface.html#faceting-and-pairing-subplots "Permalink to this heading")

As with seaborn’s figure-level functions ([`seaborn.displot()`](https://seaborn.pydata.org/generated/seaborn.displot.html#seaborn.displot "seaborn.displot"), [`seaborn.catplot()`](https://seaborn.pydata.org/generated/seaborn.catplot.html#seaborn.catplot "seaborn.catplot"), etc.), the [`Plot`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn.objects.Plot "seaborn.objects.Plot") interface can also produce figures with multiple “facets”, or subplots containing subsets of data. This is accomplished with the [`Plot.facet()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.facet.html#seaborn.objects.Plot.facet "seaborn.objects.Plot.facet") method:

(
    so.Plot(penguins, x="flipper_length_mm")
    .facet("species")
    .add(so.Bars(), so.Hist())
)

[![Image 26: ../_images/objects_interface_50_0.png](https://seaborn.pydata.org/_images/objects_interface_50_0.png)](https://seaborn.pydata.org/_images/objects_interface_50_0.png)
Call [`Plot.facet()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.facet.html#seaborn.objects.Plot.facet "seaborn.objects.Plot.facet") with the variables that should be used to define the columns and/or rows of the plot:

(
    so.Plot(penguins, x="flipper_length_mm")
    .facet(col="species", row="sex")
    .add(so.Bars(), so.Hist())
)

[![Image 27: ../_images/objects_interface_52_0.png](https://seaborn.pydata.org/_images/objects_interface_52_0.png)](https://seaborn.pydata.org/_images/objects_interface_52_0.png)
You can facet using a variable with a larger number of levels by “wrapping” across the other dimension:

(
    so.Plot(healthexp, x="Year", y="Life_Expectancy")
    .facet(col="Country", wrap=3)
    .add(so.Line())
)

[![Image 28: ../_images/objects_interface_54_0.png](https://seaborn.pydata.org/_images/objects_interface_54_0.png)](https://seaborn.pydata.org/_images/objects_interface_54_0.png)
All layers will be faceted unless you explicitly exclude them, which can be useful for providing additional context on each subplot:

(
    so.Plot(healthexp, x="Year", y="Life_Expectancy")
    .facet("Country", wrap=3)
    .add(so.Line(alpha=.3), group="Country", col=None)
    .add(so.Line(linewidth=3))
)

[![Image 29: ../_images/objects_interface_56_0.png](https://seaborn.pydata.org/_images/objects_interface_56_0.png)](https://seaborn.pydata.org/_images/objects_interface_56_0.png)
An alternate way to produce subplots is [`Plot.pair()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.pair.html#seaborn.objects.Plot.pair "seaborn.objects.Plot.pair"). Like [`seaborn.PairGrid`](https://seaborn.pydata.org/generated/seaborn.PairGrid.html#seaborn.PairGrid "seaborn.PairGrid"), this draws all of the data on each subplot, using different variables for the x and/or y coordinates:

(
    so.Plot(penguins, y="body_mass_g", color="species")
    .pair(x=["bill_length_mm", "bill_depth_mm"])
    .add(so.Dots())
)

[![Image 30: ../_images/objects_interface_58_0.png](https://seaborn.pydata.org/_images/objects_interface_58_0.png)](https://seaborn.pydata.org/_images/objects_interface_58_0.png)
You can combine faceting and pairing so long as the operations add subplots on opposite dimensions:

(
    so.Plot(penguins, y="body_mass_g", color="species")
    .pair(x=["bill_length_mm", "bill_depth_mm"])
    .facet(row="sex")
    .add(so.Dots())
)

[![Image 31: ../_images/objects_interface_60_0.png](https://seaborn.pydata.org/_images/objects_interface_60_0.png)](https://seaborn.pydata.org/_images/objects_interface_60_0.png)
### Integrating with matplotlib[#](https://seaborn.pydata.org/tutorial/objects_interface.html#integrating-with-matplotlib "Permalink to this heading")

There may be cases where you want multiple subplots to appear in a figure with a more complex structure than what [`Plot.facet()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.facet.html#seaborn.objects.Plot.facet "seaborn.objects.Plot.facet") or [`Plot.pair()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.pair.html#seaborn.objects.Plot.pair "seaborn.objects.Plot.pair") can provide. The current solution is to delegate figure setup to matplotlib and to supply the matplotlib object that [`Plot`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn.objects.Plot "seaborn.objects.Plot") should use with the [`Plot.on()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.on.html#seaborn.objects.Plot.on "seaborn.objects.Plot.on") method. This object can be either a [`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.8.2)"), [`matplotlib.figure.Figure`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure "(in Matplotlib v3.8.2)"), or [`matplotlib.figure.SubFigure`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.SubFigure "(in Matplotlib v3.8.2)"); the latter is most useful for constructing bespoke subplot layouts:

f = mpl.figure.Figure(figsize=(8, 4))
sf1, sf2 = f.subfigures(1, 2)
(
    so.Plot(penguins, x="body_mass_g", y="flipper_length_mm")
    .add(so.Dots())
    .on(sf1)
    .plot()
)
(
    so.Plot(penguins, x="body_mass_g")
    .facet(row="sex")
    .add(so.Bars(), so.Hist())
    .on(sf2)
    .plot()
)

[![Image 32: ../_images/objects_interface_62_0.png](https://seaborn.pydata.org/_images/objects_interface_62_0.png)](https://seaborn.pydata.org/_images/objects_interface_62_0.png)
### Building and displaying the plot[#](https://seaborn.pydata.org/tutorial/objects_interface.html#id1 "Permalink to this heading")

An important thing to know is that [`Plot`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn.objects.Plot "seaborn.objects.Plot") methods clone the object they are called on and return that clone instead of updating the object in place. This means that you can define a common plot spec and then produce several variations on it.

So, take this basic specification:

p = so.Plot(healthexp, "Year", "Spending_USD", color="Country")

We could use it to draw a line plot:

p.add(so.Line())

[![Image 33: ../_images/objects_interface_66_0.png](https://seaborn.pydata.org/_images/objects_interface_66_0.png)](https://seaborn.pydata.org/_images/objects_interface_66_0.png)
Or perhaps a stacked area plot:

p.add(so.Area(), so.Stack())

[![Image 34: ../_images/objects_interface_68_0.png](https://seaborn.pydata.org/_images/objects_interface_68_0.png)](https://seaborn.pydata.org/_images/objects_interface_68_0.png)
The [`Plot`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn.objects.Plot "seaborn.objects.Plot") methods are fully declarative. Calling them updates the plot spec, but it doesn’t actually do any plotting. One consequence of this is that methods can be called in any order, and many of them can be called multiple times.

When does the plot actually get rendered? [`Plot`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn.objects.Plot "seaborn.objects.Plot") is optimized for use in notebook environments. The rendering is automatically triggered when the [`Plot`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn.objects.Plot "seaborn.objects.Plot") gets displayed in the Jupyter REPL. That’s why we didn’t see anything in the example above, where we defined a [`Plot`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn.objects.Plot "seaborn.objects.Plot") but assigned it to `p` rather than letting it return out to the REPL.

To see a plot in a notebook, either return it from the final line of a cell or call Jupyter’s built-in `display` function on the object. The notebook integration bypasses [`matplotlib.pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "(in Matplotlib v3.8.2)") entirely, but you can use its figure-display machinery in other contexts by calling [`Plot.show()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.show.html#seaborn.objects.Plot.show "seaborn.objects.Plot.show").

You can also save the plot to a file (or buffer) by calling [`Plot.save()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.save.html#seaborn.objects.Plot.save "seaborn.objects.Plot.save").

Customizing the appearance[#](https://seaborn.pydata.org/tutorial/objects_interface.html#customizing-the-appearance "Permalink to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------

The new interface aims to support a deep amount of customization through [`Plot`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn.objects.Plot "seaborn.objects.Plot"), reducing the need to switch gears and use matplotlib functionality directly. (But please be patient; not all of the features needed to achieve this goal have been implemented!)

### Parameterizing scales[#](https://seaborn.pydata.org/tutorial/objects_interface.html#parameterizing-scales "Permalink to this heading")

All of the data-dependent properties are controlled by the concept of a [`Scale`](https://seaborn.pydata.org/generated/seaborn.objects.Scale.html#seaborn.objects.Scale "seaborn.objects.Scale") and the [`Plot.scale()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.scale.html#seaborn.objects.Plot.scale "seaborn.objects.Plot.scale") method. This method accepts several different types of arguments. One possibility, which is closest to the use of scales in matplotlib, is to pass the name of a function that transforms the coordinates:

(
    so.Plot(diamonds, x="carat", y="price")
    .add(so.Dots())
    .scale(y="log")
)

[![Image 35: ../_images/objects_interface_71_0.png](https://seaborn.pydata.org/_images/objects_interface_71_0.png)](https://seaborn.pydata.org/_images/objects_interface_71_0.png)
[`Plot.scale()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.scale.html#seaborn.objects.Plot.scale "seaborn.objects.Plot.scale") can also control the mappings for semantic properties like `color`. You can directly pass it any argument that you would pass to the `palette` parameter in seaborn’s function interface:

(
    so.Plot(diamonds, x="carat", y="price", color="clarity")
    .add(so.Dots())
    .scale(color="flare")
)

[![Image 36: ../_images/objects_interface_73_0.png](https://seaborn.pydata.org/_images/objects_interface_73_0.png)](https://seaborn.pydata.org/_images/objects_interface_73_0.png)
Another option is to provide a tuple of `(min, max)` values, controlling the range that the scale should map into. This works both for numeric properties and for colors:

(
    so.Plot(diamonds, x="carat", y="price", color="clarity", pointsize="carat")
    .add(so.Dots())
    .scale(color=("#88c", "#555"), pointsize=(2, 10))
)

[![Image 37: ../_images/objects_interface_75_0.png](https://seaborn.pydata.org/_images/objects_interface_75_0.png)](https://seaborn.pydata.org/_images/objects_interface_75_0.png)
For additional control, you can pass a [`Scale`](https://seaborn.pydata.org/generated/seaborn.objects.Scale.html#seaborn.objects.Scale "seaborn.objects.Scale") object. There are several different types of [`Scale`](https://seaborn.pydata.org/generated/seaborn.objects.Scale.html#seaborn.objects.Scale "seaborn.objects.Scale"), each with appropriate parameters. For example, [`Continuous`](https://seaborn.pydata.org/generated/seaborn.objects.Continuous.html#seaborn.objects.Continuous "seaborn.objects.Continuous") lets you define the input domain (`norm`), the output range (`values`), and the function that maps between them (`trans`), while [`Nominal`](https://seaborn.pydata.org/generated/seaborn.objects.Nominal.html#seaborn.objects.Nominal "seaborn.objects.Nominal") allows you to specify an ordering:

(
    so.Plot(diamonds, x="carat", y="price", color="carat", marker="cut")
    .add(so.Dots())
    .scale(
        color=so.Continuous("crest", norm=(0, 3), trans="sqrt"),
        marker=so.Nominal(["o", "+", "x"], order=["Ideal", "Premium", "Good"]),
    )
)

[![Image 38: ../_images/objects_interface_77_0.png](https://seaborn.pydata.org/_images/objects_interface_77_0.png)](https://seaborn.pydata.org/_images/objects_interface_77_0.png)
### Customizing legends and ticks[#](https://seaborn.pydata.org/tutorial/objects_interface.html#customizing-legends-and-ticks "Permalink to this heading")

The [`Scale`](https://seaborn.pydata.org/generated/seaborn.objects.Scale.html#seaborn.objects.Scale "seaborn.objects.Scale") objects are also how you specify which values should appear as tick labels / in the legend, along with how they appear. For example, the [`Continuous.tick()`](https://seaborn.pydata.org/generated/seaborn.objects.Continuous.html#seaborn.objects.Continuous.tick "seaborn.objects.Continuous.tick") method lets you control the density or locations of the ticks, and the [`Continuous.label()`](https://seaborn.pydata.org/generated/seaborn.objects.Continuous.html#seaborn.objects.Continuous.label "seaborn.objects.Continuous.label") method lets you modify the format:

(
    so.Plot(diamonds, x="carat", y="price", color="carat")
    .add(so.Dots())
    .scale(
        x=so.Continuous().tick(every=0.5),
        y=so.Continuous().label(like="${x:.0f}"),
        color=so.Continuous().tick(at=[1, 2, 3, 4]),
    )
)

[![Image 39: ../_images/objects_interface_79_0.png](https://seaborn.pydata.org/_images/objects_interface_79_0.png)](https://seaborn.pydata.org/_images/objects_interface_79_0.png)
### Customizing limits, labels, and titles[#](https://seaborn.pydata.org/tutorial/objects_interface.html#customizing-limits-labels-and-titles "Permalink to this heading")

[`Plot`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn.objects.Plot "seaborn.objects.Plot") has a number of methods for simple customization, including [`Plot.label()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.label.html#seaborn.objects.Plot.label "seaborn.objects.Plot.label"), [`Plot.limit()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.limit.html#seaborn.objects.Plot.limit "seaborn.objects.Plot.limit"), and [`Plot.share()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.share.html#seaborn.objects.Plot.share "seaborn.objects.Plot.share"):

(
    so.Plot(penguins, x="body_mass_g", y="species", color="island")
    .facet(col="sex")
    .add(so.Dot(), so.Jitter(.5))
    .share(x=False)
    .limit(y=(2.5, -.5))
    .label(
        x="Body mass (g)", y="",
        color=str.capitalize,
        title="{} penguins".format,
    )
)

[![Image 40: ../_images/objects_interface_81_0.png](https://seaborn.pydata.org/_images/objects_interface_81_0.png)](https://seaborn.pydata.org/_images/objects_interface_81_0.png)
### Theme customization[#](https://seaborn.pydata.org/tutorial/objects_interface.html#theme-customization "Permalink to this heading")

Finally, [`Plot`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn.objects.Plot "seaborn.objects.Plot") supports data-independent theming through the [`Plot.theme`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.theme.html#seaborn.objects.Plot.theme "seaborn.objects.Plot.theme") method. Currently, this method accepts a dictionary of matplotlib rc parameters. You can set them directly and/or pass a package of parameters from seaborn’s theming functions:

from seaborn import axes_style
theme_dict = {**axes_style("whitegrid"), "grid.linestyle": ":"}
so.Plot().theme(theme_dict)

[![Image 41: ../_images/objects_interface_83_0.png](https://seaborn.pydata.org/_images/objects_interface_83_0.png)](https://seaborn.pydata.org/_images/objects_interface_83_0.png)
To change the theme for all [`Plot`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn.objects.Plot "seaborn.objects.Plot") instances, update the settings in `Plot.config`:

so.Plot.config.theme.update(theme_dict)

© Copyright 2012-2024, [Michael Waskom](https://mwaskom.github.io/).

 Created using [Sphinx](https://www.sphinx-doc.org/) and the [PyData Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/).

[Archive](https://seaborn.pydata.org/tutorial/objects_interface.html#)

[v0.12](https://seaborn.pydata.org/archive/0.12/index.html)[v0.11](https://seaborn.pydata.org/archive/0.11/index.html)[v0.10](https://seaborn.pydata.org/archive/0.10/index.html)[v0.9](https://seaborn.pydata.org/archive/0.9/index.html)

v0.13.2

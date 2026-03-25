# Source: https://seaborn.pydata.org/tutorial.html

Title: User guide and tutorial — seaborn 0.13.2 documentation

URL Source: https://seaborn.pydata.org/tutorial.html

Markdown Content:
User guide and tutorial — seaborn 0.13.2 documentation
===============
- [x] - [x] 

Ctrl+K

[![Image 1: Logo image](https://seaborn.pydata.org/_static/logo-wide-lightbg.svg)![Image 2: Logo image](https://seaborn.pydata.org/_static/logo-wide-lightbg.svg)](https://seaborn.pydata.org/index.html)

*   [Installing](https://seaborn.pydata.org/installing.html)
*   [Gallery](https://seaborn.pydata.org/examples/index.html)
*   [Tutorial](https://seaborn.pydata.org/tutorial.html#)
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
*   [Tutorial](https://seaborn.pydata.org/tutorial.html#)
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

*   [The seaborn.objects interface](https://seaborn.pydata.org/tutorial/objects_interface.html)

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

*   [API Overview](https://seaborn.pydata.org/tutorial.html#api-overview)

*   [Objects interface](https://seaborn.pydata.org/tutorial.html#objects-interface)

*   [Plotting functions](https://seaborn.pydata.org/tutorial.html#plotting-functions)

*   [Statistical operations](https://seaborn.pydata.org/tutorial.html#statistical-operations)

*   [Multi-plot grids](https://seaborn.pydata.org/tutorial.html#multi-plot-grids)
*   [Figure aesthetics](https://seaborn.pydata.org/tutorial.html#figure-aesthetics)

User guide and tutorial[#](https://seaborn.pydata.org/tutorial.html#user-guide-and-tutorial "Permalink to this heading")
========================================================================================================================

[![Image 3: _images/introduction.svg](https://seaborn.pydata.org/_images/introduction.svg)](https://seaborn.pydata.org/tutorial/introduction.html)

*   [An introduction to seaborn](https://seaborn.pydata.org/tutorial/introduction.html)
    *   [A high-level API for statistical graphics](https://seaborn.pydata.org/tutorial/introduction.html#a-high-level-api-for-statistical-graphics)
    *   [Multivariate views on complex datasets](https://seaborn.pydata.org/tutorial/introduction.html#multivariate-views-on-complex-datasets)
    *   [Opinionated defaults and flexible customization](https://seaborn.pydata.org/tutorial/introduction.html#opinionated-defaults-and-flexible-customization)

API Overview[#](https://seaborn.pydata.org/tutorial.html#api-overview "Permalink to this heading")
--------------------------------------------------------------------------------------------------

[![Image 4: _images/function_overview.svg](https://seaborn.pydata.org/_images/function_overview.svg)](https://seaborn.pydata.org/tutorial/function_overview.html)

*   [Overview of seaborn plotting functions](https://seaborn.pydata.org/tutorial/function_overview.html)
    *   [Similar functions for similar tasks](https://seaborn.pydata.org/tutorial/function_overview.html#similar-functions-for-similar-tasks)
    *   [Figure-level vs. axes-level functions](https://seaborn.pydata.org/tutorial/function_overview.html#figure-level-vs-axes-level-functions)
    *   [Combining multiple views on the data](https://seaborn.pydata.org/tutorial/function_overview.html#combining-multiple-views-on-the-data)

[![Image 5: _images/data_structure.svg](https://seaborn.pydata.org/_images/data_structure.svg)](https://seaborn.pydata.org/tutorial/data_structure.html)

*   [Data structures accepted by seaborn](https://seaborn.pydata.org/tutorial/data_structure.html)
    *   [Long-form vs. wide-form data](https://seaborn.pydata.org/tutorial/data_structure.html#long-form-vs-wide-form-data)
    *   [Options for visualizing long-form data](https://seaborn.pydata.org/tutorial/data_structure.html#options-for-visualizing-long-form-data)
    *   [Options for visualizing wide-form data](https://seaborn.pydata.org/tutorial/data_structure.html#options-for-visualizing-wide-form-data)

Objects interface[#](https://seaborn.pydata.org/tutorial.html#objects-interface "Permalink to this heading")
------------------------------------------------------------------------------------------------------------

[![Image 6: _images/objects_interface.svg](https://seaborn.pydata.org/_images/objects_interface.svg)](https://seaborn.pydata.org/tutorial/objects_interface.html)

*   [The seaborn.objects interface](https://seaborn.pydata.org/tutorial/objects_interface.html)
    *   [Specifying a plot and mapping data](https://seaborn.pydata.org/tutorial/objects_interface.html#specifying-a-plot-and-mapping-data)
    *   [Transforming data before plotting](https://seaborn.pydata.org/tutorial/objects_interface.html#transforming-data-before-plotting)
    *   [Building and displaying the plot](https://seaborn.pydata.org/tutorial/objects_interface.html#building-and-displaying-the-plot)
    *   [Customizing the appearance](https://seaborn.pydata.org/tutorial/objects_interface.html#customizing-the-appearance)

[![Image 7: _images/properties.svg](https://seaborn.pydata.org/_images/properties.svg)](https://seaborn.pydata.org/tutorial/properties.html)

*   [Properties of Mark objects](https://seaborn.pydata.org/tutorial/properties.html)
    *   [Coordinate properties](https://seaborn.pydata.org/tutorial/properties.html#coordinate-properties)
    *   [Color properties](https://seaborn.pydata.org/tutorial/properties.html#color-properties)
    *   [Style properties](https://seaborn.pydata.org/tutorial/properties.html#style-properties)
    *   [Size properties](https://seaborn.pydata.org/tutorial/properties.html#size-properties)
    *   [Text properties](https://seaborn.pydata.org/tutorial/properties.html#text-properties)
    *   [Other properties](https://seaborn.pydata.org/tutorial/properties.html#other-properties)

Plotting functions[#](https://seaborn.pydata.org/tutorial.html#plotting-functions "Permalink to this heading")
--------------------------------------------------------------------------------------------------------------

[![Image 8: _images/relational.svg](https://seaborn.pydata.org/_images/relational.svg)](https://seaborn.pydata.org/tutorial/relational.html)

*   [Visualizing statistical relationships](https://seaborn.pydata.org/tutorial/relational.html)
    *   [Relating variables with scatter plots](https://seaborn.pydata.org/tutorial/relational.html#relating-variables-with-scatter-plots)
    *   [Emphasizing continuity with line plots](https://seaborn.pydata.org/tutorial/relational.html#emphasizing-continuity-with-line-plots)
    *   [Showing multiple relationships with facets](https://seaborn.pydata.org/tutorial/relational.html#showing-multiple-relationships-with-facets)

[![Image 9: _images/distributions.svg](https://seaborn.pydata.org/_images/distributions.svg)](https://seaborn.pydata.org/tutorial/distributions.html)

*   [Visualizing distributions of data](https://seaborn.pydata.org/tutorial/distributions.html)
    *   [Plotting univariate histograms](https://seaborn.pydata.org/tutorial/distributions.html#plotting-univariate-histograms)
    *   [Kernel density estimation](https://seaborn.pydata.org/tutorial/distributions.html#kernel-density-estimation)
    *   [Empirical cumulative distributions](https://seaborn.pydata.org/tutorial/distributions.html#empirical-cumulative-distributions)
    *   [Visualizing bivariate distributions](https://seaborn.pydata.org/tutorial/distributions.html#visualizing-bivariate-distributions)
    *   [Distribution visualization in other settings](https://seaborn.pydata.org/tutorial/distributions.html#distribution-visualization-in-other-settings)

[![Image 10: _images/categorical.svg](https://seaborn.pydata.org/_images/categorical.svg)](https://seaborn.pydata.org/tutorial/categorical.html)

*   [Visualizing categorical data](https://seaborn.pydata.org/tutorial/categorical.html)
    *   [Categorical scatterplots](https://seaborn.pydata.org/tutorial/categorical.html#categorical-scatterplots)
    *   [Comparing distributions](https://seaborn.pydata.org/tutorial/categorical.html#comparing-distributions)
    *   [Estimating central tendency](https://seaborn.pydata.org/tutorial/categorical.html#estimating-central-tendency)
    *   [Showing additional dimensions](https://seaborn.pydata.org/tutorial/categorical.html#showing-additional-dimensions)

Statistical operations[#](https://seaborn.pydata.org/tutorial.html#statistical-operations "Permalink to this heading")
----------------------------------------------------------------------------------------------------------------------

[![Image 11: _images/error_bars.svg](https://seaborn.pydata.org/_images/error_bars.svg)](https://seaborn.pydata.org/tutorial/error_bars.html)

*   [Statistical estimation and error bars](https://seaborn.pydata.org/tutorial/error_bars.html)
    *   [Measures of data spread](https://seaborn.pydata.org/tutorial/error_bars.html#measures-of-data-spread)
    *   [Measures of estimate uncertainty](https://seaborn.pydata.org/tutorial/error_bars.html#measures-of-estimate-uncertainty)
    *   [Error bars on regression fits](https://seaborn.pydata.org/tutorial/error_bars.html#error-bars-on-regression-fits)
    *   [Are error bars enough?](https://seaborn.pydata.org/tutorial/error_bars.html#are-error-bars-enough)

[![Image 12: _images/regression.svg](https://seaborn.pydata.org/_images/regression.svg)](https://seaborn.pydata.org/tutorial/regression.html)

*   [Estimating regression fits](https://seaborn.pydata.org/tutorial/regression.html)
    *   [Functions for drawing linear regression models](https://seaborn.pydata.org/tutorial/regression.html#functions-for-drawing-linear-regression-models)
    *   [Fitting different kinds of models](https://seaborn.pydata.org/tutorial/regression.html#fitting-different-kinds-of-models)
    *   [Conditioning on other variables](https://seaborn.pydata.org/tutorial/regression.html#conditioning-on-other-variables)
    *   [Plotting a regression in other contexts](https://seaborn.pydata.org/tutorial/regression.html#plotting-a-regression-in-other-contexts)

Multi-plot grids[#](https://seaborn.pydata.org/tutorial.html#multi-plot-grids "Permalink to this heading")
----------------------------------------------------------------------------------------------------------

[![Image 13: _images/axis_grids.svg](https://seaborn.pydata.org/_images/axis_grids.svg)](https://seaborn.pydata.org/tutorial/axis_grids.html)

*   [Building structured multi-plot grids](https://seaborn.pydata.org/tutorial/axis_grids.html)
    *   [Conditional small multiples](https://seaborn.pydata.org/tutorial/axis_grids.html#conditional-small-multiples)
    *   [Using custom functions](https://seaborn.pydata.org/tutorial/axis_grids.html#using-custom-functions)
    *   [Plotting pairwise data relationships](https://seaborn.pydata.org/tutorial/axis_grids.html#plotting-pairwise-data-relationships)

Figure aesthetics[#](https://seaborn.pydata.org/tutorial.html#figure-aesthetics "Permalink to this heading")
------------------------------------------------------------------------------------------------------------

[![Image 14: _images/aesthetics.svg](https://seaborn.pydata.org/_images/aesthetics.svg)](https://seaborn.pydata.org/tutorial/aesthetics.html)

*   [Controlling figure aesthetics](https://seaborn.pydata.org/tutorial/aesthetics.html)
    *   [Seaborn figure styles](https://seaborn.pydata.org/tutorial/aesthetics.html#seaborn-figure-styles)
    *   [Removing axes spines](https://seaborn.pydata.org/tutorial/aesthetics.html#removing-axes-spines)
    *   [Temporarily setting figure style](https://seaborn.pydata.org/tutorial/aesthetics.html#temporarily-setting-figure-style)
    *   [Overriding elements of the seaborn styles](https://seaborn.pydata.org/tutorial/aesthetics.html#overriding-elements-of-the-seaborn-styles)
    *   [Scaling plot elements](https://seaborn.pydata.org/tutorial/aesthetics.html#scaling-plot-elements)

[![Image 15: _images/color_palettes.svg](https://seaborn.pydata.org/_images/color_palettes.svg)](https://seaborn.pydata.org/tutorial/color_palettes.html)

*   [Choosing color palettes](https://seaborn.pydata.org/tutorial/color_palettes.html)
    *   [General principles for using color in plots](https://seaborn.pydata.org/tutorial/color_palettes.html#general-principles-for-using-color-in-plots)
    *   [Tools for choosing color palettes](https://seaborn.pydata.org/tutorial/color_palettes.html#tools-for-choosing-color-palettes)
    *   [Qualitative color palettes](https://seaborn.pydata.org/tutorial/color_palettes.html#qualitative-color-palettes)
    *   [Sequential color palettes](https://seaborn.pydata.org/tutorial/color_palettes.html#sequential-color-palettes)
    *   [Diverging color palettes](https://seaborn.pydata.org/tutorial/color_palettes.html#diverging-color-palettes)

© Copyright 2012-2024, [Michael Waskom](https://mwaskom.github.io/).

 Created using [Sphinx](https://www.sphinx-doc.org/) and the [PyData Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/).

[Archive](https://seaborn.pydata.org/tutorial.html#)

[v0.12](https://seaborn.pydata.org/archive/0.12/index.html)[v0.11](https://seaborn.pydata.org/archive/0.11/index.html)[v0.10](https://seaborn.pydata.org/archive/0.10/index.html)[v0.9](https://seaborn.pydata.org/archive/0.9/index.html)

v0.13.2

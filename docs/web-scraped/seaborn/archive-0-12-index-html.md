# Source: https://seaborn.pydata.org/archive/0.12/index.html

Title: statistical data visualization — seaborn 0.12.2 documentation

URL Source: https://seaborn.pydata.org/archive/0.12/index.html

Markdown Content:
seaborn: statistical data visualization — seaborn 0.12.2 documentation
===============
- [x] - [x] 

Ctrl+K

[![Image 1: Logo image](https://seaborn.pydata.org/archive/0.12/_static/logo-wide-lightbg.svg)![Image 2: Logo image](https://seaborn.pydata.org/archive/0.12/_static/logo-wide-lightbg.svg)](https://seaborn.pydata.org/archive/0.12/index.html#)

*   [Installing](https://seaborn.pydata.org/archive/0.12/installing.html)
*   [Gallery](https://seaborn.pydata.org/archive/0.12/examples/index.html)
*   [Tutorial](https://seaborn.pydata.org/archive/0.12/tutorial.html)
*   [API](https://seaborn.pydata.org/archive/0.12/api.html)
*   [Releases](https://seaborn.pydata.org/archive/0.12/whatsnew/index.html)
*   [Citing](https://seaborn.pydata.org/archive/0.12/citing.html)
*   [FAQ](https://seaborn.pydata.org/archive/0.12/faq.html)

*   [GitHub](https://github.com/mwaskom/seaborn "GitHub")
*   [StackOverflow](https://stackoverflow.com/tags/seaborn "StackOverflow")
*   [Twitter](https://twitter.com/michaelwaskom "Twitter")

Site Navigation

*   [Installing](https://seaborn.pydata.org/archive/0.12/installing.html)
*   [Gallery](https://seaborn.pydata.org/archive/0.12/examples/index.html)
*   [Tutorial](https://seaborn.pydata.org/archive/0.12/tutorial.html)
*   [API](https://seaborn.pydata.org/archive/0.12/api.html)
*   [Releases](https://seaborn.pydata.org/archive/0.12/whatsnew/index.html)
*   [Citing](https://seaborn.pydata.org/archive/0.12/citing.html)
*   [FAQ](https://seaborn.pydata.org/archive/0.12/faq.html)

*   [GitHub](https://github.com/mwaskom/seaborn "GitHub")
*   [StackOverflow](https://stackoverflow.com/tags/seaborn "StackOverflow")
*   [Twitter](https://twitter.com/michaelwaskom "Twitter")

[This is documentation for an old version. Click here to load docs for the latest release.](https://seaborn.pydata.org/)

seaborn: statistical data visualization[#](https://seaborn.pydata.org/archive/0.12/index.html#seaborn-statistical-data-visualization "Permalink to this heading")
=================================================================================================================================================================

[![Image 3: _images/scatterplot_matrix_thumb.png](https://seaborn.pydata.org/archive/0.12/_images/scatterplot_matrix_thumb.png)](https://seaborn.pydata.org/archive/0.12/examples/scatterplot_matrix.html)

[![Image 4: _images/errorband_lineplots_thumb.png](https://seaborn.pydata.org/archive/0.12/_images/errorband_lineplots_thumb.png)](https://seaborn.pydata.org/archive/0.12/examples/errorband_lineplots.html)

[![Image 5: _images/scatterplot_sizes_thumb.png](https://seaborn.pydata.org/archive/0.12/_images/scatterplot_sizes_thumb.png)](https://seaborn.pydata.org/archive/0.12/examples/scatterplot_sizes.html)

[![Image 6: _images/timeseries_facets_thumb.png](https://seaborn.pydata.org/archive/0.12/_images/timeseries_facets_thumb.png)](https://seaborn.pydata.org/archive/0.12/examples/timeseries_facets.html)

[![Image 7: _images/horizontal_boxplot_thumb.png](https://seaborn.pydata.org/archive/0.12/_images/horizontal_boxplot_thumb.png)](https://seaborn.pydata.org/archive/0.12/examples/horizontal_boxplot.html)

[![Image 8: _images/regression_marginals_thumb.png](https://seaborn.pydata.org/archive/0.12/_images/regression_marginals_thumb.png)](https://seaborn.pydata.org/archive/0.12/examples/regression_marginals.html)

Seaborn is a Python data visualization library based on [matplotlib](https://matplotlib.org/). It provides a high-level interface for drawing attractive and informative statistical graphics.

For a brief introduction to the ideas behind the library, you can read the [introductory notes](https://seaborn.pydata.org/archive/0.12/tutorial/introduction.html) or the [paper](https://joss.theoj.org/papers/10.21105/joss.03021). Visit the [installation page](https://seaborn.pydata.org/archive/0.12/installing.html) to see how you can download the package and get started with it. You can browse the [example gallery](https://seaborn.pydata.org/archive/0.12/examples/index.html) to see some of the things that you can do with seaborn, and then check out the [tutorials](https://seaborn.pydata.org/archive/0.12/tutorial.html) or [API reference](https://seaborn.pydata.org/archive/0.12/api.html) to find out how.

To see the code or report a bug, please visit the [GitHub repository](https://github.com/mwaskom/seaborn). General support questions are most at home on [stackoverflow](https://stackoverflow.com/questions/tagged/seaborn/), which has a dedicated channel for seaborn.

 Contents

*   [Installing](https://seaborn.pydata.org/archive/0.12/installing.html)
*   [Gallery](https://seaborn.pydata.org/archive/0.12/examples/index.html)
*   [Tutorial](https://seaborn.pydata.org/archive/0.12/tutorial.html)
*   [API](https://seaborn.pydata.org/archive/0.12/api.html)
*   [Releases](https://seaborn.pydata.org/archive/0.12/whatsnew/index.html)
*   [Citing](https://seaborn.pydata.org/archive/0.12/citing.html)
*   [FAQ](https://seaborn.pydata.org/archive/0.12/faq.html)

 Features

*   New Objects: [API](https://seaborn.pydata.org/archive/0.12/api.html#objects-api) | [Tutorial](https://seaborn.pydata.org/archive/0.12/tutorial/objects_interface.html)

*   Relational plots: [API](https://seaborn.pydata.org/archive/0.12/api.html#relational-api) | [Tutorial](https://seaborn.pydata.org/archive/0.12/tutorial/relational.html)

*   Distribution plots: [API](https://seaborn.pydata.org/archive/0.12/api.html#distribution-api) | [Tutorial](https://seaborn.pydata.org/archive/0.12/tutorial/distributions.html)

*   Categorical plots: [API](https://seaborn.pydata.org/archive/0.12/api.html#categorical-api) | [Tutorial](https://seaborn.pydata.org/archive/0.12/tutorial/categorical.html)

*   Regression plots: [API](https://seaborn.pydata.org/archive/0.12/api.html#regression-api) | [Tutorial](https://seaborn.pydata.org/archive/0.12/tutorial/regression.html)

*   Multi-plot grids: [API](https://seaborn.pydata.org/archive/0.12/api.html#grid-api) | [Tutorial](https://seaborn.pydata.org/archive/0.12/tutorial/axis_grids.html)

*   Figure theming: [API](https://seaborn.pydata.org/archive/0.12/api.html#style-api) | [Tutorial](https://seaborn.pydata.org/archive/0.12/tutorial/aesthetics.html)

*   Color palettes: [API](https://seaborn.pydata.org/archive/0.12/api.html#palette-api) | [Tutorial](https://seaborn.pydata.org/archive/0.12/tutorial/color_palettes.html)

© Copyright 2012-2022, [Michael Waskom](https://mwaskom.github.io/).

 Created using [Sphinx](https://www.sphinx-doc.org/) and the [PyData Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/).

[Archive](https://seaborn.pydata.org/archive/0.12/index.html#)

[v0.11](https://seaborn.pydata.org/archive/0.11/index.html)[v0.10](https://seaborn.pydata.org/archive/0.10/index.html)[v0.9](https://seaborn.pydata.org/archive/0.9/index.html)

v0.12.2

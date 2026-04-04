# Source: https://seaborn.pydata.org

Title: statistical data visualization — seaborn 0.13.2 documentation

URL Source: https://seaborn.pydata.org/

Published Time: Thu, 25 Jan 2024 13:24:12 GMT

Markdown Content:
seaborn: statistical data visualization — seaborn 0.13.2 documentation
===============
- [x] - [x] 

Ctrl+K

[![Image 1: Logo image](https://seaborn.pydata.org/_static/logo-wide-lightbg.svg)![Image 2: Logo image](https://seaborn.pydata.org/_static/logo-wide-lightbg.svg)](https://seaborn.pydata.org/#)

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

seaborn: statistical data visualization[#](https://seaborn.pydata.org/#seaborn-statistical-data-visualization "Permalink to this heading")
==========================================================================================================================================

[![Image 3: _images/scatterplot_matrix_thumb.png](https://seaborn.pydata.org/_images/scatterplot_matrix_thumb.png)](https://seaborn.pydata.org/examples/scatterplot_matrix.html)

[![Image 4: _images/errorband_lineplots_thumb.png](https://seaborn.pydata.org/_images/errorband_lineplots_thumb.png)](https://seaborn.pydata.org/examples/errorband_lineplots.html)

[![Image 5: _images/scatterplot_sizes_thumb.png](https://seaborn.pydata.org/_images/scatterplot_sizes_thumb.png)](https://seaborn.pydata.org/examples/scatterplot_sizes.html)

[![Image 6: _images/timeseries_facets_thumb.png](https://seaborn.pydata.org/_images/timeseries_facets_thumb.png)](https://seaborn.pydata.org/examples/timeseries_facets.html)

[![Image 7: _images/horizontal_boxplot_thumb.png](https://seaborn.pydata.org/_images/horizontal_boxplot_thumb.png)](https://seaborn.pydata.org/examples/horizontal_boxplot.html)

[![Image 8: _images/regression_marginals_thumb.png](https://seaborn.pydata.org/_images/regression_marginals_thumb.png)](https://seaborn.pydata.org/examples/regression_marginals.html)

Seaborn is a Python data visualization library based on [matplotlib](https://matplotlib.org/). It provides a high-level interface for drawing attractive and informative statistical graphics.

For a brief introduction to the ideas behind the library, you can read the [introductory notes](https://seaborn.pydata.org/tutorial/introduction.html) or the [paper](https://joss.theoj.org/papers/10.21105/joss.03021). Visit the [installation page](https://seaborn.pydata.org/installing.html) to see how you can download the package and get started with it. You can browse the [example gallery](https://seaborn.pydata.org/examples/index.html) to see some of the things that you can do with seaborn, and then check out the [tutorials](https://seaborn.pydata.org/tutorial.html) or [API reference](https://seaborn.pydata.org/api.html) to find out how.

To see the code or report a bug, please visit the [GitHub repository](https://github.com/mwaskom/seaborn). General support questions are most at home on [stackoverflow](https://stackoverflow.com/questions/tagged/seaborn/), which has a dedicated channel for seaborn.

 Contents

*   [Installing](https://seaborn.pydata.org/installing.html)
*   [Gallery](https://seaborn.pydata.org/examples/index.html)
*   [Tutorial](https://seaborn.pydata.org/tutorial.html)
*   [API](https://seaborn.pydata.org/api.html)
*   [Releases](https://seaborn.pydata.org/whatsnew/index.html)
*   [Citing](https://seaborn.pydata.org/citing.html)
*   [FAQ](https://seaborn.pydata.org/faq.html)

 Features

*   New Objects: [API](https://seaborn.pydata.org/api.html#objects-api) | [Tutorial](https://seaborn.pydata.org/tutorial/objects_interface.html)

*   Relational plots: [API](https://seaborn.pydata.org/api.html#relational-api) | [Tutorial](https://seaborn.pydata.org/tutorial/relational.html)

*   Distribution plots: [API](https://seaborn.pydata.org/api.html#distribution-api) | [Tutorial](https://seaborn.pydata.org/tutorial/distributions.html)

*   Categorical plots: [API](https://seaborn.pydata.org/api.html#categorical-api) | [Tutorial](https://seaborn.pydata.org/tutorial/categorical.html)

*   Regression plots: [API](https://seaborn.pydata.org/api.html#regression-api) | [Tutorial](https://seaborn.pydata.org/tutorial/regression.html)

*   Multi-plot grids: [API](https://seaborn.pydata.org/api.html#grid-api) | [Tutorial](https://seaborn.pydata.org/tutorial/axis_grids.html)

*   Figure theming: [API](https://seaborn.pydata.org/api.html#style-api) | [Tutorial](https://seaborn.pydata.org/tutorial/aesthetics.html)

*   Color palettes: [API](https://seaborn.pydata.org/api.html#palette-api) | [Tutorial](https://seaborn.pydata.org/tutorial/color_palettes.html)

© Copyright 2012-2024, [Michael Waskom](https://mwaskom.github.io/).

 Created using [Sphinx](https://www.sphinx-doc.org/) and the [PyData Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/).

[Archive](https://seaborn.pydata.org/#)

[v0.12](https://seaborn.pydata.org/archive/0.12/index.html)[v0.11](https://seaborn.pydata.org/archive/0.11/index.html)[v0.10](https://seaborn.pydata.org/archive/0.10/index.html)[v0.9](https://seaborn.pydata.org/archive/0.9/index.html)

v0.13.2

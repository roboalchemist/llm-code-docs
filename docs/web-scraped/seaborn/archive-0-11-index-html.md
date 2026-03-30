# Source: https://seaborn.pydata.org/archive/0.11/index.html

Title: statistical data visualization — seaborn 0.11.2 documentation

URL Source: https://seaborn.pydata.org/archive/0.11/index.html

Markdown Content:
seaborn: statistical data visualization — seaborn 0.11.2 documentation
===============

[![Image 1](https://seaborn.pydata.org/archive/0.11/_static/logo-wide-lightbg.svg)](https://seaborn.pydata.org/archive/0.11/index.html#)**0.11.2**

*   [Gallery](https://seaborn.pydata.org/archive/0.11/examples/index.html)
*   [Tutorial](https://seaborn.pydata.org/archive/0.11/tutorial.html)
*   [API](https://seaborn.pydata.org/archive/0.11/api.html)
*   [Site](https://seaborn.pydata.org/archive/0.11/index.html#)

    
        *   [Introduction](https://seaborn.pydata.org/archive/0.11/introduction.html)
        *   [Release notes](https://seaborn.pydata.org/archive/0.11/whatsnew.html)
        *   [Installing](https://seaborn.pydata.org/archive/0.11/installing.html)
        *   [Example gallery](https://seaborn.pydata.org/archive/0.11/examples/index.html)
        *   [Tutorial](https://seaborn.pydata.org/archive/0.11/tutorial.html)
        *   [API reference](https://seaborn.pydata.org/archive/0.11/api.html)

    
        *   [Citing](https://seaborn.pydata.org/archive/0.11/citing.html)
        *   [Archive](https://seaborn.pydata.org/archive/0.11/archive.html)

*   [Page](https://seaborn.pydata.org/archive/0.11/index.html#)

    
        *   [seaborn: statistical data visualization](https://seaborn.pydata.org/archive/0.11/index.html#)

[This is documentation for an old version. Click here to load docs for the latest release.](https://seaborn.pydata.org/)

seaborn: statistical data visualization[¶](https://seaborn.pydata.org/archive/0.11/index.html#seaborn-statistical-data-visualization "Permalink to this headline")
==================================================================================================================================================================

[![Image 2](https://seaborn.pydata.org/archive/0.11/_static/scatterplot_matrix_thumb.png)](https://seaborn.pydata.org/archive/0.11/examples/scatterplot_matrix.html)[![Image 3](https://seaborn.pydata.org/archive/0.11/_static/errorband_lineplots_thumb.png)](https://seaborn.pydata.org/archive/0.11/examples/errorband_lineplots.html)[![Image 4](https://seaborn.pydata.org/archive/0.11/_static/scatterplot_sizes_thumb.png)](https://seaborn.pydata.org/archive/0.11/examples/scatterplot_sizes.html)[![Image 5](https://seaborn.pydata.org/archive/0.11/_static/timeseries_facets_thumb.png)](https://seaborn.pydata.org/archive/0.11/examples/timeseries_facets.html)[![Image 6](https://seaborn.pydata.org/archive/0.11/_static/horizontal_boxplot_thumb.png)](https://seaborn.pydata.org/archive/0.11/examples/horizontal_boxplot.html)[![Image 7](https://seaborn.pydata.org/archive/0.11/_static/regression_marginals_thumb.png)](https://seaborn.pydata.org/archive/0.11/examples/regression_marginals.html)

Seaborn is a Python data visualization library based on [matplotlib](https://matplotlib.org/). It provides a high-level interface for drawing attractive and informative statistical graphics.

For a brief introduction to the ideas behind the library, you can read the [introductory notes](https://seaborn.pydata.org/archive/0.11/introduction.html) or the [paper](https://joss.theoj.org/papers/10.21105/joss.03021). Visit the [installation page](https://seaborn.pydata.org/archive/0.11/installing.html) to see how you can download the package and get started with it. You can browse the [example gallery](https://seaborn.pydata.org/archive/0.11/examples/index.html) to see some of the things that you can do with seaborn, and then check out the [tutorial](https://seaborn.pydata.org/archive/0.11/tutorial.html) or [API reference](https://seaborn.pydata.org/archive/0.11/api.html) to find out how.

To see the code or report a bug, please visit the [GitHub repository](https://github.com/mwaskom/seaborn). General support questions are most at home on [stackoverflow](https://stackoverflow.com/questions/tagged/seaborn/) or [discourse](https://discourse.matplotlib.org/c/3rdparty/seaborn/21), which have dedicated channels for seaborn.

### Contents

*   [Introduction](https://seaborn.pydata.org/archive/0.11/introduction.html)
*   [Release notes](https://seaborn.pydata.org/archive/0.11/whatsnew.html)
*   [Installing](https://seaborn.pydata.org/archive/0.11/installing.html)
*   [Example gallery](https://seaborn.pydata.org/archive/0.11/examples/index.html)
*   [Tutorial](https://seaborn.pydata.org/archive/0.11/tutorial.html)
*   [API reference](https://seaborn.pydata.org/archive/0.11/api.html)

### Features

*   Relational: [API](https://seaborn.pydata.org/archive/0.11/api.html#relational-api) | [Tutorial](https://seaborn.pydata.org/archive/0.11/tutorial/relational.html)

*   Distribution: [API](https://seaborn.pydata.org/archive/0.11/api.html#distribution-api) | [Tutorial](https://seaborn.pydata.org/archive/0.11/tutorial/distributions.html)

*   Categorical: [API](https://seaborn.pydata.org/archive/0.11/api.html#categorical-api) | [Tutorial](https://seaborn.pydata.org/archive/0.11/tutorial/categorical.html)

*   Regression: [API](https://seaborn.pydata.org/archive/0.11/api.html#regression-api) | [Tutorial](https://seaborn.pydata.org/archive/0.11/tutorial/regression.html)

*   Multiples: [API](https://seaborn.pydata.org/archive/0.11/api.html#grid-api) | [Tutorial](https://seaborn.pydata.org/archive/0.11/tutorial/axis_grids.html)

*   Style: [API](https://seaborn.pydata.org/archive/0.11/api.html#style-api) | [Tutorial](https://seaborn.pydata.org/archive/0.11/tutorial/aesthetics.html)

*   Color: [API](https://seaborn.pydata.org/archive/0.11/api.html#palette-api) | [Tutorial](https://seaborn.pydata.org/archive/0.11/tutorial/color_palettes.html)

[Back to top](https://seaborn.pydata.org/archive/0.11/index.html#)

© Copyright 2012-2021, [Michael Waskom](https://mwaskom.github.io/). Created using [Sphinx](https://www.sphinx-doc.org/) 3.3.1.

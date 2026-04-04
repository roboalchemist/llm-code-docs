# Source: https://graph-tool.skewed.de/doc/

Title: Welcome to graph-tool’s documentation!

URL Source: https://graph-tool.skewed.de/doc/

Published Time: Thu, 21 Aug 2025 17:15:55 GMT

Markdown Content:
Contents
--------

*   [Installing graph-tool](https://graph-tool.skewed.de/doc/#installing-graph-tool)
*   [Getting started](https://graph-tool.skewed.de/doc/#getting-started)
*   [Asking questions and reporting bugs](https://graph-tool.skewed.de/doc/#asking-questions-and-reporting-bugs)
*   [How to use the documentation](https://graph-tool.skewed.de/doc/#how-to-use-the-documentation)
*   [Contents](https://graph-tool.skewed.de/doc/#contents)
*   [References](https://graph-tool.skewed.de/doc/#references)

Welcome to graph-tool’s documentation![#](https://graph-tool.skewed.de/doc/#welcome-to-graph-tools-documentation "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------

`graph-tool` is an efficient Python module for manipulation and statistical analysis of [graphs](https://en.wikipedia.org/wiki/Graph#Mathematics) (a.k.a. [networks](https://en.wikipedia.org/wiki/Network_theory)).

The [`graph_tool`](https://graph-tool.skewed.de/static/docs/stable/graph_tool.html#module-graph_tool "graph_tool") module provides a [`Graph`](https://graph-tool.skewed.de/static/docs/stable/autosummary/graph_tool.Graph.html#graph_tool.Graph "graph_tool.Graph") class and several algorithms that operate on it. The internals of this class, and of most algorithms, are written in C++ for performance, using [template metaprogramming](https://en.wikipedia.org/wiki/Template_metaprogramming) for code specialization, and the [Boost Graph Library](http://www.boost.org/).

`graph-tool` can be [orders of magnitude faster](https://graph-tool.skewed.de/performance.html) than Python-only alternatives, and therefore it is specially suited for large-scale network analysis.

Besides superior performance, `graph-tool` contains the following set of functionalities which are currently not available in most other comparable packages:

1.   Comprehensive framework for [inferential community detection](https://graph-tool.skewed.de/static/docs/stable/demos/inference/inference.html#inference-howto), build upon statistically principled approaches that avoid overfitting and are interpretable. (See [here](https://skewed.de/tiago/blog/modularity-harmful) and [[1](https://graph-tool.skewed.de/doc/#id13 "Tiago P. Peixoto. Descriptive vs. Inferential Community Detection in Networks: Pitfalls, Myths and Half-Truths. Elements in the Structure and Dynamics of Complex Networks, July 2023. arXiv:2112.00183, doi:10.1017/9781009118897, [sci-hub].")] for why you should avoid off-the-shelf methods available in other software packages.)

2.   Support for [OpenMP](https://en.wikipedia.org/wiki/OpenMP) shared memory parallelism for several algorithms. See the [parallel algorithms](https://graph-tool.skewed.de/static/docs/stable/parallel.html#parallel-algorithms) section fore more information.

3.   High-quality [network visualization](https://graph-tool.skewed.de/static/docs/stable/draw.html#draw), both static and interactive, supporting [animations](https://graph-tool.skewed.de/static/docs/stable/demos/animation/animation.html#animation) and [matplotlib integration](https://graph-tool.skewed.de/static/docs/stable/demos/matplotlib/matplotlib.html#matplotlib-sec).

4.   [Filtered graphs](https://graph-tool.skewed.de/static/docs/stable/quickstart.html#sec-graph-filtering), i.e. graphs where nodes and edges are temporarily masked. These are first class citizens in the library, and are accepted by every function. Due to the use of C++ template metaprogramming, this functionality comes at no performance cost when filtering is not being used.

5.   Efficient and fully documented [binary format](https://graph-tool.skewed.de/static/docs/stable/gt_format.html#sec-gt-format) for network files.

6.   Integration with the [Netzschleuder](https://networks.skewed.de/) network data repository, enabling [`easy loading`](https://graph-tool.skewed.de/static/docs/stable/collection.html#graph_tool.collection.ns "graph_tool.collection.ns") of network data.

7.   Support for writing custom [C++ extensions](https://graph-tool.skewed.de/static/docs/stable/demos/cppextensions/cppextensions.html#cppextensions).

Installing graph-tool[#](https://graph-tool.skewed.de/doc/#installing-graph-tool "Link to this heading")
--------------------------------------------------------------------------------------------------------

Detailed installation instructions for various platforms are available [here](https://graph-tool.skewed.de/installation.html).

The easiest option is to use [conda](https://docs.conda.io/):

conda create --name gt -c conda-forge graph-tool
conda activate gt

For HPC systems it is also straightforward to use [`graph_tool`](https://graph-tool.skewed.de/static/docs/stable/graph_tool.html#module-graph_tool "graph_tool") with [Apptainer/Singularity](https://graph-tool.skewed.de/installation.html#installing-using-apptainer-n%C3%A9e-singularity).

Getting started[#](https://graph-tool.skewed.de/doc/#getting-started "Link to this heading")
--------------------------------------------------------------------------------------------

Yous should read first the [quick start guide](https://graph-tool.skewed.de/static/docs/stable/quickstart.html#quickstart), followed by the various [cookbooks](https://graph-tool.skewed.de/static/docs/stable/demos/index.html#demos) and explore all the examples in various [submodules](https://graph-tool.skewed.de/static/docs/stable/modules.html#submodules). For commonly asked questions, read the [FAQ](https://graph-tool.skewed.de/static/docs/stable/faq.html#sec-faq).

Asking questions and reporting bugs[#](https://graph-tool.skewed.de/doc/#asking-questions-and-reporting-bugs "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------

If you have questions about using `graph-tool`, you are welcome to visit the [discussion forum](https://forum.skewed.de/c/graph-tool/5).

If you encounter a problem, open an issue in the [git repository](https://git.skewed.de/count0/graph-tool/-/issues).

Please don’t forget to check if your question has been asked before, or if a similar issue is open. When asking questions or reporting problems, it is important to include:

1.   Your exact `graph-tool` version.

2.   Your operating system.

3.   A **minimal working example** that shows the problem.

Item **3** above is **very important**! If you provide us only the part of the code that you believe causes the problem, then it is not possible to understand the context that may have contributed to it.

How to use the documentation[#](https://graph-tool.skewed.de/doc/#how-to-use-the-documentation "Link to this heading")
----------------------------------------------------------------------------------------------------------------------

Documentation is available in two forms: docstrings provided with the code, and the full documentation available in [the graph-tool homepage](http://graph-tool.skewed.de/doc).

We recommend exploring the docstrings using [IPython](http://ipython.scipy.org/), an advanced Python shell with TAB-completion and introspection capabilities.

The docstring examples assume that `graph_tool.all` has been imported as `gt`:

>>> import graph_tool.all as gt

Code snippets are indicated by three greater-than signs:

>>> x = x + 1

Use the built-in `help` function to view a function’s docstring:

>>> help(gt.Graph)

Contents[#](https://graph-tool.skewed.de/doc/#contents "Link to this heading")
------------------------------------------------------------------------------

*   [Quick start guide](https://graph-tool.skewed.de/static/docs/stable/quickstart.html)
    *   [Creating graphs](https://graph-tool.skewed.de/static/docs/stable/quickstart.html#creating-graphs)
        *   [Adding many edges and vertices at once](https://graph-tool.skewed.de/static/docs/stable/quickstart.html#adding-many-edges-and-vertices-at-once)

    *   [Manipulating graphs](https://graph-tool.skewed.de/static/docs/stable/quickstart.html#manipulating-graphs)
        *   [Iterating over vertices and edges](https://graph-tool.skewed.de/static/docs/stable/quickstart.html#iterating-over-vertices-and-edges)

    *   [Example analysis: an online social network](https://graph-tool.skewed.de/static/docs/stable/quickstart.html#example-analysis-an-online-social-network)
    *   [Property maps](https://graph-tool.skewed.de/static/docs/stable/quickstart.html#property-maps)
        *   [Transformations](https://graph-tool.skewed.de/static/docs/stable/quickstart.html#transformations)
        *   [Internal property maps](https://graph-tool.skewed.de/static/docs/stable/quickstart.html#internal-property-maps)

    *   [Graph I/O](https://graph-tool.skewed.de/static/docs/stable/quickstart.html#graph-i-o)
    *   [Graph filtering](https://graph-tool.skewed.de/static/docs/stable/quickstart.html#graph-filtering)
        *   [Graph views](https://graph-tool.skewed.de/static/docs/stable/quickstart.html#graph-views)
        *   [In-place graph filtering](https://graph-tool.skewed.de/static/docs/stable/quickstart.html#in-place-graph-filtering)

    *   [Advanced iteration](https://graph-tool.skewed.de/static/docs/stable/quickstart.html#advanced-iteration)
        *   [Faster iteration over vertices and edges without descriptors](https://graph-tool.skewed.de/static/docs/stable/quickstart.html#faster-iteration-over-vertices-and-edges-without-descriptors)
        *   [Even faster, “loopless” iteration over vertices and edges using arrays](https://graph-tool.skewed.de/static/docs/stable/quickstart.html#even-faster-loopless-iteration-over-vertices-and-edges-using-arrays)

*   [Parallel algorithms](https://graph-tool.skewed.de/static/docs/stable/parallel.html)
    *   [The global interpreter lock (GIL)](https://graph-tool.skewed.de/static/docs/stable/parallel.html#the-global-interpreter-lock-gil)

*   [Cookbook guides](https://graph-tool.skewed.de/static/docs/stable/demos/index.html)
    *   [Inferring modular network structure](https://graph-tool.skewed.de/static/docs/stable/demos/inference/inference.html)
    *   [Background: Nonparametric statistical inference](https://graph-tool.skewed.de/static/docs/stable/demos/inference/inference.html#background-nonparametric-statistical-inference)
        *   [Minimum description length (MDL)](https://graph-tool.skewed.de/static/docs/stable/demos/inference/inference.html#minimum-description-length-mdl)

    *   [The stochastic block model (SBM)](https://graph-tool.skewed.de/static/docs/stable/demos/inference/inference.html#the-stochastic-block-model-sbm)
        *   [The nested stochastic block model](https://graph-tool.skewed.de/static/docs/stable/demos/inference/inference.html#the-nested-stochastic-block-model)

    *   [Inferring the best partition](https://graph-tool.skewed.de/static/docs/stable/demos/inference/inference.html#inferring-the-best-partition)
        *   [Hierarchical partitions](https://graph-tool.skewed.de/static/docs/stable/demos/inference/inference.html#hierarchical-partitions)
        *   [Refinements using merge-split MCMC](https://graph-tool.skewed.de/static/docs/stable/demos/inference/inference.html#refinements-using-merge-split-mcmc)

    *   [Model selection](https://graph-tool.skewed.de/static/docs/stable/demos/inference/inference.html#model-selection)
    *   [Sampling from the posterior distribution](https://graph-tool.skewed.de/static/docs/stable/demos/inference/inference.html#sampling-from-the-posterior-distribution)
        *   [Hierarchical partitions](https://graph-tool.skewed.de/static/docs/stable/demos/inference/inference.html#id18)
        *   [Characterizing the posterior distribution](https://graph-tool.skewed.de/static/docs/stable/demos/inference/inference.html#characterizing-the-posterior-distribution)

    *   [Model class selection](https://graph-tool.skewed.de/static/docs/stable/demos/inference/inference.html#model-class-selection)
    *   [Edge weights and covariates](https://graph-tool.skewed.de/static/docs/stable/demos/inference/inference.html#edge-weights-and-covariates)
        *   [Model selection](https://graph-tool.skewed.de/static/docs/stable/demos/inference/inference.html#id27)
        *   [Posterior sampling](https://graph-tool.skewed.de/static/docs/stable/demos/inference/inference.html#posterior-sampling)

    *   [Layered networks](https://graph-tool.skewed.de/static/docs/stable/demos/inference/inference.html#layered-networks)
    *   [Assortative community structure](https://graph-tool.skewed.de/static/docs/stable/demos/inference/inference.html#assortative-community-structure)
    *   [Ordered community structure](https://graph-tool.skewed.de/static/docs/stable/demos/inference/inference.html#ordered-community-structure)
    *   [References](https://graph-tool.skewed.de/static/docs/stable/demos/inference/inference.html#references)
    *   [Uncertain network reconstruction](https://graph-tool.skewed.de/static/docs/stable/demos/reconstruction_direct/reconstruction.html)
        *   [Measured networks](https://graph-tool.skewed.de/static/docs/stable/demos/reconstruction_direct/reconstruction.html#measured-networks)
        *   [Extraneous error estimates](https://graph-tool.skewed.de/static/docs/stable/demos/reconstruction_direct/reconstruction.html#extraneous-error-estimates)
        *   [Latent Poisson multigraphs](https://graph-tool.skewed.de/static/docs/stable/demos/reconstruction_direct/reconstruction.html#latent-poisson-multigraphs)
        *   [Latent triadic closures](https://graph-tool.skewed.de/static/docs/stable/demos/reconstruction_direct/reconstruction.html#latent-triadic-closures)

    *   [Edge prediction as binary classification](https://graph-tool.skewed.de/static/docs/stable/demos/reconstruction_direct/reconstruction.html#edge-prediction-as-binary-classification)
    *   [References](https://graph-tool.skewed.de/static/docs/stable/demos/reconstruction_direct/reconstruction.html#references)
    *   [Network reconstruction from dynamics and behavior](https://graph-tool.skewed.de/static/docs/stable/demos/reconstruction_indirect/reconstruction.html)
        *   [Reconstruction with synthetic data](https://graph-tool.skewed.de/static/docs/stable/demos/reconstruction_indirect/reconstruction.html#reconstruction-with-synthetic-data)
        *   [Reconstruction with empirical data](https://graph-tool.skewed.de/static/docs/stable/demos/reconstruction_indirect/reconstruction.html#reconstruction-with-empirical-data)
        *   [References](https://graph-tool.skewed.de/static/docs/stable/demos/reconstruction_indirect/reconstruction.html#references)

    *   [Animations with graph-tool](https://graph-tool.skewed.de/static/docs/stable/demos/animation/animation.html)
        *   [Simple interactive animations](https://graph-tool.skewed.de/static/docs/stable/demos/animation/animation.html#simple-interactive-animations)
        *   [SIRS epidemics](https://graph-tool.skewed.de/static/docs/stable/demos/animation/animation.html#sirs-epidemics)
        *   [Dynamic layout](https://graph-tool.skewed.de/static/docs/stable/demos/animation/animation.html#dynamic-layout)
        *   [Interactive visualizations](https://graph-tool.skewed.de/static/docs/stable/demos/animation/animation.html#interactive-visualizations)

    *   [Integration with matplotlib](https://graph-tool.skewed.de/static/docs/stable/demos/matplotlib/matplotlib.html)
        *   [Integration with `basemap`](https://graph-tool.skewed.de/static/docs/stable/demos/matplotlib/matplotlib.html#integration-with-basemap)

    *   [Writing extensions in C++](https://graph-tool.skewed.de/static/docs/stable/demos/cppextensions/cppextensions.html)
        *   [Range-based iteration over vertices and edges](https://graph-tool.skewed.de/static/docs/stable/demos/cppextensions/cppextensions.html#range-based-iteration-over-vertices-and-edges)
        *   [Extracting specific property maps](https://graph-tool.skewed.de/static/docs/stable/demos/cppextensions/cppextensions.html#extracting-specific-property-maps)
        *   [Checked and unchecked property maps](https://graph-tool.skewed.de/static/docs/stable/demos/cppextensions/cppextensions.html#checked-and-unchecked-property-maps)
        *   [References](https://graph-tool.skewed.de/static/docs/stable/demos/cppextensions/cppextensions.html#references)

*   [Submodules](https://graph-tool.skewed.de/static/docs/stable/modules.html)
    *   [`graph_tool`](https://graph-tool.skewed.de/static/docs/stable/graph_tool.html)
        *   [Fundamental classes](https://graph-tool.skewed.de/static/docs/stable/graph_tool.html#fundamental-classes)
        *   [Property Maps](https://graph-tool.skewed.de/static/docs/stable/graph_tool.html#property-maps)
        *   [Graph IO](https://graph-tool.skewed.de/static/docs/stable/graph_tool.html#graph-io)
        *   [OpenMP configuration](https://graph-tool.skewed.de/static/docs/stable/graph_tool.html#openmp-configuration)
        *   [System information](https://graph-tool.skewed.de/static/docs/stable/graph_tool.html#system-information)

    *   [`graph_tool.centrality`](https://graph-tool.skewed.de/static/docs/stable/centrality.html)
        *   [Summary](https://graph-tool.skewed.de/static/docs/stable/centrality.html#summary)

    *   [`graph_tool.clustering`](https://graph-tool.skewed.de/static/docs/stable/clustering.html)
        *   [Summary](https://graph-tool.skewed.de/static/docs/stable/clustering.html#summary)

    *   [`graph_tool.collection`](https://graph-tool.skewed.de/static/docs/stable/collection.html)
        *   [Interface to the Netzschleuder online network repository](https://graph-tool.skewed.de/static/docs/stable/collection.html#interface-to-the-netzschleuder-online-network-repository)
        *   [Built-in collection of empirical network data](https://graph-tool.skewed.de/static/docs/stable/collection.html#built-in-collection-of-empirical-network-data)
        *   [Functions returning small graphs](https://graph-tool.skewed.de/static/docs/stable/collection.html#functions-returning-small-graphs)
        *   [Small graph atlas](https://graph-tool.skewed.de/static/docs/stable/collection.html#small-graph-atlas)

    *   [`graph_tool.correlations`](https://graph-tool.skewed.de/static/docs/stable/correlations.html)
        *   [Summary](https://graph-tool.skewed.de/static/docs/stable/correlations.html#summary)

    *   [`graph_tool.dynamics`](https://graph-tool.skewed.de/static/docs/stable/dynamics.html)
        *   [Discrete-time dynamics](https://graph-tool.skewed.de/static/docs/stable/dynamics.html#discrete-time-dynamics)
        *   [Continuous-time dynamics](https://graph-tool.skewed.de/static/docs/stable/dynamics.html#continuous-time-dynamics)
        *   [Belief propagation](https://graph-tool.skewed.de/static/docs/stable/dynamics.html#belief-propagation)

    *   [`graph_tool.draw`](https://graph-tool.skewed.de/static/docs/stable/draw.html)
        *   [Layout algorithms](https://graph-tool.skewed.de/static/docs/stable/draw.html#layout-algorithms)
        *   [Graph drawing](https://graph-tool.skewed.de/static/docs/stable/draw.html#graph-drawing)

    *   [`graph_tool.flow`](https://graph-tool.skewed.de/static/docs/stable/flow.html)
        *   [Summary](https://graph-tool.skewed.de/static/docs/stable/flow.html#summary)
        *   [Example network](https://graph-tool.skewed.de/static/docs/stable/flow.html#example-network)

    *   [`graph_tool.generation`](https://graph-tool.skewed.de/static/docs/stable/generation.html)
        *   [Random graph generation](https://graph-tool.skewed.de/static/docs/stable/generation.html#random-graph-generation)
        *   [Stochastic block models](https://graph-tool.skewed.de/static/docs/stable/generation.html#stochastic-block-models)
        *   [Geometric models](https://graph-tool.skewed.de/static/docs/stable/generation.html#geometric-models)
        *   [Graph transformations](https://graph-tool.skewed.de/static/docs/stable/generation.html#graph-transformations)
        *   [Graph set operations](https://graph-tool.skewed.de/static/docs/stable/generation.html#graph-set-operations)
        *   [Deterministic graphs](https://graph-tool.skewed.de/static/docs/stable/generation.html#deterministic-graphs)

    *   [`graph_tool.inference`](https://graph-tool.skewed.de/static/docs/stable/inference.html)
        *   [Nonparametric stochastic block model inference](https://graph-tool.skewed.de/static/docs/stable/inference.html#nonparametric-stochastic-block-model-inference)
        *   [Nonparametric network reconstruction](https://graph-tool.skewed.de/static/docs/stable/inference.html#nonparametric-network-reconstruction)
        *   [Semiparametric stochastic block model inference](https://graph-tool.skewed.de/static/docs/stable/inference.html#semiparametric-stochastic-block-model-inference)
        *   [Large-scale descriptors](https://graph-tool.skewed.de/static/docs/stable/inference.html#large-scale-descriptors)

    *   [`graph_tool.search`](https://graph-tool.skewed.de/static/docs/stable/search_module.html)
        *   [Summary](https://graph-tool.skewed.de/static/docs/stable/search_module.html#summary)
        *   [Example network](https://graph-tool.skewed.de/static/docs/stable/search_module.html#example-network)

    *   [`graph_tool.spectral`](https://graph-tool.skewed.de/static/docs/stable/spectral.html)
        *   [Sparse matrices](https://graph-tool.skewed.de/static/docs/stable/spectral.html#sparse-matrices)
        *   [Operator objects](https://graph-tool.skewed.de/static/docs/stable/spectral.html#operator-objects)

    *   [`graph_tool.stats`](https://graph-tool.skewed.de/static/docs/stable/stats.html)
        *   [Summary](https://graph-tool.skewed.de/static/docs/stable/stats.html#summary)

    *   [`graph_tool.topology`](https://graph-tool.skewed.de/static/docs/stable/topology.html)
        *   [Distance and paths](https://graph-tool.skewed.de/static/docs/stable/topology.html#distance-and-paths)
        *   [Graph comparison](https://graph-tool.skewed.de/static/docs/stable/topology.html#graph-comparison)
        *   [Matching and independent sets](https://graph-tool.skewed.de/static/docs/stable/topology.html#matching-and-independent-sets)
        *   [Spanning tree](https://graph-tool.skewed.de/static/docs/stable/topology.html#spanning-tree)
        *   [Sorting and closure](https://graph-tool.skewed.de/static/docs/stable/topology.html#sorting-and-closure)
        *   [Components and connectivity](https://graph-tool.skewed.de/static/docs/stable/topology.html#components-and-connectivity)
        *   [Graph classification](https://graph-tool.skewed.de/static/docs/stable/topology.html#graph-classification)
        *   [Directionality](https://graph-tool.skewed.de/static/docs/stable/topology.html#directionality)
        *   [Combinatorial optimizaton](https://graph-tool.skewed.de/static/docs/stable/topology.html#combinatorial-optimizaton)

    *   [`graph_tool.util`](https://graph-tool.skewed.de/static/docs/stable/util.html)
        *   [Summary](https://graph-tool.skewed.de/static/docs/stable/util.html#summary)

*   [The `gt` file format](https://graph-tool.skewed.de/static/docs/stable/gt_format.html)
*   [FAQ](https://graph-tool.skewed.de/static/docs/stable/faq.html)
    *   [How do I retrieve a vertex by its property map value?](https://graph-tool.skewed.de/static/docs/stable/faq.html#how-do-i-retrieve-a-vertex-by-its-property-map-value)
    *   [Is it possible to perform modularity maximization with `graph-tool`?](https://graph-tool.skewed.de/static/docs/stable/faq.html#is-it-possible-to-perform-modularity-maximization-with-graph-tool)
    *   [How do I cite graph-tool?](https://graph-tool.skewed.de/static/docs/stable/faq.html#how-do-i-cite-graph-tool)

References[#](https://graph-tool.skewed.de/doc/#references "Link to this heading")
----------------------------------------------------------------------------------

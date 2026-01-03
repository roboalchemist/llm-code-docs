::: title
Matplotlib documentation
:::

::: module
matplotlib
:::

# Matplotlib documentation

Matplotlib is a comprehensive library for creating static, animated, and
interactive visualizations.

## Install

::: {.tab-set .sd-width-content-min}
::: tab-item
pip

``` bash
pip install matplotlib
```
:::

::: tab-item
conda

``` bash
conda install -c conda-forge matplotlib
```
:::

::: tab-item
pixi

``` bash
pixi add matplotlib
```
:::

::: tab-item
uv

``` bash
uv add matplotlib
```

::: warning
::: title
Warning
:::

uv usually installs its own versions of Python from the
python-build-standalone project, and only recent versions of those
Python builds (August 2025) work properly with the `tkagg` backend for
displaying plots in a window. Please make sure you are using uv 0.8.7 or
newer (update with e.g. `uv self update`) and that your bundled Python
installs are up to date (with `uv python upgrade --reinstall`).
Alternatively, you can use one of the other
`supported GUI frameworks <optional_dependencies>`{.interpreted-text
role="ref"}, e.g.

``` bash
uv add matplotlib pyside6
```
:::
:::

::: tab-item
other

`install-official`{.interpreted-text role="ref"}

`install-third-party`{.interpreted-text role="ref"}

`install-nightly-build`{.interpreted-text role="ref"}

`install-source`{.interpreted-text role="ref"}
:::
:::

::: {.toctree hidden=""}
install/index
:::

## Learn

::: grid
1 1 2 2

::: {.grid-item-card padding="2" columns="6"}
**How to use Matplotlib?** \^\^\^ .. toctree:: :maxdepth: 1

> users/explain/quick_start User guide \<users/index.rst\>
> tutorials/index.rst users/faq.rst
:::

::: {.grid-item-card padding="2" columns="6"}
**What can Matplotlib do?** \^\^\^ .. toctree:: :maxdepth: 1

> plot_types/index.rst gallery/index.rst
:::

::: {.grid-item-card padding="2" columns="12"}
**Reference** \^\^\^

::: {.grid class-row="sd-align-minor-center"}
1 1 2 2

::: grid-item
::: {.toctree maxdepth="1"}
API reference \<api/index\> Figure methods \<api/figure_api\> Plotting
methods \<api/axes_api\>
:::
:::

::: grid-item
Top-level interfaces to create:

-   figures: [.pyplot.figure]{.title-ref}
-   subplots: [.pyplot.subplots]{.title-ref},
    [.pyplot.subplot_mosaic]{.title-ref}
:::
:::
:::
:::

## Community

::: {.grid class-row="sd-align-minor-center"}
1 1 2 2

::: grid-item
::: rst-class
section-toc
:::

::: {.toctree maxdepth="2"}
users/resources/index.rst
:::
:::

::: grid-item
`link-external;1em;sd-text-info`{.interpreted-text role="octicon"}
[Third-party packages](https://matplotlib.org/mpl-third-party/),

provide custom, domain specific, and experimental features, including
styles, colors, more plot types and backends, and alternative
interfaces.
:::
:::

## What\'s new

::: grid
1 1 2 2

::: grid-item
Learn about new features and API changes.
:::

::: grid-item
::: {.toctree maxdepth="1"}
release/release_notes.rst
:::
:::
:::

## Contribute

::: {.grid class-row="sd-align-minor-center"}
1 1 2 2

::: grid-item
Matplotlib is a community project maintained for and by its users. See
`developers-guide-index`{.interpreted-text role="ref"} for the many ways
you can help!
:::

::: {.grid-item maxdepth="2"}
.. rst-class:: section-toc .. toctree:

devel/index.rst
:::
:::

## About us

::: {.grid class-row="sd-align-minor-center"}
1 1 2 2

::: grid-item
Matplotlib was created by neurobiologist John Hunter to work with EEG
data. It grew to be used and developed by many people in many different
fields. John\'s goal was that Matplotlib make easy things easy and hard
things possible.
:::

::: {.grid-item maxdepth="2"}
.. rst-class:: section-toc .. toctree:

project/index.rst
:::
:::

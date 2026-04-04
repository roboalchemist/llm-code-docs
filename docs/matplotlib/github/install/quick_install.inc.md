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

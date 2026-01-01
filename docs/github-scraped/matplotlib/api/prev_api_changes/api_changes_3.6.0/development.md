# Development changes

## Increase to minimum supported versions of dependencies

For Matplotlib 3.6, the
`minimum supported versions <dependencies>`{.interpreted-text
role="ref"} are being bumped:

+------------+-----------------+---------------+
| Dependency | > min in mpl3.5 | min in mpl3.6 |
+============+=================+===============+
| > Python   | > 3.7           | > 3.8         |
+------------+-----------------+---------------+
| > NumPy    | > 1.17          | > 1.19        |
+------------+-----------------+---------------+

This is consistent with our `min_deps_policy`{.interpreted-text
role="ref"} and
[NEP29](https://numpy.org/neps/nep-0029-deprecation_policy.html)

## Build setup options changes

The `gui_support.macosx` setup option has been renamed to
`packages.macosx`.

## New wheel architectures

Wheels have been added for:

-   Python 3.11
-   PyPy 3.8 and 3.9

## Increase to required versions of documentation dependencies

[sphinx](https://pypi.org/project/Sphinx/) \>= 3.0 and
[numpydoc](https://pypi.org/project/numpydoc/) \>= 1.0 are now required
for building the documentation.

# Development changes

## Documentation-specific custom Sphinx roles are now semi-public

For third-party packages that derive types from Matplotlib, our use of
custom roles may prevent Sphinx from building their docs. These custom
Sphinx roles are now public solely for the purposes of use within
projects that derive from Matplotlib types. See
`matplotlib.sphinxext.roles`{.interpreted-text role="mod"} for details.

## Increase to minimum supported versions of dependencies

For Matplotlib 3.10, the
`minimum supported versions <dependencies>`{.interpreted-text
role="ref"} are being bumped:

+------------+-----------------+----------------+
| Dependency | > min in mpl3.9 | min in mpl3.10 |
+============+=================+================+
| > Python   | > 3.9           | > 3.10         |
+------------+-----------------+----------------+

This is consistent with our `min_deps_policy`{.interpreted-text
role="ref"} and [SPEC0](https://scientific-python.org/specs/spec-0000/)

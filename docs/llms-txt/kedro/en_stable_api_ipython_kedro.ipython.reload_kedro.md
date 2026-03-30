# Source: https://docs.kedro.org/en/stable/api/ipython/kedro.ipython.reload_kedro/index.md

## kedro.ipython.reload_kedro

```
reload_kedro(path=None, env=None, runtime_params=None, local_namespace=None, conf_source=None)
```

Function that underlies the %reload_kedro Line magic. This should not be imported or run directly but instead invoked through %reload_kedro.

Source code in `kedro/ipython/__init__.py`

```
def reload_kedro(
    path: str | None = None,
    env: str | None = None,
    runtime_params: dict[str, Any] | None = None,
    local_namespace: dict[str, Any] | None = None,
    conf_source: str | None = None,
) -> None:  # pragma: no cover
    """Function that underlies the %reload_kedro Line magic. This should not be imported
    or run directly but instead invoked through %reload_kedro."""

    project_path = _resolve_project_path(path, local_namespace)

    metadata = bootstrap_project(project_path)
    _remove_cached_modules(metadata.package_name)
    configure_project(metadata.package_name)

    session = KedroSession.create(
        project_path,
        env=env,
        runtime_params=runtime_params,
        conf_source=conf_source,
    )
    context = session.load_context()
    catalog = context.catalog

    get_ipython().push(  # type: ignore[no-untyped-call]
        variables={
            "context": context,
            "catalog": catalog,
            "session": session,
            "pipelines": pipelines,
        }
    )

    logger.info("Kedro project %s", str(metadata.project_name))
    logger.info(
        "Defined global variable 'context', 'session', 'catalog' and 'pipelines'"
    )

    for line_magic in load_entry_points("line_magic"):
        register_line_magic(needs_local_scope(line_magic))  # type: ignore[no-untyped-call]
        logger.info("Registered line magic '%s'", line_magic.__name__)  # type: ignore[attr-defined]
```

# Source: https://docs.kedro.org/en/stable/api/framework/kedro.framework.startup/index.md

## kedro.framework.startup

This module provides metadata for a Kedro project.

| Name                                                              | Type     | Description                                                                                                    |
| ----------------------------------------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------- |
| [`bootstrap_project`](#kedro.framework.startup.bootstrap_project) | Function | Run setup required at the beginning of the workflow when running in project mode, and return project metadata. |
| [`ProjectMetadata`](#kedro.framework.startup.ProjectMetadata)     | Class    | Structure holding project metadata derived from `pyproject.toml`.                                              |

## kedro.framework.startup.bootstrap_project

```
bootstrap_project(project_path)
```

Run setup required at the beginning of the workflow when running in project mode, and return project metadata.

Source code in `kedro/framework/startup.py`

```
def bootstrap_project(project_path: str | Path) -> ProjectMetadata:
    """Run setup required at the beginning of the workflow
    when running in project mode, and return project metadata.
    """

    project_path = Path(project_path).expanduser().resolve()
    metadata = _get_project_metadata(project_path)
    _add_src_to_path(metadata.source_dir, project_path)
    configure_project(metadata.package_name)
    return metadata
```

## kedro.framework.startup.ProjectMetadata

Bases: `NamedTuple`

Structure holding project metadata derived from `pyproject.toml`

### config_file

```
config_file
```

### example_pipeline

```
example_pipeline
```

### kedro_init_version

```
kedro_init_version
```

### package_name

```
package_name
```

### project_name

```
project_name
```

### project_path

```
project_path
```

### source_dir

```
source_dir
```

### tools

```
tools
```

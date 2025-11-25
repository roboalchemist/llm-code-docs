# Source: https://docs.upsun.com/learn/overview/yaml/yaml-structure.md

# Upsun Fixed YAML structure

In addition to the [basic functions you should be familiar with](https://docs.upsun.com/learn/overview/yaml/what-is-yaml.md), YAML structure is important.
Upsun accepts a specific structure for YAML configuration files.

## YAML file location

When you run the [`upsun project:init` command](https://docs.upsun.com/get-started/here/configure.md), a default ``config.yaml`` file is generated in the `.upsun` folder. It contains the minimum default configuration based on your detected local stack.
This YAML file is located in your ``.upsun`` directory, at the root of your project source code, and is a good starting point before customization.

```bash
.
├── .upsun
|   └── config.yaml
└── <SOURCE_CODE>
```
## Top-level keys
In the ``config.yaml`` file, there are three top-level YAML keys:
- ``applications``: this section of the file contains all of your [app definitions](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md)

**Note**: 

Note that ``applications`` is a **mandatory** top-level key to include in your ``config.yaml`` file.

- ``routes``: this section of the file contains all of your [route definitions](https://docs.upsun.com/define-routes.md) (for each of your apps)
- ``services``: this section of the file contains all of your [service definitions](https://docs.upsun.com/add-services.md) (for each of your apps)

This looks like:
```yaml  {location="apps"}
applications:
  myapp:
    ...

services:
  mariadb:
    type: mariadb:10.6 # All available versions are: 10.6, 10.5, 10.4, 10.3

routes:
  "https://{default}/":
    type: upstream
    upstream: "myapp:http"
```

Below these three top-level key sections, you can use any of the [available YAML tags](https://docs.upsun.com/learn/overview/yaml/platform-yaml-tags.md) you need.

**Note**: 

Any YAML files located at the first level of your ``.upsun`` folder, at the root of your project source code, are taken in account. See [Rules on YAML files](#rules-on-yaml-files).

## Rules on YAML files
The following rules apply to YAML files contained in the ``.upsun`` folder:

- All the existing YAML files located at the first level of the ``.upsun`` folder are taken into account.
- All the existing YAML files located at the first level of the ``.upsun`` folder must feature the [mandatory top-level keys](#top-level-keys), and must contain a [valid YAML configuration](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md).
- All the YAML files in subdirectories of the ``.upsun`` folder need to be [manually imported](https://docs.upsun.com/learn/overview/yaml/platform-yaml-tags.md#include) and contain a [valid YAML configuration](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md).

**Warning**: 

When Upsun combines all the YAML files located at the first level of the ``.upsun`` folder, only the top-level keys (``applications``, ``services``, and ``routes``) are merged. So if you define an app named ``myapp`` in two different YAML files, Upsun only takes the second one into account.

Example:

    .upsun/app.yaml

```yaml {}
applications:
  myapp:
    type: nodejs:16
    source:
      root: folder1
    ...
```

    .upsun/app-bis.yaml

```yaml {}
applications:
  myapp:
    type: nodejs:20
    build:
      flavor: none
    ...
```

Once Upsun has combined the two configuration files,
the blended configuration will be the following:

    YAML config result

```yaml {}
applications:
  myapp:
    type: nodejs:20
    build:
      flavor: none
    ...
```

Note that ``source.root`` (and any other ``.upsun/app.yaml`` parameters) will not be included in the final configuration.



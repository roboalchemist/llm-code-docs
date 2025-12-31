# Source: https://docs.upsun.com/create-apps/app-reference/composable-image.md

# Composable image

The Upsun composable image provides enhanced flexibility when defining your app.
It allows you to install several runtimes and tools in your application container,
in a **"one image to rule them all"** approach.

The composable image is built on [Nix](https://nix.dev), which offers the following benefits:

- You can add as many packages to your application container as you need,
  choosing from over 120,000 packages from [the Nixpkgs collection](https://search.nixos.org/packages).
- The packages you add are built in total isolation, so you can install different versions of the same package.
- With [Nix](https://nix.dev/reference/glossary#term-Nix), there are no undeclared dependencies in your source code.
  What works on your local machine is guaranteed to work on any other machine.

This page introduces all the settings available to configure your composable image from your `.upsun/config.yaml` file
(usually located at the root of your Git repository). 
Note that multi-app projects can be [set in various ways](https://docs.upsun.com../multi-app.md).

If you're pressed for time, jump to this comprehensive [configuration example](https://docs.upsun.com/create-apps.md#comprehensive-example).

## Primary application properties

All application configuration takes place in a `.upsun/config.yaml` file, with each application configured
under a unique key beneath the top-level `applications` key.

It is possible to use multiple runtimes in a single application container,
for instance PHP, NodeJS and Python, while remaining in control of their versions.

For example, the unified `.upsun/config.yaml` file may look like the following:

```yaml  {location=".upsun/config.yaml"}
applications:
  frontend:
    stack:
      - "php@8.5":
          extensions:
            - apcu
            - sodium
            - xsl
            - pdo_sqlite
      - "nodejs@24"
      - "python@3.13"
    # Additional frontend configuration
```

The following table presents all properties available at the level just below the unique application name (`frontend`
above).

The column _Set in instance?_ defines whether the given property can be overridden within a `web` or `workers` instance.
To override any part of a property, you have to provide the entire property.

| Name                | Type                                                                                     | Required | Set in instance? | Description                                                                                                                                                                                                                                                       |
|---------------------|------------------------------------------------------------------------------------------|----------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `type`              | A type                                                                                   | Yes      | No               | [Defines the version of the Nix channel](#supported-nix-channels). Example: `type: "composable:25.05"`                                                                                                                                        |
| `stack`             | An array of [Nix packages](#stack)                                                       | Yes      | No               | A list of packages from the Upsun collection of [supported runtimes](#supported-nix-packages) and/or from [NixPkgs](https://search.nixos.org/packages).                                                                                             |
| `container_profile` | A [container profile](https://docs.upsun.com/manage-resources/adjust-resources.md#advanced-container-profiles) |          | Yes              | Container profile of the application.                                                                                                                                                                                                                             |
| `relationships`     | A dictionary of [relationships](#relationships)                                          |          | Yes              | Connections to other services and apps.                                                                                                                                                                                                                           |
| `mounts`            | A dictionary of [mounts](#mounts)                                                        |          | Yes              | Directories that are writable even after the app is built. Allocated disk for mounts is defined with a separate resource configuration call using `upsun resources:set`.                                                                             |
| `web`               | A [web instance](#web)                                                                   |          | N/A              | How the web application is served.                                                                                                                                                                                                                                |
| `workers`           | A [worker instance](#workers)                                                            |          | N/A              | Alternate copies of the application to run as background processes.                                                                                                                                                                                               |
| `timezone`          | `string`                                                                                 |          | No               | The timezone for crons to run. Format: a [TZ database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). Defaults to `UTC`, which is the timezone used for all logs no matter the value here. See also [app runtime timezones](https://docs.upsun.com../timezone.md). |
| `access`            | An [access dictionary](#access)                                                          |          | Yes              | Access control for roles accessing app environments.                                                                                                                                                                                                              |
| `variables`         | A [variables dictionary](#variables)                                                     |          | Yes              | Variables to control the environment.                                                                                                                                                                                                                             |
| `firewall`          | A [firewall dictionary](#firewall)                                                       |          | Yes              | Outbound firewall rules for the application.                                                                                                                                                                                                                      |
| `hooks`             | A [hooks dictionary](#hooks)                                                             |          | No               | What commands run at different stages in the build and deploy process.                                                                                                                                                                                            |
| `crons`             | A [cron dictionary](#crons)                                                              |          | No               | Scheduled tasks for the app.                                                                                                                                                                                                                                      |
| `source`            | A [source dictionary](#source)                                                           |          | No               | Information on the app's source code and operations that can be run on it.                                                                                                                                                                                        |
| `additional_hosts`  | An [additional hosts dictionary](#additional-hosts)                                      |          | Yes              | Maps of hostnames to IP addresses.                                                                                                                                                                                                                                |
| `operations`        | A [dictionary of Runtime operations](https://docs.upsun.com/create-apps/runtime-operations.md)                 |          | No               | Runtime operations for the application.                                                                                                                                                                                                                           |

**Note**: 

The ``build``, ``dependencies``, and ``runtime`` keys are only supported when using a [single-runtime image](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md).
They are **not** supported when using the composable image.
They are replaced by the ``stack`` key.

## Stack

Use the ``stack`` key to define which runtimes and binaries you want to install in your application container.
Define them as a YAML array as follows:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    stack: [ "@" ]
    # OR
    stack:
      - "@"
```

To add a language to your stack, use the `@` format. 
To add a tool to your stack, use the `` format, as no version is needed.

**Warning**: 

While technically available during the build phase, ``nix`` commands aren’t supported at runtime as the image becomes read-only.

When using the Upsun composable image, you don’t need ``nix`` commands.
Everything you install using the ``stack`` key is readily available to you as the binaries are linked and included in ``$PATH``.
For instance, to [start a secondary runtime](#primary-runtime),
just issue the command (e.g. in the [start](https://docs.upsun.com/create-apps/app-reference/composable-image.md#web-commands)) instead of the ``nix run`` command.

#### Primary runtime

If you add multiple runtimes to your application container,
the first declared runtime becomes the primary runtime.
The primary runtime is the one that is automatically started.

To start other declared runtimes, you need to start them manually, using [web commands](#web-commands).
To find out which start command to use, go to the [Languages](https://docs.upsun.com/languages.md) section,
and visit the documentation page dedicated to your runtime.

**Note**: 

If you use PHP, note that PHP-FPM is only started automatically if PHP is defined as the primary runtime.

### Supported Nix channels

A Nix channel represents a curated, tested snapshot of the Nixpkgs repository, which contains a collection of Nix expressions (code for building packages and configuring systems).

Using the latest stable Nix channel ensures that you get stable, verified packages (not all `git` commits are heavily tested before being merged into the `master` branch).

The following channels are supported:

   - [25.05](https://nixos.org/manual/nixos/stable/release-notes#sec-release-25.05)

### Deprecated Nix channels

The following channels are available but no longer supported.
They're available, but they no longer receive security updates from the Nix community and aren't guaranteed to work.
They'll be removed in the future – consider migrating to a [supported Nix channel](#supported-nix-channels).

   - [24.05](https://nixos.org/manual/nixos/stable/release-notes#sec-release-24.05)

### Configure Nix channels

The Nix channel can be configured with the [top-level property `type`](#primary-application-properties).

For example, to use the Nix channel `25.05`, you would use the following syntax:

```yaml  {location=".upsun/config.yaml"}
type: "composable:25.05"
```

### Supported Nix packages

**Note**: 

The Nix packages listed in the following table are officially supported by Upsun to provide optimal user experience. 
However, you can add any other packages from [the Nixpkgs collection](https://search.nixos.org/) to your ``stack``. 
While available for you to install, packages that aren’t listed in the following table are supported by Nix itself, not Upsun.

Depending on the Nix package, you can select only the major runtime version,
or the major and minor runtime versions as shown in the table.
Security and other patches are applied automatically.

| **Language**                                 | **Nix package** | **Supported version(s)**                        |
|----------------------------------------------|-----------------|-------------------------------------------------|
| [Clojure](https://clojure.org/)              | `clojure`       | 1                                               |
| [Elixir](https://docs.upsun.com/languages/elixir.md)             | `elixir`        | 1.181.151.14                          |
| [Go](https://docs.upsun.com/languages/go.md)                     | `golang`        | 1.221.21                                   |
| [Java](https://docs.upsun.com/languages/java.md)                 | `java`          | 2221                                       |
| [Javascript/Bun](https://bun.sh/)            | `bun`           | 1                                               |
| [JavaScript/Node.js](https://docs.upsun.com/languages/nodejs.md) | `nodejs`        | 24222018                         |
| [Perl](https://www.perl.org/)                | `perl`          | 5                                               |
| [PHP](https://docs.upsun.com/languages/php.md)                   | `php`           | 8.48.38.28.1                     |
| [Python](https://docs.upsun.com/languages/python.md)             | `python`        | 3.133.123.113.103.92.7 |
| [Ruby](https://docs.upsun.com/languages/ruby.md)                 | `ruby`          | 3.43.33.23.1                     |

**Example:**

You want to add PHP version 8.5 and ``facedetect`` to your application container.
To do so, use the following configuration:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    stack: [ "php@8.5", "facedetect" ]
    # OR
    stack:
      - "php@8.5"
      - "facedetect"
```

### PHP extensions and Python packages

When you add PHP or Python to your application container,
you can define which extensions (for PHP) or packages (for Python) you also want to add to your stack.

To find out which extensions you can install with your runtime,
follow these steps:

1. Go to the [NixOS search](https://search.nixos.org/).
2. Enter a runtime and click **Search**.
3. In the **Package sets** side bar, select the right set of extensions/packages for your runtime version. 
   You can choose the desired extensions/packages from the filtered results.

![Screenshot of the Nix package sets selection for PHP@8.3](https://docs.upsun.com/images/nixos/nixos-packages.png "0.5")

#### Install PHP extensions

To enable [PHP extensions](https://docs.upsun.com/languages/php/extensions.md),
specify a list of `extensions` below the language definition. 
To disable [PHP extensions](https://docs.upsun.com/languages/php/extensions.md),
specify a list of `disabled_extensions` below the language definition. 
For instance:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    source:
      root: "/"
    stack:
      - "php@8.5":
          extensions:
            - apcu
            - sodium
            - xsl
            - pdo_sqlite
          disabled_extensions:
            - gd
```

**Note**: 

To help you find out the name of the PHP package you want to use,
some maintainers provide a ``PHP upstream extension`` value in the [NixOS search engine](https://search.nixos.org/packages?channel=unstable&show=php82Extensions.gd).

      ![Screenshot of an upstream extension value shown in the NixOS search](https://docs.upsun.com/images/nixos/nixossearch-upstream-value.png)

If this information is not provided, note that PHP package names on NixOS always respect the ``<PHP><VERSION>Extensions.<EXTENSION-NAME>`` format.
Therefore, you can copy the ``<EXTENSION-NAME>`` as shown in the NixOS search results, and use it in your configuration.
Note that you can use environment variables or your ``php.ini`` file to [include further configuration options](https://docs.upsun.com/languages/php.md#customize-php-settings)
for your PHP extensions.

#### Install Python packages

To install Python packages, add them to your stack as new packages.
To do so, use the full name of the package.

For instance, to install [``python313Packages.yq``](https://search.nixos.org/packages?channel=unstable&show=python313Packages.yq),
use the following configuration:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    stack:
      - "python@3.13"
      - "python312Packages.yq" # python package specific
```

Alternatively, if you need to include configuration options for your extensions, use either your ``php.ini`` file or [environment variables](https://docs.upsun.com/development/variables/set-variables.md).

### Example configuration

Here is a full composable image configuration example. Note the use of the `@` format.

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    stack:
      - "php@8.5":
          extensions:
            - apcu
            - sodium
            - xsl
            - pdo_sqlite
      - "python@3.13"
      - "python313Packages.yq" # python package specific
      - "yq"                   # tool
```

### Combine single-runtime and composable images

In a [multiple application context](https://docs.upsun.com/create-apps/multi-app.md),
you can use a mix of [single-runtime images](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md)
and [composable images](https://docs.upsun.com/create-apps/app-reference/composable-image.md).
Here is an example configuration including a ``frontend`` app and a ``backend`` app:

```yaml  {location=".upsun/config.yaml"}
applications:
  frontend:
    stack:
      - "php@8.5":
          extensions:
            - apcu
            - sodium
            - xsl
            - pdo_sqlite
      - "python@3.13"
      - "python313Packages.yq" # python package specific
  backend:
    type: 'nodejs:24
```

**Note**: 

If you add multiple runtimes to your application container,
the first declared runtime becomes the primary runtime.
The primary runtime is the one that is automatically started.

To start other declared runtimes, you need to start them manually, using [web commands](#web-commands).
To find out which start command to use, go to the [Languages](https://docs.upsun.com/languages.md) section,
and visit the documentation page dedicated to your language.
If you use PHP, note that PHP-FPM is only started automatically if PHP is defined as the primary runtime.

## Resources

Resources for application containers are not committed to YAML files, but instead managed over the API using either the
Console or the `upsun resources:set` command.

For more information, see how to [manage resources](https://docs.upsun.com/manage-resources.md).

**Note**: 

Composable image container profile defaults to ``HIGH_CPU``.
<BR>If multiple runtimes are added to your stack,
you would need to change
the [default container_profile](https://docs.upsun.com/manage-resources/adjust-resources.md#advanced-container-profiles)
or change [default CPU and RAM ratio](https://docs.upsun.com/manage-resources/resource-init.md) on first deployment using the following
commands:

```bash {}
upsun push --resources-init=manual
```

## Relationships

To allow containers in your project to communicate with one another,
you need to define relationships between them.
You can define a relationship between an app and a service, or [between two apps](https://docs.upsun.com/create-apps/multi-app/relationships.md).

The quickest way to define a relationship between your app and a service
is to use the service's default endpoint. 
However, some services allow you to define multiple databases, cores, and/or permissions.
In these cases, you can't rely on default endpoints.
Instead, you can explicitly define multiple endpoints when setting up your relationships.

**Note**: 

App containers don’t have a default endpoint like services.
To connect your app to another app in your project,
you need to explicitly define the ``http`` endpoint as the endpoint to connect both apps. 
For more information, see how to [define relationships between your apps](https://docs.upsun.com/create-apps/multi-app/relationships.md).

**Availability**: 

New syntax (default and explicit endpoints) described below is supported by most, but not all, image types
(``Relationship 'SERVICE_NAME' of application 'myapp' ... targets a service without a valid default endpoint configuration.``).
This syntax is currently being rolled out for all images.
If you encounter this error, use the “legacy” Upsun configuration noted at the bottom of this section.

To define a relationship between your app and a service:

```yaml {}
applications:
  <APP_NAME>:
    # ...
    relationships:
      <SERVICE_NAME>:
```

The ``SERVICE_NAME`` is the name of the service as defined in its [configuration](https://docs.upsun.com/add-services.md).
It is used as the relationship name, and associated with a ``null`` value.
This instructs Upsun to use the service’s default endpoint to connect your app to the service.
For example, if you define the following configuration:

    .upsun/config.yaml

```yaml {}
applications:
  <APP_NAME>:
    # ...
    relationships:
      mariadb:
```

Upsun looks for a service named ``mariadb`` in your ``.upsun/config.yaml`` file,
and connects your app to it through the service’s default endpoint.
For reference, the equivalent configuration using explicit endpoints would be the following:

    .upsun/config.yaml

```yaml {}
applications:
  <APP_NAME>:
    # ...
    relationships:
      mariadb:
        service: mariadb
        endpoint: mysql
```

You can define any number of relationships in this way:

    .upsun/config.yaml

```yaml {}
applications:
  <APP_NAME>:
    # ...
    relationships:
      mariadb:
      redis:
      elasticsearch:
```

**Tip**: 

An even quicker way to define many relationships is to use the following single-line configuration:

    .upsun/config.yaml

```yaml {}
applications:
  <APP_NAME>:
    # ...
    relationships: {<SERVICE_NAME_A>, <SERVICE_NAME_B>, <SERVICE_NAME_C>}

services:
  <SERVICE_NAME_A>:
    type: mariadb:11.8
  <SERVICE_NAME_B>:
    type: redis:8.0
  <SERVICE_NAME_C>:
    type: elasticsearch:8.5
```

Use the following configuration:

    .upsun/config.yaml

```yaml {}
applications:
  <APP_NAME>:
    # ...
    relationships:
      <RELATIONSHIP_NAME>:
        service: <SERVICE_NAME>
        endpoint: <ENDPOINT_NAME>
```

 - ``RELATIONSHIP_NAME`` is the name you want to give to the relationship.
 - ``SERVICE_NAME`` is the name of the service as defined in its [configuration](https://docs.upsun.com/add-services.md).
 - ``ENDPOINT_NAME`` is the endpoint your app will use to connect to the service (refer to the service reference to know which value to use).

For example, to define a relationship named ``database`` that connects your app to a service called ``mariadb`` through the ``db1`` endpoint,
use the following configuration:

    .upsun/config.yaml

```yaml {}
applications:
  <APP_NAME>:
    # ...
    relationships:
      database: # The name of the relationship.
        service: mariadb
        endpoint: db1
```

For more information on how to handle multiple databases, multiple cores,
and/or different permissions with services that support such features,
see each service’s dedicated page:

 - [MariaDB/MySQL](https://docs.upsun.com/add-services/mysql.md#multiple-databases) (multiple databases and permissions)
 - [PostgreSQL](https://docs.upsun.com/add-services/postgresql.md#multiple-databases) (multiple databases and permissions)
 - [Redis](https://docs.upsun.com/add-services/redis.md#multiple-databases) (multiple databases)
 - [Solr](https://docs.upsun.com/add-services/solr.md#solr-6-and-later) (multiple cores)
 - [Vault KMS](https://docs.upsun.com/add-services/vault.md#multiple-endpoints-example) (multiple permissions)

You can add as many relationships as you want to your app configuration,
using both default and explicit endpoints according to your needs:

    .upsun/config.yaml

```yaml {}
applications:
  <APP_NAME>:
    # ...
    relationships:
      database1:
        service: mariadb
        endpoint: admin
      database2:
        service: mariadb
        endpoint: legacy
      cache:
        service: redis
      search:
        service: elasticsearch
```

**Legacy**: 

The following legacy syntax for specifying relationships is still supported by Upsun:

    .upsun/config.yaml

```yaml {}
applications:
  <APP_NAME>:
    # ...
    relationships:
      <RELATIONSHIP_NAME>: "<SERVICE_NAME>:<ENDPOINT_NAME>"

services:
  SERVICE_NAME_A:
    type: mariadb:11.8
```

For example:

    .upsun/config.yaml

```yaml {}
applications:
  <APP_NAME>:
    # ...
    relationships:
      database: "db:mysql"

services:
  db:
    type: mariadb:11.8
```

Feel free to use this until the default and explicit endpoint syntax is supported on all images.

## Available disk space

Disk for application containers are not committed to YAML files, but instead managed over the API using either the
Console or the `upsun resources:set` command.

For more information, see how to [manage resources](https://docs.upsun.com/manage-resources.md).

### Downsize a disk

You can decrease the size of an existing disk for an app. If you do so, be aware that:

- Backups from before the downsize are incompatible and can no longer be used. You need to [create new backups](https://docs.upsun.com/environments/backup.md).
- The downsize fails if there’s more data on the disk than the desired size.

## Mounts

After your app is built, its file system is read-only.
To make changes to your app's code, you need to use Git.

For enhanced flexibility, Upsun allows you to define and use writable directories called "mounts".
Mounts give you write access to files generated by your app (such as cache and log files)
and uploaded files without going through Git.

When you define a mount, you are mounting an external directory to your app container,
much like you would plug a hard drive into your computer to transfer data.

**Note**: 

 - Mounts aren’t available during the build
 - When you [back up an environment](https://docs.upsun.com/environments/backup.md), the mounts on that environment are backed up too

### Define a mount

To define a mount, use the following configuration:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    source:
      root: "/"
    stack: [ "nodejs@24" ]
    mounts:
      '<MOUNT_PATH>':
        source: <MOUNT_TYPE>
        source_path: <SOURCE_PATH_LOCATION>
```

<MOUNT_PATH> is the path to your mount **within the app container** (relative to the app's root).
If you already have a directory with that name, you get a warning that it isn't accessible after the build.
See how to [troubleshoot the warning](https://docs.upsun.com../troubleshoot-mounts.md#overlapping-folders).

| Name          | Type                           | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------|--------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `source`      | `storage`, `instance`, `tmp`, or `service` | Yes      | Specifies the type of the mount:- By design, `storage` mounts can be shared between instances of the same app. You can also configure them so they are [shared between different apps](#share-a-mount-between-several-apps).-`instance` mounts are local mounts. Unique to your app, they are useful to store files that remain local to the app instance, such as application logs.- `tmp` mounts are local ephemeral mounts, where an external directory is mounted to the `/tmp` directory of your app.The content of a `tmp` mount **may be removed during infrastructure maintenance operations**. Therefore, `tmp` mounts allow you to **store files that you’re not afraid to lose**, such as your application cache that can be seamlessly rebuilt.Note that the `/tmp` directory has **a maximum allocation of 8 GB**.- `service` mounts can be useful if you want to explicitly define and use a [Network Storage](https://docs.upsun.com/add-services/network-storage.md) service to share data between different apps (instead of using a `storage` mount). |
| `source_path` | `string`                       | No       | Specifies where the mount points **inside the [external directory](#mounts)**. - If you explicitly set a `source_path`, your mount points to a specific subdirectory in the external directory.  - If the `source_path` is an empty string (`""`), your mount points to the entire external directory. - If you don't define a `source_path`, Upsun uses the <MOUNT_PATH> as default value, without leading or trailing slashes. For example, if your mount lives in the `/web/uploads/` directory in your app container, it will point to a directory named `web/uploads` in the external directory.     **WARNING:** Changing the name of your mount affects the `source_path` when it's undefined. See [how to ensure continuity](#ensure-continuity-when-changing-the-name-of-your-mount) and maintain access to your files.                         |
| `service`     | `string`                       |          | The purpose of the `service` key depends on your use case.   In a multi-app context where a `storage` mount is shared between apps, `service` is required. Its value is the name of the app whose mount you want to share. See how to [share a mount between several apps](#share-a-mount-between-several-apps).   In a multi-app context where a [Network Storage service](https://docs.upsun.com/add-services/network-storage.md) (`service` mount) is shared between apps, `service` is required and specifies the name of that Network Storage.                                                                                                                                                                                                                                                                                                                                                                                     |

The accessibility to the web of a mounted directory depends on the [`web.locations` configuration](#web).
Files can be all public, all private, or with different rules for different paths and file types.

Note that when you remove a `tmp` mount from your `.upsun/config.yaml` file,
the mounted directory isn't deleted.
The files still exist on disk until manually removed,
or until the app container is moved to another host during a maintenance operation.

### Example configuration

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    source:
      root: "/"
    stack: [ "nodejs@24" ]
    mounts:
      'web/uploads':
        source: storage
        source_path: uploads
      '/.tmp_platformsh':
        source: tmp
        source_path: files/.tmp_platformsh
      '/build':
        source: storage
        source_path: files/build
      '/.cache':
        source: tmp
        source_path: files/.cache
      '/node_modules/.cache':
        source: tmp
        source_path: files/node_modules/.cache
```

### Ensure continuity when changing the name of your mount

Changing the name of your mount affects the default `source_path`.

Say you have a `/my/cache/` mount with an undefined `source_path`:

```yaml  {location=".upsun/config.yaml"}
mounts:
  '/my/cache/':
    source: tmp
```

If you rename the mount to `/cache/files/`, it will point to a new, empty `/cache/files/` directory.

To ensure continuity, you need to explicitly define the `source_path` as the previous name of the mount, without leading
or trailing slashes:

 ```yaml  {location=".upsun/config.yaml"}
mounts:
  '/cache/files/':
    source: tmp
    source_path: my/cache
```

The `/cache/files/` mount will point to the original `/my/cache/` directory, maintaining access to all your existing
files in that directory.

### Share a mount between several apps

By design, [`storage` mounts](#mounts) are shared **between different instances of the same app**,
which enables [horizontal scaling](https://docs.upsun.com/manage-resources.md).

In a [multi-application context](https://docs.upsun.com/create-apps/multi-app.md),
you can even share a `storage` mount **between different applications** in the same project.

To do so, you need to define a `storage` mount in each of your app containers,
and point each of those mounts to the same shared external network directory.

Use the following configuration:

```yaml  {location=".upsun/config.yaml"}
applications:
  app1:
    mounts:
      '<MOUNT_PATH_1>':
        source: storage
        source_path: <SOURCE_PATH_LOCATION>

  app2:
    mounts:
      '<MOUNT_PATH_2>':
        source: storage
        service: app1
        source_path: <SOURCE_PATH_LOCATION>
```

- <MOUNT_PATH_1> and <MOUNT_PATH_2> are the paths to each mount **within their
  respective app container** (relative to the app's root).
- When configuring the first `storage` mount, you don't need to include the `service` key.
  The first mount implicitly points to an external network directory.
  The `service` key is required for subsequent mounts, to ensure they use the same external network directory as the
  first mount.
- The `source_path` allows you to point each mount to the same subdirectory **within the shared external network
  directory**.

**Example**: 

You have a ``backend`` app and a ``frontend`` app.
You want both apps to share data from the same mount. 
Follow these steps:

 - In your ``backend`` app configuration, define a ``storage`` mount:

    .upsun/config.yaml

```yaml {}
applications:
  backend:
    mounts:
      var/uploads: #The path to your mount within the backend app container.
        source: storage
        source_path: backend/uploads #The path to the source of the mount within the external network directory.
```

This creates a ``storage`` mount named ``var/uploads`` in the ``backend`` app container.
The mount points to the ``backend/uploads`` directory within an external network directory.

 - In your ``frontend`` app configuration, define another ``storage`` mount:

    .upsun/config.yaml

```yaml {}
applications:
  backend:
    mounts:
      var/uploads:
        source: storage
        source_path: backend/uploads

  frontend:
    mounts:
      web/uploads: #The path to your mount within the frontend app container.
        source: storage
        service: backend #The name of the other app, so the mount can point to the same external network directory as that other app's mount.
        source_path: backend/uploads #The path to the source of the mount within the shared external network directory.
```

This creates another ``storage`` mount named ``web/uploads`` in the ``frontend`` app container.
The ``service`` key allows you to specify that the ``web/uploads`` mount should use the same external network directory
as the mount previously defined in the ``backend`` app container.
The ``source_path`` key specifies which subdirectory within the external network directory both mounts should share (
here, the ``backend/uploads`` directory).

Note that another way to share data between apps through a mount is by
explicitly [defining a Network Storage service](https://docs.upsun.com/add-services/network-storage.md).

### Local mounts

If you need a local mount (i.e. unique per container),
Upsun allows you to mount a directory within the `/tmp` directory of your app.
However, the following limitations apply:

- Content from `tmp` mounts is removed when your app container is moved to another host during an infrastructure
  maintenance operation
- The `/tmp` directory has a [maximum allocation of 8 GB](https://docs.upsun.com/create-apps/troubleshoot-disks.md#no-space-left-on-device)

Therefore, `tmp` mounts are ideal to store non-critical data, such as your application cache which can be seamlessly
rebuilt,
but aren't suitable for storing files that are necessary for your app to run smoothly.

Note that Upsun will provide new local mounts in the near future.

### Overlapping mounts

The locations of mounts as they are visible to application containers can overlap somewhat.
For example:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    # ...
    mounts:
      'var/cache_a':
        source: storage
        source_path: cacheA
      'var/cache_b':
        source: tmp
        source_path: cacheB
      'var/cache_c':
        source: instance
        source_path: cacheC
```

In this case, it does not matter that each mount is of a different `source` type.
Each mount is restricted to a subfolder within `var`, and all is well.

The following, however, is not allowed and will result in a failure:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    # ...
    mounts:
      'var/':
        source: storage
        source_path: cacheA
      'var/cache_b':
        source: tmp
        source_path: cacheB
      'var/cache_c':
        source: instance
        source_path: cacheC
```

The `storage` mount type specifically exists to share data between instances of the same application, whereas `tmp` and `instance` are meant to restrict data to build time and runtime of a single application instance, respectively.
These allowances are not compatible, and will result in an error if pushed.

## Web

Use the `web` key to configure the web server running in front of your app.

| Name        | Type                                       | Required                      | Description                                          |
|-------------|--------------------------------------------|-------------------------------|------------------------------------------------------|
| `commands`  | A [web commands dictionary](#web-commands) | See [note](#required-command) | The command to launch your app.                      |
| `upstream`  | An [upstream dictionary](#upstream)        |                               | How the front server connects to your app.           |
| `locations` | A [locations dictionary](#locations)       |                               | How the app container responds to incoming requests. |

See some [examples of how to configure what's served](https://docs.upsun.com../web.md).

### Web commands

| Name         | Type     | Required                      | Description                                                                                         |
|--------------|----------|-------------------------------|-----------------------------------------------------------------------------------------------------|
| `pre_start`  | `string` |                               | Command run just prior to `start`, which can be useful when you need to run _per-instance_ actions. |
| `start`      | `string` | See [note](#required-command) | The command to launch your app. If it terminates, it's restarted immediately.                       |
| `post_start` | `string` |                               | Command runs **before** adding the container to the router and **after** the `start` command.       |

**Note**: 

The ``pre_start`` feature is **not blocking**, which means the ``deploy`` hook may start running **before** the ``pre_start`` command finishes.
This can lead to unexpected behavior if ``pre_start`` performs setup tasks that ``deploy`` depends on.
To avoid issues, make sure any critical initialization in ``pre_start`` is either quick or safe to run concurrently with ``deploy``.

The ``post_start`` feature is experimental and may change. Please share your feedback in the
[Upsun discord](https://discord.gg/upsun/).

Example:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    source:
      root: "/"
    stack: [ "python@3.13" ]
    web:
      commands:
        start: 'uwsgi --ini conf/server.ini'
```

This command runs every time your app is restarted, regardless of whether or not new code is deployed.

**Note**: 

Never “background” a start process using ``&``.
That’s interpreted as the command terminating and the supervisor process starts a second copy,
creating an infinite loop until the container crashes.
Just run it as normal and allow the Upsun supervisor to manage it.

#### Required command

On all containers other than PHP, the value for `start` should be treated as required.

On PHP containers, it's optional and defaults to starting PHP-FPM (`/usr/bin/start-php-app`).
It can also be set explicitly on a PHP container to run a dedicated process,
such as [React PHP](https://github.com/platformsh-examples/platformsh-example-reactphp)
or [Amp](https://github.com/platformsh-examples/platformsh-example-amphp).
See how to set up [alternate start commands on PHP](https://docs.upsun.com/languages/php.md#alternate-start-commands).

### Upstream

| Name            | Type                | Required | Description                                                       | Default                                                                                                   |
|-----------------|---------------------|----------|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| `socket_family` | `tcp` or `unix`     |          | Whether your app listens on a Unix or TCP socket.                 | Defaults to `tcp` for all [primary runtimes](#primary-runtime) except PHP; for PHP the default is `unix`. |
| `protocol`      | `http` or `fastcgi` |          | Whether your app receives incoming requests over HTTP or FastCGI. | Default varies based on the [primary runtimes](#primary-runtime).                                         |

For PHP, the defaults are configured for PHP-FPM and shouldn't need adjustment.
For all other containers, the default for `protocol` is `http`.

The following example is the default on non-PHP containers:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    source:
      root: "/"
    stack: [ "python@3.13" ]
    web:
      upstream:
        socket_family: tcp
        protocol: http
```

#### Where to listen

Where to listen depends on your setting for `web.upstream.socket_family` (defaults to `tcp`).

| `socket_family` | Where to listen                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| `tcp`           | The port specified by the [`PORT` environment variable](https://docs.upsun.com/development/variables/use-variables.md#use-provided-variables)               |
| `unix`          | The Unix socket file specified by the [`SOCKET` environment variable](https://docs.upsun.com/development/variables/use-variables.md#use-provided-variables) |

If your application isn't listening at the same place that the runtime is sending requests,
you see `502 Bad Gateway` errors when you try to connect to your website.

### Locations

Each key in the `locations` dictionary is a path on your site with a leading `/`.
For `example.com`, a `/` matches `example.com/` and `/admin` matches `example.com/admin`.
When multiple keys match an incoming request, the most-specific applies.

The following table presents possible properties for each location:

| Name                | Type                                                 | Default   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|---------------------|------------------------------------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `root`              | `string`                                             |           | The directory to serve static assets for this location relative to the app's root directory ([see `source.root`](#source)). Must be an actual directory inside the root directory.                                                                                                                                                                                                                                                                                                                                              |
| `passthru`          | `boolean` or  `string`                               | `false`   | Whether to forward disallowed and missing resources from this location to the app. A string is a path with a leading `/` to the controller, such as `/index.php`. <BR> <BR> If your app is in PHP, when setting `passthru` to `true`, you might want to set `scripts` to `false` for enhanced security. This prevents PHP scripts from being executed from the specified location. You might also want to set `allow` to `false` so that not only PHP scripts can't be executed, but their source code also can't be delivered. |
| `index`             | Array of `string`s or `null`                         |           | Files to consider when serving a request for a directory. When set, requires access to the files through the `allow` or `rules` keys.                                                                                                                                                                                                                                                                                                                                                                                           |
| `expires`           | `string`                                             | `-1`      | How long static assets are cached. The default means no caching. Setting it to a value enables the `Cache-Control` and `Expires` headers. Times can be suffixed with `ms` = milliseconds, `s` = seconds, `m` = minutes, `h` = hours, `d` = days, `w` = weeks, `M` = months/30d, or `y` = years/365d.                                                                                                                                                                                                                            |
| `allow`             | `boolean`                                            | `true`    | Whether to allow serving files which don't match a rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `scripts`           | `boolean`                                            |           | Whether to allow scripts to run. Doesn't apply to paths specified in `passthru`. Meaningful only on PHP containers.                                                                                                                                                                                                                                                                                                                                                                                                             |
| `headers`           | A headers dictionary                                 |           | Any additional headers to apply to static assets, mapping header names to values (see [Set custom headers on static content](https://docs.upsun.com/create-apps/web/custom-headers.md)). Responses from the app aren't affected.                                                                                                                                                                                                                                                                                                                    |
| `request_buffering` | A [request buffering dictionary](#request-buffering) | See below | Handling for chunked requests.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `rules`             | A [rules dictionary](#rules)                         |           | Specific overrides for specific locations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

#### Rules

The rules dictionary can override most other keys according to a regular expression.
The key of each item is a regular expression to match paths exactly.
If an incoming request matches the rule, it's handled by the properties under the rule,
overriding any conflicting rules from the rest of the `locations` dictionary.

Under `rules`, you can set all the other possible [`locations` properties](#locations)
except `root`, `index`, `rules` and `request_buffering`.

In the following example, the `allow` key disallows requests for static files anywhere in the site.
This is overridden by a rule that explicitly allows common image file formats.

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    source:
      root: "/"
    stack: [ "python@3.13" ]
    web:
      locations:
        '/':
          # Handle dynamic requests
          root: 'public'
          passthru: '/index.php'
          # Disallow static files
          allow: false
          rules:
            # Allow common image files only.
            '\.(jpe?g|png|gif|svgz?|css|js|map|ico|bmp|eot|woff2?|otf|ttf)$':
              allow: true
```

#### Request buffering

Request buffering is enabled by default to handle chunked requests as most app servers don't support them.
The following table shows the keys in the `request_buffering` dictionary:

| Name               | Type      | Required | Default | Description                               |
|--------------------|-----------|----------|---------|-------------------------------------------|
| `enabled`          | `boolean` | Yes      | `true`  | Whether request buffering is enabled.     |
| `max_request_size` | `string`  |          | `250m`  | The maximum size to allow in one request. |

The default configuration would look like this:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    source:
      root: "/"
    stack: [ "python@3.13" ]
    web:
      locations:
        '/':
          passthru: true
          request_buffering:
            enabled: true
            max_request_size: 250m
```

## Workers

Workers are exact copies of the code and compilation output as a `web` instance after a [`build` hook](#hooks).
They use the same container image.

Workers can't accept public requests and so are suitable only for background tasks.
If they exit, they're automatically restarted.

The keys of the `workers` definition are the names of the workers.
You can then define how each worker differs from the `web` instance using
the [top-level properties](#primary-application-properties).

Each worker can differ from the `web` instance in all properties _except_ for:

- `crons` as cron jobs don't run on workers
- `hooks` as the `build` hook must be the same
  and the `deploy` and `post_deploy` hooks don't run on workers.

A worker named `queue` that was small and had a different start command could look like this:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    source:
      root: "/"
    stack: [ "python@3.13" ]
    workers:
      queue:
        commands:
          start: |
            ./worker.sh
```

Workers require resource definition using `upsun resources:set`, same as application containers.
For more information, see how to [manage resources](https://docs.upsun.com/manage-resources.md).

## Access

The `access` dictionary has one allowed key:

| Name  | Allowed values                      | Default       | Description                                                           |
|-------|-------------------------------------|---------------|-----------------------------------------------------------------------|
| `ssh` | `admin`, `contributor`, or `viewer` | `contributor` | Defines the minimum role required to access app environments via SSH. |

In the following example, only users with `admin` permissions for the
given [environment type](https://docs.upsun.com/administration/users.md#environment-type-roles)
can access the deployed environment via SSH:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    source:
      root: "/"
    stack: [ "python@3.13" ]
    access:
      ssh: admin
```

## Variables

Upsun provides a number of ways to set [variables](https://docs.upsun.com/development/variables.md).
Variables set in your app configuration have the lowest precedence,
meaning they're overridden by any conflicting values provided elsewhere.

All variables set in your app configuration must have a prefix.
Some [prefixes have specific meanings](https://docs.upsun.com/development/variables.md#variable-prefixes).

Variables with the prefix `env` are available as a separate environment variable.
All other variables are available in
the [`PLATFORM_VARIABLES` environment variable](https://docs.upsun.com/development/variables/use-variables.md#use-provided-variables).

The following example sets two variables:

- A variable named `env:AUTHOR` with the value `Juan` that's available in the environment as `AUTHOR`
- A variable named `d8config:system.site:name` with the value `My site rocks`
  that's available in the `PLATFORM_VARIABLES` environment variable

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    source:
      root: "/"
    stack: [ "python@3.13" ]
    variables:
      env:
        AUTHOR: 'Juan'
      d8config:
        "system.site:name": 'My site rocks'
```

You can also define and access more [complex values](https://docs.upsun.com/development/variables/use-variables.md#access-complex-values).

## Firewall

Set limits in outbound traffic from your app with no impact on inbound requests.

The `outbound` key is required and contains one or more rules.
The rules define what traffic is allowed; anything unspecified is blocked.

Each rule has the following properties where at least one is required and `ips` and `domains` can't be specified
together:

| Name      | Type                | Default         | Description                                                                                                                                                                                                             |
|-----------|---------------------|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ips`     | Array of `string`s  | `["0.0.0.0/0"]` | IP addresses in [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing). See a [CIDR format converter](https://www.ipaddressguide.com/cidr).                                                      |
| `domains` | Array of `string`s  |                 | [Fully qualified domain names](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) to specify specific destinations by hostname.                                                                                 |
| `ports`   | Array of `integer`s |                 | Ports from 1 to 65535 that are allowed. If any ports are specified, all unspecified ports are blocked. If no ports are specified, all ports are allowed. Port `25`, the SMTP port for sending email, is always blocked. |

The default settings would look like this:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    source:
      root: "/"
    stack: [ "python@3.13" ]
    firewall:
      outbound:
        - ips: [ "0.0.0.0/0" ]
```

### Support for rules

Where outbound rules for firewalls are supported in all environments.

### Multiple rules

Multiple firewall rules can be specified.
In such cases, a given outbound request is allowed if it matches _any_ of the defined rules.

So in the following example requests to any IP on port 80 are allowed
and requests to 1.2.3.4 on either port 80 or 443 are allowed:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    source:
      root: "/"
    stack: [ "python@3.13" ]
    firewall:
      outbound:
        - ips: [ "1.2.3.4/32" ]
          ports: [ 443 ]
        - ports: [ 80 ]
```

### Outbound traffic to CDNs

Be aware that many services are behind a content delivery network (CDN).
For most CDNs, routing is done via domain name, not IP address,
so thousands of domain names may share the same public IP addresses at the CDN.
If you allow the IP address of a CDN, you are usually allowing many or all of the other customers hosted behind that
CDN.

### Outbound traffic by domain

You can filter outbound traffic by domain.
Using domains in your rules rather than IP addresses is generally more specific and secure.
For example, if you use an IP address for a service with a CDN,
you have to allow the IP address for the CDN.
This means that you allow potentially hundreds or thousands of other servers also using the CDN.

An example rule filtering by domain:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    source:
      root: "/"
    stack: [ "python@3.13" ]
    firewall:
      outbound:
        - protocol: tcp
          domains: [ "api.stripe.com", "api.twilio.com" ]
          ports: [ 80, 443 ]
        - protocol: tcp
          ips: [ "1.2.3.4/29","2.3.4.5" ]
          ports: [ 22 ]
```

#### Determine which domains to allow

To determine which domains to include in your filtering rules,
find the domains your site has requested the DNS to resolve.
Run the following command to parse your server’s `dns.log` file
and display all Fully Qualified Domain Names that have been requested:

```bash
awk '/query\[[^P]\]/ { print $6 | "sort -u" }' /var/log/dns.log
```

The output includes all DNS requests that were made, including those blocked by your filtering rules.
It doesn't include any requests made using an IP address.

Example output:

```bash
facebook.com
fastly.com
upsun.com
www.google.com
www.upsun.com
```
## Hooks

There are three different hooks that run as part of the process of building and deploying your app.
These are places where you can run custom scripts.
They are: the `build` hook, the `deploy` hook, and the `post_deploy` hook.
Only the `build` hook is run for [worker instances](#workers), while [web instances](#web) run all three.

The process is ordered as:

1. Variables accessible at build time become available.
1. The `build` hook is run.
1. The file system is changed to read only (except for any [mounts](#mounts)).
1. The app container starts. Variables accessible at runtime and services become available.
1. The `deploy` hook is run.
1. The app container begins accepting requests.
1. The `post_deploy` hook is run.

Note that if an environment changes by no code changes, only the last step is run.
If you want the entire process to run, see how
to [manually trigger builds](https://docs.upsun.com/development/troubleshoot.md#manually-trigger-builds).

### Writable directories during build

During the `build` hook, there are three writeable directories:

- `PLATFORM_APP_DIR`:
  Where your code is checked out and the working directory when the `build` hook starts.
  Becomes the app that gets deployed.
- `PLATFORM_CACHE_DIR`:
  Persists between builds, but isn't deployed.
  Shared by all builds on all branches.
- `/tmp`:
  Isn't deployed and is wiped between each build.
  Note that `PLATFORM_CACHE_DIR` is mapped to `/tmp`
  and together they offer about 8GB of free space.

### Hook failure

Each hook is executed as a single script, so they're considered to have failed only if the final command in them fails.
To cause them to fail on the first failed command, add `set -e` to the beginning of the hook.

If a `build` hook fails for any reason, the build is aborted and the deploy doesn't happen.
Note that this only works for `build` hooks --
if other hooks fail, the app is still deployed.

#### Automated testing

It’s preferable that you set up and run automated tests in a dedicated CI/CD tool.
Relying on Upsun hooks for such tasks can prove difficult.

During the `build` hook, you can halt the deployment on a test failure but the following limitations apply:

- Access to services such as databases, Redis, Vault KMS, and even writable mounts is disabled.
  So any testing that relies on it is sure to fail.
- If you haven’t made changes to your app, an existing build image is reused and the build hook isn’t run.
- Test results are written into your app container, so they might get exposed to a third party.

During the `deploy` hook, you can access services but **you can’t halt the deployment based on a test failure**.
Note that there are other downsides:

- Your app container is read-only during the deploy hook,
  so if your tests need to write reports and other information, you need to create a file mount for them.
- Your app can only be deployed once the deploy hook has been completed.
  Therefore, running automated testing via the deploy hook generates slower deployments.
- Your environment isn’t available externally during the deploy hook.
  Unit and integration testing might work without the environment being available,
  but you can’t typically perform end-to-end testing until after the environment is up and available.

## Crons

The keys of the `crons` definition are the names of the cron jobs.
The names must be unique.

If an application defines both a `web` instance and `worker` instances, cron jobs run only on the `web` instance.

See how to [get cron logs](https://docs.upsun.com/increase-observability/logs/access-logs.md#container-logs).

The following table shows the properties for each job:

| Name               | Type                                         | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------------------|----------------------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `spec`             | `string`                                     | Yes      | The [cron specification](https://en.wikipedia.org/wiki/Cron#Cron_expression). To prevent competition for resources that might hurt performance, use `H` in definitions to indicate an unspecified but invariant time. For example, instead of using `0 * * * *` to indicate the cron job runs at the start of every hour, you can use `H * * * *` to indicate it runs every hour, but not necessarily at the start. This prevents multiple cron jobs from trying to start at the same time. |
| `commands`         | A [cron commands dictionary](#cron-commands) | Yes      | A definition of what commands to run when starting and stopping the cron job.                                                                                                                                                                                                                                                                                                                                                                                                               |
| `shutdown_timeout` | `integer`                                    | No       | When a cron is canceled, this represents the number of seconds after which a `SIGKILL` signal is sent to the process to force terminate it. The default is `10` seconds.                                                                                                                                                                                                                                                                                                                    |
| `timeout`          | `integer`                                    | No       | The maximum amount of time a cron can run before it's terminated. Defaults to the maximum allowed value of `86400` seconds (24 hours).                                                                                                                                                                                                                                                                                                                                                      |

Note that you can [cancel pending or running crons](https://docs.upsun.com/environments/cancel-activity.md).

### Cron commands

| Name    | Type     | Required | Description                                                                                                                                                                                                                                                                        |
|---------|----------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `start` | `string` | Yes      | The command that's run. It's run in [Dash](https://en.wikipedia.org/wiki/Almquist_shell).                                                                                                                                                                                          |
| `stop`  | `string` | No       | The command that's issued to give the cron command a chance to shutdown gracefully, such as to finish an active item in a list of tasks. Issued when a cron task is interrupted by a user through the CLI or Console. If not specified, a `SIGTERM` signal is sent to the process. |

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    source:
      root: "/"
    stack: [ "nodejs@24" ]
    crons:
      mycommand:
        spec: 'H * * * *'
        commands:
          start: sleep 60 && echo sleep-60-finished && date
          stop: killall sleep
        shutdown_timeout: 18
```

In this example configuration, the [cron specification](#crons) uses the `H` syntax.

### Example cron jobs

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    stack: [ "php@8.5" ]
    crons:
      # Run Drupal's cron tasks every 19 minutes.
      drupal:
        spec: '*/19 * * * *'
        commands:
          start: 'cd web ; drush core-cron'
      # But also run pending queue tasks every 7 minutes.
      # Use an odd number to avoid running at the same time as the `drupal` cron.
      drush-queue:
        spec: '*/7 * * * *'
        commands:
          start: 'cd web ; drush queue-run aggregator_feeds'
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    stack: [ "ruby@3.4" ]
    crons:
      # Execute a rake script every 19 minutes.
      ruby:
        spec: '*/19 * * * *'
        commands:
          start: 'bundle exec rake some:task'
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    stack: [ "php@8.5" ]
    crons:
      # Run Laravel's scheduler every 5 minutes.
      scheduler:
        spec: '*/5 * * * *'
        commands:
          start: 'php artisan schedule:run'
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"
    stack: [ "php@8.5" ]
    crons:
      # Take a backup of the environment every day at 5:00 AM.
      snapshot:
        spec: 0 5 * * *
        commands:
          start: |
            # Only run for the production environment, aka main branch
            if [ "$PLATFORM_ENVIRONMENT_TYPE" = "production" ]; then
                croncape symfony ...
            fi            
```

### Conditional crons

If you want to set up customized cron schedules depending on the environment type,
define conditional crons.
To do so, use a configuration similar to the following:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    source:
      root: "/"
    stack: [ "php@8.5" ]
    crons:
      update:
        spec: '0 0 * * *'
        commands:
          start: |
            if [ "$PLATFORM_ENVIRONMENT_TYPE" = production ]; then
              upsun backup:create --yes --no-wait
              upsun source-operation:run update --no-wait --yes
            fi
```

### Cron job timing

The minimum time between cron jobs being triggered is 5 minutes.

For each app container, only one cron job can run at a time.
If a new job is triggered while another is running, the new job is paused until the other completes.

To minimize conflicts, a random offset is applied to all triggers.
The offset is a random number of seconds up to 20 minutes or the cron frequency, whichever is smaller.

Crons are also paused while activities such as [backups](https://docs.upsun.com/environments/backup.md) are running.
The crons are queued to run after the other activity finishes.

To run cron jobs in a timezone other than UTC, set the [timezone property](#primary-application-properties).

### Paused crons

[Preview environments](https://docs.upsun.com/glossary.md#preview-environment) are often used for a limited time and then abandoned.
While it's useful for environments under active development to have scheduled tasks,
unused environments don't need to run cron jobs.
To minimize unnecessary resource use,
crons on environments with no deployments are paused.

This affects all preview environments, _and_ production environment that do not yet have a domain attached to them.

Such environments with deployments within 14 days have crons with the status `running`.
If there haven't been any deployments within 14 days, the status is `paused`.

You can see the status in the Console
or using the CLI by running `upsun environment:info` and looking under `deployment_state`.

#### Restarting paused crons

If the crons on your preview environment are paused but you're still using them,
you can push changes to the environment or redeploy it.

To restart crons without changing anything:

Run the following command:

```bash {}
upsun redeploy
```

### Sizing hints

The following table shows the properties that can be set in `sizing_hints`:

| Name              | Type      | Default | Minimum | Description                                    |
|-------------------|-----------|---------|---------|------------------------------------------------|
| `request_memory`  | `integer` | 45      | 10      | The average memory consumed per request in MB. |
| `reserved_memory` | `integer` | 70      | 70      | The amount of memory reserved in MB.           |

See more about [PHP-FPM workers and sizing](https://docs.upsun.com/languages/php/fpm.md).

## Source

The following table shows the properties that can be set in `source`:

| Name         | Type                     | Required | Description                                                                                                                       |
|--------------|--------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------|
| `operations` | An operations dictionary |          | Operations that can be applied to the source code. See [source operations](https://docs.upsun.com../source-operations.md)                               |
| `root`       | `string`                 |          | The path where the app code lives. Defaults to the root project directory. Useful for [multi-app setups](https://docs.upsun.com../multi-app.md). |

## Container profile

By default, Upsun allocates a container profile to each app and service depending on the range of resources it’s
expected to need.

Each container profile gives you access to a specific list of CPU and RAM combinations.
Using the Upsun CLI or Console, you can then pick a CPU and RAM combination for each of your apps and services.

- [Container profile types and resources](https://docs.upsun.com/manage-resources/adjust-resources.md#advanced-container-profiles)
- [Default container profiles](https://docs.upsun.com/manage-resources/adjust-resources.md#default-container-profiles) for runtime and service
  containers
- [Customize resources using the `container_profile` key](https://docs.upsun.com/manage-resources/adjust-resources.md#adjust-a-container-profile)

## Additional hosts

If you're using a private network with specific IP addresses you need to connect to,
you might want to map those addresses to hostnames to better remember and organize them.
In such cases, you can add a map of those IP addresses to whatever hostnames you like.
Then when your app tries to access the hostname, it's sent to the proper IP address.

So in the following example, if your app tries to access `api.example.com`, it's sent to `192.0.2.23`.

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    source:
      root: "/"
    stack: [ "php@8.5" ]
    additional_hosts:
      api.example.com: "192.0.2.23"
      web.example.com: "203.0.113.42"
```

This is equivalent to adding the mapping to the `/etc/hosts` file for the container.


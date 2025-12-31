# Source: https://docs.upsun.com/add-services/influxdb.md

# InfluxDB (Database service)


InfluxDB is a time series database optimized for high-write-volume use cases such as logs, sensor data, and real-time analytics.

It exposes an HTTP API for client interaction. See the [InfluxDB documentation](https://docs.influxdata.com/influxdb) for more information.

## Supported versions

You can select the major and minor version.

Patch versions are applied periodically for bug fixes and the like.
When you deploy your app, you always get the latest available patches.

   - 2.7

   - 2.3

## Deprecated versions

The following versions are still available in your projects,
but they're at their end of life and are no longer receiving security updates from upstream.

   - 2.2

   - 1.8

   - 1.7

   - 1.3

   - 1.2

To ensure your project remains stable in the future,
switch to a [supported version](#supported-versions).
See more information on [how to upgrade to version 2.3 or later](#upgrade-to-version-23-or-later).

## Relationship reference

For each service [defined via a relationship](#usage-example) to your application,
Upsun automatically generates corresponding environment variables within your application container,
in the ``$_`` format.

Here is example information available through the [service environment variables](https://docs.upsun.com/development/variables.md#service-environment-variables) themselves,
or through the [``PLATFORM_RELATIONSHIPS`` environment variable](https://docs.upsun.com/development/variables/use-variables.md#use-provided-variables).

For some advanced use cases, you can use the [PLATFORM_RELATIONSHIPS](https://docs.upsun.com/development/variables/use-variables.md#use-provided-variables).
The structure of the ``PLATFORM_RELATIONSHIPS`` environment variable can be obtained by running ``upsun relationships`` in your terminal:

```json {}
{
  "host": "influxdb.internal",
  "hostname": "azertyuiopqsdfghjklm.influxdb.service._.eu-1.platformsh.site",
  "cluster": "azertyuiopqsdf-main-bvxea6i",
  "service": "influxdb",
  "type": "influxdb:2.7",
  "rel": "influxdb",
  "scheme": "http",
  "username": "admin",
  "password": "ChangeMe",
  "port": 8086,
  "path": null,
  "query": {
    "org": "main",
    "bucket": "main",
    "api_token": "azertyuiopqsdfghjklm1234567890"
  },
  "fragment": null,
  "public": false,
  "host_mapped": false,
  "ip": "123.456.78.90"
}
```

Here is an example of how to gather [PLATFORM_RELATIONSHIPS](https://docs.upsun.com/development/variables/use-variables.md#use-provided-variables) information in a [.environment](https://docs.upsun.com/development/variables/set-variables.md#use-env-files):

    .environment

```bash {}
# Decode the built-in credentials object variable.
export RELATIONSHIPS_JSON="$(echo "$PLATFORM_RELATIONSHIPS" | base64 --decode)"

# Set environment variables for individual credentials.
export APP_INFLUXDB_HOST="$(echo $RELATIONSHIPS_JSON | jq -r '.influxdb[0].host')"
```

## Usage example

### 1. Configure the service

To define the service, use the `influxdb` type:

```yaml  {location=".upsun/config.yaml"}
services:
    # The name of the service container. Must be unique within a project.
    <SERVICE_NAME>:
        type: influxdb:<VERSION>
```

Note that changing the name of the service replaces it with a brand new service and all existing data is lost. Back up your data before changing the service.

### 2. Define the relationship

To define the relationship, use the following configuration:

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  <APP_NAME>:
    # Relationships enable access from this app to a given service.
    # The example below shows simplified configuration leveraging a default service
    # (identified from the relationship name) and a default endpoint.
    # See the Application reference for all options for defining relationships and endpoints.
    relationships:
      <SERVICE_NAME>:
```

You can define ``<SERVICE_NAME>`` as you like, so long as it’s unique between all defined services
and matches in both the application and services configuration.
The example above leverages [default endpoint](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#relationships) configuration for relationships.
That is, it uses default endpoints behind-the-scenes, providing a [relationship](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#relationships)
(the network address a service is accessible from) that is identical to the name of that service.
Depending on your needs, instead of default endpoint configuration,
you can use [explicit endpoint configuration](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#relationships).
With the above definition, the application container now has [access to the service](#use-in-app) via the relationship ``<SERVICE_NAME>`` and its corresponding [service environment variables](https://docs.upsun.com/development/variables.md#service-environment-variables).

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  <APP_NAME>:
    # Relationships enable access from this app to a given service.
    # The example below shows configuration with an explicitly set service name and endpoint.
    # See the Application reference for all options for defining relationships and endpoints.
    relationships:
      <RELATIONSHIP_NAME>:
        service: <SERVICE_NAME>
        endpoint: influxdb
```

You can define ``<SERVICE_NAME>`` and ``<RELATIONSHIP_NAME>`` as you like, so long as it’s unique between all defined services and relationships
and matches in both the application and services configuration.
The example above leverages [explicit endpoint](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#relationships) configuration for relationships.
Depending on your needs, instead of explicit endpoint configuration,
you can use [default endpoint configuration](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#relationships).
With the above definition, the application container now has [access to the service](#use-in-app) via the relationship ``<RELATIONSHIP_NAME>`` and its corresponding [service environment variables](https://docs.upsun.com/development/variables.md#service-environment-variables).

### Example configuration

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # Relationships enable access from this app to a given service.
    # The example below shows simplified configuration leveraging a default service
    # (identified from the relationship name) and a default endpoint.
    # See the Application reference for all options for defining relationships and endpoints.
    relationships:
      influxdb:
services:
  # The name of the service container. Must be unique within a project.
  influxdb:
    type: influxdb:2.7
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # Relationships enable access from this app to a given service.
    # The example below shows configuration with an explicitly set service name and endpoint.
    # See the Application reference for all options for defining relationships and endpoints.
    relationships:
      influxdb:
        service: influxdb
        endpoint: influxdb
services:
  # The name of the service container. Must be unique within a project.
  influxdb:
    type: influxdb:2.7
```

### Use in app

To use the configured service in your app, add a configuration file similar to the following to your project.

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "/"

    [...]

    # Relationships enable access from this app to a given service.
    # The example below shows simplified configuration leveraging a default service
    # (identified from the relationship name) and a default endpoint.
    # See the Application reference for all options for defining relationships and endpoints.
    relationships:
      influxdb:
service:
  influxdb:
    type: influxdb:2.7
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "myapp"

    [...]

    # Relationships enable access from this app to a given service.
    # The example below shows configuration with an explicitly set service name and endpoint.
    # See the Application reference for all options for defining relationships and endpoints.
    relationships:
      influxdb:
        service: influxdb
        endpoint: influxdb
service:
  influxdb:
    type: influxdb:2.7
```

This configuration defines a single application (`myapp`), whose source code exists in the `<PROJECT_ROOT>/myapp` directory. 
`myapp` has access to the `influxdb` service, via a relationship whose name is [identical to the service name](#2-define-the-relationship)
(as per [default endpoint](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#relationships) configuration for relationships).

From this, ``myapp`` can retrieve access credentials to the service through the [relationship environment variables](#relationship-reference).

```bash  {location="myapp/.environment"}
# Set environment variables for common InfluxDB credentials.
# For more information, please visit https://docs.upsun.com/development/variables.html#service-environment-variables.
export INFLUX_USER="${INFLUXDB_USERNAME}"
export INFLUX_HOST="${INFLUXDB_HOST}"
export INFLUX_ORG="$(echo "$INFLUXDB_QUERY" | jq -r '.org')"
export INFLUX_TOKEN="$(echo "$INFLUXDB_QUERY" | jq -r '.api_token')"
export INFLUX_BUCKET="$(echo "$INFLUXDB_QUERY" | jq -r '.bucket')"
```

The above file — ``.environment`` in the ``myapp`` directory — is automatically sourced by Upsun into the runtime environment, so that the variable ``INFLUX_HOST`` can be used within the application to connect to the service.

Note that ``INFLUX_HOST``, and all [Upsun-service environment variables](https://docs.upsun.com/development/variables.md#service-environment-variables) like ``INFLUXDBDATABASE_HOST``,
are environment-dependent.
Unlike the build produced for a given commit,
they can’t be reused across environments and only allow your app to connect to a single service instance on a single environment.

A file very similar to this is generated automatically for your when using the ``upsun ify`` command to [migrate a codebase to Upsun](https://docs.upsun.com/get-started.md).

## Export data

To export your data from InfluxDB, follow these steps:

1. Install and set up the [`influx` CLI](https://docs.influxdata.com/influxdb/cloud/tools/influx-cli/).
2. Connect to your InfluxDB service with the [Upsun CLI](https://docs.upsun.com../administration/cli/_index.md):

   ```bash
   upsun tunnel:single
   ```

   This opens an SSH tunnel to your InfluxDB service on your current environment and produces output like the following:

   ```bash
   SSH tunnel opened to <RELATIONSHIP_NAME> at: http://127.0.0.1:30000
   ```

3. Get the username, password and token from the [relationship](#relationship-reference) by running the following command:

   ```bash
   upsun relationships -P <RELATIONSHIP_NAME>
   ```

4. Adapt and run [InfluxDB's CLI export command](https://docs.influxdata.com/influxdb/v2.3/reference/cli/influx/backup/).

    ```bash
    influx backup --host <URL_FROM_STEP_2> --token <API_TOKEN_FROM_STEP_3>
    ```

## Upgrade to version 2.3 or later

### From a previous 2.x version

From version 2.3 onward, the structure of relationships changes.

If you're using a prior 2.x version, your app might currently rely on pulling the `bucket`, `org`, `api_token`,
or `user` values available in the [`PLATFORM_RELATIONSHIPS` environment variable](#relationship-reference).

If so, to ensure your upgrade is successful, make the following changes to your connection logic:

- Rename the `user` key to `username`.
- Move the `org`, `bucket` and `api_token` keys so they're contained in a dictionary under the `query` key.

If you're relying on any other attributes connecting to InfluxDB, they remain accessible as environment variable from the [service environment variable](#relationship-reference), aside from those addressed above:

### From a 1.x version

From version 2.3 onward, InfluxDB includes an upgrade utility that can convert databases from previous versions to version 2.3 or later.

To upgrade from a 1.x version to 2.3 or later,
change the service version in your `.upsun/config.yaml` file and push your project.
Any existing data you had in your 1.x system is automatically upgraded for you into the 2.3+ system.

**Note**: 

During an upgrade from a 1.x version to a 2.3 version or later,
a new admin password and a new admin API token are automatically generated.
Previous credentials can’t be retained.

You can retrieve your new credentials through the [service environment variables](https://docs.upsun.com/development/variables.md#service-environment-variables).



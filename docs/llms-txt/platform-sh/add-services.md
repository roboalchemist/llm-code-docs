# Source: https://docs.upsun.com/add-services.md

# Add services

Upsun includes many services, so you don't have to subscribe to external cache or search engine services.
Because the services are included in your project, you can manage them through Git
and they're backed up together with the rest of your project.

Your project defines the services configuration from a top-level key called `services`, which is placed in a unified configuration file like `.upsun/config.yaml`.

If you don't need any services (such as for a static website), you don't need to include this configuration. Read on to see how to add services.

## Add a service

Adding a service is a two-step process.

### 1. Configure the service

All service configuration happens in the `.upsun/config.yaml` file in your Git repository.

Configure your service in the following pattern:

```yaml  {location=".upsun/config.yaml"}
# The name of the service container. Must be unique within a project.
services:
  <SERVICE_NAME>:
    type: <SERVICE_TYPE>:<VERSION>
    # Other options...
```

An example service configuration for two databases might look like this:

```yaml  {location=".upsun/config.yaml"}
services:
  # The name of the service container. Must be unique within a project.
  mariadb:
    type: mariadb:11.8
  # The name of the service container. Must be unique within a project.
  postgresql:
    type: postgresql:18
```

This YAML file contains a dictionary defining all of the services you want to use.
The top-level key `services` defines an object of all of the services to be provisioned for the project.
Below that, come custom service names (<SERVICE_NAME>; in the example, `mariadb` and `postgresql`), which you use to identify the service in step 2.

You can give it any name you want with lowercase alphanumeric characters, hyphens, and underscores.

**Note**: 

Changing the service name is interpreted as creating an entirely new service.
This **removes all data in that service**.
Always back up your data before changing existing services in your ``.upsun/config.yaml`` file.

#### Service options

The following table presents the keys you can define for each service:

| Name            | Type       | Required          | Description |
| --------------- | ---------- | ----------------- | ----------- |
| `type`          | `string`   | Yes               | One of the [available services](#available-services) in the format `type:version`. |
| `configuration` | dictionary | For some services | Some services have additional specific configuration options that can be defined here, such as specific endpoints. See the given service page for more details. |
| `relationships` | dictionary | For some services | Some services require a relationship to your app. The content of the dictionary has the same type as the `relationships` dictionary for [app configuration](https://docs.upsun.com/create-apps/image-properties/relationships.md). The `endpoint_name` for apps is always `http`. |

##### Resources (CPU, RAM, disk)

Upsun allows you to configure resources (CPU, RAM, and disk) per environment for each of your services.
For more information, see how to [manage resources](https://docs.upsun.com/manage-resources.md).

You configure the disk size in [MB](https://docs.upsun.com/glossary.md#mb).
Your actual available disk space is slightly smaller with some space used for formatting and the filesystem journal.
When checking available space, note whether it's reported in MB or MiB.

You can decrease the size of an existing disk for a service.
If you do so, be aware that:

- You need to [create new backups](https://docs.upsun.com/environments/backup.md) that the downsized disk can accommodate.
  Backups from before the downsize cannot be restored unless you increase the disk size again.
- The downsize fails if there's more data on the disk than the desired size.

### 2. Define the relationship

To define the relationship, use the following configuration:

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  <APP_NAME>:
    # Other options...

    # Relationships enable an app container's access to a service.
    # The example below shows simplified configuration leveraging a default service (identified from the relationship name) and a default endpoint.
    # See the Application reference for all options for defining relationships and endpoints.
    relationships:
      <SERVICE_NAME>:
```

You can define ``<SERVICE_NAME>`` as you like, so long as it’s unique between all defined services
and matches in both the application and services configuration.
The example above leverages [default endpoint](https://docs.upsun.com/create-apps/image-properties/relationships.md) configuration for relationships.
That is, it uses default endpoints behind the scenes, providing a [relationship](https://docs.upsun.com/create-apps/image-properties/relationships.md)
(the network address a service is accessible from) that is identical to the name of that service.
Depending on your needs, instead of default endpoint configuration,
you can use [explicit endpoint configuration](https://docs.upsun.com/create-apps/image-properties/relationships.md).

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  <APP_NAME>:
    # Other options...

    # Relationships enable an app container's access to a service.
    # The example below shows configuration with an explicitly set service name and endpoint.
    # See the Application reference for all options for defining relationships and endpoints.
    relationships:
      <RELATIONSHIP_NAME>:
        service: <SERVICE_NAME>
        endpoint: <ENDPOINT_NAME>
```

 - ``<RELATIONSHIP_NAME>`` is the name you want to give to the relationship.
 - ``<SERVICE_NAME>`` is the name of the service as defined in the ``services`` section.
 - ``<ENDPOINT_NAME>`` is the endpoint your app will use to connect to the service (refer to the service reference to know which value to use).

An example relationship to connect to the databases given in the [example in step 1](#1-configure-the-service):

```yaml {}
applications:
  # Relationships enable access from this app to a given service.
  # The example below shows simplified configuration leveraging a default service
  # (identified from the relationship name) and a default endpoint.
  # See the Application reference for all options for defining relationships and endpoints.
  <APP_NAME>:
    relationships:
      mariadb:
      postgresql:
services:
  mariadb:
    type: mariadb:11.8
  postgresql:
    type: postgresql:18
```

    .upsun/config.yaml

```yaml {}
applications:
  # Relationships enable access from this app to a given service.
  # The example below shows configuration with explicitly set service names and endpoints.
  # See the Application reference for all options for defining relationships and endpoints.

  <APP_NAME>:
    relationships:
      database:
        service: mariadb
        endpoint: mysql
      postgresql:
        service: postgresql
        endpoint: postgresql
services:
  mariadb:
    type: mariadb:11.8
  postgresql:
    type: postgresql:18
```

As with the service name, you can give the relationship any name you want
with lowercase alphanumeric characters, hyphens, and underscores.
It helps if the service name and relationship name are different, but it isn’t required.

Each service offers one or more endpoints for connections, depending on the service.
An endpoint is a named set of credentials to give access to other apps and services in your project.
If you don't specify one in the [service configuration](#service-options), a default endpoint is created.
The default endpoint varies by service, generally being its type (such as `mysql` or `solr`).

## Available services

The following table presents the available service types and their versions.
Add them to the `type` key of the [service configuration](#1-configure-the-service) in the format `type:version`.

| Service | `type` | Supported versions |
| ------- | ------ | ------------------ |
| [Headless Chrome](https://docs.upsun.com/add-services/headless-chrome.md) | `chrome-headless` | 120 |
| [ClickHouse](https://docs.upsun.com/add-services/clickhouse.md) | `clickhouse` | 25.8, 25.3, 24.3, 23.8 |
| [Elasticsearch](https://docs.upsun.com/add-services/elasticsearch.md) | `elasticsearch` | 7.10 |
| [Elasticsearch-Enterprise](https://docs.upsun.com/add-services/elasticsearch.md) Premium | `elasticsearch-enterprise` | 7.17, 8.5, 8.19 |
| [Gotenberg](https://docs.upsun.com/add-services/gotenberg.md) | `gotenberg` | 8 |
| [InfluxDB](https://docs.upsun.com/add-services/influxdb.md) | `influxdb` | 2.7, 2.3 |
| [Kafka](https://docs.upsun.com/add-services/kafka.md) | `kafka` | 3.7 |
| [MariaDB/MySQL](https://docs.upsun.com/add-services/mysql.md) | `mariadb` | 11.8, 11.4, 10.11, 10.6 |
| [Memcached](https://docs.upsun.com/add-services/memcached.md) | `memcached` | 1.6 |
| [Mercure](https://docs.upsun.com/add-services/mercure.md) | `mercure` | 0 |
| [MongoDB](https://docs.upsun.com/add-services/mongodb.md) | `mongodb` | 4.0 |
| [MongoDB](https://docs.upsun.com/add-services/mongodb.md) Premium | `mongodb-enterprise` | 7.0 |
| [MariaDB/MySQL](https://docs.upsun.com/add-services/mysql.md) | `mysql` | 11.8, 11.4, 10.11, 10.6 |
| [Network Storage](https://docs.upsun.com/add-services/network-storage.md) | `network-storage` | 1.0 |
| [OpenSearch](https://docs.upsun.com/add-services/opensearch.md) | `opensearch` | 3, 2 |
| [Oracle MySQL](https://docs.upsun.com/add-services/mysql.md) | `oracle-mysql` | 8.4, 8.0 |
| [PostgreSQL](https://docs.upsun.com/add-services/postgresql.md) | `postgresql` | 18, 17, 16, 15, 14 |
| [RabbitMQ](https://docs.upsun.com/add-services/rabbitmq.md) | `rabbitmq` | 4.1 |
| [Redis](https://docs.upsun.com/add-services/redis.md) | `redis` | 8.0, 7.2 |
| [Solr](https://docs.upsun.com/add-services/solr.md) | `solr` | 9.9, 9.6, 9.4, 9.2, 9.1 |
| [Valkey](https://docs.upsun.com/add-services/valkey.md) | `valkey` | 8.1, 8.0 |
| [Varnish](https://docs.upsun.com/add-services/varnish.md) | `varnish` | 7.6, 6.0 |
| [Vault KMS](https://docs.upsun.com/add-services/vault.md) | `vault-kms` | 1.12 |

### Service versions

These services generally follow [semantic versioning conventions](https://semver.org/).
You can select the major version, but the latest compatible minor is applied automatically and can’t be overridden.
Patch versions are applied periodically for bug fixes and the like.
When you deploy your app, you always get the latest available patches.

## Service timezones

All services have their system timezone set to UTC by default.
For some services, you can change the timezone for the running service
(this doesn't affect the container itself and so logs are still in UTC).

* [MySQL](https://docs.upsun.com/add-services/mysql.md#service-timezone)
* [PostgreSQL](https://docs.upsun.com/add-services/postgresql.md#service-timezone)

## Connect to a service

For security reasons, you can't access services directly through HTTP.
You can connect through your app or by opening an SSH tunnel to access the service directly.

Connecting to a service using an SSH tunnel is a two-step process.

### 1. Obtain service credentials

To get the credentials for a given service, run the following command:

```bash {}
upsun relationships
```

You get output like the following:

```yaml {}
mariadb:
  -
    username: user
    scheme: mysql
    service: mariadb
    fragment: null
    ip: 198.51.100.37
    hostname: abcdefghijklm1234567890123.mariadb.service._.eu.platformsh.site
    public: false
    cluster: abcdefgh1234567-main-abcd123
    host: mariadb.internal
    rel: mysql
    query:
        is_master: true
    path: main
    password: ''
    type: 'mariadb:11.8'
    port: 3306
    host_mapped: false
    url: 'mysql://user:@mariadb.internal:3306/main'
```

With this example, you can connect to the ``mariadb`` relationship
with the user ``user``, an empty password, and the database name ``main`` (from the ``path``).
The ``url`` property shows a full database connection that can be used from your app.
You can obtain the complete list of available service environment variables in your app container by running ``upsun ssh env``.
Note that the information about the relationship can change when an app is redeployed or restarted or the relationship is changed. So your apps should only rely on the [service environment variables](https://docs.upsun.com/development/variables.md#service-environment-variables) directly rather than hard coding any values.

### 2. Open an SSH tunnel

Open a single [SSH tunnel](https://docs.upsun.com/development/ssh.md#connect-to-services) by running the following CLI command:

```bash {}
upsun tunnel:single --relationship <RELATIONSHIP_NAME>
```

By default, this opens a tunnel at ``127.0.0.1:30000``.
You can specify the port for the connection using the ``--port`` flag.
You can then connect to this service in a separate terminal or locally running app.
With the example above, you connect to a URL like the following:
``mysql://user:@127.0.0.1:30000/main``

## Upgrading services

Upsun provides a large number of [managed service versions](#available-services).
As new versions are made available, you will inevitably upgrade infrastructure to a more recent (or latest version).

When you do so, we would recommend:

1. **Use preview environments**. Leverage preview (non-production environments) to perform the upgrade, then merge the upgrade into production (promotion). This will give you an opportunity to test inherited production data in a safe, isolated environment first.
1. **Upgrade progressively**. For one reason or another, you may be more than a single version behind the upgrade you are trying to perform. To avoid data loss issues caused by large differences in versions, [upgrade one version at a time](https://www.rabbitmq.com/upgrade.md#rabbitmq-version-upgradability).


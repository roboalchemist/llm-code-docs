# Source: https://docs.upsun.com/create-apps/multi-app/relationships.md

# Source: https://docs.upsun.com/create-apps/image-properties/relationships.md

# relationships


A dictionary of relationships that defines the connections to other services and apps.

Optional in [single-runtime](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#primary-application-properties) and [composable](https://docs.upsun.com/create-apps/app-reference/composable-image.md#primary-application-properties) images.

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
(``Relationship 'SERVICE_NAME' of application 'app' ... targets a service without a valid default endpoint configuration.``).
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
    type: elasticsearch:7.10
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



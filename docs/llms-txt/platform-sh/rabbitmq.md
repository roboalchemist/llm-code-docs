# Source: https://docs.upsun.com/add-services/rabbitmq.md

# Source: https://docs.upsun.com/guides/spring/rabbitmq.md

# Source: https://docs.upsun.com/add-services/rabbitmq.md

# Source: https://docs.upsun.com/guides/spring/rabbitmq.md

# Source: https://docs.upsun.com/add-services/rabbitmq.md

# RabbitMQ (message queue service)

[RabbitMQ](https://www.rabbitmq.com/documentation.md) is a message broker
that supports multiple messaging protocols, such as the Advanced Message Queuing Protocol (AMQP).
It gives your apps a common platform to send and receive messages
and your messages a safe place to live until they're received.

## Supported versions

You can select the major and minor version.

Patch versions are applied periodically for bug fixes and the like.
When you deploy your app, you always get the latest available patches.

   - 4.1

   - 4.0

   - 3.13

   - 3.12

### Deprecated versions

The following versions are [deprecated](https://docs.upsun.com/glossary.md#deprecated-versions).
They're available, but they don't receive security updates from upstream and aren't guaranteed to work.
They'll be removed in the future – consider migrating to a [supported version](#supported-versions).

   - 3.11

   - 3.10

   - 3.9

   - 3.8

   - 3.7

   - 3.6

   - 3.5

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
  "username": "guest",
  "scheme": "amqp",
  "service": "rabbitmq",
  "fragment": null,
  "ip": "123.456.78.90",
  "hostname": "azertyuiopqsdfghjklm.rabbitmq.service._.eu-1.platformsh.site",
  "port": 5672,
  "cluster": "azertyuiopqsdf-main-afdwftq",
  "host": "rabbitmq.internal",
  "rel": "rabbitmq",
  "path": null,
  "query": [],
  "password": "ChangeMe",
  "type": "rabbitmq:4.1",
  "public": false,
  "host_mapped": false
}
```

Here is an example of how to gather [PLATFORM_RELATIONSHIPS](https://docs.upsun.com/development/variables/use-variables.md#use-provided-variables) information in a [.environment](https://docs.upsun.com/development/variables/set-variables.md#use-env-files):

    .environment

```bash {}
# Decode the built-in credentials object variable.
export RELATIONSHIPS_JSON="$(echo "$PLATFORM_RELATIONSHIPS" | base64 --decode)"

# Set environment variables for individual credentials.
export APP_RABBITMQ_HOST="$(echo "$RELATIONSHIPS_JSON" | jq -r '.rabbitmq[0].host')"
```

## Usage example

### 1. Configure the service

To define the service, use the ``rabbitmq`` type:

```yaml  {location=".upsun/config.yaml"}
services:
  # The name of the service container. Must be unique within a project.
  <SERVICE_NAME>:
    type: rabbitmq:<VERSION>
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
With the above definition, the application container (``<APP_NAME>``) now has access to the service via the relationship ``<SERVICE_NAME>`` and its corresponding [service environment variables](https://docs.upsun.com/development/variables.md#service-environment-variables).

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
        endpoint: rabbitmq
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
      rabbitmq:
services:
  # The name of the service container. Must be unique within a project.
  rabbitmq:
    type: rabbitmq:4.1
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
      rabbitmq:
        service: rabbitmq
        endpoint: rabbitmq
services:
  # The name of the service container. Must be unique within a project.
  rabbitmq:
    type: rabbitmq:4.1
```

### Use in app

To use the configured service in your app, add a configuration file similar to the following to your project.

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "myapp"

    [...]

    # Relationships enable access from this app to a given service.
    # The example below shows simplified configuration leveraging a default service
    # (identified from the relationship name) and a default endpoint.
    # See the Application reference for all options for defining relationships and endpoints.
    relationships:
      rabbitmq:
services:
  # The name of the service container. Must be unique within a project.
  rabbitmq:
    type: rabbitmq:4.1
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
      rabbitmq:
        service: rabbitmq
        endpoint: rabbitmq
services:
  # The name of the service container. Must be unique within a project.
  rabbitmq:
    type: rabbitmq:4.1
```

This configuration defines a single application (`myapp`), whose source code exists in the `<PROJECT_ROOT>/myapp` directory. 
`myapp` has access to the `rabbitmq` service, via a relationship whose name is [identical to the service name](#2-define-the-relationship)
(as per [default endpoint](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#relationships) configuration for relationships).

From this, ``myapp`` can retrieve access credentials to the service through the [relationship environment variables](#relationship-reference).

```bash  {location="myapp/.environment"}
# Set environment variables for individual credentials.
# For more information, please visit https://docs.upsun.com/development/variables.html#service-environment-variables.
export QUEUE_SCHEME="${RABBITMQ_SCHEME}"
export QUEUE_USERNAME="${RABBITMQ_USERNAME}"
export QUEUE_PASSWORD="${RABBITMQ_PASSWORD}"
export QUEUE_HOST="${RABBITMQ_HOST}"
export QUEUE_PORT="${RABBITMQ_PORT}"

# Set a single RabbitMQ connection string variable for AMQP.
export AMQP_URL="${QUEUE_SCHEME}://${QUEUE_USERNAME}:${QUEUE_PASSWORD}@${QUEUE_HOST}:${QUEUE_PORT}/"
```

The above file — ``.environment`` in the ``myapp`` directory — is automatically sourced by Upsun into the runtime environment, so that the variable ``AMQP_URL`` can be used within the application to connect to the service.

Note that ``AMQP_URL``, and all Upsun [service environment variables](https://docs.upsun.com/development/variables.md#service-environment-variables) like ``RABBITMQ_HOST``, are environment-dependent.
Unlike the build produced for a given commit,
they can’t be reused across environments and only allow your app to connect to a single service instance on a single environment.

A file very similar to this is generated automatically for your when using the ``upsun ify`` command to [migrate a codebase to Upsun](https://docs.upsun.com/get-started.md).

## Connect to RabbitMQ

When debugging, you may want to connect directly to your RabbitMQ service.
You can connect in multiple ways:

- An [SSH tunnel](#via-ssh)
- A [web interface](#access-the-management-ui)

In each case, you need the login credentials that you can obtain from the [relationship](#relationship-reference).

### Via SSH

To connect directly to your RabbitMQ service in an environment,
open an SSH tunnel with the [Upsun CLI](https://docs.upsun.com../administration/cli.md).

To open an SSH tunnel to your service with port forwarding,
run the following command:

```bash
upsun tunnel:single --gateway-ports
```

Then configure a RabbitMQ client to connect to this tunnel using the credentials from the [relationship](#relationship-reference).
See a [list of RabbitMQ client libraries](https://www.rabbitmq.com/devtools.md).

### Access the management UI

RabbitMQ offers a [management plugin with a browser-based UI](https://www.rabbitmq.com/management.md).
You can access this UI with an SSH tunnel.

To open a tunnel, follow these steps.

1.  SSH into your app container with a flag for local port forwarding:
2.
    ```bash
    ssh $(upsun ssh --pipe) -L 15672:<RELATIONSHIP_NAME>.internal:15672
    ```

    <RELATIONSHIP_NAME> is the [name you defined](#2-define-the-relationship).

2.  Open `http://localhost:15672` in your browser.
    Log in using the username and password from the [relationship](#relationship-reference).

## Configuration options

You can configure your RabbitMQ service in the [services configuration](#1-configure-the-service) with the following options:

| Name     | Type              | Required | Description                                          |
|----------|-------------------|----------|------------------------------------------------------|
| `vhosts` | List of `string`s | No       | Virtual hosts used for logically grouping resources. |

You can configure additional [virtual hosts](https://www.rabbitmq.com/vhosts.md),
which can be useful for separating resources, such as exchanges, queues, and bindings, into their own namespaces.
To create virtual hosts, add them to your configuration as in the following example:

```yaml  {location=".upsun/config.yaml"}
services:
  # The name of the service container. Must be unique within a project.
  rabbitmq:
    type: "rabbitmq:4.1"
    configuration:
      vhosts:
        - host1
        - host2
```

## Upgrading

When upgrading RabbitMQ, skipping major versions (e.g. 3.7 -> 3.11) [is not supported](https://www.rabbitmq.com/upgrade.md#rabbitmq-version-upgradability).
Make sure you upgrade sequentially (3.7 -> 3.8 -> 3.9 -> 3.10 -> 3.11) and that each upgrade commit translates into an actual deployment.


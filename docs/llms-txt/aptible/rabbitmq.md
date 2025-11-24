# Source: https://www.aptible.com/docs/core-concepts/managed-databases/supported-databases/rabbitmq.md

# RabbitMQ

# Available Versions

The following versions of RabbitMQ are currently available:

| Version |   Status   | End-Of-Life Date | Deprecation Date |
| :-----: | :--------: | :--------------: | :--------------: |
|   3.13  | Deprecated |     July 2025    |   October 2025   |
|   4.0   | Deprecated |     Nov 2025     |   February 2026  |
|   4.1   |  Available |        N/A       |        N/A       |
|   4.2   |  Available |        N/A       |        N/A       |

For databases on EOL versions, Aptible will prevent new databases from being provisioned and mark existing database as `DEPRECATED` on the deprecation date listed above. While existing databases will not be affected, we recommend end-of-life databases to be [upgraded](https://www.aptible.com/docs/core-concepts/managed-databases/managing-databases/database-upgrade-methods#database-upgrades). The latest version offered on Aptible will always be available for provisioning, regardless of end-of-life date.

# Connecting to RabbitMQ

Aptible RabbitMQ [Databases](/core-concepts/managed-databases/overview) require authentication and SSL to connect.

<Tip>RabbitMQ Databases use a valid certificate for their host, so you’re encouraged to verify the certificate when connecting.</Tip>

# Connecting to the RabbitMQ Management Interface

Aptible RabbitMQ [Databases](/core-concepts/managed-databases/overview) provide access to the management interface.

Typically, you should access the management interface via a [Database Tunnel](/core-concepts/managed-databases/connecting-databases/database-tunnels). For example:

```shell  theme={null}
aptible db:tunnel "$DB_HANDLE" --type management
```

# Connecting to RabbitMQ Prometheus

You can create a Database Tunnel to connect to the Prometheus endpoint locally, or use [Prometheus with Grafana](https://www.rabbitmq.com/docs/prometheus) as a monitoring solution.

```shell  theme={null}
aptible db:tunnel "$DB_HANDLE" --type prometheus
```

Note that the Prometheus plugin on Aptible is configured with HTTP Authentication, so you will need to provide the username and password to reach the endpoint.

# Modifying RabbitMQ Parameters & Policies

RabbitMQ [parameters](https://www.rabbitmq.com/parameters.html) can be updated via the management API and changes will persist across Database restarts.

The [log level](https://www.rabbitmq.com/logging.html#log-levels) of a RabbitMQ Database can be changed by contacting [Aptible Support](/how-to-guides/troubleshooting/aptible-support), but other [configuration file](https://www.rabbitmq.com/configure.html#configuration-files) values cannot be changed at this time.

# Connection Security

Aptible RabbitMQ Databases support connections via the following protocols:

* For RabbitMQ version 3.13, 4.0: `TLSv1.2`, `TLSv1.3`

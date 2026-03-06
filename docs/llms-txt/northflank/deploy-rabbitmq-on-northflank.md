# Source: https://northflank.com/docs/v1/application/databases-and-persistence/deploy-databases-on-northflank/deploy-rabbitmq-on-northflank.md

# Deploy RabbitMQ on Northflank

This guide explains how to quickly and easily deploy and use [RabbitMQ](https://www.rabbitmq.com/) on Northflank.

| Available versions | Description | Backups | TLS |
| --- | --- | --- | --- |
| 4.2.4, 4.0.9, 3.13.7, 3.12.14 | RabbitMQ is an open source message broker software that implements the Advanced Message Queuing Protocol (AMQP). | Disk | Yes |

## Deploy RabbitMQ

1. [Click here to create an addon](https://app.northflank.com/s/project/create/addon), or choose addon from the create new menu in the top right corner of the dashboard

2. Select RabbitMQ and enter a name

3. Choose a version or leave as default (most recent version)

4. Choose whether to [deploy with TLS](https://northflank.com/docs/v1/application/databases-and-persistence/connect-database-secrets-to-workloads#enable-tls). This can be changed later.

5. Choose whether to make RabbitMQ publicly accessible. This will give your addon a URL and make it available online. TLS must be enabled to select this.

6. If you have [secret groups](https://northflank.com/docs/v1/application/secure/manage-secret-groups) in your project, choose ones to [link to the addon](https://northflank.com/docs/v1/application/databases-and-persistence/connect-database-secrets-to-workloads#link-database-secrets-to-a-secret-group) so that RabbitMQ can be used in services and jobs that inherit variables from the secret group. To link RabbitMQ to a secret group:
  
  
  
  - Show secret groups and configure the secret groups you wish to use
  
  - Select suggested secrets from RabbitMQ to link, or select all
  
  - Set any required aliases for specific secrets to make them accessible by that name within your application

7. Select the required [resources](https://northflank.com/docs/v1/application/databases-and-persistence/scale-a-database) for your RabbitMQ deployment. You can scale RabbitMQ after creation, but available storage and replicas cannot be decreased once increased.

8. Create addon and RabbitMQ will begin provisioning, this may take a few minutes.

## Advanced options

RabbitMQ has the following advanced options available when creating your addon.

### Custom virtual host name

You can set a custom name for the default [virtual host](https://www.rabbitmq.com/docs/vhosts) to be created within your addon, otherwise it will be given a random name. The virtual host name will be used in the connection details for your RabbitMQ addon.

### Deploy with zonal redundancy

Your addon will be deployed to your [project's region](https://northflank.com/docs/v1/application/run/deploy-to-a-region). Each region may have multiple availability zones, which are data centers with independent infrastructure such as networking, power supply and cooling within the region. Some regions, however, do not have more than one availability zone.

Normally your addon replicas will be provisioned in the same availability zone, but you can enable zonal redundancy to provision replicas across multiple availability zones.

This will ensure that your addon remains available in the event that one zone fails, however networking between replicas in different zones will be slightly slower compared to replicas provisioned in the same availability zone. Replicas will be bound to the zone they are deployed in.

### Backup schedules

You can [add backup schedules](https://northflank.com/docs/v1/application/databases-and-persistence/backup-restore-and-import-data#schedule-backups) when creating your addon. Backups of the addon will be taken according to the schedules.

## Connect to RabbitMQ

You can manually copy the connection secrets for RabbitMQ from the connection details page into runtime variables or build arguments of your workloads on Northflank.

However, it is much easier to link your storage's connection details to a new or existing [secret group](https://northflank.com/docs/v1/application/databases-and-persistence/connect-database-secrets-to-workloads#link-database-secrets-to-a-secret-group).

The necessary secrets to connect your workload will vary depending on your application and the protocols you are using.

To access the [RabbitMQ management dashboard](https://www.rabbitmq.com/management.html) you can use the `MANAGEMENT_ENDPOINT` with the the `USERNAME` and `PASSWORD` secrets as credentials, which gives access to a [management user](https://www.rabbitmq.com/management.html#permissions). Using `ADMIN_USERNAME` and `ADMIN_PASSWORD` to log in to the management dashboard will allow access to [administrator account](https://www.rabbitmq.com/management.html#permissions).

You can access RabbitMQ using the [AMQP connection string](https://www.rabbitmq.com/uri-spec.html) and AMQP port.

### Available ports

| Port | TLS Port | Protocol | URI prefixes |
| --- | --- | --- | --- |
| 5672 | 5671 | AMQP | `ampq[s]://` |
| 1883 | 8883 | MQTT | `mqtt[s]://` |
| 15672 | 15671 | HTTP | `http[s]://` |

STOMP and Streams are disabled by default, contact [[support@northflank.com](mailto:support@northflank.com)](mailto:support@northflank.com) to request that they are enabled.

### Automatically inherit RabbitMQ connection details into your workload

1. Create a new [secret group](https://northflank.com/docs/v1/application/secure/manage-secret-groups) of runtime variables to connect in the running workload

2. Show addons and configure your addon with either the `AMQP_CONNECTION_STRING` and `AMQP_PORT`, or other connection details and secrets as required

3. Set the aliases required in your workload to access the secrets

4. Enable apply secrets to specific services/jobs and select the workloads you want to access the database

5. Create secret group

6. Go to one of the workloads that inherits from the group and check the environment page, you should see the inherited variables from the secret group

The connection string or secrets will now be available in your workload under the configured aliases, and your application will be able to connect to RabbitMQ using them.

## Access RabbitMQ

### Secure local access

To forward RabbitMQ for local access using the [Northflank CLI](https://northflank.com/docs/v1/api/use-the-cli), copy and execute the forward addon command from the local access section of the overview. You can then access the addon using the `AMQP` and `MQTT` connection strings.

### External access

To access your RabbitMQ deployment externally, ensure deploy with TLS and publicly accessible are enabled on the settings page under networking. The connection strings, endpoints, and ports will be updated with the new configuration if TLS was previously disabled (otherwise they will remain the same, but publicly exposed).

### Administration

You can use the `RABBITMQ_ADMIN_CMD` from the connection details page to access your RabbitMQ deployment using the [command-line client](https://www.rabbitmq.com/management-cli.html).

Alternatively you can access the web interface via the `MANAGEMENT_ENDPOINT` link, logging in with the administrator credentials `ADMIN_USERNAME` and `ADMIN_PASSWORD`.

You can also access the addon using the `AMQP` and `MQTT` admin connection strings.

## RabbitMQ specifications

### Connection limits

The number of maximum connections for a virtual host or user can be configured under limits. Log in to the RabbitMQ management endpoint using the admin credentials, open the admin page and select limits to set and update limits.

Your addon will be able to handle more concurrent connections by increasing the available memory. You can do this by selecting the compute plan on the [addon's resources page](https://northflank.com/docs/v1/application/databases-and-persistence/scale-a-database).

## Next steps

- [Configure RabbitMQ for high availability: Use quorum queues or streams for high availability RabbitMQ on Northflank.](/v1/application/databases-and-persistence/configure-addons-for-high-availability#rabbitmq)
- [Use the Northflank CLI: Learn how to create and manage projects on Northflank using the command line client.](/v1/api/use-the-cli)
- [Scale a database: Increase the storage size, number of replicas, and the available CPU and memory to improve availability and performance.](/v1/application/databases-and-persistence/scale-a-database)

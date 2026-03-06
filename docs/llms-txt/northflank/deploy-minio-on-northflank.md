# Source: https://northflank.com/docs/v1/application/databases-and-persistence/deploy-databases-on-northflank/deploy-minio-on-northflank.md

# Deploy MinIO® on Northflank

This guide explains how to quickly and easily deploy and use [MinIO®*](https://min.io/) on Northflank.

| Available versions | Description | Backups | TLS |
| --- | --- | --- | --- |
| 2025.10.15 | MinIO® is a High Performance Object Storage with an Amazon S3 cloud storage service compatible API. | Disk | Yes |

> [!note] 
> On some UNIX systems, the MinIO client `mc` may also be aliased to `mcli`.

## Deploy MinIO

1. [Click here to create an addon](https://app.northflank.com/s/project/create/addon), or choose addon from the create new menu in the top right corner of the dashboard

2. Select MinIO and enter a name

3. Choose a version or leave as default (most recent version)

4. Choose whether to [deploy with TLS](https://northflank.com/docs/v1/application/databases-and-persistence/connect-database-secrets-to-workloads#enable-tls). This can be changed later.

5. Choose whether to make MinIO publicly accessible. This will give your addon a URL and make it available online. TLS must be enabled to select this.

6. If you have [secret groups](https://northflank.com/docs/v1/application/secure/manage-secret-groups) in your project, choose ones to [link to the addon](https://northflank.com/docs/v1/application/databases-and-persistence/connect-database-secrets-to-workloads#link-database-secrets-to-a-secret-group) so that MinIO can be used in services and jobs that inherit variables from the secret group. To link MinIO to a secret group:
  
  
  
  - Show secret groups and configure the secret groups you wish to use
  
  - Select suggested secrets from MinIO to link, or select all
  
  - Set any required aliases for specific secrets to make them accessible by that name within your application

7. Select the required [resources](https://northflank.com/docs/v1/application/databases-and-persistence/scale-a-database) for your MinIO deployment. You can scale MinIO after creation, but available storage and replicas cannot be decreased once increased.

8. 

9. Create addon and MinIO will begin provisioning, this may take a few minutes.

## Advanced options

MinIO has the following advanced options available when creating your addon.

### Deploy with zonal redundancy

Your addon will be deployed to your [project's region](https://northflank.com/docs/v1/application/run/deploy-to-a-region). Each region may have multiple availability zones, which are data centers with independent infrastructure such as networking, power supply and cooling within the region. Some regions, however, do not have more than one availability zone.

Normally your addon replicas will be provisioned in the same availability zone, but you can enable zonal redundancy to provision replicas across multiple availability zones.

This will ensure that your addon remains available in the event that one zone fails, however networking between replicas in different zones will be slightly slower compared to replicas provisioned in the same availability zone. Replicas will be bound to the zone they are deployed in.

### Backup schedules

You can [add backup schedules](https://northflank.com/docs/v1/application/databases-and-persistence/backup-restore-and-import-data#schedule-backups) when creating your addon. Backups of the addon will be taken according to the schedules.

## Connect to MinIO

You can manually copy the connection secrets for MinIO from the connection details page into runtime variables or build arguments of your workloads on Northflank.

However, it is much easier to link your storage's connection details to a new or existing [secret group](https://northflank.com/docs/v1/application/databases-and-persistence/connect-database-secrets-to-workloads#link-database-secrets-to-a-secret-group).

The necessary secrets to connect your workload will vary depending on the application in your workload.

You can connect to your MinIO storage using the endpoint URL which takes the format `[http|https]://[host][:port]`, or `MINIO_CONNECT_COMMAND` for command-line clients. On some UNIX systems, the MinIO client `mc` may also be aliased to `mcli`.

You can supply connections details and secrets such as `host`, `port`, and `accessKey` to your workload if your application requires them.

### Available ports

| Internal port | External port | Protocol | URL prefix |
| --- | --- | --- | --- |
| 9000 | 443 | HTTP | `http[s]://` |

### Automatically inherit MinIO connection details into your workload

1. Create a new [secret group](https://northflank.com/docs/v1/application/secure/manage-secret-groups) of runtime variables to connect in the running workload

2. Show addons and configure your addon with either the `MINIO_ENDPOINT` or select connection details and secrets

3. Set the aliases required in your workload to access the secrets

4. Enable apply secrets to specific services/jobs and select the workloads you want to access the database

5. Create secret group

6. Go to one of the workloads that inherits from the group and check the environment page, you should see the inherited variables from the secret group

The connection string or secrets will now be available in your workload under the configured aliases, and your application will be able to connect to MinIO using them.

## Access MinIO

You can access MinIO using the [MinIO client](https://min.io/docs/minio/linux/reference/minio-mc.html) (`mc`, may be aliased to `mcli` on some systems), or open the MinIO console in a browser.

### Secure local access

To forward your MinIO addon for local access using the [Northflank CLI](https://northflank.com/docs/v1/api/use-the-cli), copy and execute the forward addon command from the local access section of the overview.

You can then use the `MINIO_CONNECT_COMMAND` from the connection details page to access your MinIO deployment using the command-line client or the `MINIO_ENDPOINT` to access in a browser, using the `ACCESS_KEY` and `SECRET_KEY` to authenticate.

### External access

To access your MinIO storage externally, ensure deploy with TLS and publicly accessible are enabled on the settings page under networking. The connection details will be updated to include an external endpoint, external ports, and an external connect command.

## MinIO specifications

### Maximum requests

By default, a MinIO addon will calculate the maximum number of API requests to accept based on the available memory. You can increase the available memory by selecting the compute plan on the [addon's resources page](https://northflank.com/docs/v1/application/databases-and-persistence/scale-a-database).

You can also manually set the maximum number of API requests to handle using the MinIO client:

```
mc admin config set myminio/ api requests_max=1600
mc admin service restart myminio/
```

Setting `requests_max` to `0` will set the limit to the default, calculated on the memory available to the addon.

### Requests deadline

Setting the requests deadline allows long waiting requests to time out when MinIO is unable to process the request. The default value, if `requests_max` is set, is `10 seconds`.

```
mc admin config set myminio/ api requests_max=1600 requests_deadline=2m
mc admin service restart myminio/
```

## Next steps

- [Configure MinIO® for high availability: Deploy multiple MinIO replicas for high availability MinIO on Northflank.](/v1/application/databases-and-persistence/configure-addons-for-high-availability#minio)
- [Use the Northflank CLI: Learn how to create and manage projects on Northflank using the command line client.](/v1/api/use-the-cli)
- [Scale a database: Increase the storage size, number of replicas, and the available CPU and memory to improve availability and performance.](/v1/application/databases-and-persistence/scale-a-database)

* MinIO is a registered trademark of the MinIO Corporation.

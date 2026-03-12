# Source: https://docs.gitguardian.com/self-hosting/installation/databases/database-config.md

# Configure your database

> Overview of database configuration options for GitGuardian self-hosted, including PostgreSQL and Redis setup for different cloud providers.

This guide will help you configure your database. Parameters here should not be
changed after installation unless you know what you are doing, as it may result
in data losses.

:::caution
If you are using external databases, remember to open ports between the GitGuardian
application cluster and your databases.
:::

## PostgreSQL

You can use the provided database with the embedded cluster installation or bring your own for both embedded and external cluster installations. We encourage you to use an external database.

### Embedded versus external

The embedded PostgreSQL requires no additional configuration. It is great for
testing and small-size instances. It does not provide high availability.
For backups, refer to the [backup page](../../management/infrastructure-management/backup).

The external PostgreSQL requires having an external database set up (e.g. with
RDS on AWS). This is the recommended setup for large-scale deployments.
Scaling, high availability, and backups should be managed with the provider's tools.

### Embedded configuration

:::info
If you have not yet upgraded to PostgreSQL version 16, please follow the **[migration guide](https://github.com/GitGuardian/ggtools/tree/main/postgresql-16-upgrade)** to migrate your existing embedded cluster to PostgreSQL 16.
:::

The embedded PostgreSQL is a PostgreSQL 16 running on a single pod.

:::caution
If you are using PgBouncer, add the following to the `pgbouncer.ini` file to allow GitGuardian tasks such as repository integration to perform correctly:

```bash
[pgbouncer]
pool_mode = session
ignore_startup_parameters = options,[... other parameters if needed]
```

For additional details, visit: [PgBouncer Configuration](https://www.pgbouncer.org/config.html)
:::

### External configuration

For an external PostgreSQL, you have the following configuration options:

- **Host:** the IP or hostname for your PostgreSQL. Defaults to "postgres".
- **Port:** the port on which PostgreSQL listens. Defaults to "5432".
- **Username:** the user used to connect to the database. Required.
- **Password:** the password used to connect to the database. Required.
- **Database:** the name of the database to connect to. Defaults to "prm". The database must exist.
- **Schema:** GitGuardian will use the default schema set for the user (usually 'public').

For scaling recommendations, refer to the hardware requirements
[for embedded clusters](../../system-requirements#embedded-kubernetes-cluster-installation)
or
[existing clusters](../../system-requirements#existing-kubernetes-cluster-installation).

### Helm-based installation

Helm installation currently supports only external databases.
[When installing via Helm](../installation-existing-cluster-helm), parameters will be passed via a YAML file.
The following parameters must be set inline :

- `host`
- `username` if relevant
- `database`
- `port` (5432 will be used as default)

:::tip
For ensuring that your databases are properly configured and accessible, you can use our **[preflight script](../installation-existing-cluster-helm#run-preflight-checks-)**.
:::

As for the password, it can either be set inside a [Kubernetes secret](../helm-secrets), or set
inline like the other parameters. Using secrets should be preferred over setting
sensitive parameters inline in values.

If you choose the first method, add a secret to your namespace, if it doesn't
exist yet:

```shell
kubectl create secret generic gitguardian-postgresql-secret \
  --from-literal=POSTGRES_PASSWORD=my_pg_password
```

If you intend to [enable TLS for your PostgreSQL database](./tls#certificates-as-a-secret),
the secret containing the password should also contain the TLS information.
Refer to the secret as the
`postgresql.existingSecret` parameter. the key to the password in this secret
should be set as `postgresql.existingSecretKeys.password`:

```yaml
postgresql:
  host: null # PostgreSQL database hostname
  username: null # PostgreSQL database username
  database: null # PostgreSQL database name
  port: 5432
  existingSecret: gitguardian-postgresql-secret
  existingSecretKeys:
    password: 'POSTGRES_PASSWORD'
```

If you choose the second method, your YAML file should contain this extract:

```yaml
postgresql:
  host: null # PostgreSQL Database host name
  username: null # PostgreSQL Database username
  database: null # PostgreSQL database name
  port: 5432
  password: 'my_pg_password'
```

### Database User Permissions

When setting up your PostgreSQL database, it is essential to configure the
database user with the appropriate permissions.

The user specified in the configuration (`username` parameter) should be the
owner of the database:

```sql
ALTER DATABASE my_pg_database OWNER TO my_pg_database_user;
```

If this is not possible due to internal regulation, the user will need the
following rights:

1. **Connection and object creation to the database:**
   The user should have the privilege to connect to the database, and to create
   extensions and schemas in it.

   ```sql
   GRANT ALL ON DATABASE my_pg_database TO my_pg_database_user;
   ```

2. **Table and other objects Creation:**
   To create tables, indexes, triggers and views, the user needs the right to
   create objects in the specified schema.

   ```sql
   GRANT ALL ON SCHEMA public TO my_pg_database_user;
   ```

3. **Data Modification Rights:**
   The user must have the necessary rights to insert, update, and delete data
   in the tables.

   ```sql
   GRANT ALL ON ALL TABLES IN SCHEMA public TO my_pg_database_user WITH GRANT OPTION;
   ```

## Redis

You can use the provided cache with the embedded cluster installation or bring your own for both embedded and external cluster installations.

:::warning Redis Compatibility
**Redis Cluster** is not supported by GitGuardian. Only **Redis Sentinel** is supported for high availability configurations.
:::

### Type: embedded/external

The embedded Redis requires no additional configuration. It is great for testing
and small-size instances. It does not provide high availability.
For backups, refer to the [backup page](../../management/infrastructure-management/backup).

The external Redis requires having an external cache set up (e.g. with
Elasticache on AWS). This is the recommended setup for large-scale deployments.
Scaling, high availability, and backups should be managed with the provider's tools.

### KOTS-based installation

#### External configuration

For an external Redis, you have the following configuration options:

- **Host:** the IP or hostname for your Redis. Defaults to "redis".
- **Port:** the port on which Redis listens. Defaults to "6379".
- **Username:** the user used to connect to the cache. Can be left empty.
- **Password:** the password used to connect to the cache. Required.
- **Use TLS:** checkbox to specify how to communicate with Redis.

#### External Redis Sentinel configuration

For an external Redis Sentinel, you have the following configuration options:

- **Host:** Comma-separated list of Redis Sentinel hosts.
- **Port:** the port on which Redis listens. Defaults to "6379".
- **Master Service Name:** the master Set name. Required.
- **Master Username:** the master user used to connect to the cache. Can be left empty.
- **Master Password:** the master password used to connect to the cache. Required.
- **Sentinel Username:** the sentinel user used to connect to the cache. Can be left empty.
- **Sentinel Password:** the sentinel password used to connect to the cache. Required.

:::info
TLS is not supported with Redis Sentinel.
:::

When utilizing **Redis Sentinel** for high availability, ensure that the Redis master password
matches with the Redis sentinel's password. By default, Sentinel operates on TCP port "26379".

### Helm-based installation

[When installing via Helm](../installation-existing-cluster-helm), parameters will be passed via a YAML file.

#### External redis server configuration

You can pass the whole URL directly, or provide `host`, `username`, `password`
and `port` individually. The URL will be composed in the following way:

```
redis(s)://$user:$password@$host:$port
```

Additionally, the `password` and `url` should be passed inline or via a [Kubernetes existing secret](../helm-secrets). Using secrets should be preferred over setting sensitive parameters inline in values.

If you choose the first option, create a Kubernetes secret in your cluster
containing either the URL or the password to your Redis, and refer to it as the
`existingSecret` in your values file.

```shell
kubectl create secret generic gitguardian-redis-secret \
  --from-literal=REDIS_URL=my_redis_url
```

If you intend to
[enable TLS for your Redis](./tls#certificates-as-a-secret),
the secret containing the password should also contain the TLS information.

Depending on your choices, your YAML file should contain one of:

  
    
    Sensitive parameter in secret (preferred)
    Sensitive parameter inline
  

Url passed directly

```yaml
redis:
  main:
    existingSecret: 'gitguardian-redis-secret'
    existingSecretKeys:
      url: 'REDIS_URL'
```

```yaml
redis:
  main:
    url: 'redis://:redis_password@123.456.789.123:6379'
```

  
  
    Url recomposed from elements

```yaml
redis:
  main:
    user: 'redis_user'
    host: '123.456.789.123'
    port: 6379
    existingSecret: 'gitguardian-redis-secret'
    existingSecretKeys:
      password: 'REDIS_PASSWORD'
```

```yaml
redis:
  main:
    user: 'redis_user'
    host: '123.456.789.123'
    port: 6379
    password: 'redis_password'
```

  

#### External Redis Sentinel configuration

Under `redis.main`, you need to configure `user`, `password`. Those credentials belongs to the master.

Under `redis.main.sentinel`, you need to configure `enabled`, `url`, `user`, `password` and `masterServiceName`.

:::info
TLS is not supported with Redis Sentinel.
:::

Additionally, both `password` fields and `url` should be passed via a Kubernetes secret,
though it is possible to pass them inline, or via an
[external secret](../helm-secrets). Using secrets
should be preferred over setting sensitive parameters inline in values.

If you choose the first option, create a Kubernetes secret in your cluster
containing either the URL or the password to your Redis, and refer to it as the
`existingSecret` in your values file.

```shell
kubectl create secret generic gitguardian-redis-secret \
  --from-literal=REDIS_URL=my_redis_url
```

If you intend to
[enable TLS for your Redis](./tls#certificates-as-a-secret),
the secret containing the password should also contain the TLS information.

Depending on your choices, your YAML file should contain one of:

  
    
    Sensitive parameter in secret (preferred)
    Sensitive parameter inline
  

Sentinel

```yaml
redis:
  main:
    existingSecret: gitguardian-redis-secret
    existingSecretKeys:
      password: redis-password
      sentinel:
        url: redis-sentinel-url
        password: redis-password
    sentinel:
      enabled: true
      masterServiceName: gitguardian-redis
```

```yaml
redis:
  main:
    password: 'redis_password'
    sentinel:
      enabled: true
      url: 123.456.789.123:26379
      password: 'redis_sentinel_password'
      masterServiceName: gitguardian-redis
```

  

### Second Redis instance for commit cache

You can configure a second Redis instance that will be dedicated to the commit
cache feature.

Commit cache allows better performances for both real-time and historical scans
by keeping the results of commits already scanned in a cache.

You can configure a second Redis instance that will be dedicated to the commit
cache feature. We only recommend this option for big instances (more than 100GB
of code for the entire perimeter) where the commit cache should be configured
with a minimum of 16GB.

This second Redis instance has the same configuration options as the main one.

On KOTS-based installations, you can access configuration options by checking
the `Commit cache Redis` checkbox in the Redis section in the KOTS Admin Console.

On Helm-based installations, you can configure this option
[under the `redis.commitCache` keys](../../management/infrastructure-management/helm-values)
in your values file.

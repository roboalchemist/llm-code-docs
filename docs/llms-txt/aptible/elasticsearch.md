# Source: https://www.aptible.com/docs/core-concepts/managed-databases/supported-databases/elasticsearch.md

# Elasticsearch

> Learn about running secure, Managed Elasticsearch Databases on Aptible

# Available Versions

<Warning> Due to Elastic licensing changes, newer versions of Elasticsearch will not be available on Aptible. 7.10 will be the final version offered, with no deprecation date. </Warning>

The following versions of [Elasticsearch](https://www.elastic.co/elasticsearch) are currently available:

| Version |   Status  | End-Of-Life Date | Deprecation Date |
| :-----: | :-------: | :--------------: | :--------------: |
|   7.10  | Available |        N/A       |        N/A       |

<Note>For databases on EOL versions, Aptible will prevent new databases from being provisioned and mark existing database as `DEPRECATED` on the deprecation date listed above. While existing databases will not be affected, we recommend end-of-life databases to be [upgraded](https://www.aptible.com/docs/core-concepts/managed-databases/managing-databases/database-upgrade-methods#database-upgrades). The latest version offered on Aptible will always be available for provisioning, regardless of end-of-life date.</Note>

# Connecting to Elasticsearch

**For Elasticsearch 6.8 or earlier:**
Elasticsearch is accessible over HTTPS, with HTTPS basic authentication.

**For Elasticsearch 7.0 or later:**
Elasticsearch is accessible over HTTPS, with Elasticsearch's native authentication mechanism.

The `aptible` user provided by the [Database Credentials](/core-concepts/managed-databases/connecting-databases/database-credentials) is the only user available by default and is configured with the [Elasticsearch Role](https://www.elastic.co/guide/en/elasticsearch/reference/current/built-in-roles.html) of `superuser`. You may [manage the password](https://www.elastic.co/guide/en/elasticsearch/reference/7.8/security-api-change-password.html) of any [Elasticsearch Built-in user](https://www.elastic.co/guide/en/elasticsearch/reference/current/built-in-users.html) if you wish and otherwise manage all aspects of user creation and permissions, with the exception of the `aptible` user.

<Info>Elasticsearch Databases deployed on Aptible use a valid certificate for their host, so you're encouraged to verify the certificate when connecting.</Info>

## Subscription Features

For Elasticsearch 7.0 or later:
Formerly referred to as X-pack features, your [Elastic Stack subscription](https://www.elastic.co/subscriptions) will determine the features available in your Deploy Elasticsearch Database. By default, you will have the "Basic" features. If you purchase a license from Elastic, you may [update your license](https://www.elastic.co/guide/en/kibana/current/managing-licenses.html#update-license) at any time.

# Plugins

Some Elasticsearch plugins may be installed by request. Contact [Aptible Support](/how-to-guides/troubleshooting/aptible-support) if you need a particular plugin.

# Configuration

Elasticsearch Databases can be configured with Elasticsearch's [Cluster Update Settings API](https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-update-settings.html). Changes made to persistent settings will persist across Database restarts.

Deploy will automatically set the JVM heap size to 50% of the container's memory allocation, per [Elastic's recommendation](https://www.elastic.co/guide/en/elasticsearch/reference/current/heap-size.html#heap-size).

## Kibana

For Elasticsearch 7.0 or later, you can easily deploy [Elastic's official Kibana image](https://hub.docker.com/_/kibana) as an App on Aptible.

<Card title="How to set up Kibana on Aptible" icon="book-open-reader" iconType="duotone" horizontal href="https://www.aptible.com/docs/running-kibana">
  Read the guide
</Card>

## Log Rotation

For Elasticsearch 7.0 or later: if you're using Elasticsearch to hold log data, you may need to periodically create new log indexes. By default, Logstash and our [Log Drains](/core-concepts/observability/logs/log-drains/overview) will create new indexes daily. As the indexes accumulate, they will require more disk space and more RAM. Elasticsearch allocates RAM on a per-index basis, and letting your logs retention grow unchecked will likely lead to fatal issues when the Database runs out of RAM or disk space.

To avoid this, we recommend using a combination of Elasticsearch's native features to ensure you don't accumulate too many open indexes:

* [Index Lifecycle Management](https://www.elastic.co/guide/en/elasticsearch/reference/current/index-lifecycle-management.html) can be configured to delete indexes over a certain age
* [Snapshot Lifecycle Management](https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshot-lifecycle-management.html) can be configured to back up indexes on a schedule, for example, to S3
* The Elasticsearch [S3 Repository Plugin](https://www.elastic.co/guide/en/elasticsearch/plugins/current/repository-s3.html), which is installed by default

<Card title="How to set up Elasticsearch Log Rotation" icon="book-open-reader" iconType="duotone" href="https://www.aptible.com/docs/elasticsearch-log-rotation" horizontal>
  Read the guide
</Card>

# Connection Security

Aptible Elasticsearch Databases support connections via the following protocols:

* For all Elasticsearch versions 6.8 and earlier: `SSLv3`, `TLSv1.0`, `TLSv1.1`, `TLSv1.2`
* For all Elasticsearch versions 7.0 and later: `TLSv1.1` , `TLSv1.2`

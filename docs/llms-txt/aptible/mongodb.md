# Source: https://www.aptible.com/docs/core-concepts/managed-databases/supported-databases/mongodb.md

# MongoDB

> Learn about running secure, Managed MongoDB Databases on Aptible

## Available Versions

<Warning> Due to MongoDB licensing changes, newer versions of MongoDB will no longer be available on Aptible. </Warning>

The following versions of [MongoDB](https://www.mongodb.com/) are currently available:

| Version |   Status  | End-Of-Life Date | Deprecation Date |
| :-----: | :-------: | :--------------: | :--------------: |
|   4.0   | Available |        N/A       |        N/A       |

<Note>For databases on EOL versions, Aptible will prevent new databases from being provisioned and mark existing database as `DEPRECATED` on the deprecation date listed above. While existing databases will not be affected, we recommend end-of-life databases to be [upgraded](https://www.aptible.com/docs/core-concepts/managed-databases/managing-databases/database-upgrade-methods#database-upgrades). The latest version offered on Aptible will always be available for provisioning, regardless of end-of-life date.</Note>

# Connecting to MongoDB

Aptible MongoDB [Databases](/core-concepts/managed-databases/overview) require authentication and SSL to connect.

<Tip> MongoDB databases use a valid certificate for their host, so you're encouraged to verify the certificate when connecting.</Tip>

## Connecting to the `admin` database

There are two MongoDB databases you might want to connect to:

* The `admin` database.
* The `db` database created by Aptible automatically.

The username (`aptible`) and password for both databases are the same. However, the users in MongoDB are different (i.e. there is a `aptible` user in the `admin` database, and a separate `aptible` user in the `db` database, which simply happens to have the same password).

This means that if you'd like to connect to the `admin` database, you need to make sure to select that one as your authentication database when connecting: connecting to `db` and running `use admin` will **not** work.

# Clustering

Replica set [clustering](/core-concepts/managed-databases/managing-databases/replication-clustering) is available for MongoDB. Replicas can be created using the [`aptible db:replicate`](/reference/aptible-cli/cli-commands/cli-db-replicate) command.

## Failover

MongoDB replica sets will automatically failover between members. In order to do so effectively, MongoDB recommends replica sets have a minimum of [three members](https://docs.mongodb.com/v4.2/core/replica-set-members/). This can be done by creating two Aptible replicas of the same primary Database.

The [connection URI](https://docs.mongodb.com/v4.2/reference/connection-string/) you provide your Apps with must contain the hostnames and ports of all members in the replica set. MongoDB clients will attempt each host until it's able to reach the replica set. With a single host, if that host is unavailable, the App will not be able to reach the replica set. The hostname and port of each member can be found in the [Database's Credentials](/core-concepts/managed-databases/connecting-databases/database-credentials), and the combined connection URI will look something like this for a three-member replica set:

```
mongodb://username:password@host1.aptible.in:27017,host2.aptible.in:27018,host3.aptible.in:27019/db
```

# Data Integrity and Durability

On Aptible, MongoDB is configured with default settings for journaling. For MongoDB 3.x instances, this means [journaling](https://docs.mongodb.com/manual/core/journaling/) is enabled. If you use the appropriate write concern (`j=1`) when writing to MongoDB, you are guaranteed that committed transactions were written to disk.

# Configuration

Configuration of MongoDB command line options is not supported on Aptible.

MongoDB Databases on Aptible autotune their Wired Tiger cache size based on the size of their Container, based upon [Mongo's recommendation](https://docs.mongodb.com/manual/faq/storage/#to-what-size-should-i-set-the-wiredtiger-internal-cache-).

# Connection Security

Aptible MongoDB Databases support connections via the following protocols:

* For Mongo versions 2.6, 3.4, and 3.6: `TLSv1.0`, `TLSv1.1`, `TLSv1.2`
* For Mongo version 4.0: `TLSv1.1`, `TLSv1.2`

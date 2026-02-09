# Source: https://www.aptible.com/docs/core-concepts/managed-databases/supported-databases/influxdb.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# InfluxDB

> Learn about running secure, Managed InfluxDB Databases on Aptible

# Available Versions

The following versions of [InfluxDB](https://www.influxdata.com/) are currently available:

| Version |   Status   |  End-Of-Life Date | Deprecation Date |
| :-----: | :--------: | :---------------: | :--------------: |
|   1.8   | Deprecated | December 31, 2021 |   January 2026   |
|   1.11  |  Available |        N/A        |        N/A       |
|   1.12  |  Available |        N/A        |        N/A       |
|   2.7   |  Available |        N/A        |        N/A       |

<Note>For databases on EOL versions, Aptible will prevent new databases from being provisioned and mark existing database as `DEPRECATED` on the deprecation date listed above. While existing databases will not be affected, we recommend end-of-life databases to be [upgraded](https://www.aptible.com/docs/core-concepts/managed-databases/managing-databases/database-upgrade-methods#database-upgrades). Restoring a database from a backup will provision a new database that matches the version associated with the backup, even if that version is EOL or Deprecated. The latest version offered on Aptible will always be available for provisioning, regardless of end-of-life date.</Note>

# Accessing data in InfluxDB using Grafana

[Grafana](https://grafana.com) is a great visualization and monitoring tool to use with InfluxDB. For detailed instructions on deploying Grafana to Aptible, follow this tutorial: [Deploying Grafana on Aptible](/how-to-guides/observability-guides/deploy-use-grafana).

# Configuration

Contact [Aptible Support](/how-to-guides/troubleshooting/aptible-support) if you need to change the configuration of an InfluxDB database on Aptible.

# Connection Security

Aptible InfluxDB Databases support connections via the following protocols:

* For InfluxDB version 1.4, 1.7, and 1.8: `TLSv1.0`, `TLSv1.1`, `TLSv1.2`

# Clustering

Clustering is not available for InfluxDB databases since this feature is not available in InfluxDB's open-source offering.

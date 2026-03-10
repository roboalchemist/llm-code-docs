# Source: https://render.com/docs/deploy-clickhouse.md

# Deploy ClickHouse

[ClickHouse](https://clickhouse.tech/) is a column-oriented OLAP database system that allows generating analytical reports in real-time using SQL queries. Clickhouse strives to maximize hardware efficiency and is capable of processing typical analytical queries two to three orders of magnitude faster than traditional row-oriented systems. It also supports multi-master asynchronous replication where all nodes are equal, which prevents single points of failure. You can run your own ClickHouse instance as a [private service](private-services) on Render backed by *high performance SSDs* with [automatic daily snapshots](disks#disk-snapshots).

We'll be deploying ClickHouse using the latest official [Docker image](https://hub.docker.com/r/yandex/clickhouse-server) and the [Render ClickHouse repository](https://github.com/render-examples/clickhouse) to install ClickHouse with a single click.

## One-Click Deploy

Click *Deploy to Render* below and follow the prompts to deploy ClickHouse on Render.

<deploy-to-render repo="https://github.com/render-examples/clickhouse">
</deploy-to-render>

## Manual Deploy

1. Create a new [*Private Service*](https://dashboard.render.com/select-repo?type=pserv) on Render and enter `https://github.com/render-examples/clickhouse` in the repository search box. You can also fork [the repository](https://github.com/render-examples/clickhouse) on GitHub or click `Use this template`.

2. Set the *Language* field to `Docker`.

3. Be sure to choose the *Standard* instance type or higher. ClickHouse may exhaust memory limits on starter instance types.

4. The `master` branch uses the latest stable version of ClickHouse. You can choose a different branch if you'd like to use a specific ClickHouse version.

5. Under *Advanced*, add a disk with the following values:

   |                |                                                      |
   | -------------- | ---------------------------------------------------- |
   | *Mount Path* | `/data/db`                                           |
   | *Size*       | `10 GB` Feel free to change this to suit your needs. |

You're all set! Save your private service, and your ClickHouse instance should be up in a few minutes.

## Connecting to ClickHouse

You should be able to connect to your ClickHouse instance using `host:port` values displayed in the dashboard like `clickhouse-xyz:8123` (port `9009` is internal and used for replication). Consult [ClickHouse documentation on interfaces](https://clickhouse.tech/docs/en/interfaces/) for more details.

| Interface         | Description                                                                                                                  |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `clickhouse:8123` | [HTTP interface](https://clickhouse.tech/docs/en/interfaces/http/)                                                           |
| `clickhouse:9000` | [Native interface](https://clickhouse.tech/docs/en/interfaces/tcp/) for driver libraries and `clickhouse-client` application |
| `clickhouse:9004` | [MySQL wire protocol](https://clickhouse.tech/docs/en/interfaces/mysql/)                                                     |

You can also use the shell in your dashboard to connect to your database.

```shell
clickhouse-client --host clickhouse-xyz
```

[image: ClickHouse Shell on Render]

## Backups

> Relying on a [disk snapshot](disks#disk-snapshots) to restore a database is not recommended. Restoring a disk snapshot will likely result in corrupted or lost database data.

Using a database’s recommended backup tool (for example: [clickhouse-copier](https://clickhouse.com/docs/en/operations/utilities/clickhouse-copier)) is the recommended way to backup and restore a database without corrupted or lost data.
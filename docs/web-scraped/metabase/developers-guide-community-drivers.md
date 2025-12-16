# Source: https://www.metabase.com/docs/latest/developers-guide/community-drivers

<div>

1.  [Home](/docs/latest/)
2.  [Developers Guide](/docs/latest/developers-guide/start)

</div>

<div>

[ v0.57 ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdib3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iY2hldnJvbiI+CjxwYXRoIG9wYWNpdHk9IjAuOSIgZD0iTTMgOC45NjMzOEwxNiAyMS45NjM0TDI5IDguOTYzMzgiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSI1IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) ]

-   [v0.56](/docs/v0.56)
-   [v0.55](/docs/v0.55)
-   [v0.54](/docs/v0.54)
-   [v0.53](/docs/v0.53)
-   [v0.52](/docs/v0.52)
-   [v0.51](/docs/v0.51)
-   [v0.50](/docs/v0.50)
-   [v0.49](/docs/v0.49)
-   [v0.48](/docs/v0.48)
-   [See more](/docs/all)

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj48cGF0aCBzdHJva2U9IiM1MDlFRTMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xNi4yODMgMTIuMjYgMTUuNSAxNWwtLjc4My0yLjc0YTQuMzMzIDQuMzMzIDAgMCAwLTIuOTc1LTIuOTc2TDkgOC41bDIuNzQtLjc4M2E0LjMzMyA0LjMzMyAwIDAgMCAyLjk3Ni0yLjk3NUwxNS41IDJsLjc4MyAyLjc0YTQuMzMzIDQuMzMzIDAgMCAwIDIuOTc1IDIuOTc2TDIyIDguNWwtMi43NC43ODNhNC4zMzQgNC4zMzQgMCAwIDAtMi45NzYgMi45NzVsLS4wMDEuMDAxWk02LjUgMjJsLjU5MS0xLjc3NGEzLjM3NSAzLjM3NSAwIDAgMSAyLjEzNS0yLjEzNUwxMSAxNy41bC0xLjc3NC0uNTkxYTMuMzc1IDMuMzc1IDAgMCAxLTIuMTM1LTIuMTM0TDYuNSAxM2wtLjU5MSAxLjc3NGEzLjM3NSAzLjM3NSAwIDAgMS0yLjEzNCAyLjEzNUwyIDE3LjVsMS43NzUuNTkxYTMuMzc1IDMuMzc1IDAgMCAxIDIuMTM0IDIuMTM0TDYuNSAyMloiPjwvcGF0aD48L3N2Zz4=) What's new](/releases)

</div>

<div>

</div>

# Community drivers

> Community drivers are not supported on [Metabase Cloud](/cloud/).

In addition to our [Officially supported drivers](../databases/connecting#connecting-to-supported-databases), many people build and maintain drivers for database integrations.

## How to use a Community driver

To use a Community driver on a self-hosted Metabase:

1.  Download the latest JAR file from the driver's repository (see the repo's Releases section for the JAR files).
2.  Copy the JAR file into the plugins directory in your Metabase directory (the directory where you run the Metabase JAR).

You can change the location of the plugins directory by setting the environment variable [`MB_PLUGINS_DIR`](../configuring-metabase/environment-variables#mb_plugins_dir).

## Community drivers

> You install these drivers at your own risk. The plugins run as part of your Metabase and will have access to anything your Metabase does. And since we can't vet for them, we don't make them available on [Metabase Cloud](/cloud/).

Anyone can build a community driver. These are the currently known third-party database drivers for Metabase.

  Database                                                                                GitHub Stars                                                                                         Last release (*if available*)
  --------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------
  [CSV](https://github.com/Markenson/csv-metabase-driver)                                 ![GitHub stars](https://img.shields.io/github/stars/Markenson/csv-metabase-driver)                   ![GitHub (Pre-)Release Date](https://img.shields.io/github/release-date-pre/Markenson/csv-metabase-driver)
  [Databend](https://github.com/databendcloud/metabase-databend-driver)                   ![GitHub stars](https://img.shields.io/github/stars/databendcloud/metabase-databend-driver)          ![GitHub (Pre-)Release Date](https://img.shields.io/github/release-date-pre/databendcloud/metabase-databend-driver)
  [DB2 for LUW](https://github.com/alisonrafael/metabase-db2-driver)                      ![GitHub stars](https://img.shields.io/github/stars/alisonrafael/metabase-db2-driver)                ![GitHub (Pre-)Release Date](https://img.shields.io/github/release-date-pre/alisonrafael/metabase-db2-driver)
  [IBM i](https://github.com/damienchambe/metabase-ibmi-driver)                           ![GitHub stars](https://img.shields.io/github/stars/damienchambe/metabase-ibmi-driver)               ![GitHub (Pre-)Release Date](https://img.shields.io/github/release-date-pre/damienchambe/metabase-ibmi-driver)
  [Dremio](https://github.com/Baoqi/metabase-dremio-driver)                               ![GitHub stars](https://img.shields.io/github/stars/Baoqi/metabase-dremio-driver)                    ![GitHub (Pre-)Release Date](https://img.shields.io/github/release-date-pre/Baoqi/metabase-dremio-driver)
  [DuckDB](https://github.com/MotherDuck-Open-Source/metabase_duckdb_driver)              ![GitHub stars](https://img.shields.io/github/stars/MotherDuck-Open-Source/metabase_duckdb_driver)   ![GitHub (Pre-)Release Date](https://img.shields.io/github/release-date-pre/MotherDuck-Open-Source/metabase_duckdb_driver)
  [Firebolt](https://github.com/firebolt-db/metabase-firebolt-driver)                     ![GitHub stars](https://img.shields.io/github/stars/firebolt-db/metabase-firebolt-driver)            ![GitHub (Pre-)Release Date](https://img.shields.io/github/release-date-pre/firebolt-db/metabase-firebolt-driver)
  [Firebird](https://github.com/evosec/metabase-firebird-driver)                          ![GitHub stars](https://img.shields.io/github/stars/evosec/metabase-firebird-driver)                 ![GitHub (Pre-)Release Date](https://img.shields.io/github/release-date-pre/evosec/metabase-firebird-driver)
  [GreptimeDB](https://github.com/greptimeteam/greptimedb-metabase-driver)                ![GitHub stars](https://img.shields.io/github/stars/greptimeteam/greptimedb-metabase-driver)         ![GitHub (Pre-)Release Date](https://img.shields.io/github/release-date-pre/greptimeteam/greptimedb-metabase-driver)
  [Hydra](https://www.hydra.so/blog-posts/2022-09-28-metabase-and-hydra)                  Hydra connections use the official [Postgres driver](../databases/connections/postgresql).           Not applicable.
  [Impala](https://github.com/brenoae/metabase-impala-driver)                             ![GitHub stars](https://img.shields.io/github/stars/brenoae/metabase-impala-driver)                  ![GitHub (Pre-)Release Date](https://img.shields.io/github/release-date-pre/brenoae/metabase-impala-driver)
  [InterSystems IRIS](https://github.com/Siddardar/metabase-iris-driver/tree/main)        ![GitHub stars](https://img.shields.io/github/stars/Siddardar/metabase-iris-driver)                  ![GitHub (Pre-)Release Date](https://img.shields.io/github/release-date-pre/Siddardar/metabase-iris-driver)
  [Materialize](https://github.com/MaterializeInc/metabase-materialize-driver)            ![GitHub stars](https://img.shields.io/github/stars/MaterializeInc/metabase-materialize-driver)      ![GitHub (Pre-)Release Date](https://img.shields.io/github/release-date-pre/MaterializeInc/metabase-materialize-driver)
  [Neo4j](https://github.com/StronkMan/metabase-neo4j-driver)                             ![GitHub stars](https://img.shields.io/github/stars/StronkMan/metabase-neo4j-driver)                 ![GitHub (Pre-)Release Date](https://img.shields.io/github/release-date-pre/StronkMan/metabase-neo4j-driver)
  [Netsuite SuiteAnalytics Connect](https://github.com/ericcj/metabase-netsuite-driver)   ![GitHub stars](https://img.shields.io/github/stars/ericcj/metabase-netsuite-driver)                 ![GitHub (Pre-)Release Date](https://img.shields.io/github/release-date-pre/ericcj/metabase-netsuite-driver)
  [Peaka](https://github.com/peakacom/metabase-driver)                                    ![GitHub stars](https://img.shields.io/github/stars/peakacom/metabase-driver)                        ![GitHub (Pre-)Release Date](https://img.shields.io/github/release-date-pre/peakacom/metabase-driver)
  [SPARQL](https://github.com/jhisse/metabase-sparql-driver)                              ![GitHub stars](https://img.shields.io/github/stars/jhisse/metabase-sparql-driver)                   ![GitHub (Pre-)Release Date](https://img.shields.io/github/release-date-pre/jhisse/metabase-sparql-driver)
  [Teradata](https://github.com/swisscom-bigdata/metabase-teradata-driver)                ![GitHub stars](https://img.shields.io/github/stars/swisscom-bigdata/metabase-teradata-driver)       ![GitHub (Pre-)Release Date](https://img.shields.io/github/release-date-pre/swisscom-bigdata/metabase-teradata-driver)

If you don't see a driver for your database, try looking in the comments of the [issue related to the database](https://github.com/metabase/metabase/labels/Database%2F). You might also find more drivers by searching on GitHub for "Metabase driver".

If you're having problems installing or using a community driver, your best bet is to contact the author of the driver.

## Write your own driver

Check out [Guide to writing a Metabase driver](./drivers/start).

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/developers-guide/community-drivers.md) ]
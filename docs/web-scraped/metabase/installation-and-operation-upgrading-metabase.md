# Source: https://www.metabase.com/docs/latest/installation-and-operation/upgrading-metabase

<div>

1.  [Home](/docs/latest/)
2.  [Installation and Operation](/docs/latest/installation-and-operation/start)

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

# Upgrading Metabase

This page covers how to upgrade to a new Metabase release.

-   [Announcement posts for major releases](/releases)
-   [Changelogs](/changelog).
-   [Release notes on GitHub](https://github.com/metabase/metabase/releases).

## Upgrading Metabase Cloud

If you're on a [Metabase Cloud](/pricing/) plan, we'll upgrade your Metabase automatically with each new release; no action needed on your end ([unless you're using the Embedded analytics SDK](#instances-using-the-embedded-analytics-sdk-on-metabase-cloud-must-request-an-upgrade)).

How soon we upgrade you depends on the type of release:

-   Minor releases (e.g., x.54.4 to x.54.5): Usually about a week.
-   Major releases (e.g., x.53.4 to x.54.1): Longer, usually months (just to make sure everything goes smoothly).

Cloud customers can request an early upgrade by emailing support at help@metabase.com. Include the URL of the Metabase you want us to upgrade.

### Instances using the Embedded analytics SDK on Metabase Cloud must request an upgrade

If you're using the [Embedded analytics SDK](../embedding/sdk/introduction) on Metabase Cloud, we pin your version so that it doesn't upgrade automatically, as you should test the changes before upgrading.

To upgrade your Metabase, you'll need to request an upgrade by [contacting support](/help-premium).

See our [upgrade guide for the Embedded analytics SDK](../embedding/sdk/upgrade).

## Upgrading a self-hosted Metabase

Here are the steps for upgrading to a new Metabase version (major or minor):

### 1. Back up of your application database 

The application database keeps track of every single thing (but the data of your connected database) of your Metabase instance. While it's unlikely you'll need to roll back to your current version, a backup will do wonders for your peace of mind in case something goes wrong.

See [Backing up Metabase application data](backing-up-metabase-application-data).

### 2. Swap in the new Metabase version 

Steps differ depending on whether you're running the container image or the JAR.

**Upgrading the container image**

1.  Stop the current container.

2.  Pull the latest Metabase Docker image (though we recommend that you pull a specific tag instead of using `latest`).

    Metabase Open Source:

    ::: 
    ::: highlight
    ``` highlight
    docker pull metabase/metabase:latest
    ```
    :::
    :::

    Metabase Pro or Enterprise:

    ::: 
    ::: highlight
    ``` highlight
    docker pull metabase/metabase-enterprise:latest
    ```
    :::
    :::

3.  Start the new container image. Depending on the ports and container name, the command will look something like:

    Metabase Open Source:

    ::: 
    ::: highlight
    ``` highlight
    docker run -d -p 3000:3000 -e MB_DB_CONNECTION_URI="jdbc:postgresql://<host>:5432/metabase?user=<username>&password=<password>" --name metabase metabase/metabase:latest
    ```
    :::
    :::

    Metabase Pro or Enterprise:

    ::: 
    ::: highlight
    ``` highlight
    docker run -d -p 3000:3000 -e MB_DB_CONNECTION_URI="jdbc:postgresql://<host>:5432/metabase?user=<username>&password=<password>" --name metabase metabase/metabase-enterprise:latest
    ```
    :::
    :::

On startup, Metabase will perform the upgrade automatically. Once Metabase has completed the upgrade, you'll be running the new version.

**Upgrading the JAR**

To upgrade, you'll need to stop the service, replace the JAR with the newer version, and restart the service.

E.g., if you're running Metabase on Debian as a service using Nginx.

1.  Stop the Metabase service. Assuming you called your service `metabase.service`, you'll run:

    ::: 
    ::: highlight
    ``` highlight
    sudo systemctl stop metabase.service
    ```
    :::
    :::

2.  Download the latest version of the JAR file:

    -   [Metabase Open Source JAR](/start/oss/jar)
    -   [Metabase Pro or Enterprise JAR](https://downloads.metabase.com/enterprise/latest/metabase.jar)

And replace the current (older) Metabase JAR file with the newer JAR you downloaded.

1.  Restart the service:

    ::: 
    ::: highlight
    ``` highlight
    sudo systemctl restart metabase.service
    ```
    :::
    :::

## Upgrading from older versions of Metabase

If you're on a Metabase version older than Metabase 40, you'll need to upgrade release by release until you're on the latest version of Metabase 40. From the latest version of Metabase 40, you can then jump to the current version of Metabase.

For example, if you're running Metabase 1.38, your upgrade path would look like:

-   1.38.X
-   1.39.X
-   1.40.X
-   Latest

With X being the latest version available for each release.

Check out a list of [Metabase releases](https://github.com/metabase/metabase/releases).

When upgrading between major versions (e.g. v53.x to v54.x), use the latest minor version available for that major version. E.g., if you want to upgrade from v50 to v51, use the latest point version available for 51.

## Upgrading Metabase on other platforms

-   [Upgrading Azure Web Apps deployments](running-metabase-on-azure#additional-configurations)

## What happens during an upgrade or downgrade?

During a **major version** upgrade (e.g., 53.1 or 54.1), Metabase will:

-   Perform all the migrations needed to upgrade to the new version, such as any schema changes to the application database between the two versions.
-   Keep all the metadata it needs to work on the application database.

Metabase will do all this automatically.

If you need to downgrade after a major version upgrade, you'll either need to restore from a backup, or manually migrate to a lower version, otherwise Metabase may refuse to start (see the next section).

During a **minor version upgrade** (e.g., 54.1 to 54.2), the new Metabase container or Jar will just work. Only in rare cases will it have to perform a migration, but, like with major version upgrades, Metabase will perform the migration automatically. And of course, you're backing up your application database each time you upgrade, right?

## Rolling back an upgrade or to an older version

> **The downgrade command must be run on the JAR with the higher version number.**

In general, regular backups (especially backups before upgrading), are the best policy, so we recommend reverting to a backup of your application database to roll back an upgrade.

But if you've made any change (adding new questions/dashboards, etc) since upgrading that you want to keep, you may be able to use the `migrate down` command to roll back your Metabase application database to support the previous Metabase version you were running. When Metabase upgrades to a new version, it runs migrations that may change the application database schema. The `migrate down` command undoes those schema changes. In general, we recommend restoring from a backup (the backup that you remembered to generate before upgrading), and only using the `migrate down` command if you need to keep changes made after your upgrade.

### Using the migrate down command

Stop your Metabase and use the current, upgraded Metabase JAR (not the Metabase JAR you want to roll back to) to complete the rollback with the `migrate down` command. Make sure that the connection details for your application database are set in the environment variables, for example:

``` highlight
export MB_DB_TYPE=postgres
export MB_DB_DBNAME=metabaseappdb
export MB_DB_PORT=5432
export MB_DB_USER=username
export MB_DB_PASS=password
export MB_DB_HOST=localhost
java --add-opens java.base/java.nio=ALL-UNNAMED -jar metabase.jar migrate down
```

If you're running Docker, use the command `"migrate down"` (with the quotes around `"migrate down"`), and include the connection details for your application database, for example:

``` highlight
docker run
  -e "MB_DB_TYPE=postgres" \
  -e "MB_DB_DBNAME=metabaseappdb" \
  -e "MB_DB_PORT=5432" \
  -e "MB_DB_USER=name" \
  -e "MB_DB_PASS=password" \
  -e "MB_DB_HOST=my-database-host" \
--rm metabase/metabase:<tag> "migrate down"
```

Note the quotes around `"migrate down"`. You can also just open a shell into the container and run the migrate command inside it.

Once the migration process completes, start up Metabase using the JAR or container image for the version you want to run.

## Upgrading Metabase running in a cluster

If you're running Metabase in a cluster:

1.  Reduce the number of nodes to a single node. You can't upgrade all nodes at the same time because the upgrade process works by acquiring a migration lock on the application database from a single client, which performs the migration. If you keep more than one node active when you do a major version upgrade, the application won't behave correctly, as schema changes to the application database could cause problems for nodes that are still running the older version of Metabase.
2.  Perform the upgrade as normal (as outlined above).
3.  Raise the number of nodes to the same number you had before.

Make sure you container orchestrator or cluster manager doesn't kill the Metabase process while it's performing the migrations, otherwise you'll may end up with a corrupted application database and you'll need to restore from a backup.

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/installation-and-operation/upgrading-metabase.md) ]
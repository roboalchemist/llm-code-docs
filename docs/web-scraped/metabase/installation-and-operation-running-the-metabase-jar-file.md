# Source: https://www.metabase.com/docs/latest/installation-and-operation/running-the-metabase-jar-file

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

# Running the Metabase OSS JAR file

> We recommend running Metabase on [Metabase Cloud](/cloud/). If you need to self-host, you *can* run Metabase as a standalone JAR, but [we recommend running Metabase in a Docker container](./running-metabase-on-docker).

To run the free, Open Source version of Metabase via a JAR file, you will need to have a Java Runtime Environment (JRE) installed on your system.

If you have a token for the [Pro or Enterprise editions](/pricing/) of Metabase, see [Activating your Metabase commercial license](../installation-and-operation/activating-the-enterprise-edition).

## Quick start

> The quick start is intended for running Metabase locally. See below for instructions on [running Metabase in production](#production-installation).

If you have Java installed:

1.  [Download the JAR file for Metabase OSS](/start/oss/jar). If you're on a [Pro](/product/pro) or [Enterprise](/product/enterprise) plan, download the [JAR for the Enterprise Edition](https://downloads.metabase.com/enterprise/latest/metabase.jar).
2.  Create a new directory and move the Metabase JAR into it.
3.  Change into your new Metabase directory and run the JAR.

``` highlight
java --add-opens java.base/java.nio=ALL-UNNAMED -jar metabase.jar
```

Metabase will log its progress in the terminal as it starts up. Wait until you see "Metabase Initialization Complete" and visit `http://localhost:3000/setup`.

If you are using a Pro or Enterprise version, be sure to [activate your license](../installation-and-operation/activating-the-enterprise-edition).

## Local installation

If you just want to try Metabase out, play around with Metabase, or just use Metabase on your local machine, Metabase ships with a default application database that you can use. **This setup is not meant for production**. If you intend to run Metabase for real at your organization, see [Production installation](#production-installation).

The below instructions are the same as the quick start above, just with a little more context around each step.

### 1. Install Java JRE 

You may already have Java installed. To check the version, open a terminal and run:

``` highlight
java -version
```

If Java isn't installed, you'll need to install Java before you can run Metabase. We recommend version 21 of JRE from [Eclipse Temurin](https://adoptium.net/) with HotSpot JVM. You can run Metabase wherever Java 21 runs. Earlier Java versions aren't supported. The particular processor architecture shouldn't matter (although we only test Metabase for x86 and ARM).

### 2. Download Metabase 

Download the JAR file:

-   [Metabase OSS](/start/oss/jar)
-   [Metabase Enterprise/Pro edition](https://downloads.metabase.com/enterprise/latest/metabase.jar)

If you want to install the [Pro or Enterprise editions](/pricing/) of Metabase, see [Activating your Metabase commercial license](../installation-and-operation/activating-the-enterprise-edition).

### 3. Create a new directory and move the Metabase JAR into it 

When you run Metabase, Metabase will create some new files, so it's important to put the Metabase Jar file in a new directory before running it (so move it out of your downloads folder and put it a new directory).

On posix systems, the commands would look something like this:

Assuming you downloaded to `/Users/person/Downloads`:

``` highlight
mkdir ~/metabase
```

then

``` highlight
mv /Users/person/Downloads/metabase.jar ~/metabase
```

### 4. Change into your new Metabase directory and run the jar 

Change into the directory you created in step 2:

``` highlight
cd ~/metabase
```

Now that you have Java working you can run the JAR from a terminal with:

``` highlight
java --add-opens java.base/java.nio=ALL-UNNAMED -jar metabase.jar
```

Metabase will start using the default settings. You should see some log entries starting to run in your terminal window showing you the application progress as it starts up. Once Metabase is fully started you'll see a confirmation such as:

``` highlight
...
06-19 10:29:34 INFO metabase.task :: Initializing task CheckForNewVersions
06-19 10:29:34 INFO metabase.task :: Initializing task SendAnonymousUsageStats
06-19 10:29:34 INFO metabase.task :: Initializing task SendAbandomentEmails
06-19 10:29:34 INFO metabase.task :: Initializing task SendPulses
06-19 10:29:34 INFO metabase.task :: Initializing task SendFollowUpEmails
06-19 10:29:34 INFO metabase.task :: Initializing task TaskHistoryCleanup
06-19 10:29:34 INFO metabase.core :: Metabase Initialization COMPLETE
```

At this point you're ready to go! You can access your new Metabase server on port 3000, most likely at `http://localhost:3000`.

You can use another port than 3000 by setting the `MB_JETTY_PORT` [environment variable](../configuring-metabase/environment-variables) before running the jar.

If you are using a Pro or Enterprise version of Metabase, be sure to [activate your license](../installation-and-operation/activating-the-enterprise-edition).

## Production installation

The steps are similar to those steps above with two important differences: if you want to run Metabase in production, you'll want to:

-   Use a [production application database](#production-application-database) to store your Metabase application data.
-   Run [Metabase as a service](#running-the-metabase-jar-as-a-service).

If you'd prefer to use Docker, check out [running Metabase on Docker](running-metabase-on-docker).

### Production application database

Here are some [databases we support](migrating-from-h2#supported-databases-for-storing-your-metabase-application-data).

For example, say you want to use [PostgreSQL](https://www.postgresql.org/). You would get a PostgreSQL service up and running and create an empty database:

``` highlight
createdb metabaseappdb
```

You can call your app db whatever you want. And there's no need to create any tables in that database; Metabase will do that for you. You'll just need to set environment variables for Metabase to use on startup so Metabase knows how to connect to this database.

You'll create a directory for your Metabase like in the steps listed above for the [Local installation](#local-installation), but when it's time to run the `java --add-opens java.base/java.nio=ALL-UNNAMED -jar` command to start up the JAR, you'll prefix the command with some environment variables to tell Metabase how to connect to the `metabaseappdb` you created:

``` highlight
export MB_DB_TYPE=postgres
export MB_DB_DBNAME=metabaseappdb
export MB_DB_PORT=5432
export MB_DB_USER=username
export MB_DB_PASS=password
export MB_DB_HOST=localhost
java --add-opens java.base/java.nio=ALL-UNNAMED -jar metabase.jar
```

The above command would connect Metabase to your Postgres database, `metabaseappdb` via `localhost:5432` with the user account `username` and password `password`. If you're running Metabase as a service, you'll put these environment variables in a separate configuration file.

### Running the Metabase JAR as a service

If you need to run the JAR in production, you should run Metabase as a service. Running Metabase as a service will:

-   Make sure Metabase runs automatically (and stay running).
-   Allow you to run Metabase with an unprivileged user (which is good for security).

The exact instructions for how to run Metabase as a service will differ depending on your operating system. For an example of how to set up Metabase as a service, check out [Running Metabase as a systemd service](./running-metabase-as-service).

### Migrating to a production installation

If you've been running Metabase with the default H2 application database and your team has already created questions, dashboards, collections and so on, you'll want to migrate that data to a production application database. And the sooner you do, the better. See [Migrating from the H2 database](migrating-from-h2).

## Troubleshooting

If you run into any problems during installation, check out our [troubleshooting page](../troubleshooting-guide/running).

## Upgrading Metabase

See [Upgrading Metabase](upgrading-metabase).

## Setting up Metabase

Now that you've installed Metabase, it's time to [set it up and connect it to your database](../configuring-metabase/setting-up-metabase).

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/installation-and-operation/running-the-metabase-jar-file.md) ]
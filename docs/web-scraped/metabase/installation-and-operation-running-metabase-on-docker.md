# Source: https://www.metabase.com/docs/latest/installation-and-operation/running-metabase-on-docker

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

# Running Metabase on Docker

> To get fast, reliable, and secure deployment with none of the work or hidden costs that come with self-hosting, check out [Metabase Cloud](/cloud/).

Metabase provides an official Docker image via Docker Hub that can be used for deployments on any system that is running Docker.

If you're trying to upgrade your Metabase version on Docker, check out these [upgrading instructions](upgrading-metabase).

## Open Source quick start

Use this quick start to run the Open Source version of Metabase locally. See below for instructions on [running Metabase in production](#production-installation).

Assuming you have [Docker](https://www.docker.com/) installed and running, get the latest Docker image:

``` highlight
docker pull metabase/metabase:latest
```

Then start the Metabase container:

``` highlight
docker run -d -p 3000:3000 --name metabase metabase/metabase
```

This will launch an Metabase server on port 3000 by default.

Optional: to view the logs as your Open Source Metabase initializes, run:

``` highlight
docker logs -f metabase
```

Once startup completes, you can access your Open Source Metabase at `http://localhost:3000`.

To run your Open Source Metabase on a different port, say port 12345:

``` highlight
docker run -d -p 12345:3000 --name metabase metabase/metabase
```

## Pro or Enterprise quick start

Use this quick start if you have a [license token](../installation-and-operation/activating-the-enterprise-edition) for a [Pro or Enterprise version](/pricing/) of Metabase, and you want to run Metabase locally. See below for instructions on [running Metabase in production](#production-installation).

Assuming you have [Docker](https://www.docker.com/) installed and running, get the latest Docker image:

``` highlight
docker pull metabase/metabase-enterprise:latest
```

Then start the Metabase container:

``` highlight
docker run -d -p 3000:3000 --name metabase metabase/metabase-enterprise
```

This will launch a Metabase server on port 3000 by default.

Optional: to view the logs as Metabase initializes, run:

``` highlight
docker logs -f metabase
```

Once startup completes, you can access your Pro or Enterprise Metabase at `http://localhost:3000`.

To run your Pro or Enterprise Metabase on a different port, say port 12345:

``` highlight
docker run -d -p 12345:3000 --name metabase metabase/metabase-enterprise
```

## Production installation

Metabase ships with an embedded H2 database that uses the file system to store its own application data. Meaning, if you remove the container, you'll lose your Metabase application data (your questions, dashboards, collections, and so on).

If you want to run Metabase in production, you'll need store your application data in a [production-ready database](./migrating-from-h2#supported-databases-for-storing-your-metabase-application-data).

Once you've provisioned a database, like Postgres, for Metabase to use to store its application data, all you need to do is provide Metabase with the connection information and credentials so Metabase can connect to it.

### Running Docker in production

Let's say you set up a Postgres database by running:

``` highlight
createdb metabaseappdb
```

No need to add any tables; Metabase will create those on startup. And let's assume that database is accessible via `my-database-host:5432` with username `name` and password `password`.

Here's an example Docker command that tells Metabase to use that database:

``` highlight
docker run -d -p 3000:3000 \
  -e "MB_DB_TYPE=postgres" \
  -e "MB_DB_DBNAME=metabaseappdb" \
  -e "MB_DB_PORT=5432" \
  -e "MB_DB_USER=name" \
  -e "MB_DB_PASS=password" \
  -e "MB_DB_HOST=my-database-host" \
   --name metabase metabase/metabase
```

Keep in mind that Metabase will be connecting from *within* your Docker container, so make sure that either: a) you're using a fully qualified hostname, or b) that you've set a proper entry in your container's `/etc/hosts file`.

## Migrating to a production installation

If you've already been running Metabase with the default application database (H2), and want to use a production-ready application database without losing your app data (your questions, dashboards, etc), see [Migrating from H2 to a production database](migrating-from-h2).

## Example Docker compose YAML file

Here's an example `docker-compose.yml` file for running Metabase with a PostgreSQL database `metabaseappdb`:

> This is an example file and is not meant to be used when running Metabase in a production environment. Please refer to our guide about [How to run Metabase in production](/learn/metabase-basics/administration/administration-and-operation/metabase-in-production)

``` highlight
services:
  metabase:
    image: metabase/metabase:latest
    container_name: metabase
    hostname: metabase
    volumes:
      - /dev/urandom:/dev/random:ro
    ports:
      - 3000:3000
    environment:
      MB_DB_TYPE: postgres
      MB_DB_DBNAME: metabaseappdb
      MB_DB_PORT: 5432
      MB_DB_USER: metabase
      MB_DB_PASS: mysecretpassword
      MB_DB_HOST: postgres
    networks:
      - metanet1
    healthcheck:
      test: curl --fail -I http://localhost:3000/api/health || exit 1
      interval: 15s
      timeout: 5s
      retries: 5
  postgres:
    image: postgres:16
    container_name: postgres
    hostname: postgres
    environment:
      POSTGRES_USER: metabase
      POSTGRES_DB: metabaseappdb
      POSTGRES_PASSWORD: mysecretpassword
    volumes:
      - ./pg_data:/var/lib/postgresql/data
    networks:
      - metanet1
networks:
  metanet1:
    driver: bridge
```

## Additional Docker maintenance and configuration

-   [Customizing the Metabase Jetty server](#customizing-the-metabase-jetty-server)
-   [Docker-specific environment variables](#docker-specific-environment-variables)
-   [Setting the Java Timezone](#setting-the-java-timezone)
-   [Copying the application database](#copying-the-application-database)
-   [Mounting a mapped file storage volume](#mounting-a-mapped-file-storage-volume)
-   [Getting your config back if you stopped your container](#getting-your-config-back-if-you-stopped-your-container)
-   [Adding external dependencies or plugins](#adding-external-dependencies-or-plugins)
-   [Use Docker Secrets to hide sensitive parameters](#use-docker-secrets-to-hide-sensitive-parameters)
-   [Troubleshooting](#troubleshooting)
-   [Continue to setup](#continue-to-setup)

### Customizing the Metabase Jetty server

You can use any of the custom settings from [Customizing the Metabase Jetty Webserver](../configuring-metabase/customizing-jetty-webserver) by setting environment variables in your Docker run command.

### Docker-specific environment variables

In addition to the standard custom settings there are two docker specific environment variables `MUID` and `MGID` which are used to set the user and group IDs used by metabase when running in a docker container. These settings make it possible to match file permissions when files, such as the application database, are shared between the host and the container.

Here's how to use a database file, owned by your account and stored in your home directory:

``` highlight
docker run -d -v ~/my-metabase-db:/metabase.db --name metabase -e MB_DB_FILE=/metabase.db -e MUID=$UID -e MGID=$GID -p 3000:3000 metabase/metabase
```

### Setting the Java Timezone

It's best to set your Java timezone to match the timezone you'd like all your reports to come in. You can do this by simply specifying the `JAVA_TIMEZONE` environment variable which is picked up by the Metabase launch script. For example:

``` highlight
docker run -d -p 3000:3000 \
  -e "JAVA_TIMEZONE=US/Pacific" \
  --name metabase metabase/metabase
```

### Copying the application database

The default location for the application database in the container is `/metabase.db/metabase.db.mv.db`. You can copy this directory out of the container using the following command (replacing `CONTAINER_ID` with the actual container ID or name, `metabase` if you named the container):

``` highlight
docker cp CONTAINER_ID:/metabase.db ./
```

The DB contents will be left in a directory named metabase.db.

### Mounting a mapped file storage volume

To persist your data outside of the container and make it available for use between container launches, we can mount a local file path inside our container.

``` highlight
docker run -d -p 3000:3000 \
  -v ~/metabase-data:/metabase-data \
  -e "MB_DB_FILE=/metabase-data/metabase.db" \
  --name metabase metabase/metabase
```

When you launch your container, Metabase will use the database file (`MB_DB_FILE`) at `~/metabase-data/metabase.db` instead of its default location. and we are mounting that folder from our local filesystem into the container.

### Getting your config back if you stopped your container

If you've previously run and configured your Metabase using the local Database and then stopped the container, your data will still be there unless you deleted the container with the `docker rm` command. To recover your previous configuration:

#### 1. Find the stopped container using the `docker ps -a` command. It will look something like this: 

``` highlight
docker ps -a | grep metabase
    ca072cd44a49        metabase/metabase        "/app/run_metabase.sh"   About an hour ago   Up About an hour          0.0.0.0:3000->3000/tcp   metabase
    02e4dff057d2        262aa3d0f714             "/app/run_metabase.sh"   23 hours ago        Exited (0) 23 hours ago                            pedantic_hypatia
    0d2170d4aa4a        262aa3d0f714             "/app/run_metabase.sh"   23 hours ago        Exited (0) 23 hours ago                            stoic_lumiere
```

Once you have identified the stopped container with your configuration in it, save the container ID from the left most column for the next step.

#### 2. Use `docker commit` to create a new custom docker image from the stopped container containing your configuration. 

``` highlight
docker commit ca072cd44a49 mycompany/metabase-custom
sha256:9ff56186de4dd0b9bb2a37c977c3a4c9358647cde60a16f11f4c05bded1fe77a
```

#### 3. Run your new image using `docker run` to get up and running again. 

``` highlight
docker run -d -p 3000:3000 --name metabase mycompany/metabase-custom
430bb02a37bb2471176e54ca323d0940c4e0ee210c3ab04262cb6576fe4ded6d
```

You should have your previously configured Metabase Installation back. If it's not the one you expected, try a different stopped container and repeat these steps.

### Adding external dependencies or plugins

To add external dependency JAR files, such as the Oracle or Vertica JDBC drivers or 3rd-party Metabase drivers), you'll need to:

-   create a `plugins` directory in your host system, and
-   bind that directory so it's available to Metabase as the path `/plugins` (using either `--mount` or `-v`/`--volume`).

For example, if you have a directory named `/path/to/plugins` on your host system, you can make its contents available to Metabase using the `--mount` option as follows:

``` highlight
docker run -d -p 3000:3000 \
  --mount type=bind,source=/path/to/plugins,destination=/plugins \
  --name metabase metabase/metabase
```

Note that Metabase will use this directory to extract plugins bundled with the default Metabase distribution (such as drivers for various databases such as SQLite), thus it must be readable and writable by Docker.

### Use Docker Secrets to hide sensitive parameters

In order to keep your connection parameters hidden from plain sight, you can use Docker Secrets to put all parameters in files so Docker can read and load them in memory before it starts the container.

Here is an example `docker-compose.yml` file to start a Metabase Docker container with secrets to connect to a PostgreSQL database.

In addition to this example yml file, you'll need to create two files:

-   `db_user.txt`
-   `db_password.txt`

These files should be in the same directory as the `docker-compose.yml`. Put the `db_user` in the `db_user.txt` file, and db_password in the `db_password.txt` file.

Notice the "\_FILE" on the environment variables that have a secret:

``` highlight
services:
  metabase:
    image: metabase/metabase:latest
    container_name: metabase
    hostname: metabase
    volumes:
      - /dev/urandom:/dev/random:ro
    ports:
      - 3000:3000
    environment:
      MB_DB_TYPE: postgres
      MB_DB_DBNAME: metabase
      MB_DB_PORT: 5432
      MB_DB_USER_FILE: /run/secrets/db_user
      MB_DB_PASS_FILE: /run/secrets/db_password
      MB_DB_HOST: postgres
    networks:
      - metanet1
    secrets:
      - db_password
      - db_user
    healthcheck:
      test: curl --fail -I http://localhost:3000/api/health || exit 1
      interval: 15s
      timeout: 5s
      retries: 5
  postgres:
    image: postgres:latest
    container_name: postgres
    hostname: postgres
    environment:
      POSTGRES_USER_FILE: /run/secrets/db_user
      POSTGRES_DB: metabase
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    networks:
      - metanet1
    secrets:
      - db_password
      - db_user
networks:
  metanet1:
    driver: bridge
secrets:
  db_password:
    file: db_password.txt
  db_user:
    file: db_user.txt
```

We currently support the following [environment variables](../configuring-metabase/environment-variables) to be used as secrets:

-   `MB_DB_USER`
-   `MB_DB_PASS`
-   `MB_DB_CONNECTION_URI`
-   `MB_EMAIL_SMTP_PASSWORD`
-   `MB_EMAIL_SMTP_USERNAME`
-   `MB_LDAP_PASSWORD`
-   `MB_LDAP_BIND_DN`

In order for the Metabase container to read the files and use the contents as a secret, the environment variable name needs to be appended with a "\_FILE" as explained above.

> This is an example file and is not meant to be used when running Metabase in a production environment. Please refer to our guide about [How to run Metabase in production](/learn/metabase-basics/administration/administration-and-operation/metabase-in-production).

## Troubleshooting

See Running Metabase in the [Troubleshooting guide](../troubleshooting-guide/running).

## Continue to setup

Now that you've installed Metabase, it's time to [set it up and connect it to your database](../configuring-metabase/setting-up-metabase).

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/installation-and-operation/running-metabase-on-docker.md) ]
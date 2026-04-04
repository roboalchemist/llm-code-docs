# Source: https://render.com/docs/deploy-mysql.md

# Deploy MySQL

[MySQL](https://www.mysql.com) is a popular database powering many of the highest traffic sites in the world. [Render Disks](disks) make it effortless to deploy production-grade MySQL on Render backed by *high performance SSDs* with [automatic daily snapshots](disks#disk-snapshots).

Render [private services](private-services) are only visible to other Render services in your workspace. They have internal URLs like `mysql:3306`, can speak any protocol and can listen on any port. Render automatically detects the ports for your services when they are deployed.

Let's get started!

## MySQL Versions

The `master` branch for Render's [MySQL repo](https://github.com/render-examples/mysql) runs *MySQL 8*. If you need *MySQL 5*, make sure to select the `mysql-5` branch when you create your service below.

> If you are using MySQL as the database for a production [Ghost 5](/deploy-ghost) deployment on Render, you must use MySQL 8 for your production database.

## One-Click Deploy

Click *Deploy to Render* below and follow the prompts to set up MySQL on Render.

<deploy-to-render repo="https://github.com/render-examples/mysql">
</deploy-to-render>

## Manual Deploy

1. Fork [render-examples/mysql](https://github.com/render-examples/mysql) on GitHub or click the green 'Use this template' button.

2. Create a new *private service* on Render, and give Render permission to access your new repo.

> Pick the `mysql-5` branch in this step if you want to deploy *MySQL 5*.

3. Set the service's *Language* field to `Docker` and add the following environment variables:

   | Key                   | Value                                           |
   | --------------------- | ----------------------------------------------- |
   | `MYSQL_DATABASE`      | `my_database` (or your preferred database name) |
   | `MYSQL_USER`          | `mysql` (or your preferred DB username)         |
   | `MYSQL_PASSWORD`      | A secure password for `MYSQL_USER`              |
   | `MYSQL_ROOT_PASSWORD` | A secure password for the MySQL `root` user     |

4. Add a Disk under *Advanced* with the following values:

|                |                                                              |
| -------------- | ------------------------------------------------------------ |
| *Mount Path* | `/var/lib/mysql` *(required)*                              |
| *Size*       | `10 GB` Feel free to change this to match your requirements. |

> The MySQL Docker image writes data to `/var/lib/mysql`. The *Mount Path* must match this exactly. Setting a different *Mount Path* does not change the MySQL configuration, and will result in lost data.

That's it! Save your private service to bring up MySQL which will take a few minutes to start. Future deploy should be much faster.

Your MySQL instance will be available on the displayed URL as soon as the deploy is live. The URL should look like `mysql-foo:3306`.

[image: MySQL]

## Connecting to your database

You can connect to MySQL from other applications running in your Render workspace using the name and port for your private service. For example, you can a create a Web Service to manage your MySQL database using [Adminer](https://www.adminer.org/). See our [Adminer Deployment Guide](/deploy-adminer) for details.

You can also use [SSH](ssh) or the shell in your dashboard to connect to your database.

Learn more about [connecting to MySQL](https://dev.mysql.com/doc/refman/8.0/en/connectors-apis.html).

```shell{outputLines:2-100}
mysql -h localhost -D $MYSQL_DATABASE -u $MYSQL_USER --password=$MYSQL_PASSWORD

mysql: [Warning] Using a password on the command line interface can be insecure.
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 92
Server version: 8.0.29 MySQL Community Server - GPL

Copyright (c) 2000, 2021, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```

## Backups

> Relying on a [disk snapshot](disks#disk-snapshots) to restore a database is not recommended. Restoring a disk snapshot will likely result in corrupted or lost database data.

Using a database’s recommended backup tool (for example: [mysqldump](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html)) is the recommended way to backup and restore a database without corrupted or lost data.
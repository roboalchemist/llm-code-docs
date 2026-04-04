# Source: https://docs.upsun.com/learn/tutorials/restrict-service-access.md

# Restrict access to a service

Upsun allows you to restrict access to a service.

In this tutorial, learn how to grant your Data team `read-only` access to your production database.

## Before you start

You need:

- A project with a database service
- A `viewer` user on your project

## 1. Add a read-only endpoint to your database service

Edit your `.upsun/config.yaml` file and add the following [endpoints](https://docs.upsun.com/add-services/mysql/_index.md#define-permissions):

- `website` with `admin` access to the `main` database
- `reporting` with read-only `ro` access to the `main` database

```yaml  {location=".upsun/config.yaml"}
services:
  maindb:
    type: mariadb:11.8
    configuration:
      schemas:
        - main
      endpoints:
        website:
          default_schema: main
          privileges:
            main: admin
        reporting:
          privileges:
            main: ro
```

## 2. Grant your app access to the new endpoints

Edit your app configuration and add new relationships to your new endpoints:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    # ...
    relationships:
      database:
        service: maindb
        endpoint: website
      reports:
        service: maindb
        endpoint: reporting
```

## 3. Create a worker with access to the read-only endpoint

Edit your app configuration to add a new worker which:

- Does nothing (`sleep infinity`)
- Can access the read-only `reporting` endpoint
- Allows SSH access to `viewer`

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    workers:
      data_access:
        mounts: {}
        commands:
          start: |
            sleep infinity
        relationships:
          reports:
            service: maindb
            endpoint: reporting
        access:
          ssh: viewer
```

You're done!
From now on, your `viewer` users can SSH in to the worker application,
and connect to your database with read-only permissions.


# Source: https://herd.laravel.com/docs/macos/herd-pro-services/postgresql.md

> ## Documentation Index
> Fetch the complete documentation index at: https://herd.laravel.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# PostgreSQL

# Installing PostgreSQL via Herd Pro

PostgreSQL is a powerful, open-source object-relational database system that is known for its reliability and robustness.
Laravel Herd Pro extends PostgreSQL by providing a number of popular extensions:

* [PostGIS](https://postgis.net/) - adds support for geographic objects to the PostgreSQL database, making it easy to store and query spatial data.
* [pgrouting](https://pgrouting.org/) - adds routing functionality to PostgreSQL, allowing you to calculate the shortest path between two points.
* [pgvector](https://github.com/pgvector/pgvector) - a vector similarity search extension for PostgreSQL, which allows you to search for (among other things) OpenAI embeddings in your database.

<Frame>
  <img alt="Screenshot of PostgreSQL settings" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-postgresql.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=bc79104b778b7c618e2a6a0867e44aff" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/setup-postgresql.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-postgresql.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=8afac0656461906d9a4e9c7c6b5a1007 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-postgresql.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=a6d405362d29fa212969c6fbf83ccb3e 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-postgresql.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=4f48bce811fc67773149d1347aea63c1 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-postgresql.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=4754847fd67c5b9ad15985c0c74c5365 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-postgresql.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=5fbdcb46e195c58fc671b8a5be97de22 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-postgresql.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=fbba81c1a21738ec88f36d71ac3ea1b1 2500w" />
</Frame>

## Configuration

Herd uses a common default configuration for your PostgreSQL instance that works seamlessly for most setups, and you can change the port of the service to run it in parallel to existing installations on your machine.

Enabling the autostart option automatically starts a service instance when you start Herd.

If you want to modify the settings of the database, you can right-click the service in the settings and open its data directory. In this data directory, there is a `postgresql.conf` that this specific PostgreSQL instance loads on startup.

Make sure to restart the service if you make changes to this configuration.

## Creating databases

Before you can connect your application to the database service, you need an actual database within the instance of the service. Herd provides a convenient way to open TablePlus or AdminerEvo in case that you don't use TablePlus.

When clicking on the related button for these tools on the right side of the service details, Herd opens a connection to the database in your preferred tool and automatically logs you in.

<Frame>
  <img alt="MySQL Sidebar" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_postgresql.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=ecc2e3add8e7a47fcff20c13895dd489" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/settings_services_postgresql.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_postgresql.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=fd6a02c06c9c80cd1ee13ed040cbd1ef 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_postgresql.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=df764f595d984c126b17c66d7d8c5248 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_postgresql.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=1efbcb16d40a2ddb94ceb32905beb3f3 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_postgresql.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=4ec8cd5912c36cce01197526930e5635 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_postgresql.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=67d9f57ceac95d4fceee4645e1d72095 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_postgresql.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=4ca42b754b308c74f2dfd27f50783721 2500w" />
</Frame>

## Connecting from your Laravel application

To connect it within your application, you can use the credentials that are listed next to the running service in the settings, or you can use the ones below.

```env  theme={null}
DB_CONNECTION=pgsql
DB_HOST=127.0.0.1
DB_PORT=5432
DB_DATABASE=laravel # set this to your project database
DB_USERNAME=root
DB_PASSWORD=
```

## Database service migrations

Whether you set up a newer version of PostgreSQL or migrate from existing instances on your machine, the most comfortable way is to use a database client like [TablePlus](https://tableplus.com/) to export and import the database tables.

## Versions

Herd Pro allows you to install the following versions directly from the services tab of the settings. New versions are available regularly.

| Service    | Version |
| ---------- | ------- |
| PostgreSQL | 14.x    |
| PostgreSQL | 15.x    |
| PostgreSQL | 16.x    |
| PostgreSQL | 17.x    |

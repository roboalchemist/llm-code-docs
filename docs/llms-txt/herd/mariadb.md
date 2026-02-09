# Source: https://herd.laravel.com/docs/macos/herd-pro-services/mariadb.md

> ## Documentation Index
> Fetch the complete documentation index at: https://herd.laravel.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MariaDB

# Installing MariaDB via Herd Pro

MariaDB is a drop-in, fully compatible replacement for MySQL, and it's the default database engine for many Linux distributions. Many popular hosting platforms like [Laravel Forge](https://forge.laravel.com) support MariaDB databases out of the box, making the switch from local to production a breeze.

<Frame>
  <img alt="Screenshot of MySQL settings" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-mariadb.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=a5d392bf631c3aa8b9a4135c465c8a86" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/setup-mariadb.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-mariadb.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=9c4610815f1eee56a993bcd7ca89a9da 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-mariadb.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=9804affd57620035855bb95939d88f1e 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-mariadb.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=31f8b7730d02b0e87de2f27fbc80c5c1 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-mariadb.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=2a19b39065e4a22116c8cd22d37dbc15 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-mariadb.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=c7f5d19b0b778a34e15ee5a44b0ce954 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-mariadb.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=c87efa27093044b5760830c4614520f0 2500w" />
</Frame>

## Configuration

Herd provides a sensible default configuration for your MariaDB instance that works seamlessly for new setups, and you can change the port of the service to run it in parallel to existing installations on your machine.

Enabling the autostart option automatically starts a service instance when you start Herd.

If you want to modify the settings of the database, you can right click the service in the settings and open its data directory. In this data directory, there is a `my.cnf` that this specific MariaDB instance loads on startup.

Make sure to restart the service if you make changes to this configuration.

## Creating databases

While Laravel applications can create a database when running the migrations for the first time, it's a good practice to set up the database within the database instance yourself.

The service details on the right side of the selected service allow you to open TablePlus or AdminerEvo with a single click. Herd automatically detects TablePlus on your machine and provides a connection string to access the database instance. If you don't use TablePlus, it opens AdminerEvo where it inserts the correct login credentials for you.

<Frame>
  <img alt="MariaDB Sidebar" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mariadb.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=462afebaf471423a072e27ccf437f233" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/settings_services_mariadb.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mariadb.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=8741f6bd32f987383137926b26a11528 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mariadb.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=b779e3143501e4fc52c5e797c2f1f18d 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mariadb.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=5a94e5cb096f06562f4929bec3b7a1d8 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mariadb.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=9c2ccb0a0a8ee218ebf778bd19aa739e 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mariadb.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=0cb6ea5e270264a33526e20706f06503 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mariadb.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=0944dbe72a47a0ca7f99dcb051e2f56b 2500w" />
</Frame>

## Connecting from your Laravel application

To connect your application to the server, you can use the credentials that are listed next to the running service in the settings, or you can use the ones below.

```env  theme={null}
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3307
DB_DATABASE=laravel # set this to your project database
DB_USERNAME=root
DB_PASSWORD=
```

## Database service migrations

Whether you set up a newer version of MariaDB or migrate from existing instances on your machine, the most comfortable way is to use a database client like [TablePlus](https://tableplus.com/) to export and import the database tables.

## Connecting via CLI

Herd symlinks the `mariadb` CLI to your PATH, so you can connect to the database via the command line.
As Laravel Herd allows you to start multiple MariaDB servers, you should specify the port to connect to the correct instance.

For example, to connect to the MariaDB server running on port 3306, you can use the following command:

```bash  theme={null}
mariadb -u root -h 127.0.0.1 -P 3306 -p
```

## Versions

Herd Pro allows you to install the following versions directly from the services tab of the settings. New versions are available regularly.

| Service | Version |
| ------- | ------- |
| MariaDB | 10.11.6 |

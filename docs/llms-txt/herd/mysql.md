# Source: https://herd.laravel.com/docs/macos/herd-pro-services/mysql.md

# MySQL

# Installing MySQL via Herd Pro

MySQL is the most popular relational database engine for web development, and setting up a database server with a few clicks makes it incredibly easy to follow tutorials or get up and running with a professional setup in minutes. Many popular hosting platforms like [Laravel Forge](https://forge.laravel.com) support MySQL databases out of the box, making the switch from local to production a breeze.

If you are new to Laravel and want to move from SQLite to a database service, MySQL is the best choice for most applications.

<Frame>
  <img alt="Screenshot of MySQL settings" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-mysql.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=d69ab65c52b0d79a18f8582e4ecbc59d" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/setup-mysql.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-mysql.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=daecc665a758ac3b4f5c6228e2d48db9 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-mysql.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=7e61d98b0fc8aa0bf4c89d4ee7ab541c 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-mysql.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=5cc01e9eaf08836fbe4d15d2be67de9d 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-mysql.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=cdffe8c5c1bc018530e882fcc8d60f2f 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-mysql.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=a62cc97354c83f873b5d76f189e2ed59 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-mysql.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=2337900e88da64d2fcda3fe0771d16f6 2500w" />
</Frame>

## Configuration

Herd provides a sensible default configuration for your MySQL instance that works seamlessly for new setups, and you can change the port of the service to run it in parallel to existing installations on your machine.

Enabling the autostart option automatically starts a service instance when you start Herd.

If you want to modify the settings of the database, you can right click the service in the settings and open its data directory. In this data directory, there is a `my.cnf` that this specific MySQL instance loads on startup.

Make sure to restart the service if you make changes to this configuration.

## Creating databases

While Laravel applications can create a database when running the migrations for the first time, it's a good practice to set up the database within the database instance yourself.

The service details on the right side of the selected service allow you to open TablePlus or AdminerEvo with a single click. Herd automatically detects TablePlus on your machine and provides a connection string to access the database instance. If you don't use TablePlus, it opens AdminerEvo where it inserts the correct login credentials for you.

<Frame>
  <img alt="MySQL Sidebar" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mysql.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=881d70dcb9912411b9da399de9ca89be" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/settings_services_mysql.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mysql.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=16cad02f11777f61b74953fe8ca5b8a7 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mysql.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=a9facd40370b8b19a60c6fb2aa491685 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mysql.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=98a745314da488df10b01fe9772421d5 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mysql.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=635f78a8a5e90e6209938f41b49bf317 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mysql.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=fe9ac0593e0f82029ab58a6e0c9298c3 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mysql.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=264296cb906146a29775621d11bfad97 2500w" />
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

Whether you set up a newer version of MySQL or migrate from existing instances on your machine, the most comfortable way is to use a database client like [TablePlus](https://tableplus.com/) to export and import the database tables.

## Connecting via CLI

Herd symlinks the `mysql` CLI to your PATH, so you can connect to the database via the command line.
As Laravel Herd allows you to start multiple MySQL servers, you should specify the port to connect to the correct instance.

For example, to connect to the MySQL server running on port 3306, you can use the following command:

```bash  theme={null}
mysql -u root -h 127.0.0.1 -P 3306 -p
```

## Versions

Herd Pro allows you to install the following versions directly from the services tab of the settings. New versions are available regularly.

| Service | Version |
| ------- | ------- |
| MySQL   | 8.4.\*  |
| MySQL   | 8.0.36  |

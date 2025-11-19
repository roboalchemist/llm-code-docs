# Source: https://herd.laravel.com/docs/macos/herd-pro-services/mongodb.md

# MongoDB

# Installing MongoDB via Herd Pro

You can install the [MongoDB Community Edition](https://www.mongodb.com/products/self-managed/community-edition) from the service management section of the settings. This uses the MongoDB PHP extension and allows a seamless use of MongoDB in your application during development.

<Frame>
  <img alt="Screenshot of MongoDB settings" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mongodb.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=30da82302d5bd9a0fff9bb5760cc3ba8" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/settings_services_mongodb.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mongodb.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=cfc310cad3460bc7af1043241835bf6d 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mongodb.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=41d16e27801de5fb9c104015e3560929 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mongodb.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=fb3b143c48826de1e85d085eb16d574f 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mongodb.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=f40ca6246dbc22379d3f893ced199df5 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mongodb.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=e28132690607ea6b1cccd51e4e15d401 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mongodb.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=eb2686f2853eb557ae2bf5a7dda3fe4a 2500w" />
</Frame>

## Configuration

Herd starts your MongoDB instance with sensible defaults that work great for new setups, and you can change the port of the service to run it in parallel to existing installations on your machine.

If you want to modify the settings of the service, you can right-click on the service in the settings and open its data directory. In this data directory, there is a `mongodb.conf` that this MongoDB instance loads on startup.

Make sure to restart the service if you make changes to this configuration.

## Creating databases

You can create databases in your MongoDB instance by using the tooling that you can download on the [official website](https://www.mongodb.com/docs/database-tools/) or use tools like TablePlus that work with a variety of database engines.

## Connecting from your Laravel application

In order to use MongoDB in combination with Laravel, you may use the `mongodb/laravel-mongodb` composer package.

Run the following command to add the dependency to your application:

```bash  theme={null}
composer require mongodb/laravel-mongodb
```

To connect your application to the database server, you can use the credentials that are listed next to the running service in the settings, or you can use the ones below.
Add these settings to your `.env` file.

```env  theme={null}
DB_CONNECTION=mongodb
DB_PORT=27020
DB_URI="mongodb://127.0.0.1:27020/laravel"
```

Please refer to the [Laravel MongoDB](https://www.mongodb.com/docs/drivers/php/laravel-mongodb/current/quick-start/download-and-install/#add-laravel-mongodb-to-the-dependencies) documentation for additional help.

## Database service migrations

Whether you set up a newer version of MongoDB or migrate from existing instances on your machine, the most comfortable way is to use a database client like [TablePlus](https://tableplus.com/) to export and import the database tables.

## Versions

Herd Pro allows you to install the following versions directly from the services tab of the settings. New versions are available regularly.

| Service | Version |
| ------- | ------- |
| MongoDB | 7.0.12  |

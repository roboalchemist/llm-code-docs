# Source: https://planetscale.com/docs/vitess/tutorials/connect-laravel-app.md

# Connect a Laravel application to PlanetScale

> In this tutorial, you'll learn how to connect a Laravel 12 application to a PlanetScale MySQL database using a sample Laravel starter app.

## Prerequisites

* [PHP](https://www.php.net/manual/en/install.php) — This tutorial uses `v8.2`
* [Composer](https://getcomposer.org/)
* A [PlanetScale account](https://auth.planetscale.com/sign-up)

## Set up the Laravel app

This guide will integrate [a simple Laravel 12 app](https://github.com/planetscale/planetscale-laravel-mysql) with PlanetScale. The application displays a list of users from your PlanetScale database. The sample repo contains migrations and seed data to create and populate the `users` table. If you have an existing application, you can also use that.

<Steps>
  <Step>
    Clone the starter Laravel application:

    ```bash  theme={null}
    git clone https://github.com/planetscale/planetscale-laravel-mysql.git
    ```
  </Step>

  <Step>
    Enter into the folder and install the dependencies:

    ```bash  theme={null}
    cd planetscale-laravel-mysql
    composer install
    ```

    You may need to run `composer update` if you haven't updated in a while.
  </Step>

  <Step>
    Copy the `.env.example` file into `.env` and generate the app key:

    ```bash  theme={null}
    cp .env.example .env
    php artisan key:generate
    ```
  </Step>
</Steps>

## Set up the database

Next, you need to set up your PlanetScale database and connect to it in the Laravel application.

<Note>
  If you have an existing cloud-hosted database, you can choose the "**Import**" option to import your database to PlanetScale using our Import tool. If you go this route, we recommend using our [Database Imports documentation](/docs/vitess/imports/database-imports).
</Note>

If this is your first time in the dashboard, you'll be prompted to create an organization and go through the database creation walkthrough. Otherwise, click "**New database**" > "**Create new database**".

* **Name** — You can use any name with lowercase, alphanumeric characters, or underscores. We also permit dashes, but don't recommend them, as they may need to be escaped in some instances.
* **Region** — Choose the [region](/docs/vitess/regions#available-regions) closest to you or your application. It's important to note if you intend to make this branch a production branch, you will not be able to change the region later, so choose the region with this in mind.
* **Storage option** — Choose a storage option. You can choose between network-attached storage or [Metal](/docs/metal) for storage. For more information, see the [plans documentation](/docs/vitess/tutorials/connect-laravel-app).
* **Cluster size** — Select the [desired cluster size](/docs/planetscale-plans) for your database.

Finally, click "**Create database**".

A [production branch](/docs/vitess/schema-changes/branching), `main`, is automatically created when you create your database. [Safe migrations](/docs/vitess/schema-changes/safe-migrations) are turned off by default, so you can make schema changes directly to this branch. Once you're ready for production, you can turn on safe migrations to protect from accidental schema changes and enable zero-downtime deployments.

That's it! Your database is ready to use. Next, let's connect it to the Laravel application and then add some data.

## Connect to the Laravel app

There are **two ways to connect** to PlanetScale:

* With an auto-generated username and password
* Using the PlanetScale proxy with the CLI

Both options are covered below.

### Option 1: Connect with username and password (Recommended)

First, you need to generate a database username and password so that you can use it to connect to your application.

You'll be presented with this option after creating your database. You can also access the password creation page by clicking "**Connect**" -> "**Create password**".

As long as you're an organization administrator, this will generate a username and password that has administrator privileges to the database.

<Tip>
  If the password value is blurred, you need to click "**New password**" to generate a new one.
</Tip>

Click "Laravel" as the framework, then copy the contents of the `.env` tab and paste them into your own `.env` file in your Laravel application. The structure will look like this:

```bash  theme={null}
DB_CONNECTION=mysql
DB_HOST=<ACCESS HOST URL>
DB_PORT=3306
DB_DATABASE=<DATABASE_NAME>
DB_USERNAME=<USERNAME>
DB_PASSWORD=<PASSWORD>
MYSQL_ATTR_SSL_CA=/etc/ssl/cert.pem
```

For `DB_DATABASE`, you can use your PlanetScale database name directly if you have a *single unsharded keyspace*. If you have a sharded keyspace, you'll need to use `@primary`. This will automatically direct incoming queries to the correct keyspace/shard. For more information, see the [Targeting the correct keyspace documentation](/docs/vitess/sharding/targeting-correct-keyspace).

The `MYSQL_ATTR_SSL_CA` value is platform-dependent. Please refer to our documentation around [how to connect to PlanetScale securely](/docs/vitess/connecting/secure-connections#ca-root-configuration) for the platform you're using.

### Option 2: Connect with the PlanetScale proxy

To connect with the PlanetScale proxy, you need to install and use the [PlanetScale CLI](https://github.com/planetscale/cli).

<Steps>
  <Step>
    Open a connection by running the following:

    ```bash  theme={null}
    pscale connect <DATABASE_NAME> <BRANCH_NAME>
    ```

    If you're following this guide exactly and haven't created any branches, you can use the default branch, `main`.
  </Step>

  <Step>
    A secure connection to your database will be established and you'll see a local address you can use to connect to your application.
  </Step>

  <Step>
    Open the `.env` file in your Laravel app and update it as follows:

    ```bash  theme={null}
    DB_CONNECTION=mysql
    DB_HOST=127.0.0.1
    DB_PORT=3306 # Get this from the output of the previous step
    DB_DATABASE=<DATABASE_NAME>
    DB_USERNAME=
    DB_PASSWORD=
    ```

    The connection uses port `3306` by default, but if that's being used, it will pick a random port. Make sure you paste in whatever port is returned in the terminal. You can leave `DB_USERNAME` and `DB_PASSWORD` blank.
  </Step>
</Steps>

## Run migrations and seeder

Now that you're connected, let's add some data to see it in action. The sample application comes with some default Laravel migration files, `database/migrations/`, to create the database schema. It also contains a user seeder to seed some mock user data.

<Note>
  Laravel uses foreign key constraints by default. PlanetScale, however, has foreign key constraint support turned off by default. For this tutorial, we're keeping the Laravel defaults, so you need to enable [foreign key constraint](/docs/vitess/foreign-key-constraints) support in your database settings page. Click the checkbox next to "Allow foreign key constraints" and press "Save database settings".
</Note>

Let's migrate and seed the database now.

<Steps>
  <Step>
    In the root of the Laravel project, run the following to migrate and seed the database:

    ```bash  theme={null}
    php artisan migrate --seed
    ```
  </Step>

  <Step>
    Start the application:

    ```bash  theme={null}
    php artisan serve
    ```
  </Step>
</Steps>

You can view the application at [http://localhost:8000](http://localhost:8000).

1. Refresh your Laravel homepage and you'll see a list of users.

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/laravel-users.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=5430150ba4ac9f7e1fbef8adf04f1820" alt="Laravel PlanetScale starter app homepage" data-og-width="2956" width="2956" data-og-height="1726" height="1726" data-path="docs/images/laravel-users.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/laravel-users.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=5518d3da4cf8aa17e3502d7ed3c5aead 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/laravel-users.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=8f4d31ac6091c921ae28f5353fcc199a 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/laravel-users.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=77a92b0460cd947aa5fd1ab5d72efef4 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/laravel-users.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=80f5542a3c9108f59cd7c7ea8b8c0436 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/laravel-users.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=9d334cea4af6626d2e0b06c85bdcabc3 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/laravel-users.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=aca493c4bcd5948322e5a9a21ba6211f 2500w" />
</Frame>

## Add data manually

If you want to continue to play around with adding data on the fly, you have a few options:

* PlanetScale [dashboard console](/docs/vitess/web-console)
* [Laravel Tinker](hhttps://laravel.com/docs/12.x/artisan#tinker)
* [PlanetScale CLI shell](/docs/cli/shell)
* Your favorite MySQL client (for a list of tested MySQL clients, review our article on [how to connect MySQL GUI applications](/docs/vitess/tutorials/connect-mysql-gui))

The first option is covered below.

### Add data in PlanetScale dashboard console

PlanetScale has a [built-in console](/docs/vitess/web-console) where you can run MySQL commands against your branches.

By default, web console access to production branches is disabled to prevent accidental deletion. From your database's dashboard page, click on the "**Settings**" tab, check the box labelled "**Allow web console access to production branches**", and click "**Save database settings**".

To access it, click "**Console**" > select your branch > "**Connect**".

From here, you can run MySQL queries and DDL against your database branch.

<Steps>
  <Step>
    Add a record to the `users` table:

    ```sql  theme={null}
    UPDATE users
    SET email = 'cyrus@planetscale.com'
    WHERE id=1;
    ```
  </Step>

  <Step>
    Refresh the Laravel homepage to see the new record. You can also verify it was added in the console with:

    ```sql  theme={null}
    SELECT * FROM users;
    ```

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/laravel-web-console.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=05af89bb7e3461c8d275b78e8fe9797d" alt="PlanetScale web console" data-og-width="2974" width="2974" data-og-height="1836" height="1836" data-path="docs/images/laravel-web-console.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/laravel-web-console.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=af415642ecc7e9746c02507d26aa27e0 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/laravel-web-console.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=32b90fd9157d0060f815d1de717c6262 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/laravel-web-console.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=359c73e3748273530b00e6b27a04d114 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/laravel-web-console.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=826dde1eae6516114b6f8dddad1d639d 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/laravel-web-console.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=4ade12ca71d1fced2c2830c3ae6d73bf 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/laravel-web-console.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=be2d156b6bcad346a93721eb91fb8ded 2500w" />
    </Frame>
  </Step>
</Steps>

## What's next?

Once you're done with initial development, you can enable [safe migrations](/docs/vitess/schema-changes/safe-migrations) to protect from accidental schema changes and enable zero-downtime deployments.

To learn more about PlanetScale, take a look at the following resources:

* [PlanetScale workflow](/docs/vitess/best-practices) — Quick overview of the PlanetScale workflow: branching, non-blocking schema changes, deploy requests, and reverting a schema change.
* [PlanetScale branching](/docs/vitess/schema-changes/branching) — Learn how to utilize branching to ship schema changes with no locking or downtime.
* [PlanetScale CLI](/docs/cli) — Power up your workflow with the PlanetScale CLI. Every single action you just performed in this quickstart (and much more) can also be done with the CLI.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt
# Source: https://planetscale.com/docs/vitess/tutorials/connect-symfony-app.md

# Connect a Symfony application to PlanetScale

> In this tutorial, you'll learn how to connect a Symfony application to a PlanetScale MySQL database using a sample Symfony starter app.

## Prerequisites

* [PHP](https://www.php.net/manual/en/install.php) — This tutorial uses `v8.1`
* [Composer](https://getcomposer.org/)
* A [PlanetScale account](https://auth.planetscale.com/sign-up)
* [PlanetScale CLI](https://github.com/planetscale/cli) — You can also follow this tutorial using just the PlanetScale admin dashboard, but the CLI will make setup quicker.

## Set up the Symfony app

This guide will integrate [a simple Symfony app](https://github.com/planetscale/symfony-example) with PlanetScale that will display a list of products stored in the database. If you have an existing application, you can also use that.

<Steps>
  <Step>
    Clone the starter Symfony application:

    ```bash  theme={null}
    git clone https://github.com/planetscale/symfony-example.git
    ```
  </Step>

  <Step>
    Enter into the folder and install the dependencies:

    ```bash  theme={null}
    cd symfony-example
    composer install
    ```
  </Step>

  <Step>
    Rename the `.env.example` file to `.env.local`:

    ```bash  theme={null}
    mv .env.example .env.local
    ```

    Once you deploy to production, don't forget to update `.env.local` to `.env`.
  </Step>

  <Step>
    Start the application:

    ```bash  theme={null}
    symfony serve
    ```
  </Step>
</Steps>

You can view the application at [http://localhost:8000](http://localhost:8000).

## Set up the database

Next, you need to set up your PlanetScale database and connect to it in the Symfony application.

You can create a database either in the [PlanetScale dashboard](https://app.planetscale.com) or from the PlanetScale CLI. This guide will use the CLI, but you can follow the database setup instructions in the [PlanetScale quickstart guide](/docs/vitess/tutorials/planetscale-quick-start-guide) if you prefer the dashboard.

<Steps>
  <Step>
    Authenticate the CLI with the following command:

    ```bash  theme={null}
    pscale auth login
    ```
  </Step>

  <Step>
    Create a new database with a default `main` branch with the following command:

    ```bash  theme={null}
    pscale database create <DATABASE_NAME> --region <REGION_SLUG>
    ```
  </Step>
</Steps>

This tutorial uses `symfony_example` for `DATABASE_NAME`, but you can use any name with lowercase, alphanumeric characters, or underscores. You can also use dashes, but we don't recommend them, as they may need to be escaped in some instances.

For `REGION_SLUG`, choose a region closest to you from the [available regions](/docs/vitess/regions#available-regions) or leave it blank.

That's it! Your database is ready to use. Next, let's connect it to the Symfony application and then add some data.

## Connect to the Symfony app

There are **two ways to connect** to PlanetScale:

* With an auto-generated username and password
* Using the PlanetScale proxy with the CLI

Both options are covered below.

### Option 1: Connect with username and password (Recommended)

These instructions show you how to use the [PlanetScale CLI](/docs/cli/planetscale-environment-setup) to generate a set of credentials.

You can also get these exact values to to copy/paste from your [PlanetScale dashboard](https://app.planetscale.com). In the dashboard, click on the database > "**Connect**" > "**Generate new password**" > "**General**" dropdown > "**Symfony**". If the password is blurred, click "**New password**". Skip to step 3 once you have these credentials.

<Steps>
  <Step>
    Create a username and password with the PlanetScale CLI by running:

    ```bash  theme={null}
    pscale password create <DATABASE_NAME> <BRANCH_NAME> <PASSWORD_NAME>
    ```

    A default branch, `main`, is created when you create the database, so you can use that for `BRANCH_NAME`.

    <Note>
      The `PASSWORD_NAME` value represents the name of the username and password being generated. You can have multiple
      credentials for a branch, so this gives you a way to categorize them. To manage your passwords in the dashboard, go to
      your database dashboard page, click "Settings", and then click "Passwords".
    </Note>

    Take note of the values returned to you, as you won't be able to see this password again.
  </Step>

  <Step>
    Open the `.env.local` file in your Symfony app, find the database connection section, and replace the existing `DATABASE_URL` value with:

    ```bash  theme={null}
    DATABASE_URL="mysql://<USERNAME>:<PASSWORD>@<ACCESS_HOST_URL>:3306/<DATABASE_NAME>?serverVersion=8.0"
    ```

    Fill in `USERNAME`, `PASSWORD`, `ACCESS HOST URL` and `DATABASE_NAME` with the appropriate values from the CLI output above.
  </Step>
</Steps>

Refresh your Symfony homepage and you should see the message that you're connected to your database!

### Option 2: Connect with the PlanetScale proxy

To connect with the PlanetScale proxy, you'll need the [PlanetScale CLI](https://github.com/planetscale/cli).

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
    Open the `.env.local` file in your Symfony app and update it as follows:

    ```bash  theme={null}
    DB_HOST=127.0.0.1
    DB_PORT=3306 # Get this from the output of the previous step
    DB_NAME=
    DATABASE_URL=mysql://${DB_HOST}:${DB_PORT}/${DB_NAME}?serverVersion=5.7
    ```

    The connection uses port `3306` by default, but if that's being used, it will pick a random port. Make sure you paste in whatever port is returned in the terminal. Fill in the database name as well.
  </Step>

  <Step>
    Open up `config/packages/doctrine.yaml`. Under `option`, you'll see a line for the SSL certificate that was used to connect with username and password:

    ```php  theme={null}
    !php/const:PDO::MYSQL_ATTR_SSL_CA: /etc/ssl/cert.pem
    ```
  </Step>
</Steps>

Delete that line and save.

Refresh your Symfony homepage and you should see the message that you're connected to your database!

## Run migrations and seeder

Now that you're connected, let's add some data to see it in action. The sample application comes with a migration file at `migrations/Version20220120102247.php` that will create `category` and `product` tables in the database.

There are also two seeder files, `src/DataFixtures/CategoryFixtures.php` and `src/DataFixtures/ProductFixtures.php`, that will add ten random categories and products to the `category` and `product` tables, respectively. Let's run those now.

<Steps>
  <Step>
    Make sure your database connection has been established. You'll see the message "You are connected to your-database-name" on the [Symfony app homepage](http://localhost:8000/) if everything is configured properly.
  </Step>

  <Step>
    In your terminal in the root of the Symfony project, run the following to run the migrations:

    ```bash  theme={null}
    symfony console doctrine:migrations:migrate
    ```

    You will get a message asking you to confirm. Type "yes" and hit enter to proceed.
  </Step>

  <Step>
    Next, seed the database by running:

    ```bash  theme={null}
    symfony console doctrine:fixtures:load
    ```

    This will purge your database and load the placeholder data into it.
  </Step>

  <Step>
    Refresh your Symfony homepage and you'll see a list of products and their category printed out.
  </Step>
</Steps>

The `templates/product/index.html.twig` file pulls this data from the `product` table with the help of the `src/Controller/ProductController.php` file.

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-symfony-app/example.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=4679f2f4f9d9c6af56e192bf4cfd7a02" alt="Symfony PlanetScale starter app homepage" data-og-width="2896" width="2896" data-og-height="2400" height="2400" data-path="docs/images/assets/docs/tutorials/connect-symfony-app/example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-symfony-app/example.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=4675897a4ffc14f46d5972fa9fcc353d 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-symfony-app/example.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=23fff82f386f197856cd88b39e6550fa 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-symfony-app/example.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=4daea7eead3c3ce9dbbe6ec31064a034 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-symfony-app/example.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=13eb631e6a0df30ecc837d649baea1e1 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-symfony-app/example.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=2f475a06f927318962ed66b599634306 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-symfony-app/example.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=c3e500abb8c8c3fddb2a04670a300e9e 2500w" />
</Frame>

## Add data manually

If you want to continue to play around with adding data on the fly, you have a few options:

* PlanetScale CLI shell
* PlanetScale dashboard console
* Your favorite MySQL client (for a list of tested MySQL clients, review our article on [how to connect MySQL GUI applications](/docs/vitess/tutorials/connect-mysql-gui))

The first two options are covered below.

### Add data with PlanetScale CLI

You can use the PlanetScale CLI to open a MySQL shell to interact with your database.

You may need to [install the MySQL command line client](/docs/cli/planetscale-environment-setup) if you haven't already.

Run the following command in your terminal:

```bash  theme={null}
pscale shell <DATABASE_NAME> <BRANCH_NAME>
```

This will open up a MySQL shell connected to the specified database and branch.

<Note>
  A branch, `main`, was automatically created when you created your database, so you can use that for `BRANCH_NAME`.
</Note>

Add a record to the `product` table:

```sql  theme={null}
INSERT INTO `store_product` (name, description, image, category_id)
VALUES  ('Spaceship', 'Get ready for the trip of a lifetime', 'https://via.placeholder.com/150.png', 2);
```

The value `id` will be filled with a default value.

You can verify it was added in the PlanetScale CLI MySQL shell with:

```sql  theme={null}
select * from product;
```

Type `exit` to exit the shell.

You can now refresh the [Symfony homepage](http://localhost:8000) to see the new record.

### Add data with PlanetScale dashboard console

If you don't care to install MySQL client or the PlanetScale CLI, another quick option using the MySQL console built into the PlanetScale dashboard.

By default, web console access to production branches is disabled to prevent accidental deletion. From your database's dashboard page, click on the "**Settings**" tab, check the box labelled "**Allow web console access to production branches**", and click "**Save database settings**".

<Steps>
  <Step>
    Go to your [PlanetScale dashboard](https://app.planetscale.com) and select your Symfony database.
  </Step>

  <Step>
    Click on the "**Branches** and select the `main` branch.
  </Step>

  <Step>
    Click on "**Console**"
  </Step>

  <Step>
    Add a new record to the `product` table with:

    ```sql  theme={null}
    INSERT INTO `store_product` (name, description, image, category_id)
    VALUES  ('Spaceship', 'Get ready for the trip of a lifetime', 'https://via.placeholder.com/150.png', 2);
    ```
  </Step>

  <Step>
    You can confirm that it was added by running:

    ```sql  theme={null}
    select * from product;
    ```
  </Step>
</Steps>

You can now refresh the [Symfony homepage](http://localhost:8000) to see the new record.

## What's next?

Once you're done with initial development, you can enable [safe migrations](/docs/vitess/schema-changes/safe-migrations) on your `main` production branch to protect it against direct schema changes and enable zero-downtime schema migrations.

Learn more about how PlanetScale allows you to make [non-blocking schema changes](/docs/vitess/schema-changes) to your database tables without locking or causing downtime for production databases.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt
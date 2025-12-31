# Source: https://planetscale.com/docs/vitess/tutorials/connect-php-app.md

# Connect a PHP application to PlanetScale

> In this tutorial, you'll learn how to connect a PHP application to a PlanetScale MySQL database with a sample PHP starter app using [MySQLi](https://www.php.net/manual/en/book.mysqli.php).

<Tip>
  Already have a PHP application and just want to connect to PlanetScale? Check out the [PHP quick connect repo](https://github.com/planetscale/connection-examples/tree/main/php).
</Tip>

## Prerequisites

* [PHP](https://www.php.net/manual/en/install.php) — This tutorial uses `v8.1`
* [Composer](https://getcomposer.org/)
* A [PlanetScale account](https://auth.planetscale.com/sign-up)
* [PlanetScale CLI](https://github.com/planetscale/cli) (Optional) — You can also follow this tutorial using just the PlanetScale admin dashboard, but the CLI will make setup quicker.

## Set up the PHP app

This guide uses [a simple PHP app](https://github.com/planetscale/php-example) that displays a list of products stored in a PlanetScale database. If you have an existing application, you can also use that.

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-php-app/example.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=01938ff12f9975f684c6861a99524fa7" alt="PHP sample application homepage priority" data-og-width="1500" width="1500" data-og-height="990" height="990" data-path="docs/images/assets/docs/tutorials/connect-php-app/example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-php-app/example.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=336c29c2c02992599f6e4a323595cdc5 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-php-app/example.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=bdd437690f4b5af41e426cbcf429c811 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-php-app/example.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=7eef53276615af1002e04cf08ea3d309 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-php-app/example.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=2847fda7092814dfe7a59650d8604d66 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-php-app/example.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=51c46dee5d5569961f215ac10639f737 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-php-app/example.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=ab15dac78852b9800781dfd272f125a3 2500w" />
</Frame>

<Steps>
  <Step>
    Clone the starter PHP application:

    ```bash  theme={null}
    git clone https://github.com/planetscale/php-example.git
    ```
  </Step>

  <Step>
    Enter into the folder and install the dependencies:

    ```bash  theme={null}
    cd php-example
    composer install
    ```
  </Step>

  <Step>
    Rename the `.env.example` file to `.env`:

    ```bash  theme={null}
    mv .env.example .env
    ```
  </Step>

  <Step>
    Start the application:

    ```bash  theme={null}
    php -S localhost:8000
    ```
  </Step>
</Steps>

You can view the application at [http://localhost:8000](http://localhost:8000).

## Set up the database

Next, you need to set up your PlanetScale database and connect it to the PHP application.

You can create a database either in the [PlanetScale dashboard](https://app.planetscale.com) or from the PlanetScale CLI.

This guide will use the CLI, but you can follow the database setup instructions in the [PlanetScale quickstart guide](/docs/vitess/tutorials/planetscale-quick-start-guide#create-a-database) if you prefer the dashboard. Just create the database and then come back here to continue.

<Steps>
  <Step>
    Install the [PlanetScale CLI](/docs/cli/planetscale-environment-setup).
  </Step>

  <Step>
    Authenticate in the CLI with the following command:

    ```bash  theme={null}
    pscale auth login
    ```
  </Step>

  <Step>
    Create a new database with the following command:

    ```bash  theme={null}
    pscale database create <DATABASE_NAME> --region <REGION_SLUG>
    ```
  </Step>
</Steps>

You can use any name with lowercase, alphanumeric characters, or underscores. You can also use dashes, but we don't recommend them, as they may need to be escaped in some instances.

For `REGION_SLUG`, choose a region closest to you from the [available regions](/docs/vitess/regions#available-regions) or leave it blank.

Your database is created with a default branch, `main`, which is meant to serve as your production database branch.

That's it! Your database is ready to use. Next, let's connect it to the PHP application and then add some data.

## Connect to the PHP app

There are **two ways to connect** to PlanetScale:

* With an auto-generated username and password
* Using the PlanetScale proxy with the CLI

Both options are covered below.

The environment variables you fill in next will be used in the [`db.php` file of the sample application](https://github.com/planetscale/php-example/blob/main/db.php):

```php  theme={null}
<?php
$hostname = $_ENV['HOST'];
$dbName = $_ENV['DATABASE'];
$username = $_ENV['USERNAME'];
$password = $_ENV['PASSWORD'];
$ssl = $_ENV['MYSQL_ATTR_SSL_CA'];
$port = 3306;

$mysqli = mysqli_init();
$mysqli->ssl_set(NULL, NULL, $ssl, NULL, NULL);
$mysqli->real_connect($hostname, $username, $password, $dbName, $port);

if ($mysqli->connect_error) {
    echo 'not connected to the database';
} else {
    echo "Connected successfully";
}
```

For `dbName`, you can use your PlanetScale database name directly if you have a *single unsharded keyspace*. If you have a sharded keyspace, you'll need to use `@primary`. This will automatically direct incoming queries to the correct keyspace/shard. For more information, see the [Targeting the correct keyspace documentation](/docs/vitess/sharding/targeting-correct-keyspace).

### Option 1: Connect with username and password (Recommended)

If you're not using the CLI, you can get the exact values to copy/paste from your PlanetScale dashboard. In the dashboard, select the branch you want to connect to from the infrastructure card (we're using `main`), click "**Connect**", and select "**PHP**" from the language dropdown. Copy these credentials, and then skip to step 2 to fill them in.

<Steps>
  <Step>
    Create a username and password with the PlanetScale CLI by running:

    ```bash  theme={null}
    pscale password create <DATABASE_NAME> <BRANCH_NAME> <PASSWORD_NAME>
    ```

    A default branch, `main`, was created when you created the database, so you can use that for `BRANCH_NAME`.

    <Note>
      The `PASSWORD_NAME` value represents the name of the username and password being generated. You can have multiple
      credentials for a branch, so this gives you a way to categorize them. To manage your passwords in the dashboard, go to
      your database dashboard page, click "Settings", and then click "Passwords".
    </Note>

    Take note of the values returned to you, as you won't be able to see this password again.
  </Step>

  <Step>
    Open the `.env` file in your PHP app:

    ```bash  theme={null}
    HOST=<ACCESS_HOST_URL>
    DATABASE=<DATABASE_NAME>
    USERNAME=<USERNAME>
    PASSWORD=<PASSWORD>
    MYSQL_ATTR_SSL_CA=
    ```

    Fill in your database name. For `USERNAME`, `PASSWORD`, and `HOST`, use the corresponding values from the CLI output.
  </Step>

  <Step>
    For `MYSQL_ATTR_SSL_CA`, use our [CA root configuration doc](/docs/vitess/connecting/secure-connections#ca-root-configuration) to find the correct value for your system. For example, if you're on MacOS, it would be:

    ```bash  theme={null}
    MYSQL_ATTR_SSL_CA=/etc/ssl/cert.pem
    ```
  </Step>

  <Step>
    Refresh your PHP homepage, and you should see the message that you're connected to your database!
  </Step>
</Steps>

### Option 2: Connect with the PlanetScale proxy

We recommend connecting with a username and password, but you can also open a quick connection with the PlanetScale proxy. You'll need the [PlanetScale CLI](https://github.com/planetscale/cli) for this option.

<Steps>
  <Step>
    Open a connection by running the following:

    ```bash  theme={null}
    pscale connect <DATABASE_NAME> <BRANCH_NAME>
    ```

    If you're following this guide exactly and haven't created any branches, you can use the default branch, `main`.
  </Step>

  <Step>
    A secure connection to your database will be established, and you'll see a local address you can use to connect to your application.
  </Step>

  <Step>
    Open the `.env` file in your PHP app and update it as follows:

    ```bash  theme={null}
    HOST=127.0.0.1
    PORT=3306 # Get this from the output of the previous step
    DATABASE=<DATABASE_NAME>
    ```

    The connection uses port `3306` by default, but we'll assign a random port if `3306` is in use. Make sure you paste in whatever port is returned in the terminal. Fill in the database name as well.
  </Step>

  <Step>
    Open `db.php` and replace it with the following:

    ```php expandable theme={null}
    <?php
    $hostname = $_ENV['HOST'];
    $dbName = $_ENV['DATABASE'];
    $port = $_ENV['PORT'];
    // $ssl = $_ENV['MYSQL_ATTR_SSL_CA'];

    $mysqli = mysqli_init();
    // $mysqli->ssl_set(NULL, NULL, $ssl, NULL, NULL);
    $mysqli->real_connect($hostname, '', '', $dbName, $port);

    if ($mysqli->connect_error) {
        echo 'not connected to the database';
    } else {
        echo "Connected successfully";
    }
    ```

    This removes all references to `username`, `password`, and `ssl`.

    <Note>
      It's important to make sure that you add the SSL check back if you switch back to username and password credentials.
      We're intentionally commenting it out instead of deleting it in case you switch back.
    </Note>
  </Step>

  <Step>
    Refresh your PHP homepage, and you should see the message that you're connected to your database!
  </Step>
</Steps>

## Add the schema and data

Now that you're connected to the database let's create the `products` and `categories` tables and add some data. There are a few ways to do this:

* PlanetScale CLI shell
* PlanetScale dashboard console
* Your favorite MySQL client (for a list of tested MySQL clients, review our article on [how to connect MySQL GUI applications](/docs/vitess/tutorials/connect-mysql-gui))

The first two options are covered below.

### Option 1: Add data with PlanetScale dashboard console

If you don't care to install the MySQL client or the PlanetScale CLI, another quick option is using the MySQL console built into the PlanetScale dashboard.

<Steps>
  <Step>
    Go to your [PlanetScale dashboard](https://app.planetscale.com) and select your PHP database.
  </Step>

  <Step>
    On the "**Dashboard**" page, you will need to select the gear icon and demote your `main` branch by toggling the "Promote to production" option. This is so you can create tables directly on your `main` branch.
  </Step>

  <Step>
    Click on the "**Console**" and select the `main` branch (or whatever development branch you used).
  </Step>

  <Step>
    Create the `categories` table:

    ```sql  theme={null}
    CREATE TABLE categories (
    id INT AUTO_INCREMENT NOT NULL,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    PRIMARY KEY(id)) DEFAULT CHARACTER SET utf8mb4 COLLATE `utf8mb4_unicode_ci` ENGINE = InnoDB;
    ```
  </Step>

  <Step>
    Create the `products` table:

    ```sql  theme={null}
    CREATE TABLE products (
    id INT AUTO_INCREMENT NOT NULL,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    image VARCHAR(255) NOT NULL,
    category_id INT NOT NULL,
    PRIMARY KEY(id)) DEFAULT CHARACTER SET utf8mb4 COLLATE `utf8mb4_unicode_ci` ENGINE = InnoDB;
    ```

    <Note>
      If you are using foreign key constraints, you must first enable [foreign key constraints](/docs/vitess/foreign-key-constraints) support in your database settings page.
    </Note>
  </Step>

  <Step>
    Add data to the `products` table with:

    ```sql  theme={null}
    INSERT INTO `products` (name, description, image, category_id) VALUES
    ('Shoes', 'Description for Shoes', 'https://via.placeholder.com/150.png', '1'),
    ('Hat', 'Description for Hats', 'https://via.placeholder.com/150.png', '1'),
    ('Bicycle', 'Description for Bicycle', 'https://via.placeholder.com/150.png', '4');
    ```
  </Step>

  <Step>
    Add data to the `categories` table with:

    ```sql  theme={null}
    INSERT INTO `categories` (name, description) VALUES
    ('Clothing', 'Description for Clothing'),
    ('Electronics', 'Description for Electronics'),
    ('Appliances', 'Description for Appliances'),
    ('Health', 'Description for Health');
    ```
  </Step>

  <Step>
    You can confirm that it was added by running:

    ```sql  theme={null}
    SELECT * FROM products;
    SELECT * FROM categories;
    ```
  </Step>
</Steps>

You can now refresh the [PHP homepage](http://localhost:8000) to see the new record.

### Option 2: Add data with PlanetScale CLI

You can use the PlanetScale CLI to open a MySQL shell to interact with your database.

You may need to [install the MySQL command line client](/docs/cli/planetscale-environment-setup) if you haven't already.

<Steps>
  <Step>
    Run the following command in your terminal:

    ```bash  theme={null}
    pscale shell <DATABASE_NAME> <BRANCH_NAME>
    ```

    This will open up a MySQL shell connected to the specified database and branch.

    <Note>
      A branch, `main`, was automatically created when you created your database, so you can use that for `BRANCH_NAME`.
    </Note>
  </Step>

  <Step>
    Create the `categories` table:

    ```sql  theme={null}
    CREATE TABLE categories (
      id INT AUTO_INCREMENT NOT NULL,
      name VARCHAR(255) NOT NULL,
      description VARCHAR(255) NOT NULL
    );
    ```
  </Step>

  <Step>
    Create the `products` table:

    ```sql  theme={null}
    CREATE TABLE products (
      id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(255) NOT NULL,
      description VARCHAR(255) NOT NULL,
      image VARCHAR(255) NOT NULL,
      category_id INT NOT NULL,
      KEY category_id_idx (category_id)
    );
    ```
  </Step>

  <Step>
    Add some records to the `products` table:

    ```sql  theme={null}
    INSERT INTO `products` (name, description, image, category_id) VALUES
    ('Shoes', 'Description for Shoes', 'https://via.placeholder.com/150.png', '1'),
    ('Hat', 'Description for Hats', 'https://via.placeholder.com/150.png', '1'),
    ('Bicycle', 'Description for Bicycle', 'https://via.placeholder.com/150.png', '4');
    ```

    The value `id` will be filled with a default value.
  </Step>

  <Step>
    Add some data to the `categories` table:

    ```sql  theme={null}
    INSERT INTO `categories` (name, description) VALUES
    ('Clothing', 'Description for Clothing'),
    ('Electronics', 'Description for Electronics'),
    ('Appliances', 'Description for Appliances'),
    ('Health', 'Description for Health');
    ```
  </Step>

  <Step>
    You can verify everything was added in the PlanetScale CLI MySQL shell with:

    ```sql  theme={null}
    SELECT * FROM products;
    SELECT * FROM categories;
    ```
  </Step>

  <Step>
    Type `exit` to exit the shell.
  </Step>
</Steps>

You can now refresh the [PHP homepage](http://localhost:8000) to see the new records.

## What's next?

Once you're done with initial development, you can promote your branch to production and enable [safe migrations](/docs/vitess/schema-changes/safe-migrations) on your `main` production branch to protect it against direct schema changes and enable zero-downtime schema migraions.

When you're reading to make more schema changes, you'll [create a new branch](/docs/vitess/schema-changes/branching) off of your production branch. Branching your database creates an isolated copy of your production schema so that you can easily test schema changes in development. Once you're happy with the changes, you'll [open a deploy request](/docs/vitess/schema-changes/deploy-requests). This will generate a diff showing the changes that will be deployed, making it easy for your team to review.

Learn more about how PlanetScale allows you to make [non-blocking schema changes](/docs/vitess/schema-changes) to your database tables without locking or causing downtime for production databases.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt
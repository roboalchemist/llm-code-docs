# Source: https://planetscale.com/docs/vitess/tutorials/connect-go-gorm-app.md

# Connect a Go application using GORM to PlanetScale

## Introduction

In this tutorial, you'll learn how to connect a Go application to a PlanetScale MySQL database using a sample Go starter app with GORM.

<Tip>
  Already have a Go application and just want to connect to PlanetScale? Check out the [Go quick connect
  repo](https://github.com/planetscale/connection-examples/tree/main/go).
</Tip>

## Prerequisites

* [Go](https://go.dev/doc/install)
* A [PlanetScale account](https://auth.planetscale.com/sign-up)
* [PlanetScale CLI](https://github.com/planetscale/cli) — You can also follow this tutorial in the PlanetScale admin dashboard, but the CLI will make setup quicker.

## Set up the Go app

This guide will integrate [a simple Go (Golang) app](https://github.com/planetscale/golang-example) with PlanetScale that will display a list of products stored in the database. If you have an existing application, you can also use that.

<Steps>
  <Step>
    Clone the starter Go application:

    ```bash  theme={null}
    git clone https://github.com/planetscale/golang-example.git
    ```
  </Step>

  <Step>
    Enter into the folder:

    ```bash  theme={null}
    cd golang-example
    ```
  </Step>

  <Step>
    Copy the `.env.example` file into `.env`:

    ```bash  theme={null}
    cp .env.example .env
    ```
  </Step>
</Steps>

## Set up the database

Next, you need to set up your PlanetScale database and connect to it in the Go application.

You can create a database in the [PlanetScale dashboard](https://app.planetscale.com) or from the PlanetScale CLI. This guide will use the CLI, but you can follow the database setup instructions in the [PlanetScale quickstart guide](/docs/vitess/tutorials/planetscale-quick-start-guide) if you prefer the dashboard.

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

    For `DATABASE_NAME`, you can use any name with lowercase, alphanumeric characters, or underscores. You can also use dashes, but we don't recommend them, as they may need to be escaped in some instances.

    For `REGION_SLUG`, choose a region closest to you from the [available regions](/docs/vitess/regions#available-regions) or leave it blank.
  </Step>
</Steps>

That's it! Your database is ready to use. Next, let's connect it to the Go application and then add some data.

## Connect to the Go app

There are **two ways to connect** your Go app to PlanetScale:

* With an auto-generated username and password
* Using the PlanetScale proxy with the CLI

Both options are covered below.

### Option 1: Connect with username and password (Recommended)

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
    Open the `.env` file in your Go app and update `DSN` as follows:

    ```bash  theme={null}
    DSN="<USERNAME>:<PASSWORD>@tcp(<ACCESS HOST URL>)/<DATABASE_NAME>?tls=true&interpolateParams=true"
    ```

    Fill in `USERNAME`, `PASSWORD`, `ACCESS HOST URL`, and `DATABASE_NAME` with the appropriate values from the CLI output above. Do not remove the parentheses around the access host URL.

    You can also get these exact values to copy/paste from your PlanetScale dashboard. In the dashboard, click on the database > "**Connect**" > "**Connect with**" language dropdown > "**Go**".
  </Step>
</Steps>

### Option 2: Connect with the PlanetScale proxy

To connect with the PlanetScale proxy, you need the [PlanetScale CLI](https://github.com/planetscale/cli).

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
    Open the `.env` file in your Go app and update it as follows:

    ```bash  theme={null}
    DSN="mysql://root@tcp(127.0.0.1:<PORT>)/<DATABASE_NAME>?interpolateParams=true"
    ```

    The connection uses port `3306` by default, but if that's being used, it will pick a random port. Make sure you paste in whatever port is returned in the terminal. Fill in the database name as well.
  </Step>
</Steps>

## Run migrations and seeder

Now that you're connected let's add some data to see it in action. The sample application has an endpoint that you can use to run migrations to create your `categories` and `products` tables. It will seed your database with sample product and category data. You can find this in `main.go`.

Let's run those now.

<Steps>
  <Step>
    First, start your Go app with:

    ```bash  theme={null}
    go run .
    ```
  </Step>

  <Step>
    Next, navigate to [`localhost:8080/seed`](http://localhost:8080/seed) to run the migrations and the seeder.
  </Step>

  <Step>
    You can now see the products and categories:

    * Get all products — [`localhost:8080/products`](http://localhost:8080/products)
    * Get all categories — [`localhost:8080/categories`](http://localhost:8080/categories)
    * Get a single product — [`localhost:8080/product/{id}`](http://localhost:8080/products/1)
    * Get a single category — [`localhost:8080/category/{id}`](http://localhost:8080/categories/1)
  </Step>
</Steps>

### Foreign key constraints

If you're using GORM in your Go application and [do not want to use foreign key constraints](/docs/vitess/operating-without-foreign-key-constraints), you can turn them off with this line in the `main.go` file of the Go starter application:

```go  theme={null}
// ...
DisableForeignKeyConstraintWhenMigrating: true,
// ...
```

If you prefer to use foreign key constraints in your Go application, you can skip the previous step. However, you need to first enable [foreign key constraint](/docs/vitess/foreign-key-constraints) support in your database settings page.

## Add data manually

If you want to continue to play around with adding data on the fly, you have a few options:

* PlanetScale CLI shell
* PlanetScale dashboard console
* Your favorite MySQL client (for a list of tested MySQL clients, review our article on [how to connect MySQL GUI applications](/docs/vitess/tutorials/connect-mysql-gui))

The first two options are covered below.

### Add data with PlanetScale CLI

You can use the PlanetScale CLI to open a MySQL shell to interact with your database.

You may need to install the MySQL command line client if you haven't already.

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
    Add a record to the `products` table:

    ```sql  theme={null}
    INSERT INTO `products` (name, description, image, category_id)
    VALUES  ('Spaceship', 'Get ready for the trip of a lifetime', 'https://via.placeholder.com/300.png', 2);
    ```

    The value `id` will be filled with a default value.
  </Step>

  <Step>
    You can verify it was added in the PlanetScale CLI MySQL shell with:

    ```sql  theme={null}
    SELECT * FROM products;
    ```
  </Step>

  <Step>
    Type `exit` to exit the shell.

    You can now navigated the [Go products page](http://localhost:8080/products) to see the new record.
  </Step>
</Steps>

### Add data with PlanetScale dashboard console

If you don't care to install MySQL client or the PlanetScale CLI, another quick option is using the MySQL console built into the PlanetScale dashboard.

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-gorm-app/console-2.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=a00e4fc53cc45987bc4558fee82a44de" alt="PlanetScale console insert and select example" data-og-width="1842" width="1842" data-og-height="1187" height="1187" data-path="docs/images/assets/docs/tutorials/connect-go-gorm-app/console-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-gorm-app/console-2.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=1f278c743487d389eba5928cb427a8b6 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-gorm-app/console-2.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=b69e99444ad36c675ee312f935aff94e 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-gorm-app/console-2.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=e7014d42f8627415a2e61afa4a44c728 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-gorm-app/console-2.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=8de7475162022d1b0db215587f008118 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-gorm-app/console-2.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=3668fe02052f60ef9848ea068d6dfe4b 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-go-gorm-app/console-2.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=d79607d812890b6c053392c6a91439d2 2500w" />
</Frame>

<Steps>
  <Step>
    Go to your [PlanetScale dashboard](https://app.planetscale.com) and select your Go database.
  </Step>

  <Step>
    Click on "**Console**".
  </Step>

  <Step>
    Select the `main` branch and click "**Connect**".
  </Step>

  <Step>
    Add a new record to the `product` table with:

    ```sql  theme={null}
    INSERT INTO `products` (name, description, image, category_id)
    VALUES  ('Spaceship', 'Get ready for the trip of a lifetime', 'https://via.placeholder.com/300.png', 2);
    ```
  </Step>

  <Step>
    You can confirm that it was added by running:

    ```sql  theme={null}
    SELECT * FROM products;
    ```
  </Step>
</Steps>

You can now refresh the [Go products page](http://localhost:8080/products) to see the new record.

## What's next?

Once you're done with initial development, you can enable [safe migrations](/docs/vitess/schema-changes/safe-migrations) on your `main` production branch to protect it against direct schema changes and enable zero-downtime schema migrations.

When you're reading to make more schema changes, you'll [create a new branch](/docs/vitess/schema-changes/branching) off of your production branch. Branching your database creates an isolated copy of your production schema so that you can easily test schema changes in development. Once you're happy with the changes, you'll open a [deploy request](/docs/vitess/schema-changes/deploy-requests). This will generate a diff showing the changes that will be deployed, making it easy for your team to review.

Learn more about how PlanetScale allows you to make [non-blocking schema changes](/docs/vitess/schema-changes) to your database tables without locking or causing downtime for production databases.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt
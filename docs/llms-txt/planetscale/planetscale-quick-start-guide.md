# Source: https://planetscale.com/docs/vitess/tutorials/planetscale-quick-start-guide.md

# PlanetScale quickstart guide

export const VimeoEmbed = ({id, title}) => {
  return <Frame>
      <iframe src={`https://player.vimeo.com/video/${id}?dnt=true`} title={title} className="aspect-video w-full" allow="autoplay; fullscreen; picture-in-picture" />
    </Frame>;
};

## Overview

The following guide will show you how to:

* Create a database with PlanetScale
* Make a schema change
* Insert data
* Promote your database branch to production

If you already have your PlanetScale database set up, you may find the [Connecting your application](/docs/vitess/tutorials/connect-any-application) or [Branching](/docs/vitess/schema-changes/branching) guides more helpful.

This guide is split up so that you can either follow it in the [PlanetScale dashboard](#getting-started--planetscale-dashboard) or using the [PlanetScale CLI](#getting-started--planetscale-cli).

<VimeoEmbed id="830571983" title="PlanetScale quickstart guide" />

## Getting started — PlanetScale dashboard

You'll need [a PlanetScale account](https://auth.planetscale.com/sign-up) to complete this guide.

### Create a database

Follow these steps to create a database:

<Steps>
  <Step>
    Click "**New database**" > "**Create a database**" on your organization's overview page.
  </Step>

  <Step>
    Name your database.
  </Step>

  <Step>
    Select a [region](/docs/vitess/regions). For the lowest latency, select a region near you or your application's hosting location.
  </Step>

  <Step>
    Select the desired [cluster and storage size](/docs/planetscale-plans#base) for your database.
  </Step>

  <Step>
    Enter a valid credit or debit card.
  </Step>

  <Step>
    Finally, click the "**Create database**" button to deploy your database.
  </Step>
</Steps>

Your database is created with a [**default production branch**](/docs/vitess/schema-changes/branching), `main`, which you will use to apply a schema change and insert data. While this is just the first branch we create for you, you can always create new development branches (isolated copies of the production schema) off of production to use for development.

### Add a schema to your database

This quickstart demonstrates how to create and use two relational tables: `categories` and `products`.

<Steps>
  <Step>
    By default, web console access to production branches is disabled to prevent accidental deletion. From your database's dashboard page, click on the "**Settings**" tab, check the box labelled "**Allow web console access to production branches**", and click "**Save database settings**".
  </Step>

  <Step>
    Click on the "**Console**" tab in the database navigation. This will open up a [web console](/docs/vitess/web-console) connected to your database branch.
    <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-quick-start-guide/the-console-tab.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=a4d3520f08cfedc57295ff6894b73e4a" alt="Branches" data-og-width="1634" width="1634" data-og-height="1084" height="1084" data-path="docs/images/assets/docs/tutorials/planetscale-quick-start-guide/the-console-tab.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-quick-start-guide/the-console-tab.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=4b45fdd728ea28a3888fa80ee4706836 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-quick-start-guide/the-console-tab.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=0733b0ebaa9cc1fcb38d25b10f124b68 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-quick-start-guide/the-console-tab.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=92dd8b845c8b6a409eb2907598209cc4 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-quick-start-guide/the-console-tab.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=58f498acbe3f6bcac0458e35ea03faef 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-quick-start-guide/the-console-tab.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=2c307dcba327b1b227d39e7429115e48 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-quick-start-guide/the-console-tab.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=c6921139d3c8048a69a36881fa2c8be6 2500w" />
  </Step>

  <Step>
    By default the `main` branch is preselected. Click **"Connect"**.
  </Step>

  <Step>
    Create the `categories` and `products` tables by running the following commands in the web console:

    ```sql  theme={null}
    CREATE TABLE categories (
      id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
      name varchar(255) NOT NULL
    );
    ```

    ```sql  theme={null}
    CREATE TABLE products (
      id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
      name varchar(255) NOT NULL,
      image_url varchar(255),
      category_id INT,
      KEY category_id_idx (category_id)
    );
    ```

    <Note>
      If you want to make schema changes containing foreign key constraints, enable [foreign key constraints](/docs/vitess/foreign-key-constraints) support in your database settings page.
    </Note>
  </Step>

  <Step>
    You can confirm that the tables have been added by running:

    ```sql  theme={null}
    SHOW TABLES;
    ```
  </Step>
</Steps>

### Insert data into your database

Now that you have created your tables, let's insert some data. Run the following commands to add a product and category to your tables:

```sql  theme={null}
INSERT INTO categories (name)
VALUES  ('Office supplies');
```

```sql  theme={null}
INSERT INTO products (name, image_url, category_id)
VALUES  ('Ballpoint pen', 'https://example.com/500x500', '1');
```

You can confirm the data has been added with:

```sql  theme={null}
SELECT * FROM products;
```

```sql  theme={null}
SELECT * FROM categories;
```

You can view the schema of your database by navigating to the "**Branches**" tab and selecting the database you want to view. For now, select the `main` database, and it will display the names of the two tables you just created. Click on the name of each table to see further schema details.

### Enable safe migrations on your `main` branch

All of the work you've done so far has been on a default production branch, `main`, that was automatically created when you created the database.

A production branch is a highly available database branch that includes an additional replica. It also has the option to enable [safe migrations](/docs/vitess/schema-changes/safe-migrations), which enables non-blocking schema changes and can protect your database from accidental schema changes.

[Safe migrations](/docs/vitess/schema-changes/safe-migrations) is an optional, but highly recommended, feature that adds an additional layer of protection to your branch by preventing accidental schema modifications and enabling no-downtime schema changes. With safe migrations enabled, any DDL issued directly to the branch will not be accepted. Instead, changes must be made using the PlanetScale flow, where deploy requests are used to safely merge changes in a collaborative environment.

### To enable safe migrations:

<Steps>
  <Step>
    Click "Dashboard" in the navigation, and click the "**cog**" in the upper right of the infrastructure card to open a modal.
    <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-quick-start-guide/production-branch-card-with-sm-disabled-2.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=847b9711b99d7eb2b8a6979fef715096" alt="Production UI card" data-og-width="1904" width="1904" data-og-height="819" height="819" data-path="docs/images/assets/docs/tutorials/planetscale-quick-start-guide/production-branch-card-with-sm-disabled-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-quick-start-guide/production-branch-card-with-sm-disabled-2.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=af62627e3b9b3aa9b3c6b26753fc8920 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-quick-start-guide/production-branch-card-with-sm-disabled-2.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=31bc516f819eba4c8fa8182cba59ea97 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-quick-start-guide/production-branch-card-with-sm-disabled-2.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=85114b57e4b57e12599f215dbe22e201 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-quick-start-guide/production-branch-card-with-sm-disabled-2.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=7b91a17d0e01136ba3197a2740ae113d 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-quick-start-guide/production-branch-card-with-sm-disabled-2.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=b0865022d0d152331122ba5a34ee7ccf 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-quick-start-guide/production-branch-card-with-sm-disabled-2.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=f3095e7a4862f24b8957cdcfc2b34736 2500w" />
  </Step>

  <Step>
    Toggle "**Enable safe migrations**", then click the "**Enable safe migrations**" button.
  </Step>
</Steps>

The `main` branch now contains the `categories` and `products` tables you created, along with the data you inserted. In addition, it is highly available with an additional replica, and is enabled for zero-downtime migrations with [safe migrations](/docs/vitess/schema-changes/safe-migrations).

### What's next?

Now that you've created a database, applied schema changes, added data, and enable safe migrations, it's time to connect to your application.

You can use our [Connect Any Application tutorial](/docs/vitess/tutorials/connect-any-application) for a general step-by-step approach, one of our language-specific guides, or head straight to our [Connection Strings documentation](/docs/vitess/connecting/connection-strings) for more information about creating connection strings.

When you want to continue development on your database:

<Steps>
  <Step>
    [Create a new branch](/docs/vitess/schema-changes/branching) off of your production branch
  </Step>

  <Step>
    Go through the same process described in this doc to make schema changes
  </Step>

  <Step>
    [Create a deploy request](/docs/vitess/schema-changes/deploy-requests) to merge the changes into your production branch
  </Step>
</Steps>

<Note>
  When you branch off of a production branch, your development branch will have the same schema as production, but it
  **will not** copy over any data from the production database. We suggest seeding development branches with mock
  data.
</Note>

## Getting started — PlanetScale CLI

Make sure you first have [downloaded and installed the PlanetScale CLI](https://github.com/planetscale/cli#installation).

You will also need a PlanetScale account. You can [sign up for a PlanetScale account here](https://auth.planetscale.com/sign-up) or run `pscale signup` to create an account straight from the CLI.

### Sign in to your account

To authenticate with the PlanetScale CLI, enter the following:

```bash  theme={null}
pscale auth login
```

You'll be taken to a screen in the browser where you'll be asked to confirm the code displayed in your terminal. If the confirmation codes match, click the "**Confirm code**" button in your browser.

You should receive the message "Successfully logged in" in your terminal. You can now close the confirmation page in the browser and proceed in the terminal.

### Create a database

Run the following command to create a database:

```bash  theme={null}
pscale database create <DATABASE_NAME> --region <REGION_SLUG>
```

* **DATABASE\_NAME** — Your database name can contain lowercase, alphanumeric characters, or underscores. We allow dashes, but don't recommend them, as they may need to be escaped in some instances.
* **REGION\_SLUG** — For the lowest latency, choose the region closest to you or your application's hosting location. You can find our regions and their slugs on the [Regions page](/docs/vitess/regions#available-regions).

<Note>
  If you do not specify a region, your database will automatically be deployed to **US East — Northern Virginia**.
</Note>

Your database is created with an [**initial branch**](/docs/vitess/schema-changes/branching), `main`, which you will use to apply a schema change and insert data. While this is just the first branch we create for you, you can always create new branches (isolated copies of the production schema) off of production to use for development.

### Add a schema to your database

To add a schema to your database, you will need to connect to MySQL, so [make sure you `mysql-client` installed](/docs/cli/planetscale-environment-setup#setup-overview).

<Steps>
  <Step>
    Run the following command:

    ```bash  theme={null}
    pscale shell <DATABASE_NAME> main
    ```

    You are now connected to your `main` branch and can run MySQL queries against it.
  </Step>

  <Step>
    Create the `categories` and `products` tables by running the following:

    ```sql  theme={null}
    CREATE TABLE categories (
      id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
      name varchar(255) NOT NULL
    );
    ```

    ```sql  theme={null}
    CREATE TABLE products (
      id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
      name varchar(255) NOT NULL,
      image_url varchar(255),
      category_id INT,
      KEY category_id_idx (category_id)
    );
    ```

    <Note>
      If you want to make schema changes containing foreign key constraints, enable [foreign key constraints](/docs/vitess/foreign-key-constraints) support in your database settings page.
    </Note>
  </Step>

  <Step>
    You can confirm that the table has been added by running:

    ```sql  theme={null}
    SHOW TABLES;
    ```
  </Step>

  <Step>
    To see the table schemas, run:

    ```sql  theme={null}
    DESCRIBE categories;
    ```

    ```sql  theme={null}
    DESCRIBE products;
    ```
  </Step>
</Steps>

### Insert data into your database

Now that you have your schema set up, let's insert some data.

<Steps>
  <Step>
    Run the following commands to add one entry to each table:

    ```sql  theme={null}
    INSERT INTO `categories` (name)
    VALUES  ('Office supplies');
    ```

    ```sql  theme={null}
    INSERT INTO `products` (name, image_url, category_id)
    VALUES  ('Ballpoint pen', 'https://example.com/500x500', '1');
    ```
  </Step>

  <Step>
    You can confirm the data has been added with:

    ```sql  theme={null}
    SELECT * FROM products;
    ```

    ```sql  theme={null}
    SELECT * FROM categories;
    ```
  </Step>

  <Step>
    Exit the shell by typing `exit`.
  </Step>
</Steps>

### Enable safe migrations

All of the work you've done so far has been on a default production branch, `main`, that was automatically created when you created the database.

A production branch is a highly available database branch that includes an additional replica. It also has the option to enable [safe migrations](/docs/vitess/schema-changes/safe-migrations), which enables non-blocking schema changes and can protect your database from accidental schema changes.

[Safe migrations](/docs/vitess/schema-changes/safe-migrations) is an optional, but highly recommended, feature that adds an additional layer of protection to your branch by preventing accidental schema modifications and enabling no-downtime schema changes. With safe migrations enabled, any DDL issued directly to the branch will not be accepted. Instead, changes must be made using the PlanetScale flow, where deploy requests are used to safely merge changes in a collaborative environment.

To enable safe migrations on your branch, run:

```bash  theme={null}
pscale branch safe-migrations enable <DATABASE_NAME> main
```

The `main` branch now contains the `categories` and `products` tables you created, along with the data you inserted. In addition, it is highly available with an additional replica, and is enabled for zero-downtime migrations with [safe migrations](/docs/vitess/schema-changes/safe-migrations).

### What's next?

Now that you've created a database, applied schema changes, added data, and enabled safe migrations, it's time to connect to your application.

You can use our [Connect Any Application tutorial](/docs/vitess/tutorials/connect-any-application) for a general step-by-step approach, one of our language-specific guides, or head straight to our [Connection Strings documentation](/docs/vitess/connecting/connection-strings) for more information about creating connection strings.

When you want to continue development on your database:

<Steps>
  <Step>
    [Create a new branch](/docs/vitess/schema-changes/branching) off of your production branch
  </Step>

  <Step>
    Go through the same process described in this doc to make schema changes
  </Step>

  <Step>
    [Create a deploy request](/docs/vitess/schema-changes/deploy-requests) to merge the changes into your production branch
  </Step>
</Steps>

<Note>
  When you branch off of a production branch, your development branch will have the same schema as production, but it
  **will not** copy over any data from the production database. We suggest seeding development branches with mock
  data.
</Note>

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt
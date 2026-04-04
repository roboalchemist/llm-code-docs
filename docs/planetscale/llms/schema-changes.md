# Source: https://planetscale.com/docs/vitess/schema-changes.md

# Non-blocking schema changes

> **Non-blocking schema changes** in PlanetScale provide a schema change workflow that allows users to update database tables without locking or causing downtime for production databases.

## Overview

<Tip>
  To make non-blocking schema changes in PlanetScale, you'll first need a basic understanding of
  [branching](/docs/vitess/schema-changes/branching), the core PlanetScale feature that provides schema changes. Our
  branching page is a great place to start.
</Tip>

PlanetScale makes it safe to deploy schema changes to production databases via *development* and *production branches with [safe migrations](/docs/vitess/schema-changes/safe-migrations) enabled*. Branches with safe migrations enabled can only be updated using deploy requests, and default branches cannot be deleted. Development branches are a separate database with a copy of the source branch's schema. Developers can make schema changes in development branches, test locally, and open a deploy request for deploying their changes to the production database.

Developers can also comment on deploy requests and request reviewers to approve a deploy request before its schema changes can deploy into base branches. Currently, requiring approval is a per-database setting that is turned off by default. With the setting turned off, developers do not need approval to merge a deploy request.

## Adding columns to large tables with PlanetScale is safe!

*Create*, *drop*, and *alter* statements, also known as Data Definition Language (DDL), are used for making schema changes in a database table.

PlanetScale enables developers to make schema changes without the fear of dropping columns, locking tables, causing downtime in their app, etc. PlanetScale also prevents schema changes with conflicts from being migrated and handles schema changes from multiple teammates. A user doesn't have to wait to find out if their changes will be rejected, they learn as they add the change to the queue.

## How do I make non-blocking schema changes with PlanetScale?

In order to make non-blocking schema changes, you **must** enable [safe migrations](/docs/vitess/schema-changes/safe-migrations) on your production branch. Without safe migrations enabled, your schema changes will run directly on your production branch, which can lead to table locking. When safe migrations are enabled on a branch, all schema changes must occur on a database branch. *(A database branch is a separate database with a copy of the production branch's schema.)*

At a high level, this is what happens during the *non-blocking schema change* process in PlanetScale:

<Steps>
  <Step>
    You create a development branch.
  </Step>

  <Step>
    You test your changes on this branch before attempting to apply the changes to the production branch. *(i.e., You made some changes to the database you wish to deploy to the production database.)*
  </Step>

  <Step>
    You open a request to deploy your changes to the base branch, the production branch.
  </Step>

  <Step>
    PlanetScale verifies that your schema changes are safe to be deployed to production. If there are any issues or schema conflicts, you'll be shown the errors.
  </Step>

  <Step>
    You click `Deploy changes`. Your deploy is added to a queue and run immediately or when existing deploys are complete.
  </Step>

  <Step>
    Your deployment makes it to the base branch, and you can now see your schema changes in production.
  </Step>
</Steps>

<Note>
  PlanetScale makes sure not to exhaust your resources; the deployment may be throttled to avoid any impact on
  production queries.
</Note>

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/nonblocking-schema-changes/diagram.png?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=10322a5a0d4c2bc678ed9225736f2830" alt="PlanetScale non-blocking schema changes diagram" data-og-width="1234" width="1234" data-og-height="720" height="720" data-path="docs/images/assets/docs/concepts/nonblocking-schema-changes/diagram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/nonblocking-schema-changes/diagram.png?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=3ab4093ecd4752c7f801729679e5e0f3 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/nonblocking-schema-changes/diagram.png?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=9d52afcc838cb1a9ac3ab1ee448c563d 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/nonblocking-schema-changes/diagram.png?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=b6b43b59a13d507f27b512382f995fe6 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/nonblocking-schema-changes/diagram.png?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=9d330b7c7141e72d1a4cab3864b3bc40 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/nonblocking-schema-changes/diagram.png?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=b089ee493d3cd689a86c69613382314e 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/nonblocking-schema-changes/diagram.png?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=0f307fca63cd0c4908208300ab8da37f 2500w" />
</Frame>

## PlanetScale workflow

The PlanetScale command-line tool (CLI) runs an interactive shell equipped with many commands designed to make the database management workflow easier for developers.

A basic non-blocking schema change workflow in PlanetScale might look like this:

<Steps>
  <Step>
    Create a database:

    ```bash  theme={null}
    pscale database create <database>
    ```
  </Step>

  <Step>
    Create a development branch:

    ```bash  theme={null}
    pscale branch create <database> <branch>
    ```
  </Step>

  <Step>
    Make a schema change on this branch:

    ```bash  theme={null}
    pscale shell <database> <branch>
    ```

    <Tip>
      A schema change is any change you make to the tables in your database environment created within the PlanetScale branch. (i.e., create, drop, and alter statements)
    </Tip>

    <Warning>
      You can only apply direct schema changes to branches without safe migrations enabled.
    </Warning>

    Here is a sample CREATE table schema change you could try using:

    ```sql  theme={null}
    CREATE TABLE `reminders` (
      `id` bigint NOT NULL AUTO_INCREMENT,
      `body` varchar(1024) NOT NULL,
      `created_at` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
      `updated_at` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
      `is_done` tinyint(1) NOT NULL DEFAULT '0',
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    ```
  </Step>

  <Step>
    Test changes on branch locally.
  </Step>

  <Step>
    Create a deployment request by running:

    ```bash  theme={null}
    pscale deploy-request create <database> <branch>
    ```
  </Step>

  <Step>
    Fix any schema conflicts.

    PlanetScale displays the difference between what is currently in the base branch and your development branch. Go back to *Step 3* of the workflow and test out new schema changes to fix the schema conflict. If you did not encounter any schema conflicts, you're ready for *Step 7*.
  </Step>

  <Step>
    Deploy the deploy request.

    * To *deploy* the **deploy request** created in *Step 5*, run the following command:

      ```bash  theme={null}
      pscale deploy-request deploy <database> <deploy-request-number>
      ```

    * To find your `deploy-request-number`, simply run:

      ```bash  theme={null}
      pscale deploy-request list <database>
      ```

    Copy the value from `NUMBER` and use that digit as your `deploy-request-number`.
  </Step>
</Steps>

## Limitations

If you want to make schema changes containing foreign key constraints, enable foreign key constraint support for your database in the database settings page.

PlanetScale doesn't support direct `RENAME` for columns and tables. Learn why and how to rename tables or columns in [this tutorial](/docs/vitess/schema-changes/handling-table-and-column-renames).

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt
# Source: https://planetscale.com/docs/vitess/schema-changes/branching.md

# Source: https://planetscale.com/docs/postgres/branching.md

# Branching

> Branches on PlanetScale Postgres are isolated database deployments that provide you with separate environments for development and testing, as well as restoring from backups.

When your PostgreSQL database is first initialized, a single production branch is created called `main` which acts as the default branch. You can then create development branches that you can use for development before shipping schema changes to production.

Branches are completely isolated databases. Changes made in one branch, whether to the schema or the data, do not affect any other branches for a given database. There is no data replication between branches, so writing data into one will not replicate to another.

<Note>
  New branches incur additional charges. The cost depends on the selected resources for the branch. The monthly price for the new branch will be shown during branch creation. See [pricing](/docs/postgres/pricing) for more information.
</Note>

## Development and production branches

PlanetScale Postgres provides two types of database branches:

* **Development branches** — Development branches run on `PS-DEV` instances that have limited performance capabilities, different egress rates, and no replicas. This is great for experimentation, testing new schemas, and limited exploration of your data.

* **Production branches** — Production branches are intended for production traffic and include optional replicas for high availability. Production branches can be created on non-HA ([single node](/docs/postgres/cluster-configuration/single-node)) or HA (primary + 2 replicas) nodes.

## Create a branch

<Note>
  We are still in the process of building out our full branching functionality Postgres. You can currently create a new empty branch with no schema and no data or create a branch from a backup, which includes schema and data.
</Note>

There are two ways to create a new Postgres branch: from the Branches page (no schema or data included) or by restoring from a backup (schema and data included).

Each branch is its own isolated database and uses its own storage separate from production. You will be charged for the storage consumed by all production and development branches.

We do not recommend using production data for development environments.

### From the Branches page

This method does not include schema or data.

Branches created via this method will always initialize as a single node `PS-DEV` database, which does not have any replicas and begins at \$5/month, depending on the region. After initialization, you have the option to upsize the branch or add replicas from the "Clusters" page in the dashboard.

<Steps>
  <Step>Click **Branches**</Step>
  <Step>Click **New branch**</Step>
  <Step>Give the branch a name</Step>

  <Step>
    Choose the base branch. This currently does not copy the schema.
  </Step>

  <Step>Select a region</Step>
  <Step>Click **Create branch**</Step>
</Steps>

### From a backup

This method includes both the schema and the data for the selected backup.

The cluster size, and therefore cost, is inherited from your main parent branch.

<Steps>
  <Step>
    From the PlanetScale organization dashboard, select the desired database
  </Step>

  <Step>
    Navigate to the **Backups** page from the menu on the left
  </Step>

  <Step>
    Select the backup you wish to restore from
  </Step>

  <Step>
    Click **Restore to new branch**
  </Step>

  <Step>
    Configure the restored branch:

    * **Branch name**: Name for the new branch
    * **Cluster size**: Choose the desired size of the new cluster
  </Step>

  <Step>
    Click **Restore backup**
  </Step>
</Steps>

A new branch will be created based on this backup and will become visible under the **Branches** page.

## View all branches

To view all branches for your PostgreSQL database:

<Steps>
  <Step>From the PlanetScale organization dashboard, select the desired database</Step>
  <Step>Click on the **Branches** drop down</Step>
  <Step>You'll see a list of all branches with their type (development/production)</Step>
  <Step>You can select a branch by its name to see its **Dashboard**</Step>
</Steps>

Similarly you can navigate directly to the Branches page to see all branches:

<Steps>
  <Step>From the PlanetScale organization dashboard, select the desired database</Step>
  <Step>Navigate to the **Branches** page from the menu on the left</Step>
</Steps>

## Connect to a branch

Each branch has its own connection details. To connect to a specific branch:

<Steps>
  <Step>Navigate to the desired branch following either of the paths shown above</Step>
  <Step>Click the **Connect** button</Step>
  <Step>If you haven't already, follow the instructions to **Create the default role**</Step>
  <Step>Choose your preferred connection method ([direct or PgBouncer](/docs/postgres/connecting))</Step>
  <Step>Copy the connection string or credentials</Step>
  <Step>You should create new roles for specific use-cases and tailor their permissions appropriately for them</Step>
  <Step>In your application, use the specific role(s) and the preferred connection method.</Step>
</Steps>

For detailed connection instructions, see the [PostgreSQL connection documentation](/docs/postgres/connecting).

## Rename a branch

To rename a branch:

<Steps>
  <Step>From the PlanetScale organization dashboard, select the desired database</Step>
  <Step>Navigate to the **Branches** page from the menu on the left</Step>
  <Step>Click on the three dots ("...") next to the branch you want to rename</Step>
  <Step>Select **Rename branch**</Step>
  <Step>Enter the new branch name</Step>
  <Step>Click **Save changes**</Step>
</Steps>

Renaming a branch does not affect that branch's credentials. You do not need to regenerate credentials if you rename a branch.

## Set as default branch

The default branch serves as the source branch when creating new development branches. To change the default branch:

### From the Branches page

<Steps>
  <Step>From the PlanetScale organization dashboard, select the desired database</Step>
  <Step>Go to the **Branches** tab in your database dashboard</Step>
  <Step>Click on the three dots ("...") next to the branch you want to set as default</Step>
  <Step>Click **Set as default branch**</Step>
</Steps>

### From the Settings page

<Steps>
  <Step>From the PlanetScale organization dashboard, select the desired database</Step>
  <Step>Navigate to the **Settings** page from the menu on the left</Step>
  <Step>Select the branch from the **Default branch** dropdown you want to be the default branch</Step>
  <Step>Scroll down and click **Save database settings**</Step>
</Steps>

If you change the default branch and intend for it to power your production application, you may need to update your application credentials to reference the new default branch.

## Delete a branch

You can delete a branch that you no longer need:

<Steps>
  <Step>From the PlanetScale organization dashboard, select the desired database</Step>
  <Step>Go to the **Branches** tab in your database dashboard</Step>
  <Step>Click on the three dots ("...") next to the branch you want to delete</Step>
  <Step>Select **Delete**</Step>
  <Step>Confirm the deletion</Step>
</Steps>

**Important notes:**

* You cannot delete the default branch. You must first set another branch as the default branch.
* You cannot set development branches as the default branch.
* Only [Organization Administrators and Database Administrators](/docs/security/access-control) have permission to delete production branches. Database Members can delete non-production branches.
* Development branches are billed only for the time they are used, so it's beneficial to delete them when no longer needed.

## Schema changes

Since PlanetScale Postgres branches don't use [deploy requests like in Vitess](/docs/vitess/schema-changes/deploy-requests), you make schema changes directly on each branch:

<Steps>
  <Step>Connect to your development branch</Step>
  <Step>Make your schema changes using standard PostgreSQL DDL commands</Step>
  <Step>Test your changes in the development environment</Step>
  <Step>When ready, manually apply the same changes to your production branch</Step>
</Steps>

There's currently no automated way to merge schema changes between PlanetScale Postgres branches. You must manually copy your changes from development to production branches.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt
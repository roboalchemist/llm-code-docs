# Source: https://planetscale.com/docs/vitess/tutorials/connect-mysql-gui.md

# Connect a MySQL GUI to PlanetScale

## Introduction

In this tutorial, you'll learn how to connect to a PlanetScale database using a MySQL GUI. While this tutorial uses Sequel Ace as a demonstration, many applications that connect to MySQL databases will support connecting to and querying a PlanetScale database as long as the applicaton supports connecting over SSL.

## Gather the credentials

To connect to a PlanetScale database, you'll need four pieces of information:

* The database name
* Host name
* Username
* Password

The easiest way to gather this information is by selecting the **Connect** button from the **Dashboard** tab. Then, on the **Connect** page, select the branch that you wish to connect to and click the **Create password** button. Within the **Select a language or framework** section, select "Other" to display the connection details as a list instead of a language or framework-specific connection string.

<Note>
  As a security best practice, passwords are only displayed when they are created.
</Note>

## Connect to the database

In the application you are using, enter the access information you gathered in the previous step into the appropriate fields. Make sure to check **"Require SSL"** as SSL is required to connect to a PlanetScale database. Click **"Connect"** once you are finished.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-mysql-gui/ace-connect.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=71ebdc9541dfc89bdc6bce8be56096d9" alt="The new connection window in Sequel Ace." data-og-width="1390" width="1390" data-og-height="953" height="953" data-path="docs/images/assets/docs/tutorials/connect-mysql-gui/ace-connect.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-mysql-gui/ace-connect.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=f469e702d200c1b9510d6b64b5a01424 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-mysql-gui/ace-connect.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=4f11670130c96ae8eab1fc6c2c8c23eb 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-mysql-gui/ace-connect.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=5a82118faac825e0d8d5d1402c032b44 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-mysql-gui/ace-connect.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=6e564e809d739026303d4883b2abd11f 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-mysql-gui/ace-connect.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=79e2f3ac9133d7c07327373ec7f5cfc0 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-mysql-gui/ace-connect.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=0b46a93847eee2ecf508630ad08419dd 2500w" />
</Frame>

If the connection is successful, you should be able to query your database and perform other [supported operations](/docs/vitess/troubleshooting/mysql-compatibility).

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-mysql-gui/ace-query.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=c09b6d81290dc195807777bd69c03c5e" alt="A sample query in Sequel Ace." data-og-width="1389" width="1389" data-og-height="909" height="909" data-path="docs/images/assets/docs/tutorials/connect-mysql-gui/ace-query.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-mysql-gui/ace-query.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=fbad5b50c91eb34868a9cc5ad1472fc4 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-mysql-gui/ace-query.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=cbbc20d09a9d798f73e9461083be6387 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-mysql-gui/ace-query.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=f0c2846c07edfb8df59f88d04fc9bd94 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-mysql-gui/ace-query.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=50f35996899c6d4c8b2f81359f867a22 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-mysql-gui/ace-query.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=838489b7ea951b2c94123f08b86d4305 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/connect-mysql-gui/ace-query.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=eb1fa75bb857be2e1654f297479e1907 2500w" />
</Frame>

## Caveats

While many standard MySQL statements are supported, there are a few caveats worth calling out:

<Steps>
  <Step>
    Each branch of a PlanetScale database is considered an isolated MySQL database. You'll need separate connection details per branch.
  </Step>

  <Step>
    Production branches with [safe migrations](/docs/vitess/schema-changes/safe-migrations) enforce the use of [branching](/docs/vitess/schema-changes/branching) and [deploy requests](/docs/vitess/schema-changes/deploy-requests) to safely make schema changes and do not support direct DDL as a result. However, DDL is supported on development branches and production branches without safe migrations enabled (not recommended).
  </Step>

  <Step>
    Creating new databases is not supported using any GUI tool.
  </Step>
</Steps>

## Tested GUIs

The following MySQL GUI applications have been tested and confirmed to work with PlanetScale databases:

<Columns cols={2}>
  <Card title="Sequel Ace" icon="rocket-launch" href="https://sequel-ace.com/" horizontal />

  <Card title="TablePlus" icon="table" href="https://tableplus.com/" horizontal />

  <Card title="MySQL Workbench" icon="desktop" href="https://www.mysql.com/products/workbench/" horizontal />

  <Card title="JetBrains DataGrip" icon="code" href="https://planetscale.com/blog/blog/using-planetscale-with-jetbrains-datagrip-mysql-gui" horizontal />
</Columns>

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt
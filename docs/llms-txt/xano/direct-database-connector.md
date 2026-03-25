# Source: https://docs.xano.com/xano-features/instance-settings/direct-database-connector.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Direct Database Connector

> Establish a direct connection to your instance's PostgreSQL database

## Note

Direct Database Connector is included with the Essential and Pro paid plans.

Database Connector is a premium add-on that is available for Launch and Scale plans. Please visit your Billing page for the most up-to-date pricing for this additional feature.

You have the option to connect your Xano instance's PostgreSQL database directly with an external application or service. This can be useful if there is a platform for manipulating your database that you prefer to use over the Xano interface, creating custom backup and restore solutions, or even performing data analytics.

Use care when accessing your database directly. This type of connection removes a significant portion of normal checks and balances for data validity that using Xano directly provides.

**Proceed with caution.**

**How to Access the Database Connector**

On your instance selection screen, click the⚙️ icon, and in the panel that opens, choose Database Connector.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/e31269f4-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=7e81e64ac9856cb12437448999aa1084" width="1257" height="328" data-path="images/e31269f4-image.jpeg" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/NAqNmVIgcJlXegps/images/04af0bc3-image.jpeg?fit=max&auto=format&n=NAqNmVIgcJlXegps&q=85&s=bedba7028c5ea6675280b9859d7a8dca" width="439" height="996" data-path="images/04af0bc3-image.jpeg" />
</Frame>

The panel that opens is split into two sections, Details and Settings.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/_Sd90ZcMa6hsPScv/images/d3405924-image.jpeg?fit=max&auto=format&n=_Sd90ZcMa6hsPScv&q=85&s=a0a521b6fad35f524d89ce43a7e9d41d" width="881" height="553" data-path="images/d3405924-image.jpeg" />
</Frame>

Details allows you to retrieve the access information for a direct database connection.

Settings allows you to enable and use an allow list, to limit direct database connections to specific IP addresses.

1. Get your database's public IP

2. Get your database credentials

3. Settings Panel

4. Add an IP address to your allow list

Clicking both of the "Get" buttons will provide us with the database IP and two sets of credentials, full-access and read-only.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/_oKnuVg5Nf4VhJM4/images/51abdd8f-image.jpeg?fit=max&auto=format&n=_oKnuVg5Nf4VhJM4&q=85&s=fe771d436ec6a299668844c8d38eca9e" width="427" height="812" data-path="images/51abdd8f-image.jpeg" />
</Frame>

From this panel, you can also **revoke and re-generate** your database credentials, should the need arise.

**Establishing a Database Connection (Example)**

You can use any application you'd like that is capable of connecting to a PostgreSQL database. In this example, we'll be using Navicat.

Select 'Connection' in the top-left, and fill in your credentials and the IP received from Xano.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/30e13433-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=2bc50844c36c42f122c0c0531e4e428c" width="1236" height="878" data-path="images/30e13433-image.jpeg" />
</Frame>

Click 'Save' to save the connection. We can now navigate the PostgreSQL database from Xano using Navicat. We can even add / update data, run queries, etc...

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/_FyaEhYRFYQZinJ0/images/df18d92b-image.jpeg?fit=max&auto=format&n=_FyaEhYRFYQZinJ0&q=85&s=9a7c6b8584f44a3f457c58b1526c8a1a" width="800" height="564" data-path="images/df18d92b-image.jpeg" />
</Frame>

## Table Format

## Table Formats - Only relevant for direct database connections

As of our **1.68 release (5/27/25)**, all new workspaces will default to the standard SQL column format for tables. For all workspaces created prior to that, read below.

Your tables can be created using one of two formats:

* **JSONB format**

  * This creates your tables with two columns:

    * `id` - the ID of the record

    * `jsonb` - contains a JSON representation of the entire record

* **Standard SQL format**

  * This creates a more standard table layout. Instead of a jsonb column, each column is written separately.

If you are using the [Direct Database Connector](/xano-features/instance-settings/direct-database-connector), Standard SQL format is usually recommended.

### Converting Tables from JSONB to standard SQL

<Warning>
  This change is **permanent**. Most users will not need to adjust these settings, and they only impact your experience if you are connecting to your database directly via third-party tools.
</Warning>

<Steps>
  <Step title="From your workspace dashboard, click the settings icon in the upper-right corner, and click Settings." />

  <Step title="Scroll down to the Database Preferences section, and check the option to 'Use standard SQL columns for new tables'">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/eb6ad281-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=46618b9fb76997b2da5873a1cd2bb54d" width="689" height="203" data-path="images/eb6ad281-image.jpeg" />
    </Frame>

    This setting must be enabled before you can convert existing tables to the new format.
  </Step>

  <Step title="Convert your table(s) from your workspace settings, or the settings of any table.">
    From the migration panel, select any of the tables you'd like to convert, and confirm your choices. The migration will begin immediately.

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/727090c5-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=b221e9dbfd6e8bb8ab6eba835bd292c8" width="763" height="1415" data-path="images/727090c5-image.jpeg" />
    </Frame>
  </Step>
</Steps>

## Custom SQL Table Names

From your Workspace settings, you can enable **Custom SQL Table Names**.

By default, Xano assigns each table a SQL name in the format mvpw\_ (e.g., mvpw1\_3). This identifier works for direct access, but can be difficult to read or use with direct queries and database tools.

You can replace this with a custom SQL name to make queries more intuitive and improve compatibility with external connectors.

If you change a table's SQL name, be sure to update any queries that reference the old name to avoid breaking functionality.

Once you've enabled **Custom SQL Table Names**, head to any database table's settings, and click Manage next to SQL Table Name.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/e3e08966-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=8b411bca8716c88da4700cee2b8e57fd" width="745" height="188" data-path="images/e3e08966-image.jpeg" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/pz6e9Ndbn8i3u8Zz/images/65aa79c8-image.jpeg?fit=max&auto=format&n=pz6e9Ndbn8i3u8Zz&q=85&s=dddc2fb2296af151ba47dd06794c7022" width="516" height="784" data-path="images/65aa79c8-image.jpeg" />
</Frame>

* Leave the SQL Table Name field blank to use Xano’s default SQL table name, which follows the format mvpw\<workspaceID>\_\<tableID> (e.g., mvpw1\_3).
* SQL table names must be globally unique across all workspaces. **Hint**: Use the Custom Prefix to ensure uniqueness across workspaces.
* Datasources automatically add a suffix based on their environment. For example, **users** becomes **users\_test** in the test datasource.\* To reuse the same base name across workspaces, use a workspace-specific prefix (e.g., projA\_users, projB\_users).


Built with [Mintlify](https://mintlify.com).
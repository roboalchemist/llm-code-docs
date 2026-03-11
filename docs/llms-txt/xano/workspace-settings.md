# Source: https://docs.xano.com/xanoscript/workspace-settings.md

# Source: https://docs.xano.com/xano-features/workspace-settings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Workspace Settings

> An explanation of all available workspace settings

## Before you begin

Please note that this page provides only a general overview of some settings. When relevant, each section will contain a link to that feature specific documentation, which is recommended reading before adjusting anything

## General Settings

<Info>
  This panel is accessible by heading to your workspace dashboard and clicking the ⋮ icon > Settings
</Info>

| Setting                                       | Purpose                                                                                                                                         |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Name\*<br />text                              | Give your workspace a unique name                                                                                                               |
| Description<br />text                         | A description of your workspace                                                                                                                 |
| Use Internal Documentation Tool<br />checkbox | Enables the Internal Documentation Tool for your function stacks--a plain text input typically used to house information such as example inputs |
| Show Start                                    | Enables the Start Page, which offers beginner guidance on working in Xano                                                                       |
| Show Marketplace                              | Enables the Marketplace, which contains snippets and extensions available for import into your Xano workspace                                   |
| AI Preferences                                | Accept AI specific license terms to use certain AI-powered features, such as our [AI Database Assistant](/xano-ai/ai-database-assistant)        |

## Data Sources

<Info>
  [Data Sources](/the-database/database-basics/data-sources) allow you to maintain separate databases with the same schema. Useful for maintaining things like separate production and testing data sets.
</Info>

| Setting | Purpose                                                                         |
| ------- | ------------------------------------------------------------------------------- |
| Manage  | Quick access to managing your data sources, such as browsing or adding new ones |
| Migrate | Allows you to migrate data from one data source to another                      |

## Branch Defaults

<Info>
  These are default settings related to what is logged in your [Request History](/maintenance-monitoring-and-logging/request-history)
</Info>

In your workspace settings, you can manage the request history for your entire workspace in the Branch Defaults panel.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/dyVYERTquSXdpw_-/images/9c38d0ca-image.jpeg?fit=max&auto=format&n=dyVYERTquSXdpw_-&q=85&s=b636196c618692d996a05b0ae63260c6" width="831" height="848" data-path="images/9c38d0ca-image.jpeg" />
</Frame>

From this panel, we can define the request history defaults for each object type (query, function, task, middleware, trigger) that maintains history.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/2a57b449-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=8d412eb62a28858ea471805170fa5715" width="397" height="596" data-path="images/2a57b449-image.jpeg" />
</Frame>

* **Enable / Disable** - Performs the selected action on the object type

* **Function Statement Limit** - The number of statements to record for each object type. You can choose between:

  * No statements

  * 100 statements

  * 1,000 statements

  * 10,000 statements

  * Store all statements

<Warning>
  Please note that request history utilizes your Database (SSD) storage. It is important to consider this when determining how many statements can be stored, or if they need to be stored at all.
</Warning>

#### Inheriting Settings

In each individual API, function, task, middleware, or trigger's settings, you can also control the request history for that object specifically.

By default, these will be set to **inherit**, which means it will obey the branch defaults. Otherwise, you can adjust this for specific objects as necessary.

## Middleware

<Info>
  Provides quick access to [Middleware](/the-function-stack/building-with-visual-development/middleware) settings
</Info>

## Clone Workspace

<Info>
  Creates a clone of your workspace
</Info>

Cloning a workspace will copy all database table schema, API groups, APIs, functions, addons, and tasks into another workspace. It will **not** copy the database table records.

## Export Workspace

<Info>
  Exports a copy of your workspace
</Info>

Exporting your data is done in the background and may take a significant amount of time to process depending on the amount of data in your workspace.

You may also include media attachments, but this may increase the export size and time significantly depending on the number of files.

**Once the export is complete, you will receive an email notification as well as a notification in Xano that your data is ready to be downloaded. This export will be available for 12 hours.**

## Xano Link

<Info>
  [Xano Link](/xano-features/advanced-back-end-features/xano-link) is a premium addon for syncing branches and database schema from one workspace to others.
</Info>

## Triggers

<Info>
  [Triggers](/the-function-stack/building-with-visual-development/triggers) allow you to build workflows that run based on when certain events happen, such as when a database record is added or when certain branch actions take place.
</Info>

## Statement Explorer

<Info>
  The [Statement Explorer](/maintenance-monitoring-and-logging/statement-explorer) allows you to search for instances of specific statements across your workspace, such as finding all Query All Records functions. This is useful for things like security audits and making sweeping changes or improvements across multiple workflows.
</Info>

## Realtime Settings

<Info>
  Access your [Realtime in Xano](/realtime/realtime-in-xano) settings from here
</Info>

## Reset Drafts

<Info>
  Resets all drafts in the current workspace
</Info>

Sometimes, you may want to clear out all drafts and revert fully back to published versions of your function stacks. This option allows you to quickly do so. It can also be useful in the rare circumstance that you have functions that are in draft state or have been recently published and are not behaving correctly.

This action is **not reversible**, so if you have questions, reach out to our support chat before proceeding.

## Compliance Center

<Info>
  Offers quick access to the [Compliance Center](/enterprise/enterprise-features/compliance-center), which is a premium feature that enables advanced auditing of the state of your workspace and actions of your team members
</Info>

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
  <Step title="From your workspace dashboard, click the settings icon in the upper-right corner, and click Settings.">
    &#x9;
  </Step>

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

<div className="flex justify-center">
  <table className="table-auto">
    <tbody>
      <tr>
        <td className="w-1/2">
          <Frame>
            <img src="https://mintcdn.com/xano-997cb9ee/pz6e9Ndbn8i3u8Zz/images/65aa79c8-image.jpeg?fit=max&auto=format&n=pz6e9Ndbn8i3u8Zz&q=85&s=dddc2fb2296af151ba47dd06794c7022" width="516" height="784" data-path="images/65aa79c8-image.jpeg" />
          </Frame>
        </td>

        <td>
          <ul>
            <li>Leave the SQL Table Name field blank to use Xano’s default SQL table name, which follows the format mvpw\<workspaceID>\_\<tableID> (e.g., mvpw1\_3).</li>
            <li>SQL table names must be globally unique across all workspaces. **Hint**: Use the Custom Prefix to ensure uniqueness across workspaces.</li>
            <li>Datasources automatically add a suffix based on their environment. For example, **users** becomes **users\_test** in the test datasource.\* To reuse the same base name across workspaces, use a workspace-specific prefix (e.g., projA\_users, projB\_users). </li>
          </ul>
        </td>
      </tr>
    </tbody>
  </table>
</div>


Built with [Mintlify](https://mintlify.com).
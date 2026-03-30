# Source: https://pipedream.com/docs/workflows/data-management/databases/working-with-sql.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Working With SQL

Pipedream makes it easy to interact with SQL databases within your workflows. You can securely connect to your database and use either pre-built no-code triggers and actions to interact with your database, or execute custom SQL queries.

## SQL Editor

With the built-in SQL editor, you access linting and auto-complete features typical of modern SQL editors.

<Frame>
  <img src="https://mintcdn.com/pipedream/xnRKrRxEtt3vxd6I/images/d979f2b8-sql-editor_jn2rpn.png?fit=max&auto=format&n=xnRKrRxEtt3vxd6I&q=85&s=0ced62255519048d4a1d0cb3be7fea19" width="3584" height="2020" data-path="images/d979f2b8-sql-editor_jn2rpn.png" />
</Frame>

## Schema Explorer

When querying a database, you need to understand the schema of the tables you’re working with. The schema explorer provides a visual interface to explore the tables in your database, view their columns, and understand the relationships between them.

* Once you connect your account with one of the [supported database apps](/workflows/data-management/databases/working-with-sql/#supported-databases), we automatically fetch and display the details of the database schema below
* You can **view the columns of a table**, their data types, and relationships between tables
* You can also **search and filter** the set of tables that are listed in your schema based on table or column name

<Frame>
  <img src="https://mintcdn.com/pipedream/nKh6d_6A4aXFb6xD/images/f0b69a83-Screenshot_2024-06-02_at_9.23.46_PM_q5lbxo.png?fit=max&auto=format&n=nKh6d_6A4aXFb6xD&q=85&s=af05658d69105eb60d18c7f12948d117" width="3584" height="2016" data-path="images/f0b69a83-Screenshot_2024-06-02_at_9.23.46_PM_q5lbxo.png" />
</Frame>

## Prepared Statements

Prepared statements let you safely execute SQL queries with dynamic inputs that are automatically defined as parameters, in order to help prevent SQL injection attacks.

To reference dynamic data in a SQL query, simply use the standard `{{ }}` notation just like any other code step in Pipedream. For example,

```sql  theme={null}
select *
  from products
  where name = {{steps.get_product_info.$return_value.name}}
  and created_at > {{steps.get_product_info.$return_value.created_at}}
```

**Prepared statement:**

<Frame>
  <img src="https://mintcdn.com/pipedream/h8oodpUDiyR1Ssvt/images/389adfd0-prepared-statement_lh1cat.png?fit=max&auto=format&n=h8oodpUDiyR1Ssvt&q=85&s=fe03de7a25a11d92440719f4834abc77" width="1423" height="481" data-path="images/389adfd0-prepared-statement_lh1cat.png" />
</Frame>

**Computed statement:**

<Frame>
  <img src="https://mintcdn.com/pipedream/xnRKrRxEtt3vxd6I/images/d9c3220b-computed-statement_pth31z.png?fit=max&auto=format&n=xnRKrRxEtt3vxd6I&q=85&s=9ed4aef65e71373eec78be39c66e59a4" width="1422" height="380" data-path="images/d9c3220b-computed-statement_pth31z.png" />
</Frame>

<Note>
  When you include step references in your SQL query, Pipedream automatically converts your query to a prepared statement using placeholders with an array of params.
</Note>

Below your query input, you can toggle between the computed and prepared statements:

<div className="relative pb-[calc(56.25%+41px)] h-0 w-full">
  <iframe
    src="https://demo.arcade.software/VdSr49JtAoLp0FXz0JBD?embed"
    title="Toggle Prepared and Computed Statements"
    loading="lazy"
    allowFullScreen
    allow="clipboard-write"
    className="absolute top-0 left-0 w-full h-full"
    style={{
    colorScheme: "light",
  }}
  />
</div>

## Getting Started

<Steps>
  <Step title="Select the Execute SQL Query action">
    * From the step selector in the builder, select the **Query a Database** action for the [relevant database app](/workflows/data-management/databases/working-with-sql/#supported-databases)

    <Frame>
      <img src="https://mintcdn.com/pipedream/nKh6d_6A4aXFb6xD/images/fe2f4d4c-database-actions-step-selector_sbrnzi.png?fit=max&auto=format&n=nKh6d_6A4aXFb6xD&q=85&s=5fc4d671db804bb6bc1d960f99ab1882" width="3584" height="2016" data-path="images/fe2f4d4c-database-actions-step-selector_sbrnzi.png" />
    </Frame>
  </Step>

  <Step title="Connect your account">
    * If you already have a connected account, select it from the dropdown. Otherwise, click **Connect Account** to configure the database connection.
    * Follow the prompts to connect your account, then click **Test connection** to ensure Pipedream can successfully connect to your database

    <Frame>
      <img src="https://mintcdn.com/pipedream/NF77kliJSewMqg65/images/245ffc8a-test-connection-mysql_bizpqk.png?fit=max&auto=format&n=NF77kliJSewMqg65&q=85&s=5a816e2410fa81db88db6d1c258cfb08" width="3584" height="2015" data-path="images/245ffc8a-test-connection-mysql_bizpqk.png" />
    </Frame>
  </Step>

  <Step title="Explore the schema">
    * Once you’ve successfully connected your account, you can explore the [database schema](/workflows/data-management/databases/working-with-sql/#schema-explorer) to understand the tables and columns in your database
  </Step>

  <Step title="Write and execute your query">
    * Write your SQL query in the editor — read more about [prepared statements](/workflows/data-management/databases/working-with-sql/#prepared-statements) above to reference dynamic data in your query
  </Step>
</Steps>

### Supported Databases

The [SQL editor](/workflows/data-management/databases/working-with-sql/#sql-editor), [schema explorer](/workflows/data-management/databases/working-with-sql/#schema-explorer), and support for [prepared statements](/workflows/data-management/databases/working-with-sql/#prepared-statements) are currently supported for these database apps:

* [MySQL](https://pipedream.com/apps/mysql)
* [PostgreSQL](https://pipedream.com/apps/postgresql)
* [Snowflake](https://pipedream.com/apps/snowflake)

Need to query a different database type? Let us know!

Built with [Mintlify](https://mintlify.com).

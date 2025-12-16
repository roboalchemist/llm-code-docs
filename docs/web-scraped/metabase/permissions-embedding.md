# Source: https://www.metabase.com/docs/latest/permissions/embedding

<div>

1.  [Home](/docs/latest/)
2.  [Permissions](/docs/latest/permissions/start)

</div>

<div>

[ v0.57 ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdib3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iY2hldnJvbiI+CjxwYXRoIG9wYWNpdHk9IjAuOSIgZD0iTTMgOC45NjMzOEwxNiAyMS45NjM0TDI5IDguOTYzMzgiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSI1IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) ]

-   [v0.56](/docs/v0.56)
-   [v0.55](/docs/v0.55)
-   [v0.54](/docs/v0.54)
-   [v0.53](/docs/v0.53)
-   [v0.52](/docs/v0.52)
-   [v0.51](/docs/v0.51)
-   [v0.50](/docs/v0.50)
-   [v0.49](/docs/v0.49)
-   [v0.48](/docs/v0.48)
-   [See more](/docs/all)

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj48cGF0aCBzdHJva2U9IiM1MDlFRTMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xNi4yODMgMTIuMjYgMTUuNSAxNWwtLjc4My0yLjc0YTQuMzMzIDQuMzMzIDAgMCAwLTIuOTc1LTIuOTc2TDkgOC41bDIuNzQtLjc4M2E0LjMzMyA0LjMzMyAwIDAgMCAyLjk3Ni0yLjk3NUwxNS41IDJsLjc4MyAyLjc0YTQuMzMzIDQuMzMzIDAgMCAwIDIuOTc1IDIuOTc2TDIyIDguNWwtMi43NC43ODNhNC4zMzQgNC4zMzQgMCAwIDAtMi45NzYgMi45NzVsLS4wMDEuMDAxWk02LjUgMjJsLjU5MS0xLjc3NGEzLjM3NSAzLjM3NSAwIDAgMSAyLjEzNS0yLjEzNUwxMSAxNy41bC0xLjc3NC0uNTkxYTMuMzc1IDMuMzc1IDAgMCAxLTIuMTM1LTIuMTM0TDYuNSAxM2wtLjU5MSAxLjc3NGEzLjM3NSAzLjM3NSAwIDAgMS0yLjEzNCAyLjEzNUwyIDE3LjVsMS43NzUuNTkxYTMuMzc1IDMuMzc1IDAgMCAxIDIuMTM0IDIuMTM0TDYuNSAyMloiPjwvcGF0aD48L3N2Zz4=) What's new](/releases)

</div>

<div>

</div>

# Configuring permissions for embedding

You can use a single Metabase to manage permissions for all of your customers. Which Metabase permissions tool you use depends on how you store your customer data.

-   [One database for all customers (commingled setups)](#one-database-for-all-customers-commingled-setups)
-   [One database per customer](#one-database-per-customer)
-   [One schema per customer](#multiple-schemas-one-schema-per-customer)

## One database for all customers (commingled setups)

If all your customer data is in the same schema and on the same tables (often referred to as "data commingling"):

  Tenant_ID   Column 1   Column 2
  ----------- ---------- ----------
  A           ...        ...
  B           ...        ...
  C           ...        ...

You could use:

-   [Row and column security](./row-and-column-security) to restrict rows and columns.
-   [Connection impersonation](./impersonation) to mimic roles set by your database. Impersonation is a good choice if you want to grant native SQL access to your data.

### Restricting rows based on tenant ID

Let's say you have a table called **Data** that looks like this:

  Tenant_ID   Metrics   Insights
  ----------- --------- ----------
  A           ...       ...
  B           ...       ...
  C           ...       ...

To display a filtered version of **Data** to different tenants based on a `Tenant_ID`, you can apply [row and column security](./row-and-column-security).

That means Tenant A will see the rows where `Tenant_ID = A`, and Tenant B will see the rows where `Tenant_ID = B`.

Here's how the basic row-level security will work:

1.  **Create a group**, for example "Restricted Tenants", and add people's Metabase accounts to that group.
2.  **Add a user attribute**. For each person's account, [add a user attribute](../people-and-groups/managing#adding-a-user-attribute) like `Tenant_ID`, with the user attribute value set to "A", "B", or "C".
3.  **Add row-level security** to the table for that group. See [row and column security](./row-and-column-security)

### Restricting columns based on tenancy

Let's say your **Insights** column is a premium feature, and Tenant B is the only customer paying to see these **Insights**.

  Tenant ID   Metrics   Insights
  ----------- --------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  A           ...       ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ij48cGF0aCBkPSJNNC41MyAzLjQ3YS43NS43NSAwIDAgMC0xLjA2IDEuMDZMNi45NCA4bC0zLjQ3IDMuNDdhLjc1Ljc1IDAgMSAwIDEuMDYgMS4wNkw4IDkuMDZsMy40NyAzLjQ3YS43NS43NSAwIDEgMCAxLjA2LTEuMDZMOS4wNiA4bDMuNDctMy40N2EuNzUuNzUgMCAwIDAtMS4wNi0xLjA2TDggNi45NCA0LjUzIDMuNDd6IiBzdHJva2U9IiNFRjhDOEMiIGZpbGw9IiNFRjhDOEMiPjwvcGF0aD48L3N2Zz4=)
  B           ...       ...
  C           ...       ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ij48cGF0aCBkPSJNNC41MyAzLjQ3YS43NS43NSAwIDAgMC0xLjA2IDEuMDZMNi45NCA4bC0zLjQ3IDMuNDdhLjc1Ljc1IDAgMSAwIDEuMDYgMS4wNkw4IDkuMDZsMy40NyAzLjQ3YS43NS43NSAwIDEgMCAxLjA2LTEuMDZMOS4wNiA4bDMuNDctMy40N2EuNzUuNzUgMCAwIDAtMS4wNi0xLjA2TDggNi45NCA0LjUzIDMuNDd6IiBzdHJva2U9IiNFRjhDOEMiIGZpbGw9IiNFRjhDOEMiPjwvcGF0aD48L3N2Zz4=)

To keep A and C from viewing the `Insights` column, you can add [column-level security](./row-and-column-security) to restrict both the rows and columns they see when they view the table.

1.  **Create a group** called "Metrics-Only Tenants".

2.  **Add Tenants A and C to the group**. When restricting data, make sure that each Metabase account only belongs to a single group.

3.  [Add a user attribute](../people-and-groups/managing#adding-a-user-attribute) like `Tenant_ID`, with the user attribute value set to "A" or "C".

4.  Next, you'll create a SQL question using the **Data** table like this:

    ::: 
    ::: highlight
    ``` highlight
    SELECT Tenant_ID, Metrics
    FROM data
    WHERE Tenant_ID =  } 
    ```
    :::
    :::

5.  Save the SQL question as "Customer Metrics".

6.  [Add row and column security](./row-and-column-security#custom-row-and-column-security-use-a-sql-question-to-create-a-custom-view-of-a-table) using the "Metrics-Only Tenants" group and "Customer Metrics" SQL question.

When, for example, Tenant A logs in, they'll only see the `Tenant_ID` and `Metrics` columns, and only the rows where `Tenant_ID = A`.

### Impersonation lets you manage access with database roles

Impersonation lets you map user attributes to database roles, which lets you do row-level security based on the database privileges you give each role.

Check out this [article on impersonation](/learn/metabase-basics/administration/permissions/impersonation).

## One database per customer

If each of your customers has their own database, you can use [database routing](./database-routing) to swap out the data source for queries. With DB routing, you just need to build a dashboard once, and Metabase will switch the database it queries depending on who's logged in.

For database routing to work, however, the schemas in each database must be identical.

For more fine-grained control over what individuals can see, even within the same tenants, you can also use the other tools Metabase provides, like [row and column security](./row-and-column-security) and [connection impersonation](./impersonation), in combination with database routing.

## Multiple schemas (one schema per customer)

If your customer data is stored in separate tables in the same schema or different schemas within one database, like this:

**Tenant A's schema**

  Tenant A   Column 1   Column 2
  ---------- ---------- ----------
  Row 1      ...        ...
  Row 2      ...        ...
  Row 3      ...        ...

**Tenant B's schema**

  Tenant B   Column 1   Column 2
  ---------- ---------- ----------
  Row 1      ...        ...
  Row 2      ...        ...
  Row 3      ...        ...

You could:

-   [Grant self-service or view-only access to a schema](#granting-customers-self-service-or-view-only-access-to-their-schema).
-   [Grant native SQL access to a schema](#granting-customers-native-sql-access-to-their-schema).

Unlike commingled data, one-schema-per-customer data is incompatible with row and column security, because it works at the table level, not the schema level.

### Granting customers self-service or view-only access to their schema

Say you have a single database with ten different tables, each corresponding to a different customer (company). You want each customer to only access their own table.

1.  **Create a group** for your first customer in **Admin settings** \> **People**. If you need different permission levels within a company (some employees can ask questions, others can only view), create multiple groups like **Company A (Self-service)** and **Company A (View only)**.

2.  **Grant table access** by going to **Permissions** \> **Data** \> **Databases** and granting your new group access to the customer's table. If you want customers to create questions and dashboards within their table, set **Create query** permissions to **Query builder**.

    For employees who should only view data and create collections to house those specific questions and dashboards, see [collection permissions](./collections).

    Avoid granting native SQL editor access --- it lets people query tables they shouldn't see.

    If you scope each group's permissions to a single table, Metabase will hide any new tables you add to the database.

3.  **Invite your first user** and add them to the appropriate group. If you're using [SSO](../people-and-groups/google-sign-in), you can skip this step.

4.  **Repeat the process** for each customer by following steps 1--3.

### Granting customers native SQL access to their schema

If you need native SQL queries:

1.  **Create a database-level user account** for your first customer (in your database, not in Metabase). This database user should only have access to their specific tables or schema. For PostgreSQL for example, you could add a user via psql and only grant them permissions to their tables.

2.  **Connect Metabase to your database** using the database user account you just created. See [databases](../databases/connecting).

3.  **Create a new group** in Metabase and grant it access to the new database connection. Since the database user role controls what's visible, you can grant the group **Can view** access to the database and **Query builder and native** access. See [groups](../people-and-groups/managing#groups).

    Group members will see all tables that the database user can access. To hide tables later, you'll need to change permissions in the database itself, not Metabase.

4.  **Invite your first user** and add them to the appropriate group. If you're using [SSO](../people-and-groups/google-sign-in), you can skip this step.

5.  **Repeat the process** for each customer by following steps 1-4. You'll end up with as many database connections as customers.

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/permissions/embedding.md) ]
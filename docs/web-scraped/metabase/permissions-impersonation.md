# Source: https://www.metabase.com/docs/latest/permissions/impersonation

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

# Impersonation permissions

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNiAyNiIgZmlsbD0ibm9uZSI+CiAgPHBhdGggZD0iTTEyIDEzVjE1IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlPSIjNTA5RUUzIj48L3BhdGg+CiAgPHBhdGggZD0iTTEyIDEwQzEyLjU1MjMgMTAgMTMgOS41NTIyOCAxMyA5QzEzIDguNDQ3NzIgMTIuNTUyMyA4IDEyIDhDMTEuNDQ3NyA4IDExIDguNDQ3NzIgMTEgOUMxMSA5LjU1MjI4IDExLjQ0NzcgMTAgMTIgMTBaIiBmaWxsPSIjNTA5RUUzIj48L3BhdGg+CiAgPHBhdGggZD0iTTEyIDE5LjI1QzE2LjAwNDEgMTkuMjUgMTkuMjUgMTYuMDA0MSAxOS4yNSAxMkMxOS4yNSA3Ljk5NTk0IDE2LjAwNDEgNC43NSAxMiA0Ljc1QzcuOTk1OTQgNC43NSA0Ljc1IDcuOTk1OTQgNC43NSAxMkM0Ljc1IDE2LjAwNDEgNy45OTU5NCAxOS4yNSAxMiAxOS4yNVoiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZT0iIzUwOUVFMyI+PC9wYXRoPgo8L3N2Zz4=)

Impersonation access is only available on [Pro](/product/pro) and [Enterprise](/product/enterprise) plans (both self-hosted and on Metabase Cloud).

This page covers the [View data](./data#view-data-permissions) permission level called Impersonation.

**Impersonation access** allows admins to "outsource" View data permissions to roles in your database. Admins can associate user attributes with database-defined roles and their privileges. If someone is in a group with their View data permission set to Impersonation, the person will be able to view and query data based on the privileges granted to the role specified by their user attribute.

## Databases that support impersonation

For now, impersonation access is only available for the following databases:

-   ClickHouse
-   MySQL
-   PostgreSQL. If you're using views in PostgreSQL, the row-level security policies on views will only work on Postgres versions 15 and higher.
-   Redshift
-   Snowflake
-   SQL Server
-   Starburst/Trino.

If you want to switch database *connections* based on who is logged in, check out [Database routing](./database-routing).

## Impersonation vs row and column security

### Impersonation sets permissions for questions written in both the SQL editor and the query builder

Impersonation operates at the database level. In a database engine, setting the role before the query runs can alter the results of the query, as the role defines the permissions that your database should use when it executes the statements.

### Row and column security only sets permissions for query builder questions

Row and column security operates at the Metabase level. Since Metabase can't parse SQL queries to find out what data people are allowed to view, row and column security only applies to questions composed in the query builder (where Metabase can interpret the queries).

## Example use case for impersonation

Let's say we have a People table that includes rows of accounts from all 50 states of the United States. Let's say you want your Vermont sales team to:

-   Be able to ask questions using both the query builder and the native SQL editor.
-   Only be able to view customer accounts in the People table who live in Vermont.

First, you'll set up permissions in your database by creating a role with a policy. Then in Metabase, you'll set data access to that database to Impersonation, so when people run queries on that database, Metabase will use that role to limit what data they can see.

## Set up connection impersonation

For impersonation access to work, you'll first need to set up roles in your database for Metabase to impersonate, then configure Metabase to impersonate those roles when people view or query data.

### Set up Metabase database connection for impersonation

Impersonation uses database roles to run queries on your database, but there still needs to be a default role that will be used to run operations like [sync, scans, and fingerprinting](../databases/sync-scan). So the user account that Metabase uses to [connect to your database](../databases/connecting) should have access to everything in that database that any Metabase group may need access to, as that database user account is what Metabase uses to sync table information.

You can then create roles in the database that have more restrictive access to the database (like row-level or table-level security). When the role is passed to the database using impersonation, the engine will return a subset of the data, or restrict the query altogether.

> For **Redshift** databases, the user account Metabase uses to [connect to your Redshift database](../databases/connections/redshift) must be a superuser, as Metabase will need to be able to run the [SET SESSION AUTHORIZATION](https://docs.aws.amazon.com/redshift/latest/dg/r_SET_SESSION_AUTHORIZATION) command, which can only be run by a database superuser.

### In your database, set up roles

In your database (not in Metabase):

1.  Create a new database role (in Redshift, this would be a new user).
2.  Grant that role privileges that you'd like impersonated users to have..

For exactly how to create a new role in your database and grant that role privileges, you'll need to consult your database's documentation. We also have some docs on [users, roles, and privileges](../databases/users-roles-privileges) that can help you get started.

For example, if you're using PostgreSQL, the SQL below will create a role called `vermont_sales_team` and only allow that role to select rows in the `people` table where the value in the `state` column is `VT` (the abbreviation for Vermont):

``` highlight
CREATE ROLE vermont_sales_team;

GRANT
SELECT ON ALL TABLES IN SCHEMA PUBLIC TO vermont_sales_team;

CREATE POLICY vermont ON people
FOR
SELECT TO vermont_sales_team USING (state = 'VT');

ALTER TABLE people ENABLE ROW LEVEL SECURITY;
```

### Snowflake connections should disable secondary roles when using impersonation

For impersonation to work correctly with **Snowflake** databases, the user account Metabase uses to [connect to your Snowflake database](../databases/connections/snowflake) must have [secondary roles](https://docs.snowflake.com/en/user-guide/security-access-control-overview#authorization-through-primary-role-and-secondary-roles) disabled. You can disable secondary roles with:

``` highlight
ALTER USER metabase_user SET DEFAULT_SECONDARY_ROLES = ();
```

If you don't disable secondary roles, each impersonated role will also get permissions of all other roles you've granted to the Metabase user.

### Set up a Metabase group

Permissions in Metabase, including impersonation, are managed by groups, so you'll need to:

1.  [Create a new group](../people-and-groups/managing#groups) (or select an existing one).
2.  [Add people to the group](../people-and-groups/managing#adding-people-to-groups).

You might want to create a test user and add them to the group to verify later that impersonation is working correctly.

### Assign a user attribute to people in the group

To associate people in the group with a role that you created in your database, you'll use a user attribute.

Assign a [user attribute](../people-and-groups/managing#adding-a-user-attribute) to people in your group:

-   The **key** of the attribute can be anything.
-   The **value** of the attribute must match the desired database role for every person.

![Setting a user attribute for impersonation](./images/user-attribute-impersonation.png)

For example, if you created a role named `vermont_sales_team` in your database with access to a subset of data relevant to the Vermont sales team (like [in the example above](#in-your-database-set-up-roles)), you could add a user attribute called `db_role` (or whatever you want to call the attribute) and assign the value `vermont_sales_team` to the person's `db_role` attribute.

Some databases enforce case sensitivity, so you might want to make sure the attribute's value and the database's role match exactly.

People in one group can have different attribute values, but must have the same attribute key. See [People in a group with impersonation access to data do not necessarily share the same privileges](#people-in-a-group-with-impersonation-access-to-data-do-not-necessarily-share-the-same-privileges).

### Set up impersonation

1.  In Metabase, hit Cmd/Ctrl + K to bring up the command palette and search for **Permissions**, or go directly to **Admin settings** \> **Permissions** \> **Data**.

2.  Select the group that you want to associate with the database role you created.

3.  Select the database to configure access to.

4.  Under **View data** setting for that database, select **Impersonation**. This option will only be visible if you already [created a user attribute](#assign-a-user-attribute-to-people-in-the-group).

    ![Select impersonated permissions](./images/select-impersonated.png)

    If your All Users group has more permissive access to this database (for example, "Can view"), you will see a warning, because [Metabase gives people the most permissive access to data across all of their groups](#metabase-gives-people-the-most-permissive-access-to-data-across-all-of-their-groups). You'll need to [block database access for the All Users group](./data#revoke-access-even-though-all-users-has-greater-access) before setting up impersonation.

5.  From the user attribute dropdown, select the user attribute that you added that maps to the role you want the group to use when querying the database.

6.  Save your changes.

Remember to also set up ["Create queries"](./data#create-queries-permissions) permissions for your group and database. For example, if you'd like people to be able to write SQL while using impersonated database roles, you'll need to set "Create queries" permissions to "Query builder and native".

### Verify that impersonated permissions are working

Admins will not be able to verify that impersonation is are working from their own account, so you should create a test user, add them to the group and set up their user attributes.

To verify that the impersonated permissions are working:

-   If the test user has "Create queries" permissions set to "Create queries and native", create a SQL question and verify that the test user can only see the right data.

For example, for the `vermont_sales_team` role from the [example above](#in-your-database-set-up-roles), you can run:

``` highlight
SELECT * FROM people;
```

to verify that the test user only sees data from Vermont.

-   If the test user has "Create queries" permissions set to "Query builder only", go to **Browse data** in the left sidebar and verify that the user can only see the tables they have access to, and only the data in those tables that

## People in a group with impersonation access to data do not necessarily share the same privileges

Metabase will use whatever role you specify in the user attribute for each person. E.g., if you select the `db_role` attribute for impersonation, one person's `db_role` could be `sales`, another person's could be `engineering`, or whatever other value that maps to a valid role in your database.

## Use impersonation to set up row-level SQL access

You can use impersonation to give people access to the SQL editor, while restricting their access to data based on a specific database role. And not just table-level access, but row-level access---or however you define access for that role in your database. Effectively, you can use impersonation to set up row and column security-like access to your data, while letting people use the SQL editor to query that data. The difference is that, *instead of setting up row and column security in Metabase, you need to set up that row-level security via the privileges granted to a role in your database.*

If instead you want to give a group SQL access to some, but not all, of the schemas or tables in that database, you can create an additional role in your database that only includes a subset of those tables---or even specific row-level access---and then use Metabase's impersonation feature to associate a user attribute with that role. Essentially what Metabase will do is take the user attribute and pass that attribute as a string into a `SET ROLE` or `USE ROLE` command for the database *before* Metabase executes the query.

Connection impersonation doesn't apply to people in the Metabase Admins group, as their more permissive privileges take precedence.

## Metabase gives people the most permissive access to data across all of their groups

So if a person is in two groups with different permissions for the same database:

-   Red group with impersonated access that limits what they can see.
-   Blue group with View data set to "Can view" and Create queries set to "Query builder and native".

Blue group's more permissive access would override the impersonated access.

## Admins won't see the effects of impersonation

Admins won't ever see the effects of impersonation effects, because their privileges will override those of any other group they're a member of.

Metabase's default Administrators group has "Can view" access to all databases, and Metabase uses the most permissive access for any person in multiple groups, so any admin will have "Can view" - not "Impersonated" - access to the database.

To test impersonation, create a test user, assign them a user attribute with the database role, and add them to the impersonated group. Then, log in as the test user and verify the data access.

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/permissions/impersonation.md) ]
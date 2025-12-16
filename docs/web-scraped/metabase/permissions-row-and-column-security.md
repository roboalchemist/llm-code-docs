# Source: https://www.metabase.com/docs/latest/permissions/row-and-column-security

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

# Row and column security

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNiAyNiIgZmlsbD0ibm9uZSI+CiAgPHBhdGggZD0iTTEyIDEzVjE1IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlPSIjNTA5RUUzIj48L3BhdGg+CiAgPHBhdGggZD0iTTEyIDEwQzEyLjU1MjMgMTAgMTMgOS41NTIyOCAxMyA5QzEzIDguNDQ3NzIgMTIuNTUyMyA4IDEyIDhDMTEuNDQ3NyA4IDExIDguNDQ3NzIgMTEgOUMxMSA5LjU1MjI4IDExLjQ0NzcgMTAgMTIgMTBaIiBmaWxsPSIjNTA5RUUzIj48L3BhdGg+CiAgPHBhdGggZD0iTTEyIDE5LjI1QzE2LjAwNDEgMTkuMjUgMTkuMjUgMTYuMDA0MSAxOS4yNSAxMkMxOS4yNSA3Ljk5NTk0IDE2LjAwNDEgNC43NSAxMiA0Ljc1QzcuOTk1OTQgNC43NSA0Ljc1IDcuOTk1OTQgNC43NSAxMkM0Ljc1IDE2LjAwNDEgNy45OTU5NCAxOS4yNSAxMiAxOS4yNVoiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZT0iIzUwOUVFMyI+PC9wYXRoPgo8L3N2Zz4=)

Row and column security is only available on [Pro](/product/pro) and [Enterprise](/product/enterprise) plans (both self-hosted and on Metabase Cloud).

Row and column security lets you give granular permissions for different groups of people. You can change what data a group [can view](./data#can-view-data-permission), as well as what data a group [can query](./data#create-queries-permissions) with the query builder.

You can use row and column security to set up [self-service analytics](/learn/metabase-basics/embedding/multi-tenant-self-service-analytics), so that each of your customers can only view the rows that match their customer ID. For example, if you have an Accounts table with information about your customers, you can add permissions to the table so that each customer only sees the data relevant to them.

> Row and column security was formerly called data sandboxing. It's the same feature, it just now has a more descriptive name.

## Row and column security examples

You can skip the theory and go [straight to examples of row and column security](row-and-column-security-examples).

## How row and column security works

You can think of row and column security as a bundle of permissions that includes:

-   The filtered version of a table that will replace your original table, everywhere that the original table is used in Metabase.
-   The [group](../people-and-groups/managing#groups) of people who should see the filtered version of the table.

You can define up to one row and column security policy for each table/group combo in your Metabase. This means you can display different versions of a table for different groups, such as "Accounts for Sales" to your salespeople, and "Accounts for Managers" for sales managers.

## Types of row and column security

Row and column security show specific data to each person based on their [user attributes](../people-and-groups/managing#adding-a-user-attribute). You can:

-   [Restrict **rows**](#row-level-security-filter-by-a-column-in-the-table)
-   [Restrict **columns** and rows](#custom-row-and-column-security-use-a-sql-question-to-create-a-custom-view-of-a-table) for specific people.

  Goal                                             Row (filter by a column in the table)   Custom (use a saved SQL question)
  ------------------------------------------------ --------------------------------------- -----------------------------------
  Restrict rows by filtering on a single column    ✅                                      ✅
  Restrict rows by filtering on multiple columns   ❌                                      ✅
  Restrict columns                                 ❌                                      ✅
  Edit columns                                     ❌                                      ✅

### Row-level security: filter by a column in the table

You can **restrict rows** by filtering a column using a [user attribute value](#choosing-user-attributes-for-row-and-column-security).

For example, you can filter the Accounts table for a group so that the user attribute filters the table:

-   "Basic" will see rows where `Plan = "Basic"` (rows where the Plan column matches the value "Basic").
-   "Premium" will see the rows where `Plan = "Premium"` (rows where the Plan column matches the value "Premium").

### Custom row and column security: use a SQL question to create a custom "view" of a table

To **restrict rows *and* columns**, you can use a SQL question to filter the table. When someone views that table, they'll instead see the question's results, not the raw table.

For example, say your original Accounts table includes the columns: `ID`, `Email`, `Plan`, and `Created At`. If you want to hide the Email column, you can create a "Restricted Accounts" SQL question with the columns: `ID`, `Plan`, and `Created At`.

You can use a question to:

-   [Display an edited column instead of hiding the column](#displaying-edited-columns).
-   [Pass a user attribute to a SQL parameter](#restricting-rows-with-user-attributes-using-a-sql-variable).

## Prerequisites for row security

-   A [group](../people-and-groups/managing#groups) of people to add row security.
-   [User attributes](../people-and-groups/managing#adding-a-user-attribute) for each person in the group.

Row security displays a filtered table, in place of an original table, to a specific group. How Metabase filters that table depends on the value in each person's user attribute.

For example, you can set up a row-level security so that the user attribute `plan` shows different rows for different values:

-   "Basic" will see a version of the Accounts table with a filter for `Plan = "Basic"` (that is, only the rows where the Plan column matches the value "Basic").
-   "Premium" will see a different version of the Accounts table with the filter `Plan = "Premium"` applied.

## Choosing user attributes for row and column security

**User attributes are required for row security, and optional for column security**. When [adding a new user attribute](../people-and-groups/managing#adding-a-user-attribute), you'll set up a key-value pair for each person.

Metabase uses the user attribute key to look up the user attribute value for a specific person. User attribute keys can be mapped to parameters in Metabase.

The **user attribute value** must be an exact, case-sensitive match for the filter value. For example, if you add row security to the Accounts table with the filter `Plan = "Basic"`, make sure that you enter "Basic" as the user attribute value. If you set the user attribute value to lowercase "basic" (a value which doesn't exist in the Plan column of the Accounts table), the person will get an empty result instead of the table.

Examples of user attributes in play:

-   [Row security](./row-and-column-security-examples#filtering-rows-based-on-user-attributes)
-   [Restricting rows and columns](./row-and-column-security-examples#custom-example-2-filtering-rows-and-columns)

## Adding row-level security

1.  Make sure to do the [prerequisites for row security](#prerequisites-for-row-security) first.
2.  Go to **Admin settings** \> **Permissions**.
3.  Select the database and table that you want to secure.
4.  Find the group that you want to put in the secure.
5.  Click on the dropdown under **View data** for that group.
6.  Select "Row and column security".
7.  Click the dropdown under **Column** and enter the column to filter the table on, such as "Plan".
8.  Click the dropdown under **User attribute** and enter the user attribute **key**, such as "Plan".

> If you have SQL questions that query data with row-level security, make sure to move all of those questions to admin-only collections. For more info, see [You cannot secure the rows or columns of SQL results](#you-cannot-secure-the-rows-or-columns-of-sql-results).

Check out [row and column security examples](./row-and-column-security-examples).

## Prerequisites for column-level security

-   A [group](../people-and-groups/managing#groups) of people.
-   An admin-only [collection](../exploration-and-organization/collections), with [collection permissions](../permissions/collections) set to **No access** for all groups except Administrators.
-   A [SQL question](../questions/native-editor/writing-sql) with the rows and columns to be displayed to the people in the group, stored in the admin-only collection.
-   Optional: if you want to restrict **rows** as well, set up [user attributes](#choosing-user-attributes-for-row-and-column-security) for each of the people in the group.

### Creating a SQL question for Metabase to display instead of a table

Metabase will display the results of the question in place of an original table to a particular group.

**Use a SQL question** to define the exact rows and columns to be included in the custom view. Avoid using a query builder (GUI) question, as you might accidentally expose extra data, since GUI questions can include data from other questions or models.

> Make sure to save the SQL question in an admin-only collection ([collection permissions](../permissions/collections) set to **No access** for all groups except Administrators). For more info, see [You cannot secure the rows or columns of SQL results](#you-cannot-secure-the-rows-or-columns-of-sql-results).

### Displaying edited columns

Aside from excluding rows and columns, you can also **display edited columns** (without changing the columns in your database).

For example, you can create a "Edited Accounts" SQL question that truncates the Email column to display usernames instead of complete email addresses.

If you edit a column, the schema of the SQL question (the question you want to display instead of the table) must match the schema of the original table. That means the "Edited Accounts" SQL question must return the same number of columns and corresponding data types as the original Accounts table.

You cannot add columns.

## Setting up column security

1.  Make sure to do the [prerequisites](#prerequisites-for-column-level-security) first.
2.  Go to **Admin settings** \> **Permissions**.
3.  Select the database and table that you want to secure.
4.  Find the group to restrict.
5.  Click on the dropdown under **Data access** for that group.
6.  Select "Row and column security".
7.  Select "Use a saved question to create a custom view for this table".
8.  Select your saved question. The question should be written in SQL. If the question contains parameters, those parameters must be required (they cannot be optional).
9.  Optional: [restrict rows based on people's user attributes](#restricting-rows-with-user-attributes-using-a-sql-variable).

You can find sample setups in the [Row and column security examples](./row-and-column-security-examples).

### Restricting rows with user attributes using a SQL variable

If you set up column security, you can also restrict different rows for each person depending on their [user attributes](../people-and-groups/managing#adding-a-user-attribute). For example, you can display the "Accounts" question with the filter `Plan = "Basic"` for one group, and the filter `Plan = "Premium"` for another group.

1.  Make sure you've done all the [prerequisites for column-level security](#prerequisites-for-column-level-security).
2.  Go to the SQL question that will be displayed to the people in place of the table.
3.  Add a [parameterized](../questions/native-editor/sql-parameters) `WHERE` clause to your SQL query, such as `WHERE plan = } `.
4.  Save the SQL question.
5.  Go to **Admin settings** \> **Permissions**.
6.  Find the group and table you want to secure.
7.  Open the dropdown under **View data**.
8.  Click **Edit row and column security**.
9.  Scroll down and set **Parameter or variable** to the name of the parameter in your SQL question (such as "Plan Variable").
10. Set the **User attribute** to a [user attribute key](#choosing-user-attributes-for-row-and-column-security) (such as the key "User's Plan", *not* the value "Basic").
11. Click **Save**.

For a sample SQL variable and user attribute setup, see the [Row and column security examples](./row-and-column-security-examples).

### How row restriction works with column security

A standard `WHERE` clause filters a table by setting a column to a fixed value:

``` highlight
WHERE column_name = column_value
```

In step 2 of the [row restriction setup](#restricting-rows-with-user-attributes-using-a-sql-variable) above, you'll add a SQL variable so that the `WHERE` clause will accept a dynamic value. The [SQL variable type](../questions/native-editor/sql-parameters#sql-variable-types) must be text, number, or date:

``` highlight
WHERE plan = }
```

In steps 9-10 of the [row restriction setup](#restricting-rows-with-user-attributes-using-a-sql-variable) above, you're telling Metabase to map the SQL variable `plan_variable` to a **user attribute key** (such as "User's Plan"). Metabase will use the key to look up the specific **user attribute value** (such as "Basic") associated with a person's Metabase account. When that person logs into Metabase and uses the secured table, they'll see the query result that is filtered on:

``` highlight
WHERE plan = "Basic"
```

Note that the parameters must be required for SQL questions used to create custom views. For example, you can't use an optional parameter; the following won't work:

``` highlight
[[WHERE plan = }]]
```

Learn more about [SQL parameters](../questions/native-editor/sql-parameters)

### Advanced row-level security: filtering tables for people that have multiple IDs

For example, say have a table like this:

  User_ID   Value
  --------- -------
  1         10
  1         50
  2         5
  2         50
  3         5
  3         5

If you want to give someone access to multiple user IDs (e.g., the person should see rows for both `User_ID` 1 and 2.), you can set up a user attribute, like `user_id` that can handle comma-separated values like "1,2".

1.  Create a SQL question that parses the comma-separated string and filters the table:

``` highlight
SELECT *
FROM users_with_values
WHERE user_id = ANY(STRING_TO_ARRAY(REGEXP_REPLACE(TRIM(}), '\\s*,\\s*', ','), ','))
```

This query:

-   Trims whitespace from the user attribute value
-   Replaces any spaces around commas with just commas
-   Converts the comma-separated string to an array
-   Filters rows where the user_id matches any value in the array

The `STRING_TO_ARRAY()` and `REGEXP_REPLACE()` functions are PostgreSQL-specific. To see which functions your database supports, see your database's documentation.

1.  Set up the row and column security using this SQL question. See [setting up column security](#setting-up-column-security).

## Preventing row and column security permissions conflicts

Some Metabase permissions can conflict with row and column security to give more permissive or more restrictive data access than you intended.

Say you've set up [column security](#custom-row-and-column-security-use-a-sql-question-to-create-a-custom-view-of-a-table) that hides the Email column from the Accounts table (for a particular group).

The Email column may get exposed to someone if:

-   The person belongs to [multiple row and column security policies](#multiple-row-and-column-security-permissions).
-   Someone else in a non-secured group shares the Email column from:
    -   A [SQL question](../questions/native-editor/writing-sql)
    -   A [public link](#public-sharing)
    -   An [alert, or dashboard subscription](../permissions/notifications)

### Multiple row and column security permissions

Multiple row and column security policies on the same table can create a permissions conflict. You can add a person to a maximum of one row and column security policy per table (via the person's group).

For example, if you have:

-   Set up security for the group "Basic Accounts" that filters the Accounts table on `Plan = "Basic"`.
-   Another setup for the group "Converted Accounts" that filters the Accounts table on `Trial Converted = true`.

If you put Vincent Accountman in both groups, he'll have conflicting permissions for the Accounts table, and get an error message whenever he tries to use Accounts in Metabase.

To resolve row and column security permissions conflicts:

-   Remove the person from all but one of the groups.
-   Set the all but one of the group's [View data](./data#view-data-permissions) access to the datatabase to "Blocked".

### You cannot secure the rows or columns of SQL results

Row and column security permissions don't apply to the results of SQL questions. That is, SQL questions will always display results from the original table rather than the secured table.

Say that you've set up column security on the Accounts table to hide the Email column. If someone creates a SQL question that includes the Email column, **anyone with collection permissions to view that SQL question** will be able to:

-   See the Email column in the SQL question results.
-   Use the SQL question to start a new question that includes the Email column (if they have query permissions).

To prevent the Email column from being exposed via a SQL question:

-   Put any SQL questions that include the Email column in a separate collection.
-   Set the [collection permissions](../permissions/collections) to **No access** for groups with row and column security set up to hide the Email column.

[Collection permissions](../permissions/collections) must be used to prevent secured groups from viewing SQL questions that reference secured tables.

### Public sharing

Row and column security permissions don't apply to public questions or public dashboards. If someone in an unsecured group creates a public link using an original table, the original table will be displayed to anyone who has the public link URL.

To prevent this from happening, you'll have to [disable public sharing](../embedding/public-links) for your Metabase.

Metabase can only create row and column security using the group membership or user attributes of people who are logged in. Since public links don't require logins, Metabase won't have enough info to apply permissions.

## Limitations of row and column security

Some things to keep in mind when using row and column security.

### Groups with native query permissions (access to the SQL editor) can bypass row and column security

Row and column security is limited to the [query builder](../questions/query-builder/editor). You can't set up [native query persmissons](./data#create-queries-permissions) for groups with row and column security.

To enforce row-level permissions with the native query editor, check out [impersonation](./impersonation).

### You can't apply row and column security to SQL questions

Since Metabase can't parse SQL queries, the results of SQL questions will always use original tables.

[Use collection permissions](#you-cannot-secure-the-rows-or-columns-of-sql-results) to prevent groups from viewing saved SQL questions with restricted data.

### Non-SQL databases have limited row and column security

MongoDB only supports [row-level security](#row-level-security-filter-by-a-column-in-the-table). Row and column security permissions are unavailable for Apache Druid.

### Advanced data types require a workaround

If you're trying to set up row security on a column with an advanced data type (like enums or arrays), you'll need to convert that data to a basic type first. Options include:

#### Option 1: Use SQL to cast the advanced data type to a basic SQL type

Create a SQL question that casts the advanced data type column to a basic data type, then use that question for your row and column security setup.

#### Option 2: Create a database view

If you can't use SQL casting in Metabase, create a view in your database that converts the advanced data type to a basic type, then set up row and column security on that view instead of the original table. You'll also need to block the original table.

## Further reading

-   [Row and column security examples](./row-and-column-security-examples)
-   [Permissions strategies](/learn/metabase-basics/administration/permissions/strategy)
-   [Configuring permissions for embedding](../permissions/embedding)
-   [Securing embedded Metabase](../embedding/securing-embeds)

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/permissions/row-and-column-security.md) ]
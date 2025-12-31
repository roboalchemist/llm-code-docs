# Source: https://fly.io/docs/mpg/configuration/

\*)\]:mx-auto \[body\_:where(&\>\*)\]:max-w-2xl \[body:not(.toc)\_:where(&\>\*)\]:lg:mx-\[calc(50%-min(50%,35rem))\] \[body\_:where(&\>\*)\]:lg:max-w-3xl min-w-0 relative\"\>

# Cluster configuration options 

<figure class="flex justify-center">
<img src="/static/images/Managed_Postgres.png" class="w-full max-w-lg mx-auto" alt="Illustration by Annie Ruygt of a balloon doing a lot of tasks" />
</figure>

## [](#connection-pooling)[Connection Pooling] 

All Managed Postgres clusters come with PGBouncer for connection pooling, which helps manage database connections efficiently. You can configure how PGBouncer assigns connections to clients by changing the pool mode.

### [](#pool-mode-options)[Pool Mode Options] 

There are two pool modes available:

-   **Session**: Connections are assigned to clients for the entire session. This is the default mode and provides the most compatibility with PostgreSQL features, including transactions, prepared statements, and advisory locks.
-   **Transaction**: Connections are assigned per transaction. This mode allows for higher connection reuse and better performance under high load, but has some limitations with certain PostgreSQL features.

### [](#when-to-use-each-mode)[When to Use Each Mode] 

**Use Session mode when**:

-   Your application uses prepared statements
-   You need advisory locks or other session-specific features
-   You're unsure which mode to choose (Session is the safer default)
-   Your application has long-running transactions

**Use Transaction mode when**:

-   You have a high-throughput application with many short transactions
-   You want to maximize connection reuse
-   Your application primarily uses simple queries without prepared statements
-   You need to support more concurrent connections with the same hardware
-   If you're using Elixir's Ecto library, you must use Transaction pool mode when connecting through the pooler, as Ecto's connection pooling behavior is incompatible with PGBouncer's Session mode.

### [](#changing-pool-mode-from-the-dashboard)[Changing Pool Mode from the Dashboard] 

To change the pool mode for your cluster:

1.  Navigate to your MPG cluster's "Connect" tab in the dashboard
2.  Click "View Pooler Settings" to expand the configuration options
3.  Select your desired pool mode.
4.  Click "Update Pool Mode"
5.  Confirm the change in the modal dialog

**Note**: Changing the pool mode will restart the connection pooler nodes, which may cause brief connection interruptions. Your database itself will remain running.

## [](#changing-your-mpg-plan)[Changing your MPG Plan] 

Your Managed Postgres Plan determines the amount of resources your cluster has. All plans include a primary and replica, pg bouncers, and backups. You can change your cluster's plan at any time and the machines in the cluster will be updated to their new resources.

In order to change your plan:

1.  Navigate to your MPG cluster's "Settings" tab in the dashboard
2.  Select your desired plan from the list
3.  Click the "Update Configuration" button
4.  Your plan will be updated and all configuration changes will be applied to your database nodes.

During the configuration update, your database nodes will restart. You may see a brief period of downtime during the upgrade and switchover. Please make sure to plan accordingly.

## [](#users-and-roles)[Users and Roles] 

Your Managed Postgres Cluster is created with one admin user named `fly-user`. You can create additional database users and set their roles from your dashboard or through `flyctl`.

Currently MPG supports the following roles for users:

### [](#schema-admin)[Schema Admin] 

The Schema Admin role is the closest to a Superuser role. It provides full read & write access to your cluster, as well as the ability to modify the structure of your database.

This is the default role granted to the `fly-user` user when your cluster is created.

**What Schema Admin users can do:**

-   Read and write to all databases, tables, and schemas
-   Create, alter, and drop tables, views, functions, and other database objects
-   Create new schemas and manage database structure
-   Connect to any database in the cluster
-   Create temporary tables for session-specific operations

**What Schema Admin users cannot do:**

-   Create new databases. This can be done from your Dashboard
-   Other actions requiring superuser permissions, other than those named above.

### [](#writer)[Writer] 

The Writer role provides full read and write access to data while restricting the ability to modify the database structure.

**What Writer users can do:**

-   Read from and write to all existing tables and schemas
-   Insert, update, and delete records across all databases
-   Connect to any database in the cluster

**What Writer users cannot do:**

-   Create or modify table structures
-   Create new schemas or databases
-   Create functions, procedures, or other schema objects
-   Create temporary tables
-   Alter database permissions or roles

### [](#reader)[Reader] 

The Reader role provides read-only access to all data in the cluster. This role works well for connecting to reporting or analytics.

**What Reader users can do:**

-   View all data across databases, tables, and schemas
-   Connect to any database in the cluster
-   Run SELECT queries

**What Reader users cannot do:**

-   Insert, update, or delete any data
-   Create any database objects or modify schemas
-   Create temporary tables
-   Modify database structure or permissions

### [](#creating-additional-users)[Creating additional users] 

To create additional users via the dashboard:

1.  Navigate to your MPG cluster's "Users" tab in the dashboard
2.  Enter a name for your new user
3.  Click "Create User" and wait for the user to be created.

To create additional users via `flyctl`:

1.  Run `fly mpg users create` to create a new user for your MPG cluster

Note: If your cluster was created before July 2025, you'll need to opt in to the new Role system before you can add new users. This can be done on the Users tab of your dashboard.

### [](#authenticating-with-a-custom-user)[Authenticating with a custom user] 

Once the user has been created, you can generate a connection string for them from the "Connect" tab of your dashboard. Select the user you'd like to authenticate as, and the connection string will be updated with their details.

## [](#databases)[Databases] 

Your Managed Postgres cluster is created with the default `fly-db` database. You can create additional databases from the dashboard or through `flyctl`.

These databases can be accessed by existing users in your cluster, based on their role.

### [](#creating-additional-databases)[Creating additional Databases] 

To create additional databases via the dashboard:

1.  Navigate to your MPG cluster's "Databases" tab in the dashboard
2.  Enter a name for your new database in the input field under the "Databases" section.
3.  Click "Create database" and wait for the database to be created.

To create additional database via `flyctl`:

1.  Run `fly mpg databases create` to create a new database for your MPG cluster.

![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSIgc3R5bGU9IndpZHRoOiAxNnB4OyBoZWlnaHQ6IDE2cHg7IHBvaW50ZXItZXZlbnRzOiBub25lOyIgdmlld2JveD0iMCAwIDIwOCAxMjgiIGZpbGw9ImN1cnJlbnRDb2xvciI+CiAgPHJlY3Qgd2lkdGg9IjE5OCIgaGVpZ2h0PSIxMTgiIHg9IjUiIHk9IjUiIHJ5PSIxMCIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMTAiIGZpbGw9Im5vbmUiPjwvcmVjdD4KICA8cGF0aCBkPSJNMzAgOThWMzBoMjBsMjAgMjUgMjAtMjVoMjB2NjhIOTBWNTlMNzAgODQgNTAgNTl2Mzl6bTEyNSAwbC0zMC0zM2gyMFYzMGgyMHYzNWgyMHoiPjwvcGF0aD4KPC9zdmc+) [Copy page as markdown]

[or] [![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE2cHg7IGhlaWdodDogMTZweDsiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8cGF0aCBkPSJNMjIuMjgyIDkuODIxYTUuOTg1IDUuOTg1IDAgMCAwLS41MTYtNC45MSA2LjA0NiA2LjA0NiAwIDAgMC02LjUxLTIuOUE2LjA2NSA2LjA2NSAwIDAgMCA0Ljk4MSA0LjE4YTUuOTg1IDUuOTg1IDAgMCAwLTMuOTk4IDIuOSA2LjA0NiA2LjA0NiAwIDAgMCAuNzQzIDcuMDk3IDUuOTggNS45OCAwIDAgMCAuNTEgNC45MTEgNi4wNTEgNi4wNTEgMCAwIDAgNi41MTUgMi45QTUuOTg1IDUuOTg1IDAgMCAwIDEzLjI2IDI0YTYuMDU2IDYuMDU2IDAgMCAwIDUuNzcyLTQuMjA2IDUuOTkgNS45OSAwIDAgMCAzLjk5Ny0yLjkgNi4wNTYgNi4wNTYgMCAwIDAtLjc0Ny03LjA3M3pNMTMuMjYgMjIuNDNhNC40NzYgNC40NzYgMCAwIDEtMi44NzYtMS4wNGwuMTQxLS4wODEgNC43NzktMi43NThhLjc5NS43OTUgMCAwIDAgLjM5Mi0uNjgxdi02LjczN2wyLjAyIDEuMTY4YS4wNzEuMDcxIDAgMCAxIC4wMzguMDUydjUuNTgzYTQuNTA0IDQuNTA0IDAgMCAxLTQuNDk0IDQuNDk0ek0zLjYgMTguMzA0YTQuNDcgNC40NyAwIDAgMS0uNTM1LTMuMDE0bC4xNDIuMDg1IDQuNzgzIDIuNzU5YS43NzEuNzcxIDAgMCAwIC43OCAwbDUuODQzLTMuMzY5djIuMzMyYS4wOC4wOCAwIDAgMS0uMDMzLjA2Mkw5Ljc0IDE5Ljk1YTQuNSA0LjUgMCAwIDEtNi4xNC0xLjY0NnpNMi4zNCA3Ljg5NmE0LjQ4NSA0LjQ4NSAwIDAgMSAyLjM2Ni0xLjk3M1YxMS42YS43NjYuNzY2IDAgMCAwIC4zODguNjc2bDUuODE1IDMuMzU1LTIuMDIgMS4xNjhhLjA3Ni4wNzYgMCAwIDEtLjA3MSAwbC00LjgzLTIuNzg2QTQuNTA0IDQuNTA0IDAgMCAxIDIuMzQgNy44NzJ6bTE2LjU5NyAzLjg1NWwtNS44MzMtMy4zODdMMTUuMTE5IDcuMmEuMDc2LjA3NiAwIDAgMSAuMDcxIDBsNC44MyAyLjc5MWE0LjQ5NCA0LjQ5NCAwIDAgMS0uNjc2IDguMTA1di01LjY3OGEuNzkuNzkgMCAwIDAtLjQwNy0uNjY3em0yLjAxLTMuMDIzbC0uMTQxLS4wODUtNC43NzQtMi43ODJhLjc3Ni43NzYgMCAwIDAtLjc4NSAwTDkuNDA5IDkuMjNWNi44OTdhLjA2Ni4wNjYgMCAwIDEgLjAyOC0uMDYxbDQuODMtMi43ODdhNC41IDQuNSAwIDAgMSA2LjY4IDQuNjZ6bS0xMi42NCA0LjEzNWwtMi4wMi0xLjE2NGEuMDguMDggMCAwIDEtLjAzOC0uMDU3VjYuMDc1YTQuNSA0LjUgMCAwIDEgNy4zNzUtMy40NTNsLS4xNDIuMDhMOC43MDQgNS40NmEuNzk1Ljc5NSAwIDAgMC0uMzkzLjY4MXptMS4wOTctMi4zNjVsMi42MDItMS41IDIuNjA3IDEuNXYyLjk5OWwtMi41OTcgMS41LTIuNjA3LTEuNXoiPjwvcGF0aD4KPC9zdmc+) Open in ChatGPT ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1sLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE0cHg7IGhlaWdodDogMTRweDsiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSI+CiAgPHJlY3Qgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiByeD0iMyIgZmlsbD0iY3VycmVudENvbG9yIiBvcGFjaXR5PSIwLjEiPjwvcmVjdD4KICA8cGF0aCBkPSJNNiA1aDV2NU0xMSA1bC01IDUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48L3BhdGg+Cjwvc3ZnPg==)](https://chatgpt.com/?hints=search&q=Read+https%3A%2F%2Fraw.githubusercontent.com%2Fsuperfly%2Fdocs%2Fmain%2Fmpg%2Fconfiguration.html.md)

[![](data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIGNsYXNzPSJtci0xLjUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3R5bGU9InBvaW50ZXItZXZlbnRzOiBub25lOyB3aWR0aDogMjBweDsgaGVpZ2h0OiAyMHB4OyIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8ZyBidWZmZXJlZC1yZW5kZXJpbmc9InN0YXRpYyI+CiAgICA8cGF0aCBkPSJNMTEuOTk5IDEuMjcxQzUuOTI1IDEuMjcxIDEgNi4xOTYgMSAxMi4yNzNjMCA0Ljg1OSAzLjE1MiA4Ljk4MiA3LjUyMyAxMC40MzcuNTUuMS43NTEtLjIzOS43NTEtLjUzbC0uMDE1LTEuODcyYy0zLjA2LjY2Ni0zLjcwNi0xLjQ3NC0zLjcwNi0xLjQ3NC0uNS0xLjI3MS0xLjIyMS0xLjYwOS0xLjIyMS0xLjYwOS0uOTk5LS42ODMuMDc1LS42NjguMDc1LS42NjggMS4xMDUuMDc3IDEuNjg1IDEuMTMzIDEuNjg1IDEuMTMzLjk4MSAxLjY4MSAyLjU3NSAxLjE5NiAzLjIwMi45MTQuMS0uNzExLjM4NC0xLjE5Ni42OTgtMS40NzEtMi40NDItLjI3Ny01LjAxMS0xLjIyMS01LjAxMS01LjQzNiAwLTEuMjAxLjQyOS0yLjE4MyAxLjEzMy0yLjk1Mi0uMTE0LS4yNzgtLjQ5MS0xLjM5Ny4xMDgtMi45MTEgMCAwIC45MjMtLjI5NiAzLjAyNSAxLjEyN0ExMC41NiAxMC41NiAwIDAgMSAxMiA2LjU5MWMuOTM1LjAwNCAxLjg3Ni4xMjcgMi43NTQuMzcgMi4xLTEuNDIzIDMuMDIyLTEuMTI3IDMuMDIyLTEuMTI3LjYgMS41MTQuMjIzIDIuNjMzLjExIDIuOTExLjcwNS43NjkgMS4xMzEgMS43NTEgMS4xMzEgMi45NTIgMCA0LjIyNS0yLjU3MyA1LjE1NS01LjAyMyA1LjQyNy4zOTUuMzQuNzQ3IDEuMDExLjc0NyAyLjAzOCAwIDEuNDcxLS4wMTQgMi42NTctLjAxNCAzLjAxOCAwIC4yOTMuMTk5LjYzNi43NTYuNTI4QzE5Ljg1MSAyMS4yNTEgMjMgMTcuMTMgMjMgMTIuMjczYzAtNi4wNzctNC45MjYtMTEuMDAyLTExLjAwMS0xMS4wMDJ6Ij48L3BhdGg+CiAgPC9nPgo8L3N2Zz4=) Report an issue](https://github.com/superfly/docs/issues/new?body=I+found+an+issue+with+this+document.%0A%0ATitle%3A+Cluster+configuration+options%0ALocation%3A+https%3A%2F%2Ffly.io%2Fdocs%2Fmpg%2Fconfiguration%2F%0ASource%3A+https%3A%2F%2Fgithub.com%2Fsuperfly%2Fdocs%2Fblob%2Fmain%2Fmpg%2Fconfiguration.html.md%0A%0A%23%23%23+Describe+the+issue%0A%0A%3C%21--+Describe+the+issue+and+include+the+section+you%27re+referring+to%2C+if+applicable.+Provide+lots+of+detail+about+the+issue+that+you+found.++--%3E%0A%0A%23%23%23+Additional+info%0A%0A%3C%21--+Add+any+other+context+about+the+issue+here.+If+applicable%2C+add+screenshots+to+help+explain+the+issue.+--%3E%0A&title=Issue+with+the+%22Cluster+configuration+options%22+doc) or [edit this page on GitHub](https://github.com/superfly/docs/edit/main/mpg/configuration.html.md)
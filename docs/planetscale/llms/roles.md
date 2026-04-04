# Source: https://planetscale.com/docs/postgres/connecting/roles.md

# Managing Roles for your Postgres database

> When you connect to your database, you have the option to connect with the default role or a user-generated role. This document covers the differences between each option and how to create new roles.

You should not connect to the database from your application servers using the default role. If you ever need to rotate your default role credentials and you use the default role to connect to your application, you will have to take some downtime while rotating the credentials.

Instead, we recommend creating [user-defined roles](#user-defined-roles) for this purpose. We'll first cover the default role below, and then explain how to generate user-defined roles.

## Default role

The default `postgres` role is similar to the Postgres `superuser`, but with fewer permissions. It is defined by the following statement:

```sql  theme={null}
CREATE ROLE $POSTGRES_USERNAME
  NOSUPERUSER CREATEDB CREATEROLE INHERIT LOGIN REPLICATION BYPASSRLS PASSWORD '$PASSWORD';
```

It also inherits the following permissions:

```sql  theme={null}
GRANT pg_read_all_data,
  pg_write_all_data,
  pg_read_all_settings,
  pg_read_all_stats,
  pg_stat_scan_tables,
  pg_monitor,
  pg_signal_backend,
  pg_checkpoint,
  pg_maintain,
  pg_use_reserved_connections,
  pg_create_subscription
TO $ALMOST_SUPERUSER_ROLENAME WITH ADMIN OPTION;
```

## User-defined roles

When creating custom roles for your application, you can select from a variety of permissions to grant specific capabilities. User-defined roles allow you to implement the principle of least privilege by granting only the permissions necessary for each use case.

For examples of common user-defined roles, see [User-defined role examples and use cases](#user-defined-role-examples-and-use-cases).

### Available permissions

Below is a list of available permissions you can set on user-defined roles.

**Data access permissions**

* **pg\_read\_all\_data** — Read data from all tables, views, and sequences. This permission allows `SELECT` queries across all database objects.

* **pg\_write\_all\_data** — Write data to all tables, views, and sequences. This permission allows `INSERT`, `UPDATE`, `DELETE`, and `TRUNCATE` operations. Note that write operations typically require `pg_read_all_data` as well to read the data being modified.

**Configuration and monitoring permissions**

* **pg\_read\_all\_settings** — Read all configuration variables. This allows viewing database configuration parameters.

* **pg\_read\_all\_stats** — Read all `pg_stat_*` views. This provides access to database statistics and performance metrics.

* **pg\_stat\_scan\_tables** — Execute monitoring functions that may take `ACCESS SHARE` locks on tables. This is useful for running database monitoring and analysis operations.

* **pg\_monitor** — Read and execute monitoring views and functions. This is a convenience role that combines several monitoring-related permissions.

**Administrative permissions**

* **pg\_signal\_backend** — Signal another backend to cancel a query or terminate its session. This is useful for managing long-running queries and terminating problematic connections.

* **pg\_checkpoint** — Execute the `CHECKPOINT` command. Checkpoints ensure that all data is written to disk and are important for database recovery.

* **pg\_maintain** — Execute maintenance operations including `VACUUM`, `ANALYZE`, `CLUSTER`, `REFRESH MATERIALIZED VIEW`, `REINDEX`, and `LOCK TABLE`. These operations are essential for database performance and maintenance.

* **pg\_use\_reserved\_connections** — Use connection slots reserved via `reserved_connections`. This allows connecting to the database even when all regular connection slots are in use.

* **pg\_create\_subscription** — Allow users with `CREATE` permission on the database to issue `CREATE SUBSCRIPTION`. This is used for logical replication scenarios.

**Superuser-equivalent permission**

* **postgres** — The default near-superuser role with extensive permissions. This role can create, modify, and drop databases, users, roles, tables, schemas, and all other objects. Use this permission carefully, as it grants broad administrative capabilities.

## Creating new user-defined roles

There are several ways to create a new role:

* Using the "Connect" button in your dashboard
* Using "Roles" section in your database settings
* Using the [`CREATE ROLE`](https://www.postgresql.org/docs/current/sql-createrole.html) command as the default role (which has elevated privileges).
* Using the Postgres [Roles API](/docs/api/reference/list_roles)
* Using the PlanetScale CLI [pscale role commands](/docs/cli/role)

### Creating roles in the dashboard

To create a new role in the dashboard, you can either click the "Connect" button on the database overview page, or navigate to "Settings" > "Roles" and click "New role".

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/roles/image3.png?fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=b3432ca882cfad33aae8c66151915aef" alt="Configure the new role" data-og-width="1980" width="1980" data-og-height="2356" height="2356" data-path="docs/images/assets/docs/postgres/roles/image3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/roles/image3.png?w=280&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=2b66a320d0fefa7ba182f112e84375b6 280w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/roles/image3.png?w=560&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=2c088beb0e7fbe62b008568c13696b0a 560w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/roles/image3.png?w=840&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=1edb57cf63f9fbb99f3b7817b416d9c7 840w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/roles/image3.png?w=1100&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=13b06d2207b178c41cda07019ee9f836 1100w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/roles/image3.png?w=1650&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=299d2c7509f89dee878fc38315dc0931 1650w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/roles/image3.png?w=2500&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=55f5c6e273f65b87aab34f9e5003cd39 2500w" />
</Frame>

### Creating roles via the CLI

You can also manage roles directly from the command line using the PlanetScale `pscale role` CLI. This provides a convenient way to create, list, and manage roles as part of your development workflow or automation scripts.

Make sure you have the [PlanetScale CLI](/docs/cli) installed

#### Available commands

**Create a new role:**

```
pscale role create <database> <branch> <name> [flags]
```

Example:

```
pscale role create my-database main api-user --inherited-roles pg_read_all_data --ttl 24h
```

**List all roles for a branch:**

```
pscale role list <database> <branch>
```

**Get details for a specific role:**

```
pscale role get <database> <branch> <role-id>
```

**Delete a role:**

```
pscale role delete <database> <branch> <role-id> [--successor <other-role>]
```

**Update a role's name:**

```
pscale role update <database> <branch> <role-id> --name <new-name>
```

**Renew a role's expiration:**

```
pscale role renew <database> <branch> <role-id>
```

**Reset the default postgres role credentials:**

```
pscale role reset-default <database> <branch>
```

**Reset a role's password:**

```
pscale role reset --org <org> <database> <branch> <role-id>
```

This command resets the password for a role after prompting for confirmation. It returns the role object with the new password.

**Reassign objects owned by a role:**

```
pscale role reassign --org <org> <database> <branch> <donor> --successor <recipient>
```

This command assigns all objects owned by the donor role to the recipient role.

Roles created via the CLI will appear in your database settings and can be managed through the dashboard as well.

### Creating roles via `CREATE ROLE`

When you create a role via the Postgres [`CREATE ROLE`](https://www.postgresql.org/docs/current/sql-createrole.html) command, these will not display on your database settings. It is up to you to manage these via the `psql` CLI.

PlanetScale's routing layer uses the `user` to identify which database or branch we are sending queries to. For example, the user `matt.nk35mx55qq` routes to the PlanetScale database with branch id `nk35mx55qq`. When you create a new role, you do not need to specify the branch id on the user. You can simply set the user to `matt`.

However, when you connect, you must append the branch id to the user so we know which branch to route to.

<Steps>
  <Step>
    From the PlanetScale organization dashboard, select the desired database
  </Step>

  <Step>
    Select the desired branch from the dropdown
  </Step>

  <Step>
    Click "**Connect**"
  </Step>

  <Step>
    Copy the branch id
  </Step>

  <Step>
    Append it to your user with `.branch_id`
  </Step>
</Steps>

## Viewing, deleting, and renaming roles

On the roles page, you will see all roles created via the dashboard, API, and the `pscale role` CLI. However, we will not display roles created manually via `CREATE ROLE` commands.

You can rename a role by clicking the "..." button for the role on the Roles page at "Settings" > "Roles".

### Deleting a role

To delete a role, click the "..." for the role on the database Roles page at "Settings" > "Roles".

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/roles/image5.png?fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=cea125353fc5aad2e54f0976c89a7950" alt="Rename or delete a role" data-og-width="3128" width="3128" data-og-height="1470" height="1470" data-path="docs/images/assets/docs/postgres/roles/image5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/roles/image5.png?w=280&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=fe2967a92dd2563429ec5ad5a93d8027 280w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/roles/image5.png?w=560&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=1d4d1e7184db2798c0463e8814aa565e 560w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/roles/image5.png?w=840&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=4aa1f9c79c4fa6fe6c90a829a52e3908 840w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/roles/image5.png?w=1100&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=522386ad984a974e88adfe1f8c5ab9d1 1100w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/roles/image5.png?w=1650&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=9b9c1b030ce50453a280cfa45d62f501 1650w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/roles/image5.png?w=2500&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=fa0b64810f8503196426b3d098f764fb 2500w" />
</Frame>

Deleting a role requires an extra step if the role has created any objects like tables or schemas, if the role has been granted any additional permissions, or if the role has created any other roles. If you try to delete a role that is still referenced, you may see this error: `Role is still referenced and cannot be dropped.`.

Such roles must designate a successor role, to which allowed objects are reassigned. Additional granted permissions are dropped as part of the transfer process. The usual successor role is `postgres`, which you can indicate in the "Delete role" modal.

You can reassign owned objects when deleting a role directly in the dashboard. When you click "Delete role", check the "**Reassign owned objects**" box on the modal.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/qADAk5S-E3Yha3-1/docs/images/assets/docs/postgres/roles/image6.png?fit=max&auto=format&n=qADAk5S-E3Yha3-1&q=85&s=984a78f6a81984aafeffd4b7dc842e88" alt="Specify a successor for a role" data-og-width="1980" width="1980" data-og-height="1620" height="1620" data-path="docs/images/assets/docs/postgres/roles/image6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/qADAk5S-E3Yha3-1/docs/images/assets/docs/postgres/roles/image6.png?w=280&fit=max&auto=format&n=qADAk5S-E3Yha3-1&q=85&s=ee31179a7639c2692da071e9339cb3c5 280w, https://mintcdn.com/planetscale-cad1a68a/qADAk5S-E3Yha3-1/docs/images/assets/docs/postgres/roles/image6.png?w=560&fit=max&auto=format&n=qADAk5S-E3Yha3-1&q=85&s=85afb016a063fb7181eae42c3a77a8c9 560w, https://mintcdn.com/planetscale-cad1a68a/qADAk5S-E3Yha3-1/docs/images/assets/docs/postgres/roles/image6.png?w=840&fit=max&auto=format&n=qADAk5S-E3Yha3-1&q=85&s=54accbd0d5109c9c340ed04a4f32004a 840w, https://mintcdn.com/planetscale-cad1a68a/qADAk5S-E3Yha3-1/docs/images/assets/docs/postgres/roles/image6.png?w=1100&fit=max&auto=format&n=qADAk5S-E3Yha3-1&q=85&s=1abc5431b57affad58994e98fd66791a 1100w, https://mintcdn.com/planetscale-cad1a68a/qADAk5S-E3Yha3-1/docs/images/assets/docs/postgres/roles/image6.png?w=1650&fit=max&auto=format&n=qADAk5S-E3Yha3-1&q=85&s=c2a3690a5ad22b2e239febe3a9941ee1 1650w, https://mintcdn.com/planetscale-cad1a68a/qADAk5S-E3Yha3-1/docs/images/assets/docs/postgres/roles/image6.png?w=2500&fit=max&auto=format&n=qADAk5S-E3Yha3-1&q=85&s=f9c21a7dee6acbb3680800261a2ac609 2500w" />
</Frame>

You can choose successors other than `postgres`, but only by using the API or the `pscale role` CLI.  Deleting a role that owns objects, has additional permissions, or has created other roles will fail if no successor is specified.

You can [delete a role using the `pscale role` CLI](/docs/cli/role#the-delete-sub-command) with:

```bash  theme={null}
pscale role delete --org <org> <database> main <role-id> --successor postgres
```

### Reassigning objects owned by a role

If you need to transfer ownership of database objects from one role to another without deleting the role, you can reassign the objects from the dashboard or the CLI.

**In the dashboard**, click the "..." button for the role on the Roles page at "Settings" > "Roles", then select "**Reassign objects**". This will transfer all objects owned by the role to the `postgres` role. Reassigning objects to a recipient other than `postgres` is only possible through the API and the CLI.

**Using the CLI**, you can reassign objects with:

```bash  theme={null}
pscale role reassign --org <org> <database> <branch> <donor> --successor <recipient>
```

This command will prompt for confirmation before transferring ownership of all objects from the donor role to the recipient role.

### Resetting role credentials

If you need to reset a role's password, you can do so from the dashboard or the CLI.

**In the dashboard**, click the "..." button for the role on the Roles page at "Settings" > "Roles", then select "**Reset credentials**". This will generate a new password for the role.

**Using the CLI**, you can reset a role's password with:

```bash  theme={null}
pscale role reset --org <org> <database> <branch> <role-id>
```

This command will prompt for confirmation before resetting the password and return the role object with the new password.

## User-defined role examples and use cases

Understanding when to use user-defined roles versus the default role is essential for maintaining secure and maintainable database access patterns. This section provides practical examples of role configurations for common scenarios.

### When to use user-defined roles vs. the default role

**Use user-defined roles when:**

* **Connecting from application servers**: Application connections should never use the default role. This allows you to rotate the default role credentials without application downtime.
* **Principle of least privilege**: Different parts of your application or different services may need different levels of access. Create specific roles for each use case.
* **Managing team access**: Different team members may need different permissions (e.g., developers vs. data analysts vs. DBAs).
* **Integrating third-party tools**: External tools and services should have their own roles with limited permissions appropriate to their function.

**Use the default role when:**

* **Performing administrative tasks**: Creating schemas, managing database structure, or performing major database migrations.
* **Initial database setup**: Setting up the initial database structure and creating the first set of user-defined roles.

### Example role configurations

The following are some example permission configurations that you may use for user-defined roles. Your use cases may vary, but these are generic examples.

**Application read-write role**

For a typical web application that needs to read and write data, you may consider these permissions:

* `pg_read_all_data`
* `pg_write_all_data`

**Read-only analytics role**

For analytics tools or reporting dashboards that only need to query data:

* `pg_read_all_data`
* `pg_read_all_settings`
* `pg_read_all_stats`

**Monitoring and observability role**

For monitoring tools like Datadog, New Relic, or custom monitoring solutions:

* `pg_monitor`
* `pg_read_all_stats`
* `pg_read_all_settings`
* `pg_stat_scan_tables`

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt
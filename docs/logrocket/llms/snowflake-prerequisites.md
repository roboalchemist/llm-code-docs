# Source: https://docs.logrocket.com/docs/snowflake-prerequisites.md

# Snowflake Prerequisites

Configuring your Snowflake destination.

## Prerequisites

* [ ] In order to complete the following setup steps, you or a Snowflake admin on your team must have the `securityadmin` and `sysadmin` roles. (To check your account for these roles, run `SHOW GRANTS TO USER <your_username>;` and review the `role` column.)

## Step 1: Create role, user, warehouse, and database in the data warehouse

1. Review and make any changes to the following setup script.

```sql
begin;

   -- create variables for user / password / role / warehouse / database
   set role_name = 'TRANSFER_ROLE'; -- all letters must be uppercase
   set user_name = 'TRANSFER_USER'; -- all letters must be uppercase
   set user_password = 'some_password'; -- alphanumeric only, special characters are not allowed
   set warehouse_name = 'TRANSFER_WAREHOUSE'; -- all letters must be uppercase
   set database_name = 'TRANSFER_DATABASE'; -- all letters must be uppercase

   -- change role to securityadmin for user / role steps
   use role securityadmin;

   -- create role for data transfer service
   create role if not exists identifier($role_name);
   grant role identifier($role_name) to role SYSADMIN; -- establish SYSADMIN as the parent of the new role. Note: this does not grant the access privileges of SYSADMIN to the new role.

   -- create a user for data transfer service
   create user if not exists identifier($user_name)
   password = $user_password;

   -- set default role and warehouse to new user
   alter user identifier($user_name) SET default_role = $role_name;
   alter user identifier($user_name) SET default_warehouse = $warehouse_name;

   grant role identifier($role_name) to user identifier($user_name);

   -- change role to sysadmin for warehouse / database steps
   use role sysadmin;

   -- create a warehouse for data transfer service
   create warehouse if not exists identifier($warehouse_name)
   warehouse_size = xsmall
   warehouse_type = standard
   auto_suspend = 60
   auto_resume = true
   initially_suspended = true;

   -- create database for data transfer service
   create database if not exists identifier($database_name);

   -- grant service role access to warehouse
   grant USAGE
   on warehouse identifier($warehouse_name)
   to role identifier($role_name);

   -- grant service access to database
   grant CREATE SCHEMA, MONITOR, USAGE
   on database identifier($database_name)
   to role identifier($role_name);

 commit;
```

> 📘 Alternative authentication method: key-pair auth
>
> By default, this script creates a new user with a basic password. If you'd prefer to use key-based authentication, instead of:
>
> ```sql SQL
>  create user if not exists identifier($user_name)
>  password = $user_password;
> ```
>
> Use the following block. Note that your public key can be found in the Streaming Data Export onboarding UI, so you will have to run this command after initiating the setup.
>
> ```sql sql
> create user if not exists identifier($user_name)
> RSA_PUBLIC_KEY='<PUBLIC_KEY>'; -- your public key can be found from in the Streaming Data Export onboarding UI
> ```

> 📘 Using an existing `schema`
>
> By default, a new schema (with a name you provide) will be created in the target Snowflake database upon the initial connection. If instead you create the `schema` ahead of time, you may remove the `CREATE SCHEMA` permission, and instead  `grant ALL PRIVILEGES` on the target `schema` for the designated `role`.
>
> The script below can be used to complete this step:
>
> ```sql
> set role_name = 'TRANSFER_ROLE';
> set database_name = 'TRANSFER_DATABASE';
> set schema_name = 'PRECREATED_SCHEMA';
>
> use database identifier($database_name);
> grant ALL PRIVILEGES on schema identifier($schema_name) to role identifier($role_name);
> ```

> 📘 Using an existing `warehouse` or `database`
>
> By default, this script creates a new warehouse and a new database. If you'd prefer to use an existing warehouse/database, change the `warehouse_name` variable from `TRANSFER_WAREHOUSE` to the name of the warehouse to be shared/`database_name` variable from `TRANSFER_DATABASE` to the name of the database to be shared.

2. In the Snowflake interface, select the dropdown next to the "Run" button, and click **Run All**. This will run every query in the script at once. If successful, you will see `Statement executed successfully` in the query results.

## Step 2: Configure the Snowflake access policy

If your Snowflake data warehouse is using Snowflake Access Policies, a new policy must be added to allow the transfer service static IP to write to the warehouse.

1. Review current network policies to check for existing IP safelists.

```sql
SHOW NETWORK POLICIES;
```

2. If there is no existing Snowflake Network Policies (the `SHOW` query returns no results), you can skip to Step 3.
3. If there is an existing Snowflake Network Policy, you must alter the existing policy or create a new one to safelist the data transfer service static IP address. Use the `CREATE NETWORK POLICY` command to specify the IP addresses that can access your Snowflake warehouse.

```sql
CREATE NETWORK POLICY <transfer_service_policy_name> ALLOWED_IP_LIST = ('34.171.168.215/32');
```

> **Creating your first network policy**
>
> If you have no existing network policies and you create your first as part of this step, all other IPs outside of the `ALLOWED_IP_LIST` will be blocked. Snowflake does not allow setting a network policy that blocks your current IP address. (An error message results while trying to create a network policy that blocks the current IP address.) But be careful when setting your first network policy.

## Step 3: Add your destination

For the data export setup, you will need

* your **host name**, **database name**,
* your chosen **schema name**,
* your **username**
* your **password**, if you've chosen username and password authentication
* your **public key**, if you've chosen key-based auth. This can be found in the Streaming Data Export onboarding UI.

Visit the [LogRocket Streaming Data Export settings page](https://app.logrocket.com/r/settings/streaming-data-export) to complete the setup.
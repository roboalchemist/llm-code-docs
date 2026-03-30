# Source: https://developers.webflow.com/browser/data-exports/destinations/snowflake.mdx

***

title: Snowflake
slug: data-exports/destinations/snowflake
description: Configure Snowflake as a destination for Data Exports
------------------------------------------------------------------

This guide walks you through configuring Snowflake as a destination for your Webflow Analyze and Optimize data export.

## Prerequisites

* Locate your Public Key generated on your behalf. The Public Key will be a long string of text, loosely resembling the format: `'MIIBI...<SHORTENED>...Xrw2nwIDAQAB'`
* In order to complete the following setup steps, you or a Snowflake admin on your team must have the securityadmin and sysadmin roles. (To check your account for these roles, run `SHOW GRANTS TO USER <your_username>;` and review the `role` column.)
* If your Snowflake data warehouse is using Snowflake Access Policies, use the Webflow static IP: `34.69.83.207/32` to complete Step 2.

<Note>
  **Recommendation: Key-pair authentication with service user**

  Snowflake is deprecating single-factor passwords and will disallow passwords for service users (TYPE=SERVICE) by October 2026. For that reason, we strongly recommend configuring the transfer user as a service user with key-pair authentication.
</Note>

## Configuration steps

<Steps>
  ### Create role, user, warehouse, and database in the data warehouse

  1. Review and make any changes to the following setup script.

     ```sql
     begin;

     -- create variables for user / role / warehouse / database
     set user_name = 'TRANSFER_USER'; -- all letters must be uppercase
     set role_name = 'TRANSFER_ROLE'; -- all letters must be uppercase
     set warehouse_name = 'TRANSFER_WAREHOUSE'; -- all letters must be uppercase
     set database_name = 'TRANSFER_DATABASE'; -- all letters must be uppercase

     -- change role to securityadmin for user / role steps
     use role securityadmin;

     -- create role for data transfer service
     create role if not exists identifier($role_name);
     grant role identifier($role_name) to role SYSADMIN; -- establish SYSADMIN as the parent of the new role. Note: this does not grant the access privileges of SYSADMIN to the new role.

     -- create a user for data transfer service
     create user if not exists identifier($user_name)
     RSA_PUBLIC_KEY='MIIBIjANBgkqh...'; -- replace with the complete public key as required in the prerequisite

     -- set default role and warehouse to new user
     alter user identifier($user_name) SET default_role = $role_name;
     alter user identifier($user_name) SET default_warehouse = $warehouse_name;
     alter user identifier($user_name) SET type = service;

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

     <Warning>
       **Alternative authentication method: username & password**

       By default, this script creates a new user using key-pair authentication. If you'd prefer to use username & password authentication, instead of:

       ```sql
        create user if not exists identifier($user_name)
        RSA_PUBLIC_KEY='MIIBIjANBgkqh...';
       ```

       Use the following block:

       ```sql
       create user if not exists identifier($user_name)
       password = 'some_password';
       ```
     </Warning>

     <Note>
       **Using an existing `schema`**

       By default, a new schema (with a name you provide) will be created in the target Snowflake database upon the initial connection. If instead you create the `schema` ahead of time, you may remove the `CREATE SCHEMA` permission, and instead  `grant ALL PRIVILEGES` on the target `schema` for the designated `role`.

       The script below can be used to complete this step:

       ```sql
       set role_name = 'TRANSFER_ROLE';
       set database_name = 'TRANSFER_DATABASE';
       set schema_name = 'PRECREATED_SCHEMA';

       use database identifier($database_name);
       grant ALL PRIVILEGES on schema identifier($schema_name) to role identifier($role_name);
       ```
     </Note>

     <Note>
       **Using an existing `warehouse` or `database`**

       By default, this script creates a new warehouse and a new database. If you'd prefer to use an existing warehouse/database, change the `warehouse_name` variable from `TRANSFER_WAREHOUSE` to the name of the warehouse to be shared/`database_name` variable from `TRANSFER_DATABASE` to the name of the database to be shared.
     </Note>

  2. In the Snowflake interface, select the dropdown next to the "Run" button, and click **Run All**. This will run every query in the script at once. If successful, you will see `Statement executed successfully` in the query results.

  ### Configure the Snowflake access policy

  If your Snowflake data warehouse is using Snowflake Access Policies, a new policy must be added to allow Webflow's static IP to write to the warehouse.

  1. Review current network policies to check for existing IP allowlists.

     ```sql
     SHOW NETWORK POLICIES;
     ```

  2. If there is no existing Snowflake Network Policies (the `SHOW` query returns no results), you can skip to Step 3.

  3. If there is an existing Snowflake Network Policy, you must alter the existing policy or create a new one to allowlist Webflow's static IP address. Use the `CREATE NETWORK POLICY` command to specify the IP addresses that can access your Snowflake warehouse.

     ```sql
     CREATE NETWORK POLICY <transfer_service_policy_name> ALLOWED_IP_LIST = ('34.69.83.207/32');
     ```

  <Note>
    **Network allowlisting**

    Webflow Static IP: `34.69.83.207/32`
  </Note>

  <Error>
    **Creating your first network policy**

    If you have no existing network policies and you create your first as part of this step, all other IPs outside of the `ALLOWED_IP_LIST` will be blocked. Snowflake does not allow setting a network policy that blocks your current IP address. (An error message results while trying to create a network policy that blocks the current IP address.) But be careful when setting your first network policy.
  </Error>

  ### Add your destination

  Use the following details to complete the connection setup: **host name**, **database name**, your chosen **schema name**, **username**, and **password**.

  * Instructions for [Analyze / Optimize for Webflow sites](https://help.webflow.com/hc/en-us/articles/49267788589587)
  * Instructions for [Optimize for non-Webflow sites](https://help-optimize.webflow.com/hc/en-us/articles/49270819766931)
</Steps>

## Permissions checklist

* Role grants:
  * `USAGE` on the target warehouse
  * If the destination schema will be created by the service:
    * `USAGE` and `CREATE SCHEMA` on the target database (the setup script also includes `MONITOR`)
  * If using a pre-created schema:
    * `USAGE` on the target database
    * `ALL PRIVILEGES` on the target schema
* User defaults set (optional but recommended): `DEFAULT_ROLE`, `DEFAULT_WAREHOUSE`
* If using key-pair authentication: user has the PKCS#8 `RSA_PUBLIC_KEY` set
* If network policies are enforced: Webflow's egress IP is allowlisted

## FAQs

<Accordion title="How is the Snowflake connection secured?">
  We recommend key-based authentication. You register a public key on a Snowflake user and we authenticate using the corresponding private key, so no password is shared or stored. You can also enforce Snowflake Network Policies to allowlist Webflow's egress IP.
</Accordion>

<Accordion title="What permissions does the data transfer role need?">
  Minimum grants:

  * `USAGE` on the warehouse
  * If the destination schema will be created by the service: `USAGE` and `CREATE SCHEMA` on the database
  * If using a pre-created schema: `USAGE` on the database and `ALL PRIVILEGES` on the schema
</Accordion>

<Accordion title="Can I use an existing warehouse?">
  Yes. Grant `USAGE` on that warehouse to the transfer role. You may also size the warehouse to control performance/cost.
</Accordion>

<Accordion title="Should I include the -----BEGIN PUBLIC KEY----- and -----END PUBLIC KEY----- tags in the public key when adding it to Snowflake?">
  No, you should only provide the raw public key string, without the `-----BEGIN PUBLIC KEY-----` and `-----END PUBLIC KEY-----` tags.
</Accordion>

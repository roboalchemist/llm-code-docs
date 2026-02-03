# Source: https://docs.datafold.com/integrations/databases/snowflake.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Snowflake

**NOTE**: Datafold needs permissions in your Snowflake dataset to read your table data. You will need to be a Snowflake *Admin* in order to grant the required permissions.

**Steps to complete:**

* [Create a user and role for Datafold](/integrations/databases/snowflake#create-a-user-and-role-for-datafold)
* [Setup password-based](/integrations/databases/snowflake#set-up-password-based-authentication) or [Use key-pair authentication](/integrations/databases/snowflake#use-key-pair-authentication)
* [Create a temporary schema](/integrations/databases/snowflake#create-schema-for-datafold)
* [Give the Datafold role access to your warehouse](/integrations/databases/snowflake#give-the-datafold-role-access)
* [Configure your data connection in Datafold](/integrations/databases/snowflake#configure-in-datafold)

## Create a user and role for Datafold

> A [full script](/integrations/databases/snowflake#full-script) can be found at the bottom of this page.

It is best practice to create a separate role for the Datafold integration (e.g., `DATAFOLDROLE`):

```
CREATE ROLE DATAFOLDROLE;
CREATE USER DATAFOLD DEFAULT_ROLE = "DATAFOLDROLE" MUST_CHANGE_PASSWORD = FALSE;
GRANT ROLE DATAFOLDROLE TO USER DATAFOLD;

```

To provide column-level lineage, Datafold needs to read & parse all SQL statements executed in your Snowflake account:

```
GRANT MONITOR EXECUTION ON ACCOUNT TO ROLE DATAFOLDROLE;
GRANT IMPORTED PRIVILEGES ON DATABASE SNOWFLAKE TO ROLE DATAFOLDROLE;

```

## Set up password-based authentication

Datafold supports username/password authentication, but also key-pair authentication.

```
ALTER USER DATAFOLD SET PASSWORD = 'SomethingSecret';

```

You can set the username/password in the Datafold web UI.

### Use key-pair authentication

If you would like to use key-pair authentication, go to **Settings** -> **Data Connections** -> **Your Snowflake Connection**, and change Authentication method from **Password** to **Key Pair**.
Generate and Download the Key Pair file, and use the value within the file when running the following command in Snowflake to set the key for this Snowflake role:

```
ALTER USER DATAFOLD SET rsa_public_key='...'

```

## Create schema for Datafold

Datafold utilizes a temporary dataset to materialize scratch work and keep data processing in the your warehouse.

```
CREATE SCHEMA <database_name>.DATAFOLD_TMP;
GRANT ALL ON SCHEMA <database_name>.DATAFOLD_TMP TO DATAFOLDROLE;

```

## Give the Datafold role access

Datafold will only scan the tables that it has access to. The snippet below will give Datafold read access to a database. If you have more than one database that you want to use in Datafold, rerun the script below for each one.

```Bash  theme={null}
/* Repeat for every DATABASE to be usable in Datafold. This allows Datafold to
correctly discover, profile & diff each table */
GRANT USAGE ON WAREHOUSE <warehouse_name> TO ROLE DATAFOLDROLE;
GRANT USAGE ON DATABASE <database_name> TO ROLE DATAFOLDROLE;

GRANT USAGE ON ALL SCHEMAS IN DATABASE <database_name> TO ROLE DATAFOLDROLE;
GRANT USAGE ON FUTURE SCHEMAS IN DATABASE <database_name> TO ROLE DATAFOLDROLE;

GRANT SELECT ON ALL TABLES IN DATABASE <database_name> TO ROLE DATAFOLDROLE;
GRANT SELECT ON FUTURE TABLES IN DATABASE <database_name> TO ROLE DATAFOLDROLE;

GRANT SELECT ON ALL VIEWS IN DATABASE <database_name> TO ROLE DATAFOLDROLE;
GRANT SELECT ON FUTURE VIEWS IN DATABASE <database_name> TO ROLE DATAFOLDROLE;

GRANT SELECT ON ALL MATERIALIZED VIEWS IN DATABASE <database_name> TO ROLE DATAFOLDROLE;
GRANT SELECT ON FUTURE MATERIALIZED VIEWS IN DATABASE <database_name> TO ROLE DATAFOLDROLE;

GRANT ALL PRIVILEGES ON ALL DYNAMIC TABLES IN DATABASE <database_name> TO ROLE DATAFOLDROLE;
GRANT SELECT ON FUTURE DYNAMIC TABLES IN DATABASE <database_name> TO ROLE DATAFOLDROLE;

```

## Full Script

```Bash  theme={null}
--Step 1: Create a user and role for Datafold
CREATE ROLE DATAFOLDROLE;
CREATE USER DATAFOLD DEFAULT_ROLE = "DATAFOLDROLE" MUST_CHANGE_PASSWORD = FALSE;
GRANT ROLE DATAFOLDROLE TO USER DATAFOLD;

GRANT MONITOR EXECUTION ON ACCOUNT TO ROLE DATAFOLDROLE;
GRANT IMPORTED PRIVILEGES ON DATABASE SNOWFLAKE TO ROLE DATAFOLDROLE;

--Step 2a: Use password-based authentication
ALTER USER DATAFOLD SET PASSWORD = 'SomethingSecret';
--OR
--Step 2b: Use key-pair authentication
--ALTER USER DATAFOLD SET rsa_public_key='abc..'

--Step 3: Create schema for Datafold
CREATE SCHEMA <database_name>.DATAFOLD_TMP;
GRANT ALL ON SCHEMA <database_name>.DATAFOLD_TMP TO DATAFOLDROLE;

--Step 4: Give the Datafold role access to your data connection
/*
  Repeat for every DATABASE to be usable in Datafold. This allows Datafold to
  correctly discover, profile & diff each table
*/
GRANT USAGE ON WAREHOUSE <warehouse_name> TO ROLE DATAFOLDROLE;
GRANT USAGE ON DATABASE <database_name> TO ROLE DATAFOLDROLE;

GRANT USAGE ON ALL SCHEMAS IN DATABASE <database_name> TO ROLE DATAFOLDROLE;
GRANT USAGE ON FUTURE SCHEMAS IN DATABASE <database_name> TO ROLE DATAFOLDROLE;

GRANT SELECT ON ALL TABLES IN DATABASE <database_name> TO ROLE DATAFOLDROLE;
GRANT SELECT ON FUTURE TABLES IN DATABASE <database_name> TO ROLE DATAFOLDROLE;

GRANT SELECT ON ALL VIEWS IN DATABASE <database_name> TO ROLE DATAFOLDROLE;
GRANT SELECT ON FUTURE VIEWS IN DATABASE <database_name> TO ROLE DATAFOLDROLE;

GRANT SELECT ON ALL MATERIALIZED VIEWS IN DATABASE <database_name> TO ROLE DATAFOLDROLE;
GRANT SELECT ON FUTURE MATERIALIZED VIEWS IN DATABASE <database_name> TO ROLE DATAFOLDROLE;

```

## Validate Snowflake Grants for Datafold

Run these queries to validate that the grants have been set up correctly:

> Note: More results may be returned than shown in the screenshots below if you have granted access to multiple roles/users

Example Placeholders:

* `<database_name>` = `DEV`
* `<warehouse_name>` = `DEMO`

```
-- Validate database usage for the DATAFOLDROLE
SHOW GRANTS ON DATABASE <database_name>;
```

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_database-cbcb5fd91f9d1ba6a680641fd1ed2cde.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=242ae31d65b18810648b26d7124c8161" data-og-width="1634" width="1634" data-og-height="167" height="167" data-path="images/grants_on_database-cbcb5fd91f9d1ba6a680641fd1ed2cde.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_database-cbcb5fd91f9d1ba6a680641fd1ed2cde.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a8b95f3f0969bb3eb017d9aa87cb1a7c 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_database-cbcb5fd91f9d1ba6a680641fd1ed2cde.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=bce109e8aa6bb78f4f7b89acdf376e92 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_database-cbcb5fd91f9d1ba6a680641fd1ed2cde.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a4b3404e2b21c32411676d7a7844f7d0 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_database-cbcb5fd91f9d1ba6a680641fd1ed2cde.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=2e768bab9f7a701c32495dec981919d8 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_database-cbcb5fd91f9d1ba6a680641fd1ed2cde.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=54c6fdeb3e359eefcdfec99a0f78a7cc 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_database-cbcb5fd91f9d1ba6a680641fd1ed2cde.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=ea23f295a92e29580646b27723c97505 2500w" />
</Frame>

```
-- Validate warehouse usage for the DATAFOLDROLE
SHOW GRANTS ON WAREHOUSE <warehouse_name>;
```

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_warehouse-45351631336f32ccbeeaa6646a1a9199.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5e98412c95861ed744dcfd60275a5b6d" data-og-width="1643" width="1643" data-og-height="170" height="170" data-path="images/grants_on_warehouse-45351631336f32ccbeeaa6646a1a9199.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_warehouse-45351631336f32ccbeeaa6646a1a9199.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=caafcc40d0f21ad5a07865393981d714 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_warehouse-45351631336f32ccbeeaa6646a1a9199.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=7497892f736cefbe3a09d9988ebdb464 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_warehouse-45351631336f32ccbeeaa6646a1a9199.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=6c242b835643e7e112a27da7d9d29f51 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_warehouse-45351631336f32ccbeeaa6646a1a9199.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=08e81bfd1b66ee1aec62e851b6a3ed66 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_warehouse-45351631336f32ccbeeaa6646a1a9199.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=974ef96a9e48f1f8aeb443d6736834e4 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_warehouse-45351631336f32ccbeeaa6646a1a9199.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=6da58b89ba217cccb3531a0363eb008c 2500w" />
</Frame>

```
-- Validate schema permissions for the DATAFOLDROLE
SHOW GRANTS ON SCHEMA <database_name>.DATAFOLD_TMP;
```

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_schema-6955ab0c695f05ab0fd245a231a20837.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5513f6f7210fcf3ead5b3c2049da36a4" data-og-width="1644" width="1644" data-og-height="926" height="926" data-path="images/grants_on_schema-6955ab0c695f05ab0fd245a231a20837.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_schema-6955ab0c695f05ab0fd245a231a20837.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=4e1ad627c40506aeaf0d7d6a38ac8171 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_schema-6955ab0c695f05ab0fd245a231a20837.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=29b4e004070780f24db2d9ee7e5f943d 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_schema-6955ab0c695f05ab0fd245a231a20837.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=4fc4fb151564fdaaa2dd278006281aa8 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_schema-6955ab0c695f05ab0fd245a231a20837.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=9aba8c9f8c64bc46333c503056b61bcf 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_schema-6955ab0c695f05ab0fd245a231a20837.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=1e8222b8cf320c449c77287e97f1b1bc 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/grants_on_schema-6955ab0c695f05ab0fd245a231a20837.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=8b6ab2cf2fe70c524d2e38e04b00ed6e 2500w" />
</Frame>

## A note on future grants

The above database grants will be insufficient if any future grants have been defined at the schema level, because [schema-level grants will override database-level grants](https://docs.snowflake.com/en/sql-reference/sql/grant-privilege#considerations). In that case, you will need to execute future grants for every existing *schema* that Datafold will operate on.

```Bash  theme={null}
GRANT SELECT ON FUTURE TABLES IN SCHEMA <database_name>.<schema_name> TO ROLE DATAFOLDROLE;
GRANT SELECT ON FUTURE VIEWS IN SCHEMA <database_name>.<schema_name> TO ROLE DATAFOLDROLE;
GRANT SELECT ON FUTURE MATERIALIZED VIEWS IN SCHEMA <database_name>.<schema_name> TO ROLE DATAFOLDROLE;
GRANT SELECT ON ALL TABLES IN SCHEMA <database_name>.<schema_name> TO ROLE DATAFOLDROLE;
GRANT SELECT ON ALL VIEWS IN SCHEMA <database_name>.<schema_name> TO ROLE DATAFOLDROLE;
GRANT SELECT ON ALL MATERIALIZED VIEWS IN SCHEMA <database_name>.<schema_name> TO ROLE DATAFOLDROLE;

```

## Configure in Datafold

| Field Name                  | Description                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                        | A name given to the data connection within Datafold                                                                                                                                                                                                                                                                                                                                          |
| Account identifier          | The Org name-Account name pair for your Snowflake account. This can be found in the browser address string. It may look like [https://orgname-accountname.snowflakecomputing.com](https://orgname-accountname.snowflakecomputing.com) or [https://app.snowflake.com/orgname/accountname](https://app.snowflake.com/orgname/accountname). In the setup form, enter \<orgname>-\<accountname>. |
| User                        | The username set in the [Setup password-based](/integrations/databases/snowflake#set-up-password-based-authentication) authentication section                                                                                                                                                                                                                                                |
| Password                    | The password set in the [Setup password-based](/integrations/databases/snowflake#set-up-password-based-authentication) authentication section                                                                                                                                                                                                                                                |
| Key Pair file               | The key file generated in the [Use key-pair authentication](/integrations/databases/snowflake#use-key-pair-authentication) section                                                                                                                                                                                                                                                           |
| Warehouse                   | The Snowflake warehouse name                                                                                                                                                                                                                                                                                                                                                                 |
| Schema for temporary tables | The schema name you created with our script (\<database\_name>.DATAFOLD\_TMP)                                                                                                                                                                                                                                                                                                                |
| Role                        | The role you created for Datafold (Typically DATAFOLDROLE)                                                                                                                                                                                                                                                                                                                                   |
| Default DB                  | A database the role above can access. If more than one database was added, whichever you prefer to be the default                                                                                                                                                                                                                                                                            |

> Note: Please review the documentation for the account name. Datafold uses Format 1 (Preferred): [https://docs.snowflake.com/en/user-guide/admin-account-identifier#using-an-account-locator-as-an-identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier#using-an-account-locator-as-an-identifier)

Click **Create**. Your data connection is ready!

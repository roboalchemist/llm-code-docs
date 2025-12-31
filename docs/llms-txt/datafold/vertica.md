# Source: https://docs.datafold.com/integrations/databases/vertica.md

# OpenText Analytics Database (Vertica)

<Note>
  **INFO**

  Column-level Lineage is not supported for Vertica.
</Note>

**Steps to complete:**

1. [Run SQL script and create schema for Datafold](/integrations/databases/vertica#run-sql-script-and-create-schema-for-datafold)
2. [Configure your data connection in Datafold](/integrations/databases/vertica#configure-in-datafold)

## Run SQL script and create schema for Datafold

To connect to Vertica, you need to create a user with read-only access to all tables in all schemas, write access to Datafold-specific schema for temporary tables:

```Bash  theme={null}
/* Datafold utilizes a temporary dataset to materialize scratch work and keep data processing in your warehouse. */

CREATE SCHEMA datafold_tmp;

/* Create a datafold user */

CREATE ROLE datafold WITH LOGIN ENCRYPTED PASSWORD 'SOMESECUREPASSWORD';

/* Give the datafold role write access to the temporary schema */

GRANT ALL ON SCHEMA datafold_tmp TO datafold;

/* Make sure that the user has read permissions on the tables */

GRANT USAGE ON SCHEMA <myschema> TO datafold;
GRANT SELECT ON ALL TABLES IN SCHEMA <myschema> TO datafold;

```

Datafold utilizes a temporary schema, named `datafold_tmp` in the above script, to materialize scratch work and keep data processing in the your warehouse.

### Configure in Datafold

| Field Name    | Description                                                               |
| ------------- | ------------------------------------------------------------------------- |
| Name          | A name given to the data connection within Datafold                       |
| Host          | The hostname address for your database; default value 127.0.0.1           |
| Port          | Vertica connection port; default value is 5433                            |
| User          | The user role created in the SQL script; datafold                         |
| Password      | The password created in the SQL permissions script                        |
| Database Name | The name of the Vertica database you want to connect to, default is VMart |

Click **Create**. Your data connection is ready!

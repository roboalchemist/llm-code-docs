# Source: https://docs.datafold.com/integrations/databases/oracle.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Oracle

<Note>
  **INFO**

  Please contact [support@datafold.com](mailto:support@datafold.com) if you use an Oracle version \< 19.x.
</Note>

<Note>
  **INFO**

  Column-level Lineage is not currently supported for Oracle.
</Note>

**Steps to complete:**

1. [Run SQL script and create schema for Datafold](/integrations/databases/oracle#run-sql-script-and-create-schema-for-datafold)
2. [Configure your data connection in Datafold](/integrations/databases/oracle#configure-in-datafold)

## Run SQL script and create schema for datafold\_group

To connect to Oracle, create a user with read-only access to all tables you wish to diff. Include read and write access to a Datafold-specific temp schema:

```Bash  theme={null}
-- Switch container context (default is "XEPDB1")
ALTER SESSION SET CONTAINER = YOURCONTAINER;

-- Create a Datafold user/schema
CREATE USER DATAFOLD IDENTIFIED BY somesecurepassword;

-- Allow Datafold user to connect
GRANT CREATE SESSION TO DATAFOLD;

-- Allow user to create tables in DATAFOLD schema
GRANT CREATE TABLE TO DATAFOLD;

-- Grant read access to diff tables in your schema
GRANT SELECT ON "YOURSCHEMA"."YOURTABLE" TO DATAFOLD;

-- Grant access to DBMS_CRYPTO utilities (hashing functions, etc.)
GRANT EXECUTE ON SYS.DBMS_CRYPTO TO DATAFOLD;

-- Allow Datafold users/schemas to use disk space (adjust if needed)
GRANT UNLIMITED TABLESPACE TO DATAFOLD;

-- Apply the changes
COMMIT;

```

Datafold utilizes a temporary dataset to materialize scratch work and keep data processing in the your warehouse.

## Configure in Datafold

| Field Name                  | Description                                                                                    |
| --------------------------- | ---------------------------------------------------------------------------------------------- |
| Name                        | A name given to the data connection within Datafold                                            |
| Host                        | The hostname address for your database                                                         |
| Port                        | Postgres connection port; default value is 1521                                                |
| User                        | The user role created in our SQL script, named DATAFOLD                                        |
| Password                    | The password created in our SQL script                                                         |
| Connection type             | Choose Service or SID depending on your connection type; default value is Service              |
| Service (or SID)            | The name of the database (Service or SID) you want to connect to, e.g. XEPDB1 or YOURCONTAINER |
| Schema for temporary tables | The user/schema created in our SQL script - DATAFOLD                                           |

Click **Create**. Your data connection is ready!

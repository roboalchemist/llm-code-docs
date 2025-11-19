# Source: https://docs.datafold.com/integrations/databases/sql-server.md

# Microsoft SQL Server

<Note>
  **INFO**

  Column-level Lineage is not currently supported for Microsoft SQL Server.
</Note>

**Steps to complete:**

1. [Run SQL script and create schema for Datafold](/integrations/databases/sql-server#run-sql-script-and-create-schema-for-datafold)
2. [Configure your data connection in Datafold](/integrations/databases/sql-server#configure-in-datafold)

## Run SQL script and create schema for Datafold

To connect to Microsoft SQL Server, create a user with read-only access to all tables you wish to diff. Include read and write access to a Datafold-specific temp schema:

```Bash  theme={null}
/* Select the database that will contain the temp schema */
USE DatabaseName;

/* Datafold utilizes a temporary dataset to materialize scratch work and keep data processing in the your warehouse. */
CREATE SCHEMA datafold_tmp;

/* Create the Datafold user */
CREATE LOGIN DatafoldUser WITH PASSWORD = 'SOMESECUREPASSWORD';
CREATE USER DatafoldUser FOR LOGIN DatafoldUser;

/* Grant read access to diff tables */
GRANT SELECT ON SCHEMA::YourSchema TO DatafoldUser;

/* Grant read + write access to datafold_tmp schema */
GRANT SELECT, INSERT, UPDATE, DELETE ON SCHEMA::datafold_tmp TO DatafoldUser;
```

## Configure in Datafold

| Field Name                   | Description                                                                                                      |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Connection name              | A name given to the data connection within Datafold                                                              |
| Host                         | The hostname for your SQL Server instance                                                                        |
| Port                         | SQL Server connection port; default value is 1433                                                                |
| Username                     | The user created in our SQL script, named DatafoldUser                                                           |
| Password                     | The password created in our SQL script                                                                           |
| Database                     | The name of the SQL Server database you want to connect to                                                       |
| Dataset for temporary tables | The schema created in our SQL script, in database.schema format: DatabaseName.datafold\_tmp in our script above. |

Click **Create**. Your data connection is ready!

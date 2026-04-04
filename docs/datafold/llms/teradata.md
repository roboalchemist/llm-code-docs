# Source: https://docs.datafold.com/integrations/databases/teradata.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Teradata

<Note>
  **INFO**

  Column-level Lineage is not currently supported for Teradata.
</Note>

**Steps to complete:**

1. [Configure user in Teradata](#configure-user-in-tedadata)
2. [Create a temporary database for Datafold](#create-a-temporary-database-for-datafold)
3. [Configure data connection in Datafold](#configure-in-datafold)

## Configure user in Teradata

To connect to Teradata, create a user with read-only access to all databases you may wish to diff, including the login database:

```
CREATE USER DATAFOLD AS PERMANENT=1000000000 BYTES PASSWORD= <PASSWORD> COLLATION = ASCII TIME ZONE ='GMT';
GRANT EXECUTE FUNTION ON DB1 TO DATAFOLD;
GRANT SELECT ON DB1 TO DATAFOLD;
...
GRANT SELECT ON DB9 TO DATAFOLD;
```

## Create a temporary database for Datafold

Datafold requires a database to store temporary data with full permissions:

```
CREATE DATABASE DATAFOLD_TMP AS PERMANENT=10000000000 BYTES;
GRANT ALL ON DATAFOLD_TMP TO DATAFOLD;
```

## Configure data connection in Datafold

| Field Name                    | Description                                                                                                                |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Connection Name               | A name given to the data connection within Datafold.                                                                       |
| Host                          | The hostname for your Teradata instance (e.g., account-name-2e3ba8b32qac9d.env.clearscape.teradata.com for Teradata SaaS). |
| Port                          | Teradata endpoint port; the default value is 1025.                                                                         |
| User ID                       | User ID, e.g., DATAFOLD.                                                                                                   |
| Password                      | Password from above.                                                                                                       |
| Database                      | The connection database, e.g., DB1 from above.                                                                             |
| Database for Temporary Tables | The temporary database, e.g., DATAFOLD\_TMP from above.                                                                    |

Click **Create**. Your data connection is now ready!

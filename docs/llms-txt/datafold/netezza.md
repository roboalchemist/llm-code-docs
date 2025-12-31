# Source: https://docs.datafold.com/integrations/databases/netezza.md

# Netezza

<Note>
  **INFO**

  Column-level Lineage is not currently supported for Netezza.
</Note>

**Steps to complete:**

1. [Configure user in Netezza](#configure-user-in-netezza)
2. [Create schema for Datafold](#create-a-temporary-database-for-datafold)
3. [Configure your data connection in Datafold](#configure-in-datafold)

## Configure user in Netezza

To connect to Netezza, create a user with read-only access to all databases you may wish to diff.

## Create a temporary database for Datafold

Datafold requires a schema with full permissions to store temporary data.

## Configure in Datafold

| Field Name                  | Description                                                                                                                                   |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Connection Name             | A name given to the data connection within Datafold.                                                                                          |
| Host                        | The hostname for your Netezza instance (e.g., nz-85dcf66c-69aa-4ba6-b7cb-827643da5a.us-east-1.data-warehouse.cloud.ibm.com for Netezza SaaS). |
| Port                        | Netezza endpoint port; the default value is 5480.                                                                                             |
| Encryption                  | Whether to use TLS.                                                                                                                           |
| User ID                     | User ID, e.g., DATAFOLD.                                                                                                                      |
| Password                    | Password from above.                                                                                                                          |
| Default DB                  | The database to connect to.                                                                                                                   |
| Schema for Temporary Tables | Use DATABASE.SCHEMA format.                                                                                                                   |

Click **Create**. Your data source is now ready!

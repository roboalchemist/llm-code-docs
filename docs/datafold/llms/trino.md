# Source: https://docs.datafold.com/integrations/databases/trino.md

# Trino

<Note>
  **INFO**

  Lineage is not currently supported for Trino.
</Note>

**Steps to complete:**

1. [Configure user in Trino](#configure-user-in-trino)
2. [Create schema for Datafold](#create-schema-for-datafold)
3. [Configure your data connection in Datafold](#configure-in-datafold)

## Configure user in Trino

To connect to Trino, create a user with read-only access to all data sources you wish to diff. Datafold also requires a schema set up with read/write permissions within one of the catalogs.

## Create schema for Datafold

Datafold utilizes a temporary dataset to materialize scratch work and keep data processing in the your warehouse.

## Configure in Datafold

| Field Name                  | Description                                                  |
| --------------------------- | ------------------------------------------------------------ |
| Connection name             | A name given to the data connection within Datafold.         |
| Host                        | The hostname for your trino instance.                        |
| Port                        | Trino endpoint port; default value is 443.                   |
| Encryption                  | Should be checked, possibly unchecked for local deployments. |
| User ID                     | User ID as created in Trino.                                 |
| Password                    | Password, as created in Trino.                               |
| Schema for temporary tables | Use `<catalog>.<schema>` format.                             |

Click **Create**. Your data source is now ready!

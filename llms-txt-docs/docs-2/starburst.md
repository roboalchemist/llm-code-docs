# Source: https://docs.datafold.com/integrations/databases/starburst.md

# Starburst

<Note>
  **INFO**

  Column-level Lineage is not currently supported for Starburst.
</Note>

**Steps to complete:**

1. [Configure user in Starburst](#configure-user-in-starburst)
2. [Create schema for Datafold](#create-schema-for-datafold)
3. [Configure your data connection in Datafold](#configure-in-datafold)

## Configure user in Starburst

To connect to Starburst, create a user with read-only access to all data sources you wish to diff and optionally generate an access token. Datafold requires a schema to be set up within one of the catalogs, typically hosted on platforms like Amazon S3 or similar services.

## Create schema for Datafold

Datafold utilizes a temporary dataset to materialize scratch work and keep data processing in the your warehouse.

## Configure in Datafold

| Field Name                  | Description                                                                                                          |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Connection name             | A name given to the data connection within Datafold.                                                                 |
| Host                        | The hostname for your Starburst instance (e.g., `sample-free-cluster.trino.galaxy.starburst.io` for Starburst SaaS). |
| Port                        | Starburst endpoint port; default value is 433.                                                                       |
| Encryption                  | Should be checked for Starburst Galaxy, possibly unchecked for local deployments.                                    |
| User ID                     | User ID as created in Starburst, typically an email address.                                                         |
| Token                       | Access token generated in Starburst.                                                                                 |
| Password                    | Alternatively, provide a password.                                                                                   |
| Schema for temporary tables | Use `<catalog>.<schema>` format.                                                                                     |

Click **Create**. Your data source is now ready!

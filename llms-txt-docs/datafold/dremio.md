# Source: https://docs.datafold.com/integrations/databases/dremio.md

# Dremio

<Note>
  **INFO**

  Column-level Lineage is not currently supported for Dremio.
</Note>

<Note>
  **INFO**

  Schemas for tables in external data sources need to be specified with quotes e.g., "Postgres prod.analytics.sales".
</Note>

**Steps to complete:**

1. [Configure user in Dremio](/integrations/databases/dremio#configure-user-in-dremio)
2. [Create schema for Datafold](/integrations/databases/dremio#create-schema-for-datafold)
3. [Configure your data connection in Datafold](/integrations/databases/dremio#configure-in-datafold)

## Configure user in Dremio

To connect to Dremio, create a user with read-only access to all data sources you wish to diff and generate an access token.

Temporary tables will be created in the `$scratch` schema that doesn't require special permissions.

## Create schema for Datafold

Datafold utilizes a temporary dataset to materialize scratch work and keep data processing in the your warehouse.

## Configure in Datafold

| Field Name                  | Description                                                                                                                                                |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Connection name             | A name given to the data connection within Datafold.                                                                                                       |
| Host                        | The hostname for your Dremio instance (data.dremio.cloud for Dremio SaaS).                                                                                 |
| Port                        | Dremio endpoint port; default value is 433.                                                                                                                |
| Encryption                  | Should be checked for Dremio Cloud, possibly unchecked for local deployments.                                                                              |
| User ID                     | User ID as created in Dremio, typically an email address.                                                                                                  |
| Project ID                  | Dremio Project UID. If left blank, the default project will be used.                                                                                       |
| Token                       | Access token generated in Dremio.                                                                                                                          |
| Password                    | Alternatively, provide a password.                                                                                                                         |
| Schema for temporary views  | A Dremio space for temporary views.                                                                                                                        |
| Schema for temporary tables | \$scratch should suit most applications, or use "\<Datasource>.\<schema>" (with quotes) if you wish to create temporary tables in an external data source. |

Click **Create**. Your data connection is now ready!

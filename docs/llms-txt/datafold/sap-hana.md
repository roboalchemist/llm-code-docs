# Source: https://docs.datafold.com/integrations/databases/sap-hana.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SAP HANA

<Note>
  **INFO**

  Column-level Lineage is not currently supported for SAP HANA.
</Note>

**Steps to complete:**

1. [Create and authorize a user](#create-and-authorize-a-user)
2. [Create schema for Datafold](#create-schema-for-datafold)
3. [Configure in Datafold](#configure-in-datafold)

## Create and authorize a user

Create a new user `DATAFOLD` using SAP HANA Administration console (Systems-Security-Users). Specify password authentication, and set "Force password change on next logon" to "No". Grant MONITORING privileges for the databases to be diffed.

## Create schema for Datafold

Datafold utilizes a temporary schema to materialize scratch work and keep data processing in the your warehouse.

```
CREATE SCHEMA datafold_tmp OWNED BY DATAFOLD;

```

## Configure in Datafold

| Field Name                  | Description                                          |
| --------------------------- | ---------------------------------------------------- |
| Name                        | A name given to the data connection within Datafold. |
| Host                        | The hostname address for your database.              |
| Port                        | Sap HANA connection port; default value is 443.      |
| User                        | The user created above, named DATAFOLD.              |
| Password                    | The password for user DATAFOLD.                      |
| Schema for temporary tables | The schema created above, named datafold\_tmp        |

Click **Create**. Your data connection is ready!

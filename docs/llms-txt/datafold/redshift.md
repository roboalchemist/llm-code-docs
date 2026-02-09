# Source: https://docs.datafold.com/integrations/databases/redshift.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Redshift

**Steps to complete:**

1. [Run SQL script and create schema for Datafold](/integrations/databases/redshift#run-sql-script-and-create-schema-for-datafold)
2. [Configure your data connection in Datafold](/integrations/databases/redshift#configure-in-datafold)

## Run SQL script and create schema for Datafold

To connect to Amazon Redshift, you must create a user with the following permissions:

* **Read-only access** to all tables in all schemas
* **Write access** to a dedicated temporary schema for Datafold
* **Access to SQL logs** for lineage construction

Datafold uses a temporary dataset to materialize scratch work and keep data processing in the your warehouse. Create the schema with:

```
CREATE SCHEMA datafold_tmp;
```

Next, create the Datafold user. To grant read access to all schemas, the user must have superuser-level privileges in Redshift:

```
CREATE USER datafold CREATEUSER PASSWORD 'SOMESECUREPASSWORD';
```

Grant unrestricted access to system logs so Datafold can build column-level lineage:

```
ALTER USER datafold WITH SYSLOG ACCESS UNRESTRICTED;
```

<Note>Datafold utilizes a temporary schema, named `datafold_tmp` in the above script, to materialize scratch work and keep data processing in your warehouse.</Note>

## Configure in Datafold

| Field Name                  | Description                                                                                                                                         |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                        | A name given to the data connection within Datafold                                                                                                 |
| Host                        | The hostname of your cluster. (Go to Redshift in your AWS console, select your cluster, the hostname is the endpoint listed at the top of the page) |
| Port                        | Redshift connection port; default value is 5439                                                                                                     |
| User                        | The user created in our SQL script, named `datafold`                                                                                                |
| Password                    | The password created in our SQL script                                                                                                              |
| Database Name               | The name of the Redshift database you want to connect to                                                                                            |
| Schema for temporary tables | The schema (`datafold_tmp`) created in our SQL script                                                                                               |

Click **Create**. Your data connection is ready!

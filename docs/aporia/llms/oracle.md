# Source: https://docs.aporia.com/data-sources/oracle.md

# Oracle

This guide describes how to connect Aporia to an Oracle data source in order to monitor your ML Model in production.&#x20;

We will assume that your model inputs, outputs and optionally delayed actuals can be queried with SQL. This data source may also be used to connect to your model's training set to be used as a baseline for model monitoring.

### Create a read-only user for Oracle access

In order to provide access to Oracle, create a read-only user for Aporia in Oracle.

Please use the SQL snippet below to create the user for Aporia. Before using the snippet, you will need to populate the following:

* `<username>`: The user name to create.
* `<aporia_password>`: Strong password to be used by the user.
* `<schema_name.table>`: The resources to which we want to granted access to the new user.

```sql
-- Create user and grant access
CREATE USER <username> IDENTIFIED BY '<aporia_password>';

-- Grant access to DB and schema
GRANT CONNECT TO <username>;

-- Grant access to multiple tables
GRANT SELECT ON schema_name.table1 TO <username>;
GRANT SELECT ON schema_name.table2 TO <username>;
GRANT SELECT ON schema_name.table3 TO <username>;
```

### Create a Oracle data source in Aporia

1. Go to [Aporia platform](https://platform.aporia.com/) and login to your account.
2. Go to **Integrations** page and click on the **Data Connectors** tab
3. Scroll to **Connect New Data Source** section
4. Click **Connect** on the Oracle card and follow the instructions
   1. Note that the provided URL should be in the following format `jdbc:oracle:thin:@hostname:port_number:instance_name`.

Bravo! :clap: now you can use the data source you've created across all your models in Aporia.

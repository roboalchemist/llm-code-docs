# Source: https://docs.datafold.com/integrations/databases/mysql.md

# MySQL

<Note>
  **INFO**

  Please contact [support@datafold.com](mailto:support@datafold.com) if you use a MySQL version \< 8.x.
</Note>

<Note>
  **INFO**

  Column-level Lineage is not currently supported for MySQL.
</Note>

**Steps to complete:**

1. [Run SQL script for permissions and create schema for Datafold](/integrations/databases/mysql#run-sql-script-and-create-schema-for-datafold)
2. [Configure your data connection in Datafold](/integrations/databases/mysql#configure-in-datafold)

### Run SQL script and create schema for Datafold

To connect to MySQL, create a user with read-only access to all tables you wish to diff. Include read and write access to a Datafold-specific dataset:

```Bash  theme={null}
-- Create a temporary dataset for Datafold to utilize
CREATE DATABASE IF NOT EXISTS datafold_tmp;

-- Create a Datafold user
CREATE USER 'datafold_user'@'%' IDENTIFIED BY 'SOMESECUREPASSWORD';

-- Grant read access to diff tables in YourSchema
GRANT SELECT ON `YourSchema`.* TO 'datafold_user'@'%';

-- Grant access to all tables in a datafold_tmp database
GRANT ALL ON `datafold_tmp`.* TO 'datafold_user'@'%';

-- Apply the changes
FLUSH PRIVILEGES;
```

Datafold utilizes a temporary dataset, named `datafold_tmp` in the above script, to materialize scratch work and keep data processing in the your warehouse.

### Configure in Datafold

| Field Name                   | Description                                                                     |
| ---------------------------- | ------------------------------------------------------------------------------- |
| Connection name              | A name given to the data connection within Datafold                             |
| Host                         | The hostname for your MySQL instance                                            |
| Port                         | MySQL connection port; default value is 3306                                    |
| Username                     | The user created in our SQL script, named datafold\_user                        |
| Password                     | The password created in our SQL script                                          |
| Database                     | The name of the MySQL database (schema) you want to connect to, e.g. YourSchema |
| Dataset for temporary tables | The datafold\_tmp database created in our SQL script                            |

Click **Create**. Your data connection is ready!

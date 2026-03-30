# Source: https://docs.axonius.com/docs/mariadb.md

# MariaDB

MariaDB is an open-source relational database management system that supports a wide range of database operations and integrations.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* Application Resources

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the MariaDB server that Axonius can communicate with via the [Required Ports](#required-ports).
2. **Port** *(required, default: 3306)* - The port used to connect to the MariaDB server.
3. **User Name** and **Password** *(required)* - The credentials for a user account that has  permission to fetch assets.
4. **Exclude Databases** *(optional)* - A comma-separated string of databases to exclude from the query. Default string: 'information\_schema, performance\_schema, mysql, sys'

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="MariaDB.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MariaDB.png" />

## APIs

Axonius uses the [MariaDB Connector/ODBC](https://mariadb.com/kb/en/mariadb-connector-odbc/).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **3306**

## Required Permissions

The value supplied in [User Name](#parameters) must have access to view all the databases and tables in order to fetch assets.

## Supported From Version

Supported from Axonius version 6.1.54.0

### Related Enforcement Actions

* [Maria DB - Create User](https://docs.axonius.com/axonius-help-docs/docs/maria-db-create-user)
* [Maria DB - Delete User](https://docs.axonius.com/axonius-help-docs/docs/maria-db-delete-user)
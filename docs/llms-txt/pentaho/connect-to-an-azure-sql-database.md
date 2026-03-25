# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/define-data-connections/enter-database-connection-information/connect-to-an-azure-sql-database.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/define-data-connections/enter-database-connection-information/connect-to-an-azure-sql-database.md

# Connect to an Azure SQL database

You can use an Azure SQL database as a data source with the PDI client. This connection is required if you want to use the PDI Bulk load into Azure SQL DB job entry to load data into your Azure SQL database from Azure Data Lake Storage. Pentaho supports the [Always Encrypted](https://docs.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver15) option, [dynamic masking](https://docs.microsoft.com/en-us/azure/azure-sql/database/dynamic-data-masking-overview), and multiple authentication methods for connecting to an Azure SQL database.

Because one physical server may host databases for multiple customers, keep in mind that SQL for Azure is different from MSSQL. For more information regarding the differences between Azure SQL and MSSQL, see <https://docs.microsoft.com/en-us/azure/azure-sql/database/features-comparison>

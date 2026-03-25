# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/bulk-load-into-azure-sql-db/before-you-begin-azure-sql-db-bulk.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/bulk-load-into-azure-sql-db/before-you-begin-azure-sql-db-bulk.md

# Before you begin

Before using the **Bulk load into Azure SQL DB** job entry in PDI, you must have the following items:

* An Azure account.
* A connection to the Azure SQL database in which to load your data. For more information, see the **Install Pentaho Data Integration and Analytics** document.
* A VFS connection to Azure Data Lake Storage.
* A table and schema set up in the database where you want to place your data. The table must have defined all the columns you need. On the first use, you need to create the table.

**Note:** The INSERT and ADMINISTER DATABASE BULK OPERATIONS permissions are required in the Azure SQL database to use the **Bulk Load into Azure SQL DB** job entry.

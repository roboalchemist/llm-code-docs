# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/define-data-connections/enter-database-connection-information/connect-to-an-azure-sql-database/use-the-always-encryption-option.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/define-data-connections/enter-database-connection-information/connect-to-an-azure-sql-database/use-the-always-encryption-option.md

# Use the Always Encryption Enabled option

Before you can use the **Always Encryption Enabled** option, you must perform the following steps. Consult the [Microsoft Azure SQL documentation](https://docs.microsoft.com/en-us/azure/azure-sql/) for assistance with your Azure SQL tools.

1. Generate a column master key in the Azure Key Vault.
2. Encrypt the column using the column master key.
3. Register the app under Azure Active Directory and obtain both the **Client id** and **Client Secret Key**.
4. Grant permissions to the **Client id** for accessing the Azure Key Vault.
5. Select **Always Encryption Enabled** and provide the **Client id** and **Client Secret Key**.

The Azure Always Encrypted feature is now active.

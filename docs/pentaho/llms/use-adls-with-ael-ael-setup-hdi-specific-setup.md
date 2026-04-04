# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/vendor-supplied-clients/microsoft-azure-hdinsight-ael-setup-vendor-supplied-clients/use-adls-with-ael-ael-setup-hdi-specific-setup.md

# Use ADLS with AEL

You need to delete, add, and modify specific properties in Amabari to use ADLS wih AEL.

1. Log in to Ambari.
2. Delete the following properties from Ambari:

   | Property                                  | Value                                                                          |
   | ----------------------------------------- | ------------------------------------------------------------------------------ |
   | `fs.azure.account.auth.type`              | `Custom`                                                                       |
   | `fs.azure.account.oauth.provider.type`    | `com.microsoft.azure.storage.oauth2.CredentialServiceBasedAccessTokenProvider` |
   | `fs.azure.delegation.token.provider.type` | `com.microsoft.azure.storage.oauth2.DelegationTokenManager`                    |
3. Add the following properties for accessing the storage account.

   | Property                                                             | Value         |
   | -------------------------------------------------------------------- | ------------- |
   | `fs.azure.account.auth.type.amitsecureadlsgen2.dfs.core.windows.net` | `SharedKey`   |
   | `fs.azure.account.key.amitsecureadlsgen2.dfs.core.windows.net`       | `<SharedKey>` |
4. Update the `fs.azure.enable.delegation.token` property to `false`.

You can now use ADLS with AEL for your instance of HDI.

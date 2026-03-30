# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/vendor-supplied-clients/microsoft-azure-hdinsight-ael-setup-vendor-supplied-clients/use-wasb-with-ael-ael-setup-hdi-specific-setup.md

# Use WASB with AEL

Perform the following steps to use WASB with AEL:

1. Log into Ambari.
2. Select the **ADVANCED** tab under **HDFS** > **CONFIGS**.
3. Edit **Custom Core-site (CCs)** for your instance of HDI.
4. Add or update the following properties under the **core-site.xml** section:

   | Property                                                                    | Value                                          |
   | --------------------------------------------------------------------------- | ---------------------------------------------- |
   | `fs.azure.account.keyprovider.<STORAGE_ACCOUNT_NAME>.blob.core.windows.net` | `org.apache.hadoop.fs.azure.SimpleKeyProvider` |
   | `fs.azure.account.key.<STORAGE_ACCOUNT_NAME>.blob.core.windows.net`         | `<DECRYPTED_ACCESS_KEY>`                       |

You can now use WASB with AEL for your instance of HDI.

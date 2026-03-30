# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-google-dataproc/install-the-google-cloud-sdk-on-your-local-machine-cp/set-command-variables-gdp.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-google-dataproc/install-the-google-cloud-sdk-on-your-local-machine-cp/set-command-variables-gdp.md

# Set command variables

Setting these commonly used command variables makes it easier to run command-line examples on your local machine or in Cloud Shell.

Perform the following steps to set command variables.

1. Export the project using the following example:

   ```
   $ export PROJECT=project;export HOSTNAME=hostname;export ZONE=zone
   ```

   1. Set the **PROJECT** variable to your Google Cloud project ID.
   2. Set the **HOSTNAME** variable to the name of the master node in your Dataproc cluster.

      **Note:** The master name ends with an -m suffix.
   3. Set the **ZONE** variable to the zone of the instances in your Dataproc cluster.

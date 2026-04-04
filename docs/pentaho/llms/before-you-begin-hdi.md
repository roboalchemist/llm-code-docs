# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-azure-hdinsight-cp/before-you-begin-hdi.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-azure-hdinsight-cp/before-you-begin-hdi.md

# Before you begin

Before you begin setting up Pentaho to connect to HDI, perform the following tasks:

1. Check the [Components Reference](https://docs.pentaho.com/install/10.2-install/components-reference) to verify that your Pentaho version supports your version of HDI.
2. Prepare your HDI instance by performing the following tasks:
   1. Configure your Azure HDInsight instance.

      View the [HDI documentation](https://docs.microsoft.com/en-us/azure/hdinsight/) if you need help.
   2. Install any required services and service client tools.
   3. Test the platform.
3. Contact your platform administrator for connection information to HDI and services that you intend to use. Some of this information may be available from the Azure manager tool or other management tools. You also need to [supply some of this information to users](https://docs.pentaho.com/install/10.2-install/use-hadoop-with-pentaho/get-started-with-hadoop-and-pdi/before-you-begin-get-started-with-hadoop-and-pdi/hadoop-connection-and-access-information-list) after you are finished.
4. Add the YARN user on the platform to the group defined by the **dfs.permissions.superusergroup** property. The **dfs.permissions.superusergroup** property is located in the `hdfs-site.xml` file on your platform.
5. [Set up Pentaho to connect to a Hadoop cluster](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster). You need to install the driver for your version of HDI.

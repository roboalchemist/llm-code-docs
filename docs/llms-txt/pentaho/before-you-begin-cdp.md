# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-cloudera-data-platform/before-you-begin-cdp.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-cloudera-data-platform/before-you-begin-cdp.md

# Before you begin

Before you begin to set up Pentaho to connect to CDP, you must perform the following tasks:

1. Check the [Components Reference](https://docs.pentaho.com/install/10.2-install/components-reference) to verify that your Pentaho version supports your version of CDP.
2. Prepare your CDP by performing the following tasks:
   1. Configure your Cloudera Data Platform.

      See [CDP's documentation](https://docs.cloudera.com/cdp-private-cloud-base/7.1.6/index.html) if you need help.
   2. Install any required services and service client tools.
   3. Test the platform.
3. Contact your platform administrator for connection information to CDP and services that you intend to use. Some of this information may be from Cloudera Manager or other management tools. You also need to [supply some of this information to users](https://docs.pentaho.com/install/10.2-install/use-hadoop-with-pentaho/get-started-with-hadoop-and-pdi/before-you-begin-get-started-with-hadoop-and-pdi/hadoop-connection-and-access-information-list) after you are finished.
4. Add the YARN user on the platform to the group defined by the **dfs.permissions.superusergroup** property. The **dfs.permissions.superusergroup** property can be found in the `hdfs-site.xml` file on your platform or in the Cloudera Manager.
5. [Set up Pentaho to connect to a Hadoop cluster](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster). You need to install the driver for your version of CDP.

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-azure-hdinsight-cp/using-oozie-shared/set-up-oozie-on-a-cluster.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-azure-hdinsight-cp/using-oozie-shared/set-up-oozie-on-a-cluster.md

# Set up Oozie on a cluster

Perform the following steps to add a PDI user to the `oozie-site.xml` file:

1. Open the `oozie-site.xml` file on the cluster.
2. Add the following lines of the code to the `oozie-site.xml` file on cluster, substituting *\<your\_pdi\_user\_name>* with the PDI user name, such as `jdoe`.

   ```xml
   <property>
   <name>oozie.service.ProxyUserService.proxyuser.*&lt;your\_pdi\_user\_name&gt;*.groups</name>
   <value>*</value>
   </property>
   <property>
   <name>oozie.service.ProxyUserService.proxyuser.*&lt;your\_pdi\_user\_name&gt;*.hosts</name>
   <value>*</value>
   </property>
   ```
3. Save and close the file.

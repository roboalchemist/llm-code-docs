# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-a-hortonworks-cluster/before-you-begin-connect-to-hdp-cluster/setup-a-secured-cluster.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-a-cloudera-cluster/before-you-begin-connect-to-cdh/setup-a-secured-cluster.md

# Set up a secured cluster

If you are connecting to a CDH cluster that is secured with Kerberos, you must also perform the following tasks.

1. Configure Kerberos security on the cluster, including the Kerberos Realm, Kerberos KDC, and Kerberos Administrative Server.
2. Configure the name, data, secondary name, job tracker, and task tracker nodes to accept remote connection requests.
3. If you have deployed CDH using an enterprise-level program, set up Kerberos for name, data, secondary name, job tracker, and task tracker nodes.
4. Add user account credentials to the Kerberos database for each Pentaho user that needs access to the Hadoop cluster.
5. Verify that an operating system user account exists on each node in your Hadoop cluster for each user you want to add to the Kerberos database. Add operating system user accounts if necessary.

   **Note:** The user account UIDs should be greater than the minimum user ID value (**min.user.id**). Usually, the minimum user ID value is set to `1000`.
6. Set up Kerberos on your Pentaho machines. For instructions, see the **Administer Pentaho Data Integration and Analytics** document.

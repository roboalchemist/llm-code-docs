# Source: https://docs.pentaho.com/pdia-admin/administer/secure-the-pentaho-system/big-data-security/kerberos-authentication-versus-secure-impersonation/how-to-enable-secure-impersonation.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/secure-the-pentaho-system/big-data-security/how-to-enable-secure-impersonation.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/big-data-security/kerberos-authentication-versus-secure-impersonation/how-to-enable-secure-impersonation.md

# How to enable secure impersonation

Here is how to enable secure impersonation and how the Pentaho Server processes that request. The mapping value `simple` in the driver configuration file turns on the secure impersonation. This value is set when you specify impersonation settings while creating a named connection. See the **Pentaho Data Integration** document for instructions on creating a named connection.

## Understanding secure impersonation

When the Pentaho Server starts, it verifies the mapping type value in the configuration file. If the value is **disabled** or **blank**, then the server does not use authentication when connecting to the cluster. The Pentaho Server cannot log onto a secured cluster if the value is set to disabled or blank. If the value is **simple**, then requests are evaluated for origination from the PDI client tool (Spoon) or from the Pentaho Server. If the request comes from a client tool, then Kerberos authentication is used; if the request comes from the Pentaho Server, then the request is evaluated to see whether the service component supports secure impersonation. If the component does not support secure impersonation, the request uses Kerberos authentication. If the component supports secure impersonation, then the request will use secure impersonation.

When impersonation is successful, the Pentaho Server log will report

```
"Everything looks good! [Hadoop User] is successfully impersonating as [Pentaho User]."
```

![Secure impersonation overview](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-07fa85ed526da61e59a2da6a784a781f2420752b%2FBig_Data_Security_Overview.png?alt=media)

**Note:** If you change the mapping type value in the configuration file, you must restart the server for it to take effect.

## Use secure impersonation with a cluster

You can implement secure impersonation when you connect to a Hadoop cluster with the PDI client, depending on the options you select. You have optional manual and advanced configurations available for secure impersonation on the Pentaho Server.

The following sections guide you through the optional manual setup and advanced configurations:

* Prerequisites
* Configuring MapReduce jobs (Windows-only)
* Connecting to a Cloudera Impala database (Cloudera-only)
* Next Steps

For an overview of secure impersonation, refer to [Setting Up Big Data Security](https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/big-data-security).

### Prerequisites

The following requirements must be met to use secure impersonation:

* The cluster must be secured with Kerberos, and the Kerberos server used by the cluster must be accessible to the Pentaho Server.
* The Pentaho computer must have Kerberos installed and configured. See [Set Up Kerberos for Pentaho](https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/big-data-security/kerberos-authentication-versus-secure-impersonation/how-to-enable-kerberos-authentication/set-up-kerberos-for-pentaho) for instructions.

**Note:** If your system has version 8 of the Java Runtime Environment (JRE) or the Java Developer's Kit (JDK) installed, you will not need to install the Kerberos client, since it is included in the Java installation. You will need to modify the Kerberos configuration file, `krb5.conf`, as specified in the [Set Up Kerberos for Pentaho](https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/big-data-security/kerberos-authentication-versus-secure-impersonation/how-to-enable-kerberos-authentication/set-up-kerberos-for-pentaho) article.

* A Pentaho driver for your Hadoop cluster must be installed and a named connection in the PDI client created. See the **Pentaho Data Integration** document for instructions.

### Configuring MapReduce jobs

If you are trying to establish secure impersonation on a Windows system, you must modify the `mapred-site.xml` file to run MapReduce jobs for secure impersonation.

Perform the following steps to modify the `mapred-site.xml` file for secure impersonation:

1. Navigate to the `<username>/.pentaho/metastore/pentaho/NamedCluster/Configs/<user-defined connection name>` directory and open the `mapred-site.xml` file with a text editor.
2. Add the following two properties to the `mapred-site.xml` file:

   ```xml
   <property>
     <name>mapreduce.app-submission.cross-platform</name>
     <value>true</value>
   </property>
   <property>
     <name>mapreduce.framework.name</name>
     <value>yarn</value>
   </property>
   ```
3. Save and close the file.

### Connecting to a Cloudera Impala database

If you are trying to establish secure impersonation with a Cloudera Hadoop cluster and you are connecting to a secure Cloudera Impala database, you must update security-specific settings on the PDI database connection.

Perform the following steps to update your connection to the secure Cloudera Impala database:

1. Download the Cloudera Impala JDBC driver for your operating system from the Cloudera web site <https://www.cloudera.com/downloads/connectors/impala/jdbc/2-6-15.html>

   **Note:** Secure impersonation with Impala is only supported with the Cloudera Impala JDBC driver. You may have to create an account with Cloudera to download the driver file.
2. Extract the `ImpalaJDBC41.jar` file from the downloaded zip file into the folder `<username>/.pentaho/metastore/pentaho/NamedCluster/Configs/cdp71/lib`. The `ImpalaJDBC41.jar` file is the only file to extract from the downloaded file.
3. Connect to a secure CDP cloud instance.

   If you have not set up a secure instance, complete the procedure for setting up Pentaho to connect to a secure cluster found in the **Install Pentaho Data Integration and Analytics** document.
4. Start the PDI Client and choose **File** > **New** > **Transformation** to add a new transformation.

   See the **Pentaho Data Integration** document for instructions on starting the PDI client.
5. Click the **View** tab, then right-click **Database Connections**and choose **New**.
6. In the **Database Connection** dialog box enter the values from the following table:

   | Field               | Value               |
   | ------------------- | ------------------- |
   | **Connection Name** | `User-defined name` |
   | **Connection Type** | Cloudera Impala     |
   | **Host Name**       | `Hostname`          |
   | **Database Name**   | default             |
   | **Port Number**     | 443                 |
7. Click **Options** in the left pane of the **Database Connection** dialog box and enter the parameter values as shown in the following table:

   | Parameter          | Value                                              |
   | ------------------ | -------------------------------------------------- |
   | **KrbHostFQDN**    | The fully qualified domain name of the Impala host |
   | **KrbServiceName** | The service principal name of the Impala server    |
   | **KrbRealm**       | The Kerberos realm used by the cluster             |
8. Click **Test** when your settings are entered.

A success message appears if everything was entered correctly.

### Next steps

When you save your changes in the repository and your Hadoop cluster is connected to the Pentaho Server, you are now ready to use secure impersonation to run your transformations and jobs from the Pentaho Server.

**Note:** Secure impersonation from the PDI client is not currently supported.

See the **Install Pentaho Data Integration and Analytics** document for instructions on any further advance configurations you may need to perform to connect your Hadoop cluster to the Pentaho Server.

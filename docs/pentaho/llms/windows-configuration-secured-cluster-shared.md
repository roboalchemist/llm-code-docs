# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-azure-hdinsight-cp/windows-configuration-secured-cluster-shared.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-azure-hdinsight-cp/windows-configuration-secured-cluster-shared.md

# Windows configuration for a secured cluster

If you are on a Windows machine, perform the following steps to edit the configuration properties:

1. Navigate to the `server/pentaho-server` directory and open the `start-pentaho.bat` file with any text editor.
2. Set the **CATALINA\_OPTS** environment variable to the location of the `krb5.conf` or `krb5.ini` file on your system, as shown in the following example:

   ```
   set "CATALINA_OPTS=%"-Djava.security.krb5.conf=C:\kerberos\krb5.conf

   ```
3. Save and close the file.

# Source: https://docs.pentaho.com/install/9.3-install/use-hadoop-with-pentaho/big-data-issues/pig-job-not-executing-after-kerberos-authentication-fails.md

# Pig job not executing after Kerberos authentication fails

Your Pig job will not execute after the Kerberos authentication fails until you restart PDI. While PDI may continue to generate new Kerberos tickets and other Hadoop components may work, Pig continues to fail until PDI is restarted.

For authentication with Pig, Pentaho uses the `UserGroupInformation` wrapper around a JAAS Subject with username and password which is used for impersonation. The `UserGroupInformation` wrapper is stored in the `KMSClientProvider` constructor. When the Kerberos ticket expires, a new `UserGroupInformation` is created, but the instance stored in the `KMSClientProvider` constructor does not update. The Pig job fails when Pig cannot obtain delegation tokens to authenticate the job at execution time.

To resolve, set the **key.provider.cache.expiry** time to a value equal to or less than the duration time of the Kerberos ticket. By default, the **key.provider.cache.expiry** time is set to a value of: 10 days

**Note:** This solution assumes you are using HortonWorks 3.0.

1. Navigate to the `hdfs-site.xml` file location.
   * In the PDI client, navigate to: `data-integration\plugins\pentaho-big-data-plugin\hadoop-configurations\hdp25`
   * For the Pentaho Server, navigate to: `pentaho-server\pentaho-solutions\system\kettle\plugins\pentaho-big-data-plugin\hadoop-configurations\hdp25`
2. Open the `hdfs-site.xml` file in a text editor.
3. Adjust the key.provider.cache.expiry value (in milliseconds) so that it is less than the duration time of the Kerberos ticket.

   **Note:** You can view the Kerberos ticket duration time in the `krb5.conf` file.

   ```xml
   <property>
   <name>dfs.client.key.provider.cache.expiry</name>
   <value>410000</value>
   </property>
   ```

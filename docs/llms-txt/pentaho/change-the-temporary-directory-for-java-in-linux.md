# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/acquire-and-install-enterprise-licenses/install-and-manage-a-local-license-server/change-the-temporary-directory-for-java-in-linux.md

# Change the temporary directory for Java in Linux

The local license server must have access to Java's temporary directory in Linux. If your deployed local license server does not have access to Java's temporary directory because your admin restricted access to that directory, you can create and use a new temporary directory for Java.

Complete the following steps to create a new temporary directory for Java and configure the license server system service to use the new temporary directory.

1. On the machine where you deployed the local license server, create a new temporary directory for Java by running the following commands with the directory name that you want to use specified as the *temp\_directory\_name* variable:

   ```
   sudo mkdir /<temp_directory_name>
   sudo chmod 777 /<temp_directory_name>
   sudo chown root:root /<temp_directory_name>
   ```
2. Stop the license server system service by running the following command:

   `sudo systemctl stop flexnetls-pentaho`
3. To edit the license server configuration file, open the file in the Vi text editor by running the following command:

   `sudo vi /etc/systemd/system/flexnetls-pentaho.service.d/flexnetls.conf`
4. In the license server configuration file, add the location to the new temporary directory by appending the following flag to the end of the JVMOPTS declaration:

   `-Djava.io.tmpdir=<full_path_to_temp_directory>`

   For example, the updated JVMOPTS declaration looks similar to the following code: `Environment="JVMOPTS=-server -Xms1750m -Xmx1750m -XX:CompressedClassSpaceSize=64m -XX:MetaspaceSize=256m -XX:MaxDirectMemorySize=256m -XX:+UseG1GC -XX:MaxGCPauseMillis=100 -XX:+DisableExplicitGC -XX:+UseStringDeduplication -XX:G1HeapWastePercent=10 -XX:InitiatingHeapOccupancyPercent=75 -XX:+ExplicitGCInvokesConcurrent -XX:SurvivorRatio=4 -XX:+IgnoreUnrecognizedVMOptions --add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.lang.invoke=ALL-UNNAMED -XX:-OmitStackTraceInFastThrow -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/var/opt/flexnetls/pentaho -Djava.security.egd=file:/dev/./urandom -Djava.io.tmpdir=/<full_path_to_temp_directory>"`
5. Save and close the license server configuration file.
6. Verify that the SELinux mode is set to permissive.

   If the SELinux mode is not set to permissive, see the Red Hat documentation, [Change SELinux to permissive mode](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/using_selinux/changing-selinux-states-and-modes_using-selinux#changing-to-permissive-mode_changing-selinux-states-and-modes).
7. Reload the license server system service by running the following command:

   `sudo systemctl daemon-reload`
8. Start the license server system service by running the following command:

   `sudo systemctl start flexnetls-pentaho`

The license server system service is configured to use the new temporary directory that you created for Java.

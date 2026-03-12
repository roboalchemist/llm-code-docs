# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/use-password-encryption-with-pentaho/using-encrypted-passwords-with-pentaho-products/using-encrypted-passwords-with-pad.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/use-password-encryption-with-pentaho/using-encrypted-passwords-with-pentaho-products/using-encrypted-passwords-with-pad.md

# Encrypted passwords with the Pentaho Aggregation Designer

To use encrypted passwords with Pentaho Aggregation Designer, you must first centralize your passwords in a `jndi.properties` file.

Perform the following steps to use an encrypted password with the Pentaho Aggregation Designer.

1. Stop the server.

   For instructions on stopping the server, see [Stop and start the Pentaho Server and repository](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/stop-and-start-the-pentaho-server-and-repository).
2. Create a `jndi.properties` file to set the default properties using the following code:

   ```
   java.naming.factory.initial=org.osjava.sj.SimpleContextFactory
   org.osjava.sj.root=file://C:/Users/<*username*>/.pentaho/simple-jndi
   org.osjava.sj.delimiter=/

   ```
3. Save the `jndi.properties` file in the `design-tools/aggregation-designer/lib` directory and close the file.
4. In the user’s home directory, navigate to the `.pentaho/simple-jndi` directory and open the `default.properties` file with any text editor.
   1. If you do not have a `default.properties` file in the `<user_HOME_folder>.pentaho/simple-jndi` directory, then create a `simple-jndi` directory in the `design-tools/aggregation-designer` directory and create a `default.properties` file in that directory.
   2. Change the following `jndi.properties` file in the `design-tools/aggregation-designer/lib` directory to indicate the new location of the `default.properties` file as shown in the following example:

      ```
      org.osjava.sj.root=file://<*install directory*>/design-tools/aggregation-designer/simple-jndi
      ```
5. Replace the **password** value in every property in the `default.properties` file with the encrypted password.

   **Note:** If you are using a remote repository, you must change **localhost** to the correct IP address of the remote repository.
6. Save and close the file.
7. Restart the server and verify that all passwords are now using encrypted values.

After you have configured an application to use encrypted passwords, all logins with the Pentaho application will use the encrypted passwords.

Connect to any databases that were edited to ensure all changes are operating correctly.

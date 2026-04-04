# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/use-password-encryption-with-pentaho/using-encrypted-passwords-with-pentaho-products/using-encrypted-passwords-with-pme.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/use-password-encryption-with-pentaho/using-encrypted-passwords-with-pentaho-products/using-encrypted-passwords-with-pme.md

# Encrypted passwords with the Pentaho Metadata Editor

The Pentaho Metadata Editor (PME) stores a password in the `default.properties` file of the JNDI connection. For information about setting up a JNDI connection, see the article [Define JNDI connections for Report Designer and Metadata Editor](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/specify-data-connections-for-ba-design-tools/jdbc-database-connections/define-jndi-connections-for-report-designer-and-metadata-editor).

Perform the following steps to use an encrypted password with the PME:

1. Stop the server.

   For instructions on stopping the server, see [Stop and start the Pentaho Server and repository](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/stop-and-start-the-pentaho-server-and-repository).
2. In the user’s home directory, navigate to the `.pentaho/simple-jndi` directory.
3. Open the `default.properties` file with any text editor.

   **Note:** If you do not have a `default.properties` file in a `<*user\_HOME\_folder*>.pentaho/simple-jndi` directory, you must create one.
4. Replace the **password** value in every property in the file with the encrypted password.

   **Note:** If you are using a remote repository, you must change **localhost** to the correct IP address of the remote repository.
5. Save and close the file.
6. Restart the server and verify that all passwords are now using encrypted values.

After you have configured an application to use encrypted passwords, all logins with the Pentaho application will use the encrypted passwords.

Connect to any databases that were edited to ensure all changes are operating correctly.

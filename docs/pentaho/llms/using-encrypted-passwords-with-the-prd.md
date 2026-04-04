# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/use-password-encryption-with-pentaho/using-encrypted-passwords-with-pentaho-products/using-encrypted-passwords-with-the-prd.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/use-password-encryption-with-pentaho/using-encrypted-passwords-with-pentaho-products/using-encrypted-passwords-with-the-prd.md

# Encrypted passwords with the Pentaho Report Designer

The Pentaho Report Designer (PRD) stores a password in the `default.properties` file of the JNDI connection. For information about setting up a JNDI connection, see the article [Define JNDI connections for Report Designer and Metadata Editor](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/specify-data-connections-for-ba-design-tools/jdbc-database-connections/define-jndi-connections-for-report-designer-and-metadata-editor).

Perform the following steps to use an encrypted password with the PRD:

1. Stop the server.

   For instructions on stopping the server, see [Stop and start the Pentaho Server and repository](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/stop-and-start-the-pentaho-server-and-repository).
2. Navigate to the `design-tools/report-designer/configuration-template/simple-jndi` directory.
3. Open the `default.properties` file with any text editor.
4. Replace the **password** value in every property in the file with the encrypted password.

   **Note:** If you are using a remote repository, adjust the **localhost** address to the correct IP. Also, make sure you use the encrypted password for all occurrences of the password.
5. Save and close the file.
6. Copy the `default.properties` file from the `design-tools/report-designer/configuration-template/simple-jndi` directory to the `.pentaho/simple-jndi` directory in the user’s home directory and replace the existing `default.properties` file.

   **Note:** If there is no existing `<*user\_HOME\_folder*>.pentaho/simple-jndi` directory, create the directory and copy the `default.properties` file into the directory that you create.
7. Restart the server and verify that all passwords are now using encrypted values.

After you have configured an application to use encrypted passwords, all logins with the Pentaho application will use the encrypted passwords.

Connect to any databases that were edited to ensure all changes are operating correctly.

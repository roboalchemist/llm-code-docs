# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/use-password-encryption-with-pentaho/using-encrypted-passwords-with-pentaho-products/using-encrypted-passwords-with-puc.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/use-password-encryption-with-pentaho/using-encrypted-passwords-with-pentaho-products/using-encrypted-passwords-with-puc.md

# Encrypted passwords with the Pentaho User Console

Perform the following steps to use an encrypted password with the Pentaho User Console (PUC).

1. Stop the server.

   For instructions on stopping the server, see [Stop and start the Pentaho Server and repository](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/stop-and-start-the-pentaho-server-and-repository).
2. Navigate to the `server/pentaho-server/tomcat/webapps/pentaho/META-INF` directory.
3. Open the `context.xml` file in any text editor.
4. Replace the **password** value in every **Resource** element with the encrypted password.
5. Save and close the file.
6. Restart the server and verify that all passwords are now using encrypted values.

After you have configured an application to use encrypted passwords, all logins with the Pentaho application will use the encrypted passwords.

Connect to any databases that were edited to ensure all changes are operating correctly.

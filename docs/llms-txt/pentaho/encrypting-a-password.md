# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/use-password-encryption-with-pentaho/encrypting-a-password.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/use-password-encryption-with-pentaho/encrypting-a-password.md

# Encrypting a password

Perform the following steps on the machine with the Pentaho Server to create an encrypted password.

1. Stop the server.

   For instructions on stopping the server, see [Stop and start the Pentaho Server and repository](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/stop-and-start-the-pentaho-server-and-repository).
2. At the command line, navigate to the `server/pentaho-server` directory.
3. Run the `encr.bat` command for Windows or the `encr.sh` command for Linux as shown in the example below:

   ```
   encr -kettle <password>
   ```

   An encrypted password is created and displays in the console window.

   **Note:** You must have a JRE or JDK installed to run this command.
4. Restart the server and verify that the password is now using encrypted values.

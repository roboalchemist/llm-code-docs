# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/define-data-connections/enter-database-connection-information/connect-to-snowflake-using-strong-authentication.md

# Connect to Snowflake using strong authentication

If you are defining a data connection to Pentaho Data Integration and Analytics from a Snowflake data warehouse in the cloud, you can improve connection security by applying strong authentication.

You can apply strong authentication to your defined Pentaho data connection from Snowflake through a key pair. Perform the following steps to configure key pair strong authentication for your Snowflake data connection:

1. After [entering the information for your Snowflake data connection](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/define-data-connections/enter-database-connection-information) in the **General** tab of the Database Connection dialog box, select the **Options** tab.
2. Set the key pair parameters as indicated in the following table:

   | Parameter              | Value                                                                                                                   |
   | ---------------------- | ----------------------------------------------------------------------------------------------------------------------- |
   | `authenticator`        | `snowflake_jwt`                                                                                                         |
   | `private_key_file`     | Specify the name of the private key file you use in your environment. For example, `/rsa_key.p8`                        |
   | `private_key_file_pwd` | Specify the password for accessing the private key file you use in your environment. For example, `PentahoSnowFlake123` |

   See <https://docs.snowflake.com/en/developer-guide/jdbc/jdbc-configure#private-key-file-name-and-password-as-connection-properties> for details on the private key file and its password.
3. Click **Test** to verify your connection. A success message appears if the connection is established.
4. Click **OK** to close the connection test dialog box.
5. To save the connection, click **OK** to close the Database Connection dialog box.

You have applied key pair authentication to your defined data connection between Pentaho and Snowflake.

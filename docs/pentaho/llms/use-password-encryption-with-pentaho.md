# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/use-password-encryption-with-pentaho.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/use-password-encryption-with-pentaho.md

# Use password encryption with Pentaho

Strengthen security by using encrypted passwords for Pentaho applications.

For IT administrators, who have permissions to modify files on the server and the permission to stop and start the server, perform these tasks when you want to enhance your company's security by encrypting the passwords that are currently stored as plain text in configuration files, for example, if you want to meet specific server security levels for regulatory compliance.

As a best practice, stop the server before modifying configuration files, then start the server when finished. After you have configured a Pentaho product to use encrypted passwords, all logins with the Pentaho product will use the encrypted passwords. Connect to any databases that were edited to ensure all changes are correct.

Encrypted passwords are supported for the following applications:

* [Pentaho Data Integration](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/use-password-encryption-with-pentaho/using-encrypted-passwords-with-pentaho-products/using-encrypted-passwords-with-pdi)
* [Pentaho User Console (PUC)](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/use-password-encryption-with-pentaho/using-encrypted-passwords-with-pentaho-products/using-encrypted-passwords-with-puc)
* [PUC email](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/use-password-encryption-with-pentaho/using-encrypted-passwords-with-pentaho-products/using-encrypted-passwords-with-puc-email)
* [Pentaho Aggregate Designer](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/use-password-encryption-with-pentaho/using-encrypted-passwords-with-pentaho-products/using-encrypted-passwords-with-pad)
* [Pentaho Metadata Editor](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/use-password-encryption-with-pentaho/using-encrypted-passwords-with-pentaho-products/using-encrypted-passwords-with-pme)
* [Pentaho Report Designer](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/use-password-encryption-with-pentaho/using-encrypted-passwords-with-pentaho-products/using-encrypted-passwords-with-the-prd)

You can also use encrypted passwords with JDBC security. See the **Administer Pentaho Data Integration and Analytics** document for instructions on switching to JDBC security.

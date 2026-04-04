# Source: https://docs.pentaho.com/pdia-admin/administer/secure-the-pentaho-system/user-security/advanced-security-providers/aes-security.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/secure-the-pentaho-system/user-security/advanced-security-providers/aes-security.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/user-security/advanced-security-providers/aes-security.md

# AES security

As a default security, Kettle obfuscation is applied to your passwords. You can increase password security by changing it to use an Advanced Encryption Standard (AES) implementation that can be applied to all passwords, including those in database connections, transformation steps, and job entries.

You can choose from two types of AES security implementations: Electronic Code Book (ECB) and Cipher Block Chaining (CBC). See <https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation> to learn more about these AES implementations.

**Note:** If you switch password security methods, all existing passwords will also use the new method. You may also have to update passwords and re-save Pentaho Data Integration (PDI) transformations (KTRs) and jobs (KJBs) to enforce any AES implementation changes.

## Create an AES key file

You need to establish an encryption key for any AES implementation you might use.

Perform the following steps to specify your encryption key by creating a key text file to contain it:

1. Create a text file that contains a key phrase, such as *!@ExampleKey#123*.

   Leading and trailing white spaces are ignored. The encryption key in the key file must be 16 bytes in length, `!@ExampleKey#123` or `1234567891234567` for example.
2. Save and close the file.

   **Note:** Safeguard the key file. If the key file becomes corrupted or lost, passwords cannot be decrypted.

You must specify the path to your key file in the `kettle.properties` file.

## Specify AES variables in the properties file

Perform the following steps to set **AES**-specific variables in the `kettle.properties` file for the PDI client (Spoon), the Pentaho Server, and any clusters.

1. Open the `kettle.properties` file for the PDI client (Spoon). By default, the `kettle.properties` file is in the user’s home directory.
2. Add the following variables and values.

| Variable                                               | Description                                                            | Value                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------ | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **KETTLE\_PASSWORD\_ENCODER\_PLUGIN** (Required)       | Indicates the type of plugin used.                                     | Use *AES* for either the ECB or CBC encryption implementation. Specifying *AES* defaults to the ECB encryption implementation.**Note:** If you are changing the plugin type from *AES* to *AES2*, you must reset your connection passwords and save the updated transformations (KTRs) and jobs (KJBs).               |
| **KETTLE\_AES\_KEY\_FILE** (Required)                  | Indicates the path to the key file.                                    | Specify the path to the key file. Relative paths are resolved against the Kettle working directory, NOT the location of the `kettle.properties` file. `c:/securearea/keyfile.txt` for example.                                                                                                                        |
| **KETTLE\_AES\_KETTLE\_PASSWORD\_HANDLING** (Optional) | Maintain backwards compatibility by setting this variable to `Decode`. | Use `DECODE`. If this variable is not set, Kettle encoded passwords are not decoded. If this variable is set to anything other than `DECODE`, a runtime exception will be thrown with a message similar to the following example: A Kettle encoded password was used: `'Encrypted 2be98afc86aa79f8da510a171da9fa6d4'` |

3\. Save and close the \`kettle.properties\` file.

4. Stop and restart the PDI client (Spoon).
5. Repeat this process for other `kettle.properties` files on the Pentaho Server and cluster nodes.

You must specify the AES implementation used by updating the `kettle-password-encoder-plugins.xml` file.

## Configure Pentaho for AES encryption

You must configure Pentaho Data Integration (PDI) and Tomcat for AES encryption, and specify which AES implementation to use.

Perform the following steps to configure PDI or Tomcat:

1. Navigate to the `kettle-password-encoder-plugins.xml` file in one of the following directories and open it with any text editor:
   * PDI: `data-integration/classes`
   * Tomcat: `server/pentaho-server/tomcat/webapps/pentaho/WEB-INF/classes`
2. Add or uncomment the following code depending on which AES implementation (ECB or CBC) you want to use:

   * For ECB:

     ```xml
     <password-encoder-plugin id="AES2">
          <description>AES Password Encoder</description>
          <classname>org.pentaho.support.encryption.AESTwoWayPasswordEncoder</classname>
          <default-encoder>true</default-encoder>
          <mode>ECB</mode>
     </password-encoder-plugin>

     ```
   * For CBC:

     ```xml
     <password-encoder-plugin id="AES2">
          <description>AES Password Encoder</description>
          <classname>org.pentaho.support.encryption.AESTwoWayPasswordEncoder</classname>
          <default-encoder>true</default-encoder>
          <mode>CBC</mode>
     </password-encoder-plugin>

     ```

   **Note:** You can only have one `default-encoder` set to true at a time within the `kettle-password-encoder-plugins.xml` file. ECB is used as the default implementation if the `<mode>` element is not specified.
3. Save and close the file.
4. Repeat this proeess for the other `kettle-password-encoder-plugins.xml` file.

You can verify AES encryption is working with either a batch file command or through the PDI client.

## Use a batch file command to verify encryption

Perform the following steps if you want to use the `Encr.bat` command to make sure your encryption implementation is working as expected:

1. Open a terminal window to a command line.
2. Navigate to one of the following directories:
   * PDI: `data-integration`
   * Tomcat: `server/pentaho-server`
3. Run one of the following commands depending on the type of encoder you set:
   * AES2: `encr.bat -aes2 password`
   * AES: `encr.bat -aes password`
   * Kettle: `encr.bat -kettle password`
   * Default: `encr.bat password`

For AES2 encryption, the first character of the encrypted password represents the encryption implementation used. The first character is a `1` for the ECB encryption implementation (`AES2 1RGySKmVU6JWiijkti3Vd8w==` for example). The first character is a `2` for the CBC encryption implementation (`AES2 2UP+e9xqhL0bkSGWgHokk6xpdhAkO1X8OBxNeGu4qdGI=` for example).

## Use the PDI client to verify encryption

Perform the following steps if you want to use the PDI client to make sure your encryption implementation is working as expected:

1. Start the PDI client (Spoon).
2. Create a blank transformation.
3. Add a database connection that requires a password.

   See the **Install Pentaho Data Integration and Analytics** document for instructions on defining a database connection.
4. Save, then close the transformation.
5. Use a text editor to open the transformation you just saved, then search for the name of the connection you created.
6. Examine the password.

   If the password is preceded by the letters *AES*, or *AES2*, the encryption was applied correctly.
7. Close the transformation.

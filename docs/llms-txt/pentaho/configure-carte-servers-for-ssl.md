# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/set-up-a-carte-cluster/carte-cluster-configuration/configure-carte-servers-for-ssl.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/set-up-a-carte-cluster/carte-cluster-configuration/configure-carte-servers-for-ssl.md

# Configure Carte servers for SSL

Carte SSL uses the JKS format for keystores, which is the default format created by the keytool command-line utility. It is a best practice to locate the keystore file in a directory that has restricted access. Carte runs on a Jetty server. For more information on how to use SSL certificates in the Jetty server, read <https://wiki.eclipse.org/Jetty/Howto/Configure_SSL>.

To configure Carte servers to use SSL, complete these steps:

1. Stop the Carte server if it is running.
2. Open the `carte-master-config.xml` configuration file.
3. Add the *keyStore*, *keyStorePassword* and optionally, the *keyPassword* values between **\<sslConfig>** **\</sslConfig>** tags in the master server configuration section. If you do not include the *keyStore* and *keyStorePassword* values in the file, Carte will not start. Here is an example of how to add the values. Adjust the values to match your environment.

   **Note:** You can use the encr tool, which is in the `data-integration` directory to generate obfuscated passwords. To use the tool, open a command prompt or shell tool and type `encr.bat -carte <password>`. (Use `encr.sh` if you are using Linux.) You can then paste the obfuscated value into the file instead of the clear-text password.

   ```xml
   <slave_config>
   <!-- on a master server, the slaveserver node contains information about this Carte instance -->
       <slaveserver>
           <name>Master</name>
           <hostname>yourhostname</hostname>
           <port>9001</port>
           <username>cluster</username>
           <password>cluster</password>
           <master>Y</master>
           <sslConfig/>
               <keyStore>D:\KEY_STORE\Pentaho</keyStore>
               <keyStorePassword>OBF:1x8g1toc1u301z0f1u2a1toi1x8e</keyStorePassword>
               <keyPassword>OBF:1iun1i9a1lfk1w261w1c1lby1i6o1irz</keyPassword>
           </sslConfig>
       </slaveserver>
   </slave_config>
   ```

   | Parameter        | Description                                                                                                           | Required |
   | ---------------- | --------------------------------------------------------------------------------------------------------------------- | -------- |
   | keyStore         | Path to the keystore file.                                                                                            | Yes      |
   | keyStorePassword | Password for the keystore.                                                                                            | Yes      |
   | keyPassword      | Password for the key. If the keyStorePassword and keyPassword are the same, omit the keyPassword parameter from file. | No       |
4. Save and close the `carte-master-config.xml` file.
5. Open the `carte-slave-config.xml` file for the slave servers and add the same values.
6. When finished save and close the `carte-slave-config.xml` file.
7. Start the Carte server.

   A message like the following appears in the console.

   ```
   2015/02/17 11:23:54 - Carte - Using SSL mode.
   ```
8. To access Carte, type the following in a browser, substituting \<host> and \<port> for valid values that are in your environment:

   ```
   https://<host>:<port>/
   ```

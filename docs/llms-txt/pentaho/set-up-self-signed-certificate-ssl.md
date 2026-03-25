# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/acquire-and-install-enterprise-licenses/install-and-manage-a-local-license-server/set-up-self-signed-certificate-ssl.md

# Set up Self-Signed Certificate (SSL)

You can apply SSL to the server configuration using the following procedure:

Port 1443 must be open for communication with the local license server.

1. Navigate to the following folder:

   ```
   cd /usr/lib/jvm/<*java\_installation\_folder*>/lib/security
   ```

   Example: `/usr/lib/jvm/java-1.11.0-openjdk-amd64/lib/security`
2. Generate the self-signed SSL certificate by running the following command:

   ```
   sudo keytool -genkey -keyalg RSA -alias selfsigned -keystore keystore.jks -storepass changeit -validity 3600 -ext san=ip:<*ip\_address*>,ip:<*local\_host*>
   ```
3. Export the generated certificate to file using the following command:

   ```
   sudo keytool -export -alias selfsigned -keystore keystore.jks -rfc -file server_cert.certs
   ```
4. Import the file into the keystore using the following command:

   ```
   sudo keytool -import -trustcacerts -keystore /usr/lib/jvm/java-1.11.0-openjdk-amd64/lib/security/cacerts -storepass changeit -alias selfsigned -file server_cert.cert
   ```
5. Update `local-setting.xml` as follows:

   ```
   # HTTPS server mode
   https-in:
     # Set to true to enable
     enabled: false
     # HTTPS listening port
     port: 1443
     # Path to keystore
     keystore-path: <path-to-your-keystore>
     # Keystore password. You can obfuscate this with java -jar flexnetls.jar -password <your-password>
     keystore-password: changeit

     # Choice of TLS cipher suites. One of MODERN, COMPATIBLE or WEAK.
     tlsCipherSuites: COMPATIBLE

   # HTTPS client mode. You generally don't need to specify this, unless you have an in-house CA chain.
   https-out:
     # Set to true to enable
     enabled: false
     # Path to truststore containing server certificate.
     truststore-path: <path-to-your-truststore>
     # Truststore password. You can obfuscate this with java -jar flexnetls.jar -password <your-password>
     truststore-password: changeit
     # Switch off if you're having host validation problems (not recommended)
     host-verify: true
     # Set to true if you're using self-signed certificates (not recommended)
     self-signed: false
   ```

SSL is now configured on your server.

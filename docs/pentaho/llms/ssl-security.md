# Source: https://docs.pentaho.com/pdia-admin/administer/secure-the-pentaho-system/user-security/advanced-security-providers/ssl-security.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/secure-the-pentaho-system/user-security/advanced-security-providers/ssl-security.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/user-security/advanced-security-providers/ssl-security.md

# SSL Security

This section contains instructions and guidance for enhancing the security of the Pentaho Server and User Console on an application server level via Secure Sockets Layer (SSL). SSL provides verification of server identity and encryption of data between clients and the Pentaho Server.

## Configure SSL (HTTPS) in the Pentaho User Console and Pentaho Server

By default, the Pentaho Server and User Console are configured to communicate over HTTP. To switch to HTTPS, follow the instructions below that apply to your scenario.

### Enable SSL in the Pentaho Server

{% tabs %}
{% tab title="Enable SSL with certificate authority" %}
If you already have an SSL certificate through a certificate authority such as Thawte or Verisign, you need to configure your application server to use the certificate. It can then be used by the Pentaho Server. Apache provides documentation for configuring Tomcat for CA-signed certificates: <http://tomcat.apache.org/tomcat-8.5-doc/ssl-howto.html>. Just follow those procedures, and skip the sections below that deal with self-signed SSL certificates.

After the application server is configured to use your certificate, you must modify the base URL tokens for both the Pentaho Server and the User Console. Make sure you follow the directions for changing the Pentaho Server Base URL. Without executing those changes, your server will not work over HTTPS.
{% endtab %}

{% tab title="Enable SSL with self-signed certificate" %}
This process explains how to enable SSL in the Pentaho Server with a self-signed certificate. These steps do not show how to generate a self-signed certificate, or how to configure Tomcat to use it. For more information on SSL certificates in Tomcat, consult [the Tomcat documentation](http://tomcat.apache.org/tomcat-8.5-doc/ssl-howto.html), beginning with the [Quick Start](http://tomcat.apache.org/tomcat-8.5-doc/ssl-howto.html#Quick_Start) section. This procedure assumes that an SSL certificate is generated and Tomcat is configured to use it.

The following instructions explain how to complete the trust relationship between the Pentaho Server (when it is configured for SSL) and the User Console:

1. Change to the home directory of the user account that starts the Pentaho Server and User Console processes or services:

   ```

   cd ~

   ```

   If you installed the default settings for Pentaho, this directory will be: `/home/pentaho/`
2. Execute the following command, changing the storepass (`pass` in the example) and keypass (`pass2` in the example) accordingly:

   ```

   keytool -export -alias tomcat -file tomcat.cer -storepass pass -keypass pass2 -keystore .keystore

   ```
3. Change to the `$PENTAHO_JAVA_HOME/jre/lib/security/` directory:

   ```

   cd $PENTAHO_JAVA_HOME/jre/lib/security/

   ```

   The **PENTAHO\_JAVA\_HOME** variable was established during your production installation procedure. If you are on Windows, environment variables are surrounded by percent signs, as in: `cd %PENTAHO_JAVA_HOME%\jre\lib\security\`. If you get an error about this path not being valid, then use **JAVA\_HOME** instead of **PENTAHO\_JAVA\_HOME**.
4. Execute the following command, changing the alias (`tomcat` in the example), the file path to the certificate (the current user's home directory in the example), and the storepass (`pass` in the example) accordingly:

   ```

   keytool -import -alias tomcat -file ~/tomcat.cer -keystore cacerts -storepass pass

   ```

   **Note:** If the path to your certificate involves spaces, you must either escape the spaces (on Linux or Unix), or put double quotes around the path (on Windows) in order for the command to work properly.
5. Execute the following command and make note of the MD5 sum for the Tomcat entry:

   ```

   keytool -list -keystore cacerts

   ```
6. Change back to the home directory of the user account that starts the Pentaho Server and User Console, and run this command:

   ```

   keytool -list -keystore .keystore

   ```
7. Compare the Tomcat entry's MD5 sum to the one you generated previously and ensure that they match. If these sums do not match, you've made a mistake someplace in the certificate trust process. Go through the steps again and ensure that you're working with the right user accounts and directories.

The Pentaho Server is now configured to allow access via SSL.
{% endtab %}
{% endtabs %}

### Change the Pentaho Server fully qualified URL

If you switch from HTTP to HTTPS, you must also change the Pentaho Server's tokenized fully qualified URL value to accommodate for the new port number.

Perform the following steps to change the fully qualified URL.

1. Stop the Pentaho Server if it is currently running.
2. Navigate to the `pentaho/server/pentaho-server/pentaho-solutions/system` directory.
3. Open the `server.properties` file with any text editor.
4. Locate the following element and modify the port number to match your SSL-enabled port number:

   `fully-qualified-server-url=http://localhost:8080/pentaho/`
5. Save and close the file.
6. Start the Pentaho Server and make sure that it is available through HTTPS on the specified port.

The Pentaho Server is now configured to allow access via SSL to communicate on an SSL-aware port.

## Use the Apache web server (HTTPd) for socket handling

Tomcat's socket handling abilities are not quite as robust as Apache HTTPd's socket handling, especially when it comes to system error handling. Tomcat performs all its socket handling through the Java VM. Since Java is designed to be cross-platform, it lacks some system-specific optimizations, such as socket optimization. In situations where the Pentaho Server is hit with a large number of dropped connections, invalid packets, or invalid requests from invalid IP addresses, HTTPd would do a much better job of dropping these error conditions than Tomcat. Therefore, you can improve Pentaho Server security by fronting Tomcat with HTTPd. A side-effect of this configuration is increased performance when delivering static content from the Pentaho Server.

Perform the following steps to configure the Apache HTTPd Web server to handle delivery of static content and facilitation of socket connections:

1. Install Apache 2.2.x, with SSL support, through your operating system's preferred installation method.

   For most people, this will be through a package manager. It's also perfectly valid to download and install the reference implementation from <http://www.apache.org>. It is possible to use Apache 1.3, but you will have to modify the instructions on your own from this point onward.
2. If the Apache server has started as a consequence of installing, stop the Apache server or service.
3. Retrieve or create your SSL keys.

   If you do not know how to generate self-signed certificates, refer to the OpenSSL documentation. Most production environments have SSL certificates issued by a certificate authority such as Thawte or Verisign.
4. Check to see if you already have the Tomcat Connector installed on your system.

   You can generally accomplish this by searching your filesystem for `mod_jk`, though you can also search your `http.conf` file for`mod_jk`. If it is present, then you only need to be concerned with the Apache HTTPd configuration details and can skip this step. If it is not there, then the Tomcat Connector module needs to be installed. If you are using Linux or BSD, use your package manager or the Ports system to install `mod_jk`. For all other platforms, visit the <http://www.apache.org/dist/tomcat/tomcat-connectors/jk/binaries/>, then click on the directory for your operating system. The module will be either an SO file (for Linux, BSD, OS X, and Solaris) or DLL file (for Windows). Save it to your Apache modules directory, which is generally `C:\Program Files\Apache Group\Apache2\modules\` on Windows, and `/usr/lib/apache2/modules/` on Unix-like operating systems, though this can vary depending on your Apache configuration.
5. Edit your `httpd.conf` file with a text editor and add the following text to the end of the file, modifying the paths and filenames as instructed in the comments:

   **Note:** Some operating systems use modular HTTPd configuration files and have unique methods of including each separate piece into one central file. Ensure that you are not accidentally interfering with an auto-generated `mod_jk` configuration before you continue. In many cases, some of the configuration example below will have to be cut out (such as the `LoadModule` statement). In some cases (such as with Ubuntu Linux), `httpd.conf` may be completely empty, in which case you should still be able to add the below lines to it. Replace `example.com` with your hostname or domain name.

   ```
   # Load mod_jk module
   # Update this path to match your mod_jk location; Windows users should change the .so to .dll
   LoadModule    jk_module  /usr/lib/apache/modules/mod_jk.so
   # Where to find workers.properties
   # Update this path to match your conf directory location
   JkWorkersFile /etc/httpd/conf/workers.properties
   # Should mod_jk send SSL information to Tomcat (default is On)
   JkExtractSSL On
   # What is the indicator for SSL (default is HTTPS)
   JkHTTPSIndicator HTTPS
   # What is the indicator for SSL session (default is SSL_SESSION_ID)
   JkSESSIONIndicator SSL_SESSION_ID
   # What is the indicator for client SSL cipher suit (default is SSL_CIPHER)
   JkCIPHERIndicator SSL_CIPHER
   # What is the indicator for the client SSL certificated (default is SSL_CLIENT_CERT)
   JkCERTSIndicator SSL_CLIENT_CERT
   # Where to put jk shared memory
   # Update this path to match your local state directory or logs directory
   JkShmFile     /var/log/httpd/mod_jk.shm
   # Where to put jk logs
   # Update this path to match your logs directory location (put mod_jk.log next to access_log)
   JkLogFile     /var/log/httpd/mod_jk.log
   # Set the jk log level [debug/error/info]
   JkLogLevel    info
   # Select the timestamp log format
   JkLogStampFormat "[%a %b %d %H:%M:%S %Y] "
   # Send everything for context /examples to worker named worker1 (ajp13)
   # JkOptions indicates to send SSK KEY SIZE
   JkOptions +ForwardKeySize +ForwardURICompat -ForwardDirectories
   # JkRequestLogFormat
   JkRequestLogFormat "%w %V %T"
   # Mount your applications
   JkMount /pentaho/* tomcat_pentaho
   # Add shared memory.
   # This directive is present with 1.2.10 and
   # later versions of mod_jk, and is needed for
   # for load balancing to work properly
   JkShmFile logs/jk.shm
   <VirtualHost example.com
   ServerName example.com
   JkMount /pentaho default
   JkMount /pentaho/* default
   JkMount /sw-style default
   JkMount /sw-style/* default
   JkMount /pentaho-style default
   JkMount /pentaho-style/* default
   </VirtualHost>
   ```
6. In your Apache configuration, ensure that SSL is enabled by uncommenting or adding and modifying the following lines:

   ```
   LoadModule ssl_module modules/mod_ssl.so
   Include conf/extra/httpd-ssl.conf
   ```
7. Save and close the file, then edit `/conf/extra/httpd-ssl.conf` and properly define the locations for your SSL certificate and key:

   ```
   SSLCertificateFile "conf/ssl/mycert.cert"
   SSLCertificateKeyFile "conf/ssl/mycert.key"
   ```
8. Ensure that your SSL engine options contain these entries:

   ```
   SSLOptions +StdEnvVars +ExportCertData
   ```
9. Add these lines to the end of the `VirtualHost` section:

   ```
   JkMount /pentaho default
   JkMount /pentaho/* default
   JkMount /sw-style default
   JkMount /sw-style/* default
   JkMount /pentaho-style default
   JkMount /pentaho-style/* default
   ```
10. Save and close the file, then create a `workers.properties` file in your Apache `conf` directory.

    If it already exists, merge it with the example configuration in the next step.
11. Copy the following text into the new `workers.properties` file, changing the location of Tomcat and Java, and the port numbers and IP addresses to match your configuration:

    ```
    workers.tomcat_home=/home/pentaho/pentaho/server/pentaho-server/tomcat/
    workers.java_home=/home/pentaho/pentaho/java/
    worker.list=tomcat_pentaho
    worker.tomcat_pentaho.type=ajp13
    ```

Apache HTTPd is now configured to securely and efficiently handle static content for Tomcat. You should now start Tomcat and HTTPd, then navigate to your domain name or hostname and verify that you can access the PentahoWeb application.

## Change the administrator role

The default administrator role in the Pentaho Server is Admin. If you need to give this privilege level to a different role name, follow these instructions:

**Note:** Role names are case sensitive, so take special care when typing in the new role name.

1. Open the `/pentaho/server/pentaho-server/pentaho-solutions/system/pentaho.xml` file with a text editor.
2. Find the `<acl-voter>` element, and replace its `<admin-role>` property with the new administrator role.

   For example, as `NewAdmin` is used in this sample procedure:

   ```
   <admin-role>NewAdmin</admin-role>
   ```
3. Find the `<acl-publisher>` element, and appropriately replace all instances of `Admin` in the properties inside of the `<default-acls>` and `<overrides>` elements as shown in the following example:

   ```
   <acl-entry role="NewAdmin" acl="ADMIN_ALL" />
   ```
4. Save the file, then open `applicationContext-spring-security.xml`.
5. Find the `filterInvocationInterceptor` bean, and modify its `objectDefinitionSource` property accordingly.

   You may need to consult the [Spring Security documentation](http://projects.spring.io/spring-security/) to complete this step:

   ```xml
   <property name="objectDefinitionSource">
       <value>
           <[
           CONVERT_URL_TO_LOWERCASE_BEFORE_COMPARISON
           ...
           \A/admin.*\Z=NewAdmin
           ...
           ]>
       </value>
   </property>
   ```

You have successfully changed the administrator role.

# Source: https://docs.pentaho.com/pdia-admin/administer/secure-the-pentaho-system/user-security/pentaho-server-security/pass-authentication-credentials-in-url-parameters.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/secure-the-pentaho-system/user-security/pentaho-server-security/pass-authentication-credentials-in-url-parameters.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/user-security/pentaho-server-security/pass-authentication-credentials-in-url-parameters.md

# Pass authentication credentials in URL parameters

Explains how to configure the Pentaho Server so you can pass authentication credentials in URL parameters.

By default, the Pentaho Server does not accept authentication credentials passed as URL parameters. To enable this, modify the security properties file on the Pentaho Server. Here is how to configure the Pentaho Server to accept credentials in a URL.

**Note:** If automatic remote authentication is required, we strongly encourage you to configure using one of the **Single Sign-On (SSO) solutions available** such as CAS. You can also use one of our other authentication methods outlined in the **Pentaho Server API documentation** instead.

1. Go to the `pentaho-server/pentaho-solutions/system` directory and open the `security.properties` file.
2. Set the**requestParameterAuthenticationEnabled** property to `true` like this:

   ```

   requestParameterAuthenticationEnabled=true

   ```
3. Save and close the file.
4. Stop and restart the Pentaho Server.
5. Test the configuration by passing a username and password as URL parameters to one of the already-installed sample reports, like this:

   ```

   http://localhost:8080/pentaho/api/repos/%3Apublic%3ASteel%20Wheels%3ACountry%20Performance%20%28heat%20grid%29.xanalyzer/editor?userid=admin&password=password

   ```

If you have configured it correctly you are not prompted to supply authentication credentials and the report displays.

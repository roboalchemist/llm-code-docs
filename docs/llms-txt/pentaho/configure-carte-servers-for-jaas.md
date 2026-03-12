# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/set-up-a-carte-cluster/carte-cluster-configuration/configure-carte-servers-for-jaas.md

# Configure Carte servers for JAAS

You can configure Carte to use the Java Authentication and Authorization Service (JAAS) for user authentication. Perform the following steps to configure Carte with JAAS:

1. Modify the following code sample for your LDAP server or properties file environment and save it as `carte-ldap.jaas.conf` in the `openldap` directory of your Carte server:

   ```
   Kettle {
       org.eclipse.jetty.jaas.spi.LdapLoginModule required
       debug="true"
       contextFactory="com.sun.jndi.ldap.LdapCtxFactory"
       hostname="localhost"
       port="389"
       bindDn="cn=admin,dc=example,dc=com"
       bindPassword="admin"
       authenticationMethod="simple"
       forceBindingLogin="true"
       userBaseDn="ou=People,dc=example,dc=com"
       userRdnAttribute="uid"
       userIdAttribute="uid"
       userPasswordAttribute="userPassword"
       userObjectClass="inetOrgPerson";

      };
      
   Kettle2 {
      org.eclipse.jetty.jaas.spi.PropertyFileLoginModule required
      debug="true"
      file="/installs/common/carte.users";
   }; 

   ```

   **Note:** You may want to set the **debug** parameter to `false` in production environments.
2. Add the following options (with updated path) to `Spoon.bat` (Windows) or `spoon.sh` (Linux)

   ```
   -Djava.security.auth.login.config=<your install path>/openldap/carte-ldap.jaas.conf" "-Dloginmodulename=Kettle
   ```
3. Start Carte and visit the server's page. Verify that it does not prompt for BASIC authentication.

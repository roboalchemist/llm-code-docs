# Source: https://docs.pentaho.com/pba/pentaho-user-console/classic-design/about-pentaho-user-console-perspectives/schedules/schedule-reports/import-emails-from-data-sources/import-emails-from-ldap.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-user-console/about-pentaho-user-console-perspectives/schedules/schedule-reports/import-emails-from-data-sources/import-emails-from-ldap.md

# Import emails from LDAP

You can import emails from your existing LDAP system using the following procedure.

1. Navigate to the `/pentaho-server/pentaho-solutions/system/scheduler-plugin` folder.
2. Open `settings.xml` file and change the `email-source` setting to `ldap`.
3. Update the file `applicationContext-email-import.properties` by providing LDAP connection and query information.

   In the following properties file, ask your administrator to provide LDAP connection information.

   ```
   # LDAP configuration
   ldap.initial-context-factory=com.sun.jndi.ldap.LdapCtxFactory
   ldap.provider-url=ldap://localhost:10389
   ldap.security-authentication=simple
   ldap.security-principal=uid=admin,ou=system
   ldap.security-credentials=Encrypted 2be98afc86aa7f2e4cb79bd75dd80aace
   ldap.search-filter=(objectClass=inetOrgPerson)
   ldap.search-path=ou=users,ou=system
   # ldap.required-attributes must be in the order of first name,
   # last name, email ex: cn=first name, sn=last name, mail=email
   ldap.required-attributes=cn,sn,mail
   ```

   The LDAP password is encrypted using the `encr` utility. This utility is provided along with other startup scripts in the `/server/pentaho-server` folder.

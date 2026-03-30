# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/troubleshooting-overview-cp/security-issues/ldap-incorrectly-authenticates-user-ids-that-do-not-match-letter-case.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/troubleshooting-overview-cp/security-issues/ldap-incorrectly-authenticates-user-ids-that-do-not-match-letter-case.md

# LDAP incorrectly authenticates user IDs that do not match letter case

Some LDAP implementations are case-insensitive, most notably Microsoft Active Directory. When using one of these LDAP distributions as a Pentaho Server authentication back end, you might run into an issue where a valid user name with invalid letter cases will improperly validate. For instance, if Bill is the valid user ID, and someone types in `bILL` at the User Console login screen, that name will authenticate, but it might have improper access to parts of the Pentaho Server.

Perform the following steps to force case-sensitivity for user names and fix this potential security risk:

1. Stop the Pentaho Server.
2. Edit the `/pentaho/server/pentaho-server/pentaho-solutions/system/applicationContext-spring-security-ldap.xml` file.
3. Find `<bean class="org.pentaho.platform.plugin.services.security.userrole.ldap.DefaultLdapAuthenticationProvider">`, and below the last `</constructor-arg>` element therein, and add the `<property>` definition shown in the following example:

   ```xml
   <property name="userDetailsContextMapper">
       <ref bean="ldapContextMapper" />
   </property>
   ```
4. After the `</bean>` tag for `daoAuthenticationProvider`, add the following bean definition, changing the `ldapUsernameAttribute` from `samAccountName` to the value that matches your environment:

   ```xml
   <bean id="ldapContextMapper" class="org.pentaho.platform.engine.security.UseridAttributeLdapContextMapper">
       <property name="ldapUsernameAttribute" value="samAccountName" />
   </bean>
   ```
5. Start the Pentaho Server.

The Pentaho Server will now force case sensitivity in LDAP user names.

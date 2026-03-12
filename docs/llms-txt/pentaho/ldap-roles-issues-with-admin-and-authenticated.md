# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/troubleshooting-overview-cp/security-issues/ldap-roles-issues-with-admin-and-authenticated.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/troubleshooting-overview-cp/security-issues/ldap-roles-issues-with-admin-and-authenticated.md

# LDAP roles issues with Admin and Authenticated

You must not use `Admin` and `Authenticated` roles in your LDAP. Instead, you must configure your system to use `pentahoAdmins` and `pentahoUsers` or other easily identifiable role names.

Open `/pentaho-solutions/system/applicationContext-spring-security.xml` in a text editor. At the bottom of this file, you will find a number of entries that look like:

```xml
A/docs/.*Z=Anonymous,Authenticated
```

These are entries for URL security. They are regular expressions to match a path on the browser’s URL that require the user to be a member of the defined role to gain access. For this example, both `Anonymous` and `Authenticated` gain access.

We replace `Authenticated` with `pentahoUsers` by entering `A/docs/.*Z=Anonymous,pentahoUsers`. For all entries that show `Authenticated`, replace it with `pentahoUsers` or your chosen name. Replace `Admin` with `pentahoAdmins` or your chosen name.

For the change from `Authenticated` to `pentahoUsers,` replace all occurrences. For `Admin` to `pentahoAdmins` you need to be a little more careful because there are some entries that look like this: `A/admin.*Z=pentahoAdmins`.

Edit the `/pentaho-solutions/system/repository.spring.xml` file and make the following changes.

From:

```xml
<bean id="singleTenantAuthenticatedAuthorityName" class="java.lang.String">
    <constructor-arg value="Authenticated" />
   </bean>
```

To:

```xml
<bean id="singleTenantAuthenticatedAuthorityName" class="java.lang.String">
    <constructor-arg value="pentahoUsers" />
   </bean>
```

From:

```xml
<bean id="singleTenantAdminAuthorityName" class="java.lang.String">
    <constructor-arg value="Admin" />
   </bean>
```

To:

```xml
<bean id="singleTenantAdminAuthorityName" class="java.lang.String">
    <constructor-arg value="pentahoAdmins" />
   </bean>
```

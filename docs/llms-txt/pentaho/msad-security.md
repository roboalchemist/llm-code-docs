# Source: https://docs.pentaho.com/pdia-admin/administer/secure-the-pentaho-system/user-security/advanced-security-providers/msad-security.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/secure-the-pentaho-system/user-security/advanced-security-providers/msad-security.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/user-security/advanced-security-providers/msad-security.md

# MSAD security

To use Microsoft Active Directory (MSAD) for user security, you must switch from the default Pentaho security to MSAD, then you must configure MSAD.

**Notes:**&#x20;

* The [LDAP properties](https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/user-security/ldap-security#ldap-properties) section of the [LDAP security](https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/user-security/advanced-security-providers/ldap-security) article contains supplemental information for LDAP values.
* See the **Pentaho Business Analytics** document for information on managing users and roles in the Pentaho User Console (PUC).

## Switch to MS Active Directory

Perform the following steps to switch to MS Active Directory:

1. From User Console **Home** menu, click **Administration**, then select **Authentication** from the left. The **Authentication** interface appears.

   **Local - Use basic Pentaho Authentication** is selected by default.
2. Select the **External - Use LDAP / Active Directory server** option.

   The **LDAP Server Connection** fields populate with a default URL, user name, and password.
3. Change the **Server URL**, **User Name**, and **Password** as needed.
4. Click **Test Server Connection** to verify the connection to your server and to complete the set up.
5. Click the **Browse** buttons to select the **Pentaho System Administrator** user and role to match your configuration. Click **OK**.

   The text box auto-populates with the selected values.
6. Select **Custom Configuration**.
7. For **Users**:
   1. For **Search Base**, enter the path where your users are located.

      ```
      CN=Users,DC=MyDomain,DC=com
      ```
   2. For **Search Filter**, enter the attribute that users log in with.

      ```
      (sAMAccountName={0})
      ```
8. For **Roles**:
   1. For **Role Attributes**, enter the attribute that is used for roles/groups.

      ```
      CN
      ```
   2. For **Role Search Filter**, enter in the ObjectClass that defines that these are roles or groups.

      ```
      (objectClass=group)
      ```
   3. For **Role Search Base**, enter in the path where your roles or groups are located.

      ```
      OU=groups,DC=MyDOmain,DC=com
      ```
9. For **Populator**:
   1. For **Group Role Attribute**, enter in the Attribute that is used for groups.

      ```
      CN
      ```
   2. For **Group Search Base**, enter in the path to where your groups are located.

      ```
      OU=groups,DC=MyDOmain,DC=com
      ```
   3. Set the **Group Search Filter** for the attribute to use:

      ```
      (member={0})
      ```

      **Note:** The following example works only for Microsoft Active Directory configurations.

      You can search down the entire tree to pull only MSAD nested groups by entering the following filter:

      ```
      populator.groupSearchFilter=(member:1.2.840.113556.1.4.1941:={0})
      ```
10. Click **Test**.

    The **LDAP Populator Test** dialog box opens.
11. Enter the LDAP/MSAD **User Name** and **User DN**, then click **OK**.

    You can see the groups and roles that the user is a member of in Microsoft Active Directory.
12. Click **Close** to close the results window, and then click **Save**.
13. Stop the Pentaho Server.
14. Delete the `server/pentaho-server/pentaho-solutions/system/karaf/caches` folder.
15. Restart the Pentaho Server.

The Pentaho Server is now configured to authenticate users against your MSAD server. You can log in to the User Console using your Active Directory credentials.

See the **Install Pentaho Data Integration and Analytics** document for instructions on starting and stopping the Pentaho Server.

## Manual configuration

After you have switched Pentaho to authenticate against Active Directory, you can proceed with configuring MSAD.

### Binding

MSAD allows you to uniquely specify users in two ways (Kerberos notation or Windows domain notation), in addition to the standard Distinguished Name (DN) method. If the standard DN is not working, try one of the following methods. Each of the following examples is shown in the context of the **userDn** property of the Spring Security `DefaultSpringSecurityContextSource` bean.

**Note:** The examples in this section use `DefaultSpringSecurityContextSource`. You may need to use the same notation (Kerberos or Windows domain) in all your DN patterns.

The following code block is an example of the Kerberos notation for *<pentahoadmin@mycompany.com>*:

File: `applicationContext-security-ldap.properties`

```xml

contextSource.providerUrl=ldap\://mycompany\:389
contextSource.userDn=pentahoadmin@mycompany.com
contextSource.password=omitte

```

The following code block is an example of the Windows domain notation for *MYCOMPANY\pentahoadmin*:

File: `applicationContext-security-ldap.properties`

```xml

contextSource.providerUrl=ldap\://mycompany\:389
contextSource.userDn=MYCOMPANY\pentahoadmin
contextSource.password=omitted

```

### Referrals

If more than one Active Directory instance is serving folder information, it may be necessary to enable **referral**, shown in the following code block. This is accomplished by modifying the `DefaultSpringSecurityContextSource` bean:

```xml

<bean id="contextSource" class="org.springframework.security.ldap.DefaultSpringSecurityContextSource">
    <constructor-arg value="${contextSource.providerUrl}"/>
    <property name="userDn" value="${contextSource.userDn}"/>
    <property name="password" value="${contextSource.password}"/>
    <property name="referral" value="follow" />
</bean>

```

### Nested groups

You can pull nested groups for Pentaho within Microsoft Active Directory.

In the **Populator Group Search Filter**, enter the following filter for MSAD nested groups:

```
populator.groupSearchFilter=(member:1.2.840.113556.1.4.1941:={0})
```

This filter will search down the entire tree of nested groups.

**Note:** This attribute only works for Microsoft Active Directory configurations.

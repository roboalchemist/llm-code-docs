# Source: https://docs.axonius.com/docs/update-active-directory-user.md

# Active Directory - Update Users

**Active Directory - Update Users** adds or updates attributes in Active Directory user accounts for the user assets returned by the selected query or assets selected on the relevant asset page.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the Active Directory adapter** - Select this option to use the first connected adapter credentials.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  * To use this option, you must successfully configure an [Microsoft Active Directory (AD)](/docs/microsoft-active-directory-ad) adapter connection.

  * The user name and the password used for the adapter connection must have permission to create users in Active Directory.
</Callout>

* **Attribute name** - Select the attribute to add or change.
* **Attribute value** - Enter a value for the attribute. When changing the value, the old value is overwritten.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  <br />

  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **DC Address** - The address of the Domain Controller (DC). Can be either an IP address or a valid DNS name that  Axonius can communicate with via the [Required Ports](#required-ports). You can configure the **DC Address** field with a customized LDAP port.

  * **Port** - To add the customized LDAP port enter a DC Address and a **Port** number separated with a colon in the following format DC\_NAME:PORT\_NUMBER. When you use this format you direct the system to use the value following DC\_NAME: as a custom port.

  * **Fallback DC Address** and **Fallback Port** - Enter a secondary DC address and port as  a secondary server to be connected if the first one fails.

  * **SASL Mechanism** *(default: no SASL)* - SASL authentication is supported. The default authentication method is *no  SASL*.  The following authentication methods are available: *No SaSL*, *External*, *GSSAPI*, *Digest MD5* and *Plain*. Each method requires different authentication parameters:

  * No SASL - Authenticate using User Name and Password

  * External - Authenticate using User Name

  * GSSAPI - Optional authentication using UserName

  * Digest MD5 - Authenticate using Username, Password, Enable signing, and  Realm (optional) Authorization ID (optional)

  * Plain - Authenticate using Username/Authentication ID and Password and Authorization ID (optional)

  * **Parameters depend on the SASL Mechanism selection**
    a.  **User Name** (DOMAIN\USERNAME) and **Password** *(required, depends on authentication method)* - A user with regular LDAP query rights and its password.   Enter the userPrincipalName (username\@domain) OR domain\username. When connecting over SSL, the username must be in the format username\@domain.
    b.   	**Authentication ID**  - Use for SASL Plain Mechanism.\
    c.     **Realm** *(optional)* - The LDAP Realm.
    d.      **Authorization ID** (authzid) *(optional)* - The SASL authzid
    e.      **Enable signing** - Enable LDAP signing, refer to [LDAP Signing for AD](https://u-tools.com/help/LdapMismatch.asp).

  * **DNS Server Address** - Axonius assumes that Domain Controller listed in each connection is also a DNS server. If your Domain Controller does not have the DNS role installed and you would like to use a different system for name resolution of discovered assets you can enter an alternate IP address here (even if it is installed, but you enter a field here, Axonius will use it). Please note that this setting is only used for discovered assets and will not affect resolution of the Domain Controller name entered in the connection configuration. This configuration value is used in conjunction with the **Enable IP Resolving** advanced setting.

  * **Alternative DNS Suffix** -  Replace the device original DNS suffix for DNS resolving. For example, if the device name is windows8.acme.corp , and the Alternative DNS Suffix defined is 'acme-corp.lan', DNS resolving will be done for windows8.acme-corp.lan.

  * **Use SSL for connection** *(default: Unencrypted)* - Select either Unencrypted (LDAP) or Verified / Unverified to use LDAPS (LDAP over SSL).

  * **CA File** - If you choose the Verified option to use LDAPS (LDAP over SSL), you need to add SSL certificates (PEM format CA file) to the credentials.

  * **SSL cipher** -  Enter an SSL cipher to use for the TLS object of the connection. Using a stronger cipher can solve connection failures when using the default cipher.[Examples of OpenSSl ciphers](https://www.openssl.org/docs/man1.1.1/man1/ciphers.html).

  * **Do Not Fetch Users** - Select this option if you do not want to fetch users.

  * **Fetch Disabled Devices** and **Fetch Disabled Users** - Select to fetch disabled devices or users. By default, Axonius fetches only enabled devices and users.

  * **Filter Deleted Devices** - By default Axonius fetches deleted devices. Select this option to not fetch deleted devices.

  * **Filter Deleted Users** - By default Axonius fetches deleted users. Select this option to not fetch deleted users.

  * **Connect to Global Catalog (GC)** - Select this option if the configured DC has a Global Catalog role.

  * **Organizational units include list** - Set one or more OUs so Axonius will fetch entities that reside only in the listed organizational units. Each item in the list should represent an 'OU' value of the desired OU DN. For example, for OU DN (“Ireland Office/acme/corp , New York Office/acme/corp”), specify the organizational units of Acme corporation of the Ireland Office and New York Office.

  * **Organizational units to exclude** - Set one or more OUs so that Axonius will not fetch entities that belong to the specified organizational units. Each item in the list should represent an 'OU' value of the OU DN that should be excluded. For example, for OU DN (“Ireland Office/acme/corp , New York Office/acme/corp”), specify the organizational units of Acme corporation of the Ireland Office and New York Office.

  * **Search Base** - LDAP Search Base.

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the necessary permissions to perform this enforcement action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).
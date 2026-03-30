# Source: https://docs.axonius.com/docs/deploying-the-active-directory-adapter.md

# Deploying the Active Directory Adapter

To deploy the Active Directory Adapter, perform the following steps:

## 1. Create Active Directory credentials with the appropriate permissions

You can connect Axonius to Active Directory using a Service Account with a username and password or via Kerberos

<Accordion title="Service Account" icon="fa-user">
  **Prerequisites:** Sign in with an account that can create users and modify group membership in the domain (Domain Admin or delegated equivalent).

  1. Open **Active Directory Users and Computers** (`dsa.msc`).
  2. Create (or choose) an OU for service accounts (e.g., **OU=Service Accounts**).
  3. Right-click → **New → User**.
     1. Enter *User logon name (UPN):*  e.g.`axonius-svc` `@<your-domain>`.
     2. Enter *User logon name (pre-Windows 2000):* e.g.`axonius-svc`.
     3. Set a strong password.
     4. Uncheck “User must change password at next logon.”
     5. Check “Password never expires.”
  4. **Finish** creating the user.
  5. Create or edit a GPO to deny interactive logon. Go to **Computer Configuration → Windows Settings → Security Settings → Local Policies → User Rights Assignment**.
  6. Add the service account to **Deny log on locally**.
  7. Add the service account to **Deny log on through Remote Desktop Services**.
  8. Link the GPO to the appropriate scope (e.g., Domain Controllers OU or Workstations/Servers OUs).
  9. Add the service account to the **Builtin → Account Operators** group.
  10. Add the service account to the **Remote Management Users** local group on each target computer (preferably via GPO Preferences).
</Accordion>

<Accordion title="Kerberos" icon="fa-ticket">
  **Prerequisites:** Service Account with appropriate permissions (follow the Service Account steps if needed).

  1. Confirm a **Key Distribution Center (KDC)** is available. Every AD domain controller functions as a KDC by default.
  2. Ensure the **realm name** (your AD domain in uppercase, e.g. CONTOSO.LOCAL) is known and matches the value you enter in Axonius.
  3. Verify **DNS resolution for the DCs/KDCs**. Active Directory automatically creates the required A and SRV records; just confirm that Axonius or the Axonius Gateway can resolve them.
  4. Confirm that **port 88 (Kerberos)** is reachable from Axonius or the Axonius Gateway to the domain controllers.
</Accordion>

## 2. Set up the Active Directory adapter in Axonius

Create the Adapter connection in Axonius. Based on the authentication method (Service Account or Kerberos), fill out the specific fields and configure optional settings.

## Add a New Connection

* Navigate to the **Adapters** page → search for `Microsoft Active Directory(AD)` → click on the adapter tile.

  <Image align="left" border={false} width="300px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/MSAD_Adapter.png" />

* On the top right side, click on **Add Connection**.

* The **Add Connection** drawer opens.

<Image border={false} src="https://files.readme.io/64294b633b415872df05ca619595bd91be4ac06529cfdda18fd5d5e67f69b56c-image.png" />

<br />

### Required Fields

<Tabs>
  <Tab title="Service Account - LDAPS (LDAP over SSL)">
    * **DC Address** - Specify the IP address of a single domain controller, **or** an FQDN that resolves to a single domain controller in an Active Directory Domain. It is recommended to enter a domain controller with DNS and Primary (PDC) roles.

    * **Port** - 636 (LDAPS default, refer to the [Required Ports](https://docs.axonius.com/docs/deploying-the-active-directory-adapter-test#required-ports) table if you setup differently)

    * **SASL Mechanism** - No SASL

    * **Username** and **Password** - A Service Account with appropriate permissions and its password.

      * **Username format** - `username@domain` OR `domain\username`

      <Callout icon="📘" theme="info">
        **Note**:

        When connecting over SSL, the username must be in the format `username@domain`
      </Callout>

    * **Use SSL for connection** -
      * **Verified** - The DC Address above must be the FQDN provided by the certificate.
      * **Unverified** - *(not recommended for production environments)* Skips certificate verification

    * **CA File** - To use LDAPS, you must upload an SSL certificate in PEM format

    * **Connection Label** - Friendly name for your new adapter connection.
  </Tab>

  <Tab title="Service Account - LDAP">
    * **DC Address** - Specify the IP address of a single domain controller, **or** an FQDN that resolves to a single domain controller in an Active Directory Domain. It is recommended to enter a domain controller with DNS and Primary (PDC) roles.
    * **Port** - 389 (LDAP default, refer to the [Required Ports](https://docs.axonius.com/docs/deploying-the-active-directory-adapter-test#required-ports) table if you setup differently)
    * **SASL Mechanism** - No SASL
    * **Username** and **Password** - A Service Account with appropriate permissions and its password.

      * **Username format** - `username@domain` OR `domain\username`

      <Callout icon="📘" theme="info">
        **Note**:

        When connecting over SSL, the username must be in the format `username@domain`
      </Callout>

      * **Use SSL for connection** - Unencrypted
    * **Connection Label** - Friendly name for your new adapter connection.
  </Tab>

  <Tab title="Kerberos">
    * **DC Address** - Specify the IP address of a single domain controller, **or** an FQDN that resolves to a single domain controller in an Active Directory Domain. It is recommended to enter a domain controller with DNS and Primary (PDC) roles.

    * **Port** - 88 (Kerberos default, refer to the [Required Ports](https://docs.axonius.com/docs/deploying-the-active-directory-adapter-test#required-ports) table if you setup differently)

    * **SASL Mechanism** -
      * **GSSAPI** - Kerbero's default mechanism. (`Realm` / `Kerberos KDC` fields required)
      * **External** - Authenticate using User Name
      * **Digest MD5** - Authenticate using Username, Password, Enable signing, and  Realm Authorization ID (`Realm` / `Authorization ID (authzid)` fields required)
      * **Plain** - Authenticate using Username/Authentication ID and Password and Authorization ID (`Authorization ID (authzid)` fields required)

    * **Realm** - The LDAP Realm, it must match the realm configured on your DCs (which is your AD DNS domain in uppercase - e.g., `EXAMPLE.COM`).

    * **Kerberos KDC** - The **hostname** or **IP address** of a Domain Controller that issues Kerberos tickets (e.g., `dc01.example.com`).

    * **Authorization ID (authzid)** - The SASL *authzid*.

    * **Enable signing** - Enable LDAP signing, refer to [LDAP Signing for AD](https://u-tools.com/help/LdapMismatch.asp)

    * **Username** and **Password** - A Service Account with appropriate permissions and its password.

      * **Username format** - `username@domain` OR `domain\username`

      <Callout icon="📘" theme="info">
        **Note**:

        When connecting over SSL, the username must be in the format `username@domain`
      </Callout>

    * **Use SSL for connection** - Unencrypted.

    * **Connection Label** - Friendly name for your new adapter connection.
  </Tab>
</Tabs>

### Required Ports

Axonius must be able to communicate with the address supplied in **DC Address** using one of the following ports:

| Port       | Description                                                                                     |
| :--------- | :---------------------------------------------------------------------------------------------- |
| **88**     | when using **Kerberos** authorization                                                           |
| **389**    | when **LDAP - SSL unencrypted** is selected                                                     |
| **636**    | when **LDAPS - SSL encrypted or unverified** is selected                                        |
| **3268**   | when the **insecure Global Catalog - SSL unencrypted**   is selected                            |
| **3269**   | when both **SSL encrypted or unverified** is selected and **Secure Global Catalog**  is enabled |
| **5986**   | when the **Fetch Permissions** advanced setting is enabled                                      |
| **Custom** | when you set a **custom port** in DC Address                                                    |

<br />

### Optional Fields

<Accordion title="Expand/Collapse">
  * **Fallback DC Address**, **Fallback Port** - Enter a secondary DC address and port as  a secondary server to be connected if the first one fails.
  * **DNS Server Address** - Axonius assumes that Domain Controller listed in each connection is also a DNS server. If your Domain Controller does not have the DNS role installed and you would like to use a different system for name resolution of discovered assets you can enter an alternate IP address here (even if it is installed, but you enter a field here, Axonius will use it). Please note that this setting is only used for discovered assets and will not affect resolution of the Domain Controller name entered in the connection configuration. This configuration value is used in conjunction with the **Enable IP Resolving** advanced setting.
  * **Alternative DNS Suffix** -  Replace the device original DNS suffix for DNS resolving. For example, if the device name is windows8.acme.corp , and the Alternative DNS Suffix defined is 'acme-corp.lan', DNS resolving will be done for windows8.acme-corp.lan.
  * **SSL cipher** -  Enter an SSL cipher to use for the TLS object of the connection. Using a stronger cipher can solve connection failures when using the default cipher. [Examples of OpenSSl ciphers](https://www.openssl.org/docs/man1.1.1/man1/ciphers.html)
  * **Do Not Fetch Users** - Select this option if you do not want to fetch users
  * **Fetch Disabled Devices** and **Fetch Disabled Users** - Select to fetch disabled devices or users. By default, Axonius fetches only enabled devices and users.
  * **Filter Deleted Devices** - By default Axonius fetches deleted devices. Select this option to not fetch deleted devices.
  * **Filter Deleted Users** - By default Axonius fetches deleted users. Select this option to not fetch deleted users.
  * **Connect to Global Catalog (GC)**  - Select this option if the configured DC has a Global Catalog role.
  * **Organizational units include list** - To ensure Axonius fetches entities only from specific organizational units (OUs), input the desired OUs using their distinguished names (DNs). Each entry in the list should correspond to a separate OU. For example, if you want to include the organizational units for Acme Corporation in both the Ireland and New York Offices, specify them as follows:
    * `Ireland Office/Acme/Corp`,`New York Office/Acme/Corp`
  * **Organizational units to exclude** - To prevent Axonius from fetching entities belonging to specific organizational units (OUs), list the OUs using their distinguished names (DNs). Each entry in the list should correspond to a separate OU. For instance, if you want to exclude the organizational units for Acme Corporation in both the Ireland and New York Offices, specify them as follows:
    * `Ireland Office/Acme/Corp`,`New York Office/Acme/Corp`
  * **Search Base** - Search Base: This field specifies a path for conducting searches within a defined scope. By default, searches are conducted across the entire domain. However, configuring this option can be beneficial when dealing with multiple Active Directory (AD) subdomains, as it allows you to limit the search to resources within a specific subdomain.
  * **HTTPS Proxy** - A proxy to use when connecting to the value supplied in **Root Domain**.
  * **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Root Domain** via the value supplied in **HTTPS Proxy**.
  * **HTTPS Proxy Password** - The password to use when connecting to the value supplied in **Root Domain** via the value supplied in **HTTPS Proxy**.
</Accordion>

## 3. (optional) Configure Advanced Settings

Refer to the Active Directory [Advanced Settings](https://docs.axonius.com/axonius-help-docs/docs/active-directory-advanced-settings).

<br />
# Authentication configuration settings

Mattermost supports up to 4 distinct, concurrent methods of user
authentication:

- An OpenID provider
- A SAML provider
- An LDAP instance (e.g., Active Directory, OpenLDAP)
- Email and Password

Review and manage the following authentication configuration options in
the System Console by selecting the **Product**
[\|product-list\|](##SUBST##|product-list|) menu, selecting **System
Console**, and then selecting **Authentication**:

- [Signup](#signup)
- [Email](#email)
- [Password](#password)
- [MFA](#mfa)
- [AD/LDAP](#ad-ldap)
- [SAML 2.0](#saml-2-0)
- [OAuth 2.0](#oauth-2-0)
- [OpenID Connect](#openid-connect)
- [Guest Access](#guest-access)

:::: tip
::: title
Tip
:::

System admins managing a self-hosted Mattermost deployment can edit the
`config.json` file as described in the following tables. Each
configuration value below includes a JSON path to access the value
programmatically in the `config.json` file using a JSON-aware tool. For
example, the `EnableUserCreation` value is under `TeamSettings`.

- If using a tool such as [jq](https://stedolan.github.io/jq/), you\'d
  enter:
  `cat config/config.json | jq '.TeamSettings.EnableUserCreation'`
- When working with the `config.json` file manually, look for an object
  such as `TeamSettings`, then within that object, find the key
  `EnableUserCreation`.
::::

------------------------------------------------------------------------

## Signup

Access the following configuration settings in the System Console by
going to **Authentication \> Signup**.

### Enable account creation

+----------------------------------+----------------------------------------+
| - **true**: **(Default)** Anyone | - System Config path: **Authentication |
|   can sign up for a user account |   \> Signup**                          |
|   on this server without needing | - `config.json` setting:               |
|   to be invited. Applies to      |   `TeamSettings` \>                    |
|   email-based signups only.      |   `EnableUserCreation` \> `true`       |
| - **false**: The ability to      | - Environment variable:                |
|   create accounts is disabled.   |   `MM_TEAMSETTINGS_ENABLEUSERCREATION` |
|   Selecting **Create Account**   |                                        |
|   displays an error. Applies to  |                                        |
|   email, OpenID Connect, and     |                                        |
|   OAuth 2.0 user account         |                                        |
|   authentication.                |                                        |
+----------------------------------+----------------------------------------+

:::: note
::: title
Note
:::

\- LDAP and SAML users can always create a Mattermost account by logging
in using LDAP or SAML user credentials, regardless of whether this
configuration setting is enabled. - From Mattermost v10.9, email
addresses enclosed in angle brackets (e.g., `<billy@example.com>`) will
be rejected. To avoid issues, ensure all user emails comply with the
plain address format (e.g., `billy@example.com`). In addition, we
strongly recommend taking proactive steps to audit and update Mattermost
user data to align with this product change, as impacted users may face
issues accessing Mattermost or managing their user profile. You can
update these user emails manually using
`mmctl user email <administration-guide/manage/mmctl-command-line-tool:mmctl user email>`{.interpreted-text
role="ref"}. - See the encryption options documentation for details on
what
`encryption methods <deployment-guide/encryption-options:saml encryption support>`{.interpreted-text
role="ref"} Mattermost supports for SAML.
::::

### Restrict account creation to specified email domains

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| This setting limits the email address domains that can be used to create a new account or team. \| - System Config path: **Authentication \>        |
| Signup** You **must** set                                                                                                                           |
| `Require Email Verification <administration-guide/configure/authentication-configuration-settings:require email verification>`{.interpreted-text    |
| role="ref"} \| - `config.json` setting: `TeamSettings` \> `RestrictCreationToDomains` to `true` for the restriction to function. This setting only  |
| affects email login. \| - Environment variable: `MM_TEAMSETTINGS_RESTRICTCREATIONTODOMAINS`                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

### Enable open server

+---------------------------------------+--------------------------------------+
| - **true**: Users can create accounts | - System Config path:                |
|   on the server without an            |   **Authentication \> Signup**       |
|   invitation.                         | - `config.json` setting:             |
| - **false**: **(Default)** Users      |   `TeamSettings` \>                  |
|   **must** have an invitation to      |   `EnableOpenServer`                 |
|   create an account on the server.    | - Environment variable:              |
|                                       |   `MM_TEAMSETTINGS_ENABLEOPENSERVER` |
+---------------------------------------+--------------------------------------+

### Enable email invitations

+--------------------------+-----------------------------------------------+
| - **true**: **(Default   | - System Config path: **Authentication \>     |
|   for Cloud              |   Signup**                                    |
|   deployments)** Allows  | - `config.json` setting: `ServiceSettings` \> |
|   users to send email    |   `EnableEmailInvitations` \> `false`         |
|   invitations.           | - Environment variable:                       |
| - **false**: **(Default  |   `MM_SERVICESETTINGS_ENABLEEMAILINVITATIONS` |
|   for self-hosted        |                                               |
|   deployments)**         |                                               |
|   Disables email         |                                               |
|   invitations.           |                                               |
+--------------------------+-----------------------------------------------+

:::: note
::: title
Note
:::

Cloud admins can\'t modify this configuration setting.
::::

### Invalidate pending email invites

+-------------------------------------------------+--------------------+
| This button invalidates email invitations that  | - System Config    |
| have not been accepted (by default, invitations |   path:            |
| expire after 48 hours).                         |   **Authentication |
|                                                 |   \> Signup**      |
| This option has no `config.json` setting or     | - `config.json`    |
| environment variable.                           |   setting: N/A     |
|                                                 | - Environment      |
|                                                 |   variable: N/A    |
+-------------------------------------------------+--------------------+

------------------------------------------------------------------------

## Email

Access the following configuration settings in the System Console by
going to **Authentication \> Email**.

### Enable account creation with email

+---------------------------------------+--------------------------------------------+
| - **true**: **(Default)** Allows      | - System Config path: **Authentication \>  |
|   creation of team and user accounts  |   Email**                                  |
|   with email and password.            | - `config.json` setting: `EmailSettings`   |
| - **false**: Disables creation of     |   \> `EnableSignUpWithEmail`               |
|   team and user accounts with email   | - Environment variable:                    |
|   and password. Requires a single     |   `MM_EMAILSETTINGS_ENABLESIGNUPWITHEMAIL` |
|   sign-on (SSO) service to create     |                                            |
|   accounts.                           |                                            |
+---------------------------------------+--------------------------------------------+

:::: note
::: title
Note
:::

Cloud admins can\'t modify this configuration setting.
::::

### Require email verification

+--------------------------------+-----------------------------------------------+
| - **true**: **(Default for     | - System Config path: **Authentication \>     |
|   Cloud deployments)**         |   Email**                                     |
|   Requires email verification  | - `config.json` setting: `EmailSettings` \>   |
|   for new accounts before      |   `RequireEmailVerification` \> `false`       |
|   allowing the user to         | - Environment variable:                       |
|   sign-in.                     |   `MM_EMAILSETTINGS_REQUIREEMAILVERIFICATION` |
| - **false**: **(Default for    |                                               |
|   self-hosted deployments)**   |                                               |
|   Disables email verification. |                                               |
|   can be used to speed         |                                               |
|   development by skipping the  |                                               |
|   verification process.        |                                               |
+--------------------------------+-----------------------------------------------+

### Enable sign-in with email

+-----------------------------------+--------------------------------------------+
| - **true**: **(Default)** Allows  | - System Config path: **Authentication \>  |
|   users to sign-in with email and |   Email**                                  |
|   password.                       | - `config.json` setting: `EmailSettings`   |
| - **false**: Disables             |   \> `EnableSignInWithEmail`               |
|   authentication with email and   | - Environment variable:                    |
|   password, and removes the       |   `MM_EMAILSETTINGS_ENABLESIGNINWITHEMAIL` |
|   option from the login screen.   |                                            |
|   Use this option to limit        |                                            |
|   authentication to single        |                                            |
|   sign-on services.               |                                            |
+-----------------------------------+--------------------------------------------+

:::: note
::: title
Note
:::

\- To provide users with only a single email sign in option on the login
page, ensure that the [enable sign-in with
username](#enable-sign-in-with-username) configuration setting is set to
**false**. - From Mattermost v10.9, email addresses enclosed in angle
brackets (e.g., `<billy@example.com>`) will be rejected. To avoid
issues, ensure all user emails comply with the plain address format
(e.g., `billy@example.com`). In addition, we strongly recommend taking
proactive steps to audit and update Mattermost user data to align with
this product change, as impacted users may face issues accessing
Mattermost or managing their user profile. You can update these user
emails manually using
`mmctl user email <administration-guide/manage/mmctl-command-line-tool:mmctl user email>`{.interpreted-text
role="ref"}.
::::

### Enable sign-in with username

+-------------------------------------+-----------------------------------------------+
| - **true**: **(Default)** Allows    | - System Config path: **Authentication \>     |
|   authentication with a username    |   Email**                                     |
|   and password for accounts created | - `config.json` setting: `EmailSettings` \>   |
|   with an email address. This       |   `EnableSignInWithUsername`                  |
|   setting does not affect AD/LDAP   | - Environment variable:                       |
|   sign-in.                          |   `MM_EMAILSETTINGS_ENABLESIGNINWITHUSERNAME` |
| - **false**: Disables authenticaton |                                               |
|   with a username and removes the   |                                               |
|   sign in option from. from the     |                                               |
|   login screen.                     |                                               |
+-------------------------------------+-----------------------------------------------+

:::: note
::: title
Note
:::

We highly recommended that email-based authentication is only used in
small teams on private networks.
::::

------------------------------------------------------------------------

## Password

Access the following configuration settings in the System Console by
going to **Authentication \> Password**.

:::: note
::: title
Note
:::

From Mattermost v11.0, password hashing uses PBKDF2 for enhanced
security. User passwords are automatically migrated when they log in
after upgrading to v11.0 or later. This migration is progressive and
happens transparently when users authenticate.
::::

### Minimum password length

+------------------------------------------------+---------------------------------------+
| This setting determines the minimum number of  | - System Config path:                 |
| characters in passwords. It must be a whole    |   **Authentication \> Password**      |
| number greater than or equal to 5 and less     | - `config.json` setting:              |
| than or equal to 72.                           |   `PasswordSettings` \>               |
|                                                |   `MinimumLength`                     |
| Numerical input. Default is **5**.             | - Environment variable:               |
|                                                |   `MM_PASSWORDSETTINGS_MINIMUMLENGTH` |
+------------------------------------------------+---------------------------------------+

### Password requirements

+----------------------------------------+----------------------------------------------+
| This setting controls password         | - System Config path: **Authentication \>    |
| character requirements. By checking    |   Password**                                 |
| the corresponding box, passwords must  | - `config.json` settings: `PasswordSettings` |
| contain:                               |   \> `Lowercase` \> `false`,                 |
|                                        |   `PasswordSettings` \> `Uppercase` \>       |
| - **At least one lowercase letter**    |   `false`, `PasswordSettings` \> `Number` \> |
| - **At least one uppercase letter**    |   `false`, `PasswordSettings` \> `Symbol` \> |
| - **At least one number**              |   `false`                                    |
| - **At least one symbol** out of       | - Environment variables:                     |
|   these:                               |   `MM_PASSWORDSETTINGS_LOWERCASE`,           |
|   `` !"#$%&'()*+,-./:;<=>?@[]^_`|~ ``. |   `MM_PASSWORDSETTINGS_UPPERCASE`,           |
|                                        |   `MM_PASSWORDSETTINGS_NUMBER`,              |
| The error message previewed in the     |   `MM_PASSWORDSETTINGS_SYMBOL`               |
| System Console will appear if the user |                                              |
| attempts to set an invalid password.   |                                              |
|                                        |                                              |
| The default for all boxes is           |                                              |
| unchecked. The default for all         |                                              |
| settings in `config.json` is `false`.  |                                              |
+----------------------------------------+----------------------------------------------+

### Maximum login attempts

+---------------------------------------------+---------------------------------------------+
| This setting determines the number of       | - System Config path: **Authentication \>   |
| failed sign-in attempts a user can make     |   Password**                                |
| before being locked out and required to go  | - `config.json` setting: `ServiceSettings`  |
| through a password reset by email.          |   \> `MaximumLoginAttempts` \> `10`         |
|                                             | - Environment variable:                     |
| Numerical input. Default is **10**.         |   `MM_SERVICESETTINGS_MAXIMUMLOGINATTEMPTS` |
+---------------------------------------------+---------------------------------------------+

### Enable forgot password link

+----------------------------------+----------------------------------------+
| - **true**: **(Default)**        | - System Config path: **Authentication |
|   Displays the **Forget          |   \> Enable forgot password link**     |
|   Password** link on the         | - `config.json` setting:               |
|   Mattermost login page.         |   `LdapSettings` \>                    |
| - **false**: Hides the **Forgot  |   `ForgotPasswordLink` \> `true`       |
|   Password** link from the       | - Environment variable:                |
|   Mattermost login page.         |   `MM_LDAPSETTINGS_FORGOTPASSWORDLINK` |
+----------------------------------+----------------------------------------+

:::: note
::: title
Note
:::

You can customize the **Forgot Password** link URL by going to **Site
Configuration \> Customization \> Forgot Password Custom Link**. See the
`configuration <administration-guide/configure/site-configuration-settings:forgot password custom link>`{.interpreted-text
role="ref"} documentation for details.
::::

------------------------------------------------------------------------

## MFA

Access the following configuration settings in the System Console by
going to **Authentication \> MFA**.

We recommend deploying Mattermost within your own private network, and
using VPN clients for mobile access, so that Mattermost is secured with
your existing protocols. If you choose to run Mattermost outside your
private network, bypassing your existing security protocols, we
recommend adding a multi-factor authentication service specifically for
accessing Mattermost.

### Enable multi-factor authentication

+---------------------------------------------------------------------------------------------------------------+--------------------------------------------------------+
| - **true**: Users who sign-in with AD/LDAP or an email address have the option to add                         | - System Config path: **Authentication \> MFA**        |
|   `multi-factor authentication </administration-guide/onboard/multi-factor-authentication>`{.interpreted-text | - `config.json` setting: `ServiceSettings` \>          |
|   role="doc"} to their accounts.                                                                              |   `EnableMultifactorAuthentication` \> `false`         |
| - **false**: **(Default)** Disables multi-factor authentication.                                              | - Environment variable:                                |
|                                                                                                               |   `MM_SERVICESETTINGS_ENABLEMULTIFACTORAUTHENTICATION` |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------------------------+

### Enforce multi-factor authentication

+----------------------------------------------------------------------------------+---------------------------------------------------------+
| - **true**: Requires `multi-factor authentication (MFA)                          | - System Config path: **Authentication \> MFA**         |
|   </administration-guide/onboard/multi-factor-authentication>`{.interpreted-text | - `config.json` setting: `ServiceSettings` \>           |
|   role="doc"} for users who sign-in with AD/LDAP or an email address. New users  |   `EnforceMultifactorAuthentication` \> `false`         |
|   must set up MFA. Logged in users are redirected to the MFA setup page until    | - Environment variable:                                 |
|   configuration is complete.                                                     |   `MM_SERVICESETTINGS_ENFORCEMULTIFACTORAUTHENTICATION` |
| - **false**: **(Default)** MFA is optional.                                      |                                                         |
+----------------------------------------------------------------------------------+---------------------------------------------------------+

:::: note
::: title
Note
:::

If your system has users who authenticate with methods other than
AD/LDAP and email, MFA must be enforced with the authentication provider
outside of Mattermost.
::::

------------------------------------------------------------------------

## AD/LDAP

Access the following configuration settings in the System Console by
going to **Authentication \> AD/LDAP**. This opens the AD/LDAP setup
wizard with step-by-step sections and testing to help configure each
setting.

The wizard is organized into the following sections:

- [Connection settings](#connection-settings): Configure server
  connection details
- [User filters](#user-filters): Set up user identification and
  filtering
- [Account synchronization](#account-synchronization): Map AD/LDAP
  attributes to Mattermost user fields
- [Group synchronization](#group-synchronization): Configure group
  settings and group attributes (if using LDAP groups)
- [Synchronization performance](#synchronization-performance): Adjust
  synchronization timing and performance settings
- [Synchronization history](#synchronization-history): View
  synchronization status and manually trigger syncs

:::: note
::: title
Note
:::

Each section includes a **Test** option you can use to verify your
configuration incrementally, helping identify and resolve issues early
in the setup process.
::::

### Connection settings

Configure your AD/LDAP server connection and basic authentication
settings. Use the **Test Connection** button in this section to verify
your server connection before proceeding to other configuration steps.

#### Enable sign-in with AD/LDAP

+-----------------------------------+----------------------------------+
| - **true**: Allows sign-in with   | - System Config path:            |
|   AD/LDAP.                        |   **Authentication \> AD/LDAP**  |
| - **false**: **(Default)**        | - `config.json` setting:         |
|   Disables sign-in with AD/LDAP.  |   `LdapSettings` \> `Enable` \>  |
|                                   |   `false`                        |
|                                   | - Environment variable:          |
|                                   |   `MM_LDAPSETTINGS_ENABLE`       |
+-----------------------------------+----------------------------------+

#### Enable synchronization with AD/LDAP

+--------------------------------+-------------------------------------+
| - **true**: Mattermost         | - System Config path:               |
|   periodically syncs users     |   **Authentication \> AD/LDAP**     |
|   from AD/LDAP.                | - `config.json` setting:            |
| - **false**: **(Default)**     |   `LdapSettings` \> `EnableSync` \> |
|   Disables AD/LDAP             |   `false`                           |
|   synchronization.             | - Environment variable:             |
|                                |   `MM_LDAPSETTINGS_ENABLESYNC`      |
+--------------------------------+-------------------------------------+

:::: note
::: title
Note
:::

Synchronization with AD/LDAP settings in the System Console can be used
to determine the connectivity and availability of arbitrary hosts.
System admins concerned about this can use custom admin roles to limit
access to modifying these settings. See the
`delegated granular administration <administration-guide/onboard/delegated-granular-administration:edit privileges of admin roles (advanced)>`{.interpreted-text
role="ref"} documentation for details.
::::

#### Login field name

+-------------------------------------------------+------------------------------------+
| This setting will display placeholder text in   | - System Config path:              |
| the login field of the sign-in page. This text  |   **Authentication \> AD/LDAP**    |
| can remind users to sign-in with their AD/LDAP  | - `config.json` setting:           |
| credentials.                                    |   `LdapSettings` \>                |
|                                                 |   `LoginFieldName`                 |
| String input. Default is `AD/LDAP Username`.    | - Environment variable:            |
|                                                 |   `MM_LDAPSETTINGS_LOGINFIELDNAME` |
+-------------------------------------------------+------------------------------------+

#### AD/LDAP server

+--------------------------------+-------------------------------------+
| This is the domain name or IP  | - System Config path:               |
| address of the AD/LDAP server. |   **Authentication \> AD/LDAP**     |
|                                | - `config.json` setting:            |
| String input.                  |   `LdapSettings` \> `LdapServer`    |
|                                | - Environment variable:             |
|                                |   `MM_LDAPSETTINGS_LDAPSERVER`      |
+--------------------------------+-------------------------------------+

:::: note
::: title
Note
:::

Synchronization with AD/LDAP settings in the System Console can be used
to determine the connectivity and availability of arbitrary hosts.
System admins concerned about this can use custom admin roles to limit
access to modifying these settings. See the
`delegated granular administration <administration-guide/onboard/delegated-granular-administration:edit privileges of admin roles (advanced)>`{.interpreted-text
role="ref"} documentation for details.
::::

#### AD/LDAP port

+----------------------------------+-----------------------------------+
| This is the port Mattermost uses | - System Config path:             |
| to connect to the AD/LDAP        |   **Authentication \> AD/LDAP**   |
| server.                          | - `config.json` setting:          |
|                                  |   `LdapSettings` \> `LdapPort` \> |
| Numerical input. Default is      |   `389`                           |
| **389**.                         | - Environment variable:           |
|                                  |   `MM_LDAPSETTINGS_LDAPPORT`      |
+----------------------------------+-----------------------------------+

#### Bind username

+------------------------------------------------+----------------------------------+
| This is the username for the account           | - System Config path:            |
| Mattermost utilizes to perform an AD/LDAP      |   **Authentication \> AD/LDAP**  |
| search. This should be an account specific to  | - `config.json` setting:         |
| Mattermost.                                    |   `LdapSettings` \>              |
|                                                |   `BindUsername`                 |
| Limit the permissions of the account to        | - Environment variable:          |
| read-only access to the portion of the AD/LDAP |   `MM_LDAPSETTINGS_BINDUSERNAME` |
| tree specified in the **Base DN** setting.     |                                  |
|                                                |                                  |
| When using Active Directory, **Bind Username** |                                  |
| should specify domain in `"DOMAIN/username"`   |                                  |
| format.                                        |                                  |
|                                                |                                  |
| String input.                                  |                                  |
+------------------------------------------------+----------------------------------+

:::: note
::: title
Note
:::

This field is required. Anonymous bind is not currently supported.
::::

#### Bind password

+--------------------------------------+----------------------------------+
| This is the password for the         | - System Config path:            |
| username given in the **Bind         |   **Authentication \> AD/LDAP**  |
| Username** setting.                  | - `config.json` setting:         |
|                                      |   `LdapSettings` \>              |
| String input.                        |   `BindPassword`                 |
|                                      | - Environment variable:          |
|                                      |   `MM_LDAPSETTINGS_BINDPASSWORD` |
+--------------------------------------+----------------------------------+

#### Connection security

+----------------------------------+----------------------------------------+
| This setting controls the type   | - System Config path: **Authentication |
| of security Mattermost uses to   |   \> AD/LDAP**                         |
| connect to the AD/LDAP server,   | - `config.json` setting:               |
| with these options:              |   `LdapSettings` \>                    |
|                                  |   `ConnectionSecurity` \> `""`         |
| - **None**: **(Default for       | - Environment variable:                |
|   self-hosted deployments)** No  |   `MM_LDAPSETTINGS_CONNECTIONSECURITY` |
|   encryption. With this option,  |                                        |
|   it is **highly recommended**   |                                        |
|   that the connection be secured |                                        |
|   outside of Mattermost, such as |                                        |
|   by a stunnel proxy.            |                                        |
|   `config.json` option: `""`     |                                        |
| - **TLS**: **(Default for Cloud  |                                        |
|   deployments)** Encrypts        |                                        |
|   communication with TLS.        |                                        |
|   `config.json` option: `"TLS"`  |                                        |
| - **STARTTLS**: Attempts to      |                                        |
|   upgrade an existing insecure   |                                        |
|   connection to a secure         |                                        |
|   connection with TLS.           |                                        |
|   `config.json` option:          |                                        |
|   `"STARTTLS"`                   |                                        |
+----------------------------------+----------------------------------------+

#### Skip certificate verification

+----------------------------------------------+-------------------------------------------------+
| - **true**: Disables the certificate         | - System Config path: **Authentication \>       |
|   verification step for TLS and STARTTLS     |   AD/LDAP**                                     |
|   connections. Use this option for testing.  | - `config.json` setting: `LdapSettings` \>      |
|   **Do not use** this option when TLS is     |   `SkipCertificateVerification` \> `false`      |
|   required in production.                    | - Environment variable:                         |
| - **false**: **(Default)** Enables           |   `MM_LDAPSETTINGS_SKIPCERTIFICATEVERIFICATION` |
|   certification verification.                |                                                 |
+----------------------------------------------+-------------------------------------------------+

#### Private key

+-------------------------------------------------+------------------------------------+
| Use this setting to upload the private key file | - System Config path:              |
| from your LDAP authentication provider, if TLS  |   **Authentication \> AD/LDAP**    |
| client certificates are the primary             | - `config.json` setting:           |
| authentication mechanism.                       |   `LdapSettings` \>                |
|                                                 |   `PrivateKeyFile`                 |
| String input.                                   | - Environment variable:            |
|                                                 |   `MM_LDAPSETTINGS_PRIVATEKEYFILE` |
+-------------------------------------------------+------------------------------------+

#### Public certificate

+------------------------------------------------+-------------------------------------------+
| Use this setting to upload the public TLS      | - System Config path: **Authentication \> |
| certificate from your LDAP authentication      |   AD/LDAP**                               |
| provider, if TLS client certificates are the   | - `config.json` setting: `LdapSettings`   |
| primary authentication mechanism.              |   \> `PublicCertificateFile`              |
|                                                | - Environment variable:                   |
| String input.                                  |   `MM_LDAPSETTINGS_PUBLICCERTIFICATEFILE` |
+------------------------------------------------+-------------------------------------------+

#### Maximum login attempts

+---------------------------------------------+------------------------------------------+
| This setting determines the number of       | - System Config path: **Authentication   |
| failed sign-in attempts a user can make     |   \> AD/LDAP**                           |
| before being locked out and required to go  | - `config.json` setting: `LdapSettings`  |
| through a password reset by email.          |   \> `MaximumLoginAttempts` \> `10`      |
|                                             | - Environment variable:                  |
| You can unlock the account in System        |   `MM_LDAPSETTINGS_MAXIMUMLOGINATTEMPTS` |
| Console on the users page. Setting this     |                                          |
| value lower than your LDAP maximum login    |                                          |
| attempts ensures that the users won\'t be   |                                          |
| locked out of your LDAP server because of   |                                          |
| failed login attempts in Mattermost.        |                                          |
|                                             |                                          |
| Numerical input. Default is **10**.         |                                          |
+---------------------------------------------+------------------------------------------+

:::: note
::: title
Note
:::

- Adjust this value to align with your organization's authentication
  policies.
- If a user\'s account is locked, you can unlock it manually by going to
  **System console \> User Management \> Users**.
::::

### User filters

Define how Mattermost identifies and filters users and groups from your
AD/LDAP directory. Use the **Test Filters** button in this section to
verify your filters work correctly before proceeding to other
configuration steps.

#### Base DN

+------------------------------------------------+----------------------------+
| This is the **Base Distinguished Name** of the | - System Config path:      |
| location in the AD/LDAP tree where Mattermost  |   **Authentication \>      |
| will start searching for users.                |   AD/LDAP**                |
|                                                | - `config.json` setting:   |
| String input.                                  |   `LdapSettings` \>        |
|                                                |   `BaseDN`                 |
|                                                | - Environment variable:    |
|                                                |   `MM_LDAPSETTINGS_BASEDN` |
+------------------------------------------------+----------------------------+

#### User filter

+----------------------------------------------------------------------------------+--------------------------------+
| This setting accepts a [general                                                  | - System Config path:          |
| syntax](https://www.ldapexplorer.com/en/manual/109010000-ldap-filter-syntax.htm) |   **Authentication \>          |
| AD/LDAP filter that is applied when searching for user objects. Only the users   |   AD/LDAP**                    |
| selected by the query can access Mattermost. For example, to filter out disabled | - `config.json` setting:       |
| users, the filter is:                                                            |   `LdapSettings` \>            |
| `(&(objectCategory=Person)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))`.   |   `UserFilter`                 |
|                                                                                  | - Environment variable:        |
| To filter by group membership, determine the `distinguishedName` of the group,   |   `MM_LDAPSETTINGS_USERFILTER` |
| then use group membership general syntax to format the filter. For example, if   |                                |
| the security group `distinguishedName` is                                        |                                |
| `CN=group1,OU=groups,DC=example,DC=com`, then the filter is:                     |                                |
| `(memberOf=CN=group1,OU=groups,DC=example,DC=com)`. The user must explicitly     |                                |
| belong to this group for the filter to apply.                                    |                                |
|                                                                                  |                                |
| String input.                                                                    |                                |
+----------------------------------------------------------------------------------+--------------------------------+

:::: note
::: title
Note
:::

This filter uses the permissions of the **Bind Username** account to
execute the search. This account should be specific to Mattermost and
have read-only access to the portion of the AD/LDAP tree specified in
the **Base DN** field.
::::

#### Group filter

+-------------------------------------------------------------------------------------+---------------------------------+
| This setting accepts a [general                                                     | - System Config path:           |
| syntax](https://www.ldapexplorer.com/en/manual/109010000-ldap-filter-syntax.htm)    |   **Authentication \> AD/LDAP** |
| AD/LDAP filter that is applied when searching for group objects. Only the groups    | - `config.json` setting:        |
| selected by the query can access Mattermost.                                        |   `LdapSettings` \>             |
|                                                                                     |   `GroupFilter`                 |
| String input. Default is                                                            | - Environment variable:         |
| `(|(objectClass=group)(objectClass=groupOfNames)(objectClass=groupOfUniqueNames))`. |   `MM_LDAPSETTINGS_GROUPFILTER` |
+-------------------------------------------------------------------------------------+---------------------------------+

:::: note
::: title
Note
:::

This filter is only used when AD/LDAP Group Sync is enabled. See
`AD/LDAP Group Sync </administration-guide/onboard/ad-ldap-groups-synchronization>`{.interpreted-text
role="doc"} for more information.
::::

#### Enable admin filter

+---------------------------------------------------+---------------------------------------+
| - **true**: Enables the **Admin Filter** setting  | - System Config path:                 |
|   that designates system admins using an AD/LDAP  |   **Authentication \> AD/LDAP**       |
|   filter.                                         | - `config.json` setting:              |
| - **false**: **(Default)** Disables the **Admin   |   `LdapSettings` \>                   |
|   Filter** setting.                               |   `EnableAdminFilter` \> `false`      |
|                                                   | - Environment variable:               |
|                                                   |   `MM_LDAPSETTINGS_ENABLEADMINFILTER` |
+---------------------------------------------------+---------------------------------------+

:::: note
::: title
Note
:::

If this setting is `false`, no additional users are designated as system
admins by the filter. Users that were previously designated as system
admins retain this role unless the filter is changed or removed.
::::

#### Admin filter

+----------------------------------------------------+---------------------------------+
| This setting accepts an AD/LDAP filter that        | - System Config path:           |
| designates the selected users as system admins.    |   **Authentication \> AD/LDAP** |
| Users are promoted to this role on their next      | - `config.json` setting:        |
| sign-in or on the next scheduled AD/LDAP sync.     |   `LdapSettings` \>             |
|                                                    |   `AdminFilter`                 |
| If the Admin Filter is removed, users who are      | - Environment variable:         |
| currently logged in retain their Admin role until  |   `MM_LDAPSETTINGS_ADMINFILTER` |
| their next sign-in.                                |                                 |
|                                                    |                                 |
| String input.                                      |                                 |
+----------------------------------------------------+---------------------------------+

#### Guest filter

+-----------------------------------------------------------------------------------+---------------------------------+
| This setting accepts an AD/LDAP filter to apply when searching for external users | - System Config path:           |
| with Guest Access to Mattermost. Only users selected by the query can access      |   **Authentication \> AD/LDAP** |
| Mattermost as Guests.                                                             | - `config.json` setting:        |
|                                                                                   |   `LdapSettings` \>             |
| See                                                                               |   `GuestFilter`                 |
| `Guest Accounts </administration-guide/onboard/guest-accounts>`{.interpreted-text | - Environment variable:         |
| role="doc"} for more information.                                                 |   `MM_LDAPSETTINGS_GUESTFILTER` |
|                                                                                   |                                 |
| String input.                                                                     |                                 |
+-----------------------------------------------------------------------------------+---------------------------------+

### Account synchronization

Map AD/LDAP user attributes to Mattermost user profile fields. Use the
**Test Attributes** button in this section to verify correct attribute
mapping and data synchronization before proceeding to other
configuration steps.

#### ID attribute

+------------------------------------------+---------------------------------+
| This is the attribute in the AD/LDAP     | - System Config path:           |
| server that is serves as a unique user   |   **Authentication \> AD/LDAP** |
| identifier in Mattermost.                | - `config.json` setting:        |
|                                          |   `LdapSettings` \>             |
| The attribute should have a unique value |   `IdAttribute`                 |
| that does not change, such as            | - Environment variable:         |
| `objectGUID` or `entryUUID`. Confirm     |   `MM_LDAPSETTINGS_IDATTRIBUTE` |
| that these attributes are available in   |                                 |
| your environment before making any       |                                 |
| changes.                                 |                                 |
|                                          |                                 |
| String input.                            |                                 |
+------------------------------------------+---------------------------------+

:::: note
::: title
Note
:::

If a user\'s ID Attribute changes, a new Mattermost account is created
that is not associated with the previous account. If you need to change
this field after users have signed-in, use the
`mmctl ldap idmigrate <administration-guide/manage/mmctl-command-line-tool:mmctl ldap idmigrate>`{.interpreted-text
role="ref"} command.
::::

#### Login ID attribute

+--------------------------------------------------+--------------------------------------+
| This is the attribute in the AD/LDAP server that | - System Config path:                |
| is used for signing-in to Mattermost. This is    |   **Authentication \> AD/LDAP**      |
| normally the same as the **Username Attribute**. | - `config.json` setting:             |
|                                                  |   `LdapSettings` \>                  |
| If your team uses `domain\username` to sign-in   |   `LoginIdAttribute`                 |
| to other services with AD/LDAP, you may enter    | - Environment variable:              |
| `domain\username` in this field to maintain      |   `MM_LDAPSETTINGS_LOGINIDATTRIBUTE` |
| consistency between sites.                       |                                      |
|                                                  |                                      |
| String input.                                    |                                      |
+--------------------------------------------------+--------------------------------------+

#### Username attribute

+-------------------------------------------------------+---------------------------------------+
| This is the attribute in the AD/LDAP server that      | - System Config path:                 |
| populates the username field in Mattermost.           |   **Authentication \> AD/LDAP**       |
|                                                       | - `config.json` setting:              |
| This attribute identifies users in the UI. For        |   `LdapSettings` \>                   |
| example, if a Username Attribute is set to            |   `UsernameAttribute`                 |
| `john.smith`, typing `@john` will show `@john.smith`  | - Environment variable:               |
| as an auto-complete option, and posting a message     |   `MM_LDAPSETTINGS_USERNAMEATTRIBUTE` |
| with `@john.smith` will send a notification to that   |                                       |
| user.                                                 |                                       |
|                                                       |                                       |
| This is normally the same as the **Login ID           |                                       |
| Attribute**, but it can be mapped to a different      |                                       |
| attribute.                                            |                                       |
|                                                       |                                       |
| String input.                                         |                                       |
+-------------------------------------------------------+---------------------------------------+

#### Email attribute

+----------------------------------------------+------------------------------------+
| This is the attribute in AD/LDAP server that | - System Config path:              |
| populates the email address field in         |   **Authentication \> AD/LDAP**    |
| Mattermost.                                  | - `config.json` setting            |
|                                              |   `LdapSettings` \>                |
| Email notifications are sent to this         |   `EmailAttribute`                 |
| address. The address may be seen by other    | - Environment variable:            |
| Mattermost users depending on privacy        |   `MM_LDAPSETTINGS_EMAILATTRIBUTE` |
| settings.                                    |                                    |
|                                              |                                    |
| String input.                                |                                    |
+----------------------------------------------+------------------------------------+

#### First name attribute

+----------------------------------------------------------------------------------------+----------------------------------------+
| This is the attribute in the AD/LDAP server that populates the first name field in     | - System Config path: **Authentication |
| Mattermost.                                                                            |   \> AD/LDAP**                         |
|                                                                                        | - `config.json` setting:               |
| When set, users cannot edit their first name.                                          |   `LdapSettings` \>                    |
|                                                                                        |   `FirstNameAttribute`                 |
| When not set, users can edit their first name in their                                 | - Environment variable:                |
| `profile settings </end-user-guide/preferences/manage-your-profile>`{.interpreted-text |   `MM_LDAPSETTINGS_FIRSTNAMEATTRIBUTE` |
| role="doc"}.                                                                           |                                        |
|                                                                                        |                                        |
| String input.                                                                          |                                        |
+----------------------------------------------------------------------------------------+----------------------------------------+

#### Last name attribute

+----------------------------------------------------------------------------------------+---------------------------------------+
| This is the attribute in the AD/LDAP server that populates the last name field in      | - System Config path:                 |
| Mattermost.                                                                            |   **Authentication \> AD/LDAP**       |
|                                                                                        | - `config.json` setting:              |
| When set, users cannot edit their last name.                                           |   `LdapSettings` \>                   |
|                                                                                        |   `LastNameAttribute`                 |
| When not set, users can edit their last name as part of their                          | - Environment variable:               |
| `profile settings </end-user-guide/preferences/manage-your-profile>`{.interpreted-text |   `MM_LDAPSETTINGS_LASTNAMEATTRIBUTE` |
| role="doc"}. \|                                                                        |                                       |
|                                                                                        |                                       |
| String input.                                                                          |                                       |
+----------------------------------------------------------------------------------------+---------------------------------------+

#### Nickname attribute

+----------------------------------------------------------------------------------------+---------------------------------------+
| This is the attribute in the AD/LDAP server that populates the nickname field in       | - System Config path:                 |
| Mattermost.                                                                            |   **Authentication \> AD/LDAP**       |
|                                                                                        | - `config.json` setting:              |
| When set, users cannot edit their nickname.                                            |   `LdapSettings` \>                   |
|                                                                                        |   `NicknameAttribute`                 |
| When not set, users can edit their nickname as part of their                           | - Environment variable:               |
| `profile settings </end-user-guide/preferences/manage-your-profile>`{.interpreted-text |   `MM_LDAPSETTINGS_NICKNAMEATTRIBUTE` |
| role="doc"}.                                                                           |                                       |
|                                                                                        |                                       |
| String input.                                                                          |                                       |
+----------------------------------------------------------------------------------------+---------------------------------------+

#### Position attribute

+----------------------------------------------------------------------------------------+---------------------------------------+
| This is the attribute in the AD/LDAP server that populates the position field in       | - System Config path:                 |
| Mattermost.                                                                            |   **Authentication \> AD/LDAP**       |
|                                                                                        | - `config.json` setting:              |
| When set, users cannot edit their position.                                            |   `LdapSettings` \>                   |
|                                                                                        |   `PositionAttribute`                 |
| When not set, users can edit their position as part of their                           | - Environment variable:               |
| `profile settings </end-user-guide/preferences/manage-your-profile>`{.interpreted-text |   `MM_LDAPSETTINGS_POSITIONATTRIBUTE` |
| role="doc"}.                                                                           |                                       |
|                                                                                        |                                       |
| String input.                                                                          |                                       |
+----------------------------------------------------------------------------------------+---------------------------------------+

#### Profile picture attribute

+-----------------------------------------+--------------------------------------+
| This is the attribute in the AD/LDAP    | - System Config path:                |
| server that syncs and locks the profile |   **Authentication \> AD/LDAP**      |
| picture in Mattermost.                  | - `config.json` setting:             |
|                                         |   `LdapSettings` \>                  |
| The image is updated when users         |   `PictureAttribute`                 |
| sign-in, not when Mattermost syncs with | - Environment variable:              |
| the AD/LDAP server.                     |   `MM_LDAPSETTINGS_PICTUREATTRIBUTE` |
|                                         |                                      |
| The image is not updated if the         |                                      |
| Mattermost image already matches the    |                                      |
| AD/LDAP image.                          |                                      |
|                                         |                                      |
| String input.                           |                                      |
+-----------------------------------------+--------------------------------------+

### Group synchronization

Configure group mapping for AD/LDAP group synchronization. Use the
**Test Group Attributes** button in this section to verify proper group
attribute mapping before proceeding to other configuration steps.

#### Group display name attribute

+----------------------------+-----------------------------------------------+
| This is the AD/LDAP Group  | - System Config path: **Authentication \>     |
| Display name attribute     |   AD/LDAP**                                   |
| that populates the         | - `config.json` setting: `LdapSettings` \>    |
| Mattermost group name      |   `GroupDisplayNameAttribute`                 |
| field.                     | - Environment variable:                       |
|                            |   `MM_LDAPSETTINGS_GROUPDISPLAYNAMEATTRIBUTE` |
| String input.              |                                               |
+----------------------------+-----------------------------------------------+

:::: note
::: title
Note
:::

This attribute is only used when AD/LDAP Group Sync is enabled and it is
**required**. See the
`AD/LDAP Group Sync documentation </administration-guide/onboard/ad-ldap-groups-synchronization>`{.interpreted-text
role="doc"} for more information.
::::

#### Group ID attribute

+--------------------------------+--------------------------------------+
| This is an AD/LDAP Group ID    | - System Config path:                |
| attribute that sets a unique   |   **Authentication \> AD/LDAP**      |
| identifier for groups.         | - `config.json` setting:             |
|                                |   `LdapSettings` \>                  |
| This should be a value that    |   `GroupIdAttribute`                 |
| does not change, such as       | - Environment variable:              |
| `entryUUID` or `objectGUID`.   |   `MM_LDAPSETTINGS_GROUPIDATTRIBUTE` |
|                                |                                      |
| String input.                  |                                      |
+--------------------------------+--------------------------------------+

:::: note
::: title
Note
:::

This attribute is only used when AD/LDAP Group Sync is enabled and it is
**required**. See the
`AD/LDAP Group Sync documentation </administration-guide/onboard/ad-ldap-groups-synchronization>`{.interpreted-text
role="doc"} for more information.
::::

### Synchronization performance

Configure timing and performance settings for AD/LDAP synchronization.
These settings control how often Mattermost syncs with your AD/LDAP
server.

#### Synchronization interval (minutes)

+------------------------------------------+-----------------------------------------+
| This value determines how often          | - System Config path: **Authentication  |
| Mattermost syncs with the AD/LDAP server |   \> AD/LDAP**                          |
| by setting the number of minutes between | - `config.json` setting: `LdapSettings` |
| each sync.                               |   \> `SyncIntervalMinutes` \> `60`      |
|                                          | - Environment variable:                 |
| Syncing with the AD/LDAP server will     |   `MM_LDAPSETTINGS_SYNCINTERVALMINUTES` |
| update Mattermost accounts to match any  |                                         |
| changes made to AD/LDAP attributes.      |                                         |
|                                          |                                         |
| Disabled AD/LDAP accounts become         |                                         |
| deactivated users in Mattermost, and any |                                         |
| active sessions are revoked.             |                                         |
|                                          |                                         |
| Use the **AD/LDAP Synchronize Now**      |                                         |
| button to immediately revoke a session   |                                         |
| after disabling an AD/LDAP account.      |                                         |
|                                          |                                         |
| Numerical input. Default is **60**.      |                                         |
+------------------------------------------+-----------------------------------------+

:::: note
::: title
Note
:::

LDAP syncs require a large number of database read queries. Monitor
database load and adjust the sync interval to minimize performance
degradation.
::::

#### Maximum page size

+--------------------------------------------+---------------------------------+
| This setting paginates the results of      | - System Config path:           |
| AD/LDAP server queries. Use this setting   |   **Authentication \> AD/LDAP** |
| if your AD/LDAP server has a page size     | - `config.json` setting:        |
| limit.                                     |   `LdapSettings` \>             |
|                                            |   `MaxPageSize` \> `0`          |
| The recommended setting is **1500**. This  | - Environment variable:         |
| is the default AD/LDAP `MaxPageSize`.      |   `MM_LDAPSETTINGS_MAXPAGESIZE` |
|                                            |                                 |
| A page size of **0** disables pagination   |                                 |
| of results.                                |                                 |
|                                            |                                 |
| Numerical input. Default is **0**.         |                                 |
+--------------------------------------------+---------------------------------+

#### Query timeout (seconds)

+-----------------------------------------------+----------------------------------+
| This setting determines the timeout period,   | - System Config path:            |
| in seconds, for AD/LDAP queries. Increase     |   **Authentication \> AD/LDAP**  |
| this value to avoid timeout errors when       | - `config.json` setting:         |
| querying a slow server.                       |   `LdapSettings` \>              |
|                                               |   `QueryTimeout` \> `60`         |
| Numerical input. Default is **60**.           | - Environment variable:          |
|                                               |   `MM_LDAPSETTINGS_QUERYTIMEOUT` |
+-----------------------------------------------+----------------------------------+

### Synchronization history

View synchronization status and manually trigger AD/LDAP
synchronization. This section includes the **AD/LDAP Synchronize Now**
button for immediate synchronization.

#### AD/LDAP synchronize now

+-----------------------------------------------+----------------------+
| Use this button to immediately sync with the  | - System Config      |
| AD/LDAP server.                               |   path:              |
|                                               |   **Authentication   |
| The status of the sync is displayed in the    |   \> AD/LDAP**       |
| table underneath the button (see the figure   | - `config.json`      |
| below).                                       |   setting: N/A       |
|                                               | - Environment        |
| Following a manual sync, the next sync will   |   variable: N/A      |
| occur after the time set in the               |                      |
| **Synchronization Interval**.                 |                      |
+-----------------------------------------------+----------------------+

:::: note
::: title
Note
:::

If a sync is `Pending` and does not complete, check that **Enable
Synchronization with AD/LDAP** is set to `true`.
::::

![](../../images/ldap-sync-table.png){alt="An example screenshot of an AD/LDAP Synchronization table in the Mattermost System Console."}

### Config settings not available in the AD/LDAP Wizard

The following AD/LDAP configuration settings are available in the
`config.json` file only and aren\'t available via the AD/LDAP wizard
interface in the System Console.

#### Re-add removed members on sync

+----------------------------------+-----------------------------------------+
| Enable this setting to re-add    | - System Config path: **Authentication  |
| members of the LDAP group that   |   \> AD/LDAP**                          |
| were previously removed from     | - `config.json` setting: `LdapSettings` |
| group-synchronized teams or      |   \> `ReAddRemovedMembers`              |
| channels during LDAP             | - Environment variable:                 |
| synchronization.                 |   `MM_LDAPSETTINGS_READDREMOVEDMEMBERS` |
|                                  |                                         |
| - **true**: Members of the LDAP  |                                         |
|   group who were previously      |                                         |
|   removed are re-added to        |                                         |
|   group-synchronized teams or    |                                         |
|   channels during LDAP           |                                         |
|   synchronization.               |                                         |
| - **false**: **(Default)**       |                                         |
|   Members of the LDAP group who  |                                         |
|   were previously removed are    |                                         |
|   not re-added to                |                                         |
|   group-synchronized teams or    |                                         |
|   channels during LDAP           |                                         |
|   synchronization.               |                                         |
+----------------------------------+-----------------------------------------+

:::: note
::: title
Note
:::

The
`mmctl ldap sync <administration-guide/manage/mmctl-command-line-tool:mmctl ldap sync>`{.interpreted-text
role="ref"} command takes precedence over this server configuration
setting. If you have this setting disabled, and run the mmctl command
with the `--include-removed-members` flag, removed members will be
re-added during LDAP synchronization.
::::

::: {#saml-enterprise}

------------------------------------------------------------------------
:::

## SAML 2.0

Access the following configuration settings in the System Console by
going to **Authentication \> SAML 2.0**.

See the encryption options documentation for details on what
`encryption methods <deployment-guide/encryption-options:saml encryption support>`{.interpreted-text
role="ref"} Mattermost supports for SAML.

:::: important
::: title
Important
:::

In line with Microsoft ADFS guidance, we recommend [configuring intranet
forms-based authentication for devices that do not support
WIA](https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia).
::::

### Enable login with SAML

+------------------------------------------------------------------------------------+----------------------------+
| - **true**: Enables sign-in with SAML. See                                         | - System Config path:      |
|   `SAML Single Sign-On </administration-guide/onboard/sso-saml>`{.interpreted-text |   **Authentication \> SAML |
|   role="doc"} to learn more.                                                       |   2.0**                    |
| - **false**: **(Default)** Disables sign-in with SAML.                             | - `config.json` setting:   |
|                                                                                    |   `SamlSettings` \>        |
|                                                                                    |   `Enable` \> `false`      |
|                                                                                    | - Environment variable:    |
|                                                                                    |   `MM_SAMLSETTINGS_ENABLE` |
+------------------------------------------------------------------------------------+----------------------------+

### Enable synchronizing SAML accounts with AD/LDAP

+----------------------------------------+----------------------------------------+
| - **true**: Mattermost updates         | - System Config path: **Authentication |
|   configured Mattermost user           |   \> SAML 2.0**                        |
|   attributes (ex. FirstName, Position, | - `config.json` setting:               |
|   Email) with their values from        |   `SamlSettings` \>                    |
|   AD/LDAP. From v10.9, Mattermost      |   `EnableSyncWithLdap` \> `false`      |
|   checks whether a user exists on the  | - Environment variable:                |
|   connected LDAP server during login.  |   `MM_SAMLSETTINGS_ENABLESYNCWITHLDAP` |
|   If the user doesn\'t exist on the    |                                        |
|   LDAP server, login fails.            |                                        |
| - **false**: **(Default)** Disables    |                                        |
|   syncing of SAML-authenticated        |                                        |
|   Mattermost users with AD/LDAP. From  |                                        |
|   Mattermost v10.9, Mattermost         |                                        |
|   doesn\'t check whether a user exists |                                        |
|   on the connected LDAP server during  |                                        |
|   login.                               |                                        |
+----------------------------------------+----------------------------------------+

:::: note
::: title
Note
:::

- AD/LDAP synchronization must be enabled and configured through the
  settings under **Authentication \> AD/LDAP**.
- Prior to Mattermost v10.9, users not present on the LDAP server could
  log in, but would be deactivated on the next LDAP sync.
- See
  `AD/LDAP Setup </administration-guide/onboard/ad-ldap>`{.interpreted-text
  role="doc"} to learn more about configuring AD/LDAP.
::::

### Ignore guest users when synchronizing with AD/LDAP

+------------------------------------+------------------------------------------+
| - **true**: When syncing with the  | - System Config path: **Authentication   |
|   AD/LDAP server, Mattermost does  |   \> SAML 2.0**                          |
|   not sync any information about   | - `config.json` setting: `SamlSettings`  |
|   SAML-authenticated Guest Users   |   \> `IgnoreGuestsLdapSync` \> `false`   |
|   from the AD/LDAP server. Manage  | - Environment variable:                  |
|   guest deactivation manually via  |   `MM_SAMLSETTINGS_IGNOREGUESTSLDAPSYNC` |
|   **System Console \> Users**.     |                                          |
| - **false**: **(Default)** Syncing |                                          |
|   Mattermost with the AD/LDAP      |                                          |
|   server updates Guest User        |                                          |
|   attributes and deactivates and   |                                          |
|   removes SAML-authenticated       |                                          |
|   accounts for Guest Users that    |                                          |
|   are no longer active on the      |                                          |
|   AD/LDAP server.                  |                                          |
+------------------------------------+------------------------------------------+

For more information, see
`AD/LDAP Setup </administration-guide/onboard/ad-ldap>`{.interpreted-text
role="doc"} for details.

### Override SAML bind data with AD/LDAP information

+----------------------------------------+---------------------------------------------------+
| - **true**: If the SAML ID attribute   | - System Config path: **Authentication \> SAML    |
|   is configured, Mattermost overrides  |   2.0**                                           |
|   the SAML ID attribute with the       | - `config.json` setting: `SamlSettings` \>        |
|   AD/LDAP ID attribute. If the SAML ID |   `EnableSyncWithLdapIncludeAuth` \> `false`      |
|   attribute is not present, Mattermost | - Environment variable:                           |
|   overrides the SAML Email attribute   |   `MM_SAMLSETTINGS_ENABLESYNCWITHLDAPINCLUDEAUTH` |
|   with the AD/LDAP Email attribute.    |                                                   |
| - **false**: **(Default)** Mattermost  |                                                   |
|   uses the email attribute to bind     |                                                   |
|   users to SAML.                       |                                                   |
|                                        |                                                   |
| This setting is only available when    |                                                   |
| SAML authentication is enabled and     |                                                   |
| AD/LDAP synchronization is enabled.    |                                                   |
+----------------------------------------+---------------------------------------------------+

:::: note
::: title
Note
:::

\- This setting should be **false** unless LDAP sync is enabled.
Changing this setting from **true** to **false** will disable the
override. - SAML IDs must match LDAP IDs when the override is enabled. -
For more information, see
`AD/LDAP Setup </administration-guide/onboard/ad-ldap>`{.interpreted-text
role="doc"} for details.
::::

### Identity provider metadata URL

+---------------------------------------+------------------------------------+
| This setting is the URL from which    | - System Config path:              |
| Mattermost requests setup metadata    |   **Authentication \> SAML 2.0**   |
| from the provider.                    | - `config.json` setting:           |
|                                       |   `SamlSettings` \>                |
| String input.                         |   `IdpMetadataURL`                 |
|                                       | - Environment variable:            |
|                                       |   `MM_SAMLSETTINGS_IDPMETADATAURL` |
+---------------------------------------+------------------------------------+

### SAML SSO URL

+-------------------------------------------+----------------------------+
| This setting is the URL where Mattermost  | - System Config path:      |
| sends a SAML request to start the login   |   **Authentication \> SAML |
| sequence.                                 |   2.0**                    |
|                                           | - `config.json` setting:   |
| String input.                             |   `SamlSettings` \>        |
|                                           |   `IdpURL`                 |
|                                           | - Environment variable:    |
|                                           |   `MM_SAMLSETTINGS_IDPURL` |
+-------------------------------------------+----------------------------+

### Identity provider issuer URL

+------------------------------------+--------------------------------------+
| This setting is the issuer URL for | - System Config path:                |
| the Identity Provider for SAML     |   **Authentication \> SAML 2.0**     |
| requests.                          | - `config.json` setting:             |
|                                    |   `SamlSettings` \>                  |
| String input.                      |   `IdpDescriptorURL`                 |
|                                    | - Environment variable:              |
|                                    |   `MM_SAMLSETTINGS_IDPDESCRIPTORURL` |
+------------------------------------+--------------------------------------+

### Identity provider public certificate

+----------------------------------+----------------------------------------+
| The public authentication        | - System Config path: **Authentication |
| certificate issued by your       |   \> SAML 2.0**                        |
| Identity Provider.               | - `config.json` setting:               |
|                                  |   `SamlSettings` \>                    |
| String input.                    |   `IdpCertificateFile`                 |
|                                  | - Environment variable:                |
|                                  |   `MM_SAMLSETTINGS_IDPCERTIFICATEFILE` |
+----------------------------------+----------------------------------------+

### Verify signature

+---------------------------------------------+----------------------------+
| - **true**: **(Default)** Mattermost checks | - System Config path:      |
|   that the SAML Response signature matches  |   **Authentication \> SAML |
|   the Service Provider Login URL.           |   2.0**                    |
| - **false**: The signature is not verified. | - `config.json` setting:   |
|   This is **not recommended** for           |   `SamlSettings` \>        |
|   production. Use this option for testing   |   `Verify` \> `true`       |
|   only.                                     | - Environment variable:    |
|                                             |   `MM_SAMLSETTINGS_VERIFY` |
+---------------------------------------------+----------------------------+

### Service provider login URL

+-----------------------------------------+-------------------------------------------------+
| Enter the URL of your Mattermost        | - System Config path: **Authentication \> SAML  |
| server, followed by `/login/sso/saml`,  |   2.0**                                         |
| i.e.                                    | - `config.json` setting: `SamlSettings` \>      |
| `https://example.com/login/sso/saml`.   |   `AssertionConsumerServiceURL`                 |
|                                         | - Environment variable:                         |
| Use HTTP or HTTPS depending on the      |   `MM_SAMLSETTINGS_ASSERTIONCONSUMERSERVICEURL` |
| configuration of the server.            |                                                 |
|                                         |                                                 |
| This setting is also known as the       |                                                 |
| Assertion Consumer Service URL.         |                                                 |
+-----------------------------------------+-------------------------------------------------+

### Service provider identifier

+-------------------------------------------------+-----------------------------------------------+
| This setting is the unique identifier for the   | - System Config path: **Authentication \>     |
| Service Provider, which in most cases is the    |   SAML 2.0**                                  |
| same as the Service Provider Login URL. In      | - `config.json` setting: `SamlSettings` \>    |
| ADFS, this must match the Relying Party         |   `ServiceProviderIdentifier`                 |
| Identifier.                                     | - Environment variable:                       |
|                                                 |   `MM_SAMLSETTINGS_SERVICEPROVIDERIDENTIFIER` |
| String input.                                   |                                               |
+-------------------------------------------------+-----------------------------------------------+

### Enable encryption

+----------------------------------------------+-----------------------------+
| - **true**: **(Default)** Mattermost will    | - System Config path:       |
|   decrypt SAML Assertions that are encrypted |   **Authentication \> SAML  |
|   with your Service Provider Public          |   2.0**                     |
|   Certificate.                               | - `config.json` setting:    |
| - **false**: Mattermost does not decrypt     |   `SamlSettings` \>         |
|   SAML Assertions. Use this option for       |   `Encrypt` \> `true`       |
|   testing only. It is **not recommended**    | - Environment variable:     |
|   for production.                            |   `MM_SAMLSETTINGS_ENCRYPT` |
+----------------------------------------------+-----------------------------+

### Service provider private key

+----------------------------------------+------------------------------------+
| This setting stores the private key    | - System Config path:              |
| used to decrypt SAML Assertions from   |   **Authentication \> SAML 2.0**   |
| the Identity Provider.                 | - `config.json` setting:           |
|                                        |   `SamlSettings` \>                |
| String input.                          |   `PrivateKeyFile`                 |
|                                        | - Environment variable:            |
|                                        |   `MM_SAMLSETTINGS_PRIVATEKEYFILE` |
+----------------------------------------+------------------------------------+

### Service provider public certificate

+-------------------------------------------------+-------------------------------------------+
| This setting stores the certificate file used   | - System Config path: **Authentication \> |
| to sign a SAML request to the Identity Provider |   SAML 2.0**                              |
| for a SAML login when Mattermost is initiating  | - `config.json` setting: `SamlSettings`   |
| the login as the Service Provider.              |   \> `PublicCertificateFile`              |
|                                                 | - Environment variable:                   |
| String input.                                   |   `MM_SAMLSETTINGS_PUBLICCERTIFICATEFILE` |
+-------------------------------------------------+-------------------------------------------+

### Sign request

+---------------------------------------+---------------------------------+
| - **true**: Mattermost signs the SAML | - System Config path:           |
|   request with the Service Provider   |   **Authentication \> SAML      |
|   Private Key.                        |   2.0**                         |
| - **false**: Mattermost does not sign | - `config.json` setting:        |
|   the SAML request.                   |   `SamlSettings` \>             |
|                                       |   `SignRequest`                 |
|                                       | - Environment variable:         |
|                                       |   `MM_SAMLSETTINGS_SIGNREQUEST` |
+---------------------------------------+---------------------------------+

### Signature algorithm

+----------------------------------------------+----------------------------------------+
| This setting determines the signature        | - System Config path: **Authentication |
| algorithm used to sign the SAML request.     |   \> SAML 2.0**                        |
| Options are: `RSAwithSHA1`, `RSAwithSHA256`, | - `config.json` setting:               |
| `RSAwithSHA512`.                             |   `SamlSettings` \>                    |
|                                              |   `SignatureAlgorithm`                 |
| String input.                                | - Environment variable:                |
|                                              |   `MM_SAMLSETTINGS_SIGNATUREALGORITHM` |
| :::: note                                    |                                        |
| ::: title                                    |                                        |
| Note                                         |                                        |
| :::                                          |                                        |
|                                              |                                        |
| From Mattermost v11, the default signature   |                                        |
| algorithm has been updated from              |                                        |
| `RSAwithSHA1` to `RSAwithSHA256` for         |                                        |
| improved security. Existing configurations   |                                        |
| will continue to work, but new installations |                                        |
| will default to `RSAwithSHA256`.             |                                        |
| ::::                                         |                                        |
+----------------------------------------------+----------------------------------------+

### Canonical algorithm

+---------------------------------------------------------------------+----------------------------------------+
| This setting determines the canonicalization algorithm. With these  | - System Config path: **Authentication |
| options:                                                            |   \> SAML 2.0**                        |
|                                                                     | - `config.json` setting:               |
| - **Canonical1.0**: **(Default)** [Exclusive XML Canonicalization   |   `SamlSettings` \>                    |
|   1.0 (omit                                                         |   `CanonicalAlgorithm`                 |
|   comments)](https://www.w3.org/TR/2002/REC-xml-exc-c14n-20020718/) | - Environment variable:                |
|   (`http://www.w3.org/2001/10/xml-exc-c14n#`). `config.json`        |   `MM_SAMLSETTINGS_CANONICALALGORITHM` |
|   setting: `Canonical1.0`.                                          |                                        |
| - **Canonical1.1**: [Canonical XML 1.1 (omit                        |                                        |
|   comments)](https://www.w3.org/TR/2008/REC-xml-c14n11-20080502/)   |                                        |
|   (`http://www.w3.org/2006/12/xml-c14n11`). `config.json` setting:  |                                        |
|   `Canonical1.1`.                                                   |                                        |
|                                                                     |                                        |
| String input.                                                       |                                        |
+---------------------------------------------------------------------+----------------------------------------+

### Email attribute

+------------------------------------------------+------------------------------------+
| This setting determines the attribute from the | - System Config path:              |
| SAML Assertion that populates the user email   |   **Authentication \> SAML 2.0**   |
| address field in Mattermost.                   | - `config.json` setting:           |
|                                                |   `SamlSettings` \>                |
| Notifications are sent to this email address.  |   `EmailAttribute`                 |
| This email address may be visible to other     | - Environment variable:            |
| users, depending on how the system admin has   |   `MM_SAMLSETTINGS_EMAILATTRIBUTE` |
| set-up user privacy.                           |                                    |
|                                                |                                    |
| String input.                                  |                                    |
+------------------------------------------------+------------------------------------+

### Username attribute

+------------------------------------------------------+---------------------------------------+
| This setting determines the SAML Assertion attribute | - System Config path:                 |
| that populates the username field in the Mattermost  |   **Authentication \> SAML 2.0**      |
| UI.                                                  | - `config.json` setting:              |
|                                                      |   `SamlSettings` \>                   |
| This attribute identifies users in the UI. For       |   `UsernameAttribute`                 |
| example, if a username is set to `john.smith`,       | - Environment variable:               |
| typing `@john` will show `@john.smith` as an         |   `MM_SAMLSETTINGS_USERNAMEATTRIBUTE` |
| auto-complete option, and posting a message with     |                                       |
| `@john.smith` will send a notification to that user. |                                       |
|                                                      |                                       |
| String input.                                        |                                       |
+------------------------------------------------------+---------------------------------------+

### Id attribute

+----------------------------------------------+---------------------------------+
| (Optional) This setting determines the SAML  | - System Config path:           |
| Assertion attribute used to bind users from  |   **Authentication \> SAML      |
| SAML to users in Mattermost.                 |   2.0**                         |
|                                              | - `config.json` setting:        |
| String input.                                |   `SamlSettings` \>             |
|                                              |   `IdAttribute`                 |
|                                              | - Environment variable:         |
|                                              |   `MM_SAMLSETTINGS_IDATTRIBUTE` |
+----------------------------------------------+---------------------------------+

### Guest attribute

+-------------------------------------------------------------------------------------------------+------------------------------------+
| (Optional) This setting determines the SAML Assertion attribute used to apply a Guest role to   | - System Config path:              |
| users in Mattermost.                                                                            |   **Authentication \> SAML 2.0**   |
|                                                                                                 | - `config.json` setting:           |
| See the                                                                                         |   `SamlSettings` \>                |
| `Guest Accounts documentation </administration-guide/onboard/guest-accounts>`{.interpreted-text |   `GuestAttribute`                 |
| role="doc"} for more information.                                                               | - Environment variable:            |
|                                                                                                 |   `MM_SAMLSETTINGS_GUESTATTRIBUTE` |
| String input.                                                                                   |                                    |
+-------------------------------------------------------------------------------------------------+------------------------------------+

### Enable admin attribute

+---------------------------------------+------------------------------------------+
| - **true**: System admin status is    | - System Config path: **Authentication   |
|   determined by the SAML Assertion    |   \> SAML 2.0**                          |
|   attribute set in **Admin            | - `config.json` setting: `SamlSettings`  |
|   attribute**.                        |   \> `EnableAdminAttribute` \> `false`   |
| - **false**: **(Default)** System     | - Environment variable:                  |
|   admin status is **not** determined  |   `MM_SAMLSETTINGS_ENABLEADMINATTRIBUTE` |
|   by the SAML Assertion attribute.    |                                          |
+---------------------------------------+------------------------------------------+

### Admin attribute

+---------------------------------------------+------------------------------------+
| (Optional) This setting determines the      | - System Config path:              |
| attribute in the SAML Assertion for         |   **Authentication \> SAML 2.0**   |
| designating system admins.                  | - `config.json` setting:           |
|                                             |   `SamlSettings` \>                |
| Users are automatically promoted to this    |   `AdminAttribute`                 |
| role when logging in to Mattermost.         | - Environment variable:            |
|                                             |   `MM_SAMLSETTINGS_ADMINATTRIBUTE` |
| If the Admin attribute is removed, users    |                                    |
| that are logged in retain Admin status. The |                                    |
| role is revoked only when users log out.    |                                    |
|                                             |                                    |
| String input.                               |                                    |
+---------------------------------------------+------------------------------------+

### First name attribute

+-------------------------------------------+----------------------------------------+
| (Optional) This setting determines the    | - System Config path: **Authentication |
| SAML Assertion attribute that populates   |   \> SAML 2.0**                        |
| the first name of users in Mattermost.    | - `config.json` setting:               |
|                                           |   `SamlSettings` \>                    |
| String input.                             |   `FirstNameAttribute`                 |
|                                           | - Environment variable:                |
|                                           |   `MM_SAMLSETTINGS_FIRSTNAMEATTRIBUTE` |
+-------------------------------------------+----------------------------------------+

### Last name attribute

+-------------------------------------------+---------------------------------------+
| (Optional) This setting determines the    | - System Config path:                 |
| SAML Assertion attribute that populates   |   **Authentication \> SAML 2.0**      |
| the last name of users in Mattermost.     | - `config.json` setting:              |
|                                           |   `SamlSettings` \>                   |
| String input.                             |   `LastNameAttribute`                 |
|                                           | - Environment variable:               |
|                                           |   `MM_SAMLSETTINGS_LASTNAMEATTRIBUTE` |
+-------------------------------------------+---------------------------------------+

### Nickname attribute

+-------------------------------------------+---------------------------------------+
| (Optional) This setting determines the    | - System Config path:                 |
| SAML Assertion attribute that populates   |   **Authentication \> SAML 2.0**      |
| the nickname of users in Mattermost.      | - `config.json` setting:              |
|                                           |   `SamlSettings` \>                   |
| String input.                             |   `NicknameAttribute`                 |
|                                           | - Environment variable:               |
|                                           |   `MM_SAMLSETTINGS_NICKNAMEATTRIBUTE` |
+-------------------------------------------+---------------------------------------+

### Position attribute

+-----------------------------------------------+---------------------------------------+
| (Optional) This setting determines the SAML   | - System Config path:                 |
| Assertion attribute that populates the        |   **Authentication \> SAML 2.0**      |
| position (job title or role at company) of    | - `config.json` setting:              |
| users in Mattermost.                          |   `SamlSettings` \>                   |
|                                               |   `PositionAttribute`                 |
| String input.                                 | - Environment variable:               |
|                                               |   `MM_SAMLSETTINGS_POSITIONATTRIBUTE` |
+-----------------------------------------------+---------------------------------------+

### Preferred language attribute

+----------------------------------------------+-------------------------------------+
| (Optional) This setting determines the SAML  | - System Config path:               |
| Assertion attribute that populates the       |   **Authentication \> SAML 2.0**    |
| language preference of users in Mattermost.  | - `config.json` setting:            |
|                                              |   `SamlSettings` \>                 |
| String input.                                |   `LocaleAttribute`                 |
|                                              | - Environment variable:             |
|                                              |   `MM_SAMLSETTINGS_LOCALEATTRIBUTE` |
+----------------------------------------------+-------------------------------------+

### Login button text

+-------------------------------------+-------------------------------------+
| (Optional) The text that appears in | - System Config path:               |
| the login button on the sign-in     |   **Authentication \> SAML 2.0**    |
| page.                               | - `config.json` setting:            |
|                                     |   `SamlSettings` \>                 |
| String input. Default is **SAML**.  |   `LoginButtonText`                 |
|                                     | - Environment variable:             |
|                                     |   `MM_SAMLSETTINGS_LOGINBUTTONTEXT` |
+-------------------------------------+-------------------------------------+

------------------------------------------------------------------------

## OAuth 2.0

Access the following configuration settings in the System Console by
going to **Authentication \> OAuth 2.0**. Settings for GitLab OAuth
authentication can also be accessed under **Authentication \> GitLab**
in self-hosted deployments.

Use these settings to configure OAuth 2.0 for account creation and
login.

### Select OAuth 2.0 service provider

+---------------------------------------------------+--------------------+
| Use this setting to enable OAuth and specify the  | - System Config    |
| service provider, with these options:             |   path:            |
|                                                   |   **Authentication |
| - **Do not allow login via an OAuth 2.0           |   \> OAuth 2.0**   |
|   provider**                                      | - `config.json`    |
| - **GitLab** (Available in all plans; see [GitLab |   setting: N/A     |
|   2.0 OAuth                                       | - Environment      |
|   settings](#gitlab-oauth-2-0-settings))          |   variable: N/A    |
| - **Google Apps** (Available in Mattermost        |                    |
|   Enterprise and Professional; see [Google OAuth  |                    |
|   2.0 settings](#google-oauth-2-0-settings))      |                    |
| - **Entra ID** (Available in Mattermost           |                    |
|   Enterprise and Professional; see [Entra ID      |                    |
|   OAuth 2.0                                       |                    |
|   settings](#entraid-oauth-2-0-settings))         |                    |
+---------------------------------------------------+--------------------+

#### GitLab OAuth 2.0 settings

:::: note
::: title
Note
:::

For Enterprise subscriptions, GitLab settings can be found under **OAuth
2.0**
::::

##### Enable OAuth 2.0 authentication with GitLab

+---------------------------------------------+------------------------------+
| - **true**: Allows team and account         | - System Config path:        |
|   creation using GitLab OAuth               |   **Authentication \> OAuth  |
|   authentication. Input the **Secret** and  |   2.0 (or GitLab)**          |
|   **ID** credentials to configure.          | - `config.json` setting:     |
| - **false**: **(Default)** Disables GitLab  |   `GitLabSettings` \>        |
|   OAuth authentication.                     |   `Enable` \> `false`        |
|                                             | - Environment variable:      |
|                                             |   `MM_GITLABSETTINGS_ENABLE` |
+---------------------------------------------+------------------------------+

##### GitLab OAuth 2.0 Application ID

+-------------------------------------------------------------+--------------------------+
| This setting holds the OAuth Application ID from GitLab.    | - System Config path:    |
| Generate the ID by these steps:                             |   **Authentication \>    |
|                                                             |   OAuth 2.0 (or          |
| 1.  Login to your GitLab account.                           |   GitLab)**              |
| 2.  Go to **Profile Settings \> Applications \> New         | - `config.json` setting: |
|     Application** and enter a name.                         |   `GitLabSettings` \>    |
| 3.  Enter the Redirect URLs:                                |   `Id`                   |
|     `https://<your-mattermost-url>/login/gitlab/complete`   | - Environment variable:  |
|     and                                                     |   `MM_GITLABSETTINGS_ID` |
|     `https://<your-mattermost-url>/signup/gitlab/complete`. |                          |
| 4.  Take the Application ID provided by GitLab and enter it |                          |
|     in the Mattermost System Console field, `config.json`   |                          |
|     setting, or Environment variable.                       |                          |
|                                                             |                          |
| String input.                                               |                          |
+-------------------------------------------------------------+--------------------------+

:::: note
::: title
Note
:::

GitLab provides the [Application Secret
Key](#gitlab-oauth-2-0-application-secret-key) along with the the ID.
::::

##### GitLab OAuth 2.0 Application secret key

+-----------------------------------------------------+------------------------------+
| This setting holds the OAuth Application Secret Key | - System Config path:        |
| from GitLab. The key is generated at the same time  |   **Authentication \> OAuth  |
| as the **Application ID** (see [GitLab OAuth 2.0    |   2.0 (or GitLab)**          |
| Application ID](#gitlab-oauth-2-0-application-id)). | - `config.json` setting:     |
|                                                     |   `GitLabSettings` \>        |
| Enter the key provided by GitLab in the Mattermost  |   `Secret`                   |
| System Console field, `config.json` setting, or     | - Environment variable:      |
| Environment variable.                               |   `MM_GITLABSETTINGS_SECRET` |
|                                                     |                              |
| String input.                                       |                              |
+-----------------------------------------------------+------------------------------+

##### GitLab OAuth 2.0 site URL

+------------------------------------------------+---------------------+
| This setting holds the URL of your GitLab      | - System Config     |
| instance, e.g. `https://example.com:3000`. Use |   path:             |
| `http://` if SSL is not enabled on your GitLab |   **Authentication  |
| instance.                                      |   \> OAuth 2.0 (or  |
|                                                |   GitLab)**         |
|                                                | - `config.json`     |
|                                                |   setting: N/A      |
|                                                | - Environment       |
|                                                |   variable: N/A     |
+------------------------------------------------+---------------------+

##### GitLab OAuth 2.0 User API endpoint

+-------------------------------------------------+---------------------------------------+
| This setting holds the URL of your GitLab User  | - System Config path:                 |
| API endpoint, e.g.                              |   **Authentication \> OAuth 2.0 (or   |
| `https://<your-gitlab-url>/api/v3/user`. Use    |   GitLab)**                           |
| `http://` if SSL is not enabled on your GitLab  | - `config.json` setting:              |
| instance.                                       |   `GitLabSettings` \>                 |
|                                                 |   `UserAPIEndpoint`                   |
| Enter the URL in the Mattermost System Console  | - Environment variable:               |
| field, `config.json` setting, or Environment    |   `MM_GITLABSETTINGS_USERAPIENDPOINT` |
| variable.                                       |                                       |
|                                                 |                                       |
| String input.                                   |                                       |
+-------------------------------------------------+---------------------------------------+

##### GitLab OAuth 2.0 Auth endpoint

+--------------------------------------------------+------------------------------------+
| This setting holds the URL of your GitLab Auth   | - System Config path:              |
| endpoint, e.g.                                   |   **Authentication \> OAuth 2.0    |
| `https://<your-gitlab-url>/oauth/authorize`. Use |   (or GitLab)**                    |
| `http://` if SSL is not enabled on your GitLab   | - `config.json` setting:           |
| instance.                                        |   `GitLabSettings` \>              |
|                                                  |   `AuthEndpoint`                   |
| Enter the URL in the Mattermost System Console   | - Environment variable:            |
| field, `config.json` setting, or Environment     |   `MM_GITLABSETTINGS_AUTHENDPOINT` |
| variable.                                        |                                    |
|                                                  |                                    |
| String input.                                    |                                    |
+--------------------------------------------------+------------------------------------+

##### GitLab OAuth 2.0 Token endpoint

+---------------------------------------------------+-------------------------------------+
| This setting holds the URL of your GitLab OAuth   | - System Config path:               |
| Token endpoint, e.g.                              |   **Authentication \> OAuth 2.0 (or |
| `https://<your-gitlab-url>/oauth/token`. Use      |   GitLab)**                         |
| `http://` if SSL is not enabled on your GitLab    | - `config.json` setting:            |
| instance.                                         |   `GitLabSettings` \>               |
|                                                   |   `TokenEndpoint`                   |
| Enter the URL in the Mattermost System Console    | - Environment variable:             |
| field, `config.json` setting, or Environment      |   `MM_GITLABSETTINGS_TOKENENDPOINT` |
| variable.                                         |                                     |
|                                                   |                                     |
| String input.                                     |                                     |
+---------------------------------------------------+-------------------------------------+

#### Google OAuth 2.0 settings

##### Enable OAuth 2.0 authentication with Google

+--------------------------------------------------------------------------------------+------------------------------+
| - **true**: Allows team and account creation using Google OAuth authentication.      | - System Config path:        |
|   Input the **Client ID** and **Client Secret** credentials to configure.            |   **Authentication \> OAuth  |
| - **false**: **(Default)** Disables Google OAuth authentication.                     |   2.0**                      |
|                                                                                      | - `config.json` setting:     |
| See                                                                                  |   `GoogleSettings` \>        |
| `Google Single Sign-On </administration-guide/onboard/sso-google>`{.interpreted-text |   `Enable` \> `false`        |
| role="doc"} implementation instructions.                                             | - Environment variable:      |
|                                                                                      |   `MM_GOOGLESETTINGS_ENABLE` |
+--------------------------------------------------------------------------------------+------------------------------+

##### Google OAuth 2.0 Client ID

+--------------------------------------------------------------------------------------+--------------------------+
| This setting stores the OAuth Client ID from Google. Generate the ID by going to the | - System Config path:    |
| **Credentials** section of the Google Cloud Platform APIs & Services menu and        |   **Authentication \>    |
| selecting **Create Credentials \> OAuth client ID**.                                 |   OAuth 2.0**            |
|                                                                                      | - `config.json` setting: |
| See                                                                                  |   `GoogleSettings` \>    |
| `Google Single Sign-On </administration-guide/onboard/sso-google>`{.interpreted-text |   `Id`                   |
| role="doc"} for instructions that can be used to implement Google OAuth or OpenID    | - Environment variable:  |
| authentication.                                                                      |   `MM_GOOGLESETTINGS_ID` |
|                                                                                      |                          |
| String input.                                                                        |                          |
+--------------------------------------------------------------------------------------+--------------------------+

##### Google OAuth 2.0 Client secret

+----------------------------------------------+------------------------------+
| This setting stores the OAuth Client Secret  | - System Config path:        |
| from Google. The Secret is generated at the  |   **Authentication \> OAuth  |
| same time as the Client ID.                  |   2.0**                      |
|                                              | - `config.json` setting:     |
| String input.                                |   `GoogleSettings` \>        |
|                                              |   `Secret`                   |
|                                              | - Environment variable:      |
|                                              |   `MM_GOOGLESETTINGS_SECRET` |
+----------------------------------------------+------------------------------+

##### Google OAuth 2.0 User API endpoint

+---------------------------------------------------------------------------------------------------+---------------------------------------+
| We recommend                                                                                      | - System Config path:                 |
| `https://people.googleapis.com/v1/people/me?personFields=names,emailAddresses,nicknames,metadata` |   **Authentication \> OAuth 2.0**     |
| as the User API Endpoint. Otherwise, enter a custom endpoint in `config.json` with HTTP, or       | - `config.json` setting:              |
| HTTPS, if available on the API server.                                                            |   `GoogleSettings` \>                 |
|                                                                                                   |   `UserAPIEndpoint`                   |
| String input.                                                                                     | - Environment variable:               |
|                                                                                                   |   `MM_GOOGLESETTINGS_USERAPIENDPOINT` |
+---------------------------------------------------------------------------------------------------+---------------------------------------+

##### Google OAuth 2.0 Auth endpoint

+----------------------------------------------------+------------------------------------+
| We recommend                                       | - System Config path:              |
| `https://accounts.google.com/o/oauth2/v2/auth` as  |   **Authentication \> OAuth 2.0**  |
| the Auth Endpoint. Otherwise, enter a custom       | - `config.json` setting:           |
| endpoint in `config.json` with HTTP, or HTTPS, if  |   `GoogleSettings` \>              |
| available on the server.                           |   `AuthEndpoint`                   |
|                                                    | - Environment variable:            |
| String input.                                      |   `MM_GOOGLESETTINGS_AUTHENDPOINT` |
+----------------------------------------------------+------------------------------------+

##### Google OAuth 2.0 Token endpoint

+---------------------------------------------------+-------------------------------------+
| We recommend                                      | - System Config path:               |
| `https://www.googleapis.com/oauth2/v4/token` as   |   **Authentication \> OAuth 2.0**   |
| the Token Endpoint. Otherwise, enter a custom     | - `config.json` setting:            |
| endpoint in `config.json` with HTTP, or HTTPS, if |   `GoogleSettings` \>               |
| available on the server.                          |   `TokenEndpoint`                   |
|                                                   | - Environment variable:             |
| String input.                                     |   `MM_GOOGLESETTINGS_TOKENENDPOINT` |
+---------------------------------------------------+-------------------------------------+

#### Entra ID OAuth 2.0 settings

:::: note
::: title
Note
:::

In line with Microsoft ADFS guidance we recommend [configuring intranet
forms-based authentication for devices that do not support
WIA](https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia).
::::

##### Enable OAuth 2.0 Authentication with Entra ID

+-------------------------------------+---------------------------------+
| - **true**: Allows team and account | - System Config path:           |
|   creation using Entra ID OAuth     |   **Authentication \> OAuth     |
|   authentication.                   |   2.0**                         |
| - **false**: **(Default)** Disables | - `config.json` setting:        |
|   Entra ID OAuth authentication.    |   `Office365Settings` \>        |
|                                     |   `Enable` \> `false`           |
|                                     | - Environment variable:         |
|                                     |   `MM_OFFICE365SETTINGS_ENABLE` |
+-------------------------------------+---------------------------------+

:::: note
::: title
Note
:::

See the
`Entra ID Single Sign-On </administration-guide/onboard/sso-entraid>`{.interpreted-text
role="doc"} documentation for details.
::::

##### Entra ID OAuth 2.0 Application ID

+--------------------------------------------------+-----------------------------+
| This setting holds the **Application ID**        | - System Config path:       |
| generated when configuring Entra ID as a Single  |   **Authentication \> OAuth |
| Sign-On service through the Microsoft Azure      |   2.0**                     |
| Portal.                                          | - `config.json` setting:    |
|                                                  |   `Office365Settings` \>    |
| String input.                                    |   `Id`                      |
|                                                  | - Environment variable:     |
|                                                  |   `MM_OFFICE365SETTINGS_ID` |
+--------------------------------------------------+-----------------------------+

:::: note
::: title
Note
:::

See the
`Entra ID Single Sign-On </administration-guide/onboard/sso-entraid>`{.interpreted-text
role="doc"} documentation for details.
::::

##### Entra ID OAuth 2.0 Application secret password

+--------------------------------------------------+---------------------------------+
| This setting holds the **Application Secret      | - System Config path:           |
| Password** generated when configuring Entra ID   |   **Authentication \> OAuth     |
| as a Single Sign-On service through the          |   2.0**                         |
| Microsoft Azure Portal.                          | - `config.json` setting:        |
|                                                  |   `Office365Settings` \>        |
| String input.                                    |   `Secret`                      |
|                                                  | - Environment variable:         |
|                                                  |   `MM_OFFICE365SETTINGS_SECRET` |
+--------------------------------------------------+---------------------------------+

:::: note
::: title
Note
:::

See the
`Entra ID Single Sign-On </administration-guide/onboard/sso-entraid>`{.interpreted-text
role="doc"} documentation for details.
::::

##### Entra ID OAuth 2.0 Directory (tenant) ID

+----------------------------------------+--------------------------------------+
| This setting holds the **Directory     | - System Config path:                |
| (tenant) ID** set for Mattermost       |   **Authentication \> OAuth 2.0**    |
| through the Azure Portal.              | - `config.json` setting:             |
|                                        |   `Office365Settings` \>             |
| String input.                          |   `DirectoryId`                      |
|                                        | - Environment variable:              |
|                                        |   `MM_OFFICE365SETTINGS_DIRECTORYID` |
+----------------------------------------+--------------------------------------+

:::: note
::: title
Note
:::

See the
`Entra ID Single Sign-On </administration-guide/onboard/sso-entraid>`{.interpreted-text
role="doc"} documentation for details.
::::

##### Entra ID OAuth 2.0 User API endpoint

+---------------------------------------------------+------------------------------------------+
| We recommend                                      | - System Config path: **Authentication   |
| `https://graph.microsoft.com/v1.0/me` as the User |   \> OAuth 2.0**                         |
| API Endpoint. Otherwise, enter a custom endpoint  | - `config.json` setting:                 |
| in `config.json` with `http`, or `https`, if      |   `Office365Settings` \>                 |
| available on the server.                          |   `UserAPIEndpoint`                      |
|                                                   | - Environment variable:                  |
| String input.                                     |   `MM_OFFICE365SETTINGS_USERAPIENDPOINT` |
+---------------------------------------------------+------------------------------------------+

##### Entra ID OAuth 2.0 Auth endpoint

+------------------------------------------------------------------+---------------------------------------+
| We recommend                                                     | - System Config path:                 |
| `https://login.microsoftonline.com/common/oauth2/v2.0/authorize` |   **Authentication \> OAuth 2.0**     |
| as the Auth Endpoint. Otherwise, enter a custom endpoint in      | - `config.json` setting:              |
| `config.json` with `http`, or `https`, if available on the       |   `Office365Settings` \>              |
| server.                                                          |   `AuthEndpoint`                      |
|                                                                  | - Environment variable:               |
| String input.                                                    |   `MM_OFFICE365SETTINGS_AUTHENDPOINT` |
+------------------------------------------------------------------+---------------------------------------+

##### Entra ID OAuth 2.0 Token endpoint

+--------------------------------------------------------------+----------------------------------------+
| We recommend                                                 | - System Config path: **Authentication |
| `https://login.microsoftonline.com/common/oauth2/v2.0/token` |   \> OAuth 2.0**                       |
| as the Token Endpoint. Otherwise, enter a custom endpoint in | - `config.json` setting:               |
| `config.json` with `http`, or `https`, if available on the   |   `Office365Settings` \>               |
| server.                                                      |   `TokenEndpoint`                      |
|                                                              | - Environment variable:                |
| String input.                                                |   `MM_OFFICE365SETTINGS_TOKENENDPOINT` |
+--------------------------------------------------------------+----------------------------------------+

------------------------------------------------------------------------

## OpenID Connect

Access the following configuration settings in the System Console by
going to **Authentication \> OpenID Connect**.

### Select OpenID Connect service provider

+----------------------------------------------+-----------------------------+
| Use this setting to enable OpenID Connect,   | - System Config path:       |
| with these options:                          |   **Authentication \>       |
|                                              |   OpenID Connect**          |
| - **Do not allow login via an OpenID         | - `config.json` setting:    |
|   provider**                                 |   N/A                       |
| - **GitLab** ([see                           | - Environment variable: N/A |
|   settings](#gitlab-openid-settings))        |                             |
| - **Google Apps** ([see                      |                             |
|   settings](#google-openid-settings))        |                             |
| - **Entra ID** ([see                         |                             |
|   settings](#entra-id-openid-settings))      |                             |
| - **OpenID Connect (Other)** ([see           |                             |
|   settings](#openid-connect-other-settings)) |                             |
+----------------------------------------------+-----------------------------+

:::: note
::: title
Note
:::

**GitLab** OpenID is available in all plans. All other providers require
Mattermost Enterprise or Professional.
::::

#### GitLab OpenID settings

##### Enable OpenID Connect authentication with GitLab

+--------------------------------------+-------------------------------+
| - **true**: Allows team and account  | - System Config path:         |
|   creation using GitLab OpenID       |   **Authentication \> OpenID  |
|   Connect authentication.            |   Connect**                   |
| - **false**: **(Default)** Disables  | - `config.json` setting:      |
|   GitLab OpenID Connect              |   `GitLabSettings` \>         |
|   authentication.                    |   `Enable` \> `false`         |
|                                      | - Environment variable:       |
|                                      |   `MM_GITLABSETTINGS_ENABLE`  |
+--------------------------------------+-------------------------------+

:::: note
::: title
Note
:::

See the
`GitLab Single Sign-On </administration-guide/onboard/sso-gitlab>`{.interpreted-text
role="doc"} documentation for details.
::::

##### GitLab OpenID site URL

+------------------------------------------+---------------------------+
| This setting stores the URL of your      | - System Config path:     |
| GitLab instance, e.g.                    |   **Authentication \>     |
| **https://example.com:3000**.            |   OpenID Connect**        |
|                                          | - `config.json` setting:  |
| String input.                            |   N/A                     |
|                                          | - Environment variable:   |
|                                          |   N/A                     |
+------------------------------------------+---------------------------+

:::: note
::: title
Note
:::

See **Step 2** of the
`GitLab Single Sign-On </administration-guide/onboard/sso-gitlab>`{.interpreted-text
role="doc"} documentation for details.
::::

##### GitLab OpenID Discovery endpoint

+-------------------------------------------------------+-----------------------------------------+
| This setting is prepopulated with the Discovery       | - System Config path: **Authentication  |
| Endpoint for GitLab OpenID Connect.                   |   \> OpenID Connect**                   |
|                                                       | - `config.json` setting:                |
| String input. Default is                              |   `GitLabSettings` \>                   |
| `https://gitlab.com/.well-known/openid-configuration` |   `DiscoveryEndpoint`                   |
|                                                       | - Environment variable:                 |
|                                                       |   `MM_GITLABSETTINGS_DISCOVERYENDPOINT` |
+-------------------------------------------------------+-----------------------------------------+

:::: note
::: title
Note
:::

See **Step 2** of the
`GitLab Single Sign-On </administration-guide/onboard/sso-gitlab>`{.interpreted-text
role="doc"} documentation for details.
::::

##### GitLab OpenID Client ID

+--------------------------------+-------------------------------------+
| This setting stores the        | - System Config path:               |
| **Application ID** generated   |   **Authentication \> OpenID        |
| by GitLab.                     |   Connect**                         |
|                                | - `config.json` setting:            |
| String input.                  |   `GitLabSettings` \> `Id`          |
|                                | - Environment variable:             |
|                                |   `MM_GITLABSETTINGS_ID`            |
+--------------------------------+-------------------------------------+

:::: note
::: title
Note
:::

See **Step 2** of the
`GitLab Single Sign-On </administration-guide/onboard/sso-gitlab>`{.interpreted-text
role="doc"} documentation for details.
::::

##### GitLab OpenID Client secret

+------------------------------------+---------------------------------+
| This setting stores the            | - System Config path:           |
| **Application Secret Key**         |   **Authentication \> OpenID    |
| generated by GitLab.               |   Connect**                     |
|                                    | - `config.json` setting:        |
| String input.                      |   `GitLabSettings` \> `Secret`  |
|                                    | - Environment variable:         |
|                                    |   `MM_GITLABSETTINGS_SECRET`    |
+------------------------------------+---------------------------------+

:::: note
::: title
Note
:::

See **Step 2** of the
`GitLab Single Sign-On </administration-guide/onboard/sso-gitlab>`{.interpreted-text
role="doc"} documentation for details.
::::

#### Google OpenID settings

##### Enable OpenID Connect authentication with Google

> - **true**: Allow team creation and account signup using Google OpenID
>   Connect.
> - **false**: **(Default)** Google OpenID Connect cannot be used for
>   team creation or account signup.

+--------------------------------------------------------------------------------------+------------------------------+
| - **true**: Allows team and account creation using Google OpenID authentication.     | - System Config path:        |
| - **false**: **(Default)** Disables Google OpenID authentication.                    |   **Authentication \> OpenID |
|                                                                                      |   Connect**                  |
| See                                                                                  | - `config.json` setting:     |
| `Google Single Sign-On </administration-guide/onboard/sso-google>`{.interpreted-text |   `GoogleSettings` \>        |
| role="doc"} implementation instructions.                                             |   `Enable` \> `false`        |
|                                                                                      | - Environment variable:      |
|                                                                                      |   `MM_GOOGLESETTINGS_ENABLE` |
+--------------------------------------------------------------------------------------+------------------------------+

##### Google OpenID Discovery endpoint

+---------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------+
| This setting is prepopulated with the Discovery Endpoint for Google OpenID Connect.                                                                     | - System Config path: **Authentication  |
|                                                                                                                                                         |   \> OpenID Connect**                   |
| See                                                                                                                                                     | - `config.json` setting:                |
| `Configure Mattermost for Google Apps SSO <administration-guide/onboard/sso-google:step 3: configure mattermost for google apps sso>`{.interpreted-text |   `GoogleSettings` \>                   |
| role="ref"}.                                                                                                                                            |   `DiscoveryEndpoint`                   |
|                                                                                                                                                         | - Environment variable:                 |
| String input. Default is `https://accounts.google.com/.well-known/openid-configuration`                                                                 |   `MM_GOOGLESETTINGS_DISCOVERYENDPOINT` |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------+

##### Google OpenID Client ID

+--------------------------------------------------------------------------------------+--------------------------+
| This setting stores the Client ID generated by Google.                               | - System Config path:    |
|                                                                                      |   **Authentication \>    |
| See                                                                                  |   OpenID Connect**       |
| `Google Single Sign-On </administration-guide/onboard/sso-google>`{.interpreted-text | - `config.json` setting: |
| role="doc"} implementation instructions.                                             |   `GoogleSettings` \>    |
|                                                                                      |   `Id`                   |
| String input.                                                                        | - Environment variable:  |
|                                                                                      |   `MM_GOOGLESETTINGS_ID` |
+--------------------------------------------------------------------------------------+--------------------------+

##### Google OpenID Client secret

+--------------------------------------------------------------------------------------+------------------------------+
| This setting stores the Client Secret generated by Google.                           | - System Config path:        |
|                                                                                      |   **Authentication \> OpenID |
| See                                                                                  |   Connect**                  |
| `Google Single Sign-On </administration-guide/onboard/sso-google>`{.interpreted-text | - `config.json` setting:     |
| role="doc"} implementation instructions.                                             |   `GoogleSettings` \>        |
|                                                                                      |   `Secret`                   |
| String input.                                                                        | - Environment variable:      |
|                                                                                      |   `MM_GOOGLESETTINGS_SECRET` |
+--------------------------------------------------------------------------------------+------------------------------+

#### Entra ID OpenID settings

:::: note
::: title
Note
:::

In line with Microsoft ADFS guidance, we recommend [configuring intranet
forms-based authentication for devices that do not support
WIA](https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia).
::::

##### Enable OpenID Connect authentication with Entra ID

+-----------------------------------------------------------------------------------------+---------------------------------+
| - **true**: Allows team and account creation using Entra ID OpenID Connect              | - System Config path:           |
|   authentication.                                                                       |   **Authentication \> OpenID    |
| - **false**: **(Default)** Disables Entra ID OpenID Connect authentication.             |   Connect**                     |
|                                                                                         | - `config.json` setting:        |
| See                                                                                     |   `Office365Settings` \>        |
| `Entra ID Single Sign-On </administration-guide/onboard/sso-entraid>`{.interpreted-text |   `Enable` \> `false`           |
| role="doc"} implementation instructions.                                                | - Environment variable:         |
|                                                                                         |   `MM_OFFICE365SETTINGS_ENABLE` |
+-----------------------------------------------------------------------------------------+---------------------------------+

##### Entra ID OpenID Directory (tenant) ID

+-----------------------------------------------------------------------------------------+--------------------------------------+
| This setting holds the Directory (tenant) ID set for Mattermost through the Microsoft   | - System Config path:                |
| Azure Portal.                                                                           |   **Authentication \> OpenID         |
|                                                                                         |   Connect**                          |
| See                                                                                     | - `config.json` setting:             |
| `Entra ID Single Sign-On </administration-guide/onboard/sso-entraid>`{.interpreted-text |   `Office365Settings` \>             |
| role="doc"} implementation instructions.                                                |   `DirectoryId`                      |
|                                                                                         | - Environment variable:              |
| String input.                                                                           |   `MM_OFFICE365SETTINGS_DIRECTORYID` |
+-----------------------------------------------------------------------------------------+--------------------------------------+

##### Entra ID OpenID Discovery endpoint

+-----------------------------------------------------------------------------------------+--------------------------------------------+
| This setting is prepopulated with the Discovery Endpoint for Entra ID OpenID Connect.   | - System Config path: **Authentication \>  |
|                                                                                         |   OpenID Connect**                         |
| See                                                                                     | - `config.json` setting:                   |
| `Entra ID Single Sign-On </administration-guide/onboard/sso-entraid>`{.interpreted-text |   `Office365Settings` \>                   |
| role="doc"} implementation instructions.                                                |   `DiscoveryEndpoint`                      |
|                                                                                         | - Environment variable:                    |
| String input. Default is                                                                |   `MM_OFFICE365SETTINGS_DISCOVERYENDPOINT` |
| `https://login.microsoftonline.com/common/v2.0/.well-known/openid-configuration`        |                                            |
+-----------------------------------------------------------------------------------------+--------------------------------------------+

##### Entra ID Client ID

+-----------------------------------------------------------------------------------------+-----------------------------+
| This setting stores the **Application (client) ID** generated through the Microsoft     | - System Config path:       |
| Azure Portal.                                                                           |   **Authentication \>       |
|                                                                                         |   OpenID Connect**          |
| See                                                                                     | - `config.json` setting:    |
| `Entra ID Single Sign-On </administration-guide/onboard/sso-entraid>`{.interpreted-text |   `Office365Settings` \>    |
| role="doc"} implementation instructions.                                                |   `Id`                      |
|                                                                                         | - Environment variable:     |
| String input.                                                                           |   `MM_OFFICE365SETTINGS_ID` |
+-----------------------------------------------------------------------------------------+-----------------------------+

##### Entra ID Client secret

+-----------------------------------------------------------------------------------------+---------------------------------+
| This setting stores the **Client Secret** generated through the Microsoft Azure Portal. | - System Config path:           |
|                                                                                         |   **Authentication \> OpenID    |
| See                                                                                     |   Connect**                     |
| `Entra ID Single Sign-On </administration-guide/onboard/sso-entraid>`{.interpreted-text | - `config.json` setting:        |
| role="doc"} implementation instructions.                                                |   `Office365Settings` \>        |
|                                                                                         |   `Secret`                      |
| String input.                                                                           | - Environment variable:         |
|                                                                                         |   `MM_OFFICE365SETTINGS_SECRET` |
+-----------------------------------------------------------------------------------------+---------------------------------+

#### OpenID Connect (other) settings

##### Enable OpenID Connect authentication with other service providers

+-----------------------------------------------------------------------------------------------------+------------------------------+
| - **true**: Allows team and account creation using other OpenID Connect service providers.          | - System Config path:        |
| - **false**: **(Default)** Disables OpenID Connect authentication with other service providers.     |   **Authentication \> OpenID |
|                                                                                                     |   Connect**                  |
| See                                                                                                 | - `config.json` setting:     |
| `OpenID Connect Single Sign-On </administration-guide/onboard/sso-openidconnect>`{.interpreted-text |   `OpenIdSettings` \>        |
| role="doc"} implementation instructions.                                                            |   `Enable` \> `false`        |
|                                                                                                     | - Environment variable:      |
|                                                                                                     |   `MM_OPENIDSETTINGS_ENABLE` |
+-----------------------------------------------------------------------------------------------------+------------------------------+

##### OpenID Connect (other) Button name

+--------------------------------+-------------------------------------+
| This setting is the text for   | - System Config path:               |
| the OpenID login button.       |   **Authentication \> OpenID        |
|                                |   Connect**                         |
| String input.                  | - `config.json` setting:            |
|                                |   `OpenIdSettings` \> `ButtonText`  |
|                                | - Environment variable:             |
|                                |   `MM_OPENIDSETTINGS_BUTTONTEXT`    |
+--------------------------------+-------------------------------------+

##### OpenID Connect (other) Button color

+----------------------------------------------+-----------------------------------+
| This setting is the color of the OpenID      | - System Config path:             |
| login button. Use a hex code with a #-sign   |   **Authentication \> OpenID      |
| before the code, for example `#145DBF`.      |   Connect**                       |
|                                              | - `config.json` setting:          |
| String input.                                |   `OpenIdSettings` \>             |
|                                              |   `ButtonColor`                   |
|                                              | - Environment variable:           |
|                                              |   `MM_OPENIDSETTINGS_BUTTONCOLOR` |
+----------------------------------------------+-----------------------------------+

##### OpenID Connect (other) Discovery endpoint

+-----------------------------------------------------------------------------------------------------+-----------------------------------------+
| This setting stores the Discovery Endpoint URL from the OpenID provider. The URL should be in the   | - System Config path: **Authentication  |
| format of `https://myopenid.provider.com/{my_organization}/ .well-known/openid-configuration`.      |   \> OpenID Connect**                   |
|                                                                                                     | - `config.json` setting:                |
| See                                                                                                 |   `OpenIdSettings` \>                   |
| `OpenID Connect Single Sign-On </administration-guide/onboard/sso-openidconnect>`{.interpreted-text |   `DiscoveryEndpoint`                   |
| role="doc"} implementation instructions.                                                            | - Environment variable:                 |
|                                                                                                     |   `MM_OPENIDSETTINGS_DISCOVERYENDPOINT` |
| String input.                                                                                       |                                         |
+-----------------------------------------------------------------------------------------------------+-----------------------------------------+

:::: note
::: title
Note
:::

The **Discovery Endpoint** setting can be used to determine the
connectivity and availability of arbitrary hosts. System admins
concerned about this can use custom admin roles to limit access to
modifying these settings. See the
`delegated granular administration <administration-guide/onboard/delegated-granular-administration:edit privileges of admin roles (advanced)>`{.interpreted-text
role="ref"} documentation for details.
::::

##### OpenID Connect (other) Client ID

+-----------------------------------------------------------------------------------------------------+--------------------------+
| This setting stores the Client ID from the OpenID provider.                                         | - System Config path:    |
|                                                                                                     |   **Authentication \>    |
| See                                                                                                 |   OpenID Connect**       |
| `OpenID Connect Single Sign-On </administration-guide/onboard/sso-openidconnect>`{.interpreted-text | - `config.json` setting: |
| role="doc"} implementation instructions.                                                            |   `OpenIdSettings` \>    |
|                                                                                                     |   `Id`                   |
| String input.                                                                                       | - Environment variable:  |
|                                                                                                     |   `MM_OPENIDSETTINGS_ID` |
+-----------------------------------------------------------------------------------------------------+--------------------------+

##### OpenID Connect (other) Client secret

+-----------------------------------------------------------------------------------------------------+------------------------------+
| This setting stores the Client Secret from the OpenID provider.                                     | - System Config path:        |
|                                                                                                     |   **Authentication \> OpenID |
| See                                                                                                 |   Connect**                  |
| `OpenID Connect Single Sign-On </administration-guide/onboard/sso-openidconnect>`{.interpreted-text | - `config.json` setting:     |
| role="doc"} implementation instructions.                                                            |   `OpenIdSettings` \>        |
|                                                                                                     |   `Secret`                   |
| String input.                                                                                       | - Environment variable:      |
|                                                                                                     |   `MM_OPENIDSETTINGS_SECRET` |
+-----------------------------------------------------------------------------------------------------+------------------------------+

------------------------------------------------------------------------

## Guest access

Access the following configuration settings in the System Console by
going to **Authentication \> Guest Access**.

### Enable guest access

+-------------------------------+--------------------------------------+
| - **true**: Enables the guest | - System Config path:                |
|   account feature.            |   **Authentication \> Guest Access** |
| - **false**: **(Default)**    | - `config.json` setting:             |
|   Disables the guest account  |   `GuestAccountsSettings` \>         |
|   feature.                    |   `Enable` \> `false`                |
|                               | - Environment variable:              |
|                               |   `MM_GUESTACCOUNTSSETTINGS_ENABLE`  |
+-------------------------------+--------------------------------------+

:::: note
::: title
Note
:::

For billing purposes, activated guest accounts do consume a licensed
seat, which is returned when the guest account is deactivated.This means
that guest accounts count as a paid user in your Mattermost
`workspace </end-user-guide/end-user-guide-index>`{.interpreted-text
role="doc"}.
::::

### Whitelisted guest domains

+--------------------------------------------+--------------------------------------------------------+
| Use this setting to restrict the creation  | - System Config path: **Authentication \> Guest        |
| of guest accounts. When set, guest         |   Access**                                             |
| accounts require a verified email address  | - `config.json` setting: `GuestAccountsSettings` \>    |
| from one of the listed domains.            |   `RestrictCreationToDomains`                          |
|                                            | - Environment variable:                                |
| String input of one or more domains,       |   `MM_GUESTACCOUNTSSETTINGS_RESTRICTCREATIONTODOMAINS` |
| separated by commas.                       |                                                        |
+--------------------------------------------+--------------------------------------------------------+

### Show guest tag

+-------------------------------+---------------------------------------+
| - **true**: **(Default)**     | - System Config path:                 |
|   Guest tags are visible in   |   **Authentication \> Guest Access**  |
|   Mattermost.                 | - `config.json` setting:              |
| - **false**: Guest tags       |   `GuestAccountsSettings` \>          |
|   aren\'t visible in          |   `HideTags` \> `true`                |
|   Mattermost.                 | - Environment variable:               |
|                               |   `MM_GUESTACCOUNTSSETTINGS_HIDETAGS` |
+-------------------------------+---------------------------------------+

:::: note
::: title
Note
:::

This configuration setting applies to all Mattermost clients, including
web, desktop app, and mobile app. See the
`guest accounts </administration-guide/onboard/guest-accounts>`{.interpreted-text
role="doc"} documentation for details.
::::

### Enable guest magic link authentication

+----------------------------------+-----------------------------------+
| - **true**: Enables magic link   | - System Config path:             |
|   passwordless authentication    |   **Authentication \> Guest       |
|   for guest users.               |   Access**                        |
| - **false**: **(Default)** Magic | - `config.json` setting:          |
|   link authentication for guest  |   `GuestAccountsSettings` \>      |
|   users is disabled.             |   `EnableGuestMagicLink` \>       |
|                                  |   `false`                         |
+----------------------------------+-----------------------------------+

:::: note
::: title
Note
:::

See the
`guest accounts <administration-guide/onboard/guest-accounts:configure magic links for guests>`{.interpreted-text
role="ref"} documentation for guest user setup details.
::::

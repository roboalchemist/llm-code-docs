# Source: https://docs.sonarsource.com/sonarqube-server/8.9/instance-administration/delegating-authentication.md

# Delegating authentication

SonarQube comes with an onboard user database, as well as the ability to delegate authentication via HTTP Headers, GitHub Authentication, GitLab Authentication, SAML, or LDAP. Each method offers user identity management, group synchronization/mapping, and authentication.

### Group mapping <a href="#group-mapping" id="group-mapping"></a>

When using group mapping, the following caveats apply regardless of which delegated authentication method is used:

* Membership in synchronized groups will override any membership locally configured in SonarQube *at each login*
* Membership in a group is synched only if a group with the same name exists in SonarQube
* Membership in the default group `sonar-users` remains (this is a built-in group) even if the group does not exist in the identity provider

{% hint style="warning" %}
When group mapping is configured, the delegated authentication source becomes the only place to manage group membership, and the user’s groups are re-fetched with each log-in.
{% endhint %}

### HTTP header authentication <a href="#http-header-authentication" id="http-header-authentication"></a>

You can delegate user authentication to third-party systems (proxies/servers) using HTTP Header Authentication.

When this feature is activated, SonarQube expects that the authentication is handled prior to any query reaching the server. The tool that handles the authentication should:

* Intercept calls to the SonarQube server
* Take care of the authentication
* Update the HTTP request header with the relevant SonarQube user information
* Re-route the request to SonarQube with the appropriate header information

![](https://4108688904-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FG0n8jfxwZN8LmyH08dMa%2Fuploads%2Fgit-blob-cf613ec4030d22bbd004f621ba94723058de47cc%2F427aabec883bfd25b61b383cc6ca0fc598450279.png?alt=media)

All the parameters required to activate and configure this feature are available in SonarQube server configuration file (in `<SONARQUBE_HOME>/conf/sonar.properties`).

Using HTTP header authentication is an easy way to integrate your SonarQube deployment with an in-house SSO implementation.

### GitHub and GitLab authentication <a href="#github-and-gitlab-authentication" id="github-and-gitlab-authentication"></a>

You can delegate authentication to GitHub or GitLab. See the corresponding DevOps platform integration page for more information:

* [github-integration](https://docs.sonarsource.com/sonarqube-server/8.9/alm-integration/github-integration "mention")
* [gitlab-integration](https://docs.sonarsource.com/sonarqube-server/8.9/alm-integration/gitlab-integration "mention")

### SAML authentication <a href="#saml-authentication" id="saml-authentication"></a>

You can delegate authentication to a SAML 2.0 Identity Provider using SAML Authentication.

#### Limitations <a href="#limitations" id="limitations"></a>

* SAML requests are not signed. Client signature validation should be disabled in the identity provider.
* SAML encrypted responses are not supported. SAML encryption should be disabled in the identity provider.

#### Example: Using Keycloak as a SAML identity provider <a href="#example-using-keycloak-as-a-saml-identity-provider" id="example-using-keycloak-as-a-saml-identity-provider"></a>

The following example may be useful if you’re using Keycloak as a SAML identity provider. If you’re not using Keycloak, your settings are likely to be different.

<details>

<summary>In the Keycloak server, create a new SAML client</summary>

Create a new client

1. **Client ID**: Something like "sonarqube", it must not contain whitespace.
2. **Client Protocol**: *saml*
3. **Client SAML Endpoint**: Can be left empty.

Configure the new client

1. Under *Settings*
   1. **Client Signature Required:** OFF.
   2. **Valid Redirect URIs**: `<SONARQUBE_URL>/oauth2/callback/saml` (for example, <https://sonarqube.mycompany.com/oauth2/callback/saml>).
2. In **Client Scopes > Default Client Scopes**, remove `role_list` from **Assigned Default Client Scopes** (to prevent the error `com.onelogin.saml2.exception.ValidationError: Found an Attribute element with duplicated Name` during authentication).
3. Under **Mappers**, create a mapper for each user attribute:
   1. Create a mapper for the login:
      1. **Name**: `Login`
      2. **Mapper Type**: *User Property*
      3. **Property**: `<USER_LOGIN>` (Substitute the actual user login. This value should not contain any special characters other than `.-_@` to meet SonarQube restrictions)
      4. **SAML Attribute Name**: *login*
   2. Create a mapper for the name:
      1. **Name**: `Name`
      2. **Mapper Type**: *User Property*
      3. **Property**: `<USER_NAME>` (Substitute the actual user name)
      4. **SAML Attribute Name**: *name*
   3. (Optional) Create a mapper for the email:
      1. **Name**: `Email`
      2. **Mapper Type**: *User Property*
      3. **Property**: `<USER_EMAIL>` (Substitute the actual user email)
      4. **SAML Attribute Name**: "email"
   4. (Optional) Create a mapper for the groups (if you rely on a list of roles defined in **Roles** of the realm , not in **Roles** of the client):
      1. **Name**: `Groups`
      2. **Mapper Type**: *Role list*
      3. **Role Attribute Name**: `groups`
      4. **Single Role Attribute**: *ON*
   5. If you rely on a list of groups defined in "Groups":
      1. **Name**: `Groups`
      2. **Mapper Type**: *Group list*
      3. **Role Attribute Name**: `groups`
      4. **Single Role Attribute**: *ON*
      5. **Full Group Path**: *OFF*
4. In **Realm Settings > General > Endpoints**, click on **SAML 2.0 Identify Provider Metadata** to obtain the XML configuration file from Keycloak.

</details>

<details>

<summary>In SonarQube, configure SAML authentication</summary>

Go to **Administration > Configuration > General Settings > Security > SAML**

* **Enabled**: *true.*
* **Application ID**: The value of the **Client ID** you set in Keycloak (for example `sonarqube`).
* **Provider ID**: The value of the `EntityDescriptor > entityID` attribute in the XML configuration file (e.g., "<http://keycloak:8080/auth/realms/sonarqube%22>).
* **SAML login url**: The value of `SingleSignOnService > Location` attribute in the XML configuration file (e.g., "<http://keycloak:8080/auth/realms/sonarqube/protocol/saml%22>).
* **Identity provider certificate**: The value you get from **Realm Settings > Keys**. Click on the *Certificate* button.
* **SAML user login attribute**: The value set in the login mapper in **SAML Attribute Name** (`login`, in the above example).
* **SAML user name attribute**: The value set in the name mapper in **SAML Attribute Name** (`name`, in the above example).
* (Optional) **SAML user email attribute**: The value set in the email mapper in **SAML Attribute Name** (`email`, in the above example).
* (Optional) **SAML group attribute**: the value set in the groups mapper in **Role/Group Attribute Name** (`groups`, in the above example).

In the login form, the new button **Log in with SAML** allows users to connect with their SAML account.

</details>

#### SAML and reverse proxy configuration <a href="#saml-and-reverse-proxy-configuration" id="saml-and-reverse-proxy-configuration"></a>

When using SAML, make sure your reverse proxy is properly configured. See [operating-the-server](https://docs.sonarsource.com/sonarqube-server/8.9/setup-and-upgrade/configure-and-operate-a-server/operating-the-server "mention") for more information.

### LDAP Authentication <a href="#ldap-authentication" id="ldap-authentication"></a>

You can configure SonarQube authentication and authorization to an LDAP server (including LDAP Service of Active Directory) by configuring the correct values in `<SONARQUBE_HOME>/conf/sonar.properties`.

The main features are:

* Password checking against the external authentication engine.
* Automatic synchronization of usernames and emails.
* Automatic synchronization of relationships between users and groups (authorization).
* Ability to authenticate against both the external and the internal authentication systems. There is an automatic fallback on SonarQube internal system if the LDAP server is down.
* During the first authentication trial, if the user’s password is correct, the SonarQube database is automatically populated with the new user. Each time a user logs into SonarQube, the username, the email and the groups this user belongs to that are refreshed in the SonarQube database. You can choose to have group membership synchronized as well, but this is not the default.

|            |               |              |             |                      |
| ---------- | ------------- | ------------ | ----------- | -------------------- |
|            | **Apache DS** | **OpenLDAP** | **Open DS** | **Active Directory** |
| Anonymous  | **Y**         | **Y**        | **Y**       |                      |
| Simple     | **Y**         | **Y**        | **Y**       | **Y**                |
| LDAPS      | **Y**         | **Y**        | <p><br></p> | **Y**                |
| DIGEST-MD5 | **Y**         | <p><br></p>  | **Y**       | **Y**                |
| CRAM-MD5   | **Y**         | <p><br></p>  | **Y**       | **Y**                |
| GSSAPI     | **Y**         | <p><br></p>  | <p><br></p> | <p><br></p>          |

**Y** = successfully tested

#### Setup <a href="#setup" id="setup"></a>

* Configure LDAP by editing `<SONARQUBE_HOME>/conf/sonar.properties` (see table below).
* Restart the SonarQube server and check the log file for:

```css-79elbk
INFO org.sonar.INFO Security realm: LDAP ...
INFO o.s.p.l.LdapContextFactory Test LDAP connection: OK
```

* Log into SonarQube
* On logout users will be presented a login page (`/sessions/login`), where they can choose to login as technical user or a domain user by passing appropriate credentials

From SonarScanners, we recommend using [security](https://docs.sonarsource.com/sonarqube-server/8.9/instance-administration/security "mention") for authentication against SonarQube Server.

**General configuration**

|                                |                                                                                                                                                                                                                                         |                                    |              |                                 |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | ------------ | ------------------------------- |
| **Property**                   | **Description**                                                                                                                                                                                                                         | **Default value**                  | **Required** | **Example**                     |
| `sonar.security.realm`         | Set this to `LDAP` authenticate first against the external sytem. If the external system is not reachable or if the user is not defined in the external system, authentication will be performed against SonarQube’s internal database. | none                               | Yes          | `LDAP` (only possible value)    |
| `sonar.authenticator.downcase` | Set to true when connecting to a LDAP server using a case-insensitive setup.                                                                                                                                                            | `false`                            | No           | <p><br></p>                     |
| `ldap.url`                     | URL of the LDAP server. If you are using ldaps, you should install the server certificate into the Java truststore.                                                                                                                     | none                               | Yes          | `ldap://localhost:10389`        |
| `ldap.bindDn`                  | The username of an LDAP user to connect (or bind) with. Leave this blank for anonymous access to the LDAP directory.                                                                                                                    | none                               | No           | `cn=sonar,ou=users,o=mycompany` |
| `ldap.bindPassword`            | The password of the user to connect with. Leave this blank for anonymous access to the LDAP directory.                                                                                                                                  | none                               | No           | `secret`                        |
| `ldap.authentication`          | Possible values: `simple`, `CRAM-MD5`, `DIGEST-MD5`, `GSSAPI`. See [the tutorial on authentication mechanisms](http://java.sun.com/products/jndi/tutorial/ldap/security/auth.html)                                                      | `simple`                           | No           | <p><br></p>                     |
| `ldap.realm`                   | See [Digest-MD5 Authentication](http://java.sun.com/products/jndi/tutorial/ldap/security/digest.html), [CRAM-MD5 Authentication](http://java.sun.com/products/jndi/tutorial/ldap/security/crammd5.html)                                 | none                               | No           | example.org                     |
| `ldap.contextFactoryClass`     | Context factory class.                                                                                                                                                                                                                  | `com.sun.jndi.ldap.LdapCtxFactory` | No           | <p><br></p>                     |
| `ldap.StartTLS`                | Enable use of `StartTLS`                                                                                                                                                                                                                | `false`                            | No           | <p><br></p>                     |
| `ldap.followReferrals`         | Follow referrals or not. See [Referrals in the JNDI](http://docs.oracle.com/javase/jndi/tutorial/ldap/referral/jndi.html)                                                                                                               | `true`                             | <p><br></p>  | <p><br></p>                     |

**User mapping**

|                               |                                                                                  |                                               |              |                                                 |
| ----------------------------- | -------------------------------------------------------------------------------- | --------------------------------------------- | ------------ | ----------------------------------------------- |
| **Property**                  | **Description**                                                                  | **Default value**                             | **Required** | **Example for Active Directory**                |
| `ldap.user.baseDn`            | Distinguished Name (DN) of the root node in LDAP from which to search for users. | None                                          | Yes          | `cn=users,dc=example,dc=org`                    |
| `ldap.user.request`           | LDAP user request.                                                               | `(&(objectClass=inetOrgPerson)(uid={login}))` | No           | `(&(objectClass=user)(sAMAccountName={login}))` |
| `ldap.user.realNameAttribute` | Attribute in LDAP defining the user’s real name.                                 | `cn`                                          | No           | <p><br></p>                                     |
| `ldap.user.emailAttribute`    | Attribute in LDAP defining the user’s email.                                     | `mail`                                        | No           | <p><br></p>                                     |

**Group Mapping** Only groups (not roles) and static groups (not dynamic groups) are supported. Click [here](http://identitycontrol.blogspot.fr/2007/07/static-vs-dynamic-ldap-groups.html) for more information.

For the delegation of authorization, [security](https://docs.sonarsource.com/sonarqube-server/8.9/instance-administration/security "mention"). Then, the following properties must be defined to allow SonarQube to automatically synchronize the relationships between users and groups.

|                          |                                                                                                                     |                                                          |              |                                       |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | ------------ | ------------------------------------- |
| **Property**             | **Description**                                                                                                     | **Default value**                                        | **Required** | **Example for Active Directory**      |
| `ldap.group.baseDn`      | Distinguished Name (DN) of the root node in LDAP from which to search for groups.                                   | none                                                     | No           | `cn=groups,dc=example,dc=org`         |
| `ldap.group.request`     | LDAP group request.                                                                                                 | `(&(objectClass=groupOfUniqueNames)(uniqueMember={dn}))` | No           | `(&(objectClass=group)(member={dn}))` |
| `ldap.group.idAttribute` | Property used to specifiy the attribute to be used for returning the list of user groups in the compatibility mode. | `cn`                                                     | No           | `sAMAccountName`                      |

#### Sample configuration <a href="#sample-configuration" id="sample-configuration"></a>

```css-79elbk
# LDAP configuration
# General Configuration
sonar.security.realm=LDAP
ldap.url=ldap://myserver.mycompany.com
ldap.bindDn=my_bind_dn
ldap.bindPassword=my_bind_password
  
# User Configuration
ldap.user.baseDn=ou=Users,dc=mycompany,dc=com
ldap.user.request=(&(objectClass=inetOrgPerson)(uid={login}))
ldap.user.realNameAttribute=cn
ldap.user.emailAttribute=mail
 
# Group Configuration
ldap.group.baseDn=ou=Groups,dc=sonarsource,dc=com
ldap.group.request=(&(objectClass=posixGroup)(memberUid={uid}))
```

### Advanced LDAP Topics <a href="#advanced-ldap-topics" id="advanced-ldap-topics"></a>

#### Authentication methods <a href="#authentication-methods" id="authentication-methods"></a>

* **`Anonymous`** - Used when only read-only access to non-protected entries and attributes is needed when binding to the LDAP server.
* **`Simple`** Simple authentication is not recommended for production deployments not using the ldaps secure protocol since it sends a cleartext password over the network.
* **`CRAM-MD5`** - The Challenge-Response Authentication Method (CRAM) based on the HMAC-MD5 MAC algorithm ([RFC 2195](http://tools.ietf.org/html/rfc2195)).
* **`DIGEST-MD5`** - This is an improvement on the CRAM-MD5 authentication method ([RFC 2831](http://www.ietf.org/rfc/rfc2831.txt)).
* **`GSSAPI`** - GSS-API is Generic Security Service API ([RFC 2744](http://www.ietf.org/rfc/rfc2744.txt)). One of the most popular security services available for GSS-API is the Kerberos v5, used in Microsoft’s Windows 2000 platform.

For a full discussion of LDAP authentication approaches, see [RFC 2829](http://www.ietf.org/rfc/rfc2829.txt) and [RFC 2251](http://www.ietf.org/rfc/rfc2251.txt).

#### Multiple servers <a href="#multiple-servers" id="multiple-servers"></a>

To configure multiple servers:

```css-79elbk
# List the different servers
ldap.servers=server1,server2
  
# Configure server1
ldap.server1.url=ldap://server1:1389
ldap.server1.user.baseDn=dc=dept1,dc=com
...
 
# Configure server2
ldap.server2.url=ldap://server2:1389
ldap.server2.user.baseDn=dc=dept2,dc=com
...
```

Authentication will be tried on each server, in the order that they are listed in the configuration until one succeeds. User/group mapping will be performed against the first server on which the user is found.

Note that all the LDAP servers must be available while (re)starting the SonarQube server.

#### Migrate users to a new authentication method <a href="#migrate-users-to-a-new-authentication-method" id="migrate-users-to-a-new-authentication-method"></a>

If you are changing your delegated authentication method and migrating existing users from your previous authentication method, you can use the `api/users/update_identity_provider` web API to update your users’ identity provider.

#### Troubleshooting <a href="#troubleshooting" id="troubleshooting"></a>

* Detailed connection logs (and potential error codes received from LDAP server) are output to SonarQube’s `<SONARQUBE_HOME>/logs/web.log` when logging is in `DEBUG` mode.
* Time out when running SonarQube analysis using LDAP Java parameters are documented here: <http://docs.oracle.com/javase/jndi/tutorial/ldap/connect/config.html>. Such parameters can be set in `sonar.web.javaAdditionalOpts` in `<SONARQUBE_HOME>/conf/sonar.properties`.

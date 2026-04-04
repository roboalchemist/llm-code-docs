# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/authentication/ldap.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/instance-administration/authentication/ldap.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/instance-administration/authentication/ldap.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/instance-administration/authentication/ldap.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/instance-administration/authentication/ldap.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/instance-administration/authentication/ldap.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/instance-administration/authentication/ldap.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/instance-administration/authentication/ldap.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/instance-administration/authentication/ldap.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/instance-administration/authentication/ldap.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/authentication/ldap.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/authentication/ldap.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/authentication/ldap.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/authentication/ldap.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/authentication/ldap.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/ldap.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/authentication/ldap.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/authentication/ldap.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/ldap.md

# LDAP

You can configure SonarQube Server authentication and authorization to an LDAP server (including the LDAP service of Active Directory) through system properties (see [system-properties](https://docs.sonarsource.com/sonarqube-server/server-installation/system-properties "mention")).

The main features are:

* Password checking against the external authentication engine.
* Automatic synchronization of usernames and emails.
* Automatic synchronization of relationships between users and groups (authorization).
* During the first successful authentication, the user account is created in the SonarQube Server database. Each time a user logs into SonarQube, the username and the email are synchronized.
* Group synchronization is an option that will sync SonarQube Server group memberships with the LDAP service.

|            | Apache DS                           | OpenLDAP                            | Open DS                             | Active Directory                    |
| ---------- | ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- |
| Anonymous  | ![Checkmark icon](broken-reference) | ![Checkmark icon](broken-reference) | ![Checkmark icon](broken-reference) |                                     |
| Simple     | ![Checkmark icon](broken-reference) | ![Checkmark icon](broken-reference) | ![Checkmark icon](broken-reference) | ![Checkmark icon](broken-reference) |
| LDAPS      | ![Checkmark icon](broken-reference) | ![Checkmark icon](broken-reference) | <p><br></p>                         | ![Checkmark icon](broken-reference) |
| DIGEST-MD5 | ![Checkmark icon](broken-reference) | <p><br></p>                         | ![Checkmark icon](broken-reference) | ![Checkmark icon](broken-reference) |
| CRAM-MD5   | ![Checkmark icon](broken-reference) | <p><br></p>                         | ![Checkmark icon](broken-reference) | ![Checkmark icon](broken-reference) |
| GSSAPI     | ![Checkmark icon](broken-reference) | <p><br></p>                         | <p><br></p>                         | <p><br></p>                         |

![](https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/BZvHoOJ4lR3Kqs4mhMpx/green-check.svg)= successfully tested

### Setup <a href="#setup" id="setup"></a>

1. Configure LDAP by editing `<sonarqubeHome>/conf/sonar.properties` (see table below).
2. Restart SonarQube Server and check the log file for:\
   `INFO org.sonar.INFO Security realm: LDAP ...`\
   `INFO o.s.p.l.LdapContextFactory Test LDAP connection: OK`
3. Log in to SonarQube Server.
4. On log out users will be presented with a login page (`/sessions/login`), where they can choose to log in as a technical user or a domain user by passing the appropriate credentials.

For SonarScanners, we recommend using manually created technical accounts for authentication against SonarQube Server.

#### General Configuration <a href="#general-configuration" id="general-configuration"></a>

Set the properties listed in [#general-1](https://docs.sonarsource.com/sonarqube-server/server-installation/system-properties/common-properties#general-1 "mention").

#### User Mapping <a href="#user-mapping" id="user-mapping"></a>

Set the properties listed in [#user-mapping](https://docs.sonarsource.com/sonarqube-server/server-installation/system-properties/common-properties#user-mapping "mention").

#### Group synchronization <a href="#group-synchronization" id="group-synchronization"></a>

Only groups and static groups are supported. Roles and dynamic groups are not supported; this page about [Static Vs Dynamic LDAP Group management](http://identitycontrol.blogspot.com/2007/07/static-vs-dynamic-ldap-groups.html) offers more detail about the differences.

To set up group synchronization:

1. Create first the groups in SonarQube Server (see[user-groups](https://docs.sonarsource.com/sonarqube-server/instance-administration/user-management/user-groups "mention")) so that the automatic group synchronization can take place properly.
2. After your groups are created, the properties listed in [#group-synchronization](https://docs.sonarsource.com/sonarqube-server/server-installation/system-properties/common-properties#group-synchronization "mention") must be defined to allow SonarQube Server to automatically synchronize the relationships between users and groups.

#### Configuration sample <a href="#configuration-sample" id="configuration-sample"></a>

```properties
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

#### Authentication Methods <a href="#authentication-methods" id="authentication-methods"></a>

* **`Anonymous`** - Used when only read-only access to non-protected entries and attributes is needed when binding to the LDAP server.
* **`Simple`** Simple authentication is not recommended for production deployments not using the LDAP secure protocol since it sends a cleartext password over the network.
* **`CRAM-MD5`** - The Challenge-Response Authentication Method (CRAM), based on the HMAC-MD5 MAC algorithm ([RFC 2195](http://tools.ietf.org/html/rfc2195)).
* **`DIGEST-MD5`** - This is an improvement on the CRAM-MD5 authentication method ([RFC 2831](http://www.ietf.org/rfc/rfc2831.txt)).
* **`GSSAPI`** - GSS-API is Generic Security Service API ([RFC 2744](http://www.ietf.org/rfc/rfc2744.txt)). One of the most popular security services available for GSS-API is the Kerberos v5, used in Microsoft’s Windows 2000 platform.

For a full discussion of LDAP authentication approaches, see [RFC 2829](http://www.ietf.org/rfc/rfc2829.txt) and [RFC 2251](http://www.ietf.org/rfc/rfc2251.txt).

#### Multiple Servers <a href="#multiple-servers" id="multiple-servers"></a>

You can use multiple LDAP servers to manage your users. The purpose is to enable connections for organizations using distinct LDAP servers for different user populations.

{% hint style="warning" %}
You cannot use multiple LDAP servers as a failover cluster. When a user authenticates for the first time via a specific LDAP server, their account is linked to that server. Subsequent authentication by the same user through a different LDAP server will result in the creation of a separate user account, leading to email address conflicts.
{% endhint %}

To configure multiple servers:

```properties
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

Authentication will be tried on each server, in the order they are listed in the configurations until one succeeds.

Note that all the LDAP servers must be available while (re)starting SonarQube Server.

#### Migrate users to a new authentication method <a href="#migrate-users-to-a-new-authentication-method" id="migrate-users-to-a-new-authentication-method"></a>

If you are changing your delegated authentication method and migrating existing users from your previous authentication method, you can use the `/api/v2/users-management/users/{id}` [web API](https://next.sonarqube.com/sonarqube/web_api_v2#/users-management/users/%7Bid%7D--patch) to update your users’ identity provider.

### About user and identity provider IDs <a href="#user-identification" id="user-identification"></a>

To avoid the risk of misidentification, the following identification methods are used on all LDAP setups, including SonarQube Server instances with a single LDAP connection:

* The local login of a new account is made unique with a suffix to the identifier. eg. `login_<additional_id>`.
* The name of the External Identity Provider is also made unique with the addition of the server key provided in the configuration, e.g., `LDAP_<server_key>` where `<server_key>` is defined through `ldap.servers` property.

### Troubleshooting <a href="#troubleshoting" id="troubleshoting"></a>

Detailed connection logs (and potential error codes received from the LDAP server) are output to SonarQube Server’s `<sonarqubeHome>/logs/web.log`, when logging is in `DEBUG` mode.

#### Timeouts <a href="#timeouts" id="timeouts"></a>

If you experience time outs when running SonarQube Server analysis using LDAP, [Java parameters are documented here](http://docs.oracle.com/javase/jndi/tutorial/ldap/connect/config.html). Such parameters can be set in `sonar.web.javaAdditionalOpts` in `<sonarqubeHome>/conf/sonar.properties`.

#### No subject alternative DNS name matching LDAP domain found <a href="#no-subject-alternative-dns-name-matching-ldap-domain-found" id="no-subject-alternative-dns-name-matching-ldap-domain-found"></a>

The following errors:

* `javax.net.ssl.SSLHandshakeException: No subject alternative DNS name matching <LDAP domain> found`
* `java.security.cert.CertificateException: No subject alternative DNS name matching <LDAP domain> found`

are typically caused by an extensive amount of time when following referrals.

To fix the error, try the following:

1. Set `ldap.followReferrals=false`.
2. Ensure that you are using port 3269 and not 636 when using LDAPS.\
   Port 3269 will avoid the referral issue. For more information, see [Why You Shouldn’t Use Port 636 to Bind to LDAP Signing](https://www.nogalis.com/2020/05/18/why-you-shouldnt-use-port-636-to-bind-to-ldap-signing/).

# Source: https://doc.openidentityplatform.org/openam/admin-guide/chap-realms

Title: Configuring Realms :: Open Identity Platform Documentation

URL Source: https://doc.openidentityplatform.org/openam/admin-guide/chap-realms

Markdown Content:
When you first set up a realm, the new realm inherits the data store from the parent realm. Yet, if your administrators are in one realm and your users in another, your new child realm might retrieve users from a different data store.

To Configure a Data Store

1.   An _external identity repository_ is a user store other than the OpenAM embedded repository. Before configuring an OpenAM data store as an external identity repository, make sure that you have prepared the external identity repository for OpenAM. For more information, see ["Preparing an External Identity Repository"](https://doc.openidentityplatform.org/openam/install-guide/chap-prepare-install#prepare-identity-repository) in the _Installation Guide_.

2.   In the OpenAM console, browse to Realms >_Realm Name_> Data Stores.

3.   Click New in the Data Stores table to create a data store profile, and to provide the information needed to connect to the data store.

4.   In the first screen, name the data store and select the type of data store.

Most data stores are directory services, though the Database Repository lets you connect to an SQL database through JDBC.

5.   In the second screen, provide information on how to connect to your data store, and then click Finish to save your work.

See the following sections for hints depending on the type of data store.

    *   ["Hints for Configuring Active Directory Data Stores"](https://doc.openidentityplatform.org/openam/admin-guide/chap-realms#sec-data-stores-active-directory)

    *   ["Hints for Configuring Active Directory Application Mode Data Stores"](https://doc.openidentityplatform.org/openam/admin-guide/chap-realms#sec-data-stores-adam)

    *   ["Hints for Configuring Generic LDAPv3 Data Stores"](https://doc.openidentityplatform.org/openam/admin-guide/chap-realms#sec-data-stores-generic-ldapv3)

    *   ["Hints for Configuring OpenDJ Data Stores"](https://doc.openidentityplatform.org/openam/admin-guide/chap-realms#sec-data-stores-opendj)

    *   ["Hints for Configuring Sun/Oracle DSEE Data Stores"](https://doc.openidentityplatform.org/openam/admin-guide/chap-realms#sec-data-stores-dsee)

    *   ["Hints for Configuring Tivoli Directory Server Data Stores"](https://doc.openidentityplatform.org/openam/admin-guide/chap-realms#sec-data-stores-tivoli)

6.   You must index several directory attributes as a post-configuration step if you configured the data store as follows:

    *   You configured the data store to access an external identity repository.

    *   You used the "Load schema when finished" option.

7.   Click the Subjects tab, and make sure the connection to your new data store is working, by searching for a known identity.

By default the Subjects list only retrieves 100 entries from the data store. Narrow your search if you do not see the identity you are looking for.

8.   If you no longer need the connection to the inherited data store _in this realm_, then you can delete its entry in the Data Stores table.

Also, once you change the data store for a realm, you might opt to change the authentication module configuration to use your realm data store, rather than the inherited settings. See ["Configuring Authentication Modules"](https://doc.openidentityplatform.org/openam/admin-guide/chap-auth-services#configure-authn-modules).

### [](https://doc.openidentityplatform.org/openam/admin-guide/chap-realms#sec-data-stores-active-directory)Hints for Configuring Active Directory Data Stores

Use these hints when configuring Active Directory Data Stores:

`ssoadm` service name: `sunIdentityRepositoryService`

Name
Name for the data store configuration

Load schema when finished
Add appropriate LDAP schema to the directory server when saving the configuration. The LDAP Bind DN user must have access to perform this operation.

This attribute is not available for use with the `ssoadm` command.

Default: false

LDAP Server
`host:port` to contact the directory server, with optional `|server_ID|site_ID` for deployments with multiple servers and sites.

OpenAM uses the optional settings to determine which directory server to contact first. OpenAM tries to contact directory servers in the following priority order, with highest priority first:

1.   The first directory server in the list whose _server\_ID_ matches the current OpenAM server.

2.   The first directory server in the list whose _site\_ID_ matches the current OpenAM server.

3.   The first directory server in the remaining list.

If the directory server is not available, OpenAM proceeds to the next directory server in the list.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-ldap-server`

Default: `host:port` of the initial directory server configured for this OpenAM server.

LDAP Bind DN
Bind DN for connecting to the directory server. Some OpenAM capabilities require write access to directory entries.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-authid`

Default: `CN=Administrator,CN=Users,base-dn`

LDAP Bind Password
Bind password for connecting to the directory server

`ssoadm` attribute: `sun-idrepo-ldapv3-config-authpw`

LDAP Organization DN
The base DN under which to find user and group profiles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-organization_name`

Default: `base-dn`

LDAP SSL/TLS Enabled
Whether to use LDAPS or StartTLS to connect to the directory server. If you enable SSL or StartTLS, OpenAM must be able to trust server certificates, either because the server certificates were signed by a CA whose certificate is already included in the trust store used by the container where OpenAM runs, or because you imported the certificates into the trust store.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-connection-mode`

Possible values: `LDAP`, `LDAPS`, and `StartTLS`

LDAP Connection Pool Maximum Size
Maximum number of connections to the directory server. Make sure the directory service can cope with the maximum number of client connections across all servers.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-connection_pool_max_size`

Default: 10

LDAP Connection Heartbeat Interval
How often to send a heartbeat request to the directory server to ensure that the connection does not remain idle. Some network administrators configure firewalls and load balancers to drop connections that are idle for too long. You can turn this off by setting the value to 0 or to a negative number. To set the units for the interval use LDAP Connection Heartbeat Time Unit.

`ssoadm` attribute: `openam-idrepo-ldapv3-heartbeat-interval`

Default: 10

LDAP Connection Heartbeat Time Unit
Time unit for the LDAP Connection Heartbeat Interval setting.

`ssoadm` attribute: `openam-idrepo-ldapv3-heartbeat-timeunit`

Default: `SECONDS`

Maximum Results Returned from Search
A cap for the number of search results to request. For example, when using the Subjects tab to view profiles, even if you set Configuration > Console > Administration > Maximum Results Returned from Search to a larger number, OpenAM does not exceed this setting. Rather than raise this number, consider narrowing your search to match fewer directory entries.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-max-result`

Default: 1000

Search Timeout
Maximum time to wait for search results in seconds. Does not apply to persistent searches.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-time-limit`

Default: 10

LDAPv3 Plugin Search Scope
LDAP searches can apply to a single entry (SCOPE_BASE), entries directly below the search DN (SCOPE_ONE), or all entries below the search DN (SEARCH_SUB)

`ssoadm` attribute: `sun-idrepo-ldapv3-config-search-scope`

Default: `SCOPE_SUB`

LDAPv3 Repository Plugin Class Name
OpenAM identity repository implementation.

`ssoadm` attribute: `sunIdRepoClass`

Default: `org.forgerock.openam.idrepo.ldap.DJLDAPv3Repo`

Attribute Name Mapping
Map of OpenAM profile attribute names to directory server attribute names.

`ssoadm` attribute: `sunIdRepoAttributeMapping`

Default: `userPassword=unicodePwd`

LDAPv3 Plugin Supported Types and Operations
Map of OpenAM operations that can be performed in the specified OpenAM contexts.

`ssoadm` attribute: `sunIdRepoSupportedOperations`

Default: `group=read,create,edit,delete`, `realm=read,create,edit,delete,service`, `user=read,create,edit,delete`

LDAP Users Search Attribute
When searching for a user by name, match values against this attribute.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-users-search-attribute`

Default: `cn`

Do not modify the value of the search attribute in user profiles. Modifying this attribute value can result in incorrectly cached identity data. For example, if you configure the search attribute to `mail`, it could prevent users from being able to update their email addresses in their user profiles.

LDAP Users Search Filter
When searching for users, apply this LDAP search filter as well.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-users-search-filter`

Default: `(objectclass=person)`

LDAP People Container Naming Attribute
RDN attribute of the LDAP base DN which contains user profiles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-people-container-name`

Default: `cn`

LDAP People Container Value
RDN attribute value of the LDAP base DN which contains user profiles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-people-container-value`

Default: `users`

LDAP User Object Class
User profiles have these LDAP object classes.

OpenAM handles only those attributes listed in this setting. OpenAM discards any such unlisted attributes from requests and the request proceeds without the attribute.

For example, with default settings, if you request that OpenAM execute a search that asks for the `mailAlternateAddress` attribute, OpenAM does the search, but does not request `mailAlternateAddress`. In the same way, OpenAM does perform an update operation with a request to set the value of an unlisted attribute like `mailAlternateAddress`, but it drops the unlisted attribute from the update request.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-user-objectclass`

Default: `organizationalPerson`, `person`, `top`, `User`,

LDAP User Attributes
User profiles have these LDAP attributes.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-user-attributes`

Default: `assignedDashboard`, `cn`, `devicePrintProfiles`, `displayName`, `distinguishedName`, `dn`, `employeeNumber`, `givenName`, `iplanet-am-auth-configuration`, `iplanet-am-session-add-session-listener-on-all-sessions`, `iplanet-am-session-destroy-sessions`, `iplanet-am-session-get-valid-sessions`, `iplanet-am-session-max-caching-time`, `iplanet-am-session-max-idle-time`, `iplanet-am-session-max-session-time`, `iplanet-am-session-quota-limit`, `iplanet-am-session-service-status`, `iplanet-am-user-account-life`, `iplanet-am-user-admin-start-dn`, `iplanet-am-user-alias-list`, `iplanet-am-user-auth-config`, `iplanet-am-user-auth-modules`, `iplanet-am-user-failure-url`, `iplanet-am-user-federation-info-key`, `iplanet-am-user-federation-info`, `iplanet-am-user-login-status`, `iplanet-am-user-password-reset-force-reset`, `iplanet-am-user-password-reset-options`, `iplanet-am-user-password-reset-question-answer`, `iplanet-am-user-success-url`, `mail`, `name`, `objectclass`, `objectGUID`, `postalAddress`, `preferredlanguage`, `preferredLocale`, `preferredtimezone`, `sAMAccountName`, `sn`, `sun-fm-saml2-nameid-info`, `sun-fm-saml2-nameid-infokey`, `sunAMAuthInvalidAttemptsData`, `sunIdentityMSISDNNumber`, `sunIdentityServerDiscoEntries`, `sunIdentityServerPPAddressCard`, `sunIdentityServerPPCommonNameAltCN`, `sunIdentityServerPPCommonNameCN`, `sunIdentityServerPPCommonNameFN`, `sunIdentityServerPPCommonNameMN`, `sunIdentityServerPPCommonNamePT`, `sunIdentityServerPPCommonNameSN`, `sunIdentityServerPPDemographicsAge`, `sunIdentityServerPPDemographicsBirthDay`, `sunIdentityServerPPDemographicsDisplayLanguage`, `sunIdentityServerPPDemographicsLanguage`, `sunIdentityServerPPDemographicsTimeZone`, `sunIdentityServerPPEmergencyContact`, `sunIdentityServerPPEmploymentIdentityAltO`, `sunIdentityServerPPEmploymentIdentityJobTitle`, `sunIdentityServerPPEmploymentIdentityOrg`, `sunIdentityServerPPEncryPTKey`, `sunIdentityServerPPFacadegreetmesound`, `sunIdentityServerPPFacadeGreetSound`, `sunIdentityServerPPFacadeMugShot`, `sunIdentityServerPPFacadeNamePronounced`, `sunIdentityServerPPFacadeWebSite`, `sunIdentityServerPPInformalName`, `sunIdentityServerPPLegalIdentityAltIdType`, `sunIdentityServerPPLegalIdentityAltIdValue`, `sunIdentityServerPPLegalIdentityDOB`, `sunIdentityServerPPLegalIdentityGender`, `sunIdentityServerPPLegalIdentityLegalName`, `sunIdentityServerPPLegalIdentityMaritalStatus`, `sunIdentityServerPPLegalIdentityVATIdType`, `sunIdentityServerPPLegalIdentityVATIdValue`, `sunIdentityServerPPMsgContact`, `sunIdentityServerPPSignKey`, `telephoneNumber`, `unicodePwd`, `userAccountControl`, `userpassword`, `userPrincipalname`

Create User Attribute Mapping
When creating a user profile, apply this map of OpenAM profile attribute names to directory server attribute names.

The LDAP user profile entries require the Common Name (`cn`) and Surname (`sn`) attributes, so that LDAP constraint violations do not occur when performing an add operation.

The `cn` attribute gets its value from the `uid` attribute, which comes from the User Name field on the console’s login page. The `sn` attribute gets the value of the `givenName` attribute. Attributes not mapped to another attribute and attributes mapped to themselves (for example, `cn=cn`) take the value of the username unless the attribute values are provided when creating the profile.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-createuser-attr-mapping`

Default: `cn`, `sn`

Attribute Name of User Status
Attribute to check/set user status.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-isactive`

Default: `userAccountControl`

User Status Active Value
Active users have the user status attribute set to this value.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-active`

Default: 544

User Status Inactive Value
Inactive users have the user status attribute set to this value.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-inactive`

Default: 546

Authentication Naming Attribute
RDN attribute for building the bind DN when given a username and password to authenticate a user against the directory server.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-auth-naming-attr`

Default: `cn`

LDAP Groups Search Attribute
When searching for a group by name, match values against this attribute.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-groups-search-attribute`

Default: `cn`

LDAP Groups Search Filter
When searching for groups, apply this LDAP search filter as well.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-groups-search-filter`

Default: `(objectclass=group)`

LDAP Groups Container Naming Attribute
RDN attribute of the LDAP base DN which contains group profiles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-group-container-name`

Default: `cn`

LDAP Groups Container Value
RDN attribute value of the LDAP base DN which contains group profiles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-group-container-value`

Default: `users`

LDAP Groups Object Class
Group profiles have these LDAP object classes.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-group-objectclass`

Default: `Group`, `top`

LDAP Groups Attributes
Group profiles have these LDAP attributes.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-group-attributes`

Default: `cn`, `distinguishedName`, `dn`, `member`, `name`, `objectCategory`, `objectclass`, `sAMAccountName`, `sAMAccountType`

Attribute Name for Group Membership
LDAP attribute in the member’s LDAP entry whose values are the groups to which a member belongs.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-memberof`

Attribute Name of Unique Member
Attribute in the group’s LDAP entry whose values are the members of the group.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-uniquemember`

Default: `member`

Persistent Search Base DN
Base DN for LDAP-persistent searches used to receive notification of changes in directory server data.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-psearchbase`

Default: `base-dn`

Persistent Search Scope
LDAP searches can apply to a single entry (SCOPE_BASE), entries directly below the search DN (SCOPE_ONE), or all entries below the search DN (SEARCH_SUB).

Specify either `SCOPE_BASE` or `SCOPE_ONE`. Do not specify `SCOPE_SUB`, as it can have a severe impact on Active Directory performance.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-psearch-scope`

Default: `SCOPE_SUB`

The Delay Time Between Retries
How long to wait after receiving an error result that indicates OpenAM should try the LDAP operation again.

`ssoadm` attribute: `com.iplanet.am.ldap.connection.delay.between.retries`

Default: 1000 milliseconds

DN Cache Enabled
Whether to enable the DN cache, which is used to cache DN lookups that can happen in bursts during authentication. As the cache can become stale when a user is moved or renamed, enable DN caching when the directory service allows move/rename operations (Mod DN), and when OpenAM uses persistent searches to obtain notification of such updates.

`ssoadm` attribute: `sun-idrepo-ldapv3-dncache-enabled`

Default: false

DN Cache Size
Maximum number of DNs cached when caching is enabled.

`ssoadm` attribute: `sun-idrepo-ldapv3-dncache-size`

Default: 1500 items

### [](https://doc.openidentityplatform.org/openam/admin-guide/chap-realms#sec-data-stores-adam)Hints for Configuring Active Directory Application Mode Data Stores

Use these hints when configuring Active Directory Application Mode (ADAM) Data Stores. `ssoadm` service name: `sunIdentityRepositoryService`

Name
Name for the data store configuration.

Load schema when finished
Add appropriate LDAP schema to the directory server when saving the configuration. The LDAP Bind DN user must have access to perform this operation.

This attribute is not available for use with the `ssoadm` command.

Default: false

LDAP Server
`host:port` to contact the directory server, with optional `|server_ID|site_ID` for deployments with multiple servers and sites.

OpenAM uses the optional settings to determine which directory server to contact first. OpenAM tries to contact directory servers in the following priority order, with highest priority first:

1.   The first directory server in the list whose _server\_ID_ matches the current OpenAM server.

2.   The first directory server in the list whose _site\_ID_ matches the current OpenAM server.

3.   The first directory server in the remaining list.

If the directory server is not available, OpenAM proceeds to the next directory server in the list.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-ldap-server`

Default: `host:port` of the initial directory server configured for this OpenAM server.

LDAP Bind DN
Bind DN for connecting to the directory server. Some OpenAM capabilities require write access to directory entries.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-authid`

Default: `CN=Administrator,CN=Users,base-dn`

LDAP Bind Password
Bind password for connecting to the directory server.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-authpw`

LDAP Organization DN
The base DN under which to find user and group profiles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-organization_name`

Default: `base-dn`

LDAP SSL/TLS Enabled
Whether to use LDAPS or StartTLS to connect to the directory server. If you enable SSL or StartTLS, OpenAM must be able to trust server certificates, either because the server certificates were signed by a CA whose certificate is already included in the trust store used by the container where OpenAM runs, or because you imported the certificates into the trust store.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-connection-mode`

Possible values: `LDAP`, `LDAPS`, and `StartTLS`

LDAP Connection Pool Maximum Size
Maximum number of connections to the directory server. Make sure the directory service can cope with the maximum number of client connections across all servers.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-connection_pool_max_size`

Default: 10

LDAP Connection Heartbeat Interval
How often to send a heartbeat request to the directory server to ensure that the connection does not remain idle. Some network administrators configure firewalls and load balancers to drop connections that are idle for too long. You can turn this off by setting the value to 0 or to a negative number. To set the units for the interval, use LDAP Connection Heartbeat Time Unit.

`ssoadm` attribute: `openam-idrepo-ldapv3-heartbeat-interval`

Default: 10

LDAP Connection Heartbeat Time Unit
Time unit for the LDAP Connection Heartbeat Interval setting

`ssoadm` attribute: `openam-idrepo-ldapv3-heartbeat-timeunit`

Default: `second`

Maximum Results Returned from Search
A cap for the number of search results to request. For example, when using the Subjects tab to view profiles, even if you set Configuration > Console > Administration > Maximum Results Returned from Search to a larger number, OpenAM does not exceed this setting. Rather than raise this number, consider narrowing your search to match fewer directory entries.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-max-result`

Default: 1000

Search Timeout
Maximum time to wait for search results in seconds. Does not apply to persistent searches.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-time-limit`

Default: 10

LDAPv3 Plugin Search Scope
LDAP searches can apply to a single entry (SCOPE_BASE), entries directly below the search DN (SCOPE_ONE), or all entries below the search DN (SEARCH_SUB).

`ssoadm` attribute: `sun-idrepo-ldapv3-config-search-scope`

Default: `SCOPE_SUB`

LDAPv3 Repository Plugin Class Name
OpenAM identity repository implementation.

`ssoadm` attribute: `sunIdRepoClass`

Default: `org.forgerock.openam.idrepo.ldap.DJLDAPv3Repo`

Attribute Name Mapping
Map of OpenAM profile attribute names to directory server attribute names.

`ssoadm` attribute: `sunIdRepoAttributeMapping`

Default: `userPassword=unicodePwd`

LDAPv3 Plugin Supported Types and Operations
Map of OpenAM operations that can be performed in the specified OpenAM contexts.

`ssoadm` attribute: `sunIdRepoSupportedOperations`

Default: `group=read,create,edit,delete`, `realm=read,create,edit,delete,service`, `user=read,create,edit,delete`

LDAP Users Search Attribute
When searching for a user by name, match values against this attribute.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-users-search-attribute`

Default: `cn`

Do not modify the value of the search attribute in user profiles. Modifying this attribute value can result in incorrectly cached identity data. For example, if you configure the search attribute to `mail`, it could prevent users from being able to update their email addresses in their user profiles.

LDAP Users Search Filter
When searching for users, apply this LDAP search filter as well.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-users-search-filter`

Default: `(objectclass=person)`

LDAP People Container Naming Attribute
RDN attribute of the LDAP base DN which contains user profiles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-people-container-name`

LDAP People Container Value
RDN attribute value of the LDAP base DN which contains user profiles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-people-container-value`

LDAP User Object Class
User profiles have these LDAP object classes.

OpenAM handles only those attributes listed in this setting. OpenAM discards any unlisted attributes from requests and the request proceeds without the attribute.

For example, with default settings, if you request that OpenAM execute a search that asks for the `mailAlternateAddress` attribute, OpenAM does the search, but does not request `mailAlternateAddress`. In the same way, OpenAM does perform an update operation with a request to set the value of an unlisted attribute like `mailAlternateAddress`, but it drops the unlisted attribute from the update request.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-user-objectclass`

Default: `devicePrintProfilesContainer`, `forgerock-am-dashboard-service`, `iplanet-am-auth-configuration-service`, `iplanet-am-managed-person`, `iplanet-am-user-service`, `iPlanetPreferences`, `organizationalPerson`, `person`, `sunAMAuthAccountLockout`, `sunFederationManagerDataStore`, `sunFMSAML2NameIdentifier`, `sunIdentityServerLibertyPPService`, `top`, `User`

LDAP User Attributes
User profiles have these LDAP attributes.

OpenAM handles only those attributes listed in this setting. OpenAM discards any unlisted attributes from requests and the request proceeds without the attribute.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-user-attributes`

Default: `assignedDashboard`, `cn`, `devicePrintProfiles`, `displayName`, `distinguishedName`, `dn`, `employeeNumber`, `givenName`, `iplanet-am-auth-configuration`, `iplanet-am-session-add-session-listener-on-all-sessions`, `iplanet-am-session-destroy-sessions`, `iplanet-am-session-get-valid-sessions`, `iplanet-am-session-max-caching-time`, `iplanet-am-session-max-idle-time`, `iplanet-am-session-max-session-time`, `iplanet-am-session-quota-limit`, `iplanet-am-session-service-status`, `iplanet-am-user-account-life`, `iplanet-am-user-admin-start-dn`, `iplanet-am-user-alias-list`, `iplanet-am-user-auth-config`, `iplanet-am-user-auth-modules`, `iplanet-am-user-failure-url`, `iplanet-am-user-federation-info-key`, `iplanet-am-user-federation-info`, `iplanet-am-user-login-status`, `iplanet-am-user-password-reset-force-reset`, `iplanet-am-user-password-reset-options`, `iplanet-am-user-password-reset-question-answer`, `iplanet-am-user-success-url`, `mail`, `name`, `objectclass`, `objectGUID`, `postalAddress`, `preferredlanguage`, `preferredLocale`, `preferredtimezone`, `sAMAccountName`, `sn`, `sun-fm-saml2-nameid-info`, `sun-fm-saml2-nameid-infokey`, `sunAMAuthInvalidAttemptsData`, `sunIdentityMSISDNNumber`, `sunIdentityServerDiscoEntries`, `sunIdentityServerPPAddressCard`, `sunIdentityServerPPCommonNameAltCN`, `sunIdentityServerPPCommonNameCN`, `sunIdentityServerPPCommonNameFN`, `sunIdentityServerPPCommonNameMN`, `sunIdentityServerPPCommonNamePT`, `sunIdentityServerPPCommonNameSN`, `sunIdentityServerPPDemographicsAge`, `sunIdentityServerPPDemographicsBirthDay`, `sunIdentityServerPPDemographicsDisplayLanguage`, `sunIdentityServerPPDemographicsLanguage`, `sunIdentityServerPPDemographicsTimeZone`, `sunIdentityServerPPEmergencyContact`, `sunIdentityServerPPEmploymentIdentityAltO`, `sunIdentityServerPPEmploymentIdentityJobTitle`, `sunIdentityServerPPEmploymentIdentityOrg`, `sunIdentityServerPPEncryPTKey`, `sunIdentityServerPPFacadegreetmesound`, `sunIdentityServerPPFacadeGreetSound`, `sunIdentityServerPPFacadeMugShot`, `sunIdentityServerPPFacadeNamePronounced`, `sunIdentityServerPPFacadeWebSite`, `sunIdentityServerPPInformalName`, `sunIdentityServerPPLegalIdentityAltIdType`, `sunIdentityServerPPLegalIdentityAltIdValue`, `sunIdentityServerPPLegalIdentityDOB`, `sunIdentityServerPPLegalIdentityGender`, `sunIdentityServerPPLegalIdentityLegalName`, `sunIdentityServerPPLegalIdentityMaritalStatus`, `sunIdentityServerPPLegalIdentityVATIdType`, `sunIdentityServerPPLegalIdentityVATIdValue`, `sunIdentityServerPPMsgContact`, `sunIdentityServerPPSignKey`, `telephoneNumber`, `unicodePwd`, `userAccountControl`, `userpassword`, `userPrincipalname`

Create User Attribute Mapping
When creating a user profile, apply this map of OpenAM profile attribute names to directory server attribute names.

Attributes not mapped to another attribute (for example, `cn`) and attributes mapped to themselves, (for example, `cn=cn`) take the value of the username unless the attribute values are provided when creating the profile. The object classes for user profile LDAP entries generally require Common Name (cn) and Surname (sn) attributes, so this prevents an LDAP constraint violation when performing the add operation.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-createuser-attr-mapping`

Default: `cn`, `sn`

Attribute Name of User Status
Attribute to check/set user status.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-isactive`

Default: `msDS-UserAccountDisabled`

User Status Active Value
Active users have the user status attribute set to this value.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-active`

Default: FALSE

User Status Inactive Value
Inactive users have the user status attribute set to this value.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-inactive`

Default: TRUE

Authentication Naming Attribute
RDN attribute for building the bind DN when given a username and password to authenticate a user against the directory server.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-auth-naming-attr`

Default: `cn`

LDAP Groups Search Attribute
When searching for a group by name, match values against this attribute.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-groups-search-attribute`

Default: `cn`

LDAP Groups Search Filter
When searching for groups, apply this LDAP search filter as well.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-groups-search-filter`

Default: `(objectclass=group)`

LDAP Groups Container Naming Attribute
RDN attribute of the LDAP base DN which contains group profiles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-group-container-name`

Default: `cn`

LDAP Groups Container Value
RDN attribute value of the LDAP base DN which contains group profiles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-group-container-value`

LDAP Groups Object Class
Group profiles have these LDAP object classes.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-group-objectclass`

Default: `Group`, `top`

LDAP Groups Attributes
Group profiles have these LDAP attributes.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-group-attributes`

Default: `cn`, `distinguishedName`, `dn`, `member`, `name`, `objectCategory`, `objectclass`, `sAMAccountName`, `sAMAccountType`

Attribute Name for Group Membership
LDAP attribute in the member’s LDAP entry whose values are the groups to which a member belongs.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-memberof`

Attribute Name of Unique Member
Attribute in the group’s LDAP entry whose values are the members of the group.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-uniquemember`

Default: `member`

Persistent Search Base DN
Base DN for LDAP-persistent searches used to receive notification of changes in directory server data.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-psearchbase`

Default: `base-dn`

Persistent Search Scope
LDAP searches can apply to a single entry (SCOPE_BASE), entries directly below the search DN (SCOPE_ONE), or all entries below the search DN (SEARCH_SUB).

Specify either `SCOPE_BASE` or `SCOPE_ONE`. Do not specify `SCOPE_SUB`, as it can have a severe impact on Active Directory performance.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-psearch-scope`

Default: `SCOPE_SUB`

The Delay Time Between Retries
How long to wait after receiving an error result that indicates OpenAM should try the LDAP operation again.

`ssoadm` attribute: `com.iplanet.am.ldap.connection.delay.between.retries`

Default: 1000 milliseconds

DN Cache Enabled
Whether to enable the DN cache, which is used to cache DN lookups that can happen in bursts during authentication. As the cache can become stale when a user is moved or renamed, enable DN caching when the directory service allows move/rename operations (Mod DN), and when OpenAM uses persistent searches to obtain notification of such updates.

`ssoadm` attribute: `sun-idrepo-ldapv3-dncache-enabled`

Default: false

DN Cache Size
Maximum number of DNs cached when caching is enabled.

`ssoadm` attribute: `sun-idrepo-ldapv3-dncache-size`

Default: 1500 items

### [](https://doc.openidentityplatform.org/openam/admin-guide/chap-realms#sec-data-stores-generic-ldapv3)Hints for Configuring Generic LDAPv3 Data Stores

Use these hints when configuring Generic LDAPv3 compliant data stores. `ssoadm` service name: `sunIdentityRepositoryService`

Name
Name for the data store configuration.

Load schema when finished
Add appropriate LDAP schema to the directory server when saving the configuration. The LDAP Bind DN user must have access to perform this operation.

This attribute is not available for use with the `ssoadm` command.

Default: false

LDAP Server
`host:port` to contact the directory server, with optional `|server_ID|site_ID` for deployments with multiple servers and sites.

OpenAM uses the optional settings to determine which directory server to contact first. OpenAM tries to contact directory servers in the following priority order, with highest priority first:

1.   The first directory server in the list whose _server\_ID_ matches the current OpenAM server.

2.   The first directory server in the list whose _site\_ID_ matches the current OpenAM server.

3.   The first directory server in the remaining list.

If the directory server is not available, OpenAM proceeds to the next directory server in the list.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-ldap-server`

Default: `host:port` of the initial directory server configured for this OpenAM server

LDAP Bind DN
Bind DN for connecting to the directory server. Some OpenAM capabilities require write access to directory entries.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-authid`

LDAP Bind Password
Bind password for connecting to the directory server.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-authpw`

LDAP Organization DN
The base DN under which to find user and group profiles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-organization_name`

Default: `base-dn`

LDAP SSL/TLS Enabled
Whether to use LDAPS or StartTLS to connect to the directory server. If you enable SSL or StartTLS, OpenAM must be able to trust server certificates, either because the server certificates were signed by a CA whose certificate is already included in the trust store used by the container where OpenAM runs, or because you imported the certificates into the trust store.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-connection-mode`

Possible values: `LDAP`, `LDAPS`, and `StartTLS`

LDAP Connection Pool Maximum Size
Maximum number of connections to the directory server. Make sure the directory service can cope with the maximum number of client connections across all servers.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-connection_pool_max_size`

Default: 10

LDAP Connection Heartbeat Interval
How often to send a heartbeat request to the directory server to ensure that the connection does not remain idle. Some network administrators configure firewalls and load balancers to drop connections that are idle for too long. You can turn this off by setting the value to 0 or to a negative number. To set the units for the interval, use LDAP Connection Heartbeat Time Unit.

`ssoadm` attribute: `openam-idrepo-ldapv3-heartbeat-interval`

Default: 10

LDAP Connection Heartbeat Time Unit
Time unit for the LDAP Connection Heartbeat Interval setting.

`ssoadm` attribute: `openam-idrepo-ldapv3-heartbeat-timeunit`

Default: `second`

Maximum Results Returned from Search
A cap for the number of search results to request. For example, when using the Subjects tab to view profiles, even if you set Configuration > Console > Administration > Maximum Results Returned from Search to a larger number, OpenAM does not exceed this setting. Rather than raise this number, consider narrowing your search to match fewer directory entries.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-max-result`

Default: 1000

Search Timeout
Maximum time to wait for search results in seconds. Does not apply to persistent searches.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-time-limit`

Default: 10

LDAPv3 Plugin Search Scope
LDAP searches can apply to a single entry (SCOPE_BASE), entries directly below the search DN (SCOPE_ONE), or all entries below the search DN (SEARCH_SUB).

`ssoadm` attribute: `sun-idrepo-ldapv3-config-search-scope`

Default: `SCOPE_SUB`

LDAPv3 Repository Plugin Class Name
OpenAM identity repository implementation.

`ssoadm` attribute: `sunIdRepoClass`

Default: `org.forgerock.openam.idrepo.ldap.DJLDAPv3Repo`

Attribute Name Mapping
Map of OpenAM profile attribute names to directory server attribute names.

`ssoadm` attribute: `sunIdRepoAttributeMapping`

LDAPv3 Plugin Supported Types and Operations
Map of OpenAM operations that can be performed in the specified OpenAM contexts.

`ssoadm` attribute: `sunIdRepoSupportedOperations`

Default: `realm=read,create,edit,delete,service`, `user=read,create,edit,delete`, `group=read,create,edit,delete`

LDAP Users Search Attribute
When searching for a user by name, match values against this attribute.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-users-search-attribute`

Default: `uid`

Do not modify the value of the search attribute in user profiles. Modifying this attribute value can result in incorrectly cached identity data. For example, if you configure the search attribute to `mail`, it could prevent users from being able to update their email addresses in their user profiles.

LDAP Users Search Filter
When searching for users, apply this LDAP search filter as well.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-users-search-filter`

Default: `(objectclass=inetorgperson)`

LDAP People Container Naming Attribute
RDN attribute of the LDAP base DN which contains user profiles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-people-container-name`

LDAP People Container Value
RDN attribute value of the LDAP base DN which contains user profiles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-people-container-value`

LDAP User Object Class
User profiles have these LDAP object classes.

OpenAM handles only those attributes listed in this setting. OpenAM discards any unlisted attributes from requests and the request proceeds without the attribute.

For example, with default settings, if you request that OpenAM execute a search that asks for the `mailAlternateAddress` attribute, OpenAM does the search, but does not request `mailAlternateAddress`. In the same way, OpenAM does perform an update operation with a request to set the value of an unlisted attribute like `mailAlternateAddress`, but it drops the unlisted attribute from the update request.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-user-objectclass`

Default: `inetorgperson`, `inetUser`, `organizationalPerson`, `person`, `top`,

LDAP User Attributes
User profiles have these LDAP attributes.

OpenAM handles only those attributes listed in this setting. OpenAM discards any unlisted attributes from requests and the request proceeds without the attribute.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-user-attributes`

Default: `uid`, `caCertificate`, `authorityRevocationList`, `inetUserStatus`, `mail`, `sn`, `manager`, `userPassword`, `adminRole`, `objectClass`, `givenName`, `memberOf`, `cn`, `telephoneNumber`, `preferredlanguage`, `userCertificate`, `postalAddress`, `dn`, `employeeNumber`, `distinguishedName`

Create User Attribute Mapping
When creating a user profile, apply this map of OpenAM profile attribute names to directory server attribute names.

Attributes not mapped to another attribute (for example, `cn`) and attributes mapped to themselves (for example, `cn=cn`) take the value of the username unless the attribute values are provided when creating the profile. The object classes for user profile LDAP entries generally require Common Name (cn) and Surname (sn) attributes, so this prevents an LDAP constraint violation when performing the add operation.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-createuser-attr-mapping`

Default: `cn`, `sn`

Attribute Name of User Status
Attribute to check/set user status.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-isactive`

Default: `inetuserstatus`

User Status Active Value
Active users have the user status attribute set to this value.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-active`

Default: `Active`

User Status Inactive Value
Inactive users have the user status attribute set to this value.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-inactive`

Default: `Inactive`

Authentication Naming Attribute
RDN attribute for building the bind DN when given a username and password to authenticate a user against the directory server.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-auth-naming-attr`

Default: `uid`

LDAP Groups Search Attribute
When searching for a group by name, match values against this attribute.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-groups-search-attribute`

Default: `cn`

LDAP Groups Search Filter
When searching for groups, apply this LDAP search filter as well.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-groups-search-filter`

Default: `(objectclass=groupOfUniqueNames)`

LDAP Groups Container Naming Attribute
RDN attribute of the LDAP base DN which contains group profiles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-group-container-name`

Default: `ou`

LDAP Groups Container Value
RDN attribute value of the LDAP base DN which contains group profiles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-group-container-value`

Default: `groups`

LDAP Groups Object Class
Group profiles have these LDAP object classes.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-group-objectclass`

Default: `groupofuniquenames`, `top`

LDAP Groups Attributes
Group profiles have these LDAP attributes.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-group-attributes`

Default: `ou`, `cn`, `description`, `dn`, `objectclass`, `uniqueMember`

Attribute Name for Group Membership
LDAP attribute in the member’s LDAP entry whose values are the groups to which a member belongs.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-memberof`

Attribute Name of Unique Member
Attribute in the group’s LDAP entry whose values are the members of the group.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-uniquemember`

Default: `uniqueMember`

Attribute Name of Group Member URL
Attribute in the dynamic group’s LDAP entry whose value is a URL specifying the members of the group.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-memberurl`

Default: `memberUrl`

Default Group Member’s User DN
DN of member added to all newly created groups.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-dftgroupmember`

Persistent Search Base DN
Base DN for LDAP-persistent searches used to receive notification of changes in directory server data.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-psearchbase`

Default: `base-dn`

Persistent Search Filter
LDAP filter to apply when performing persistent searches.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-psearch-filter`

Default: `(objectclass=*)`

Persistent Search Scope
LDAP searches can apply to a single entry (SCOPE_BASE), entries directly below the search DN (SCOPE_ONE), or all entries below the search DN (SEARCH_SUB).

`ssoadm` attribute: `sun-idrepo-ldapv3-config-psearch-scope`

Default: `SCOPE_SUB`

The Delay Time Between Retries
How long to wait after receiving an error result that indicates OpenAM should try the LDAP operation again.

`ssoadm` attribute: `com.iplanet.am.ldap.connection.delay.between.retries`

Default: 1000 milliseconds

DN Cache Enabled
Whether to enable the DN cache, which is used to cache DN lookups that can happen in bursts during authentication. As the cache can become stale when a user is moved or renamed, enable DN caching when the directory service allows move/rename operations (Mod DN), and when OpenAM uses persistent searches to obtain notification of such updates.

`ssoadm` attribute: `sun-idrepo-ldapv3-dncache-enabled`

Default: false

DN Cache Size
Maximum number of DNs cached when caching is enabled.

`ssoadm` attribute: `sun-idrepo-ldapv3-dncache-size`

Default: 1500 items

### [](https://doc.openidentityplatform.org/openam/admin-guide/chap-realms#sec-data-stores-opendj)Hints for Configuring OpenDJ Data Stores

Use these hints when configuring OpenDJ data stores. `ssoadm` service name: `sunIdentityRepositoryService`

Name
Name for the data store configuration.

Load schema when finished
Add appropriate LDAP schema to the directory server when saving the configuration. The LDAP Bind DN user must have access to perform this operation.

This attribute is not available for use with the `ssoadm` command.

Default: false

LDAP Server
`host:port` to contact the directory server, with optional `|server_ID|site_ID` for deployments with multiple servers and sites.

OpenAM uses the optional settings to determine which directory server to contact first. OpenAM tries to contact directory servers in the following priority order, with highest priority first:

1.   The first directory server in the list whose _server\_ID_ matches the current OpenAM server.

2.   The first directory server in the list whose _site\_ID_ matches the current OpenAM server.

3.   The first directory server in the remaining list.

If the directory server is not available, OpenAM proceeds to the next directory server in the list.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-ldap-server`

Default: `host:port` of the initial directory server configured for this OpenAM server

LDAP Bind DN
Bind DN for connecting to the directory server. Some OpenAM capabilities require write access to directory entries.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-authid`

LDAP Bind Password
Bind password for connecting to the directory server.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-authpw`

LDAP Organization DN
The base DN under which to find user and group profiles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-organization_name`

Default: `base-dn`

LDAP SSL/TLS Enabled
Whether to use LDAPS or StartTLS to connect to the directory server. If you enable SSL or StartTLS, OpenAM must be able to trust server certificates, either because the server certificates were signed by a CA whose certificate is already included in the trust store used by the container where OpenAM runs, or because you imported the certificates into the trust store.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-connection-mode`

Possible values: `LDAP`, `LDAPS`, and `StartTLS`

LDAP Connection Pool Maximum Size
Maximum number of connections to the directory server. Make sure the directory service can cope with the maximum number of client connections across all servers.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-connection_pool_max_size`

Default: 10

LDAP Connection Heartbeat Interval
How often to send a heartbeat request to the directory server to ensure that the connection does not remain idle. Some network administrators configure firewalls and load balancers to drop connections that are idle for too long. You can turn this off by setting the value to 0 or to a negative number. To set the units for the interval, use LDAP Connection Heartbeat Time Unit.

`ssoadm` attribute: `openam-idrepo-ldapv3-heartbeat-interval`

Default: 10

LDAP Connection Heartbeat Time Unit
Time unit for the LDAP Connection Heartbeat Interval setting.

`ssoadm` attribute: `openam-idrepo-ldapv3-heartbeat-timeunit`

Default: `second`

Maximum Results Returned from Search
A cap for the number of search results to request. For example, when using the Subjects tab to view profiles, even if you set Configuration > Console > Administration > Maximum Results Returned from Search to a larger number, OpenAM does not exceed this setting. Rather than raise this number, consider narrowing your search to match fewer directory entries.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-max-result`

Default: 1000

Search Timeout
Maximum time to wait for search results in seconds. Does not apply to persistent searches.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-time-limit`

Default: 10

LDAPv3 Plugin Search Scope
LDAP searches can apply to a single entry (SCOPE_BASE), entries directly below the search DN (SCOPE_ONE), or all entries below the search DN (SEARCH_SUB).

`ssoadm` attribute: `sun-idrepo-ldapv3-config-search-scope`

Default: `SCOPE_SUB`

LDAPv3 Repository Plugin Class Name
OpenAM identity repository implementation.

`ssoadm` attribute: `sunIdRepoClass`

Default: `org.forgerock.openam.idrepo.ldap.DJLDAPv3Repo`

Attribute Name Mapping
Map of OpenAM profile attribute names to directory server attribute names.

`ssoadm` attribute: `sunIdRepoAttributeMapping`

LDAPv3 Plugin Supported Types and Operations
Map of OpenAM operations that can be performed in the specified OpenAM contexts.

`ssoadm` attribute: `sunIdRepoSupportedOperations`

Default: `realm=read,create,edit,delete,service`, `user=read,create,edit,delete`, `group=read,create,edit,delete`

LDAP Users Search Attribute
When searching for a user by name, match values against this attribute.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-users-search-attribute`

Default: `uid`

Do not modify the value of the search attribute in user profiles. Modifying this attribute value can result in incorrectly cached identity data. For example, if you configure the search attribute to `mail`, it could prevent users from being able to update their email addresses in their user profiles.

LDAP Users Search Filter
When searching for users, apply this LDAP search filter as well.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-users-search-filter`

Default: `(objectclass=inetorgperson)`

LDAP People Container Naming Attribute
RDN attribute of the LDAP base DN which contains user profiles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-people-container-name`

Default: `ou`

LDAP People Container Value
RDN attribute value of the LDAP base DN which contains user profiles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-people-container-value`

Default: `people`

LDAP User Object Class
User profiles have these LDAP object classes.

OpenAM handles only those attributes listed in this setting. OpenAM discards any unlisted attributes from requests and the request proceeds without the attribute.

For example, with default settings, if you request that OpenAM execute a search that asks for the `mailAlternateAddress` attribute, OpenAM does the search, but does not request `mailAlternateAddress`. In the same way, OpenAM does perform an update operation with a request to set the value of an unlisted attribute like `mailAlternateAddress`, but it drops the unlisted attribute from the update request.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-user-objectclass`

Default: `devicePrintProfilesContainer`, `forgerock-am-dashboard-service`, `inetorgperson`, `inetuser`, `iplanet-am-auth-configuration-service`, `iplanet-am-managed-person`, `iplanet-am-user-service`, `iPlanetPreferences`, `organizationalperson`, `person`, `sunAMAuthAccountLockout`, `sunFederationManagerDataStore`, `sunFMSAML2NameIdentifier`, `sunIdentityServerLibertyPPService`, `top`

LDAP User Attributes
User profiles have these LDAP attributes.

OpenAM handles only those attributes listed in this setting. OpenAM discards any unlisted attributes from requests and the request proceeds without the attribute.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-user-attributes`

Default: `sunIdentityServerPPDemographicsBirthDay`, `uid`, `sunIdentityServerPPLegalIdentityLegalName`, `manager`, `assignedDashboard`, `sunIdentityServerPPCommonNameSN`, `userPassword`, `iplanet-am-session-get-valid-sessions`, `sunIdentityServerPPEmploymentIdentityJobTitle`, `iplanet-am-user-password-reset-question-answer`, `sunIdentityServerPPLegalIdentityDOB`, `sunIdentityServerPPEmergencyContact`, `sunIdentityServerPPCommonNameCN`, `iplanet-am-user-success-url`, `iplanet-am-user-admin-start-dn`, `iplanet-am-user-federation-info`, `userCertificate`, `sunIdentityServerPPFacadeGreetSound`, `sunAMAuthInvalidAttemptsData`, `sunIdentityServerPPFacadeNamePronounced`, `distinguishedName`, `sunIdentityServerPPDemographicsTimeZone`, `sunIdentityMSISDNNumber`, `iplanet-am-session-max-caching-time`, `sn`, `iplanet-am-session-quota-limit`, `iplanet-am-session-max-session-time`, `adminRole`, `sunIdentityServerPPEmploymentIdentityAltO`, `objectClass`, `sun-fm-saml2-nameid-info`, `sunIdentityServerPPLegalIdentityMaritalStatus`, `iplanet-am-user-login-status`, `sunIdentityServerPPLegalIdentityAltIdType`, `devicePrintProfiles`, `iplanet-am-session-max-idle-time`, `sunIdentityServerPPFacadegreetmesound`, `cn`, `iplanet-am-user-password-reset-options`, `telephoneNumber`, `preferredlanguage`, `iplanet-am-user-federation-info-key`, `sunIdentityServerPPMsgContact`, `sunIdentityServerPPLegalIdentityGender`, `iplanet-am-user-alias-list`, `sunIdentityServerPPCommonNameFN`, `caCertificate`, `inetUserStatus`, `sunIdentityServerPPCommonNameMN`, `sunIdentityServerPPEncryPTKey`, `givenName`, `memberOf`, `sunIdentityServerPPLegalIdentityVATIdValue`, `preferredLocale`, `iplanet-am-session-service-status`, `sun-fm-saml2-nameid-infokey`, `sunIdentityServerPPDemographicsAge`, `sunIdentityServerDiscoEntries`, `sunIdentityServerPPLegalIdentityVATIdType`, `iplanet-am-user-auth-config`, `iplanet-am-user-failure-url`, `sunIdentityServerPPAddressCard`, `sunIdentityServerPPCommonNamePT`, `dn`, `iplanet-am-session-add-session-listener-on-all-sessions`, `mail`, `authorityRevocationList`, `iplanet-am-user-password-reset-force-reset`, `inetUserHttpURL`, `sunIdentityServerPPLegalIdentityAltIdValue`, `sunIdentityServerPPCommonNameAltCN`, `preferredtimezone`, `sunIdentityServerPPInformalName`, `sunIdentityServerPPSignKey`, `sunIdentityServerPPEmploymentIdentityOrg`, `iplanet-am-session-destroy-sessions`, `sunIdentityServerPPFacadeMugShot`, `sunIdentityServerPPFacadeWebSite`, `sunIdentityServerPPDemographicsDisplayLanguage`, `postalAddress`, `iplanet-am-auth-configuration`, `employeeNumber`, `iplanet-am-user-account-life`, `iplanet-am-user-auth-modules`, `sunIdentityServerPPDemographicsLanguage`

Create User Attribute Mapping
When creating a user profile, apply this map of OpenAM profile attribute names to directory server attribute names.

Attributes not mapped to another attribute (for example, `cn`) and attributes mapped to themselves (for example, `cn=cn`) take the value of the username unless the attribute values are provided when creating the profile. The object classes for user profile LDAP entries generally require Common Name (cn) and Surname (sn) attributes, so this prevents an LDAP constraint violation when performing the add operation.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-createuser-attr-mapping`

Default: `cn`, `sn`

Attribute Name of User Status
Attribute to check/set user status.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-isactive`

Default: `inetuserstatus`

User Status Active Value
Active users have the user status attribute set to this value.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-active`

Default: `Active`

User Status Inactive Value
Inactive users have the user status attribute set to this value.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-inactive`

Default: `Inactive`

Authentication Naming Attribute
RDN attribute for building the bind DN when given a username and password to authenticate a user against the directory server.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-auth-naming-attr`

Default: `uid`

LDAP Groups Search Attribute
When searching for a group by name, match values against this attribute.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-groups-search-attribute`

Default: `cn`

LDAP Groups Search Filter
When searching for groups, apply this LDAP search filter as well.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-groups-search-filter`

Default: `(objectclass=groupOfUniqueNames)`

LDAP Groups Container Naming Attribute
RDN attribute of the LDAP base DN which contains group profiles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-group-container-name`

Default: `ou`

LDAP Groups Container Value
RDN attribute value of the LDAP base DN which contains group profiles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-group-container-value`

Default: `groups`

LDAP Groups Object Class
Group profiles have these LDAP object classes.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-group-objectclass`

Default: `groupofuniquenames`, `top`

LDAP Groups Attributes
Group profiles have these LDAP attributes.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-group-attributes`

Default: `cn`, `dn`, `objectclass`, `uniqueMember`

Attribute Name for Group Membership
LDAP attribute in the member’s LDAP entry whose values are the groups to which a member belongs.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-memberof`

Attribute Name of Unique Member
Attribute in the group’s LDAP entry whose values are the members of the group.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-uniquemember`

Default: `uniqueMember`

Persistent Search Base DN
Base DN for LDAP-persistent searches used to receive notification of changes in directory server data.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-psearchbase`

Default: `base-dn`

Persistent Search Filter
LDAP filter to apply when performing persistent searches.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-psearch-filter`

Default: `(objectclass=*)`

Persistent Search Scope
LDAP searches can apply to a single entry (SCOPE_BASE), entries directly below the search DN (SCOPE_ONE), or all entries below the search DN (SEARCH_SUB).

`ssoadm` attribute: `sun-idrepo-ldapv3-config-psearch-scope`

Default: `SCOPE_SUB`

The Delay Time Between Retries
How long to wait after receiving an error result that indicates OpenAM should try the LDAP operation again.

The OpenDJ data store uses this setting only for persistent searches.

`ssoadm` attribute: `com.iplanet.am.ldap.connection.delay.between.retries`

Default: 1000 milliseconds

DN Cache Enabled
Whether to enable the DN cache, which is used to cache DN lookups that can happen in bursts during authentication. As the cache can become stale when a user is moved or renamed, enable DN caching when the directory service allows move/rename operations (Mod DN), and when OpenAM uses persistent searches to obtain notification of such updates.

`ssoadm` attribute: `sun-idrepo-ldapv3-dncache-enabled`

Default: true

DN Cache Size
Maximum number of DNs cached when caching is enabled.

`ssoadm` attribute: `sun-idrepo-ldapv3-dncache-size`

Default: 1500 items

### [](https://doc.openidentityplatform.org/openam/admin-guide/chap-realms#sec-data-stores-dsee)Hints for Configuring Sun/Oracle DSEE Data Stores

Use these hints when configuring Data Stores for Oracle DSEE or Sun DSEE using OpenAM schema. `ssoadm` service name: `sunIdentityRepositoryService`

Name
Name for the data store configuration.

Load schema when finished
Add appropriate LDAP schema to the directory server when saving the configuration. The LDAP Bind DN user must have access to perform this operation.

This attribute is not available for use with the `ssoadm` command.

Default: false

LDAP Server
`host:port` to contact the directory server, with optional `|server_ID|site_ID` for deployments with multiple servers and sites.

OpenAM uses the optional settings to determine which directory server to contact first. OpenAM tries to contact directory servers in the following priority order, with highest priority first:

1.   The first directory server in the list whose _server\_ID_ matches the current OpenAM server.

2.   The first directory server in the list whose _site\_ID_ matches the current OpenAM server.

3.   The first directory server in the remaining list.

If the directory server is not available, OpenAM proceeds to the next directory server in the list.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-ldap-server`

Default: `host:port` of the initial directory server configured for this OpenAM server.

LDAP Bind DN
Bind DN for connecting to the directory server. Some OpenAM capabilities require write access to directory entries.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-authid`

Default: `cn=dsameuser,ou=DSAME Users,base-dn`

LDAP Bind Password
Bind password for connecting to the directory server.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-authpw`

LDAP Organization DN
The base DN under which to find user and group profiles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-organization_name`

Default: `base-dn`

LDAP SSL/TLS Enabled
Whether to use LDAPS or StartTLS to connect to the directory server. If you enable SSL or StartTLS, OpenAM must be able to trust server certificates, either because the server certificates were signed by a CA whose certificate is already included in the trust store used by the container where OpenAM runs, or because you imported the certificates into the trust store.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-connection-mode`

Possible values: `LDAP`, `LDAPS`, and `StartTLS`

LDAP Connection Pool Maximum Size
Maximum number of connections to the directory server. Make sure the directory service can cope with the maximum number of client connections across all servers.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-connection_pool_max_size`

Default: 10

LDAP Connection Heartbeat Interval
How often to send a heartbeat request to the directory server to ensure that the connection does not remain idle. Some network administrators configure firewalls and load balancers to drop connections that are idle for too long. You can turn this off by setting the value to 0 or to a negative number. To set the units for the interval, use LDAP Connection Heartbeat Time Unit.

`ssoadm` attribute: `openam-idrepo-ldapv3-heartbeat-interval`

Default: 10

LDAP Connection Heartbeat Time Unit
Time unit for the LDAP Connection Heartbeat Interval setting.

`ssoadm` attribute: `openam-idrepo-ldapv3-heartbeat-timeunit`

Default: `second`

Maximum Results Returned from Search
A cap for the number of search results to request. For example, when using the Subjects tab to view profiles, even if you set Configuration > Console > Administration > Maximum Results Returned from Search to a larger number, OpenAM does not exceed this setting. Rather than raise this number, consider narrowing your search to match fewer directory entries.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-max-result`

Default: 1000

Search Timeout
Maximum time to wait for search results in seconds. Does not apply to persistent searches.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-time-limit`

Default: 10

LDAPv3 Plugin Search Scope
LDAP searches can apply to a single entry (SCOPE_BASE), entries directly below the search DN (SCOPE_ONE), or all entries below the search DN (SEARCH_SUB).

`ssoadm` attribute: `sun-idrepo-ldapv3-config-search-scope`

Default: `SCOPE_SUB`

LDAPv3 Repository Plugin Class Name
OpenAM identity repository implementation.

`ssoadm` attribute: `sunIdRepoClass`

Default: `org.forgerock.openam.idrepo.ldap.DJLDAPv3Repo`

Attribute Name Mapping
Map of OpenAM profile attribute names to directory server attribute names.

`ssoadm` attribute: `sunIdRepoAttributeMapping`

LDAPv3 Plugin Supported Types and Operations
Map of OpenAM operations that can be performed in the specified OpenAM contexts.

`ssoadm` attribute: `sunIdRepoSupportedOperations`

Default: `filteredrole=read,create,edit,delete`, `group=read,create,edit,delete`, `realm=read,create,edit,delete,service`, `role=read,create,edit,delete`, `user=read,create,edit,delete,service`

LDAP Users Search Attribute
When searching for a user by name, match values against this attribute.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-users-search-attribute`

Default: `uid`

Do not modify the value of the search attribute in user profiles. Modifying this attribute value can result in incorrectly cached identity data. For example, if you configure the search attribute to `mail`, it could prevent users from being able to update their email addresses in their user profiles.

LDAP Users Search Filter
When searching for users, apply this LDAP search filter as well.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-users-search-filter`

Default: `(objectclass=inetorgperson)`

LDAP People Container Naming Attribute
RDN attribute of the LDAP base DN which contains user profiles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-people-container-name`

Default: `ou`

LDAP People Container Value
RDN attribute value of the LDAP base DN which contains user profiles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-people-container-value`

Default: `people`

LDAP User Object Class
User profiles have these LDAP object classes.

OpenAM handles only those attributes listed in this setting. OpenAM discards any unlisted attributes from requests and the request proceeds without the attribute.

For example, with default settings, if you request that OpenAM execute a search that asks for the `mailAlternateAddress` attribute, OpenAM does the search, but does not request `mailAlternateAddress`. In the same way, OpenAM does perform an update operation with a request to set the value of an unlisted attribute like `mailAlternateAddress`, but it drops the unlisted attribute from the update request.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-user-objectclass`

Default: `devicePrintProfilesContainer`, `forgerock-am-dashboard-service`, `inetadmin`, `inetorgperson`, `inetuser`, `iplanet-am-auth-configuration-service`, `iplanet-am-managed-person`, `iplanet-am-user-service`, `iPlanetPreferences`, `organizationalperson`, `person`, `sunAMAuthAccountLockout`, `sunFederationManagerDataStore`, `sunFMSAML2NameIdentifier`, `sunIdentityServerLibertyPPService`, `top`

LDAP User Attributes
User profiles have these LDAP attributes.

OpenAM handles only those attributes listed in this setting. OpenAM discards any unlisted attributes from requests and the request proceeds without the attribute.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-user-attributes`

Default: `sunIdentityServerPPDemographicsBirthDay`, `uid`, `sunIdentityServerPPLegalIdentityLegalName`, `manager`, `assignedDashboard`, `sunIdentityServerPPCommonNameSN`, `userPassword`, `iplanet-am-session-get-valid-sessions`, `sunIdentityServerPPEmploymentIdentityJobTitle`, `iplanet-am-user-password-reset-question-answer`, `sunIdentityServerPPLegalIdentityDOB`, `sunIdentityServerPPEmergencyContact`, `sunIdentityServerPPCommonNameCN`, `iplanet-am-user-success-url`, `iplanet-am-user-admin-start-dn`, `iplanet-am-user-federation-info`, `userCertificate`, `sunIdentityServerPPFacadeGreetSound`, `sunAMAuthInvalidAttemptsData`, `sunIdentityServerPPFacadeNamePronounced`, `distinguishedName`, `sunIdentityServerPPDemographicsTimeZone`, `sunIdentityMSISDNNumber`, `iplanet-am-session-max-caching-time`, `sn`, `iplanet-am-session-quota-limit`, `iplanet-am-session-max-session-time`, `adminRole`, `sunIdentityServerPPEmploymentIdentityAltO`, `objectClass`, `sun-fm-saml2-nameid-info`, `sunIdentityServerPPLegalIdentityMaritalStatus`, `iplanet-am-user-login-status`, `sunIdentityServerPPLegalIdentityAltIdType`, `devicePrintProfiles`, `iplanet-am-session-max-idle-time`, `sunIdentityServerPPFacadegreetmesound`, `cn`, `iplanet-am-user-password-reset-options`, `telephoneNumber`, `preferredlanguage`, `iplanet-am-user-federation-info-key`, `sunIdentityServerPPMsgContact`, `sunIdentityServerPPLegalIdentityGender`, `iplanet-am-user-alias-list`, `sunIdentityServerPPCommonNameFN`, `caCertificate`, `inetUserStatus`, `sunIdentityServerPPCommonNameMN`, `sunIdentityServerPPEncryPTKey`, `givenName`, `memberOf`, `iplanet-am-static-group-dn`, `sunIdentityServerPPLegalIdentityVATIdValue`, `preferredLocale`, `iplanet-am-session-service-status`, `sun-fm-saml2-nameid-infokey`, `sunIdentityServerPPDemographicsAge`, `sunIdentityServerDiscoEntries`, `sunIdentityServerPPLegalIdentityVATIdType`, `iplanet-am-user-auth-config`, `iplanet-am-user-failure-url`, `sunIdentityServerPPAddressCard`, `sunIdentityServerPPCommonNamePT`, `dn`, `iplanet-am-session-add-session-listener-on-all-sessions`, `mail`, `authorityRevocationList`, `iplanet-am-user-password-reset-force-reset`, `inetUserHttpURL`, `sunIdentityServerPPLegalIdentityAltIdValue`, `sunIdentityServerPPCommonNameAltCN`, `preferredtimezone`, `sunIdentityServerPPInformalName`, `sunIdentityServerPPSignKey`, `sunIdentityServerPPEmploymentIdentityOrg`, `iplanet-am-session-destroy-sessions`, `sunIdentityServerPPFacadeMugShot`, `sunIdentityServerPPFacadeWebSite`, `sunIdentityServerPPDemographicsDisplayLanguage`, `postalAddress`, `iplanet-am-auth-configuration`, `employeeNumber`, `iplanet-am-user-auth-modules`, `iplanet-am-user-account-life`, `sunIdentityServerPPDemographicsLanguage`

Create User Attribute Mapping
When creating a user profile, apply this map of OpenAM profile attribute names to directory server attribute names.

Attributes not mapped to another attribute (for example, `cn`) and attributes mapped to themselves (for example, `cn=cn`) take the value of the username unless the attribute values are provided when creating the profile. The object classes for user profile LDAP entries generally require Common Name (cn) and Surname (sn) attributes, so this prevents an LDAP constraint violation when performing the add operation.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-createuser-attr-mapping`

Default: `cn`, `sn`

Attribute Name of User Status
Attribute to check/set user status.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-isactive`

Default: `inetuserstatus`

User Status Active Value
Active users have the user status attribute set to this value.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-active`

Default: `Active`

User Status Inactive Value
Inactive users have the user status attribute set to this value.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-inactive`

Default: `Inactive`

Authentication Naming Attribute
RDN attribute for building the bind DN when given a username and password to authenticate a user against the directory server.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-auth-naming-attr`

Default: `uid`

LDAP Groups Search Attribute
When searching for a group by name, match values against this attribute.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-groups-search-attribute`

Default: `cn`

LDAP Groups Search Filter
When searching for groups, apply this LDAP search filter as well.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-groups-search-filter`

Default: `(objectclass=groupOfUniqueNames)`

LDAP Groups Container Naming Attribute
RDN attribute of the LDAP base DN which contains group profiles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-group-container-name`

Default: `ou`

LDAP Groups Container Value
RDN attribute value of the LDAP base DN which contains group profiles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-group-container-value`

Default: `groups`

LDAP Groups Object Class
Group profiles have these LDAP object classes.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-group-objectclass`

Default: `groupofuniquenames`, `iplanet-am-managed-group`, `iplanet-am-managed-static-group`, `groupofurls`, `top`

LDAP Groups Attributes
Group profiles have these LDAP attributes.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-group-attributes`

Default: `cn`, `iplanet-am-group-subscribable`, `dn`, `objectclass`, `uniqueMember`

Attribute Name for Group Membership
LDAP attribute in the member’s LDAP entry whose values are the groups to which a member belongs.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-memberof`

Attribute Name of Unique Member
Attribute in the group’s LDAP entry whose values are the members of the group.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-uniquemember`

Default: `uniqueMember`

Attribute Name of Group Member URL
Attribute in the dynamic group’s LDAP entry whose values are LDAP URLs specifying members of the group.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-memberurl`

Default: `memberUrl`

LDAP Roles Search Attribute
When searching for a role by name, match values against this attribute.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-roles-search-attribute`

Default: `cn`

LDAP Roles Search Filter
When searching for roles, apply this LDAP search filter as well.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-roles-search-filter`

Default: `(&(objectclass=ldapsubentry)(objectclass=nsmanagedroledefinition))`

LDAP Roles Object Class
Role profiles have these LDAP object classes.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-role-objectclass`

Default: `ldapsubentry`, `nsmanagedroledefinition`, `nsroledefinition`, `nssimpleroledefinition`, `top`

LDAP Filter Roles Search Attribute
When searching for a filtered role by name, match values against this attribute.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-filterroles-search-attribute`

Default: `cn`

LDAP Filter Roles Search Filter
When searching for filtered roles, apply this LDAP search filter as well.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-filterroles-search-filter`

Default: `(&(objectclass=ldapsubentry)(objectclass=nsfilteredroledefinition))`

LDAP Filter Roles Object Class
Filtered role profiles have these LDAP object classes.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-filterrole-objectclass`

Default: `ldapsubentry`, `nscomplexroledefinition`, `nsfilteredroledefinition`, `nsroledefinition`

LDAP Filter Roles Attributes
Filtered role profiles have these LDAP attributes.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-filterrole-attributes`

Default: `nsRoleFilter`

Attribute Name for Filtered Role Membership
LDAP attribute in the member’s LDAP entry whose values are the filtered roles to which a member belongs.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-nsrole`

Default: `nsrole`

Attribute Name of Role Membership
LDAP attribute in the member’s LDAP entry whose values are the roles to which a member belongs.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-nsroledn`

Default: `nsRoleDN`

Attribute Name of Filtered Role Filter
LDAP attribute whose values are the filters for filtered roles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-nsrolefilter`

Default: `nsRoleFilter`

Persistent Search Base DN
Base DN for LDAP-persistent searches used to receive notification of changes in directory server data.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-psearchbase`

Default: `base-dn`

Persistent Search Filter
LDAP filter to apply when performing persistent searches.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-psearch-filter`

Default: `(objectclass=*)`

Persistent Search Scope
LDAP searches can apply to a single entry (SCOPE_BASE), entries directly below the search DN (SCOPE_ONE), or all entries below the search DN (SEARCH_SUB).

`ssoadm` attribute: `sun-idrepo-ldapv3-config-psearch-scope`

Default: `SCOPE_SUB`

The Delay Time Between Retries
How long to wait after receiving an error result that indicates OpenAM should try the LDAP operation again.

`ssoadm` attribute: `com.iplanet.am.ldap.connection.delay.between.retries`

Default: 1000 milliseconds

DN Cache Enabled
Whether to enable the DN cache, which is used to cache DN lookups that can happen in bursts during authentication. As the cache can become stale when a user is moved or renamed, enable DN caching when the directory service allows move/rename operations (Mod DN), and when OpenAM uses persistent searches to obtain notification of such updates.

`ssoadm` attribute: `sun-idrepo-ldapv3-dncache-enabled`

Default: true

DN Cache Size
Maximum number of DNs cached when caching is enabled.

`ssoadm` attribute: `sun-idrepo-ldapv3-dncache-size`

Default: 1500 items

### [](https://doc.openidentityplatform.org/openam/admin-guide/chap-realms#sec-data-stores-tivoli)Hints for Configuring Tivoli Directory Server Data Stores

Use these hints when configuring Tivoli Directory Server data stores. `ssoadm` service name: `sunIdentityRepositoryService`

Name
Name for the data store configuration.

Load schema when finished
Add appropriate LDAP schema to the directory server when saving the configuration. The LDAP Bind DN user must have access to perform this operation.

This attribute is not available for use with the `ssoadm` command.

Default: false

LDAP Server
`host:port` to contact the directory server, with optional `|server_ID|site_ID` for deployments with multiple servers and sites.

OpenAM uses the optional settings to determine which directory server to contact first. OpenAM tries to contact directory servers in the following priority order, with highest priority first.

1.   The first directory server in the list whose _server\_ID_ matches the current OpenAM server.

2.   The first directory server in the list whose _site\_ID_ matches the current OpenAM server.

3.   The first directory server in the remaining list.

If the directory server is not available, OpenAM proceeds to the next directory server in the list.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-ldap-server`

Default: `host:port` of the initial directory server configured for this OpenAM server

LDAP Bind DN
Bind DN for connecting to the directory server. Some OpenAM capabilities require write access to directory entries.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-authid`

LDAP Bind Password
Bind password for connecting to the directory server.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-authpw`

LDAP Organization DN
The base DN under which to find user and group profiles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-organization_name`

Default: `base-dn`

LDAP SSL/TLS Enabled
Whether to use LDAPS or StartTLS to connect to the directory server. If you enable SSL or StartTLS, OpenAM must be able to trust server certificates, either because the server certificates were signed by a CA whose certificate is already included in the trust store used by the container where OpenAM runs, or because you imported the certificates into the trust store.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-connection-mode`

Possible values: `LDAP`, `LDAPS`, and `StartTLS`

LDAP Connection Pool Maximum Size
Maximum number of connections to the directory server. Make sure the directory service can cope with the maximum number of client connections across all servers.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-connection_pool_max_size`

Default: 10

LDAP Connection Heartbeat Interval
How often to send a heartbeat request to the directory server to ensure that the connection does not remain idle. Some network administrators configure firewalls and load balancers to drop connections that are idle for too long. You can turn this off by setting the value to 0 or to a negative number. To set the units for the interval, use LDAP Connection Heartbeat Time Unit.

`ssoadm` attribute: `openam-idrepo-ldapv3-heartbeat-interval`

Default: 10

LDAP Connection Heartbeat Time Unit
Time unit for the LDAP Connection Heartbeat Interval setting.

`ssoadm` attribute: `openam-idrepo-ldapv3-heartbeat-timeunit`

Default: `second`

Maximum Results Returned from Search
A cap for the number of search results to request. For example, when using the Subjects tab to view profiles, even if you set Configuration > Console > Administration > Maximum Results Returned from Search to a larger number, OpenAM does not exceed this setting. Rather than raise this number, consider narrowing your search to match fewer directory entries.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-max-result`

Default: 1000

Search Timeout
Maximum time to wait for search results in seconds. Does not apply to persistent searches.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-time-limit`

Default: 10

LDAPv3 Plugin Search Scope
LDAP searches can apply to a single entry (SCOPE_BASE), entries directly below the search DN (SCOPE_ONE), or all entries below the search DN (SEARCH_SUB).

`ssoadm` attribute: `sun-idrepo-ldapv3-config-search-scope`

Default: `SCOPE_SUB`

LDAPv3 Repository Plugin Class Name
OpenAM identity repository implementation.

`ssoadm` attribute: `sunIdRepoClass`

Default: `org.forgerock.openam.idrepo.ldap.DJLDAPv3Repo`

Attribute Name Mapping
Map of OpenAM profile attribute names to directory server attribute names.

`ssoadm` attribute: `sunIdRepoAttributeMapping`

LDAPv3 Plugin Supported Types and Operations
Map of OpenAM operations that can be performed in the specified OpenAM contexts.

`ssoadm` attribute: `sunIdRepoSupportedOperations`

Default: `group=read,create,edit,delete`, `realm=read,create,edit,delete,service`, `user=read,create,edit,delete,service`

LDAP Users Search Attribute
When searching for a user by name, match values against this attribute.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-users-search-attribute`

Default: `cn`

Do not modify the value of the search attribute in user profiles. Modifying this attribute value can result in incorrectly cached identity data. For example, if you configure the search attribute to `mail`, it could prevent users from being able to update their email addresses in their user profiles.

LDAP Users Search Filter
When searching for users, apply this LDAP search filter as well.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-users-search-filter`

Default: `(objectclass=inetorgperson)`

LDAP People Container Naming Attribute
RDN attribute of the LDAP base DN which contains user profiles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-people-container-name`

Default: `ou`

LDAP People Container Value
RDN attribute value of the LDAP base DN which contains user profiles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-people-container-value`

LDAP User Object Class
User profiles have these LDAP object classes.

OpenAM handles only those attributes listed in this setting. OpenAM discards any unlisted attributes from requests and the request proceeds without the attribute.

For example, with default settings if you request that OpenAM execute a search that asks for the `mailAlternateAddress` attribute, OpenAM does the search, but does not request `mailAlternateAddress`. In the same way, OpenAM does perform an update operation with a request to set the value of an unlisted attribute like `mailAlternateAddress`, but it drops the unlisted attribute from the update request.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-user-objectclass`

Default: `devicePrintProfilesContainer`, `forgerock-am-dashboard-service`, `inetorgperson`, `inetuser`, `iplanet-am-auth-configuration-service`, `iplanet-am-managed-person`, `iplanet-am-user-service`, `iPlanetPreferences`, `organizationalperson`, `person`, `sunAMAuthAccountLockout`, `sunFederationManagerDataStore`, `sunFMSAML2NameIdentifier`, `sunIdentityServerLibertyPPService`, `top`

LDAP User Attributes
User profiles have these LDAP attributes.

OpenAM handles only those attributes listed in this setting. OpenAM discards any unlisted attributes from requests and the request proceeds without the attribute.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-user-attributes`

Default: `adminRole`, `assignedDashboard`, `authorityRevocationList`, `caCertificate`, `cn`, `devicePrintProfiles`, `distinguishedName`, `dn`, `employeeNumber`, `givenName`, `inetUserHttpURL`, `inetUserStatus`, `iplanet-am-auth-configuration`, `iplanet-am-session-add-session-listener-on-all-sessions`, `iplanet-am-session-destroy-sessions`, `iplanet-am-session-get-valid-sessions`, `iplanet-am-session-max-caching-time`, `iplanet-am-session-max-idle-time`, `iplanet-am-session-max-session-time`, `iplanet-am-session-quota-limit`, `iplanet-am-session-service-status`, `iplanet-am-user-account-life`, `iplanet-am-user-admin-start-dn`, `iplanet-am-user-alias-list`, `iplanet-am-user-auth-config`, `iplanet-am-user-auth-modules`, `iplanet-am-user-failure-url`, `iplanet-am-user-federation-info-key`, `iplanet-am-user-federation-info`, `iplanet-am-user-login-status`, `iplanet-am-user-password-reset-force-reset`, `iplanet-am-user-password-reset-options`, `iplanet-am-user-password-reset-question-answer`, `iplanet-am-user-success-url`, `mail`, `manager`, `memberOf`, `objectClass`, `postalAddress`, `preferredlanguage`, `preferredLocale`, `preferredtimezone`, `sn`, `sun-fm-saml2-nameid-info`, `sun-fm-saml2-nameid-infokey`, `sunAMAuthInvalidAttemptsData`, `sunIdentityMSISDNNumber`, `sunIdentityServerDiscoEntries`, `sunIdentityServerPPAddressCard`, `sunIdentityServerPPCommonNameAltCN`, `sunIdentityServerPPCommonNameCN`, `sunIdentityServerPPCommonNameFN`, `sunIdentityServerPPCommonNameMN`, `sunIdentityServerPPCommonNamePT`, `sunIdentityServerPPCommonNameSN`, `sunIdentityServerPPDemographicsAge`, `sunIdentityServerPPDemographicsBirthDay`, `sunIdentityServerPPDemographicsDisplayLanguage`, `sunIdentityServerPPDemographicsLanguage`, `sunIdentityServerPPDemographicsTimeZone`, `sunIdentityServerPPEmergencyContact`, `sunIdentityServerPPEmploymentIdentityAltO`, `sunIdentityServerPPEmploymentIdentityJobTitle`, `sunIdentityServerPPEmploymentIdentityOrg`, `sunIdentityServerPPEncryPTKey`, `sunIdentityServerPPFacadegreetmesound`, `sunIdentityServerPPFacadeGreetSound`, `sunIdentityServerPPFacadeMugShot`, `sunIdentityServerPPFacadeNamePronounced`, `sunIdentityServerPPFacadeWebSite`, `sunIdentityServerPPInformalName`, `sunIdentityServerPPLegalIdentityAltIdType`, `sunIdentityServerPPLegalIdentityAltIdValue`, `sunIdentityServerPPLegalIdentityDOB`, `sunIdentityServerPPLegalIdentityGender`, `sunIdentityServerPPLegalIdentityLegalName`, `sunIdentityServerPPLegalIdentityMaritalStatus`, `sunIdentityServerPPLegalIdentityVATIdType`, `sunIdentityServerPPLegalIdentityVATIdValue`, `sunIdentityServerPPMsgContact`, `sunIdentityServerPPSignKey`, `telephoneNumber`, `uid`, `userCertificate`, `userPassword`

Create User Attribute Mapping
When creating a user profile, apply this map of OpenAM profile attribute names to directory server attribute names.

Attributes not mapped to another attribute (for example, `cn`) and attributes mapped to themselves (for example, `cn=cn`) take the value of the username unless the attribute values are provided when creating the profile. The object classes for user profile LDAP entries generally require Common Name (cn) and Surname (sn) attributes, so this prevents an LDAP constraint violation when performing the add operation.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-createuser-attr-mapping`

Default: `cn`, `sn`

Attribute Name of User Status
Attribute to check/set user status.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-isactive`

Default: `inetuserstatus`

User Status Active Value
Active users have the user status attribute set to this value.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-active`

Default: `Active`

User Status Inactive Value
Inactive users have the user status attribute set to this value.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-inactive`

Default: `Inactive`

Authentication Naming Attribute
RDN attribute for building the bind DN when given a username and password to authenticate a user against the directory server.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-auth-naming-attr`

Default: `cn`

LDAP Groups Search Attribute
When searching for a group by name, match values against this attribute.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-groups-search-attribute`

Default: `cn`

LDAP Groups Search Filter
When searching for groups, apply this LDAP search filter as well.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-groups-search-filter`

Default: `(objectclass=groupOfNames)`

LDAP Groups Container Naming Attribute
RDN attribute of the LDAP base DN which contains group profiles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-group-container-name`

Default: `ou`

LDAP Groups Container Value
RDN attribute value of the LDAP base DN which contains group profiles.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-group-container-value`

LDAP Groups Object Class
Group profiles have these LDAP object classes.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-group-objectclass`

Default: `groupofnames`, `top`

LDAP Groups Attributes
Group profiles have these LDAP attributes.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-group-attributes`

Default: `cn`, `description`, `dn`, `member`, `objectclass`, `ou`

Attribute Name for Group Membership
LDAP attribute in the member’s LDAP entry whose values are the groups to which a member belongs.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-memberof`

Attribute Name of Unique Member
Attribute in the group’s LDAP entry whose values are the members of the group.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-uniquemember`

Default: `member`

Default Group Member’s User DN
DN of member added to all newly created groups.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-dftgroupmember`

Persistent Search Base DN
Base DN for LDAP-persistent searches used to receive notification of changes in directory server data.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-psearchbase`

Default: `base-dn`

Persistent Search Filter
LDAP filter to apply when performing persistent searches.

`ssoadm` attribute: `sun-idrepo-ldapv3-config-psearch-filter`

Default: `(objectclass=*)`

Persistent Search Scope
LDAP searches can apply to a single entry (SCOPE_BASE), entries directly below the search DN (SCOPE_ONE), or all entries below the search DN (SEARCH_SUB).

`ssoadm` attribute: `sun-idrepo-ldapv3-config-psearch-scope`

Default: `SCOPE_SUB`

The Delay Time Between Retries
How long to wait after receiving an error result that indicates OpenAM should try the LDAP operation again.

`ssoadm` attribute: `com.iplanet.am.ldap.connection.delay.between.retries`

Default: 1000 milliseconds

DN Cache Enabled
Whether to enable the DN cache, which is used to cache DN lookups that can happen in bursts during authentication. As the cache can become stale when a user is moved or renamed, enable DN caching when the directory service allows move/rename operations (Mod DN), and when OpenAM uses persistent searches to obtain notification of such updates.

`ssoadm` attribute: `sun-idrepo-ldapv3-dncache-enabled`

Default: true

DN Cache Size
Maximum number of DNs cached when caching is enabled.

`ssoadm` attribute: `sun-idrepo-ldapv3-dncache-size`

Default: 1500 items

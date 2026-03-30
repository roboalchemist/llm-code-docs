# Source: https://symfony.com/doc/8.0/security/ldap.html

Title: Authenticating against an LDAP server (Symfony Docs)

URL Source: https://symfony.com/doc/8.0/security/ldap.html

Markdown Content:
[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/security/ldap.rst)

Symfony provides different means to work with an LDAP server.

The Security component offers:

* The `ldap`[user provider](https://symfony.com/doc/current/security/user_providers.html), using the [LdapUserProvider](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Ldap/Security/LdapUserProvider.php "Symfony\Component\Ldap\Security\LdapUserProvider") class. Like all other user providers, it can be used with any authentication provider.
* The `form_login_ldap` authentication provider, for authenticating against an LDAP server using a login form. Like all other authentication providers, it can be used with any user provider.
* The `http_basic_ldap` authentication provider, for authenticating against an LDAP server using HTTP Basic. Like all other authentication providers, it can be used with any user provider.

This means that the following scenarios will work:

* Checking a user's password and fetching user information against an LDAP server. This can be done using both the LDAP user provider and either the LDAP form login or LDAP HTTP Basic authentication providers.
* Checking a user's password against an LDAP server while fetching user information from another source (like your main database for example).
* Loading user information from an LDAP server, while using another authentication strategy (token-based pre-authentication, for example).

[Installation](https://symfony.com/doc/8.0/security/ldap.html#installation "Permalink to this headline")
--------------------------------------------------------------------------------------------------------

In applications using [Symfony Flex](https://symfony.com/doc/current/setup.html#symfony-flex), run this command to install the Ldap component before using it:

[Configuring the LDAP client](https://symfony.com/doc/8.0/security/ldap.html#configuring-the-ldap-client "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------

All mechanisms actually need an LDAP client previously configured. The providers are configured to use a default service named `ldap`, but you can override this setting in the security component's configuration.

An LDAP client can be configured using the built-in [LDAP PHP extension](https://www.php.net/manual/en/intro.ldap.php) with the following service definition:

[Fetching Users Using the LDAP User Provider](https://symfony.com/doc/8.0/security/ldap.html#fetching-users-using-the-ldap-user-provider "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you want to fetch user information from an LDAP server, you may want to use the `ldap` user provider.

Danger

The Security component escapes provided input data when the LDAP user provider is used. However, the LDAP component itself does not provide any escaping yet. Thus, it's your responsibility to prevent LDAP injection attacks when using the component directly.

Warning

The user configured above in the user provider is only used to retrieve data. It's a static user defined by its username and password (for improved security, define the password as an environment variable).

If your LDAP server allows retrieval of information anonymously, you can set the `search_dn` and `search_password` options to `null`.

The `ldap` user provider supports many different configuration options:

### [service](https://symfony.com/doc/8.0/security/ldap.html#service "Permalink to this headline")

**type**: `string`**default**: `ldap`

This is the name of your configured LDAP client. You can freely choose the name, but it must be unique in your application and it cannot start with a number or contain white spaces.

### [base_dn](https://symfony.com/doc/8.0/security/ldap.html#base-dn "Permalink to this headline")

**type**: `string`**default**: `null`

This is the base DN for the directory

### [search_dn](https://symfony.com/doc/8.0/security/ldap.html#search-dn "Permalink to this headline")

**type**: `string`**default**: `null`

This is your read-only user's DN, which will be used to authenticate against the LDAP server to fetch the user's information.

### [search_password](https://symfony.com/doc/8.0/security/ldap.html#search-password "Permalink to this headline")

**type**: `string`**default**: `null`

This is your read-only user's password, which will be used to authenticate against the LDAP server to fetch the user's information.

### [default_roles](https://symfony.com/doc/8.0/security/ldap.html#default-roles "Permalink to this headline")

**type**: `array`**default**: `[]`

This is the default role you wish to give to a user fetched from the LDAP server. If you do not configure this key, your users won't have any roles, and will not be considered as authenticated fully.

### [role_fetcher](https://symfony.com/doc/8.0/security/ldap.html#role-fetcher "Permalink to this headline")

**Type**: `string`**Default**: `null`

When your LDAP service provides user roles, this option allows you to define the service that retrieves these roles. The role fetcher service must implement the `Symfony\Component\Ldap\Security\RoleFetcherInterface`. When this option is set, the `default_roles` option is ignored.

Symfony provides `Symfony\Component\Ldap\Security\MemberOfRoles`, a concrete implementation of the interface that fetches roles from the `ismemberof` attribute.

### [uid_key](https://symfony.com/doc/8.0/security/ldap.html#uid-key "Permalink to this headline")

**type**: `string`**default**: `null`

This is the entry's key to use as its UID. Depends on your LDAP server implementation. Commonly used values are:

* `sAMAccountName` (default)
* `userPrincipalName`
* `uid`

If you pass `null` as the value of this option, the default UID key is used `sAMAccountName`.

**type**: `array`**default**: `null`

Defines the custom fields to pull from the LDAP server. If any field does not exist, an `\InvalidArgumentException` will be thrown.

### [filter](https://symfony.com/doc/8.0/security/ldap.html#filter "Permalink to this headline")

**type**: `string`**default**: `null`

This key lets you configure which LDAP query will be used. The `{uid_key}` string will be replaced by the value of the `uid_key` configuration value (by default, `sAMAccountName`), and the `{user_identifier}` string will be replaced by the user identified you are trying to load.

For example, with a `uid_key` of `uid`, and if you are trying to load the user `fabpot`, the final string will be: `(uid=fabpot)`.

If you pass `null` as the value of this option, the default filter is used `({uid_key}={user_identifier})`.

To prevent [LDAP injection](http://projects.webappsec.org/w/page/13246947/LDAP%20Injection), the username will be escaped.

The syntax for the `filter` key is defined by [RFC4515](https://datatracker.ietf.org/doc/rfc4515/).

[Authenticating against an LDAP server](https://symfony.com/doc/8.0/security/ldap.html#authenticating-against-an-ldap-server-1 "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------------------

Authenticating against an LDAP server can be done using either the form login or the HTTP Basic authentication providers.

They are configured exactly as their non-LDAP counterparts, with the addition of two configuration keys and one optional key:

### [service](https://symfony.com/doc/8.0/security/ldap.html#service-1 "Permalink to this headline")

**type**: `string`**default**: `ldap`

This is the name of your configured LDAP client. You can freely choose the name, but it must be unique in your application and it cannot start with a number or contain white spaces.

### [dn_string](https://symfony.com/doc/8.0/security/ldap.html#dn-string "Permalink to this headline")

**type**: `string`**default**: `{user_identifier}`

This key defines the form of the string used to compose the DN of the user, from the username. The `{user_identifier}` string is replaced by the actual username of the person trying to authenticate.

For example, if your users have DN strings in the form `uid=einstein,dc=example,dc=com`, then the `dn_string` will be `uid={user_identifier},dc=example,dc=com`.

### [query_string](https://symfony.com/doc/8.0/security/ldap.html#query-string "Permalink to this headline")

**type**: `string`**default**: `null`

This (optional) key makes the user provider search for a user and then use the found DN for the bind process. This is useful when using multiple LDAP user providers with different `base_dn`. The value of this option must be a valid search string (e.g. `uid="{user_identifier}"`). The placeholder value will be replaced by the actual user identifier.

When this option is used, `query_string` will search in the DN specified by `dn_string` and the DN resulted of the `query_string` will be used to authenticate the user with their password. Following the previous example, if your users have the following two DN: `dc=companyA,dc=example,dc=com` and `dc=companyB,dc=example,dc=com`, then `dn_string` should be `dc=example,dc=com`.

Note that usernames must be unique across both DN, as the authentication provider won't be able to select the correct user for the bind process if more than one is found.

Examples are provided below, for both `form_login_ldap` and `http_basic_ldap`.

This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.

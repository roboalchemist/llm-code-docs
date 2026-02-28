# Harbor docs | Harbor Configuration

**Source:** https://goharbor.io/docs/2.14.0/install-config/configure-system-settings-cli/

Harbor Configuration

[Harbor version 2.14.0](/docs/2.14.0)

[Harbor Installation and Configuration](/docs/2.14.0/install-config/)

* [Test Harbor with the Demo Server](/docs/2.14.0/install-config/demo-server/)
* [Harbor Compatibility List](/docs/2.14.0/install-config/harbor-compatibility-list/)
* [Harbor Installation Prerequisites](/docs/2.14.0/install-config/installation-prereqs/)
* [Download the Harbor Installer](/docs/2.14.0/install-config/download-installer/)
* [Configure HTTPS Access to Harbor](/docs/2.14.0/install-config/configure-https/)
* [Configure Internal TLS communication between Harbor Component](/docs/2.14.0/install-config/configure-internal-tls/)
* [Configure the Harbor YML File](/docs/2.14.0/install-config/configure-yml-file/)
* [Run the Installer Script](/docs/2.14.0/install-config/run-installer-script/)
* [Deploying Harbor with High Availability via Helm](/docs/2.14.0/install-config/harbor-ha-helm/)
* [Troubleshooting Harbor Installation](/docs/2.14.0/install-config/troubleshoot-installation/)
* [Reconfigure Harbor and Manage the Harbor Lifecycle](/docs/2.14.0/install-config/reconfigure-manage-lifecycle/)
* [Customize the Harbor Token Service](/docs/2.14.0/install-config/customize-token-service/)
* [Harbor Configuration](/docs/2.14.0/install-config/configure-system-settings-cli/)

[Harbor Administration](/docs/2.14.0/administration/)

[Working with Projects](/docs/2.14.0/working-with-projects/)

[Building, Customizing, and Contributing to Harbor](/docs/2.14.0/build-customize-contribute/)

Some Harbor configuration is configured separately from the
[Configure the Harbor YML File](/docs/2.14.0/install-config/configure-yml-file/) section. You can change the configuration in the Harbor interface, through HTTP requests, or using an environment variable. This page describes the available configuration items, and how to use the commandline or environment variable to update the configuration.

## Example Configuration Commands for the Commandline

**Get the current configuration:**

```
curl -u "<username>:<password>" -H "Content-Type: application/json" -ki <Harbor Server URL>/api/v2.0/configurations
```

**Update the current configuration:**

```
curl -X PUT -u "<username>:<password>" -H "Content-Type: application/json" -ki <Harbor Server URL>/api/v2.0/configurations -d'{"<item_name>":"<item_value>"}'
```

**Update Harbor to use LDAP authentication:**

Command

```
curl -X PUT -u "<username>:<password>" -H "Content-Type: application/json" -ki https://harbor.sample.domain/api/v2.0/configurations -d'{"auth_mode":"ldap_auth"}'
```

Output

```
HTTP/1.1 200 OK
Server: nginx
Date: Wed, 08 May 2019 08:22:02 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 0
Connection: keep-alive
Set-Cookie: sid=a5803a1265e2b095cf65ce1d8bbd79b1; Path=/; HttpOnly
```

**Restrict project creation to Harbor administrators:**

Command

```
curl -X PUT -u "<username>:<password>" -H "Content-Type: application/json" -ki https://harbor.sample.domain/api/v2.0/configurations -d'{"project_creation_restriction":"adminonly"}'
```

Output

```
HTTP/1.1 200 OK
Server: nginx
Date: Wed, 08 May 2019 08:24:32 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 0
Connection: keep-alive
Set-Cookie: sid=b7925eaf7af53bdefb13bdcae201a14a; Path=/; HttpOnly
```

**Update the token expiration time:**

Command

```
curl -X PUT -u "<username>:<password>" -H "Content-Type: application/json" -ki https://harbor.sample.domain/api/v2.0/configurations -d'{"token_expiration":"300"}'
```

Output

```
HTTP/1.1 200 OK
Server: nginx
Date: Wed, 08 May 2019 08:23:38 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 0
Connection: keep-alive
Set-Cookie: sid=cc1bc93ffa2675253fc62b4bf3d9de0e; Path=/; HttpOnly
```

## Set Configuration Items Using An Environment Variable

Introduced in 2.3.0 is the ability to use an environment variable, `CONFIG_OVERWRITE_JSON`, in the core container to set the configuration. Once the `CONFIG_OVERWRITE_JSON` variable is set, you can only update or remove the configuration by updating the `CONFIG_OVERWRITE_JSON` and restarting the container. You will not be able to update the configuration in the Harbor interface or in the commandline.

**Example CONFIG\_OVERWRITE\_JSON configuration:**

```
CONFIG_OVERWRITE_JSON={"ldap_verify_cert":"false", "auth_mode":"ldap_auth","ldap_base_dn":"dc=example,dc=com", "ldap_search_dn":"cn=admin,dc=example,dc=com","ldap_search_password":"admin","ldap_url":"myldap.example.com", "ldap_scope":2}
```

See the
[Harbor Configuration Items](#harbor-configuration-items) table below for more information about available inputs for `CONFIG_OVERWRITE_JSON`.

If there is a legacy user in your instance of Harbor, the authentication mode can’t be changed by the environment variable `CONFIG_OVERWRITE_JSON`.

## Harbor Configuration Items

| Configure item name | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| auth\_mode | Authentication mode, it can be db\_auth, ldap\_auth, uaa\_auth or oidc\_auth | string |  |  |
| primary\_auth\_mode | Set Identity Provider to be the primary auth method | boolean | optional | false |
| ldap\_url | LDAP URL | string | required |  |
| ldap\_base\_dn | LDAP base DN | string | required(ldap\_auth) |  |
| ldap\_filter | LDAP filter | string | optional |  |
| ldap\_scope | LDAP search scope, 0-Base Level, 1- One Level, 2-Sub Tree | number | optional | 2-Sub Tree |
| ldap\_search\_dn | LDAP DN to search LDAP users | string | required(ldap\_auth) |  |
| ldap\_search\_password | LDAP DN’s password | string | required(ldap\_auth) |  |
| ldap\_timeout | LDAP connection timeout | number | optional | 5 |
| ldap\_uid | LDAP attribute to indicate the username in Harbor | string | optional | cn |
| ldap\_verify\_cert | Verify cert when create SSL connection with LDAP server, true or false | boolean | optional | true |
| ldap\_group\_admin\_dn | LDAP Group Admin DN | string | optional |  |
| ldap\_group\_attribute\_name | LDAP Group Attribute, the LDAP attribute indicate the groupname in Harbor, it can be gid or cn | string | optional | cn |
| ldap\_group\_base\_dn | The Base DN which to search the LDAP groups | string | required(ldap\_auth and LDAP group) |  |
| ldap\_group\_search\_filter | The filter to search LDAP groups | string | optional |  |
| ldap\_group\_search\_scope | LDAP group search scope, 0-Base Level, 1- One Level, 2-Sub Tree | number | optional | 2-Sub Tree |
| ldap\_group\_membership\_attribute | LDAP group membership attribute, to indicate the group membership, it can be memberof, or ismemberof | string | optional | memberof |
| project\_creation\_restriction | The option to indicate user can be create object, it can be everyone, adminonly | string | optional | everyone |
| read\_only | The option to set repository read only, it can be true or false | boolean | optional | false |
| self\_registration | User can register account in Harbor, it can be true or false | boolean | optional | true |
| token\_expiration | Security token expirtation time in minutes | number | optional | 30 |
| uaa\_client\_id | UAA client ID | string | required(uaa\_auth) |  |
| uaa\_client\_secret | UAA certificate | string | required(uaa\_auth) |  |
| uaa\_endpoint | UAA endpoint | string | required(uaa\_auth) |  |
| uaa\_verify\_cert | UAA verify cert, true or false | boolean | optional | true |
| oidc\_name | Name for OIDC authentication | string | required(oidc\_auth) |  |
| oidc\_endpoint | Endpoint for OIDC auth | string | required(oidc\_auth) |  |
| oidc\_extra\_redirect\_parms | Extra parameters to add when redirect request to OIDC provider | string | optional | {} |
| oidc\_client\_id | Client id for OIDC auth | string | required(oidc\_auth) |  |
| oidc\_client\_secret | Client secret for OIDC auth | string | required(oidc\_auth) |  |
| oidc\_groups\_claim | The name of a custom group claim that you have configured in your OIDC provider, that includes the groups to add to Harbor | string | optional |  |
| oidc\_admin\_group | The name of the admin group, if the ID token of the user shows that he is a member of this group, the user will have admin privilege in Harbor. Note: You can only set one Admin Group. | string | optional |  |
| oidc\_scope | Scope for OIDC auth | string | required(oidc\_auth) |  |
| oidc\_verify\_cert | Verify certificate for OIDC auth, true or false | boolean | optional | true |
| oidc\_auto\_onboard | Skip the onboarding screen, so user cannot change its username. Username is provided from ID Token, true or false | boolean | optional | false |
| oidc\_user\_claim | The name of the claim in the ID Token where the username is retrieved from | string | optional | name |
| robot\_token\_duration | Robot token expiration time in minutes | number | optional | 43200 (30days) |
| robot\_name\_prefix | Prefixed string for each robot account name | string | optional | robot$ |
| audit\_log\_forward\_endpoint | Forward audit logs to the syslog endpoint, for example: harbor-log:10514 | string | optional |  |
| skip\_audit\_log\_database | Skip to log audit log in the database, only available when audit log forward endpoint is configured | boolean | optional | false |
| scanner\_skip\_update\_pulltime | Vulnerability scanner(e.g. Trivy) will not update the image “last pull time” when the image is scanned | boolean | optional |  |
| banner\_message | The banner message for the UI. It is the stringified result of the banner message object | string | optional |  |

Both booleans and numbers can be enclosed with double quote in the request json, for example: `123`, `"123"`, `"true"` or `true` is OK.

On this page

  
  

Contributing

[Page source](https://github.com/goharbor/website/blob/release-2.14.0/docs/install-config/configure-system-settings-cli.md)
[Create issue](https://github.com/goharbor/harbor/issues)
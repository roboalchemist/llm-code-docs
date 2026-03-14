# Source: https://virustotal.readme.io/docs/admins-guide.md

# Walkthrough guide for VirusTotal group administrators

VirusTotal’s premium users are categorized into two primary **group** roles: **Users** (standard users) and **Admins** (group administrators). Additionally, role-based access controls are applied to users for certain features and tools available across the platform.

This document outlines the enhanced privileges of group administrators, detailing the management actions available to them at both the organizational group and individual user levels.

# General notions

All management actions restricted to administrators are accessible from the **web interface** under the **My Group** menu option, on the top right corner.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a72b086f61044810bcebbf3589f1dc22202415c112a7cd6b3bc2483680421ed0-enterprise-group-access-20251218.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

## Group information

Here you can find the group’s preferences including two of the most important group level parameters, the **group’s ID** and the **group's Token**, which are required in multiple automation and object-sharing tasks.\
Additional group related information is split in several tabs which allow management of different types of features. Please note that depending on the group's configuration and acquired services, the number of tabs available for each group can vary.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/cbb4cca33bc115dd3301a205e93ca9204f9ab09bb3875deb3513461cb42e28f4-group_tabs_20260210.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

## User information

Going down to the user level, they are listed in the **USERS** tab, where group administrators can easily filter shown group members by security settings and group role and also by typing the name or email address of the user of interest.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ceda65f2d7bd68b0634aa117013a7618d1db3a75422cbefb9e69c0119e14da6a-user_filter_20260210.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

Additionally, by clicking on a user name, you automatically pivot to the user’s profile where **user ID** is shown next to the user's avatar. This ID is required in multiple automation tasks that are shown in next sections.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/9a81cc481c66fc0c5221987410c85d0da21694c1b10b389d6442a29c9ea30acd-user-profile-20251218.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "600px"
    }
  ]
}
[/block]

## Service account information

Apart from users, a **group** could also have **service accounts** which are very useful for tasks automation since they are unaffected by people changes, as they are not tied to any specific individual and they don’t require an email address to be created. This makes them a more reliable and consistent way to grant access to automation resources than user accounts.\
Service accounts are listed on the **Service accounts** section available on the **USERS** tab where you can check their **IDs**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ed38227b42ad07369401d46faf2cb51b71d9dbf7e24f72003df75eb97e4cf002-service_account_id_20260210.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

## API notions

In addition to the web interface there is a set of **API** endpoints designed to automate most administrative tasks (more on this later). These endpoints are shown on the **VT ENTERPRISE ADMINISTRATION** section of the [API v3 documentation](https://virustotal.readme.io/reference/overview) - please note that NOT all of them require administrator privileges.\
Their usage requires authentication/authorization through the admin's API key that can be found [here](https://www.virustotal.com/gui/my-apikey) (or on the top right corner of the web interface -> API key menu option).

# Everything a VT Admin can do

As we discussed, almost every action in VT can be performed in 2 ways: via web interface and via API v3 requests. We grouped all actions reserved for administrator users in the following categories.

* [1. Group members management](#1-group-members-management)
  * [1.1. Getting group members](#11-getting-group-members)
    * [1.1.1. Getting the list of users and service accounts](#111-getting-the-list-of-users-and-service-accounts)
  * [1.2. Users management](#12-users-management)
    * [1.2.1. Adding new user to the VT group](#121-adding-new-user-to-the-vt-group)
    * [1.2.2. Removing user from the VT group](#123-removing-user-from-the-vt-group)
    * [1.2.3. Managing user privileges](#124-managing-user-privileges)
    * [1.2.4. Managing user API allowance](#125-managing-user-api-allowance)
  * [1.3. Service accounts management](#13-service-accounts-management)
    * [1.3.1. Adding a new service account to the VT group](#131-adding-a-new-service-account-to-the-vt-group)
    * [1.3.2. Removing a service account from the VT group](#132-removing-a-service-account-from-the-vt-group)
    * [1.3.3. Getting a service accounts API key](#133-getting-a-service-accounts-api-key)
* [2. Group management](#2-group-management)
  * [2.1. General settings](#21-general-settings)
    * [2.1.1. Editing organization name, domain name and avatar](#211-editing-organization-name-domain-name-and-avatar)
  * [2.2. Security features](#22-security-features)
    * [2.2.1. Editing all group members session timings](#221-editing-all-group-members-session-timings)
    * [2.2.2. Single Sign On - SSO](#222-single-sign-on---sso)
  * [2.3. Private Scanning settings](#23-private-scanning-settings)
    * [2.3.1. Editing PS retention period and storage region](#231-editing-ps-retention-period-and-storage-region)
  * [2.4. Invoice settings](#24-invoice-settings)
    * [2.4.1. Getting invoice notifications](#241-getting-invoice-notifications)
* [3. Consumption](#3-consumption)
  * [3.1. VirusTotal enterprise features consumption](#31-virustotal-enterprise-features-consumption)
    * [3.1.1. Getting current month group overall enterprise consumption](#311-getting-current-month-group-overall-enterprise-consumption)
    * [3.1.2. Getting users individual enterprise consumption](#312-getting-users-individual-enterprise-consumption)
  * [3.2. VirusTotal API consumption](#32-virustotal-api-consumption)
    * [3.2.1. Getting group overall API consumption](#321-getting-group-overall-api-consumption)
    * [3.2.2. Getting users individual API consumption](#322-getting-users-individual-api-consumption)
* [4. Audit Log](#4-audit-log)
  * [4.1. Filtering logs](#41-filtering-logs)
  * [4.2. Exporting logs](#42-exporting-logs)
  * [4.3. Seeing details](#43-seeing-details)

## 1. Group members management

### 1.1. Getting group members

#### 1.1.1. Getting the list of users and service accounts

**Web interface =>** On the **My Group** menu option -> **USERS** tab, the list of users is shown under the **Group Members** section, and the list of service accounts under the **Service accounts** section. All of them can be exported by administrators through the **Export** button in several file formats, as shown in the following image.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/aef387bd8c022885643f28c009cec2b9d4f6f372c4a351f50f94d4690a956bd5-users_service_accounts_list_20260210.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

The result file will include the following information: username, first name, last name, email and type to identify whether it is a user account or a service account.

**VirusTotal API =>** The endpoint [/v3/groups/{id}/{relationship}](https://virustotal.readme.io/reference/groups-relationships) returns the objects related to the group based on group’s ID [(check group ID)](#group-information) and relationship which identifies the type of objects to request and whose values in this case are  “users” and “service\_accounts”.\
Other endpoints provide the list of users and service accounts, but they don’t provide the same information as the already mentioned one: [/v3/groups/{id}/relationships/users](https://virustotal.readme.io/reference/get-group-users) and [/v3/groups/{id}/relationships/service\_accounts](https://virustotal.readme.io/reference/get-service-accounts-of-a-group).

[Back to top](#:~:text=VirusTotal’s-premium-users)

### 1.2. Users management

#### 1.2.1. Adding new user to the VT group

**Web interface =>** From the **My Group** menu option -> **USERS** tab -> **Add** dropdown button -> **User** option, a group administrator is able to create or add new members to their group by entering a comma-separated list of email addresses and assigning them either **Admin** or **User** (standard access) roles via the corresponding checkboxes.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/63e1ae6b6c421745c121397ef61f3858580a7ac945295d5c24a3057fe9052d90-add_user_20260210.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

If a user is added to a group but doesn't yet have an account, they will be sent an email invitation to create one. Upon account creation, the user will be automatically added to the group. On the contrary, if the user already has an existing account, they will be automatically added to the group and receive a welcome email.

Please note that users can only belong to one group at a time. If a user is already a member of another group, they must be removed from it before they can be added to yours.

**VirusTotal API =>** The [/v3/groups/{id}/relationships/users](https://virustotal.readme.io/reference/update-group-users) endpoint allows administrators to add users to the group as common members. This endpoint requires the group ID ([check group ID](#group-information)) as a parameter, and a list of user objects identified by their email addresses to convert in new group members as in the following example:

```json
payload = {
  "data": [
    {"type":"user","id":"user_1_email_address"},
    {"type":"user","id":"user_2_email_address"}
  ]
}
```

There’s no specific endpoint for creating administrator members as in the web interface, although there’s a way of granting admin privileges to common users when needed. Check out the ‘[Managing users privileges](#123-managing-user-privileges)’ section.

[Back to top](#:~:text=VirusTotal’s-premium-users)

#### 1.2.2. Removing user from the VT group

**Web interface =>** The list of users is given on the **My Group** menu option -> **USERS** tab -> **Group Members** section. Each user has a bin icon at the right, that allows administrators to remove it from the VT group, so that it is no longer a group member. Instead, it becomes a free user with limited access to VirusTotal’s products.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e3b296d9ae360bf490271cc7f76e83f1e6ef1fee305639101f2ea05548dc3c7f-remove_user_20260210.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

**VirusTotal API** => The [/v3/groups/{id}/relationships/users/{user_id}](https://virustotal.readme.io/reference/delete-user-from-group) endpoint removes a given user from a given group, based on their identifiers. ([Check group ID](#group-information)) ([Check user ID](#user-information)) When removing a user from the group, it becomes a free user with limited access to VirusTotal’s products.

[Back to top](#:~:text=VirusTotal’s-premium-users)

#### 1.2.3. Managing user privileges

**Web interface =>** The list of users is given on the **My Group** menu option -> **USERS** tab -> **Group Members** section. Users' group role and features access privileges are displayed in the **Roles** column. Access levels for specific features and the group role are represented by color-coded symbols in light mode:

* Blue: administrative access
* Black: standard access
* Gray: no access

While in dark mode the color-coded symbols are as follows:

* Blue: administrative access
* White: standard access
* Gray: no access

Administrators can manage these settings **individually** via the **pen** (edit) button in the **Roles** column, or in **bulk** by selecting multiple users and clicking the **Manage Roles** button at the top of the **Group Members** section, as shown in the image below.

* **Individual Management**: the edit form displays the user's current configuration, allowing for precise adjustments.
* **Bulk Management**: no current settings are displayed. Any roles selected in the form will be applied to all highlighted users, and any roles left unselected will remain unchanged from their original state.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d547121ccd99e04bb6d605ff19346515e6abc42cbb2943f70fbf123d8c1bf402-change_user_privileges_20260210.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

**VirusTotal API =>** The [/v3/groups/\{id}/relationships/users](https://virustotal.readme.io/reference/patch-group-users-roles) endpoint allows to manage users roles and privileges based on their user IDs and the group ID parameter. ([Check group ID](#group-information))\
On the other hand, the [/v3/groups/{id}/relationships/administrators/{user_id}](https://virustotal.readme.io/reference/delete-user-group-administrator) endpoint revokes admin privileges of a given user based on its ID and the group ID. ([Check user ID](#user-information)) ([Check group ID](#group-information))

[Back to top](#:~:text=VirusTotal’s-premium-users)

#### 1.2.4. Managing user API allowance

**Web interface =>** The list of users is given on the **My Group** menu option -> **USERS** tab -> **Group Members** section. Each of them has a pen icon that allows administrators to change the user’s **Daily API cap** that is shown next to the pen icon.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4cf9119baff4e861eb2d63b7dca1a2bd1344fb7070b2ff79dece74023179c5ba-change_user_api_20260210.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

**VirusTotal API =>** The [/v3/groups/\{id}/relationships/users](https://virustotal.readme.io/reference/patch-group-users-roles) endpoint can be used to PATCH relationships between user objects and a VirusTotal group based on its ID.  ([Check user ID](#user-information)) ([Check group ID](#group-information)) This endpoint also serves to change users' daily API cap as in the following example:

```json
payload = {
  "data": [
    {
      "context_attributes": {
        "quota_limits": {
          "api_requests_daily": {
            "allowed": 300
          }
        }
      },
      "type": "user",
      "user": "user_id"
    }
  ]
}
```

[Back to top](#:~:text=VirusTotal’s-premium-users)

### 1.3. Service accounts management

#### 1.3.1. Adding a new service account to the VT group

**Web interface =>** Service accounts are very useful in automating enrichment and other automation tasks, since they are not tied to any specific individual.\
From the **My Group** menu option -> **USERS** tab -> **Add** dropdown button -> **Service Account** option, administrators are able to create new service accounts.

On the opened form, administrators only have to specify the name or identifier that the new service account will receive, before saving the request.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ca41498a5531ea34fd63ca7c82292d97c35bc20f6d2506518ce30fd03baa1cf3-add_service_account_20260210.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

**VirusTotal API =>** Although creating new service accounts is a very occasional activity and you might not need to automate it because the web interface serves well for this purpose, the [/v3/groups/{id}/relationships/service\_accounts](https://virustotal.readme.io/reference/create-a-new-service-account) endpoint can be used as well. It only requires the group ID ([check group ID](#group-information)) and a new service account object with the ID that it will receive as in the following example:

```json json
payload = {
  "data": [
    {"id": "vt_enrichment", "type": "service_account"}
  ]
}
```

[Back to top](#:~:text=VirusTotal’s-premium-users)

#### 1.3.2. Removing a service account from the VT group

**Web interface =>** The list of service accounts is given on the **My Group** menu option -> **USERS** tab -> **Service accounts** section. Each of them has a bin icon at the right, that allows administrators to delete the specific service account.\
Please make sure that you are not going to interfere with any integration with VT by removing service accounts whose API key is being used internally.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e55467757dad028281f4894152ed2148245d2c9425fbc6c504b288d65326cbf4-remove_service_account_20260210.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

[Back to top](#:~:text=VirusTotal’s-premium-users)

#### 1.3.3. Getting a service accounts API key

**Web interface =>** The list of service accounts is given on the **My Group** menu option -> **USERS** tab -> **Service accounts** section. Each of them has an icon for unhiding the API key and another icon for copying it to the clipboard. Only administrators are able to get the API key of a service account to use it on automation tasks such as IoCs enrichment.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f914b69f9181385af25a412ce67c9e9aaa661d93b9ebd44170a3d41501a8a065-service_account_api_key_20260210.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

**VirusTotal API =>** Although checking service accounts API keys is a very occasional activity and you might not need to automate it because the web interface serves well to this purpose, the [/v3/service\_accounts/{id}](https://virustotal.readme.io/reference/get-a-service-account-object) endpoint can be used as well. It only requires the service account ID or name. ([Check service account ID](#service-account-information))

[Back to top](#:~:text=VirusTotal’s-premium-users)

## 2. Group management

### 2.1. General settings

#### 2.1.1. Editing organization name, domain name and avatar

**Web interface =>** On the web platform, administrators can find 2 ways of modifying organization name and domain name.

* The first one is on the **My Group** menu option -> **GROUP PREFERENCES**. By selecting the pen icon administrators are able to edit **Organization** and **Domain name** parameters.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a0b593c8e4f30b5454614741b97d9ce3ebe9caef5bee9e8982f16a4159ec1d96-org_name_domain_1_20260210.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

* The second way of editing this data is from the **My Group** menu option -> **SETTINGS** tab -> **Group info** section -> **Organization** and **Domain name** text boxes.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/95be200f9ae8d8fa8acf8ef9240f163ead344ff97f018a44462055e388d2b983-org_name_domain_2_20260210.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

As for the group avatar, on the **My Group** menu option, at the top left is a **Change avatar** button that allows not only administrators but also common users to change group's avatar.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6ef133fc80139ca10d9fdca6ee8b0c8e9fad130ecfb131e5d294a795f149f481-change_avatar_20260210.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

[Back to top](#:~:text=VirusTotal’s-premium-users)

### 2.2. Security features

#### 2.2.1. Editing all group members session timings

**Web interface =>** On the **My Group** menu option -> **SETTINGS** tab -> **Security controls** section, administrators are able to define session maximum lifetime and inactivity time. Both of them are represented in seconds although they also show some default options by clicking on the input box.\
When these times are exceeded, users are forced to re-authenticate.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/141b538845f3bad6908e790804001cd70a25a81cba9eaeb2afd2b769d2076dcd-session_timings_20260210.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

[Back to top](#:~:text=VirusTotal’s-premium-users)

#### 2.2.2. Single Sign On - SSO

**Web interface =>** On the **My Group** menu option -> **SETTINGS** tab -> **Single sign-on** section, administrators are able to configure the **Identity provider** for SSO. Through the dropdown option, administrators can enable one of the 3 SSO services already integrated or configure other preferred identity providers via Security Assertion Markup Language (**SAML**).\
Please note that this only affects the authentication on the web platform. VirusTotal API authentication is not affected.

* ***Already integrated identity provider services***

If users have accounts in any of the 3 services (Google, GitHub, Microsoft), they can use those services to authenticate on our platform. For more information, refer to this [document](https://virustotal.readme.io/docs/sso-authentication). Please note that users can always use one of these accounts without having to modify the My Group SSO configuration, but once configured, no one no longer will be able to authenticate on the platform via common credentials.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f552f6d30f4bb148dc01bd76668c7fbc6fc662ed9d92eeb001f89fed7f7bc138-SSO_integrated_providers_20260210.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

* ***SAML***

For configuring SAML administrators can check out these guide examples for [Okta](https://virustotal.readme.io/docs/saml-okta), [Ping](https://virustotal.readme.io/docs/saml-ping) or [Entra ID](https://virustotal.readme.io/docs/saml-entraid) and replicate it to the preferred identity provider. The information needed to configure it is shown when selecting the **Other (SAML)** option in the **Identity provider** dropdown element.

Please note that for forcing users to only authenticate via SAML, a checkbox is provided. If this checkbox is not selected, users can use both methods of authentication: SAML and common credentials. We recommend allowing both authentication mechanisms during SAML configuration to avoid losing access to the platform in case of any misconfiguration.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/48339cf99ab93dee2cae80687da629b23f234cfa218d0cc5f7a6e8976f40e4d5-SSO_SAML_20260210.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

Please note that you must manually update rotated certificates in the SAML settings on the platform.

* ***OIDC***

The information needed to configure it is shown when selecting the **Other (OIDC)** option in the **Identity provider** dropdown element.\
Please note that for forcing users to only authenticate via OIDC, a checkbox is provided. If this checkbox is not selected, users can use both methods of authentication: OIDC and common credentials. We recommend allowing both authentication mechanisms during OIDC configuration to avoid losing access to the platform in case of any misconfiguration.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3fe8fbdf5426172badc8021bd06ee95456dbb491e1f35032eb42e709f70b8687-SSO_OIDC_20260210.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

[Back to top](#:~:text=VirusTotal’s-premium-users)

* ***Adding new user to an existing VirusTotal group - automatically***

**Web interface =>** On **My group** menu option -> **SETTINGS** tab -> **Group info** section -> **Auto add emails** text box. Additionally, here group administrators can enable the below checkbox to be notified every time a new user is added to their group as a group member. This text box supports 2 types of inputs or conditions: complete email addresses and/or organization domain names regular expressions, with wildcards,(<_@google.com>, <_@virustotal.com>), *one entry per line*.\
When enabling this feature, new users whose email addresses meet one of the configured conditions and who are created through the group SSO sign-in link, are automatically added to the group, inheriting group's default configurations.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f8f2760d546cf2e9400355294dbf8ecff09ab5b458c2cc1d301786d6835aad51-SSO_autoadd_20260210.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

**VirusTotal API =>** The [/v3/groups/\{id}](https://virustotal.readme.io/reference/patch-group) endpoint can be used to PATCH a VirusTotal group object based on its group ID. [(Check group ID)](#group-information) The parameter associated with the automatically adding users to groups feature is *data->attributes->auto\_add\_users*. This parameter is a list of regular expressions (\*@company\_domain) and complete email addresses that are going to be checked with every new user, and those meeting any entry will be automatically added to the group as a new member. When using this endpoint, don't forget to specify the object `'type': 'group'` in the payload parameter as in the following example:

```json
payload = {
  "data": {
    "type": "group",
    "attributes": {
      "auto_add_users":["*@google.com", "*@virustotal.com", "email_addres1", "email_address2"]
    }
  }
}
```

Please note that since this parameter is rarely edited and the web interface is more than enough to cover it, we highly recommend editing this parameter manually through the web interface.

[Back to top](#:~:text=VirusTotal’s-premium-users)

### 2.3. Private Scanning settings

#### 2.3.1. Editing PS retention period and storage region

**Web interface =>** On the **My Group** menu option -> **SETTINGS** tab -> **Private scanning** section, group administrators can configure the default **Retention period days** of files submitted to Private Scanning, their **Storage region** during their lifetime in VirusTotal's database and also some analysis preferences such as **detonating the sample in dynamic analysis sandboxes** to be not just statically but also dynamically analyzed. For this, other configurations are available such as **enabling internet access** to allow external communications of the file and **intercepting HTTP/TLS communications**. Additionally, there's an option for **enabling live interactions** of analysts with the sandbox where the sample is detonated.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/bbc437cb832b079cd37e892e80d19fc6d81b113e1e89632f16d17174bbd3d7e7-private_scanning_1_20260210.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

This configuration will be used by default, although users are able to configure these parameters for each file they are submitting to Private Scanning directly from the submission form.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2ca76dee2901aa65bb98cf63edf5daefc99c3de03672d5e48b964ebc7d63298d-private_scanning_2_20260210.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "450px"
    }
  ]
}
[/block]

[Back to top](#:~:text=VirusTotal’s-premium-users)

### 2.4. Invoice settings

#### 2.4.1. Getting invoice notifications

**Web interface =>** On the **My Group** menu option -> **SETTINGS** tab -> **Group info** section -> **Send invoices to** text box, administrators can configure a list of email addresses to be notified of every new invoice.\
Please note that this is available only if the organization is paying VirusTotal Enterprise via credit card.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1a8693e7b322ec857da8662971ccd573cd8d89cb0c7147627da5771fce9a7978-invoice_1_20260210.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

Additionally, invoices can be accessed by administrators from the **My Group** menu option -> **INVOICES** tab.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/be6399f238b29fd5a1f048fbc019bd2497d0cfc2b3d324ec54688e8e9aec8912-invoice_2_20260210.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

[Back to top](#:~:text=VirusTotal’s-premium-users)

## 3. Consumption

### 3.1. VirusTotal enterprise features consumption

#### 3.1.1. Getting current month group overall enterprise consumption

**Web interface =>** On the **My Group** menu option -> **USAGE** tab -> the **Consumption current month** section displays usage per VirusTotal feature relative to your monthly allowance. If any of the features is not available Exceeded consumption will be highlighted in red.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/bc8d9ea2f71bea065920ea67dc6acdbd64f90e28412a6a75132f0e47d5c88182-group_enterprise_consumption_20260210.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

[Back to top](#:~:text=VirusTotal’s-premium-users)

#### 3.1.2. Getting users individual enterprise consumption

**Web interface =>** On the **My Group** menu option -> **USAGE** tab, there are several sections providing a breakdown of the group’s monthly consumption by feature and user, displaying only those features with active usage:

* **Search consumption by user**
* **Downloads consumption by user**
* **Livehunt rules consumption by user**
* **Retrohunt consumption by user**
* etc

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a15ac9ac5f904925d47a78e48eda9bb23d7545de9bb9a31ab61ea6e565d0eb7e-user_enterprise_consumption_20260210.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

[Back to top](#:~:text=VirusTotal’s-premium-users)

### 3.2. VirusTotal API consumption

#### 3.2.1 Getting group overall API consumption

**Web interface =>** On the **My Group** menu option -> **API** tab, there's a section showing the **Access level** and API allowance assigned to the group as the **Daily quota** and the **Request rate** per minute.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/827060f0408b7e6210221bf67580975c59de07c37e7d5e67f0aed1bc9bdda709-group_api_allowance_20260213.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

There are 2 additional sections showing the group's overall API consumption: **Consumption last 30 days** breaks down the group's last 30 days API consumption by day, and **Consumption by endpoint** shows previous day consumption by endpoint. For more granular details please use the VirusTotal APIv3.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1932b197916ee3266980436404098f7ed1eacb3ffc6cbe1007ad2c2eb7931394-group_api_1_20260210.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

**VirusTotal API =>** The [/v3/groups/{id}/api\_usage](https://virustotal.readme.io/reference/group-api-usage) endpoint shows a group’s API usage broken down by day and endpoint, pointing out the endpoints that really consume API as well as those that do not (`not_consuming_quota`). The data available includes only the last 60 natural days and the required parameter is the group ID. ([Check group ID](#group-information)) Additionally, you can specify the start day and last day parameters of the time range you want to track (yyyymmdd format).

[Back to top](#:~:text=VirusTotal’s-premium-users)

#### 3.2.2. Getting users individual API consumption

**Web interface =>** On the **My Group** menu option -> **API** tab -> **Consumption by user** section shows previous day’s consumption by user. For more granular details please use the APIv3.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ed14e1c96d93f0121dba70ffa0fc578f70b824fba1039f310eece9307a362772-group_api_2_20260210.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

**VirusTotal API =>** The [/v3/users/{id}/api\_usage](https://virustotal.readme.io/reference/user-api-usage) endpoint shows an user's API usage broken down by day and endpoint, pointing out the endpoints that really consume API as well as those that do not (`not_consuming_quota`). The data available includes only the last 60 natural days and the required parameter is the user ID. ([Check user ID](#user-information)) Additionally, you can specify the start day and last day parameters of the time range you want to track (yyyymmdd format).

[Back to top](#:~:text=VirusTotal’s-premium-users)

## 4. Audit Log

### 4.1. Filtering logs

**Web interface =>** From the **My group** menu option -> **AUDIT LOG** tab -> administrators can view the Audit Log, detailing the platform's most relevant actions. The log includes fields like **Timestamp (UTC)**, **Username**, **User Email**, **Source IP**, **Target Type**, **Target Identifier**, and the **Action** taken.

Logs can be filtered using the collapsible left-side panel, which features key attributes like **Date**, **User**, **Action** and **Target Identifier**.

The **User** filter, along with the **Username** and **User Email** fields in the log table, all refer to the user who performed the action.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/345c8ae4e9a3c95756287831321d2b4101b03410ef9297aa67b0ddbc0fcd62ca-audit_log_filters_20260210.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

**VirusTotal API =>** The [/api/v3/groups/{group}/activity\_log\_entries](https://virustotal.readme.io/reference/get-activity-log) endpoint retrieves a list of activity logs. It supports a `filter` query parameter that allows you to narrow the results using the same criteria available in the UI.

Be aware that unlike the UI (where **Username** and **User Email** are direct columns), the API requires you to access the user who performed the action through the dedicated `user` relationship. Consult the endpoint document for details.

[Back to top](#:~:text=VirusTotal’s-premium-users)

### 4.2. Exporting logs

**Web interface =>** From the **My group** menu option -> **AUDIT LOG** tab -> **Export** drop-down menu, administrators can export the Audit Log in **CSV** or **Json** format, or **Copy to clipboard** in JSON format. The current filters are applied to all exported logs.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/aa2399c3c27e148109e956c4c371638c9c74794a775e5a761335660939b4b327-audit_log_export_20260210.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

**VirusTotal API =>** Use the [/api/v3/groups/{group}/activity\_log\_entries](https://virustotal.readme.io/reference/get-activity-log) endpoint to retrieve activity logs in JSON format, applying the filters and relationships detailed in the endpoint documentation.

[Back to top](#:~:text=VirusTotal’s-premium-users)

### 4.3. Seeing details

**Web interface =>** From the **My group** menu option -> **AUDIT LOG** tab -> administrators can view the Audit Log of the platform's most relevant actions. For detailed context on an event, like which user was granted admin privileges or which user was removed from the group, admins can click the **See details** button located on the right of each log entry, which automatically displays the **Audit Log Event Details**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/eaa46516e0afc0f6841aeeb0f3cf964fd48871c05c583d78dfd491e14e1c5518-audit_log_details_20260210.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

**VirusTotal API =>** The [/api/v3/groups/{group}/activity\_log\_entries](https://virustotal.readme.io/reference/get-activity-log) endpoint retrieves activity logs allowing the application of filters and relationships as detailed in the endpoint documentation.

[Back to top](#:~:text=VirusTotal’s-premium-users)
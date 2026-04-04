# Source: https://docs.avaamo.com/user-guide/release-notes/v5.0-to-v5.8.x-releases/v5.6.x/release-notes-v5.6.0.md

# Release notes v5.6.0

The Avaamo Conversational AI Platform v5.6.0 minor release includes 3 new features and 1 enhancement distributed as follows:

* **New features**:
  * [Ability to integrate seamlessly with MS-Azure Active Directory (AD) groups](#ability-to-integrate-seamlessly-with-ms-azure-active-directory-ad-groups)
  * [Ability to manage user roles and agent permission via groups](#ability-to-manage-user-roles-and-agent-permission-via-groups)
  * [Ability to restrict login IP address at the company-level](#ability-to-restrict-login-ip-address-at-the-company-level)
* **Enhancements**: This release also includes enhancements related to masking location IP addresses in the Agent Console page. See [Enhancements](#enhancements), for more information.

{% hint style="danger" %}
**Deprecation notice**: In this release, the Organization system entity is deprecated. See [Deprecation notice](#deprecation-notice), for more information.
{% endhint %}

## Component-wise distribution

The following table lists the component-wise distribution of new feature, enhancements, and changes in the v5.6.0 release:

{% tabs %}
{% tab title="New features" %}
The following lists the usage of the new features across different components in the platform:

| New feature                                                                                                                                                   | Components                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| [Ability to integrate seamlessly with MS-Azure Active Directory (AD)  groups](#ability-to-integrate-seamlessly-with-ms-azure-active-directory-ad-groups)      | <p></p><ul><li>SAML Support - MS Azure</li><li>Settings -> Users & Groups -> Groups</li><li>Agent -> Configuration -> Permissions</li></ul> |
| <p></p><p></p><p><a href="#ability-to-manage-user-roles-and-agent-permission-via-groups">Ability to manage user roles and agent permission via groups</a></p> | <ul><li>Settings -> Users & Groups -> Groups</li><li>Agent -> Configuration -> Permissions</li></ul>                                        |
| [Ability to restrict login IP address at the company-level](#ability-to-restrict-login-ip-address-at-the-company-level)                                       | <ul><li>Login</li></ul>                                                                                                                     |
| {% endtab %}                                                                                                                                                  |                                                                                                                                             |

{% tab title="Enhancements" %}
The following lists the usage of the enhancement across different components in the platform:

| Enhancement                                                                   | Components                      |
| ----------------------------------------------------------------------------- | ------------------------------- |
| [Masking IP address in Agent Console](#1-masking-ip-address-in-agent-console) | <ul><li>Agent Console</li></ul> |
| {% endtab %}                                                                  |                                 |
| {% endtabs %}                                                                 |                                 |

## New features

### Ability to integrate seamlessly with MS-Azure Active Directory (AD)  groups

In this release, you can integrate seamlessly with MS-Azure Active Directory (AD) groups when you enable Avaamo Platform SSO integration with your MS-Azure IDP. This feature provides more security as it restricts user and group management only via MS-Azure AD.&#x20;

In order to use this feature, you must first configure and integrate MS-Azure SSO with the Avaamo Platform. See [SAML Support - MS Azure](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/identity-providers/saml-support-ms-azure), for more information on steps to integrate MS Azure with the Avaamo platform.&#x20;

* After you configure and integrate MS-Azure SSO with Avaamo Platform, the users are automatically signed in to the Avaamo Platform when they are on their corporate devices and connected to the network. See [SAML Support - MS Azure](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/identity-providers/saml-support-ms-azure), for more information on steps to integrate MS Azure with the Avaamo platform.&#x20;
* Once the users sign in, the groups set up in Azure AD are synced automatically as per the group's policy setup in MS-Azure AD.  Signed-in users are associated with the roles as set up in the Azure AD groups and access is accordingly provided in the Avaamo Platform. See [Syncing with Azure AD groups](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/users-and-permissions/groups#syncing-with-azure-ad-groups), for more information.

### Ability to manage user roles and agent permission via groups

In this release, a new concept of "Groups" has been introduced that allows you to:&#x20;

* Manage and distribute roles at the group level instead of managing at each user level.&#x20;
* Assign agent permissions to specific groups instead of assigning them to each individual user. Note that when permissions are assigned to a group, it is applicable to all the users of a group.&#x20;

This feature helps in easier and efficient user management. **Example**: Consider that you have created a group and assigned edit permission to the group in 10 agents. You wish to provide "Edit" permission to all 10 agents for a new user. Instead of providing "Edit" permission to the user individually in each agent, you can simply add the user to the group and the permission applicable to the group is now available to the new user too.

{% hint style="info" %}
**Note**: **Groups** page is available only for users with the **Settings** role. See [Roles and permissions](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/understand-roles-and-permissions), for more information.
{% endhint %}

You can create and manage groups via the Settings -> Users & Groups -> Groups page.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MTH9CBtwmlUJmxohyxA%2F-MTH9jZnYq6UGsudPrzz%2F5.6-rn-groups-avaamo.png?alt=media\&token=beb75379-efa6-4aeb-be13-be4a68d87d2f)

The following illustration depicts a group assigned with a "Testing" role and members assigned to the group:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MSR3JCnGUjJvGWoiAPH%2F-MSR64_N7zRc3x-CgHRf%2F5.6-%20create-group.png?alt=media\&token=3d889741-7c04-4315-bb0a-81cabae67051)

See [Creating and managing groups in the Avaamo Platform](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/users-and-permissions/groups#creating-and-managing-groups-in-the-avaamo-platform), for more information.

The following illustration depicts how permissions can be assigned to groups in the Agent -> Configuration -> Permission pop-up:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MTLLgyJQRe-UbO0fjma%2F-MTLWQOBJTHKtm3mQlnR%2F5.6-rn-groups-new.png?alt=media\&token=bd183826-5f67-4ab0-a6a3-168cd215434e)

See [Agent permissions](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/permissions), for more information.

### Ability to restrict login IP address at the company-level

In this release, you can control login access to the Avaamo Platform dashboard at the company level by specifying a range of allowed IP addresses on the company's profile. Dashboard users of the company can login only through allowed or restricted IP addresses. When you define IP address restrictions for a profile, a login from any other IP address to the Avaamo Platform is denied and the following message is displayed:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MTnsBAX4Z1PEBQ24FRG%2F-MTnyS5MQT5LRN-SCL7T%2F5.6.1-invalid%20email-pin.png?alt=media\&token=2660e770-dc04-4122-8d2d-ecde4648bb5c)

This feature helps in providing better overall security, remote access, and anonymity. See [Restrict login IP address](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/restrict-login-ip-address), for more information.

## Enhancements

### 1. Masking location IP address in Agent Console

In this release, masking the location IP address in the Agent Console has been enhanced to:&#x20;

* Mask all the octets of the location IP address, when enabled at the company level from the Privacy page using the **Mask user IP** slider.&#x20;
* Mask the location IP address in the Agent Console only for a specific agent instead of masking for all the agents within the company, when enabled at the agent level.

The following illustration depicts how the location IP address is masked in the Accept chat request pop-up:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MTA4_ZmJLlyv05-5_AX%2F-MTA7N84uvclp782zfsd%2F5.6.0-rn-masking-new_censored.jpg?alt=media\&token=c15f79c0-21eb-4a3e-9b92-e6eaccbdb757)

See [Masking location IP address in Agent Console](https://docs.avaamo.com/user-guide/how-to/agent-console#masking-location-ip-address-in-agent-console), for more information.

In the previous release, masking the location IP address in Agent Console was available only at the company level and only the last octet in the IP address was masked as 0.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MTA4_ZmJLlyv05-5_AX%2F-MTA6wi3lCW096sd5-FT%2F5.6.0-rn-masking-previous_censored.jpg?alt=media\&token=74b6f56c-8667-4733-bb66-4ccb2a2a3b62)

## <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MTZ5YWcSjzjFT6eEzmh%2F-MTZC9Fv7M4NnKibmWgw%2FScreenshot%202021-02-15%20at%2011.10.31%20AM.png?alt=media&#x26;token=435a778d-2525-4628-af78-58a3809180e9" alt="" data-size="line"> Deprecation notice

In order to provide better capability and flexibility of building enterprise agents in the Avaamo Conversational AI Platform, the legacy Organization system entity is deprecated from the v5.6.0 release onwards.

### Why?

Instead of trying to create a system organization entity that covers every permutation of the names for all organizations across the world,  you can consider creating a custom entity that is relevant to your context, train your agent to recognize the context in which such names must be used. This provides more flexibility on how you wish to use the Organization system entity.

### When is the support completely stopped?

Support for the deprecated features ends on March 31st, 2021. It is recommended to take appropriate action on the deprecated features for a smooth transition.

### What action to take?

* Remove references to the Organization system entity in your Dialog and Dynamic Q\&A skills.  &#x20;
* As per your business requirement, consider using a custom organization entity as a way to capture these types of proper nouns. See [Add entity types to agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-entity-types-to-agent), for more information.

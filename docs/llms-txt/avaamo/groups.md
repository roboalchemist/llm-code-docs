# Source: https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/users-and-permissions/groups.md

# Groups

Typically, in a large organization with many users, instead of creating each individual user with the required roles, you can create groups and add users to the group. This allows you to manage and assign roles at the group level instead of managing at each user level. This feature helps in easier and efficient user management. With the Groups feature, you can:

* Manage and distribute roles at the group level instead of managing at each user level.&#x20;
* Assign agent permissions to specific groups instead of assigning them to each individual user. See [Permissions](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/permissions), for more information.<br>

See [Users](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/users-and-permissions/users), for more information on how to create and manage users.

## How does it work?

You can use one of the following ways to manage Groups in the Avaamo Platform:

**Syncing with Azure AD groups**: In order to use this feature, you must first configure and integrate MS-Azure SSO with Avaamo Platform. See [SAML Support - MS Azure](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/identity-providers/saml-support-ms-azure), for more information on steps to integrate MS Azure with the Avaamo platform.&#x20;

* After you configure and integrate MS-Azure SSO with Avaamo Platform, the users are automatically signed in to the Avaamo Platform when they are on their corporate devices and connected to the network. See [SAML Support - MS Azure](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/identity-providers/saml-support-ms-azure), for more information on steps to integrate MS Azure with the Avaamo platform.&#x20;
* Once the users sign in, the groups set up in Azure AD are synced automatically as per the group's policy setup in MS-Azure AD.  Signed-in users are associated with the roles as set up in the Azure AD groups and access is accordingly provided in the Avaamo Platform. See [Syncing with Azure AD groups](#syncing-with-azure-ad-groups), for more information.

This feature provides more security as it restricts user and group management only via MS-Azure AD. &#x20;

**Creating and managing groups in the Avaamo Platform**: If you are not using MS-Azure AD integration with the Avaamo Platform, then you can also independently create and manage groups in the Avaamo Platform itself.  See [Creating and managing groups in the Avaamo Platform](#creating-and-managing-groups-in-the-avaamo-platform) and [Agent permissions](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/permissions), for more information.

{% hint style="info" %}
**Note**: **Groups** page is available only for users with the **Settings** role. See [Roles and permissions](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/understand-roles-and-permissions), for more information.
{% endhint %}

## Syncing with Azure AD groups

* If you have **Settings** role access, then you can view the groups as per the groups claims policy setup in MS-Azure AD in the Settings -> User & Groups -> Groups page. See [User Attribute and Claims](https://docs.avaamo.com/user-guide/how-to/identity-providers/saml-support-ms-azure#user-attributes-and-claims), for more information.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MTFLZ3TDilqEDFxFnxL%2F-MTFMFUtZ7vTgqY0_f_s%2F5.6-saml-group-dashboard.png?alt=media\&token=a7e5c77d-a53d-4235-b984-377c357c72a2)

* The group object IDs are displayed in the **Group name** column. This is the same unique identifier for each group created in the MS-Azure AD application.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MTFQSHh2YK2bztIxvNw%2F-MTFRThOMdPQZY7NAKM9%2F5.6-saml-group-azure.png?alt=media\&token=ccd3bd11-0df9-4005-a883-26a96fa37c6f)

* Click **Edit** and update the group name as per your requirement.&#x20;

{% hint style="info" %}
**Notes**:

* The **Group name** must be unique.
* When groups are synced from MS-Azure AD, certain admin-related security groups also visible in the **Groups** page. Hence, it is recommended to edit the group names for those groups that have a significance in the Avaamo Platform. This helps in easy identification.
  {% endhint %}

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MTFLZ3TDilqEDFxFnxL%2F-MTFOAp-xtBLroirmPxj%2F5.6-saml-group-dashboard-edit.png?alt=media\&token=4951ef4b-227c-4383-b2e2-7c856d391be8)

{% hint style="success" %}
**Key Points**:&#x20;

* You can now manage all the users and groups via Azure AD and it is synced when the user logs in to the Avaamo Platform Dashboard. For example, if you assign the roles for a group, then the same is applied to the user when the user logs out and logs back into the Avaamo Platform.&#x20;
* Deleted users or groups in the MS-Azure AD are synced once every 40 minutes. Note that this works only when provisioning is enabled in MS-Azure AD.
* If users log out from the Avaamo dashboard, then the users are logged out from MS-Azure IDP too.
  {% endhint %}

## Creating and managing groups in the Avaamo Platform

{% hint style="info" %}
**Note**: This option is provided when you wish to create and manage groups within the Avaamo Platform itself and hence available only when you are logged in to the Avaamo Platform without using MS Azure SSO. &#x20;
{% endhint %}

In the **Groups** page, you view and manage all the groups in the company. You can also define roles for each group.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MSHt_Qz5yFm-tUutHSS%2F-MSHvPVqEf8WS0YYEmQz%2F5.6-groups.png?alt=media\&token=c9353152-690f-44dd-8bfa-eccf95eae402)

### Create group and add members

* In the **Groups** page, click **Create.**
* Specify the name and description of the group with the following details and click **Submit.** Note that the Group name must be unique
  * **Roles**: Select the roles applicable to the group. The roles selected is associated with all the users (members) in the group. See [Roles and permissions](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/understand-roles-and-permissions), for more information.
  * **Add members**: Add a list of users to the group. As you start entering the name, a list of user names is displayed. Select the users and click **Add**. Click **Delete** in the **Actions** column, if you wish to delete the user from the group.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbFW0cwSaEh99AXALgI%2F-MbFecj6flscIswqHt1t%2F5.7-roles-groups.png?alt=media\&token=901bf9cf-7981-4b9a-99ec-0af366ca8fe2)

{% hint style="info" %}
**Note**: If a user belongs to multiple groups, then the roles applicable to a user is a union of all the roles from individual groups.&#x20;

**Example**: Consider the following scenario:

* Group 1 is associated with the Development role
* Group 2 is associated with the Testing role
* User John Miller is added to Group 1 and Group 2.

Roles applicable to John Miller -> Roles from Group 1 + Roles from Group 2. Hence, John Miller has both Development and Testing role.
{% endhint %}

### Delete group

In the **Groups** page, click the **Delete** option in the **Actions** column for a group that you wish to delet&#x65;**.**&#x20;

* The following pop-up message is displayed. Note that deleting a group revokes all the access to the users provided through that group.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MTFRpd5FcDI7v-HdVlD%2F-MTFSZlySH9UsEAqZKBj%2F5.6-group-manual-delete.png?alt=media\&token=a94e2367-1575-4062-a574-928548bf3730)

* Click OK to confirm the deletion.&#x20;

### Edit group

In the **Groups** page, click **Edit** in the Actions column of the user. The **Groups** page is displayed. Edit the group details as required and click **Submit**. Note that the Group name must be unique.

## Access token for users in groups

The **User access token** is used for APIs when user authentication is required.&#x20;

Click the user icon at the top-right corner of your dashboard. You can either use the access token that is already available or click **Regenerate Access Token** to generate a new one. Note that each access token is user-specific.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MbFfsyXVtmZjjF-AqEY%2F-MbFgG2tiMS-kMqVu3Bb%2F5.7-access-token-groups.png?alt=media\&token=6f2effe9-b6e1-4a32-bebb-2b3817a321ed)

See [Message API](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/message-api#header), for an example of user token usage.

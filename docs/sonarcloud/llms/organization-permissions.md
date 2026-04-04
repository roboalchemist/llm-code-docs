# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/organization-permissions.md

# Managing organization permissions

This section explains how to manage the user and group permissions related to an organization.

{% hint style="info" %}
It’s recommended to manage the permissions through the user groups, see [user-groups](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/user-groups "mention"). This feature is available starting in Team plan. In addition, with the Team plan, you can manage the permissions set by default to new projects, see [templates](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/manage-org-projects/manage-project-permissions/templates "mention").
{% endhint %}

### Permissions related to an organization <a href="#permissions-related-to-organization" id="permissions-related-to-organization"></a>

<table><thead><tr><th width="224">Permission Type</th><th>Description</th></tr></thead><tbody><tr><td>Execute analysis</td><td>Can start an analysis on every project in the organization. This includes the ability to get all settings required to perform an analysis (including secured settings like passwords) and to push analysis results to the SonarQube Cloud server.</td></tr><tr><td>Administer Quality Gates</td><td>Can create and update <a data-mention href="../../../improving/quality-gates">quality-gates</a> that can be applied to the organization’s projects.</td></tr><tr><td>Administer Quality Profiles</td><td>Can create and update quality profiles that can be applied to the organization’s projects. See <a data-mention href="../../../standards/managing-quality-profiles">managing-quality-profiles</a> for more details.</td></tr><tr><td>Create Projects</td><td>Can create new projects in the organization.</td></tr><tr><td>Administer Organization</td><td>Has full control over the organization.</td></tr></tbody></table>

{% hint style="info" %}
View access to organizations is not managed through permissions but depends on the organization’s subscription plan: any user can view a free plan organization whereas access to a Team or Enterprise plan organization is restricted to its members. See [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") for more information.
{% endhint %}

### Setting the permissions of the groups and users <a href="#setting-permissions" id="setting-permissions"></a>

You must be an organization admin to be able to manage the permissions related to your organization.

{% hint style="info" %}
If you have a Free plan organization, you cannot change group permissions.
{% endhint %}

To set the organization-related permissions of the groups and users:

1. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more information.
2. Go to **Administration** > **Permissions**. The **Permissions** page opens.
3. In the permissions grid, select a check box to grant the corresponding permission.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-4772e595c6d970c7b5c4329810efea3a33db6ab1%2Fa936db4b2b10b51ae73d21a09681589617c4fbba.png?alt=media" alt="On SonarQube Cloud&#x27;s Permissions page, Users and Groups can be filtered on the left side, while the Permissions applied to each user is on the right side."><figcaption></figcaption></figure></div>

### Transferring ownership of an organization <a href="#transferring-ownership-of-organization" id="transferring-ownership-of-organization"></a>

As the administrator, there may be cases where you wish to transfer ownership of an organization. For example, if you are leaving a team or company, you can simply grant the **Administer Organization** permission to another member, see [organization-permissions](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/organization-permissions "mention") for more details.

### Restoring administrator access to an organization <a href="#restoring-administrator-access" id="restoring-administrator-access"></a>

If you lost administrator access to your organization, send a request to [contact@sonarsource.com](http://contact@sonarsource.com) with all the necessary details.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [setup-overview](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setup-overview "mention")
* [introduction](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/introduction "mention") to Managing your subscription
* [introduction](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setting-config-at-org-level/introduction "mention") to Performing global analysis setup
* [organization-members](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/organization-members "mention")
* [user-groups](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/user-groups "mention")
* [projects-management-page](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/manage-org-projects/projects-management-page "mention")

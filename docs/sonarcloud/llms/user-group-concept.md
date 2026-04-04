# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/user-management/user-group-concept.md

# User group concept

To manage permissions more easily, the members of an organization are managed through groups. The following applies:

* Permissions can be set at both user and group levels.
* A user can belong to several groups within an organization.
* A user’s permissions are the sum of all the permissions granted to them individually plus all the permissions granted by the groups they are a member of.

Built-in groups are added to each organization. Starting in [Team plan](https://www.sonarsource.com/plans-and-pricing/sonarcloud/), you can define and add custom groups to your organization.

### Built-in groups <a href="#built-in-groups" id="built-in-groups"></a>

When a new organization is created, two built-in groups are automatically created for the organization:

* **Members** group: This group contains all DevOps platform (DOP) users of the organization. Any DOP user added to the organization is automatically added to this group. See [devops-platform-authentication](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/user-management/devops-platform-authentication "mention") for more details.
* **Owners** group: This group is intended to include the organization admins. The organization’s creator, if they use a DOP user account, is automatically added to this group. By default, members of this group have full control over the organization.

You can never delete the Members group, or change its name and composition. Starting in Team plan, you can:

* Change the permissions of the Members group.
* Manage the Owners group: change its name, composition, and permissions; or delete it.

The figure below shows the two groups related by default to an organization.

<figure><img src="broken-reference" alt="The Members group and Owners group are both assigned to a SonarQube Cloud Organization."><figcaption></figcaption></figure>

### Built-in group permissions on Free plan <a href="#built-in-group-permissions-on-free" id="built-in-group-permissions-on-free"></a>

This section shows the permissions assigned to the built-in groups in a Free plan organization.

{% hint style="info" %}
In a Team or Enterprise organization, those permissions are default permissions that you can change.
{% endhint %}

<details>

<summary>Organization-level permissions</summary>

| **Permission type**         | **Description**                                                                            | **Members** | **Owners** |
| --------------------------- | ------------------------------------------------------------------------------------------ | ----------- | ---------- |
| Administer Quality Gates    | Can create and update quality gates that can be applied to the organization’s projects.    | <p><br></p> | x          |
| Administer Quality Profiles | Can create and update quality profiles that can be applied to the organization’s projects. | <p><br></p> | x          |
| Create Projects             | Can create new projects in the organization.                                               | <p><br></p> | x          |
| Administer                  | Has full control over the organization.                                                    | <p><br></p> | x          |

</details>

<details>

<summary>Project-level permissions</summary>

| **Permission Type**          | **Description**                                                                                                                                                                                                                                                                                                           | **Members** | **Owners**  |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ----------- |
| Browse Project               | <p>Applies only to private projects.<br>Can view the project.</p>                                                                                                                                                                                                                                                         | x           | <p><br></p> |
| See Source Code              | <p>Applies only to private projects.<br>Can view the source code (via API and web view) provided the Browse project permission is also granted.</p>                                                                                                                                                                       | x           | <p><br></p> |
| Administer Issues            | <p>Can perform the following actions:</p><p>• Accept an issue</p><p>• Mark an issue as False positive</p>                                                                                                                                                                                                                 | x           | <p><br></p> |
| Administer Security Hotspots | Can change the status of a security hotspot. For private projects, the Browse project permission must also be granted.                                                                                                                                                                                                    | x           | <p><br></p> |
| Execute Analysis             | Can start an analysis on the project. This includes the ability to get all settings required to perform an analysis (including secured settings like passwords) and to push analysis results to the SonarQube Cloud server.                                                                                               | <p><br></p> | x           |
| Administer                   | <p>Can perform the following actions:</p><p>• Delete a project.</p><p>• Change the project settings including project-level permissions.</p><p>• Configure various project functions, such as PDF reporting, snapshots, and webhooks.</p><p>For private projects, the Browse project permission must also be granted.</p> | <p><br></p> | x           |

</details>

{% hint style="info" %}
Groups are only supported at the organization level.
{% endhint %}

### Related pages <a href="#related-pages" id="related-pages"></a>

* [user-groups](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/user-groups "mention")
* [organization-permissions](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/organization-permissions "mention")
* Setting the project-related permissions of a group:
  * [templates](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/manage-org-projects/manage-project-permissions/templates "mention") (through templates)
  * [setting-permissions](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/setting-permissions "mention")

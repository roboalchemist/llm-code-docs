# Source: https://docs.sonarsource.com/sonarqube-community-build/project-administration/setting-project-permissions.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/project-administration/setting-project-permissions.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/project-administration/setting-project-permissions.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/project-administration/setting-project-permissions.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/project-administration/setting-project-permissions.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/project-administration/setting-project-permissions.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/project-administration/setting-project-permissions.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/project-administration/setting-project-permissions.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/project-administration/setting-project-permissions.md

# Source: https://docs.sonarsource.com/sonarqube-server/project-administration/setting-project-permissions.md

# Setting project permissions

When a project is created, a set of permissions defined through a permission template is applied by default. You can update these permissions provided you’re a project admin.

{% hint style="info" %}
If permissions are synchronized automatically in your system, you cannot update them manually. See [#if-permission-synchronization](#if-permission-synchronization "mention") for additional information.
{% endhint %}

### Permissions related to a project <a href="#project-level-permissions" id="project-level-permissions"></a>

<table><thead><tr><th width="155">Permission Type</th><th>Description</th></tr></thead><tbody><tr><td>Browse Project</td><td><p>Applies only to private projects (Anyone, including anonymous users, can view the public projects.).</p><p>Can view the project.</p></td></tr><tr><td>See Source Code</td><td><p>Applies only to private projects.</p><p>Can view the source code (via API and web view) provided the Browse project permission is also granted.</p></td></tr><tr><td>Administer Issues</td><td><p>Can perform the following actions:</p><p>• Accept an issue</p><p>• Mark an issue as False positive</p></td></tr><tr><td>Administer Security Hotspots</td><td>Can change the status of a security hotspot. For private projects, the Browse project permission must also be granted.</td></tr><tr><td>Administer project</td><td><p>Can perform the following actions:</p><p>• Delete a project.</p><p>• Change the project settings including project-level permissions.</p><p>• Configure various project functions, such as PDF reporting, snapshots, and webhooks.</p><p>For private projects, the Browse project permission must also be granted.</p></td></tr><tr><td>Execute Analysis on project</td><td>Can start an analysis on the project. This includes the ability to get all settings required to perform an analysis (including secured settings like passwords) and to push analysis results to SonarQube.</td></tr></tbody></table>

### Changing the project visibility <a href="#changing-project-visibility" id="changing-project-visibility"></a>

By default, any newly created project will be public. It means every SonarQube user, authenticated or not, will be able to:

* **Browse**: Access a project, browse its measures and issues, and perform some issue edits (confirm, assign, comment).
* **See Source Code**: View the project’s source code.

If you want to be sure only a limited list of groups and users can see the project, you need to change its visibility to private. Once a project is private you will be able to define which groups and users can **Browse** the project or **See Source Code**.

To change the visibility of your project:

1. Retrieve the project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-server/user-guide/viewing-projects/retrieving-projects "mention") for more information.
2. Go to **Project settings > Permissions**. The **Permissions** page opens.
3. Select **Public** or **Private**.

{% hint style="info" %}
As a system administrator, you can change the default project visibility for new projects. See [user-permissions](https://docs.sonarsource.com/sonarqube-server/instance-administration/user-management/user-permissions "mention").
{% endhint %}

### Updating the permissions of your project <a href="#updating-resetting-permissions" id="updating-resetting-permissions"></a>

To update the permissions of your project

1. Retrieve the project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-server/user-guide/viewing-projects/retrieving-projects "mention") for more information.
2. Go to **Project settings > Permissions**. The **Permissions** page opens.
3. Select a check box on a user or group row to change the respective permission.

{% hint style="info" %}
Only System Administrator can apply a permission template to a project. See [#permission-templates](https://docs.sonarsource.com/sonarqube-server/instance-administration/user-management/user-permissions#permission-templates "mention") for more information.
{% endhint %}

### If permissions are synchronized automatically <a href="#if-permission-synchronization" id="if-permission-synchronization"></a>

Project permission synchronization is enabled if you use GitHub, GitLab, or SCIM’s automatic user and group provisioning mode in SonarQube Server. In that case, you cannot change the project permissions of auto-provisioned users. However, you can remove the permissions of local users (Local users are all the users who are not managed through the automatic provisioning process, i.e. manually created users and through another identity provider Just-in-Time-provisioned users.).

### Related pages <a href="#related-pages" id="related-pages"></a>

* As a System Administrator, you can set permissions at the system level for global and project permissions:
  * [user-permissions](https://docs.sonarsource.com/sonarqube-server/instance-administration/user-management/user-permissions "mention")
* Project permission synchronization is enabled with:
  * SCIM automatic provisioning [overview](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/saml/scim/overview "mention") page
  * [github](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/github "mention") automatic provisioning
  * GitLab [automatic](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/gitlab/provisioning-modes/automatic "mention")

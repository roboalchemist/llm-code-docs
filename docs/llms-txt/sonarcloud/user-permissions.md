# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/user-management/user-permissions.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/user-management/user-permissions.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/user-management/user-permissions.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/user-management/user-permissions.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/user-management/user-permissions.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/user-management/user-permissions.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/user-management/user-permissions.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/user-management/user-permissions.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/user-management/user-permissions.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/user-management/user-permissions.md

# Managing permissions

As a System Administrator, you can grant users and groups global permissions (permissions not related to a project) and you can manage the project-related permissions granted by default when a new project is created.

{% hint style="info" %}
Permissions can be set automatically depending on the authentication and provisioning method used.
{% endhint %}

### Setting the global permissions <a href="#global-permissions" id="global-permissions"></a>

<details>

<summary>List of global permissions</summary>

<table><thead><tr><th width="173">Permission type</th><th>Description</th></tr></thead><tbody><tr><td>Administer System</td><td>Has full control over the SonarQube instance.</td></tr><tr><td>Administer Quality Gates</td><td>Can create and update quality gates that can be applied to the organization’s projects.</td></tr><tr><td>Administer Quality Profiles</td><td><ul><li>Can create and update quality profiles that can be applied to the organization’s projects. </li><li>Can add tags to rules.</li></ul></td></tr><tr><td>Execute analysis</td><td><p>Can start an analysis on every project in SonarQube. This includes the ability to get all settings required to perform an analysis, including secured settings like passwords, and to push analysis results to SonarQube.</p><p><br>This permission is applied by default to the <code>sonar-users</code> group, which means that its users can see the branch status of any project, even if they don’t have explicit permissions for it. We recommend that after you install SonarQube, you review all global permissions and ensure they comply with your company policy.</p></td></tr><tr><td>Create Projects</td><td>Can create new projects in SonarQube.</td></tr><tr><td>Create Applications</td><td>Can create new applications in SonarQube.</td></tr><tr><td>Create Portfolios</td><td>Can create new portfolios in SonarQube.</td></tr></tbody></table>

</details>

<details>

<summary>Setting the global permissions of groups and users</summary>

To set the global-level permissions of the groups and users:

1. In the top navigation bar, go to **Administration** > **Security** > **Global permissions**. The **Global Permissions** page opens.
2. You can search for users or groups.
3. In the permissions grid, select a check box to grant the corresponding permission.

</details>

### Changing the default visibility of new projects <a href="#changing-default-project-visibility" id="changing-default-project-visibility"></a>

By default, any newly created project will be public. It means every SonarQube user, authenticated or not, will be able to:

* **Browse**: Access a project, browse its measures and issues, and perform some issue edits (confirm, assign, comment).
* **See Source Code**: View the project’s source code.

To change the default visibility of new projects:

1. In the top navigation bar, go to **Administration** > **Projects** > **Management**.
2. In the top right corner of the page, select the pen icon near **Default visibility of new projects**. The **Set Default Visibility of New Projects** dialog opens.
3. Select **Public** or **Private**.
4. Select **Change default visibility**.

### Managing project-related permissions through templates <a href="#permission-templates" id="permission-templates"></a>

A permission template defines the project-related permissions granted to groups and members of the organization.

As a System Administrator, you can define several permission templates in your organization:

* You define the default template.
* You can define a template that applies to specific projects according to their key pattern by using a regular expression.

When a new project is created, SonarQube Server uses a permission template to grant the default permissions on the project. It retrieves the template according to the following rules:

* If the project key complies with the project key pattern of a template, then this template is used.\
  If several templates comply, an error is raised.
* Otherwise, the default template is used.

<details>

<summary>Creating a new template</summary>

1. In the top navigation bar, go to **Administration > Security > Permission Templates**. The **Permission Templates** page opens with the list of templates.
2. Select the **Create** button. The **Create Permission Template** dialog opens.
3. Enter the template name and description.
4. If you want to apply the template to specific new projects according to their key, enter the corresponding regular expression in **Project key pattern**.\
   The regular expression must specify the complete key (not only a part of the key). For example, to match the project keys `abc-def1-<anyString>` and `abc-def2-<anyString>`, use the pattern `^abc-(def1|def2)-.*`.
5. Select the **Create** button. The dialog closes and the new template is displayed.
6. Set the permissions by selecting the respective check boxes.

</details>

<details>

<summary>Setting the default template for projects, applications or portfolios</summary>

1. In the top navigation bar, go to **Administration > Security > Permission Templates**. The **Permission Templates** page opens with the list of templates.
2. Select the three-dot menu to the far right of the template you want to change.
3. In the menu, select **Set Default for Projects**, **Set Default for Applications**, or **Set Default for Portfolios**.

</details>

<details>

<summary>Deleting a template</summary>

1. In the top navigation bar, go to **Administration > Security > Permission Templates**. The **Permission Templates** page opens with the list of templates.
2. Select the three-dot menu to the far right of the template you want to delete.
3. In the menu, select **Delete** and confirm.

</details>

<details>

<summary>Changing a template</summary>

1. In the top navigation bar, go to **Administration > Security > Permission Templates**. The **Permission Templates** page opens with the list of templates.
2. Select the three-dot menu to the far right of the template you want to change.
3. In the menu:
   * To change the template name, description or patter: select **Update Details**.
   * To change the template permissions, description or patter: select **Edit Permissions**.

Please note that changing the template does not automatically apply the updated permissions to projects associated with it. You must reapply the template to your projects.

</details>

<details>

<summary>Applying a permission template to several projects at a time</summary>

1. In the top navigation bar, go to **Administration > Projects > Management.**
2. Retrieve and select in the grid the projects you want to update.
3. In the tool bar, select **Bulk Apply Permission Template**. The **Bulk Apply Permission Template** dialog opens.
4. Select the template and select **Apply**.

</details>

Following are the project related permissions that you can manage through a permission template:

<details>

<summary>List of project related permissions</summary>

<table><thead><tr><th width="155">Permission Type</th><th>Description</th></tr></thead><tbody><tr><td>Browse Project</td><td><p>Applies only to private projects (Anyone, including anonymous users, can view the public projects.).</p><p>Can view the project.</p></td></tr><tr><td>See Source Code</td><td><p>Applies only to private projects.</p><p>Can view the source code (via API and web view) provided the Browse project permission is also granted.</p></td></tr><tr><td>Administer Issues</td><td><p>Can perform the following actions:</p><p>• Accept an issue</p><p>• Mark an issue as False positive</p></td></tr><tr><td>Administer Security Hotspots</td><td>Can change the status of a security hotspot. For private projects, the Browse project permission must also be granted.</td></tr><tr><td>Administer project</td><td><p>Can perform the following actions:</p><p>• Delete a project.</p><p>• Change the project settings including project-level permissions.</p><p>• Configure various project functions, such as PDF reporting, snapshots, and webhooks.</p><p>For private projects, the Browse project permission must also be granted.</p></td></tr><tr><td>Execute Analysis on project</td><td>Can start an analysis on the project. This includes the ability to get all settings required to perform an analysis (including secured settings like passwords) and to push analysis results to SonarQube.</td></tr></tbody></table>

</details>

### Restoring administrator access to SonarQube Server <a href="#restoring-admin-access" id="restoring-admin-access"></a>

If you lost global administrator access to SonarQube Server, you can restore it by executing the following queries directly in your database. You can:

* Regrant the global Administer System permission to an existing user.
* Reactivate and/or reset the password of the built-in `admin` account

<details>

<summary>Regranting the Administer System permission to a user</summary>

Use the query below where `<userLogin>` represents the login of the user who should become a system administrator:

```sql
insert into user_roles(uuid, user_uuid, role)
values ('random-uuid', (select uuid from users where login='<userLogin>'), 'admin');
```

</details>

<details>

<summary>Reactivating the built-in admin account</summary>

If you changed and then lost the password to the built-in `admin` account or deactivated this user, you can activate the user and reset the password using the following query, depending on the database engine:

**PostgreSQL and Microsoft SQL Server**

```sql
update users set
crypted_password='100000$t2h8AtNs1AlCHuLobDjHQTn9XppwTIx88UjqUm4s8RsfTuXQHSd/fpFexAnewwPsO6jGFQUv/24DnO55hY6Xew==',
salt='k9x9eN127/3e/hf38iNiKwVfaVk=',
hash_method='PBKDF2',
reset_password='true',
user_local='true',
active='true'
where login='admin';
```

**Oracle**

```sql
update users set
crypted_password='100000$t2h8AtNs1AlCHuLobDjHQTn9XppwTIx88UjqUm4s8RsfTuXQHSd/fpFexAnewwPsO6jGFQUv/24DnO55hY6Xew==',
salt='k9x9eN127/3e/hf38iNiKwVfaVk=',
hash_method='PBKDF2',
reset_password=1,
user_local=1,
active=1
where login='admin';
```

</details>

### Related pages <a href="#related-pages" id="related-pages"></a>

* [setting-project-permissions](https://docs.sonarsource.com/sonarqube-server/project-administration/setting-project-permissions "mention")
* [authentication](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication "mention")

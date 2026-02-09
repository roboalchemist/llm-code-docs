# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/manage-org-projects/manage-project-permissions/templates.md

# Using permission templates

*This feature is only available in the Team and Enterprise plans. See* [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") *for more information.*

As the organization admin, using permission templates allows you to:

* Define the permissions granted by default to users, groups, project creators, and individual users on new projects.&#x20;
* Apply different sets of permissions to one or several projects at a time.

{% hint style="info" %}
If you have a Free plan organization, the permissions set to the built-in groups (Members and Owners) on new projects are defined through the default built-in template and cannot be changed. See [#built-in-group-permissions-on-free](https://docs.sonarsource.com/sonarqube-cloud/about-sonarqube-cloud-solution/user-management/user-group-concept#built-in-group-permissions-on-free "mention")for more information.
{% endhint %}

### Introduction to the permission template concept <a href="#introduction" id="introduction"></a>

A permission template defines the project-related permissions granted to groups and members of the organization.

You can define several permission templates in your organization:

* You define the default template.
* You can define a template that applies to specific projects according to their key pattern by using a regular expression.

When a new project is created, SonarQube Cloud uses a permission template to grant the default permissions on the project. It retrieves the template according to the following rules:

* If the project key complies with the project key pattern of a template, then this template is used.\
  If several templates comply, an error is raised.
* Otherwise, the default template is used.

### Creating a new template <a href="#create-template" id="create-template"></a>

1. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more details.
2. Go to **Administration** > **Permission Templates**. The **Permission Templates** page opens with the list of templates.
3. Select the **Create** button. The **Create Permission Template** dialog opens.
4. Enter the template name and description.
5. If you want to apply the template to specific new projects according to their key, enter the corresponding regular expression in **Project key pattern**.\
   The regular expression must specify the complete key (not only a part of the key). For example, to match the project keys `abc-def1-<anyString>` and `abc-def2-<anyString>`, use the pattern `^abc-(def1|def2)-.*`.
6. Select the **Create** button. The dialog closes and the new template is displayed.
7. Set the permissions by selecting the respective check boxes. See [#project-level-permissions](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/setting-permissions#project-level-permissions "mention") for more information about the project permissions.

### Setting the default template <a href="#set-default-template" id="set-default-template"></a>

1. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more details.
2. Go to **Administration** > **Permission Templates**. The **Permission Templates** page opens with the list of templates.
3. Select the three-dot menu to the far right of the template you want to change.
4. In the menu, select **Set Default**.

### Deleting a template <a href="#delete-template" id="delete-template"></a>

1. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more details.
2. Go to **Administration** > **Permission Templates**. The **Permission Templates** page opens with the list of templates.
3. Select the three-dot menu to the far right of the template you want to delete.
4. In the menu, select **Delete** and confirm.

### Changing a template <a href="#change-template" id="change-template"></a>

1. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more details.
2. Go to **Administration** > **Permission Templates**. The **Permission Templates** page opens with the list of templates.
3. Select the three-dot menu to the far right of the template you want to change.
4. In the menu:
   * To change the template name, description or patter: select **Update Details**.
   * To change the template permissions, description or patter: select **Edit Permissions**.

### Applying a permission template to projects <a href="#apply-template-to-several-projects" id="apply-template-to-several-projects"></a>

You can apply a permission template to a project, or, with the Enterprise plan, to several projects at a time.&#x20;

#### To a single project

1. Retrieve the project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") for more details.
2. In the left sidebar, select **Administration** > **Permissions**. The **Permissions** page opens.
3. Select the **Apply Permission Template** button in the top right corner of the page. The **Apply Permission Template** dialog opens.
4. Select the template you want to apply and select the **Apply** button.

#### To several projects at a time

1. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more details.
2. Go to **Administration** > **Projects management.**
3. Retrieve and select the projects you want to update.
4. In the tool bar, select **Bulk Apply Permission Template**. The **Bulk Apply Permission Template** dialog opens.
5. Select the template and select **Apply**.

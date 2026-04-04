# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/setting-permissions.md

# Setting user permissions

As a project admin, you can update your project’s permissions manually or, with a [Team or Enterprise plan](https://www.sonarsource.com/plans-and-pricing/sonarcloud/) organization, reset the default permissions and apply a permission template defined by the organization administrator.

{% hint style="info" %}
If you are an organization admin, you can:

* Apply a permission template to several projects of your Enterprise plan organization at a time. See [projects-management-page](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/manage-org-projects/projects-management-page "mention") for more information.
* Recover administration access to an organization’s project. See [recovering-admin-access](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/manage-org-projects/manage-project-permissions/recovering-admin-access "mention") for more information.
  {% endhint %}

### Permissions related to a project <a href="#project-level-permissions" id="project-level-permissions"></a>

| **Permission Type**          | **Description**                                                                                                                                                                                                                                                                                                           |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Browse Project               | <p>Applies only to private projects (Anyone, including anonymous users, can view the public projects.).</p><p>Can view the project.</p>                                                                                                                                                                                   |
| See Source Code              | <p>Applies only to private projects.</p><p>Can view the source code (via API and web view) provided the Browse project permission is also granted.</p><p><strong>Note</strong>: Anonymous and unauthorized users are prevented from easily downloading public projects’ source code via API and web views.</p>            |
| Administer Issues            | <p>Can perform the following actions:</p><p>• Accept an issue</p><p>• Mark an issue as False positive</p>                                                                                                                                                                                                                 |
| Administer Security Hotspots | Can change the status of a security hotspot. For private projects, the Browse project permission must also be granted.                                                                                                                                                                                                    |
| Execute Analysis on project  | Can start an analysis on the project. This includes the ability to get all settings required to perform an analysis (including secured settings like passwords) and to push analysis results to the SonarQube Cloud server.                                                                                               |
| Administer project           | <p>Can perform the following actions:</p><p>• Delete a project.</p><p>• Change the project settings including project-level permissions.</p><p>• Configure various project functions, such as PDF reporting, snapshots, and webhooks.</p><p>For private projects, the Browse project permission must also be granted.</p> |

### Updating the permissions of your project <a href="#updating-resetting-permissions" id="updating-resetting-permissions"></a>

To update the permissions of your project:

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") for more details.
2. In the left sidebar, select **Administration** > **Permissions**. The **Permissions** page opens.
3. Navigate to the bottom of the page to view the list of users and groups.
4. Select the check box to change the permissions.

### Changing the project’s visibility <a href="#changing-visibility" id="changing-visibility"></a>

The project’s visibility may be:

* Public: Anyone, including anonymous users, can view public projects. A public project may be part of any organization.
* Or private: Only authorized users, who are members of the organization, can view a private project. By default, the visibility of newly created projects is set to private on [Free, Team and Enterprise](https://www.sonarsource.com/plans-and-pricing/#sonarqube-cloud-features) plans.

If you’re a project admin, you can change your project’s visibility.

To change the visibility of your project:

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") for more details.
2. In the left sidebar, select **Administration** > **Permissions**. The **Permissions** page opens.
3. In the **Project visibility** section, select the **Public** or **Private** checkbox. (You can also upgrade your organization from this section.) The **Turn to Private / Public** dialog opens.
4. Confirm the change.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [setting-up-project](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/setting-up-project "mention")
* [introduction](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/devops-platform-integration/introduction "mention") to Setting up the integration of your project with your DevOps platform
* [changing-binding](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/changing-binding "mention")
* [customizing-info-page](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/customizing-info-page "mention")
* [deleting-project](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/deleting-project "mention")

# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/manage-org-projects/manage-project-permissions/recovering-admin-access.md

# Restoring administrator access

If you lost administrator access to a project of your organization, you can restore it if you’re an organization admin:

* At the project level. This requires the Browse Project permission in case of a private project.
* By using the Projects Management page. This is only possible with an Enterprise plan.
* By using the API.

### At the project level <a href="#project-level" id="project-level"></a>

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") for more details.
2. In the left sidebar, select **Administration** > **Restore access**. The **Restore admin permissions** dialog opens.
3. Select the **Restore permissions** button. You are now granted the Administer and/or Browse permission for the project.

### By using the Projects Management page <a href="#projects-management-page" id="projects-management-page"></a>

This method is only possible with an Enterprise plan organization.

To restore administrator access to a project by using the Projects Management page:

1. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more details.
2. Go to **Administration** > **Projects Management**.
3. In the three-dot menu at the far right of the project line, select **Restore access**. You will then be granted the Administer and/or Browse permission for the project.

### By using the API <a href="#api" id="api"></a>

Use the [add\_user API endpoint](https://sonarcloud.io/web_api/api/permissions/add_user?deprecated=false) to grant an organization administrator `admin` permission to the project. To identify the project, you can use the `projectKey` (the `projectId` is optional).

### Related page <a href="#related-pages" id="related-pages"></a>

* [setting-permissions](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/setting-permissions "mention")

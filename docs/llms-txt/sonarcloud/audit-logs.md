# Source: https://docs.sonarsource.com/sonarqube-server/9.8/instance-administration/audit-logs.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/instance-administration/audit-logs.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/instance-administration/audit-logs.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/instance-administration/audit-logs.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/instance-administration/audit-logs.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/instance-administration/audit-logs.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/instance-administration/monitoring/audit-logs.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/instance-administration/monitoring/audit-logs.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/instance-administration/monitoring/audit-logs.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/server-upgrade-and-maintenance/monitoring/audit-logs.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/server-upgrade-and-maintenance/monitoring/audit-logs.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/server-update-and-maintenance/monitoring/audit-logs.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-update-and-maintenance/monitoring/audit-logs.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-update-and-maintenance/monitoring/audit-logs.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/monitoring/audit-logs.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-update-and-maintenance/monitoring/audit-logs.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/security/audit-logs.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/security/audit-logs.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/audit-logs.md

# Audit logs

*This feature is available with the Enterprise plan.*

As an Enterprise admin, you can access audit logs through the [Audit logs API](https://api-docs.sonarsource.com/sonarqube-cloud/default/public-audit-logs-1-0-1). To authenticate to the Web API, see [web-api](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/web-api "mention").

{% hint style="info" %}
Audit logs are retained for 180 days.
{% endhint %}

### List of logged events

| Event type                          | Description                                                                    | For more details                                                                                                                                                                                        |
| ----------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| authentication.user\_login          | An SSO user logs in to SonarQube Cloud.                                        |                                                                                                                                                                                                         |
| authentication.user\_logout         | An SSO user logs out of SonarQube Cloud.                                       |                                                                                                                                                                                                         |
| user.create                         | An SSO user account is created.                                                |                                                                                                                                                                                                         |
| user.remove                         | An SSO user account is removed.                                                |                                                                                                                                                                                                         |
| permission\_template.create         | An organization admin creates a permission template.                           | [templates](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/manage-org-projects/manage-project-permissions/templates "mention")                             |
| permission\_template.delete         | An organization admin deletes a permission template.                           | [templates](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/manage-org-projects/manage-project-permissions/templates "mention")                             |
| org.add\_user                       | A user is added to an organization.                                            |                                                                                                                                                                                                         |
| org.remove\_user                    | A user is removed from an organization.                                        |                                                                                                                                                                                                         |
| org.add\_group                      | A group is created in the organization.                                        | [user-group-concept](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/user-management/user-group-concept "mention")                                 |
| org.remove\_group                   | A group is removed from the organization.                                      | [user-group-concept](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/user-management/user-group-concept "mention")                                 |
| org.add\_permission                 | An organization-related permission is added to a user or group.                | [#permissions-related-to-organization](https://docs.sonarsource.com/sonarqube-cloud/managing-organization/users-and-permissions/organization-permissions#permissions-related-to-organization "mention") |
| org.remove\_permission              | An organization-related permission is removed from a user or group.            | [#permissions-related-to-organization](https://docs.sonarsource.com/sonarqube-cloud/managing-organization/users-and-permissions/organization-permissions#permissions-related-to-organization "mention") |
| org.membersync\_enabled             | An organization admin enables the GitHub member synchronization.               | [github-member-synchronization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/user-management/github-member-synchronization "mention")           |
| org.membersync\_disabled            | An organization admin disables the GitHub member synchronization.              | [github-member-synchronization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/user-management/github-member-synchronization "mention")           |
| portfolio.add\_permission           | A portfolio admin adds a portfolio-related permission to a user or group.      | [#permissions](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/administering-portfolios#permissions "mention")                                                             |
| portfolio.remove\_permission        | A portfolio admin removes a portfolio-related permission from a user or group. | [#permissions](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/administering-portfolios#permissions "mention")                                                             |
| project.apply\_permission\_template | A project admin applies a permission template to their project.                | [#updating-resetting-permissions](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/setting-permissions#updating-resetting-permissions "mention")         |
| project.add\_permission             | A project admin adds a project-related permission to a user or group.          | [#project-level-permissions](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/setting-permissions#project-level-permissions "mention")                   |
| project.remove\_permission          | A project admin removes a project-related permission from a user or group.     | [#project-level-permissions](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/setting-permissions#project-level-permissions "mention")                   |
| group.create                        | A group is created in an organization.                                         | [user-group-concept](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/user-management/user-group-concept "mention")                                 |
| group.remove                        | A group is removed from an organization.                                       | [user-group-concept](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/user-management/user-group-concept "mention")                                 |

### Related pages <a href="#related-pages" id="related-pages"></a>

[ip-allow-lists](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/ip-allow-lists "mention")\
[sso](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso "mention")

# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/manage-org-projects/migrate-projects-to-another-org.md

# Migrating projects

Once an organization is created on the SonarQube Cloud side, it is bound to its peer organization on the repository platform until one or the other is deleted. The SonarQube Cloud organization cannot be re-bound to another organization.

If you are migrating projects to another organization:

1. Create a new SonarQube Cloud organization and bind it to the new platform organization. See [setup-overview](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setup-overview "mention") for more information
2. Re-import the projects you want to analyze. See [setting-up-project](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/setting-up-project "mention") for more information.

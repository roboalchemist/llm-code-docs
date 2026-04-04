# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/setting-up-project.md

# Creating and setting up your project

To set up your project on SonarQube Cloud:

1. Create your project: You can create projects by importing your DevOps platform repositories (see below) which automatically binds new projects to the respective repository. This binding has many advantages, see [binding-with-dop](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/ressources-structure/binding-with-dop "mention") for more details. Users will need the correct permission level to create new projects. You can also create projects manually however, manually created projects are unbound.
2. Set up project integration with your DevOps platform. See [introduction](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/devops-platform-integration/introduction "mention") to DevOps platform for more details.
3. Set up user permissions for your project. See [setting-permissions](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/setting-permissions "mention") for more information.
4. Set up project analysis. See the [project-analysis](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis "mention") pages for details.

### Importing one or several repositories to SonarQube Cloud <a href="#importing-repos" id="importing-repos"></a>

{% hint style="info" %}
Repository import is only possible if your SonarQube Cloud organization is bound to its corresponding DevOps platform organization (i.e. the DevOps platform organization has been imported to SonarQube Cloud). See [binding-with-dop](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/ressources-structure/binding-with-dop "mention") for more details.
{% endhint %}

1. On the top right of the SonarQube Cloud interface, select the ✚ (plus) menu and select **Analyze new project**. The **Analyze projects** page opens.
2. Select your organization.
3. Select the repositories you want to import.
4. Select the **Set up** button. The **Set up project for Clean as You Code** page opens.
5. Select the new code definition for your project, see [about-new-code](https://docs.sonarsource.com/sonarqube-cloud/standards/about-new-code "mention") for more details.
6. Select the **Create project** button. The project is created and the [automatic-analysis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/automatic-analysis "mention") is started if supported.

{% hint style="info" %}
To import a monorepo, see [monorepo-support](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/monorepo-support "mention").
{% endhint %}

### Creating a project manually <a href="#creating-manually" id="creating-manually"></a>

1. On the top right of the SonarQube Cloud interface, select the ✚ (plus) menu and select **Analyze new project**. The **Analyze projects** page opens.
2. On the right of the page, select **create a project manually**.
3. Select the organization and enter the project name and key.
4. Click **Next**.
5. Select the new code definition for your project, see [about-new-code](https://docs.sonarsource.com/sonarqube-cloud/standards/about-new-code "mention").
6. Select the **Create project** button. The project is created. You must now set up your [overview-of-integrated-cis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/overview-of-integrated-cis "mention"). Automatic analysis is not supported for unbound projects.

By default, the visibility of newly created projects is set to private on [Free, Team and Enterprise](https://www.sonarsource.com/plans-and-pricing/#sonarqube-cloud-features) plans.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [introduction](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/devops-platform-integration/introduction "mention") Setting up the integration of your project with your DevOps platform
* [setting-permissions](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/setting-permissions "mention") and visibility
* [changing-binding](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/changing-binding "mention") and other parameters
* [customizing-info-page](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/customizing-info-page "mention")
* [deleting-project](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/deleting-project "mention")
* [importing-github-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-github-organization "mention")
* [importing-bitbucket-workspace](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-bitbucket-workspace "mention")
* [importing-gitlab-group](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-gitlab-group "mention")
* [importing-azure-devops-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-azure-devops-organization "mention")

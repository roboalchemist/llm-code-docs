# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/ressources-structure/binding-with-dop.md

# Binding with the DevOps platform

Through the integration of SonarQube Cloud with your DevOps platform (GitHub, Bitbucket Cloud, GitLab, or Azure DevOps), your organizations and projects in SonarQube Cloud are bound to their respective organization or repository on the DevOps platform.

The following applies:

* The binding is performed automatically by importing the DevOps organization and its repositories into SonarQube Cloud. Note that you cannot import repositories into SonarQube Cloud if the respective DevOps organization has not been imported into SonarQube Cloud.
* If you create organizations or projects manually (i.e., without importing the DevOps organizations or projects), they are not bound with any peers on the DevOps platform. Manual organizations and projects are like empty containers identified solely by their keys, which you choose when you create them. They are only linked to your code by you explicitly setting the analysis parameters sonar.projectKey and `sonar.organization` to those keys in your CI-based analysis setup. [automatic-analysis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/automatic-analysis "mention") is not supported for manual projects.

{% hint style="info" %}

* You can bind an unbound project and you can bind a bound project to another repository.
* You can bind an unbound organization but you cannot change the binding of a bound organization.
  {% endhint %}

The binding presents many advantages as described below.

### Advantages of bound organizations <a href="#bound-organizations" id="bound-organizations"></a>

The advantages of bound SonarQube Cloud organizations over unbound ones are:

* Bound organizations enable the easy selection and import of projects into SonarQube Cloud, as mentioned above.
* Bound organizations support automatic member synchronization. This feature is only supported with GitHub, see [devops-platform-authentication](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/user-management/devops-platform-authentication "mention") for more details.
* Importing a project via a bound organization is the only way to create a bound project, and bound projects have their own set of advantages.

### Advantages of bound projects <a href="#bound-projects" id="bound-projects"></a>

The advantages of bound SonarQube Cloud projects over unbound ones are:

* [automatic-analysis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/automatic-analysis "mention") is only available for bound projects. This feature is only supported with GitHub.
* The pull request decoration is automatically configured on bound projects if your CI tool is integrated with SonarQube Cloud.
* Upon import, bound projects on the SonarQube Cloud side automatically adopt the privacy setting of their DevOps platform peer. Projects that are private on the DevOps platform remain private on SonarQube Cloud. With manually created projects, you must make sure to explicitly set the privacy status of your SonarQube Cloud project. This opens up the possibility of inadvertently exposing the code of a private project to the public through SonarQube Cloud.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [binding-unbound-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/binding-unbound-organization "mention")
* [changing-binding](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/changing-binding "mention")

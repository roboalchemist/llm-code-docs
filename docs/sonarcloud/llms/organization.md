# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/ressources-structure/organization.md

# Organization

Projects on a repository platform are typically grouped into organizations. This enables teams to work together, define different permissions for different users, and configure common settings and features.

{% hint style="info" %}
In GitHub and Azure DevOps collections of projects are called organizations, in BitBucket Cloud, workspaces, and in GitLab, groups. For simplicity, we will refer to all of these generically as organizations.
{% endhint %}

SonarQube Cloud uses the same organization-based structure. Each organization represents an organization on the repository platform side. The SonarQube Cloud organization is created by importing and binding it to the DevOps platform organization. It’s also possible to create organizations manually but they won’t benefit from the same features. A SonarQube Cloud user can be a member of one or several organizations.

{% hint style="warning" %}
SonarQube Cloud does not support linking an organization to more than one DevOps platform. If you want to link to more than one, you will need to create a separate organization to link to each DevOps platform.
{% endhint %}

Different management and analysis features are supported for an organization depending on its [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention").

The figure below shows SonarQube Cloud reproducing the organization-based structure of the DevOps platform service it is used with.

<figure><img src="broken-reference" alt="Your SonarQube Cloud organization is bound to your DevOps platform organization."><figcaption></figcaption></figure>

### Related pages <a href="#related-pages" id="related-pages"></a>

* [setup-overview](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setup-overview "mention")
* [introduction](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/introduction "mention") to Managing your subscription
* [importing-github-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-github-organization "mention")
* [importing-bitbucket-workspace](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-bitbucket-workspace "mention")
* [importing-gitlab-group](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-gitlab-group "mention")
* [importing-azure-devops-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-azure-devops-organization "mention")
* [introduction](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setting-config-at-org-level/introduction "mention") to Performing global analysis setup
* [organization-members](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/organization-members "mention")
* [user-groups](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/user-groups "mention")
* [organization-permissions](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/organization-permissions "mention")
* [projects-management-page](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/manage-org-projects/projects-management-page "mention")

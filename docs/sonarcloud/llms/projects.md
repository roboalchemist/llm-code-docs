# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/ressources-structure/projects.md

# Organization's projects

A project in SonarQube Cloud represents a repository of a DevOps platform organization.

The project’s visibility may be:

* Public: anyone, including anonymous users, can view the code and analysis results of public projects.\
  However:
  * Non-members are not able to see the list of members in the organization.
  * Anonymous and unauthorized users are prevented from easily downloading source code via API and web views.
* Or private: only authorized users, who are organization members, can view a private project. By default, the visibility of newly created projects is set to private on [Free, Team and Enterprise](https://www.sonarsource.com/plans-and-pricing/#sonarqube-cloud-features) plans.

A project is created by importing and binding to a repository from the DevOps platform. It’s also possible to create projects manually, but they won’t benefit from the same features. A bound project inherits its visibility from its corresponding repository. However, you can change it if the organization is not on a free subscription plan. See [changing-binding](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/changing-binding "mention") for more information.

You can grant SonarQube Cloud users analysis-related permissions on the projects of the organizations they are members of. You can manage permissions through the user group function. See [user-group-concept](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/user-management/user-group-concept "mention") for more details.

The figure below shows SonarQube Cloud projects that were created by importing the repositories from a DevOps platform’s organization.

<figure><img src="broken-reference" alt="A project in SonarQube Cloud is created by importing a DevOps platform repository. The project is bound to the repository."><figcaption></figcaption></figure>

{% hint style="info" %}
Default project analysis configurations can be defined at the organization level: new code definition, quality gate, and quality profiles.
{% endhint %}

### Related pages <a href="#related-pages" id="related-pages"></a>

* [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention")
* [managing-your-project-as-developer](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/managing-your-project-as-developer "mention")
* [introduction](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/introduction "mention") to Administering your project

# Source: https://docs.sonarsource.com/sonarqube-community-build/project-administration/creating-project.md

# Creating your project

There are several ways to create a project in SonarQube Server:

* **Import from DevOps Platforms**: If your repository is hosted on GitHub, GitLab, Azure DevOps, or BitBucket, you can import it to create your corresponding project in SonarQube Server (The so created project is *bound* to the DevOps platform repository). This way, you can benefit from the integration features out of the box.
* **Local project**: For a project not linked to a DevOps platform, you can create your SonarQube project manually.
* **Automate through the API**: Both methods mentioned above can be automated using the Web API.
* **First scan**: If none of the above is relevant, you can create a project by scanning it for the first time.\
  In this case, the default configuration applies: default quality profile for each language, default quality gate, default visibility, a permissions template is applied if applicable, etc.

All the above methods require the Create Projects permission.&#x20;

{% content-ref url="creating-project/importing-repo" %}
[importing-repo](https://docs.sonarsource.com/sonarqube-community-build/project-administration/creating-project/importing-repo)
{% endcontent-ref %}

{% content-ref url="creating-project/creating-manually" %}
[creating-manually](https://docs.sonarsource.com/sonarqube-community-build/project-administration/creating-project/creating-manually)
{% endcontent-ref %}

{% content-ref url="creating-project/automating-creation" %}
[automating-creation](https://docs.sonarsource.com/sonarqube-community-build/project-administration/creating-project/automating-creation)
{% endcontent-ref %}

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/project-administration/creating-and-importing-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/project-administration/creating-and-importing-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/project-administration/creating-and-importing-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/project-administration/creating-and-importing-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/project-administration/creating-and-importing-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/project-administration/creating-and-importing-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/project-administration/creating-and-importing-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/project-administration/creating-and-importing-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/project-administration/creating-and-importing-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/project-administration/creating-and-importing-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/project-administration/creating-and-importing-projects.md

# Creating and importing projects

### Overview <a href="#overview" id="overview"></a>

There are several ways to create a project in SonarQube Server:

* **Import from DevOps Platforms**: If your project is bound to a DevOps platform and you want to benefit from the integration features out of the box.
* **Local project**: For a project not linked to a DevOps platform, you can create your SonarQube project manually.
* **Automate through the API**: Both methods mentioned above can be automated using the Web API.
* **First scan**: If none of the above is relevant, you can create a project by scanning it for the first time.

All the above methods require the Create Projects permission. See [user-permissions](https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/user-management/user-permissions "mention") for more information.

### Choosing a method for project creation <a href="#choosing-a-method-for-project-creation" id="choosing-a-method-for-project-creation"></a>

When a project is created in SonarQube Server through a first scan, the default configuration applies: default quality profile for each language, default quality gate, default visibility, a permissions template is applied if applicable, etc.

While this is handy, this method is not always desirable as it doesn’t allow a proper configuration upfront. If you want to configure your project before you run a first analysis, use one of the following options:

* **Import from DevOps Platforms**: If your project is hosted on GitHub, GitLab, Azure DevOps, or BitBucket.
* **Local project:** If your project is not hosted on a DevOps platform (in rare cases).

### Importing a DevOps platform repository <a href="#importing-repository" id="importing-repository"></a>

Once the global-level integration with your DevOps platform is complete, you can create your SonarQube Server project by importing your DevOps platform repository. The so-created SonarQube Server project is "bound" to its Azure DevOps repository. With a bound project, you benefit from integration features, such as pull request decoration, code scanning alerts, permission synchronization, etc.

To import your repository, you need the Create Projects permission in SonarQube Server and the corresponding access rights on the repository.

To import a DevOps platform repository into SonarQube Server:

1. In the top navigation bar of SonarQube Server, select the **Projects** tab.
2. In the top right corner, select the **Create Project > From \<DevOps Platform>** button.
3. If your instance has multiple DevOps platform Integrations, select the configuration from which you want to import your project.
4. Select the repository to be imported.

{% hint style="info" %}
Starting in [Enterprise Edition](https://www.sonarsource.com/plans-and-pricing/enterprise/), you can import a monorepo. See [monorepos](https://docs.sonarsource.com/sonarqube-server/2025.4/project-administration/monorepos "mention").
{% endhint %}

### Creating your SonarQube Server project manually (local project) <a href="#creating-project-manually" id="creating-project-manually"></a>

You need the Create Projects permission in SonarQube Server.

Proceed as follows:

1. In the top navigation bar of SonarQube Server, select the **Projects** tab.
2. In the top right corner, select the **Create Project > Local Project** button.

### Automating project creation and import <a href="#automating-project-creation-and-import" id="automating-project-creation-and-import"></a>

When you have a large project base, it can be beneficial to automate project creation and import using the Web API. If you’re getting started with Web APIs, check out the [web-api](https://docs.sonarsource.com/sonarqube-server/2025.4/extension-guide/web-api "mention") documentation.

#### Automate local project creation <a href="#automate-local-project-creation" id="automate-local-project-creation"></a>

Only using the Web API `POST /api/projects/create` endpoint is enough to create a local project. A name and a project key are the only necessary parameters.

#### Automate the import of projects hosted on a DevOps platform <a href="#automate-the-import-of-projects-hosted-on-a-devops-platform" id="automate-the-import-of-projects-hosted-on-a-devops-platform"></a>

You can create a project in SonarQube Server and automatically bind it with a project in your DevOps platform using the Web API.

1. As an instance administrator, you must first configure your SonarQube Server instance with your DevOps platform. You can use the `POST api/alm_settings/create_<yourPlatform>` endpoint to create the integration or set it up in the SonarQube Server UI by going to **Administration** > **Configuration** > **General Settings** > **DevOps Platform Integrations**.
2. As a user, create a SonarQube project with the information from your DevOps platform project using the `POST api/v2/dop-translation/bound-projects` [endpoint](https://next.sonarqube.com/sonarqube/web_api_v2#/dop-translation/bound-projects--post). Requirements:
   * Make sure you have the Create Project permissions. See [user-permissions](https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/user-management/user-permissions "mention") for more information.
   * Set a Personal Access Token using the `POST api/alm_integrations/set_pat` [endpoint](https://next.sonarqube.com/sonarqube/web_api/api/alm_integrations/set_pat).
   * List all DevOps platform integrations to retrieve the information needed for the project creation endpoint parameters using the `GET /api/v2/dop-translation/dop-settings` [endpoint](https://www.google.com/search?q=https://next.sonarqube.com/sonarqube/web_api_v2#/dop-translation/dop-settings--get).

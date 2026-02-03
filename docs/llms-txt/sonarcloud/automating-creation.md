# Source: https://docs.sonarsource.com/sonarqube-community-build/project-administration/creating-project/automating-creation.md

# Automating project creation and import

If you’re getting started with Web APIs, see [web-api](https://docs.sonarsource.com/sonarqube-community-build/extension-guide/web-api "mention").

### Automating the local project creation <a href="#automate-local-project-creation" id="automate-local-project-creation"></a>

Only using the Web API `POST /api/projects/create` endpoint is enough to create a local project. A name and a project key are the only necessary parameters.

### Automating the import of projects hosted on a DevOps platform <a href="#automate-the-import-of-projects-hosted-on-a-devops-platform" id="automate-the-import-of-projects-hosted-on-a-devops-platform"></a>

You can create a project in SonarQube and automatically bind it with a project in your DevOps platform using the Web API.

* As an instance administrator, you must first configure your SonarQube instance with your DevOps platform. You can use the `POST api/alm_settings/create_<yourPlatform>` endpoint to create the integration or set it up in the SonarQube UI by going to **Administration** > **Configuration** > **General Settings** > **DevOps Platform Integrations**.
* As a user, create a SonarQube project with the information from your DevOps platform project using the `POST api/v2/dop-translation/bound-projects` [endpoint](https://next.sonarqube.com/sonarqube/web_api_v2#/dop-translation/bound-projects--post). Requirements:
  * Make sure you have the Create Project permissions.&#x20;
  * Set a Personal Access Token using the `POST api/alm_integrations/set_pat` [endpoint](https://next.sonarqube.com/sonarqube/web_api/api/alm_integrations/set_pat).
  * List all DevOps platform integrations to retrieve the information needed for the project creation endpoint parameters using the `GET /api/v2/dop-translation/dop-settings` [endpoint](https://www.google.com/search?q=https://next.sonarqube.com/sonarqube/web_api_v2#/dop-translation/dop-settings--get).

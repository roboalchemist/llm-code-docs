# Source: https://docs.sonarsource.com/sonarqube-community-build/devops-platform-integration/azure-devops-integration/creating-your-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/devops-platform-integration/azure-devops-integration/creating-your-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/devops-platform-integration/azure-devops-integration/creating-your-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/devops-platform-integration/azure-devops-integration/creating-your-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/devops-platform-integration/azure-devops-integration/creating-your-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/devops-platform-integration/azure-devops-integration/creating-your-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/project-administration/creating-your-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/devops-platform-integration/azure-devops-integration/creating-your-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/project-administration/creating-your-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/creating-your-project.md

# Creating and configuring your Azure DevOps project

Once the [setting-up-integration-at-global-level](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/setting-up-integration-at-global-level "mention") with Azure DevOps is complete, you can create your SonarQube Server project by importing your Azure DevOps repository. You can also create it manually but you won’t benefit from the integration features.

{% hint style="warning" %}
It’s highly recommended to create your SonarQube Server project before running your first analysis. Creating the project from the first analysis has side-effects (e.g., you can’t choose the main branch name).
{% endhint %}

### Before your first repository import <a href="#before-first-import" id="before-first-import"></a>

On your first repository import, you will have to insert an Azure Personal Authentication Token (PAT) so that you are able to list the repositories you have access to in Azure DevOps.

Proceed as follows to create your Azure PAT:

1\. Log in to Azure DevOps.

2\. Go to your Azure DevOps organization **User settings** > **Personal access tokens** and select **+ New token**.

<figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/Nu9Gz5WaaXMQ4KOtCq3S/azure-devops-create-new-personal-access-token-for-sonarqube.png" alt="Personal access tokens page"><figcaption></figcaption></figure>

3\. On the next page, under **Scopes**, make sure that you specify at least the scope **Code** > **Read**.

4\. Click **Create** to generate the token.

5\. When the personal access token is displayed, copy it (you will have to paste it during your first repository import as described below).\
You may ask your administrator to encrypt this token. See [encrypting-settings](https://docs.sonarsource.com/sonarqube-server/instance-administration/security/encrypting-settings "mention") for more details.

### Importing your Azure DevOps repository <a href="#importing-azdo-repo" id="importing-azdo-repo"></a>

To import your repository, you need the Create Projects permission in SonarQube Server.

The so-created SonarQube Server project is "bound" to its Azure DevOps repository. With a bound project:

* You can see in the SonarQube Server UI with which repository the project is associated.
* You benefit from pull request integration features.

To import an Azure DevOps repository into SonarQube Server:

1. In the top navigation bar of SonarQube Server, select the **Projects** tab.
2. In the top right corner, select the **Create Project > From Azure DevOps** button.
3. If it’s your first repository import, you’ll be prompted to enter the Azure PAT you created as described in *Before your first repository import* above. Enter your PAT and select **Save**.

<div align="left"><figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/IYcEAvhNfVmLWVAZAyGV/azure-devops-grant-personal-access-token-for-sonarqube.png" alt="Grant access to your repositories"><figcaption></figcaption></figure></div>

4\. If your instance has multiple Azure DevOps Integrations, select the **Azure** **DevOps configuration** from which you want to import your project.

5\. Select the repository to be imported.

### Importing a monorepo <a href="#monorepo" id="monorepo"></a>

Starting in [Enterprise edition](https://www.sonarsource.com/plans-and-pricing/enterprise/), you can import an Azure DevOps monorepo. See [monorepos](https://docs.sonarsource.com/sonarqube-server/project-administration/monorepos "mention").

### Creating your SonarQube Server project manually <a href="#creating-project-manually" id="creating-project-manually"></a>

You need the Create Projects permission in SonarQube Server.

Proceed as follows:

1. In the top navigation bar of SonarQube Server, select the **Projects** tab.
2. In the top right corner, select the **Create Project > Local Project** button.

### Configuring the project analysis parameters <a href="#configuring-analysis-parameters" id="configuring-analysis-parameters"></a>

You can configure analysis parameters at different levels:

* In your build environment.
* In the `sonar-project.properties` file.
* In SonarQube Server UI.
* At the Azure pipeline level.\
  Parameters set at the pipeline level have precedence over parameters set at other levels.

For general information on setting up analysis parameters at the global and project levels, see [analysis-parameters](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/analysis-parameters "mention") and the respective SonarScanner section: [sonarscanner-for-maven](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/sonarscanner-for-maven "mention"), [sonarscanner-for-gradle](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/sonarscanner-for-gradle "mention"), [configuring](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/dotnet/configuring "mention"), or [sonarscanner](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/sonarscanner "mention").

### Related pages <a href="#related-pages" id="related-pages"></a>

* [azure-pipelines-integration-overview](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/azure-pipelines-integration-overview "mention")
* [setting-up-integration-at-global-level](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/setting-up-integration-at-global-level "mention")
* [setting-up-project-integration](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/setting-up-project-integration "mention") at the project level
* [introduction](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/introduction "mention") to adding analysis to your Azure build pipeline
* [troubleshooting-analysis](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/troubleshooting-analysis "mention")

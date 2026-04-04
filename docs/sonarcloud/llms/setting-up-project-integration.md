# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/devops-platform-integration/azure-devops-integration/setting-up-project-integration.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/devops-platform-integration/azure-devops-integration/setting-up-project-integration.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/devops-platform-integration/azure-devops-integration/setting-up-project-integration.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/devops-platform-integration/azure-devops-integration/setting-up-project-integration.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/devops-platform-integration/azure-devops-integration/setting-up-project-integration.md

# Source: https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/setting-up-project-integration.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/setting-up-project-integration.md

# Setting up project integration

### Adding SonarQube service connection to Azure Pipelines (SonarQube endpoint) <a href="#adding-sonarqube-service-connection" id="adding-sonarqube-service-connection"></a>

Service connections are authenticated connections between Azure Pipelines and external or remote services. You must declare your SonarQube Cloud as a service connection in your Azure DevOps project.

Proceed as follows:

1. In SonarQube Cloud, create an authentication token that will be used by Azure DevOps to execute the analysis of your project in SonarQube Cloud. To do so, create a personal access token *and copy it*. For more information about tokens, see [managing-tokens](https://docs.sonarsource.com/sonarqube-cloud/managing-your-account/managing-tokens "mention").
2. In your Azure DevOps project, go to **Project Settings** > **Service connections**.
3. Select **New service connection** and then select **SonarQube Cloud** from the service connection list.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-ca2514a70aaa774931a1ba9722445c4abbb266f0%2Fsonarqube-cloud-azure-pipelines-service-connection.png?alt=media" alt="Search for &#x22;sonar&#x22; when adding a new service connection to your Azure DevOps pipeline." width="563"><figcaption></figcaption></figure></div>

4. Set the parameters:
   * In **Region (optional)** field, make sure **Global** is selected (default value).
   * In **SonarQube Cloud Token**, enter the token created in the first step.
   * In **Service Connection Name**, enter a memorable name (You will need this name when configuring your Azure build pipelines).
5. Select **Save** to save your connection.

### Enabling the pull request analysis in your build pipeline <a href="#enabling-pull-request-analysis" id="enabling-pull-request-analysis"></a>

The Azure DevOps extension running in your Azure pipeline can automatically detect branches or pull requests being built (you don't need to pass them as parameters to the scanner).

To enable the pull request analysis in your Azure pipeline of code stored on Azure DevOps, you must configure a pull request trigger on the target branch (main development branch) as explained on the [azure-devops](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/devops-platform-integration/azure-devops "mention") page. If your code is stored on GitHub or Bitbucket Cloud, open the expandable content below.

<details>

<summary>GitHub or Bitbucket Cloud</summary>

To configure a pull request trigger in your Azure build pipeline for code stored on GitHub or Bitbucket Cloud:

1. Select **Edit** to modify your build pipeline.
2. Go to the **Triggers** tab.
3. Select the correct repository under **Pull request validation**.
4. Select **Enable pull request validation**.
5. Set up the branch filters: Note that this is the **target** branch of the pull request. See the [Microsoft documentation](https://docs.microsoft.com/en-us/azure/devops/pipelines/build/triggers?view=azure-devops\&tabs=yaml#pr-triggers) for more details.
6. Select **Save** to update your pipeline.

</details>

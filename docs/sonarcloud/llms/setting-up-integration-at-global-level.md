# Source: https://docs.sonarsource.com/sonarqube-community-build/devops-platform-integration/azure-devops-integration/setting-up-integration-at-global-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/devops-platform-integration/azure-devops-integration/setting-up-integration-at-global-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/devops-platform-integration/azure-devops-integration/setting-up-integration-at-global-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/devops-platform-integration/azure-devops-integration/setting-up-integration-at-global-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/devops-platform-integration/azure-devops-integration/setting-up-integration-at-global-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/devops-platform-integration/azure-devops-integration/setting-up-integration-at-global-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/devops-platform-integration/azure-devops-integration/setting-up-integration-at-global-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/setting-up-integration-at-global-level.md

# Setting up Azure DevOps integration at global level

For the integration of an Azure DevOps Services organization or an Azure DevOps Server collection with SonarQube Server, you must:

* Create a configuration record in SonarQube Server. This record stores the Personal Access Token (PAT) of the technical account used by SonarQube Server to connect to Azure DevOps. This is necessary for importing Azure DevOps repositories and reporting the quality gate status.
* Install an Azure DevOps Extension for SonarQube Server on the CI/CD host to integrate with Azure Pipelines.

<figure><img src="broken-reference" alt="Installing Azure DevOps Extension for SonarQube Server on the CI/CD host"><figcaption></figcaption></figure>

For more information about the Azure DevOps integration solution, see [#related-pages](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/introduction#related-pages "mention").

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

See [#requirements](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/sonarqube-extension-for-azure-devops#requirements "mention") for Azure DevOps extension.

The SonarQube Server base URL must be properly set, otherwise, integration features will not work correctly. See [server-base-url](https://docs.sonarsource.com/sonarqube-server/instance-administration/server-base-url "mention").

### Preparing the integration <a href="#preparing" id="preparing"></a>

SonarQube Server uses an Azure DevOps user account to import Azure DevOps repositories to SonarQube Server and report the quality gate status to Azure DevOps. You must provide a [Personal Access Token](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=tfs-2017\&tabs=preview-page) (PAT) from this account.

{% hint style="warning" %}
Be aware of the following PAT failure points:

* Azure PATs require an expiration date. Check the [Microsoft documentation](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops\&tabs=Windows#create-a-pat) for details when creating your PAT.
* Azure requires that a user log in every 30 days, or it automatically stops a PAT; this action may cause your related pipeline to fail. Here is [an Azure Q\&A](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops\&tabs=Windows#q-why-did-my-pat-stop-working) on this topic.
  {% endhint %}

<details>

<summary>Creating a technical user account</summary>

We highly recommend that you use a dedicated technical user account in Azure DevOps to manage the integration with SonarQube.

* Do not set the technical user’s account with a **Stakeholder** access type. Use the **Basic** access type instead. (Users with the **Stakeholder** access type can have problems finding their repos when trying to Analyze projects.)
* We recommend that you add the account to the **Contributors** security group.

See the Azure documentation for more information [about access levels](https://learn.microsoft.com/en-us/azure/devops/organizations/security/access-levels?view=azure-devops).

</details>

<details>

<summary>Generating your Azure PAT</summary>

1\. Log in to Azure DevOps with the technical user account created before.

2\. Go to your Azure DevOps organization **User settings** > **Personal access tokens** and select **+ New token**.

<div align="left"><figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/Nu9Gz5WaaXMQ4KOtCq3S/azure-devops-create-new-personal-access-token-for-sonarqube.png" alt="The Personal access tokens page found in Azure DevOps." width="563"><figcaption></figcaption></figure></div>

3\. On the next page, under **Scopes**, make sure that you specify at least the scope **Code** > **Read & write**.

<div align="left"><figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/Ff1u1f1NNBl1ykDAhUan/azure-devops-scope-of-global-personal-access-token-for-sonarqube.png" alt="The Create a new personal access token modal found in Azure DevOps." width="375"><figcaption></figcaption></figure></div>

4\. Click **Create** to generate the token.

5\. When the personal access token is displayed, copy it (you will have to paste it to SonarQube’s configuration record as described below).

6\. If necessary, encrypt this token: see [encrypting-settings](https://docs.sonarsource.com/sonarqube-server/instance-administration/security/encrypting-settings "mention").

</details>

### Creating the global configuration record in SonarQube Server <a href="#creating-config-record" id="creating-config-record"></a>

You need the global System Administration permission to perform this procedure.

In SonarQube Server, a global configuration record stores the parameters necessary to connect to your Azure DevOps Server collection or Azure DevOps Services organization.

{% hint style="info" %}
Starting in [Enterprise edition](https://www.sonarsource.com/plans-and-pricing/enterprise/), you can set up the integration of SonarQube Server with multiple Azure DevOps platform instances. To do so, you create in SonarQube Server a configuration record for each instance.
{% endhint %}

To create the Azure DevOps configuration record in SonarQube:

1. Go to **Administration** > **Configuration** > **General Settings** > **DevOps Platform Integrations**.
2. Select the **Azure DevOps** tab.
3. Select the **Create configuration** button. The **Create a configuration** dialog opens.
4. Specify the settings as described below.

| Field                 | Description                                                                                                                                                                                                                                                                                         |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Configuration Name    | Enterprise and Data Center edition only. The name used to identify your Azure DevOps configuration at the project level. Use something succinct and easily recognizable.                                                                                                                            |
| Azure DevOps URL      | <p>• If you are using Azure DevOps Server: the full Azure DevOps collection URL. For example, <https://ado.your-company.com/DefaultCollection>.</p><p>• If you are using Azure DevOps Services: the full Azure DevOps organization URL. For example, <https://dev.azure.com/your_organization>.</p> |
| Personal Access Token | Personal access token generated in **Generating your Azure PAT** above (or its encrypted value).                                                                                                                                                                                                    |

### Installing the Azure DevOps Extension for SonarQube <a href="#installing-extension" id="installing-extension"></a>

See the [sonarqube-extension-for-azure-devops](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/sonarqube-extension-for-azure-devops "mention") page.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [azure-pipelines-integration-overview](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/azure-pipelines-integration-overview "mention")
* [creating-your-project](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/creating-your-project "mention")
* [setting-up-project-integration](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/setting-up-project-integration "mention")
* [adding-analysis-to-pipeline](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline "mention")
* [troubleshooting-analysis](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/troubleshooting-analysis "mention")

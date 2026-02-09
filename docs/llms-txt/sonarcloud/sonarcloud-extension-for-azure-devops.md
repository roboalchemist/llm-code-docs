# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarcloud-extension-for-azure-devops.md

# Azure DevOps Extension

{% hint style="info" %}
**4.0.1** *2025-12-10*

* <sup>Rotation of binary signing keys</sup>&#x20;

[**Download**](https://marketplace.visualstudio.com/items?itemName=SonarSource.sonarqube)  [Release notes](https://sonarsource.atlassian.net/issues?jql=project%20%3D%2010078%20AND%20fixversion%20%3D%20sq-8.0.1)
{% endhint %}

The [Azure DevOps extension for SonarQube Cloud](https://marketplace.visualstudio.com/items?itemName=SonarSource.sonarcloud) makes it easy to integrate analysis into your Azure build pipeline. The extension allows the analysis of all languages supported by SonarQube Cloud. For more information, see [azure-pipelines-integration-overview](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/azure-pipelines-integration-overview "mention") page.

This page explains how to install the extension. Once you have [setting-up-project](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/setting-up-project "mention"), you can add your SonarQube analyses to your [azure-pipelines](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines "mention").

### Installation requirements <a href="#requirements" id="requirements"></a>

<table><thead><tr><th width="185">Category</th><th>Requirement</th></tr></thead><tbody><tr><td>Azure DevOps</td><td><p>The extension will work with:</p><p>• Azure DevOps Services</p></td></tr><tr><td>Azure pipeline agents</td><td><p>The extension will work with all of the hosted agents (Windows, Linux, and macOS):</p><p>• If you are using Microsoft-hosted agents, there is nothing else to install.</p><p>• If you are self-hosting the agents, check that at least the minimal version of Java supported by SonarQube Cloud is installed. In addition, make sure the appropriate build tools are installed on the agent for the type of project you are analyzing. For example, .NET Framework v4.6.2+/NET Core 3.1+ if building using MSBuild, Maven for Java projects, etc.</p><p>The minimum agent version for @4 tasks of the Azure DevOps extension for SonarQube Cloud is 3.218.0.</p></td></tr><tr><td>Allowed websites</td><td><p>In order to download binaries and communicate with SonarQube Cloud, the following URLs should be allow listed:</p><p>• sonarcloud.io</p><p>• If using the Maven/Gradle mode or not using the default version of SonarScanner for .NET or CLI: the Sonar binaries site (binaries.sonarsource.com).</p></td></tr></tbody></table>

### Installing the extension <a href="#installing-extension" id="installing-extension"></a>

1. Sign in to your Azure DevOps Services organization with the dedicated technical account you created when [importing-azure-devops-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-azure-devops-organization "mention").
2. From the Visual Studio Marketplace, install the [Azure DevOps extension for SonarQube Cloud](https://marketplace.visualstudio.com/items?itemName=SonarSource.sonarcloud) by selecting the **Get it free** button.

### If upgrading from a previous version of the extension <a href="#upgrading-from-previous-version" id="upgrading-from-previous-version"></a>

#### Smooth migration <a href="#smooth-migration" id="smooth-migration"></a>

The latest version of the Azure DevOps extension for SonarQube embeds the latest version of SonarScanner for .NET and SonarScanner CLI. However, to allow a smooth migration, you can set up your Azure build pipeline to use a previous version of one of these scanners and thus, continue using a previous SonarQube tasks version until you’re ready to upgrade. See the [#specific-scanner-version](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/azure-pipelines/adding-analysis-to-build-pipeline/various-features#specific-scanner-version "mention") article.

{% hint style="info" %}
In that case, the Sonar binaries site (`binaries.sonarsource.com`) must be allow listed.
{% endhint %}

#### Prepare analysis configuration task: new scanner mode values <a href="#prepare-analysis-configuration-task-new-scanner-mode-values" id="prepare-analysis-configuration-task-new-scanner-mode-values"></a>

Allowable values for the `scannerMode` required property of the [#prepare-analysis-configuration](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/azure-pipelines/sonarqube-tasks#prepare-analysis-configuration "mention") have changed with the v3 extension. Please use the following in your @4 tasks:

* `dotnet` for the .NET mode
* `cli` for the CLI mode
* `other` for the Maven / Gradle mode

#### Deprecation notices <a href="#deprecation-notices" id="deprecation-notices"></a>

* Version @3 tasks were deprecated in v4.0 of the extension and will be dropped in a subsequent release.
* Version @1 and @2 tasks were dropped in v4.0 of the extension.

### Previous versions <a href="#previous-versions" id="previous-versions"></a>

As new scanner versions are released, previous requirements and/or deprecations will be listed here.

<details>

<summary><strong>Azure DevOps extension v3.x.x for SonarQube Cloud</strong> </summary>

* The minimum Azure pipeline agents version for @3 tasks of the Azure DevOps extension for SonarQube Cloud is 3.218.0.
* Version @2 tasks were deprecated in v3.0 and will be dropped in a subsequent release.

</details>

<details>

<summary><strong>Azure DevOps extension v2.2.x for SonarQube Cloud</strong> </summary>

Because the current versions of the [sonarscanner-for-dotnet](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-dotnet "mention") or [sonarscanner-cli](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-cli "mention") scanners are embedded, some additional setup may be required depending on your configuration.

* The SonarScanner for .NET has a new parameter for scanning multiple languages. The [#multi-language-analysis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/sonarscanner-for-dotnet/configuring#multi-language-analysis "mention") article has full details.
* If you want to specify the exact .NET or CLI scanner version, use the `msBuildVersion` and `cliVersion` properties. See the [#prepare-analysis-configuration](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/azure-pipelines/sonarqube-tasks#prepare-analysis-configuration "mention") article for details.

When specifying a particular scanner version, internet access is required by the pipelines calling the .NET or CLI scanners:

* Access to [github.com](http://github.com/) is required to download previous versions of the SonarScanner for .NET; see the [installing](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-dotnet/installing "mention") page. If you are allow listing [sonarcloud.io](http://sonarcloud.io/), GitHub and its HTTP redirect, `objects.githubusercontent.com`, should also be allow listed.
* Access to [binaries.sonarsource.com](http://binaries.sonarsource.com/) is required to download previous versions of the [sonarscanner-cli](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-cli "mention"). If you are allow-listing [sonarcloud.io](http://sonarcloud.io/), the Sonar binaries should also be allow listed.

For users running on-premise or using self-hosted agents, the minimum Azure pipeline agents version for SonarCloud v2 tasks is 3.218.0.

**in v2.0.1**

* Version @1 tasks were deprecated and will be dropped in a subsequent release.

</details>

<details>

<summary><strong>Azure DevOps extension for SonarQube Cloud v1.x.x</strong></summary>

From version 1.0 of the Azure DevOps extension, the extension was fully rewritten in Node.js which means that analyses can be triggered on Linux and macOS agents. The mono dependency was dropped in version 1.3; this is not possible when using previous versions of the extension.

For users running on-premise or using self-hosted agents, the minimum Azure pipeline agents version for SonarCloud v1 tasks is 2.114.0.

</details>

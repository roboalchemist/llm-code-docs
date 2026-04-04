# Source: https://docs.sonarsource.com/sonarqube-server/10.5/devops-platform-integration/github-integration/setting-up-your-projects.md

# Setting up your projects

For general information about project creation and import, see [creating-and-importing-projects](https://docs.sonarsource.com/sonarqube-server/10.5/project-administration/creating-and-importing-projects "mention").

### Reporting your quality gate status in GitHub <a href="#reporting-your-quality-gate-status-in-github" id="reporting-your-quality-gate-status-in-github"></a>

After [setting-up-global-integration](https://docs.sonarsource.com/sonarqube-server/10.5/devops-platform-integration/github-integration/setting-up-global-integration "mention"), SonarQube can report your quality gate status and analysis metrics directly to your GitHub branches and pull requests.

To do this, add a project from GitHub by doing one of the following:

* On the **Projects Overview** page, select **Add project** > **GitHub**, and follow the steps in SonarQube to analyze your project.
* Scan a project from a GitHub action. SonarQube will find a matching GitHub configuration.

SonarQube automatically sets the project settings required to show your quality gate in your branches and pull requests.

{% hint style="info" %}
To report your quality gate status in your branches and pull requests, a SonarQube analysis needs to be run on your code. You can find the additional parameters required for pull request analysis on the [pull-request-analysis](https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/pull-request-analysis "mention") page.
{% endhint %}

If you’re creating your projects manually or adding quality gate reporting to an existing project, see the following section.

#### Reporting your quality gate status in manually created or existing projects <a href="#reporting-your-quality-gate-status-in-manually-created-or-existing-projects" id="reporting-your-quality-gate-status-in-manually-created-or-existing-projects"></a>

SonarQube can also report your quality gate status to GitHub pull requests and branches for existing and manually created projects. After you’ve created and installed your GitHub App and updated your global DevOps Platform Integration settings as shown in the **Importing your GitHub repositories into SonarQube** section above, set the following project settings at **Project Settings** > **General Settings** > **DevOps Platform Integration**:

* **Configuration name**: The configuration name that corresponds to your GitHub instance.
* **Repository identifier**: The path of your repository URL.

#### Showing your analysis summary under the GitHub Conversation tab <a href="#showing-your-analysis-summary-under-the-github-conversation-tab" id="showing-your-analysis-summary-under-the-github-conversation-tab"></a>

Make sure that for your project, **Enable analysis summary** under the **GitHub Conversation** tab in **Project settings > General settings > Pull Request Decoration** is on (default value). If it’s the case, your pull request analysis will be shown under both the **Conversation** and **Checks** tabs in GitHub. When off, your pull request analysis summary is only shown under the **Checks** tab.

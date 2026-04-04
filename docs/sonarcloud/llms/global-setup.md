# Source: https://docs.sonarsource.com/sonarqube-community-build/devops-platform-integration/gitlab-integration/global-setup.md

# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/ci-integration/jenkins-integration/global-setup.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/ci-integration/jenkins-integration/global-setup.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/devops-platform-integration/gitlab-integration/global-setup.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/ci-integration/jenkins-integration/global-setup.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/devops-platform-integration/gitlab-integration/global-setup.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/ci-integration/jenkins-integration/global-setup.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/devops-platform-integration/gitlab-integration/global-setup.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/ci-integration/jenkins-integration/global-setup.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/devops-platform-integration/gitlab-integration/global-setup.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/ci-integration/jenkins-integration/global-setup.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/devops-platform-integration/gitlab-integration/global-setup.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/ci-integration/jenkins-integration/global-setup.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/devops-platform-integration/gitlab-integration/global-setup.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/ci-integration/jenkins-integration/global-setup.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/devops-platform-integration/gitlab-integration/global-setup.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/ci-integration/jenkins-integration/global-setup.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/devops-platform-integration/gitlab-integration/global-setup.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/ci-integration/jenkins-integration/global-setup.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/devops-platform-integration/gitlab-integration/global-setup.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/ci-integration/jenkins-integration/global-setup.md

# Source: https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/gitlab-integration/global-setup.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/ci-integration/jenkins-integration/global-setup.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/jenkins/global-setup.md

# Setting up Jenkins

The Jenkins extension for SonarQube facilitates a global integration with SonarQube Cloud. Using the Jenkins extension is not mandatory but allows a centralized installation and setup of the SonarScanner directly from Jenkins.

Proceed as follows:

1. Install the Jenkins extension.
2. Install the SonarScanner from Jenkins.
3. Set up the multi-branch features.

These steps are explained below.

### Installing the Jenkins extension <a href="#install-extension" id="install-extension"></a>

[Jenkins extension](https://plugins.jenkins.io/sonar/) version 2.11 or later is required.

Proceed as follows:

1. From the Jenkins Dashboard, navigate to **Manage Jenkins** > **Manage Plugins** and install the **SonarQube Scanner** plugin.
2. Back at the Jenkins Dashboard, navigate to **Credentials** > **System** from the left navigation.
3. Click the **Global credentials (unrestricted)** link in the **System** table.
4. Click **Add credentials** in the left navigation and add the following information:
   * **Kind**: Secret Text
   * **Scope**: Global
   * **Secret**: Generate a token at **User** > **My Account** > **Security** in SonarQube Cloud, and copy and paste it here.
5. Click **OK**.
6. From the Jenkins Dashboard, navigate to **Manage Jenkins** > **Configure System**.
7. From the **SonarQube Servers** section, click **Add SonarQube**. Add the following information:
   * **Name**: SonarQube Cloud
   * **Server URL**: <https://sonarcloud.io>
   * **Credentials**: Select the credentials created during step 4.
8. Click **Save**

### Installing the SonarScanner <a href="#install-scanner" id="install-scanner"></a>

From Jenkins, install and configure the SonarScanner instance(s). This step depends on the project type.

{% tabs %}
{% tab title="MAVEN OR GRADLE" %}

1. Log into Jenkins as an administrator and go to **Manage Jenkins** > **Configure System.**
2. Scroll to the **SonarQube servers** section and check **Enable injection of SonarQube server configuration as build environment variables**.
   {% endtab %}

{% tab title=".NET" %}
This step is mandatory if you want to trigger any of your analyses with the SonarScanner for .NET. You can define as many scanner instances as you wish. Then for each Jenkins job, you will be able to choose which launcher to use to run the analysis.

To install and configure the scanner instances:

1. Log into Jenkins as an administrator and go to **Manage Jenkins** > **Global Tool Configuration.**
2. Click on **Add SonarScanner for MSBuild.**
3. Add an installation of the latest available version. Check **Install automatically** to have the SonarScanner for .NET automatically provisioned on your Jenkins executors.\
   If you do not see any available version under Install from GitHub, first go to **Manage Jenkins** > **Manage Plugins** > **Advanced** and click on **Check now.**

{% hint style="info" %}
In version 5.0 of the SonarScanner, we changed the name of the *SonarScanner for MSBuild* to *SonarScanner for .NET*.

The documentation is updated with the new name and we will call the scanner *SonarScanner for .NET* moving forward.
{% endhint %}
{% endtab %}

{% tab title="OTHER" %}
This step is mandatory if you want to trigger any of your analyses with the SonarScanner CLI. You can define as many scanner instances as you wish. Then, for each Jenkins job, you will be able to choose which launcher to use to run the analysis.

To install and configure the scanner instances:

1. Log into Jenkins as an administrator and go to **Manage Jenkins** > **Global Tool Configuration.**
2. Scroll down to the SonarScanner configuration section and select **Add SonarScanner**. It is based on the typical Jenkins tool auto-installation. You can either choose to point to an already installed version of the SonarScanner CLI (uncheck **Install automatically**) or tell Jenkins to grab the installer from a remote location (check **Install automatically**).\
   If you don’t see a drop-down list with all available SonarScanner CLI versions but instead see an empty text field, this is because Jenkins still hasn’t downloaded the required update center file (the default period is one day). You may force this refresh by selecting **Check Now** in **Manage Plugins** > **Advanced tab**.
   {% endtab %}
   {% endtabs %}

### Setting up the multi-branch features <a href="#branch-features-settings" id="branch-features-settings"></a>

To analyze Jenkins Multibranch Pipeline jobs, you must install, on your CI host, the Branch Source plugin for Jenkins corresponding to your DevOps platform.

{% tabs %}
{% tab title="GITHUB" %}
[GitHub Branch Source plugin](https://plugins.jenkins.io/github-branch-source/) version 2.7.1 or later is required

1. From the Jenkins Dashboard, navigate to **Manage Jenkins** > **Manage Plugins** and install the **GitHub Branch Source** plugin.
2. From the Jenkins Dashboard, navigate to **Manage Jenkins** > **Configure System**.
3. From the **GitHub** or **GitHub Enterprise Servers** section, add your GitHub server.
4. Select **Save**.
   {% endtab %}

{% tab title="BITBUCKET SERVER OR DATA CENTER" %}
[Bitbucket Branch Source plugin](https://plugins.jenkins.io/cloudbees-bitbucket-branch-source/) version 2.7 or later is required

From the Jenkins Dashboard, navigate to **Manage Jenkins** > **Manage Plugins** and install the **Bitbucket Branch Source** plugin. Then configure the following:

1. From the Jenkins Dashboard, navigate to **Manage Jenkins** > **Configure System**.
2. From the **Bitbucket Endpoints** section, open the **Add** drop-down menu and select **Bitbucket Server**. Add the following information:
   * **Name**: Give a unique name to your Bitbucket Server or Data Center instance.
   * **Server URL**: Your Bitbucket Server or Data Center instance URL.
3. Select **Save**.
   {% endtab %}

{% tab title="BITBUCKET CLOUD" %}
[Bitbucket Branch Source plugin](https://plugins.jenkins.io/cloudbees-bitbucket-branch-source/) version 2.7 or later is required

From the Jenkins Dashboard, navigate to **Manage Jenkins** > **Manage Plugins** and install the **Bitbucket Branch Source** plugin.
{% endtab %}

{% tab title="GITLAB" %}
[GitLab Branch Source plugin](https://plugins.jenkins.io/gitlab-branch-source/) version 1.5.3 or later is required

1. From the Jenkins Dashboard, navigate to **Manage Jenkins** > **Manage Plugins** and install the **GitLab Branch Source** plugin.
2. From the Jenkins Dashboard, navigate to **Manage Jenkins** > **Configure System**.
3. From the **GitLab** section, add your GitLab server. Make sure to select the **Manage Web Hooks** checkbox.
4. Select **Save**.
   {% endtab %}
   {% endtabs %}

### Other settings <a href="#other-settings" id="other-settings"></a>

To set up an automatic interruption of the pipeline in case the quality gate fails, configure your [webhooks](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/webhooks "mention") at the global level when used in pipeline jobs. Interrupting your pipeline (with a failed quality gate) is only available in Team plans. See the [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") page for more details.

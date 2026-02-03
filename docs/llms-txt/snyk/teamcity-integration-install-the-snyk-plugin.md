# Source: https://docs.snyk.io/developer-tools/snyk-ci-cd-integrations/teamcity-jetbrains-integration-using-the-snyk-security-plugin/teamcity-integration-install-the-snyk-plugin.md

# TeamCity integration: install the Snyk plugin

Follow these steps to install or upgrade the Snyk Security plugin. When the installation is complete, you can add a Snyk step to your Projects.

Before you begin, sign up for a Snyk account.

1. Log in to your TeamCity instance to install the Snyk Security plugin.
2. Configure the **Plugins list** to **Periodically check for plugin updates**, to ensure regular automatic upgrades in the background.
3. Navigate to the [JetBrains Plugins Repository](https://plugins.jetbrains.com/plugin/12227-snyk-security), search for Snyk, and, from the **Get** dropdown list, select the plugin for your TeamCity installation.
4. In response to the prompt, click **Install**.
5. When the installation ends, and the **Administration Plugins List** loads with a notification that the plugin has been uploaded, ensure the plugin is enabled.

![Install plugin from the JetBrains Plugins Repository](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-62e4090cfaecf64e1b4acab68d627dea3e55b7f6%2Fuuid-fe65f4bc-9578-016c-00dd-6ddb97d2ead7-en.png?alt=media\&token=2428a0b1-218f-4787-99f0-92b3b7f620d3)

To configure the integration, see [TeamCity configuration parameters](https://docs.snyk.io/developer-tools/snyk-ci-cd-integrations/teamcity-jetbrains-integration-using-the-snyk-security-plugin/teamcity-configuration-parameters). For information on how to configure your build with a Snyk step, see [Team City integration: use Snyk in your build](https://docs.snyk.io/developer-tools/snyk-ci-cd-integrations/teamcity-jetbrains-integration-using-the-snyk-security-plugin/teamcity-integration-use-snyk-in-your-build).

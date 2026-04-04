# Source: https://docs.sonarsource.com/sonarqube-community-build/user-guide/issues/fixing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/user-guide/issues/fixing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/user-guide/issues/fixing.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/user-guide/issues/fixing.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/user-guide/issues/fixing.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/user-guide/issues/fixing.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/issues/fixing.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/user-guide/issues/fixing.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/user-guide/issues/fixing.md

# Source: https://docs.sonarsource.com/sonarqube-server/user-guide/issues/fixing.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/fixing.md

# Fixing issues

Depending on the issue, you may get fix suggestions:

* In the **How can I fix it?** tab of the issue's detail view. See [reviewing](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/reviewing "mention") for more details.
* Available in the Team plan, generated through AI: see [#getting-ai-generated-fix-suggestions](#getting-ai-generated-fix-suggestions "mention") below.

### Opening issues in your IDE <a href="#opening-in-ide" id="opening-in-ide"></a>

To speed up the time it takes to find and fix the issue, use connected mode to connect SonarQube Cloud with [connected-mode](https://docs.sonarsource.com/sonarqube-cloud/improving/connected-mode "mention") and use the **Open in IDE** feature.

{% hint style="info" %}
If you’ve already fixed the issue in your code, SonarQube for IDE will not be able to find it in the IDE; only matching code will be highlighted.&#x20;

Keep in mind that the revision or branch analyzed by SonarQube Cloud may not be the same as what you have opened in the IDE. When setting up connected mode, SonarQube for IDE considers the branch currently checked out in the IDE and tries to synchronize it with the most appropriate branch from the server. This is called branch matching in SonarQube for IDE.
{% endhint %}

To open an issue in your IDE, it’s easier if you are already running in connected mode:

1. Follow the [retrieving](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/retrieving "mention") instructions and open an issue's detail view.
2. Select the **Open in IDE** button.

Check the individual instructions for your IDE for more details or to troubleshoot failed connections:

* [Opening issues in SonarQube for VS Code](https://docs.sonarsource.com/sonarqube-for-vs-code/using/investigating-issues#opening-issues-in-the-ide)
* [Opening issues in SonarQube for IntelliJ](https://docs.sonarsource.com/sonarqube-for-intellij/using/investigating-issues#opening-issues-in-the-ide)
* [Opening issues in SonarQube for Visual Studio](https://docs.sonarsource.com/sonarqube-for-visual-studio/using/investigating-issues#opening-issues-in-the-ide)
* [Opening issues in SonarQube for Eclipse](https://docs.sonarsource.com/sonarqube-for-eclipse/using/investigating-issues#opening-issues-in-the-ide)

{% hint style="warning" %}
**Open in IDE** is not supported in Safari. Safari has strict security policies regarding custom protocol links which are required to open files directly in your IDE. When using SonraQube (Server, Cloud) or SonarQube Community Build, please use Chrome or Firefox for this functionality.
{% endhint %}

### Getting AI-generated fix suggestions <a href="#getting-ai-generated-fix-suggestions" id="getting-ai-generated-fix-suggestions"></a>

*AI features are only available in SonarQube Cloud Team and Enterprise plans*. See the [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") page for more detail&#x73;*.*

Sonar's AI CodeFix is available to provide AI-generated fix suggestions for a select set of issues. See the [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") and [rules-for-ai-codefix](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/rules-for-ai-codefix "mention") pages for more details. If needed, the [enable-ai-codefix](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/ai-features/enable-ai-codefix "mention") page has more information for SonarQube Cloud administrators to activate the feature for your organization.

The suggestions are generated for select rules and languages using <code class="expression">space.vars.SQC\_Supported\_LLM\_version</code>.

To generate a fix suggestion in your IDE:

* Simply open your project in SonarQube for SonarQube for VS Code or SonarQube for IntelliJ using connected mode with SonarQube Cloud.
  * In your IDE, select an issue marked with the ![$ai-icon-sparkle](https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-975a17de7ce8ae3b164dd9f9db9c791adb294bbb%2F4be9087a2b059c269f15df202838af7a74e71a96.svg?alt=media) icon, open the **Rule description** > ![$ai-icon-sparkle](https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-975a17de7ce8ae3b164dd9f9db9c791adb294bbb%2F4be9087a2b059c269f15df202838af7a74e71a96.svg?alt=media)**AI CodeFix** tab, and select ![$ai-icon-sparkle](https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-975a17de7ce8ae3b164dd9f9db9c791adb294bbb%2F4be9087a2b059c269f15df202838af7a74e71a96.svg?alt=media)**Generate Fix**. A fix will be generated in the code editor and you’ll have a chance to **Apply** or **Decline** the suggestion.
    * See the VS Code page for [AI CodeFix in your IDE](https://docs.sonarsource.com/sonarqube-for-vs-code/ai-capabilities/ai-codefix)&#x20;
    * See the IntelliJ page for [AI CodeFix in your IDE](https://docs.sonarsource.com/sonarqube-for-intellij/ai-capabilities/ai-codefix)

To generate a fix suggestion in SonarQube Cloud:

* Follow the [retrieving](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/retrieving "mention") instructions in SonarQube Cloud and open an issue's detail view. If an AI CodeFix is an option for that particular issue, you will see the ![$ai-icon-sparkle](https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-975a17de7ce8ae3b164dd9f9db9c791adb294bbb%2F4be9087a2b059c269f15df202838af7a74e71a96.svg?alt=media)**Generate AI Fix** button.
* From either the **Where is the Issue** or the **AI CodeFix** tabs, select the **Generate Fix** button.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-ed411d54da4a12bad88727f510b7433599e86e21%2Fb53347349ef7798278cd15d552fe0033e7f03be0.png?alt=media" alt="If an AI CodeFix is available for your issue, SonarQube Cloud will offer a Generate AI Fix button to select."><figcaption></figcaption></figure></div>

An AI CodeFix will be generated, and you’ll see a diff view in the **AI CodeFix** tab. Simply copy and paste the generated fix into your IDE; If you’re using SonarQube for IDE and have connected mode set up for [connected-mode](https://docs.sonarsource.com/sonarqube-cloud/improving/connected-mode "mention"), feel free to use the **Open in IDE** feature to streamline the process.

* If you are running SonarQube for Visual Studio, selecting **View fix in IDE** will offer you a diff view in the IDE which provides an opportunity to accept or reject the suggestion before committing the change.

An AI Code Assurance badge is available to any SonarQube Cloud plan to mark your AI projects as reviewed by SonarQube Cloud. Any user with project access can use the badge. For more detailed instructions, see the [#marking-a-project-as-containing-ai-generated-code](https://docs.sonarsource.com/sonarqube-cloud/ai-capabilities/ai-code-assurance#marking-a-project-as-containing-ai-generated-code "mention") article on the *AI settings* page.

Note that for some issues, an AI CodeFix suggestion is not available. To learn more about which rules are eligible for AI CodeFix, please see the list of [#ai-codefix-rules](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/rules-for-ai-codefix#ai-codefix-rules "mention").

#### Usage limits <a href="#limits" id="limits"></a>

Limits are placed on the AI CodeFix feature to manage abuse. Developers will be notified directly when the monthly allocation is reached for your organization. If the instance is blocked due to reaching the allowance, users attempting to generate a fix will see an error message. Usage quotas are reset on the first day of each month.

### SonarQube Remediation agent

{% hint style="success" %}
The SonarQube Remediation Agent is a [Beta](https://docs.sonarsource.com/sonarqube-cloud/appendices/product-release-lifecycle#beta) feature available with Enterprise plan accounts. It is free during the beta phase and will be a paid feature when it moves to [General Availability](https://docs.sonarsource.com/sonarqube-cloud/appendices/product-release-lifecycle#general-availability). To learn more about the terms & conditions, please see our legal page about features in [Early Access](https://www.sonarsource.com/legal/early-access/).

If your SonarQube Cloud organization is not on an Enterprise plan, please see the [getting-started-with-enterprise](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise "mention") pages to get the process started.
{% endhint %}

The SonarQube Remediation Agent runs an independent review and analysis to help you fix reliability and maintainability issues found in your latest code. It focuses on new issues discovered in your latest GitHub pull request (PR). These issues, picked up by the agent, would otherwise break the new code conditions of your quality gate and block the merge of your PR.&#x20;

The agent uses <code class="expression">space.vars.SQC\_Remediation\_agent\_LLM</code> to generate fix suggestions in the background and checks that the new code does not introduce new issues before offering the suggestion.

To enable and install the agent, see the [sonarqube-remediation-agent](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/ai-features/sonarqube-remediation-agent "mention") page. To understand the agent's behavior and learn how to engage with the agent in your pull request, see the [agents-in-your-github-pull-request](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/with-ai-features/agents-in-your-github-pull-request "mention") page.

### Creating Jira Cloud work items from SonarQube issues

You can create a Jira Cloud work item from a single or multiple SonarQube issues. See [jira-integration](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/jira-integration "mention") for more information.

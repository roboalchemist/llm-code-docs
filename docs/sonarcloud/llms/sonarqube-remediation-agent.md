# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/ai-features/sonarqube-remediation-agent.md

# SonarQube Remediation Agent

{% hint style="success" %}
The SonarQube Remediation Agent is a [Beta](https://docs.sonarsource.com/sonarqube-cloud/appendices/product-release-lifecycle#beta) feature available with Enterprise plan accounts. It is free during the beta phase and will be a paid feature when it moves to [General Availability](https://docs.sonarsource.com/sonarqube-cloud/appendices/product-release-lifecycle#general-availability). To learn more about the terms & conditions, please see our legal page about features in [Early Access](https://www.sonarsource.com/legal/early-access/).

If your SonarQube Cloud organization is not on an Enterprise plan, please see the [getting-started-with-enterprise](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise "mention") pages to get the process started.
{% endhint %}

The SonarQube Remediation Agent runs an independent review and analysis to help you fix reliability and maintainability issues found in your latest code. It focuses on new issues discovered in your latest GitHub pull request (PR). These issues, picked up by the agent, would otherwise break the new code conditions of your quality gate and block the merge of your PR.&#x20;

The agent uses <code class="expression">space.vars.SQC\_Remediation\_agent\_LLM</code> to generate fix suggestions in the background and checks that the new code does not introduce new issues before offering the suggestion.

The SonarQube Remediation Agent is only triggered by a [pull-request-analysis](https://docs.sonarsource.com/sonarqube-cloud/improving/pull-request-analysis "mention") and does not engage with your branch analysis. See the [#quality-gate-and-metrics](https://docs.sonarsource.com/sonarqube-cloud/improving/pull-request-analysis#quality-gate-and-metrics "mention") article to learn more about how the quality gate is computed on during a PR analysis.

### Requirements and limitations

The [SonarQube Remediation Agent](https://github.com/apps/sonarqube-agent), when enabled, runs in your PR on private projects in GitHub.

You must have either [automatic-analysis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/automatic-analysis "mention") enabled or be running a [#ci-based-analysis](https://docs.sonarsource.com/sonarqube-cloud/getting-started/github#ci-based-analysis "mention") on your GitHub repository.

The agent can suggest code fixes on your pull request for [#maintainability](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/software-qualities#maintainability "mention"), [#reliability](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/software-qualities#reliability "mention"), and a select set of [#security](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/software-qualities#security "mention") issues found in Java, JavaScript/TypeScript, and Python code; the agent can also suggest fixes for [secrets](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/secrets "mention") detected in your code.

For a full list of supported rules, open the expandable below with your selected language:

<details>

<summary>Java</summary>

#### Supported Java rules

* see the languages page about [java](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/java "mention") for general information about rule support
* [Java maintainability rules](https://rules.sonarsource.com/java/impact/maintainability/)
* [Java reliability rules](https://rules.sonarsource.com/java/impact/reliability/)

#### **Supported Java security rules**

Go to the [Sonar Rules website](https://rules.sonarsource.com/) to search for more information about your rule.

* select any rule at <https://rules.sonarsource.com/java/>
* replace the RSPEC number in the rule’s URL with the relevant rule number listed below.

For example, to read about rule `java:S2053`, go to <https://rules.sonarsource.com/java/RSPEC-2053/>

java:S2053

java:S2658

java:S4347

java:S4426

java:S4433

java:S5445

java:S5547

#### **Blocked Java rules**

The SonarQube Remediation Agent does not have access to a limited number of rules because they are too complex for an LLM to solve.&#x20;

java:S1135

java:S1134

java:S1144

java:S3776

java:S1228

</details>

<details>

<summary>JavaScript</summary>

#### Supported JavaScript rules

* see the languages page about [javascript-typescript-css](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/javascript-typescript-css "mention") for general information about rule support
* [JavaScript maintainability rules](https://rules.sonarsource.com/javascript/impact/maintainability/)
* [JavaScript reliability rules](https://rules.sonarsource.com/javascript/impact/reliability/)

#### **Supported JavaScript security rules**

Go to the [Sonar Rules website](https://rules.sonarsource.com/) to search for more information about your rule.

* select any rule at <https://rules.sonarsource.com/javascript/>
* replace the RSPEC number in the rule’s URL with the relevant rule number listed below.

For example, to read about rule `javascript:S1442`, go to <https://rules.sonarsource.com/javascript/RSPEC-1442/>

javascript:S1442

javascript:S2598

javascript:S2755

javascript:S4423

javascript:S4426

javascript:S4830

javascript:S5527

javascript:S5542

javascript:S5547

javascript:S5659

javascript:S6317

javascript:S6321

#### **Blocked JavaScript rules**

The SonarQube Remediation Agent does not have access to a limited number of rules because they are too complex for an LLM to solve.&#x20;

javascript:S1135

javascript:S1134

javascript:S1144

javascript:S3776

</details>

<details>

<summary>Python</summary>

#### Supported Python rules

* see the languages page about [python](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/python "mention") for general information about rule support
* [Python maintainability rules](https://rules.sonarsource.com/python/impact/maintainability/)
* [Python reliability rules](https://rules.sonarsource.com/python/impact/reliability/)

#### **Supported Python security rules**

Go to the [Sonar Rules website](https://rules.sonarsource.com/) to search for more information about your rule.

* select any rule at <https://rules.sonarsource.com/python/>
* replace the RSPEC number in the rule’s URL with the relevant rule number listed below.

For example, to read about rule `python:S2053`, go to <https://rules.sonarsource.com/python/RSPEC-2053/>

python:S2053

python:S2115

python:S2755

python:S3329

python:S4423

python:S4426

python:S4830

python:S5344

python:S5439

python:S5445

python:S5527

python:S5542

python:S5547

python:S5659

python:S6321

python:S6437

python:S6727

python:S6779

python:S6781

python:S6785

python:S6786

#### **Blocked Python rules**

The SonarQube Remediation Agent does not have access to a limited number of rules because they are too complex for an LLM to solve.&#x20;

python:S1135

python:S1134

python:S1144

python:S3776

</details>

<details>

<summary>TypeScript</summary>

#### Supported TypeScript rules

* see the languages page about [javascript-typescript-css](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/javascript-typescript-css "mention") for general information about rule support
* [TypeScript maintainability rules](https://rules.sonarsource.com/typescript/impact/maintainability/)
* [TypeScript reliability rules](https://rules.sonarsource.com/typescript/impact/reliability/)

Go to the [Sonar Rules website](https://rules.sonarsource.com/) to search for more information about your rule.

* select any rule at <https://rules.sonarsource.com/typescript/>
* replace the RSPEC number in the rule’s URL with the relevant rule number listed below.

For example, to read about rule `typescript:S2598`, go to <https://rules.sonarsource.com/typescript/RSPEC-2598/>

typescript:S2598

typescript:S2755

typescript:S4426

typescript:S5542

typescript:S6321

#### **Blocked TypeScript rules**

The SonarQube Remediation Agent does not have access to a limited number of rules because they are too complex for an LLM to solve.&#x20;

typescript:S1135

typescript:S1134

typescript:S1144

typescript:S3776

</details>

<details>

<summary>Secrets</summary>

#### **Supported Secrets rules**

* see the page about [secrets](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/secrets "mention") detection for general information about rule support
* [Secrets rules](https://rules.sonarsource.com/secrets/)

</details>

Limits are placed on the agent’s activity to avoid noise in the comment history of your GitHub pull request. Currently, the limit is 50 issues; if more than 50 issues are introduced in your PR, the agent will not be triggered.

{% hint style="warning" %}
The SonarQube Remediation Agent will only work with issues found in one of the supported language types.

Once enabled in SonarQube Cloud, any of your GitHub repositories can add the SonarQube Remediation Agent as a GitHub App, irregardless of the language type.

Although SonarQube Cloud may find issues in a repository that contains an unsupported language for example, in C++, the agent won't be triggered in a pull request because C++ is not a supported language type.
{% endhint %}

### Subscription

The SonarQube Remediation Agent is a [#beta](https://docs.sonarsource.com/sonarqube-cloud/appendices/product-release-lifecycle#beta "mention") feature available with Enterprise plan accounts. It is free during the beta phase and will be a paid feature when it moves to [#general-availability](https://docs.sonarsource.com/sonarqube-cloud/appendices/product-release-lifecycle#general-availability "mention").

If your SonarQube Cloud organization is not on an Enterprise plan, please see the [getting-started-with-enterprise](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise "mention") pages to get the process started. To learn more about the terms & conditions for Beta, please see our legal page about features in [Early Access](https://www.sonarsource.com/legal/early-access/).

### Sharing your code with Sonar <a href="#sharing-your-code-with-sonar" id="sharing-your-code-with-sonar"></a>

If you use the SonarQube Remediation Agent, the affected code snippet will be sent by the agent to an LLM to generate a fix suggestion. These suggestions are verified by Sonar before being offered as an issue fix. Service agreements with Sonar’s LLMs prevent your code from being used to train those models and it is not stored by the LLM provider nor by any third party.&#x20;

For details about terms and conditions, please refer to the [Early Access terms](https://www.sonarsource.com/legal/early-access/) in our [Legal Documentation](https://www.sonarsource.com/legal/).

### Enable your agent

A SonarQube Cloud organization admin and an administrator for your GitHub account are needed to set up Sonar's AI Agent for automated developer workflows:

1. If you haven't already, follow the instructions about [#activating-automatic-analysis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/automatic-analysis#activating-automatic-analysis "mention") or enabling a [#ci-based-analysis](https://docs.sonarsource.com/sonarqube-cloud/getting-started/github#ci-based-analysis "mention") on your project hosted in a GitHub repository.
2. Navigate to *Your SonarQube Cloud Organization* > **Administration** > **AI capabilities** > **AI agent**.
3. A GitHub administrator needs to install the [SonarQube Agent GitHub app](https://github.com/apps/sonarqube-agent). Under **Install app**, select **GitHub**. The administrator will be prompted to install the app on the GitHub organization already linked to your SonarQube Cloud organization. If installed, the agent will be granted:
   * Read and write access to code and pull requests,
   * And Read-only access to issues and metadata.
4. Choose either **All repositories** or **Only select repositories** to control which repositories the AI agent can access. Once you've made your selection, select **Install & Authorize** to finish the setup. Please note that the installation may take a few seconds to complete.
5. After all the steps are successfully finished, the **Enable agent** > **Remediation agent** option will be automatically selected in SonarQube Cloud, and you will be able to commit the agent’s suggestions directly from your PRs.

### Manage agent access

The SonarQube Remediation agent only has access to the repositories you define. To change repository access, a GitHub administrator who is also a SonarCloud Administrator can navigate in SonarQube Cloud to *Your Organization* > **Administration** > **AI capabilities** > **AI agent**. Under Install app, select **Manage Permissions** which takes you to your GitHub Apps page.

Alternatively, a GitHub administrator can navigate in GitHub to *Your GitHub Organization* > **Settings** > **Third-party Access** > **GitHub Apps**. Under **Installed GitHub Apps** > **SonarQube Agent**, select **Configure**.

* In GitHub, under **SonarQube Agent** > **Repository access**, add or remove your repositories from the list. When finished, select **Save** to confirm your selection.

#### Disable or suspend agent access

It is possible to disable the SonarQube Remediation agent in SonarQube Cloud or in GitHub, if you prefer.

A SonarCloud Administrator can navigate to *Your Organization* > **Administration** > **AI capabilities** > **AI agent** > **Enable agent** and unselect **Remediation agent**. Once **Save** is selected, the agent will no longer be triggered in GitHub.

To suspend or uninstall SonarQube Agent completely, navigate in GitHub to *Your GitHub Organization* > **Third-party Access** > **GitHub Apps** > **SonarQube Agent** > **Danger zone** and select **Suspend** or **Uninstall**.

* **Suspend** will block the agent’s access to your repositories. Choosing this option is the easiest way to restart the agent, when you're ready.
* If you select and confirm **Uninstall**, the SonarQube Agent will be removed from all of your repositories and from your SonarQube Cloud Organization. The agent's activity will be remain in your PR history but if you want to use the agent again, you must return to the beginning to [#enable-your-agent](#enable-your-agent "mention").

### Agent behavior

The SonarQube Remediation agent's behavior is described on the [agents-in-your-github-pull-request](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/with-ai-features/agents-in-your-github-pull-request "mention") page, along side other topics about [issues](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues "mention") in SonarQube Cloud.

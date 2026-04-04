# Source: https://docs.sonarsource.com/sonarqube-cloud/ai-capabilities/ai-agents.md

# SonarQube Remediation Agent

### The SonarQube Remediation Agent

{% hint style="success" %}
The SonarQube Remediation Agent is a [Beta](https://docs.sonarsource.com/sonarqube-cloud/appendices/product-release-lifecycle#beta) feature available with Enterprise plan accounts. It is free during the beta phase and will be a paid feature when it moves to [General Availability](https://docs.sonarsource.com/sonarqube-cloud/appendices/product-release-lifecycle#general-availability). To learn more about the terms & conditions, please see our legal page about features in [Early Access](https://www.sonarsource.com/legal/early-access/).

If your SonarQube Cloud organization is not on an Enterprise plan, please see the [getting-started-with-enterprise](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise "mention") pages to get the process started.
{% endhint %}

The SonarQube Remediation Agent runs an independent review and analysis to help you fix reliability and maintainability issues found in your latest code. It focuses on new issues discovered in your latest GitHub pull request (PR). These issues, picked up by the agent, would otherwise break the new code conditions of your quality gate and block the merge of your PR.&#x20;

The agent uses <code class="expression">space.vars.SQC\_Remediation\_agent\_LLM</code> to generate fix suggestions in the background and checks that the new code does not introduce new issues before offering the suggestion.

The agent reviews issues found during your pull request analysis, proposes fixes, and adds a commit to the PR when the fix suggestion is accepted. Users maintain full control of the agent at all times from enabling it on a per-project basis, to reviewing and approving code suggestions on an issue-by-issue basis.

It works with your most common languages (Java, JavaScript/TypeScript, and Python) by providing feedback on maintainability, reliability, and select security issues. In addition, it also offers fix suggestions for [secrets](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/secrets "mention"); see the [#requirements-and-limitations](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/ai-features/sonarqube-remediation-agent#requirements-and-limitations "mention") for complete details.

To enable and install the agent, see the [sonarqube-remediation-agent](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/ai-features/sonarqube-remediation-agent "mention") page. To understand the agent's behavior and learn how to engage with the agent in your pull request, see the [agents-in-your-github-pull-request](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/with-ai-features/agents-in-your-github-pull-request "mention") page.

### Sharing your code with Sonar <a href="#sharing-your-code-with-sonar" id="sharing-your-code-with-sonar"></a>

If you use the SonarQube Remediation Agent, the affected code snippet will be sent by the agent to an LLM to generate a fix suggestion. These suggestions are verified by Sonar before being offered as an issue fix. Service agreements with Sonar’s LLMs prevent your code from being used to train those models and it is not stored by the LLM provider nor by any third party.&#x20;

For details about terms and conditions, please refer to the [Early Access terms](https://www.sonarsource.com/legal/early-access/) in our [Legal Documentation](https://www.sonarsource.com/legal/).

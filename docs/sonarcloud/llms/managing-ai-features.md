# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/system-functions/managing-ai-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/system-functions/managing-ai-features.md

# Managing AI features

Sonar’s AI CodeFix uses a large language model (LLM) to automatically generate AI-driven code fixes for the issues discovered by SonarQube Server. The process is simple. When you request a fix, the affected code and issue description are sent to an LLM. AI CodeFix then proposes an edit that resolves the problem without changing the code’s functionality.

AI CodeFix currently uses <code class="expression">space.vars.SQS\_20252\_Supported\_LLM\_version</code> your own Azure OpenAI LLM, to suggest fixes for a select set of rules in Java, JavaScript, TypeScript, Python, C#, and C++. To learn more about which rules are eligible for AI CodeFix, please see the list of [#ai-codefix-rules](https://docs.sonarsource.com/sonarqube-server/2025.2/user-guide/rules/rules-for-ai-codefix#ai-codefix-rules "mention").

### Enabling AI-generated fix suggestions <a href="#enabling-ai-generated-fix-suggestions" id="enabling-ai-generated-fix-suggestions"></a>

As an Instance Admin, you can enable or disable AI-generated fix suggestions on your projects. To enable AI CodeFix:

1. Go to **Administration** > **Configuration** > **General Settings** > **Early Access** > **Enable AI-Generated fix suggestions** and select **Enable AI CodeFix**.
2. Select your **Provider**:
   * The default option is Sonar’s **OpenAI** which uses <code class="expression">space.vars.SQS\_20252\_Recommended\_LLM\_version</code>.
   * To choose your own **Azure OpenAI** LLM:
     1. Select **Self-hosted Bring Your Own Model**.
     2. Provide your Azure OpenAI **Endpoint**. The endpoint URL should include the `deployment-id` and `api-version` parameters.\
        Here is an example: `https://<YOUR-ENDPOINT>/openai/deployments/<YOUR-DEPLOYMENT-ID>/completions?api-version=<YOUR-API-VERSION>`
     3. Provide your Azure OpenAI **API Key**. For information about using Azure AI models, see the [Azure OpenAI Service documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/).
3. Once AI CodeFix is enabled, choose either **All projects** or **Only selected projects:**

When choosing **Only selected projects**, add projects individually from the list to activate the feature. New projects will not be added automatically.

{% hint style="warning" %}
Sonar recommends using <code class="expression">space.vars.SQS\_20252\_Recommended\_LLM\_version</code> as your Azure OpenAI Service model because it produces the best results. Using other models may produce unexpected fix suggestions that have undesirable effects.

For more information on your choices, see the [Azure documentation on service models](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models?tabs=global-standard%2Cstandard-chat-completions).
{% endhint %}

{% hint style="info" %}
You’ll need a connection to the internet to access SonarQube Server’s AI CodeFix service.

The service is provided via api.sonarqube.io and has these static IP addresses:

* 99.83.135.55 (CIDR: 99.83.135.55/32)
* 15.197.164.24 (CIDR: 15.197.164.24/32)
  {% endhint %}

Once enabled, developers can get AI-generated fix suggestions from the **Issues** page in their projects. See [fixing](https://docs.sonarsource.com/sonarqube-server/2025.2/user-guide/issues/fixing "mention") for more details.

#### Disabling AI CodeFix <a href="#disabling-ai-codefix" id="disabling-ai-codefix"></a>

To disable AI CodeFix completely in SonarQube Server and hide the feature from all users, including Instance Admins, set `sonar.ai.codefix.hidden=true` in your sonar.properties file.

### Usage limits <a href="#limits" id="limits"></a>

Limits are placed on the AI CodeFix feature to manage abuse. Developers will be notified directly when the monthly allocation is reached for your organization. If the instance is blocked due to reaching the allowance, users attempting to generate a fix will see an error message. Usage quotas are reset on the first day of each month.

SonarQube Server instances that are using its own self-hosted LLM are not subject to these limits.

### AI Code Assurance <a href="#ai-code-assurance" id="ai-code-assurance"></a>

Sonar recognizes that AI-generated code should be monitored with additional quality standards and offers administrators a series of tools described on the [ai-standards](https://docs.sonarsource.com/sonarqube-server/2025.2/ai-capabilities/ai-standards "mention") page.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [overview](https://docs.sonarsource.com/sonarqube-server/2025.2/ai-capabilities/overview "mention")
* [#ai-codefix-rules](https://docs.sonarsource.com/sonarqube-server/2025.2/user-guide/rules/rules-for-ai-codefix#ai-codefix-rules "mention")
* see [#getting-ai-generated-fix-suggestions](https://docs.sonarsource.com/sonarqube-server/2025.2/user-guide/issues/fixing#getting-ai-generated-fix-suggestions "mention")
* see [#label-projects-with-ai-code](https://docs.sonarsource.com/sonarqube-server/2025.2/ai-capabilities/ai-standards#label-projects-with-ai-code "mention")

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/ai-capabilities/ai-fix-suggestions.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/ai-capabilities/ai-fix-suggestions.md

# AI CodeFix

*AI CodeFix is only available in SonarQube Server* [*Enterprise and Data Center editions*](https://www.sonarsource.com/plans-and-pricing/sonarqube/) to provide AI-generated fixes for your issues.

Sonar AI CodeFix uses a large language model (LLM) to automatically generate AI-driven code fixes for the issues discovered by SonarQube Server. The process is simple. When you request a fix, the affected code and issue description are sent to an LLM. AI CodeFix then proposes an edit that resolves the problem without changing the code’s functionality.

AI CodeFix currently uses <code class="expression">space.vars.SQS\_20251\_Supported\_LLM\_version</code> to suggest fixes for a select set of rules in Java, JavaScript, TypeScript, Python, C#, and C++. To learn more about which rules are eligible for AI CodeFix, please see the list of [#ai-codefix-rules](https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/rules/rules-for-ai-codefix#ai-codefix-rules "mention").

### Enabling AI-generated fix suggestions <a href="#enabling-ai-generated-fix-suggestions" id="enabling-ai-generated-fix-suggestions"></a>

As an Instance Admin, you can activate or deactivate AI CodeFix for your organization at the global and project levels; see the [enable-ai-codefix](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/ai-features/enable-ai-codefix "mention") page for the full details.

### Sharing your code with Sonar <a href="#sharing-your-code-with-sonar" id="sharing-your-code-with-sonar"></a>

If you use Sonar’s AI CodeFix LLM, the affected code snippet will be sent by the AI CodeFix service to the selected LLM. Service agreements with Sonar’s LLMs prevent your code from being used to train those models.

For details about terms and conditions, please refer to the [AI CodeFix terms](https://www.sonarsource.com/legal/ai-codefix-terms/) in our [Legal Documentation](https://www.sonarsource.com/legal/).

### Getting AI-generated fix suggestions <a href="#getting-ai-generated-fix-suggestions" id="getting-ai-generated-fix-suggestions"></a>

Once AI CodeFix is enabled, users will be able to select **Generate AI Fix** on eligible issues and copy/paste the fix into their IDE with the **Open in IDE** feature when using [connected-mode](https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/connected-mode "mention").

For complete details about using AI CodeFix to fix your issues in SonarQube Server, see the article on [#getting-ai-generated-fix-suggestions](https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/issues/fixing#getting-ai-generated-fix-suggestions "mention").

### Usage limits <a href="#limits" id="limits"></a>

Limits are placed on the AI CodeFix feature to manage abuse. Developers will be notified directly when the monthly allocation is reached for your organization. If the instance is blocked due to reaching the allowance, users attempting to generate a fix will see an error message. Usage quotas are reset on the first day of each month.

### AI Code Assurance <a href="#ai-code-assurance" id="ai-code-assurance"></a>

Sonar recognizes that AI-generated code should be monitored with additional quality standards and offers administrators a series of tools described on the [ai-standards](https://docs.sonarsource.com/sonarqube-server/2025.1/ai-capabilities/ai-standards "mention") page.

It’s possible to view ratings for projects with AI Code Assurance in your portfolios beginning in the [Enterprise edition](https://www.sonarsource.com/plans-and-pricing/enterprise/). There, you will see a breakdown of projects, applications, and nested portfolios that include the standards you’ve set for AI-generated code. See the [#portfolio-breakdown](https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/viewing-reports/portfolios#portfolio-breakdown "mention") article for more information.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [overview](https://docs.sonarsource.com/sonarqube-server/2025.1/ai-capabilities/overview "mention") of AI capabilities
* [#ai-codefix-rules](https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/rules/rules-for-ai-codefix#ai-codefix-rules "mention")
* [autodetect-ai-code](https://docs.sonarsource.com/sonarqube-server/2025.1/ai-capabilities/autodetect-ai-code "mention")
* learn about [#getting-ai-generated-fix-suggestions](https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/issues/fixing#getting-ai-generated-fix-suggestions "mention")
* see [#label-projects-with-ai-code](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/analysis-functions/ai-code-assurance/overview#label-projects-with-ai-code "mention")

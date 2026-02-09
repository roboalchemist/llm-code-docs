# Source: https://docs.sonarsource.com/sonarqube-for-intellij/ai-capabilities/ai-codefix.md

# Source: https://docs.sonarsource.com/sonarqube-for-vs-code/ai-capabilities/ai-codefix.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/ai-capabilities/ai-codefix.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/ai-capabilities/ai-codefix.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/ai-capabilities/ai-codefix.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/ai-capabilities/ai-codefix.md

# Source: https://docs.sonarsource.com/sonarqube-server/ai-capabilities/ai-codefix.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/ai-capabilities/ai-codefix.md

# AI CodeFix

*AI features are only available in SonarQube Cloud Team and Enterprise plans*. See the [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") page for more detail&#x73;*.*

Sonar’s AI CodeFix uses a large language model (LLM) to automatically generate AI-driven code fixes for the issues discovered by SonarQube Cloud. The feature is available with SonarQube Cloud Team and Enterprise plans.

Using AI CodeFix is simple. When you request a fix, the affected code and issue description are sent to an LLM. AI CodeFix then proposes an edit that resolves the problem without changing the code’s functionality.

### Enabling AI-generated fix suggestions <a href="#enabling-ai-generated-fix-suggestions" id="enabling-ai-generated-fix-suggestions"></a>

SonarQube Cloud’s AI CodeFix is a feature that uses <code class="expression">space.vars.SQC\_Supported\_LLM\_version</code> to suggest fixes for a select set of rules in Java, JavaScript, TypeScript, Python, C#, and C++. See the [Sonar AI CodeFix terms](https://www.sonarsource.com/legal/ai-codefix-terms/) for details about the terms of access.

To learn more about which rules are eligible for AI CodeFix, please see the list of [#ai-codefix-rules](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/rules-for-ai-codefix#ai-codefix-rules "mention").

As an Organization Admin, you can activate or deactivate AI CodeFix for your organization at the global and project levels; see the [enable-ai-codefix](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/ai-features/enable-ai-codefix "mention") page for the full details.

### Sharing your code with Sonar <a href="#sharing-your-code-with-sonar" id="sharing-your-code-with-sonar"></a>

If you use Sonar’s AI CodeFix LLM, the affected code snippet will be sent by the AI CodeFix service to the selected LLM. Service agreements with Sonar’s LLMs prevent your code from being used to train those models.

For details about terms and conditions, please refer to the [AI CodeFix terms](https://www.sonarsource.com/legal/ai-codefix-terms/) in our [Legal Documentation](https://www.sonarsource.com/legal/).

### Getting AI-generated fix suggestions <a href="#getting-ai-generated-fix-suggestions" id="getting-ai-generated-fix-suggestions"></a>

Once AI CodeFix is enabled, users will be able to select **Generate AI Fix** on eligible issues and copy/paste the fix into their IDE with the **Open in IDE** feature when using [connected-mode](https://docs.sonarsource.com/sonarqube-cloud/improving/connected-mode "mention"). If your Engineers are using SonarQube for [VS Code](https://app.gitbook.com/o/2ibCvzwZt86Nlk2zloB7/s/6LPRABg3ubAJhpfR5K0Y/ "mention") or SonarQube for [Intellij](https://app.gitbook.com/o/2ibCvzwZt86Nlk2zloB7/s/NvI4wotPmITyM0mnsmtp/ "mention"), AI CodeFix is available in the IDE and follows the settings you defined in your quality profile.

* See the IntelliJ page for [AI CodeFix #AI CodeFix in your IDE](https://app.gitbook.com/s/NvI4wotPmITyM0mnsmtp/ai-capabilities/ai-codefix#ai-codefix "mention")
* See the VS Code page for [AI CodeFix #AI CodeFix in your IDE](https://app.gitbook.com/s/6LPRABg3ubAJhpfR5K0Y/ai-capabilities/ai-codefix#ai-codefix "mention")

To use AI CodeFix in SonarQube, please see the article about [#getting-ai-generated-fix-suggestions](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/fixing#getting-ai-generated-fix-suggestions "mention")*.*

### Usage limits <a href="#limits" id="limits"></a>

Limits are placed on the AI CodeFix feature to manage abuse. Developers will be notified directly when the monthly allocation is reached for your organization. If the instance is blocked due to reaching the allowance, users attempting to generate a fix will see an error message. Usage quotas are reset on the first day of each month.

### AI Code Assurance <a href="#ai-code-assurance" id="ai-code-assurance"></a>

Sonar recognizes that AI-generated code should be monitored with additional quality standards and offers administrators a series of tools described on the [ai-code-assurance](https://docs.sonarsource.com/sonarqube-cloud/ai-capabilities/ai-code-assurance "mention") page. The feature includes labels to mark projects with AI-generated code, custom quality gates that help protect your projects, and a set of external badges to monitor projects containing AI code.

If you’ve already set up AI Code Assurance and are ready to use the badges, it works just like any other. For instructions, please see the [#using-project-badge](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/managing-your-project-as-developer#using-project-badge "mention") article. You do not need to enable the AI CodeFix feature to use AI Code Assurance.

### Related pages <a href="#related-pages" id="related-pages"></a>

* Administering your [ai-features](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/ai-features "mention") as an Organization Admin
* [#ai-codefix-rules](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/rules-for-ai-codefix#ai-codefix-rules "mention")
* [ai-code-assurance](https://docs.sonarsource.com/sonarqube-cloud/ai-capabilities/ai-code-assurance "mention")
* [enable-ai-codefix](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/ai-features/enable-ai-codefix "mention") to get AI-generated fix suggestions

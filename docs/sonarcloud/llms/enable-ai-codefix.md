# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/ai-features/enable-ai-codefix.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/project-administration/ai-features/enable-ai-codefix.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/ai-features/enable-ai-codefix.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/project-administration/ai-features/enable-ai-codefix.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/ai-features/enable-ai-codefix.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/project-administration/ai-features/enable-ai-codefix.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/ai-features/enable-ai-codefix.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/project-administration/ai-features/enable-ai-codefix.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/ai-features/enable-ai-codefix.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/project-administration/ai-features/enable-ai-codefix.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/ai-features/enable-ai-codefix.md

# Source: https://docs.sonarsource.com/sonarqube-server/project-administration/ai-features/enable-ai-codefix.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/ai-features/enable-ai-codefix.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/ai-features/enable-ai-codefix.md

# AI CodeFix

Sonar’s AI CodeFix uses a large language model (LLM) to automatically generate AI-driven code fixes for the issues discovered by SonarQube Cloud AI CodeFix must be enabled by an Instance Admin and is defined for **All projects** or for **Only selected projects**.

See the [enable-ai-codefix](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/ai-features/enable-ai-codefix "mention") page for the full details.

### Getting AI-generated fix suggestions <a href="#getting-ai-generated-fix-suggestions" id="getting-ai-generated-fix-suggestions"></a>

SonarQube Cloud’s AI CodeFix is a feature that uses <code class="expression">space.vars.SQC\_Supported\_LLM\_version</code> to suggest fixes for a select set of rules in Java, JavaScript, TypeScript, Python, C#, and C++. To learn more about which rules are eligible for AI CodeFix, check the list of [#ai-codefix-rules](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/rules-for-ai-codefix#ai-codefix-rules "mention").

When an Instance Admin enables AI CodeFix for your project, you can get an AI-generated fix suggestion for eligible issues. See the [Sonar AI CodeFix terms](https://www.sonarsource.com/legal/ai-codefix-terms/) for details about the terms of access.

If you’re using connected mode with SonarQube for VS Code or SonarQube for IntelliJ, it's possible to get AI-generated fix suggestions directly in your IDE. See the relevant SonarQube for IDE pages to see how it works:

* In SonarQube for VS Code: [AI CodeFix #AI CodeFix in your IDE](https://app.gitbook.com/s/6LPRABg3ubAJhpfR5K0Y/ai-capabilities/ai-codefix#ai-codefix "mention")
* In SonarQube for IntelliJ: [AI CodeFix #AI CodeFix in your IDE](https://app.gitbook.com/s/NvI4wotPmITyM0mnsmtp/ai-capabilities/ai-codefix#ai-codefix "mention")

If you're not using connected mode with SonarQube for IDE, see the [#getting-ai-generated-fix-suggestions](https://docs.sonarsource.com/sonarqube-cloud/issues/fixing#getting-ai-generated-fix-suggestions "mention") article for alternative instructions. Then use the [#opening-issues-in-your-ide](https://docs.sonarsource.com/sonarqube-cloud/issues/fixing#opening-issues-in-your-ide "mention") feature to apply the fix.

### Related pages <a href="#related-pages" id="related-pages"></a>

* Administering your [ai-features](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/ai-features "mention") as an Organization Admin
* [set-up-ai-code-assurance](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/ai-features/set-up-ai-code-assurance "mention")

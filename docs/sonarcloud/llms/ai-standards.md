# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/analysis-functions/ai-standards.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/ai-capabilities/ai-standards.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/ai-capabilities/ai-standards.md

# AI Code Assurance

Sonar’s AI Code Assurance helps you ensure security and code quality within projects containing AI-generated code. By utilizing project labels, custom quality gate certification and marking, and dynamic project badge publishing, you can maintain high standards and confidently assure the quality of your AI projects.

### Assuring your AI code <a href="#assuring-your-ai-code" id="assuring-your-ai-code"></a>

Sonar recognizes that AI-generated code should be monitored with additional quality standards. Recommended checks include high standards to reduce code complexity, remove bugs, and eliminate injection vulnerabilities. SonarQube’s AI Code Assurance features bring confidence that your AI-generated code is being reviewed to avoid any accountability crisis.

These objectives are achieved with three features that allow Quality Standard administrators to qualify projects as AI Code Assured:

1. [#label-projects-with-ai-code](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/analysis-functions/ai-code-assurance/overview#label-projects-with-ai-code "mention")
2. [#apply-qualified-quality-gate](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/analysis-functions/ai-code-assurance/overview#apply-qualified-quality-gate "mention")
3. Publish an [#using-the-ai-code-assurance-badge](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/analysis-functions/ai-code-assurance/monitor-projects-with-ai-code#using-the-ai-code-assurance-badge "mention") externally to your websites (optional)

The full details are outlined on the [overview](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/analysis-functions/ai-code-assurance/overview "mention") page.

### Quality gates for AI code <a href="#quality-gates-for-ai-code" id="quality-gates-for-ai-code"></a>

Quality gates designed for projects containing AI-generated code are an important part of the quality control and review process. The [quality-gates-for-ai-code](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/analysis-functions/ai-code-assurance/quality-gates-for-ai-code "mention") page outlines the important control measures that help protect against the buildup of new issues as you leverage AI assistance in your coding process, and adds an extra layer of protection helps catch vulnerabilities and critical reliability issues that could be lurking in your project.

{% hint style="warning" %}
In SonarQube Server version 10.7, the Sonar way quality gate was enforced on projects marked as containing AI Code. If you’re migrating from this version, projects using this quality gate will lose their AI Code Assurance status until a new, AI-qualified quality gate is applied.
{% endhint %}

### Monitoring your projects <a href="#monitoring-your-projects" id="monitoring-your-projects"></a>

If you’ve completed the steps above to apply AI Code Assured quality gates to your projects, a series of external badges are available to publish on your websites. For more details, please see the [monitor-projects-with-ai-code](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/analysis-functions/ai-code-assurance/monitor-projects-with-ai-code "mention") page.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [overview](https://docs.sonarsource.com/sonarqube-server/2025.1/ai-capabilities/overview "mention") of AI capabilities
* [autodetect-ai-code](https://docs.sonarsource.com/sonarqube-server/2025.1/ai-capabilities/autodetect-ai-code "mention")
* Learn about [#getting-ai-generated-fix-suggestions](https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/issues/fixing#getting-ai-generated-fix-suggestions "mention") to use AI CodeFix

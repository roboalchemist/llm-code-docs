# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/quality-standards-administration/ai-code-assurance.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/ai-capabilities/ai-code-assurance.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/quality-standards-administration/ai-code-assurance.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/ai-capabilities/ai-code-assurance.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/analysis-functions/ai-code-assurance.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/quality-standards-administration/ai-code-assurance.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/ai-capabilities/ai-code-assurance.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/quality-standards-administration/ai-code-assurance.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/ai-capabilities/ai-code-assurance.md

# Source: https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/ai-code-assurance.md

# Source: https://docs.sonarsource.com/sonarqube-server/ai-capabilities/ai-code-assurance.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/ai-capabilities/ai-code-assurance.md

# AI Code Assurance

SonarQube Cloud’s AI Code Assurance features help you set appropriate standards for projects containing AI-generated code. A combination of tools, including project labels, a default quality gate, and the availability of externally published project badges, lets you ensure that your AI projects are protected for security and code quality.

### Assuring your AI code <a href="#assuring-your-ai-code" id="assuring-your-ai-code"></a>

Sonar recognizes that AI-generated code should be monitored with additional quality standards. Recommended checks include high standards to reduce code complexity, remove bugs, and eliminate injection vulnerabilities. SonarQube’s AI Code Assurance features bring confidence that your AI-generated code is being reviewed to avoid any accountability crisis.

These objectives are achieved with three features that allow Quality Standard administrators to qualify projects as AI Code Assured:

1. [#label-projects-with-ai-code](https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance/overview#label-projects-with-ai-code "mention")
2. [#apply-a-quality-gate-for-ai-code-assurance](https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance/overview#apply-a-quality-gate-for-ai-code-assurance "mention")
3. Publish an AI Code Assurance badge externally to your websites. See the [#monitor-projects-containing-ai-code](https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance/overview#monitor-projects-containing-ai-code "mention") page for instructions.

The full details to setting up AI Code Assurance are outlined on the [overview](https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance/overview "mention") page.

### Quality gates for AI code <a href="#quality-gates-for-ai-code" id="quality-gates-for-ai-code"></a>

Quality gates designed for projects containing AI-generated code are an important part of the quality control and review process. The [quality-gates-for-ai-code](https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance/quality-gates-for-ai-code "mention") page outlines the important control measures that help protect against the buildup of new issues as you leverage AI assistance in your coding process, and adds an extra layer of protection helps catch vulnerabilities and critical reliability issues that could be lurking in your project.

### Quality profiles for AI code <a href="#quality-profiles-for-ai-code" id="quality-profiles-for-ai-code"></a>

When AI Code Assurance is enabled on a project, it should protect the AI-generated code by applying a suitable quality standard for developers to follow. Therefore, it’s important to define a set of rules that will offer the necessary protection to AI-generated code. To ensure protection of a project with AI code, the project should not only have a strict quality gate, but also a strict quality profile. The [quality-profiles-for-ai-code](https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance/quality-profiles-for-ai-code "mention") page helps you define, for a given language, the set of coding rules to be applied during analysis.

### Autodetecting AI code <a href="#autodetecting-ai-code" id="autodetecting-ai-code"></a>

Knowing if your project contains AI-generated code helps raise awareness of code ownership and code security. To help build this awareness, SonarQube Cloud can autodetect AI-generated code in projects on GitHub using GitHub Copilot. See the page about [autodetect-ai-code](https://docs.sonarsource.com/sonarqube-cloud/ai-capabilities/autodetect-ai-code "mention") for an overview.

If your SonarCloud Organization is integrated with GitHub and you’re using GitHub Copilot, your project is eligible for automatically detecting AI-generated code. For more information, see [autodetect-ai-code](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/ai-features/autodetect-ai-code "mention").

### Monitoring your projects <a href="#monitoring-your-projects" id="monitoring-your-projects"></a>

If you’ve completed the steps above to apply AI Code Assured quality gates to your projects, a series of external badges are available to publish on your websites. For more details, please see the [monitor-projects-with-ai-code](https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance/monitor-projects-with-ai-code "mention") page.

### Related pages <a href="#related-pages" id="related-pages"></a>

* Administering your [ai-features](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/ai-features "mention") as an Organization Admin
* Learn about [ai-codefix](https://docs.sonarsource.com/sonarqube-cloud/ai-capabilities/ai-codefix "mention") to get AI-generated fix suggestions

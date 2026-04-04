# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/quality-standards-administration/ai-code-assurance/quality-gates-for-ai-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/quality-standards-administration/ai-code-assurance/quality-gates-for-ai-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/analysis-functions/ai-code-assurance/quality-gates-for-ai-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/quality-standards-administration/ai-code-assurance/quality-gates-for-ai-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/quality-standards-administration/ai-code-assurance/quality-gates-for-ai-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/ai-code-assurance/quality-gates-for-ai-code.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance/quality-gates-for-ai-code.md

# Quality gates for AI code

### Overview <a href="#overview" id="overview"></a>

The first objective for AI Code Assurance is labeling projects with the ![$contains-ai-code](https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-ca3b9de37a93a3d09c496b45878e418adab02c9f%2Fc151514ef7beca0f865ee429bc9fe0e33b05ceb4.svg?alt=media) label. For details, see [#label-projects-with-ai-code](https://docs.sonarsource.com/sonarqube-cloud/standards/overview#label-projects-with-ai-code "mention").

To complete the second objective, you will assign a quality gate qualified for AI Code Assurance to your projects. You can use the default quality gate, Sonar way for AI Code, or create a custom quality gate to meet your requirements; all of the instructions are on this page. If you already have an AI-qualified quality gate you want to use, skip to [#apply-your-quality-gate-for-ai-code-assurance](#apply-your-quality-gate-for-ai-code-assurance "mention") below.

With the correct quality gate applied, check if your project qualifies for [#autodetecting-ai-code](#autodetecting-ai-code "mention").

Projects completing these steps will show their AI Code Assurance status on the **Projects**, main-branch **Overview**, and **Project Information** pages. When using AI Code Assured quality gates, a series of external badges are available to publish on your websites. For more details, please see the [monitor-projects-with-ai-code](https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance/monitor-projects-with-ai-code "mention") page.

### Quality gates for AI code <a href="#quality-gates-for-ai-code" id="quality-gates-for-ai-code"></a>

#### Creating a custom quality gate for AI code <a href="#create-custom-quality-gates-for-ai-code" id="create-custom-quality-gates-for-ai-code"></a>

Creating a custom quality gate for AI code begins like any other. In SonarQube Cloud, navigate to *Your Organization* > **Quality Gates** and select **Create**. For more details about defining your conditions, see the [managing-custom-quality-gates](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/managing-custom-quality-gates "mention") page. Once you’ve defined your conditions, go to the three-dots menu and select **Qualify for AI Code Assurance**.

The use of the *Sonar way* quality gate is no longer enforced on projects marked as containing AI code.

#### Recommendations on custom quality gates for AI code <a href="#recommendations-on-custom-quality-gates-for-ai-code" id="recommendations-on-custom-quality-gates-for-ai-code"></a>

To safeguard your projects from potential issues introduced by AI-generated code and fixes, it’s crucial to implement stringent quality control and review processes. By setting conditions on your [about-new-code](https://docs.sonarsource.com/sonarqube-cloud/standards/about-new-code "mention") (NCD) within your quality gate, you can proactively prevent the buildup of new issues as you leverage AI assistance in your coding process.

Remember that AI assistants might have been used to generate code in your projects even before you defined your NCD. Therefore, it’s essential to also apply conditions to Overall Code. This extra layer of protection helps catch vulnerabilities and critical reliability issues that could be lurking in your project, beyond the reach of your NCD.

#### Sonar way for AI code <a href="#use-the-sonar-way-for-ai-code" id="use-the-sonar-way-for-ai-code"></a>

The *Sonar way for AI Code* quality gate is the recommended quality gate for AI Code Assurance and is the suggested quality gate for AI code projects. To ensure your AI-generated code is secure, high-quality, and maintainable, while also boosting development productivity and avoiding business risks, it needs strict quality control and reviews on both new and overall code.

**Conditions applied to the Sonar way for AI code quality gate**

The Sonar way for AI code quality gate has seven conditions:

* Conditions on new code:
  * No new issues are introduced
  * All new Security Hotspots are reviewed
  * New code test coverage is greater than or equal to 80.0%
  * Duplication in the new code is less than or equal to 3.0%
* Conditions on overall code:
  * Security rating: A
  * All security hotspots are reviewed
  * Reliability rating: C

{% hint style="info" %}
It’s possible that AI-generated code exists in your overall code, outside of the scope of your new code definition. To address this, Sonar recommends *adding a coverage condition with suitable threshold on overall code* because AI-generated code found in old code can be risky. See the [#managing-conditions](https://docs.sonarsource.com/sonarqube-cloud/managing-quality-gates/managing-custom-quality-gates#managing-conditions "mention") article to learn how to add a coverage condition.
{% endhint %}

### Qualifying your quality gate for AI Code Assurance <a href="#qualify-your-quality-gate-for-ai-code" id="qualify-your-quality-gate-for-ai-code"></a>

Any quality gate can be marked as qualified for AI code with the ![$in-shield-on](https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-d7f52ebf82d639fd6bae4f80add21c21628c518e%2F185be81999243203ea71699933ca21b534b1d0c8.svg?alt=media)**AI Code Assurance** status label available for quality gates. To activate this label, open the **Actions** menu of your quality gate on the **Quality Gates** page and select **Qualify for AI Code Assurance**. Before you create a custom quality gate for AI code, check the recommendations listed above for conditions included in the *Sonar way for AI Code* quality gate.

### Apply your quality gate for AI Code Assurance <a href="#apply-your-quality-gate-for-ai-code-assurance" id="apply-your-quality-gate-for-ai-code-assurance"></a>

The final step in achieving AI Code Assurance requires that an AI-qualified quality gate be applied to your project. In SonarQube Cloud, navigate to *Your Organization* > *Your Project* > **Administration** > **AI Code Assurance**.

1. If you’ve already [#label-projects-with-ai-code](https://docs.sonarsource.com/sonarqube-cloud/standards/overview#label-projects-with-ai-code "mention"), it’s eligible for the ![$in-shield-on](https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-d7f52ebf82d639fd6bae4f80add21c21628c518e%2F185be81999243203ea71699933ca21b534b1d0c8.svg?alt=media)**AI Code Assurance** status label; all you need to do is apply an AI-qualified quality gate.
2. Select a quality gate qualified for AI Code Assurance.

Projects completing these steps will show their AI Code Assurance status on the **Projects** page, each of the branch overview pages (**Overview**, **Main Branch**, **Pull Requests**, and **Branches**), and your project’s **Information** page. To understand the status labels and badges for AI Code Assurance, see the [monitor-projects-with-ai-code](https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance/monitor-projects-with-ai-code "mention") page.

Projects marked as containing AI-generated code and *do not use an AI Code Assured quality gate* will only display the ![$contains-ai-code](https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-ca3b9de37a93a3d09c496b45878e418adab02c9f%2Fc151514ef7beca0f865ee429bc9fe0e33b05ceb4.svg?alt=media) label.

### Autodetecting AI code <a href="#autodetecting-ai-code" id="autodetecting-ai-code"></a>

If your SonarCloud Organization is integrated with GitHub and you’re using GitHub Copilot, your project is eligible for automatically detecting AI-generated code. For more information, see [autodetect-ai-code](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/ai-features/autodetect-ai-code "mention").

### Monitoring your projects <a href="#monitoring-your-projects" id="monitoring-your-projects"></a>

If you’ve completed the steps above to apply AI Code Assured quality gates to your project, a series of external badges are available to publish on your websites. For more details, please see the [monitor-projects-with-ai-code](https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance/monitor-projects-with-ai-code "mention") page.

### Related pages <a href="#related-pages" id="related-pages"></a>

* SonarQube Cloud's [ai-capabilities](https://docs.sonarsource.com/sonarqube-cloud/ai-capabilities "mention")
* [overview](https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance/overview "mention")
* Administering your [ai-features](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/ai-features "mention") as an Organization Admin
  * Learn how to[autodetect-ai-code](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/ai-features/autodetect-ai-code "mention") in projects using GitHub and GitHub Copilot
  * Quickly [enable-ai-codefix](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/ai-features/enable-ai-codefix "mention") to get AI-generated fix suggestions

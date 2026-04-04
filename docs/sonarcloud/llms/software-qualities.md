# Source: https://docs.sonarsource.com/sonarqube-community-build/user-guide/rules/software-qualities.md

# Source: https://docs.sonarsource.com/sonarqube-for-eclipse/using/software-qualities.md

# Source: https://docs.sonarsource.com/sonarqube-for-visual-studio/using/software-qualities.md

# Source: https://docs.sonarsource.com/sonarqube-for-intellij/using/software-qualities.md

# Source: https://docs.sonarsource.com/sonarqube-for-vs-code/using/software-qualities.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/user-guide/clean-code/software-qualities.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/user-guide/clean-code/software-qualities.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/user-guide/clean-code/software-qualities.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/core-concepts/clean-code/software-qualities.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/core-concepts/clean-code/software-qualities.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/user-guide/rules/software-qualities.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/user-guide/rules/software-qualities.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/user-guide/rules/software-qualities.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/rules/software-qualities.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/user-guide/rules/software-qualities.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/user-guide/rules/software-qualities.md

# Source: https://docs.sonarsource.com/sonarqube-server/user-guide/rules/software-qualities.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/software-qualities.md

# Software qualities

High quality code contributes to software that is secure, reliable, and maintainable. These three aspects - security, reliability, and maintainability - are called software qualities in SonarQube and they contribute to the long-term value of your software.

### Security <a href="#security" id="security"></a>

Security is the protection of your software from unauthorized access, use, or destruction.

### Reliability <a href="#reliability" id="reliability"></a>

Reliability is a measure of how your software is capable of maintaining its level of performance under stated conditions for a stated period of time.

### Maintainability <a href="#maintainability" id="maintainability"></a>

Maintainability refers to the ease with which you can repair, improve and understand software code.

### Severity at the software quality level <a href="#quality-level-severity" id="quality-level-severity"></a>

| **Severity** | **Definition**                                                                                                                                                                                                                                                                 |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Blocker      | An issue that has a significant probability of severe unintended consequences on the application that should be fixed immediately. This includes bugs leading to production crashes and security flaws allowing attackers to extract sensitive data or execute malicious code. |
| High         | An issue with a high impact on the application that should be fixed as soon as possible.                                                                                                                                                                                       |
| Medium       | An issue with a medium impact.                                                                                                                                                                                                                                                 |
| Low          | An issue with a low impact.                                                                                                                                                                                                                                                    |
| Info         | There is no expected impact on the application. For informational purposes only.                                                                                                                                                                                               |

### Code analysis <a href="#code-analysis" id="code-analysis"></a>

The Sonar automated code review aims to identify any issue in your code. Each code attribute is evaluated, for a given language, based on a series of rules.

* Each rule is associated with one or more software qualities (security, reliability, or maintainability).
* Each associated software quality is assigned a severity (blocker, high, medium, low, or info). This severity determines how much that software quality is impacted when the rule is broken.

When a rule is broken, an issue is raised. The issue affects one or more software qualities with varying severity as inherited from the rule.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [rules](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/rules "mention")
* [introduction](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/introduction "mention") to managing your code issues

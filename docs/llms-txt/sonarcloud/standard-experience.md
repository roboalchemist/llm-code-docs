# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/analysis-functions/instance-mode/standard-experience.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/analysis-functions/instance-mode/standard-experience.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/analysis-functions/instance-mode/standard-experience.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/analysis-functions/instance-mode/standard-experience.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/analysis-functions/instance-mode/standard-experience.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/analysis-functions/instance-mode/standard-experience.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/analysis-functions/instance-mode/standard-experience.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/analysis-functions/instance-mode/standard-experience.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/instance-mode/standard-experience.md

# Standard Experience

This approach focuses on assigning severity to a rule based on the single software quality (e.g. security, reliability, or maintainability) it has the largest impact on.

### How severity works in Standard Experience mode <a href="#se-severity" id="se-severity"></a>

<table><thead><tr><th width="105">Severity</th><th>Severity</th></tr></thead><tbody><tr><td>Blocker</td><td>An issue that has a significant probability of severe unintended consequences on the application that should be fixed immediately. This includes bugs leading to production crashes and security flaws allowing attackers to extract sensitive data or execute malicious code.</td></tr><tr><td>Critical</td><td>An issue with a critical impact on the application that should be fixed as soon as possible.</td></tr><tr><td>Major</td><td>An issue with a major impact on the application.</td></tr><tr><td>Minor</td><td>An issue with a minor impact on the application.</td></tr><tr><td>Info</td><td>There is no expected impact on the application. For informational purposes only.</td></tr></tbody></table>

### Related pages <a href="#related-pages" id="related-pages"></a>

* [mqr-mode](https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/instance-mode/mqr-mode "mention")
* [changing-modes](https://docs.sonarsource.com/sonarqube-server/user-guide/code-metrics/changing-modes "mention")

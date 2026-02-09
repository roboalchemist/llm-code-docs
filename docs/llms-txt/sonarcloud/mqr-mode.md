# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/analysis-functions/instance-mode/mqr-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/analysis-functions/instance-mode/mqr-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/analysis-functions/instance-mode/mqr-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/analysis-functions/instance-mode/mqr-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/analysis-functions/instance-mode/mqr-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/analysis-functions/instance-mode/mqr-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/analysis-functions/instance-mode/mqr-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/analysis-functions/instance-mode/mqr-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/instance-mode/mqr-mode.md

# MQR mode

This approach focuses on ensuring the impact on all [software-qualities](https://docs.sonarsource.com/sonarqube-server/user-guide/rules/software-qualities "mention") is clear, not just the one most severely impacted.

### How severity works in MQR mode <a href="#mqr-severity" id="mqr-severity"></a>

<table><thead><tr><th width="101">Severity</th><th>Definition</th></tr></thead><tbody><tr><td>Blocker</td><td>An issue that has a significant probability of severe unintended consequences on the application that should be fixed immediately. This includes bugs leading to production crashes and security flaws allowing attackers to extract sensitive data or execute malicious code.</td></tr><tr><td>High</td><td>An issue with a high impact on the application that should be fixed as soon as possible.</td></tr><tr><td>Medium</td><td>An issue with a medium impact.</td></tr><tr><td>Low</td><td>An issue with a low impact.</td></tr><tr><td>Info</td><td>There is no expected impact on the application. For informational purposes only.</td></tr></tbody></table>

### Related pages <a href="#related-pages" id="related-pages"></a>

* [standard-experience](https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/instance-mode/standard-experience "mention")
* [changing-modes](https://docs.sonarsource.com/sonarqube-server/user-guide/code-metrics/changing-modes "mention")

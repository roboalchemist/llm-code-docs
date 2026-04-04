# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/analysis-functions/instance-mode/instance-mode-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/analysis-functions/instance-mode/instance-mode-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/analysis-functions/instance-mode/instance-mode-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/analysis-functions/instance-mode/instance-mode-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/analysis-functions/instance-mode/instance-mode-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/analysis-functions/instance-mode/instance-mode-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/analysis-functions/instance-mode/instance-mode-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/analysis-functions/instance-mode/instance-mode-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/instance-mode/instance-mode-overview.md

# Overview

{% hint style="info" %}
New SonarQube Server instances use MQR Mode by default. Upon upgrading, existing SonarQube Server 10.1 and earlier are configured with the Standard Experience by default.
{% endhint %}

* [standard-experience](https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/instance-mode/standard-experience "mention"): Standard Experience mode encompasses the use of rule types such as bugs, code smells, and vulnerabilities, with a single type and severity level for each rule. This approach focuses on assigning severity to a rule based on the single software quality (e.g. security, reliability, or maintainability) it has the largest impact on.
* [mqr-mode](https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/instance-mode/mqr-mode "mention")**:** MQR Mode aims to more accurately represent the impact an issue has on all software qualities. It does this by assigning a separate severity to a rule for each software quality it might impact. This approach focuses on ensuring the impact on all software qualities is clear, not just the one most severely impacted.

Instance administrators can set or update the mode by navigating to **Administration** > **Configuration** > **General Settings** > **Mode.** See [changing-modes](https://docs.sonarsource.com/sonarqube-server/user-guide/code-metrics/changing-modes "mention") for more information about how switching between the modes might affect your metrics and workflow.

Both the MQR and Standard Experience modes are compatible with [SonarQube for IDE](https://www.sonarsource.com/products/sonarlint/).

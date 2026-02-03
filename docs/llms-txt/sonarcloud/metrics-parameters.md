# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/analysis-functions/metrics-parameters.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/analysis-functions/metrics-parameters.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/analysis-functions/metrics-parameters.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/analysis-functions/metrics-parameters.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/analysis-functions/metrics-parameters.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/analysis-functions/metrics-parameters.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/analysis-functions/metrics-parameters.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/analysis-functions/metrics-parameters.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/analysis-functions/metrics-parameters.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/metrics-parameters.md

# Code metrics

You can modify some parameters related to the maintainability metrics at the global level in the SonarQube Server UI, provided you have the Administer system permission. Alternatively, you can set the corresponding sonar property on the CI/CD host (see [analysis-parameters](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/analysis-parameters "mention")).

### Changing the software development cost calculation <a href="#dev-cost-calculation" id="dev-cost-calculation"></a>

The development cost of one line of code is used in the Technical debt ratio calculation. To change the default value:

1. In the top navigation bar of SonarQube Server, select **Administration > Configuration > General settings > Technical Debt**.
2. In **Development cost**, change the values (in minutes).

The corresponding sonar property is `sonar.technicalDebt.developmentCost`.

### Changing the maintainability rating grid <a href="#maintainability-rating" id="maintainability-rating"></a>

To change the default Maintainability rating grid:

1. In the top navigation bar of SonarQube Server, select **Administration > Configuration > General settings > Technical Debt**.
2. In **Maintainability rating grid**, change the rating definition.

The corresponding sonar property is `sonar.technicalDebt.ratingGrid`.

### Related pages

* [metrics-definition](https://docs.sonarsource.com/sonarqube-server/user-guide/code-metrics/metrics-definition "mention")

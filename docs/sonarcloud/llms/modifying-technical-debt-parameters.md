# Source: https://docs.sonarsource.com/sonarqube-server/10.6/user-guide/code-metrics/modifying-technical-debt-parameters.md

# Modifying technical-debt parameters

You can modify in the SonarQube UI at the global level some parameters related to the [metrics-definition](https://docs.sonarsource.com/sonarqube-server/10.6/user-guide/code-metrics/metrics-definition "mention") provided you have the Administer system permission. Alternatively, you can set the corresponding sonar property on the CI/CD host (see Analysis parameters).

### Changing the software development cost calculation <a href="#sw-dev-cost-calculation" id="sw-dev-cost-calculation"></a>

The development cost of one line of code is used in the Technical debt ratio calculation. To change the default value:

1. In the top navigation bar of SonarQube, select **Administration > Configuration > General settings > Technical Debt**.
2. In **Development cost**, change the values (in minutes).

The corresponding sonar property is `sonar.technicalDebt.developmentCost`.

### Changing the maintainability rating grid <a href="#maintainability-rating-grid" id="maintainability-rating-grid"></a>

To change the default Maintainability rating grid:

1. In the top navigation bar of SonarQube, select **Administration > Configuration > General settings > Technical Debt**.
2. In **Maintainability rating grid**, change the rating definition.

The corresponding sonar property is `sonar.technicalDebt.ratingGrid`.

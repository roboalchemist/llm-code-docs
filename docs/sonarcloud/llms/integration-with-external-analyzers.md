# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/analysis-functions/integration-with-external-analyzers.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/analysis-functions/integration-with-external-analyzers.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/analysis-functions/integration-with-external-analyzers.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/integration-with-external-analyzers.md

# Integration with external analyzers at instance level

Many languages have dedicated analyzers (also known as linters) that are commonly used to spot problems in code. SonarQube can integrate the results from many of these external analyzers. This lets you see this information alongside the other SonarQube metrics and allows the external results to be taken into account when calculating quality gate status.

You can set up in the UI and at the instance level the integration of the third-party analyzers supported by SonarQube, except the .NET and go analyzers. This setup can be overridden at the project level. For the list of supported analyzers, see [about-external-issues](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/importing-external-issues/about-external-issues "mention").

Proceed as follows:

1. In your SonarQube instance, go to **Administration > Configuration > General Settings > External Analyzers**.
2. In the page, navigate to the language you want to set up.
3. In the parameter corresponding to your analyzer, enter the list of import directories or files. This parameter accepts a comma-delimited list of paths. A path definition is either relative to the `sonar.projectBaseDir` analysis parameter (which is by default the directory from which the analysis was started) or absolute.

### Related pages

[about-external-issues](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/importing-external-issues/about-external-issues "mention")\
[#for-files](https://docs.sonarsource.com/sonarqube-server/project-administration/adjusting-analysis/setting-analysis-scope/defining-matching-patterns#for-files "mention")\
[importing-external-issues](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/importing-external-issues "mention") (at the project level)\
[analysis-parameters](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/analysis-parameters "mention")

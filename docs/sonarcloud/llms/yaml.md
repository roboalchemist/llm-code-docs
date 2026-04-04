# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/languages/yaml.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/languages/yaml.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/languages/yaml.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/yaml.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/yaml.md

# YAML

The analysis of YAML files is disabled by default. You can enable it by setting the `sonar.yaml.activate` property to `true`.

This property does not affect analysis of language / framework specific YAML files.

YAML files that are detected as belonging to [cloudformation](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/cloudformation "mention"), [kubernetes](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/kubernetes "mention"), or [ansible](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/ansible "mention") will be additionally analyzed by the dedicated analyzers, next to the general YAML analysis.

### Language-specific properties <a href="#language-specific-properties" id="language-specific-properties"></a>

To discover and update the YAML-specific properties, navigate in SonarQube Cloud to *Your Project* > **Administration** > **General Settings** > **Languages** > **YAML**. See the [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") page for more information about specific properties.

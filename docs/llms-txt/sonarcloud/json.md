# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/languages/json.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/languages/json.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/languages/json.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/json.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/json.md

# JSON

The analysis of JSON files is disabled by default. You can enable it by setting the `sonar.json.activate` property to `true`.

This property does not affect analysis of language / framework specific JSON files.

JSON files that are detected as belonging to the [cloudformation](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/cloudformation "mention") or [azure-resource-manager](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/azure-resource-manager "mention") language-types will be additionally analyzed by the dedicated analyzers, adjacent to this general JSON analysis.

### Language-specific properties <a href="#language-specific-properties" id="language-specific-properties"></a>

To discover and update the JSON-specific properties, navigate in SonarQube Cloud to *Your Project* > **Administration** > **General Settings** > **Languages** > **JSON**. See the [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") page for more information about specific properties.

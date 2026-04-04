# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/languages/terraform.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/analyzing-source-code/languages/terraform.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/languages/terraform.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code/languages/terraform.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/languages/terraform.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/languages/terraform.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/languages/terraform.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/languages/terraform.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/languages/terraform.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/languages/terraform.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/languages/terraform.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/languages/terraform.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/languages/terraform.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/languages/terraform.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/languages/terraform.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/terraform.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/terraform.md

# Terraform

### Supported versions <a href="#supported-versions" id="supported-versions"></a>

The level of support for a language is defined as follows:

* Fully supported: Analysis will complete. All the language features are understood and examined.
* Supported: Most language features are understood and examined but the version includes unsupported features. Analysis might break or provide incomplete results.

Versions 1.3, 1.4 and 1.5 are supported

### Language-specific properties <a href="#language-specific-properties" id="language-specific-properties"></a>

To discover and update the Terraform-specific properties, navigate in SonarQube Cloud to *Your Project* > **Administration** > **General Settings** > **Languages** > **Terraform**. See the [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") page for more information about specific properties.

### Supported platforms <a href="#supported-platforms" id="supported-platforms"></a>

Platforms:

* Amazon Web Services
* Azure Cloud
* Google Cloud Platform

### Terraform provider versions <a href="#terraform-provider-versions" id="terraform-provider-versions"></a>

The various Terraform providers are frequently updated. New resources, properties, and default values are added, while at the same time, others are deprecated or dropped. For this reason, Terraform analysis is defensive by default; some issues will be automatically silenced to avoid raising false positives. In order to get a more precise analysis, you can specify the provider versions your code supports via a parameter.

**AWS**: `sonar.terraform.provider.aws.version`\
**Azure**: `sonar.terraform.provider.azure.version`\
**GCP**: For Google Cloud Platform, no versions are currently considered in the analysis

Accepted are versions having the format: `X.Y.Z`, `X.Y` or `X`.

Examples:

* `sonar.terraform.provider.aws.version=1.93.4`
* `sonar.terraform.provider.aws.version=3.4`
* `sonar.terraform.provider.aws.version=4`

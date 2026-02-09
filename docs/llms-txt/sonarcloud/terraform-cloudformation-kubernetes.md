# Source: https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/languages/terraform-cloudformation-kubernetes.md

# Terraform/CloudFormation/Kubernetes

### Language-specific properties <a href="#language-specific-properties" id="language-specific-properties"></a>

Discover and update the Terraform [analysis-parameters](https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/analysis-parameters "mention") in **Administration > General Settings > Languages > Terraform**

Discover and update the CloudFormation [analysis-parameters](https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/analysis-parameters "mention") in **Administration > General Settings > Languages > CloudFormation**

Discover and update the Kubernetes [analysis-parameters](https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/analysis-parameters "mention") in **Administration > General Settings > Languages > Kubernetes**

### Supported versions <a href="#supported-versions" id="supported-versions"></a>

* Terraform 1.x (HCL format only)
* CloudFormation with AWSTemplateFormatVersion 2010-09-09 (YAML and JSON)
* Kubernetes (YAML)
* AWS, Azure and GCP

#### Terraform provider versions <a href="#terraform-provider-versions" id="terraform-provider-versions"></a>

The respective Terraform providers are frequently updated. New resources, properties and default values are added. At the same time, others are deprecated or dropped. For this reason, the Terraform analysis is defensive by default: some issues will be automatically silenced to avoid raising false positives. In order to get a more precise analysis you can specify the provider versions your code supports via a parameter.

**AWS**: `sonar.terraform.provider.aws.version`\
**Azure**: `sonar.terraform.provider.azure.version`\
**GCP**: For Google Cloud Platform, no versions are currently considered in the analysis.

Accepted are versions having the format: `X.Y.Z`, `X.Y` or `X`

Examples:

* `sonar.terraform.provider.aws.version=1.93.4`
* `sonar.terraform.provider.aws.version=3.4`
* `sonar.terraform.provider.aws.version=4`

### Related pages <a href="#related-pages" id="related-pages"></a>

For CloudFormation you can import `cfn-lint` reports. See **Administration > General Settings > External Analyzers** for more information

### Issue tracker <a href="#issue-tracker" id="issue-tracker"></a>

Check the [issue tracker](https://sonarsource.atlassian.net/jira/software/c/projects/SONARIAC/boards/365) for this language.

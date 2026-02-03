# Source: https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/languages/terraform-cloudformation-kubernetes-docker.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/languages/terraform-cloudformation-kubernetes-docker.md

# Terraform/CloudFormation/Kubernetes/Docker

### Language-specific properties <a href="#language-specific-properties" id="language-specific-properties"></a>

Discover and update the Terraform [analysis-parameters](https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/analysis-parameters "mention") in **Administration > General Settings > Languages > Terraform**

Discover and update the CloudFormation [analysis-parameters](https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/analysis-parameters "mention") in **Administration > General Settings > Languages > CloudFormation**

Discover and update the Kubernetes [analysis-parameters](https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/analysis-parameters "mention") in **Administration > General Settings > Languages > Kubernetes**

Discover and update the Docker [analysis-parameters](https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/analysis-parameters "mention") in **Administration > General Settings > Languages > Docker**

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

Accepted are versions having the format: `X.Y.Z`, `X.Y` or `X`Examples:

* `sonar.terraform.provider.aws.version=1.93.4`
* `sonar.terraform.provider.aws.version=3.4`
* `sonar.terraform.provider.aws.version=4`

### Dockerfiles <a href="#dockerfiles" id="dockerfiles"></a>

**No NoSonar Support:**

Trailing comments are not permitted in Dockerfiles. For this reason, our Dockerfile parser does not support NOSONAR comments to suppress issues. Issues and hotspots must be reviewed in the UI.

**Missing Uniform Filename Convention:**

Dockerfiles can have all kinds of names and do not need a file extension. For this reason, it is difficult for the scanner and the analyzer to recognize all Dockerfiles. By default, all files named Dockerfile, Dockerfile.\*, or \*.dockerfile are considered Dockerfiles. If other conventions apply, these can be specified via the scanner property sonar.lang.patterns.docker.

### Related pages <a href="#related-pages" id="related-pages"></a>

For CloudFormation you can import `cfn-lint` reports. See **Administration > General Settings > External Analyzers** for more information

# Source: https://docs.snyk.io/scan-with-snyk/snyk-iac/detect-manually-created-resources.md

# Detect manually created resources

Snyk IaC can report unmanaged resources. Unmanaged resources are resources that are present on your cloud provider but not on your Terraform state. You can import these resources into Terraform or delete them from your IaaS account.

For information about detecting drift of managed resources, see [Command: plan](https://developer.hashicorp.com/terraform/cli/commands/plan) in the Terraform CLI documentation.

The information in this group of pages supports using the `snyk iac describe` command. Information is provided about the following:

* [Get started with Snyk IaC Describe on AWS](https://docs.snyk.io/scan-with-snyk/snyk-iac/detect-manually-created-resources/get-started-with-snyk-iac-describe-on-aws)
* [Configure cloud providers](https://docs.snyk.io/scan-with-snyk/snyk-iac/detect-manually-created-resources/configure-cloud-providers)
* [Supported resources](https://docs.snyk.io/scan-with-snyk/snyk-iac/detect-manually-created-resources/supported-resources)
* [IaC describe command examples](https://docs.snyk.io/scan-with-snyk/snyk-iac/detect-manually-created-resources/iac-describe-command-examples)
* [Filter rules](https://docs.snyk.io/scan-with-snyk/snyk-iac/detect-manually-created-resources/filter-rules)
* [Ignore resources for drift](https://docs.snyk.io/scan-with-snyk/snyk-iac/detect-manually-created-resources/ignore-unmanaged-resources)
* [IAC sources usage](https://docs.snyk.io/scan-with-snyk/snyk-iac/detect-manually-created-resources/iac-sources-usage)

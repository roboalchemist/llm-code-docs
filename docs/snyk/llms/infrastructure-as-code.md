# Source: https://docs.snyk.io/implementation-and-setup/enterprise-implementation-guide/phase-6-rolling-out-the-prevention-stage/infrastructure-as-code.md

# Source: https://docs.snyk.io/implementation-and-setup/team-implementation-guide/phase-5-rolling-out-the-prevention-stage/infrastructure-as-code.md

# Infrastructure as code

For Snyk IaC, you may choose to integrate with [Terraform Cloud](https://docs.snyk.io/developer-tools/snyk-ci-cd-integrations/terraform-cloud-integration-for-snyk-iac-using-run-tasks/how-to-use-the-terraform-cloud-integration-for-iac) to run snyk iac test as part of a ‘run’ workflow, in addition to scanning Terraform and YAML files that are included as part of your source control repositories.

For instructions on how to implement Snyk per IaC type in the Snyk CLI, see [Snyk CLI for IaC](https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/snyk-cli-for-iac).

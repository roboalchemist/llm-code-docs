# Source: https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration.md

# Direct CI/CD Integration

The Direct Source Control integration allows teams to define their configurations using a YAML file directly within their repositories. This method provides the flexibility to customize the integration settings and behavior for each project.

Most CI systems (e.g., GitHub Actions, GitLab CI) allow defining pipelines using YAML files. You can add OX scan steps to these files directly in the repository.

* Example: Add a scan command to `.gitlab-ci.yml` or `.github/workflows/scan.yml`
* You can specify flags, severity filters, and behavior per pipeline job.

This method provides granular control over integration settings and allows version-controlled configuration management, but requires configuration for each repository and might be more complex in configuration and maintenance than other methods.

You can use this method in the following systems:

* [GitHub Actions](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration/github-actions)
* [GitLab CI/CD](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration/gitlab-ci-cd)
* [Bitbucket Pipelines](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration/bitbucket-pipelines)
* [Jenkins](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration/jenkins)
* [Azure Pipelines and Azure DevOps](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration/azure-pipelines-and-azure-devops)
* [Generic CI](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration/generic-ci)

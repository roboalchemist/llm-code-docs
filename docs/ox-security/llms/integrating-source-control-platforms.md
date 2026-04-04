# Source: https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms.md

# Integrating Source Control Platforms

OX supports App, Webhook, and Direct CI/CD methods for integrating with your source control system. These methods are not mutually exclusive; you can combine them.

Required scopes and permissions for each source control integration are described in their respective configuration guides.

#### Comparison of Integration Methods

| Method                                                                                                                                                                              | Pros                                      | Considerations                                                                                                                                                    |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub App and Bitbucket App](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/app-pipeline-integration)   | Minimal setup per repo, UI-based control  | Available only for supported platforms (GitHub, Bitbucket).                                                                                                       |
| [Direct CI/CD](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration) | Full customization per repo               | <ul><li>Requires configuring and maintaining YAML file in each repository.</li><li>Setup can be more complex and requires familiarity with YAML syntax.</li></ul> |
| [Webhook](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/broken-reference)                                                                     | Centralized setup, easy to apply at scale | Less flexible than per-repo YAML.                                                                                                                                 |

OX integrates with the following source control platforms:

* **App**
  * [GitHub App](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/broken-reference)
  * [Bitbucket App](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/app-pipeline-integration/bitbucket-app)
* **Webhooks**
  * [GitLab Webhooks](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/broken-reference)
* **Direct CI/CD**
  * [GitHub Actions](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration/github-actions)
  * [GitLab CI/CD](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration/gitlab-ci-cd)
  * [Bitbucket Pipelines](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration/bitbucket-pipelines)
  * [Jenkins](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration/jenkins)
  * [Azure Pipelines and Azure DevOps](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration/azure-pipelines-and-azure-devops)

## Configuring SaaS and On-Prem source control platforms

All source control systems operate both as Software as a Service (SaaS) and on-premises solutions, with the exception of Gerrit, which only functions as an on-prem solution.

To configure your source control system on-premises, it must meet the following requirements:

* Whitelist IPs for OX connection.
* OX\_HOST\_URL: <https://your.onprem.url/>
* For OX Broker, you need to whitelist outgoing traffic to OX IPs.

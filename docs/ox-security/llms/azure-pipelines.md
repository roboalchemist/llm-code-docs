# Source: https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration/azure-pipelines-and-azure-devops/azure-pipelines.md

# Azure Pipelines

OX Security integrates with Azure Pipelines to scan builds for vulnerabilities during the CI/CD process. Azure Pipelines integration is ideal for streamlined security embedded directly into the CI/CD process.

## Prerequisites

* **Docker support:** Ensure your Azure agents can run Docker containers and execute `docker run`.

## Required environment variables

| Variable     | Description                                                                                                                                                                                                                                               |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `OX_API_KEY` | [The OX Security integration key.](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration/azure-pipelines-and-azure-devops/broken-reference) |

## Optional environment variables

| Variable               | Description                                                        |
| ---------------------- | ------------------------------------------------------------------ |
| `OX_OVERRIDE_BLOCKING` | Set to `true` to override job failure caused by blocking issues.   |
| `OX_TIMEOUT`           | Maximum duration of the scan, in minutes.                          |
| `OX_FAIL_ON_TIMEOUT`   | Set to `true` to fail the job if a scan times out.                 |
| `OX_FAIL_ON_ERROR`     | Set to `true` to fail the job if a system or network error occurs. |

## Advanced environment variables

| Variable                    | Description                                                                                                  |
| --------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `OX_DISABLE_SSL_VALIDATION` | Set to `true` to disable SSL certificate validation for self-signed certificates in on-premise environments. |

### Integration example (`azure-pipelines.yml`)

```yaml
pool:
  vmImage: ubuntu-latest

variables:
  - group: "OX"

stages:
  - stage: OX Security Scan
    jobs:
      - job: OX
        displayName: Run OX Security Scan
        steps:
          - script: |
              docker run \
                -e OX_API_KEY=$(OX_API_KEY) \
                --env-file <(env | grep 'SYSTEM_\|BUILD_') \
                oxsecurity/ox-block-mode:latest
```

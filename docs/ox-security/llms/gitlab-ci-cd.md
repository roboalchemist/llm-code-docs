# Source: https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration/gitlab-ci-cd.md

# GitLab CI/CD

OX Security integrates with GitLab CI/CD pipelines to detect vulnerabilities in Docker-based jobs.

To run scans on merge requests before they are merged, you must enable `merge request pipelines` in your GitLab CI/CD settings.

### Prerequisites

* **Docker support:** Your GitLab runners must support Docker and be able to run Docker-based jobs.

### Required environment variables

| Variable     | Description                                                                                                                                                                                                      |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `OX_API_KEY` | [The OX Security API key.](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration/broken-reference) |

### Optional environment variables

| Variable               | Description                                                        |
| ---------------------- | ------------------------------------------------------------------ |
| `OX_OVERRIDE_BLOCKING` | Set to `true` to override job failure caused by blocking issues.   |
| `OX_TIMEOUT`           | Maximum duration of the scan, in minutes.                          |
| `OX_FAIL_ON_TIMEOUT`   | Set to `true` to fail the job if a scan times out.                 |
| `OX_FAIL_ON_ERROR`     | Set to `true` to fail the job if a system or network error occurs. |

### Advanced environment variables

| Variable                    | Description                                                                                                  |
| --------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `OX_DISABLE_SSL_VALIDATION` | Set to `true` to disable SSL certificate validation for self-signed certificates in on-premise environments. |

### Integration example (`.gitlab-ci.yml`)

```yaml
stages:
  - test

ox_security_scan:
  stage: test
  image: oxsecurity/ox-block-mode:latest
  variables:
    OX_API_KEY: $OX_API_KEY
    # OX_OVERRIDE_BLOCKING: false
    # OX_TIMEOUT: 20
    # OX_FAIL_ON_TIMEOUT: false
    # OX_FAIL_ON_ERROR: false
  script:
    - ox-block-mode
  allow_failure: false
```

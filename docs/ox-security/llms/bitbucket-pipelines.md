# Source: https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration/bitbucket-pipelines.md

# Bitbucket Pipelines

OX Security supports integration with Bitbucket Pipelines to scan code changes during development. This allows you to detect security issues before the code is merged or deployed.

## Prerequisites

* Bitbucket Pipelines must support running Docker image–based pipes.
* The `OX_BITBUCKET_FULL_COMMIT` variable must be set explicitly due to a known Bitbucket issue that causes `BITBUCKET_COMMIT` to be shortened. Without this, scans may fail.

## Required environment variables

| Variable     | Description                                                                                                                                                                                                       |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `OX_API_KEY` | [Your OX Security API key.](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration/broken-reference) |

## Optional environment variables

| Variable                   | Description                                                                   |
| -------------------------- | ----------------------------------------------------------------------------- |
| `OX_BITBUCKET_FULL_COMMIT` | Full commit SHA. Required due to Bitbucket’s short SHA issue.                 |
| `OX_OVERRIDE_BLOCKING`     | Set to `true` to allow the job to continue even if blocking issues are found. |
| `OX_TIMEOUT`               | Scan timeout (in minutes).                                                    |
| `OX_FAIL_ON_TIMEOUT`       | Set to `true` to fail the job if the scan times out.                          |
| `OX_FAIL_ON_ERROR`         | Set to `true` to fail the job if an infrastructure or network error occurs.   |

## Advanced environment variables

| Variable                    | Description                                                                 |
| --------------------------- | --------------------------------------------------------------------------- |
| `OX_DISABLE_SSL_VALIDATION` | Disables SSL certificate validation for self-signed certs (on-premise use). |

### Integration Example (`bitbucket-pipelines.yml`)

```yaml
image: node:18

pipelines:
  pull-requests:
    main:
      - step:
          name: OX
          script:
            - export OX_BITBUCKET_FULL_COMMIT=$(git rev-parse --verify $BITBUCKET_COMMIT 2>/dev/null)
            - pipe: docker://oxsecurity/ox-block-mode
              variables:
                OX_API_KEY: $OX_API_KEY
                OX_BITBUCKET_FULL_COMMIT: $OX_BITBUCKET_FULL_COMMIT
                # OX_OVERRIDE_BLOCKING: false
                # OX_TIMEOUT: 20
                # OX_FAIL_ON_TIMEOUT: false
                # OX_FAIL_ON_ERROR: false
```

> **Note:** The `OX_BITBUCKET_FULL_COMMIT` variable is required for proper scan functionality. Bitbucket's default `BITBUCKET_COMMIT` may return a short SHA and cause issues in scan context detection.

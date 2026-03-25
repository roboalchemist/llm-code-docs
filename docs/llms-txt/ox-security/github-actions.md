# Source: https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration/github-actions.md

# GitHub Actions

OX Security integrates with GitHub Actions to detect vulnerabilities in your code or container images during CI/CD builds.

The OX GitHub Action runs a full security scan, covering secrets, SAST, SCA, IaC, and more, on every push or pull request, and evaluates the results against your defined security policies. If a blocking issue is detected, the workflow will fail unless overridden.

You can configure global or repository-specific policies in the OX platform to determine enforcement behavior.

This integration is highly customizable and supports any event trigger supported by GitHub Actions.

> When using pull request or push triggers in GitHub Actions, scans run automatically without needing manual webhook setup.

## Prerequisites

* A **GitHub repository** connected to your OX application.
* A valid **OX Security API key** stored as `OX_API_KEY` in your repository secrets.

## Required environment variables

| Input        | Description                                                                                                                                                                                                      |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ox_api_key` | [The OX Security API key.](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration/broken-reference) |

## Optional environment variables

| Input                  | Description                                                                  |
| ---------------------- | ---------------------------------------------------------------------------- |
| `ox_override_blocking` | Set to `true` to override blocking issues and allow the workflow to succeed. |
| `ox_timeout`           | Maximum scan duration in minutes. Defaults to `20`.                          |
| `ox_fail_on_timeout`   | Set to `true` to fail the job if the scan times out.                         |
| `ox_fail_on_error`     | Set to `true` to fail the job when network or system errors occur.           |

## Advanced environment variables

| Input                       | Description                                                                                         |
| --------------------------- | --------------------------------------------------------------------------------------------------- |
| `ox_disable_ssl_validation` | Set to `true` to disable SSL certificate validation (useful for self-signed or internal endpoints). |

## Integration Example (`.github/workflows/scan.yml`)

```yaml
name: Security Scan

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: OX Security Scan
        uses: oxsecurity/ox-security-scan@main
        with:
          ox_api_key: ${{ secrets.OX_API_KEY }}
          # ox_override_blocking: false
          # ox_timeout: 20
          # ox_fail_on_timeout: false
          # ox_fail_on_error: false
          # ox_disable_ssl_validation: false
```

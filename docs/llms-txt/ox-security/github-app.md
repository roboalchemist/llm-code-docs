# Source: https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/app-pipeline-integration/github-app.md

# GitHub App

OX Security supports pipeline scanning using the GitHub App, which uses GitHub webhooks to trigger scans.

This approach does not require modifying CI/CD configurations or adding the OX CLI to pipeline jobs. Instead, OX listens for GitHub events and initiates scans automatically.

OX detects pull requests and push events directly from GitHub. Based on the event, OX identifies the modified files and performs a scan.

The scan runs outside your pipeline and reports results in the OX UI. No CLI or container is needed inside your GitHub workflow.

## Prerequisites

* The GitHub App must be installed in your GitHub organization.
* [You must grant the app access to the repositories you want to scan.](https://docs.ox.security/get-started/onboarding-to-ox/source-control/github)

## Required Configuration

OX initiates scans using webhook data from GitHub. You do not need to add variables or modify settings. You just need to [make sure that webhooks are enabled.](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/webhooks-pipeline-integration)

# Source: https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/app-pipeline-integration/bitbucket-app.md

# Bitbucket App

OX Security supports integration with Bitbucket Cloud using the OX Bitbucket App.

This integration enables automatic pipeline scans triggered by events such as push and pull requests, without modifying your CI/CD pipeline configuration.

OX listens for push and pull request events from Bitbucket Cloud. When an event is detected, OX identifies the modified files and triggers a pipeline scan for the specific repository.

Scans run outside the Bitbucket pipeline and results are [displayed in the OX platform](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/understanding-pipeline-scan-results).

## Prerequisites

* Bitbucket Cloud account
* Admin access to your Bitbucket workspace
* The OX Bitbucket App is installed and authorized for your repositories

## Required Configuration

OX initiates scans using webhook data from BitBucket. You do not need to add variables or modify settings. You just need to [make sure that webhooks are enabled.](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/app-pipeline-integration/broken-reference)

**To connect to Bitbucket app:**

1. Go to the OX platform and navigate to **Connectors > Source Control**.
2. Select **Bitbucket App** and click **Connect**. You are redirected to Bitbucket.
3. Approve the OX Security app.
4. Select the repositories you want to monitor with OX. When connected, OX automatically receives webhook events and perform scans on changes.

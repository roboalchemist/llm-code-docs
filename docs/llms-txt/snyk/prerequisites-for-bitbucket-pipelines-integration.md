# Source: https://docs.snyk.io/developer-tools/snyk-ci-cd-integrations/bitbucket-pipelines-integration-using-a-snyk-pipe/prerequisites-for-bitbucket-pipelines-integration.md

# Prerequisites for Bitbucket Pipelines integration

The following are prerequisites for Bitbucket Pipelines integration:

* For your Bitbucket Pipelines, ensure you have build minutes in your account, which are necessary to enable ongoing CI/CD workflows.
* Create a Snyk account and retrieve the Snyk API token or Snyk PAT from your **Account settings**.
* Create a Repository variable from Bitbucket for your token. Call the variable SNYK\_TOKEN.
* If you supply a custom image, ensure it meets the [requirements](https://docs.snyk.io/developer-tools/user-defined-custom-images-for-cli#requirements-for-user-defined-custom-images-for-cli) for custom images

# Source: https://docs.snyk.io/developer-tools/snyk-ci-cd-integrations/bitbucket-pipelines-integration-using-a-snyk-pipe.md

# Bitbucket Pipelines integration using a Snyk pipe

Snyk integrates with Bitbucket Pipelines using a Snyk pipe, seamlessly scanning your application dependencies and Docker images for security vulnerabilities as part of the continuous integration/continuous delivery (CI/CD) workflow.

[Bitbucket Pipes](https://bitbucket.org/blog/meet-bitbucket-pipes-30-ways-to-automate-your-ci-cd-pipeline) enables users to customize and automate a Bitbucket Pipeline CI/CD workflow with a group of ready-to-use tasks that can be added inside of your pipelines by copying and pasting them from the Bitbucket interface.

With the Snyk pipe, you can quickly add Snyk scanning to your pipelines to test and monitor for vulnerabilities at different points in the CI/CD workflow, based on your configurations. Results are then displayed in the Bitbucket Pipelines output view and can also be monitored on the [Snyk Web UI](http://app.snyk.io).

## Snyk pipe information in Bitbucket

From the build directory, Bitbucket Pipelines displays a list of available pipes customized for you, similar to the list in the following screen image:

![Bitbucket Pipelines list of available pipes](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-fe9ba26ffd13739587c99ca411ea72b6874c309a%2Fuuid-6fff2668-6e2e-22ae-200f-124c8a240b02-en.png?alt=media\&token=19f94885-05c4-41b9-84d6-876b36ed6e03)

On this list, find and click **Snyk** to view the pipe, examples, parameters, and values:

![Snyk Scan pipe information](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-cc1bd37c0e6f0ee0f8c1bc4f043efb420264f88f%2Fmceclip0-25-.png?alt=media\&token=6b7c5bd7-4753-4996-9dc4-146ac80c7beb)

## Setup and use details

For setup and use details, see the following pages:

* [Language support for Bitbucket Pipelines integration](https://docs.snyk.io/developer-tools/snyk-ci-cd-integrations/bitbucket-pipelines-integration-using-a-snyk-pipe/language-support-for-bitbucket-pipelines-integration)
* [Bitbucket Pipelines integration: how it works](https://docs.snyk.io/developer-tools/snyk-ci-cd-integrations/bitbucket-pipelines-integration-using-a-snyk-pipe/bitbucket-pipelines-integration-how-it-works)
* [Prerequisites for Bitbucket Pipelines integration](https://docs.snyk.io/developer-tools/snyk-ci-cd-integrations/bitbucket-pipelines-integration-using-a-snyk-pipe/prerequisites-for-bitbucket-pipelines-integration)
* [Configure your Bitbucket Pipelines integration](https://docs.snyk.io/developer-tools/snyk-ci-cd-integrations/bitbucket-pipelines-integration-using-a-snyk-pipe/configure-your-bitbucket-pipelines-integration)
* [How to add a Snyk pipe](https://docs.snyk.io/developer-tools/snyk-ci-cd-integrations/bitbucket-pipelines-integration-using-a-snyk-pipe/how-to-add-a-snyk-pipe)
* [Snyk pipe parameters and values (Bitbucket Cloud)](https://docs.snyk.io/developer-tools/snyk-ci-cd-integrations/bitbucket-pipelines-integration-using-a-snyk-pipe/snyk-pipe-parameters-and-values-bitbucket-cloud)
* [Snyk pipe examples for Bitbucket Cloud](https://bitbucket.org/snyk/snyk-scan/src/develop/README.md)

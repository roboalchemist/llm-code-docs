# Source: https://docs.snyk.io/developer-tools/snyk-ci-cd-integrations/azure-pipelines-integration/simple-example-of-a-snyk-task-to-run-a-code-test.md

# Simple example of a Snyk task to run a code test

The following is a simple example of a Snyk task to run a Snyk Code test.

```
- task: SnykSecurityScan@1
  inputs:
    serviceConnectionEndpoint: 'snykToken'
    testType: 'code'
    codeSeverityThreshold: 'medium'
    failOnIssues: true
```

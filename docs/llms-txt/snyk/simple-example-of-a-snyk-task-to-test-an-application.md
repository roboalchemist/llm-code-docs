# Source: https://docs.snyk.io/developer-tools/snyk-ci-cd-integrations/azure-pipelines-integration/simple-example-of-a-snyk-task-to-test-an-application.md

# Simple example of a Snyk task to test an application

The following is a simple example of a Snyk task to test an application's open-source dependencies (SCA).

```
- task: SnykSecurityScan@1
  inputs:
    serviceConnectionEndpoint: 'snykToken'
    testType: 'app'
    monitorWhen: 'always'
    failOnIssues: true
```

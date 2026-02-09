# Source: https://docs.snyk.io/developer-tools/snyk-ci-cd-integrations/azure-pipelines-integration/simple-example-of-a-snyk-task-to-test-a-container-image.md

# Simple example of a Snyk task to test a container image

The following is a simple example of a Snyk task to test a container image.

```
- task: SnykSecurityScan@1
  inputs:
    serviceConnectionEndpoint: 'snykToken'
    testType: 'container'
    dockerImageName: 'goof'
    dockerfilePath: 'Dockerfile'
    monitorWhen: 'always'
    failOnIssues: true
```

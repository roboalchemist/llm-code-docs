# Source: https://kreya.app/docs/cli/integrations/azure.md

# Azure DevOps

The Kreya CLI can be used in Azure DevOps Pipelines to automatically test APIs with the kreyac docker image.

```
jobs:
  - job: Test
    pool:
      vmImage: 'ubuntu-latest'
    container: 'riok/kreyac:1'
    variables:
      KREYA_ENV_MySecret: $(MY_SECRET) # gets merged into the active Kreya environment as MySecret
    steps:
      - displayName: 'Run Kreya Operations'
        workingDirectory: './kreya' # Specify the directory where the Kreya project is stored in the repository. Omit this if it is located in the root directory.
        script: |
          kreyac info
          kreyac environment set-active Production                                                            # set the active environment
          kreyac operation invoke "REST/Get books.krop"                                                       # invoke a single REST operation by name
          kreyac operation invoke "gRPC/Say hello.krop"                                                       # invoke a single gRPC operation by name
          kreyac operation invoke "WebSocket/Echo.krop"                                                       # invoke a single WebSocket operation by name
          kreyac collection invoke "Kreya features/Collection/Collection.krcol" --test-report-junit junit.xml # invoke a collection and generate a JUnit report
      - task: PublishTestResults@2
        condition: always() # Ensures this task runs even if there was a test failure
        inputs:
          testResultsFormat: 'JUnit'
          testResultsFiles: './kreya/junit.xml'
          failTaskOnFailedTests: true
          testRunTitle: 'Kreya Tests'
```

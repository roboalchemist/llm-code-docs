# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/jfrog-evidence-collection.md

# JFrog Evidence Collection

The [JFrog Evidence Collection](https://jfrog.com/evidence/) expands JFrog’s Release Lifecycle Management capabilities to enrich artifacts, builds, and release bundles with signed attestation metadata that can be easily tracked and verified for governance and compliance.

SonarQube Cloud integrates with JFrog Evidence Collection to provide trusted auditing for software packages.

### Integration overview <a href="#integration-ove" id="integration-ove"></a>

The [JFrog CLI](https://docs.jfrog-applications.jfrog.io/jfrog-applications/jfrog-cli) is used within the CI pipeline to create the Sonar evidence that will be displayed on the JFrog platform. This evidence contains the quality gate status computed by SonarQube Cloud and made accessible via its API.

The figure below shows the process:

1. The CI pipeline starts the SonarQube analysis.
2. The SonarScanner performs the analysis and sends the results to SonarQube Cloud.
3. SonarQube Cloud processes the analysis results and computes the quality gate status.
4. The CI pipeline asks JFrog CLI to create the Sonar evidence for the analysis.
5. The JFrog CLI, which waits for the analysis completion, retrieves SonarQube analysis evidence payload from SonarQube Cloud's endpoint: [api.sonarcloud.io/dop-translation/jfrog-evidence](http://api.sonarcloud.io/dop-translation/jfrog-evidence/%7BtaskId%7D) (see the [#example-of-a-sonar-endpoint-response](#example-of-a-sonar-endpoint-response "mention") expandable below).

<figure><img src="broken-reference" alt="The JFrog CLI waits for the SonarQube Cloud analysis completion, retrieves SonarQube analysis evidence payload from SonarQube Cloud&#x27;s endpoint, creates the Sonar evidence, and sends it to JFrog Evidence Collection."><figcaption></figcaption></figure>

<details>

<summary>Example of a Sonar endpoint response</summary>

The endpoint response contains the evidence payload in JSON format with a markdown section.

```json
{
   "predicateType":"https://jfrog.com/evidence/sonarqube/v1",
   "predicate":{
      "projectStatus":{
         "status":"ERROR",
         "ignoredConditions":false,
         "caycStatus":"non-compliant",
         "conditions":[
            {
               "status":"ERROR",
               "metricKey":"new_coverage",
               "comparator":"LT",
               "errorThreshold":"85",
               "actualValue":"82.50562381034781"
            },
            {
               "status":"OK",
               "metricKey":"skipped_tests",
               "comparator":"GT",
               "actualValue":"0"
            }
         ],
         "period":{
            "mode":"last_version",
            "date":"2000-04-27T00:45:23+0200",
            "parameter":"2015-12-07"
         }
      }
   },
    "createdAt": "2222-01-01T00:00:00.000Z",
    "createdBy": "SonarQube",
    "markdown": "# SVG in Markdown example\n\n## Details\n\n- **Type**: svg examples\n\nThis demonstrates the syntax for embedding an SVG without a separate file.\n\n!"
}
```

</details>

### Prerequisites

* SonarQube Cloud Enterprise license
* JFrog Artifactory Enterprise+ license
* Minimum JFrog CLI version: 2.78.9

### Setting up the integration

You must set up your pipeline to use the JFrog CLI to create the Sonar evidence. See the [JFrog pipelines documentation](https://jfrog.com/help/r/jfrog-pipelines-documentation/jfrog-pipelines).

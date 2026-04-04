# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/ci-integration/jenkins-integration/pipeline-pause.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/ci-integration/jenkins-integration/pipeline-pause.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/ci-integration/jenkins-integration/pipeline-pause.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/ci-integration/jenkins-integration/pipeline-pause.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/ci-integration/jenkins-integration/pipeline-pause.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/ci-integration/jenkins-integration/pipeline-pause.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/ci-integration/jenkins-integration/pipeline-pause.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/ci-integration/jenkins-integration/pipeline-pause.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/ci-integration/jenkins-integration/pipeline-pause.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/ci-integration/jenkins-integration/pipeline-pause.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/ci-integration/jenkins-integration/pipeline-pause.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/ci-integration/jenkins-integration/pipeline-pause.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/jenkins/pipeline-pause.md

# Setting up a pipeline pause

Starting in the SonarQube Cloud Team plan, you can configure an automatic failing of your pipeline in case the quality gate fails (see the [#pipeline-interruption](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/key-features#pipeline-interruption "mention") article). To do so, you must set up a pipeline pause by using the `waitForQualityGate` step.

Proceed as follows:

1. Make sure the `withSonarQubeEnv` step is included in your pipeline so that the taskId is correctly attached to the pipeline context; see the [#pipeline-job](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/add-analysis-to-job#pipeline-job "mention") article.
2. Configure a webhook for your project in SonarQube Cloud pointing to `<yourJenkinsInstance>/sonarqube-webhook/`(This is the URL exposed by the Jenkins extension). You may use a webhook configured at the global level if applicable to your project. This step is mandatory (and cannot be performed in a Free plan organization)! For more information, check the [webhooks](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/webhooks "mention") page.
3. You may want to enable the verification of the quality gate payload sent to Jenkins by setting a webhook secret: see below.
4. Add a quality gate stage with `waitForQualityGate` to your Jenkins file as described below through examples.

### Adding a quality gate stage <a href="#add-quality-gate-stage" id="add-quality-gate-stage"></a>

This section gives examples of the adding of a quality gate stage to your Jenkins file with `waitForQualityGate`.

#### Scripted pipeline <a href="#scripted-pipeline" id="scripted-pipeline"></a>

Thanks to the webhook, the step is implemented in a very lightweight way: no need to occupy a node doing polling, and it doesn’t prevent Jenkins from restarting (the step will be restored after restart). Note that to prevent race conditions, when the step starts (or is restarted) a direct call is made to the server to check if the task is already completed.

<details>

<summary>Example</summary>

```groovy
 node {
  stage('SonarCloud analysis') {
    withSonarQubeEnv('SonarCloud') {
      sh 'mvn clean verify org.sonarsource.scanner.maven:sonar-maven-plugin:sonar'
    } // submitted taskId is automatically attached to the pipeline context
  }
}

// No need to occupy a node

stage("Quality Gate"){
  timeout(time: 1, unit: 'HOURS') { // Just in case something goes wrong, pipeline will be stopped after a timeout
    def qg = waitForQualityGate() // Reuse taskId previously collected by withSonarQubeEnv
    if (qg.status != 'OK') {
      error "Pipeline aborted due to quality gate failure: ${qg.status}"
    }
  }
}
```

</details>

#### Declarative pipeline <a href="#declarative-pipeline" id="declarative-pipeline"></a>

<details>

<summary>Example</summary>

```groovy
pipeline {
    agent any
    stages {
        stage('build && SonarCloud analysis') {
            steps {
                withSonarQubeEnv('SonarCloud') {
                    // Optionally use a Maven environment you've configured already
                    withMaven(maven:'Maven 3.5') {
                        sh 'mvn clean package org.sonarsource.scanner.maven:sonar-maven-plugin:sonar'
                    }
                }
            }
        }
        stage("Quality Gate") {
            steps {
                timeout(time: 1, unit: 'HOURS') {
                    // Parameter indicates whether to set pipeline to UNSTABLE if Quality Gate fails
                    // true = set pipeline to UNSTABLE, false = don't
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}
```

</details>

<details>

<summary>Multiple analyses in the same pipeline</summary>

If you want to run multiple analyses in the same pipeline and use waitForQualityGate you have to do everything in order as shown in the example below.

```groovy
pipeline {
    agent any
    stages {
        stage('SonarCloud analysis 1') {
            steps {
                sh 'mvn clean verify org.sonarsource.scanner.maven:sonar-maven-plugin:sonar'
            }
        }
        stage("Quality Gate 1") {
            steps {
                waitForQualityGate abortPipeline: true
            }
        }
        stage('SonarCloud analysis 2') {
            steps {
                sh 'gradle sonar'
            }
        }
        stage("Quality Gate 2") {
            steps {
                waitForQualityGate abortPipeline: true
            }
        }
    }
}
```

</details>

### Configuring a Webhook secret <a href="#webhook-secret" id="webhook-secret"></a>

If you want to verify the webhook payload that is sent to Jenkins, you can add a secret to your webhook on SonarQube Cloud.

To set the secret:

1. In Jenkins, navigate to **Manage Jenkins** > **Configure System** > **SonarQube Server** > **Advanced** > **Webhook Secret** and click the **Add** button.
2. Select **Secret text** and give the secret an ID.
3. Select the secret from the dropdown menu.

If you want to override the webhook secret on a project level, you can add the secret to Jenkins and then reference the secret ID when calling `waitForQualityGate` as follows:

<details>

<summary>Scripted pipeline</summary>

```groovy
waitForQualityGate webhookSecretId: 'yourSecretID'
```

</details>

<details>

<summary>Declarative pipeline</summary>

```groovy
waitForQualityGate(webhookSecretId: 'yourSecretID') 
```

</details>

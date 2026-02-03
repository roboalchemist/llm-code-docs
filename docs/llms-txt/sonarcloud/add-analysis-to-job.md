# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/ci-integration/jenkins-integration/add-analysis-to-job.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/ci-integration/jenkins-integration/add-analysis-to-job.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/ci-integration/jenkins-integration/add-analysis-to-job.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/ci-integration/jenkins-integration/add-analysis-to-job.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/ci-integration/jenkins-integration/add-analysis-to-job.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/ci-integration/jenkins-integration/add-analysis-to-job.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/ci-integration/jenkins-integration/add-analysis-to-job.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/ci-integration/jenkins-integration/add-analysis-to-job.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/ci-integration/jenkins-integration/add-analysis-to-job.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/ci-integration/jenkins-integration/add-analysis-to-job.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/ci-integration/jenkins-integration/add-analysis-to-job.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/ci-integration/jenkins-integration/add-analysis-to-job.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/jenkins/add-analysis-to-job.md

# Adding analysis to a Jenkins job

You can add the SonarQube Cloud analysis to your Jenkins Freestyle or Pipeline jobs and easily configure your project analysis with Jenkins through the in-product tutorial.

To be able to add a SonarQube Cloud analysis to a Jenkins job, Jenkins must have been set up for SonarQube Cloud integration. See the [global-setup](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/jenkins/global-setup "mention") page to learn more.

### Adding analysis to a Freestyle job <a href="#freestyle-job" id="freestyle-job"></a>

The procedure depends on the project type.

{% tabs %}
{% tab title="MAVEN OR GRADLE" %}

1. Create and configure your Jenkins job, and go to the **Build Environment** section.
2. Enable **Prepare SonarScanner environment** to allow the injection of SonarQube Cloud values into this particular job. Once the environment variables are available, use them in a standard Maven build step (**Invoke top-level Maven targets**) by setting the **Goals** to include, or a standard Gradle build step (**Invoke Gradle script**) by setting the **Tasks** to execute.

Maven goal:

```bash
SONAR_MAVEN_GOAL
```

Gradle task:

```bash
sonar
```

{% hint style="info" %}
In both cases, launching your analysis may require authentication. In that case, make sure that the global configuration in Jenkins of SonarQube Cloud defines a valid SonarQube Cloud token (see the [global-setup](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/jenkins/global-setup "mention") page).
{% endhint %}
{% endtab %}

{% tab title=".NET" %}

1. Create and configure your Jenkins job, and go to the **Build** section.
2. Add the **SonarQube for MSBuild - Begin Analysis** to your build.
3. Configure the SonarQube Cloud Project Key, Name, and Version in the **SonarScanner for MSBuild - Begin Analysis** build step.
4. Add the compatible **MSBuild build step** or the **Execute Windows batch command** to execute the build.
5. Add the **SonarQube for MSBuild - End Analysis** build steps to your build.

{% hint style="info" %}
In version 5.0 of the SonarScanner, we changed the name of the *SonarScanner for MSBuild* to *SonarScanner for .NET*.

The documentation is updated with the new name and we will call the scanner *SonarScanner for .NET* moving forward.
{% endhint %}
{% endtab %}

{% tab title="OTHER" %}

1. Create and configure your Jenkins job, and go to the **Build** section.
2. Add the SonarScanner CLI build step to your build.
3. Configure the analysis properties. You can either point to an existing `sonar-project.properties` file or set the analysis properties directly in the **Analysis properties** field.
   {% endtab %}
   {% endtabs %}

### Adding analysis to a Pipeline job <a href="#pipeline-job" id="pipeline-job"></a>

1. In Jenkins, create your Pipeline job.
2. Add the SonarQube Cloud analysis stage to the Jenkins file: see below.
3. [pipeline-pause](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/jenkins/pipeline-pause "mention") until the quality gate is computed.

### Adding analysis to a Multibranch Pipeline job <a href="#multibranch-pipeline" id="multibranch-pipeline"></a>

1. In Jenkins, create your Multibranch Pipeline job.
2. From your Jenkins job, go to **Configure** > **Branch Sources > Behaviors** and:
   1. Under **Discover branches**, make sure \*\*Exclude branches that are also filed as PRs (\*\*or **MRs)** is selected.
   2. Under \*\*Discover pull (\*\*or **merge) requests from origin**, make sure \*\*The current pull (\*\*or **merge) request revision** is selected.
   3. Under **Specify ref specs,** make sure the **Ref Spec value** will include any target branches (the default value should be enough).\
      If the **Specify ref specs** behavior is not active, click on **Add** and select **Specify ref specs.**
3. Add the SonarQube Cloud analysis stage to the Jenkins file: see below.
4. Set up a pipeline pause until the quality gate is computed. The [pipeline-pause](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/jenkins/pipeline-pause "mention") page has instructions.

### Adding an analysis stage to the Jenkins file <a href="#add-analysis-stage" id="add-analysis-stage"></a>

You must use the `withSonarQubeEnv` step in the SonarQube Cloud analysis stage of your pipeline job. This step is used to set the environment variables necessary to connect to SonarQube Cloud. The connection details are retrieved from the Jenkins global configuration.

The `withSonarQubeEnv`() method can take the following optional parameters:

* `installationName`(string): name of the SonarQube Cloud installation as configured in Jenkins.
* `credentialsId`(string): if you want to overwrite the credentials configured in the Jenkins global configuration.
* `envOnly`(boolean): set it to true if you only want the SonarQube Cloud environment variables to be expanded in the build context

#### Examples <a href="#examples" id="examples"></a>

Note that you don’t need to specify an SCM stage in your Jenkins Pipeline or Multibranch Pipeline job.

{% tabs %}
{% tab title="GRADLE" %}
Scripted pipeline example:

```groovy
node {
  stage('SonarCloud analysis') {
    withSonarQubeEnv() { // Will pick the global server connection you have configured
      sh './gradlew sonar'
    }
  }
}
```

{% endtab %}

{% tab title="MAVEN" %}
Scripted pipeline example:

```groovy
node {
  stage('SonarCloud analysis') {
    withSonarQubeEnv(credentialsId: 'f225455e-ea59-40fa-8af7-08176e86507a', installationName: 'SonarCloud') { // You can override the credential to be used
      sh 'mvn org.sonarsource.scanner.maven:sonar-maven-plugin:3.11.0.3922:sonar'
    }
  }
}
```

{% endtab %}

{% tab title=".NET" %}
Scripted pipeline example:

```groovy
node {
  stage('Build + SonarCloud analysis') {
    def sqScannerMsBuildHome = tool 'Scanner for .Net Framework'
    withSonarQubeEnv('SonarCloud') {
      bat "${sqScannerMsBuildHome}\\SonarScanner.MSBuild.exe begin /k:myKey"
      bat 'MSBuild.exe /t:Rebuild'
      bat "${sqScannerMsBuildHome}\\SonarScanner.MSBuild.exe end"
    }
  }
}
```

{% endtab %}

{% tab title="OTHER" %}
Scripted pipeline example:

```groovy
node {
  stage('SonarQube analysis') {
    def scannerHome = tool '<sonarqubeScannerInstallation>'; // must match the name of an actual scanner installation directory on your Jenkins build agent
    withSonarQubeEnv('SonarCloud') { 
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
}
```

Declarative pipeline example:

```groovy
pipeline {
  agent any
  stages {
    stage('SonarQube analysis') {
      steps {
        script {
            scannerHome = tool '<sonarqubeScannerInstallation>'// must match the name of an actual scanner installation directory on your Jenkins build agent
        }
        withSonarQubeEnv('SonarCloud') {
          sh "${scannerHome}/bin/sonar-scanner"
        }
      }
    }
  }
} 
```

{% endtab %}
{% endtabs %}

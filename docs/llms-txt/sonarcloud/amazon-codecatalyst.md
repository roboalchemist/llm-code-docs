# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/amazon-codecatalyst.md

# Amazon CodeCatalyst

{% hint style="warning" %}
**Deprecation notice**

On October 7th, 2025, AWS announced the retirement of CodeCatalyst. Starting November 7th, 2025, no new spaces can be created, and access is limited to existing customers. As a consequence, this tool won't be maintained anymore starting December 16th, 2025.

* Your code is built with Maven: run `org.sonarsource.scanner.maven:sonar-maven-plugin:3.11.0.3922:sonar` during the build (more info in the [sonarscanner-for-maven](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-maven "mention") documentation)
* Your code is built with Gradle: use the [sonarscanner-for-gradle](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-gradle "mention") during the build
* You want to analyze a .NET solution: follow our interactive tutorial for other CI's
* You want to analyze C and C++ code: rely on our [SonarQube Cloud Scan for C and C++](https://github.com/marketplace/actions/sonarcloud-scan-for-c-and-c) and look at [our sample C and C++ project](https://github.com/sonarsource-cfamily-examples?q=gh-actions-sc\&type=all\&language=\&sort=)
* Your code uses another language or ecosystem: use [sonarscanner-cli](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-cli "mention")
  {% endhint %}

To configure an analysis of your project in Amazon CodeCatalyst CI/CD, follow the SonarQube Cloud in-product tutorial when creating a new project. The tutorial will walk you through the precise steps to set up the analysis. Meanwhile, here's a summary of the basic steps you will follow:

* Define the `SONAR_TOKEN` environment variable in your repository by setting up a CodeCatalyst Secret. The `SONAR_TOKEN` identifies and authenticates you to SonarQube Cloud
* Define your main branch on SonarQube Cloud to match the one in your repository (for unbound projects only; see the [binding-with-dop](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/ressources-structure/binding-with-dop "mention") page)
* Set the essential analysis parameters, `sonar.projectKey`, `sonar.organization`, and `sonar.host.url`.The tutorial will be populated with the correct values for your specific account. These parameters are set differently depending on your project type:
  * In the `pom.xml` for Java Maven projects
  * In the `build.gradle` file for Java Gradle projects
  * In the SonarScanner command line for .NET projects
  * In the `sonar-project.properties` file for other types of projects. You can also add additional analysis parameters to further specify your analysis details (See the [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") page)
* Create the `.codecatalyst/workflows/build.yml` file that defines the steps of your build. In addition to the usual steps that build your project, you need to invoke the SonarScanner to perform the analysis of your code. This is done differently depending on your project type (detailed below)

### Creating a CodeCatalyst Secret <a href="#creating-a-codecatalyst-secret" id="creating-a-codecatalyst-secret"></a>

First of all, you need to go to your CodeCatalyst project, navigate to CI/CD → Secrets and create a new secret with the following details:

* In the Name field, enter `SONAR_TOKEN`
* In the Value field, enter the token you generated on SonarQube Cloud

### Defining your main branch <a href="#defining-your-main-branch" id="defining-your-main-branch"></a>

{% hint style="info" %}
This step is relevant to manual projects that are *not bound* to a repository on one of the supported DevOps platforms.
{% endhint %}

You then need to define your main branch on SonarQube Cloud to match the one in your repository.

To do this, go to the Branches page within your SonarQube Cloud project, and rename it to match the main branch of your repository.

### Analyzing a project <a href="#analyzing-a-project" id="analyzing-a-project"></a>

Create or update your `.codecatalyst/workflows/build.yaml` file.

The following example shows a base configuration to run a SonarQube Cloud analysis on all your branches. If you already have existing workflows, you can simply add some of these new steps to an existing one.

```yaml
Name: SonarCloudAnalysis
SchemaVersion: "1.0"

# Optional - Set automatic triggers.
Triggers:
  - Type: Push
# Required - Define action configurations.
Actions:
  SonarCloudScanAction:
    # Identifies the SonarCloud Scan Action. Do not modify this value, just the version if needed.
    Identifier: sonar/sonarcloud-scan@v1.0.7
    # Specifies the source and/or artifacts to pass to the action as input.
    Inputs:
      # Required
      Sources:
        - WorkflowSource # This specifies that the action requires this Workflow as a source
    Compute:
      Type: EC2
    # Defines the action's properties.
    Configuration:
      SonarToken: ${Secrets.SONAR_TOKEN}
```

Create a configuration file in the root directory of the project and name it `sonar-project.properties`.

```properties
sonar.projectKey=your-project-key
sonar.organization=your-organization-key

# This is the name and version displayed in the SonarCloud UI.
#sonar.projectName=csharp-my-app
#sonar.projectVersion=1.0

# Path is relative to the sonar-project.properties file. Replace "\" by "/" on Windows.
#sonar.sources=.
sonar.exclusions=venv/**

# Encoding of the source code. Default is default system encoding
#sonar.sourceEncoding=UTF-8
```

### Analyzing a Java project with Maven <a href="#analyzing-a-java-project-with-maven" id="analyzing-a-java-project-with-maven"></a>

Update your pom.xml file with the following properties:

```xml
<properties>
  <sonar.projectKey>your-project-key</sonar.projectKey>
  <sonar.organization>your-organization-key</sonar.organization>
  <sonar.host.url>https://sonarcloud.io</sonar.host.url>
</properties>
```

Create or update your `.codecatalyst/workflows/build.yaml` file.

The following is a base configuration to run a SonarQube Cloud analysis on all your branches. If you already have existing workflows, you can simply add some of these new steps to an existing one.

```yaml
Name: SonarCloudAnalysis
SchemaVersion: "1.0"

Triggers:
  - Type: PUSH
Actions:
  Analysis:
    Identifier: aws/build@v1.0.0
    Inputs:
      Sources:
        - WorkflowSource
      Variables:
      - Name: SONAR_TOKEN
        Value: ${Secrets.SONAR_TOKEN}
    Compute:
      Type: EC2

    Configuration:
      Steps:
        - Run: mvn verify org.sonarsource.scanner.maven:sonar-maven-plugin:sonar -Dsonar.branch.name=${WorkflowSource.BranchName}
```

### Analyzing a Java project with Gradle <a href="#analyzing-a-java-project-with-gradle" id="analyzing-a-java-project-with-gradle"></a>

Update your `build.gradle` file with the `org.sonarqube` plugin and its configuration:

```properties
plugins {
  id "org.sonarqube" version "4.2.1.3168"
}

sonar {
  properties {
    property "sonar.projectKey", "your-project-key"
    property "sonar.organization", "your-organization-key"
    property "sonar.host.url", "https://sonarcloud.io"
  }
}
```

Create or update your .`codecatalyst/workflows/build.yaml` file.

Here is a base configuration to run a SonarQube Cloud analysis on all your branches. If you already have existing workflows, you might want to just add some of these new steps to an existing one.

```yaml
Name: SonarCloudAnalysis
SchemaVersion: "1.0"

Triggers:
  - Type: PUSH
Actions:
  Analysis:
    Identifier: aws/build@v1.0.0
    Inputs:
      Sources:
        - WorkflowSource
      Variables:
      - Name: SONAR_TOKEN
        Value: ${Secrets.SONAR_TOKEN}
    Compute:
      Type: EC2

    Configuration:
      Steps:
        - Run: ./gradlew build sonar -Dsonar.branch.name=${WorkflowSource.BranchName}
```

### Analyzing a .NET solution <a href="#analyzing-a-net-solution" id="analyzing-a-net-solution"></a>

Create or update your `.codecatalyst/workflows/build.yaml` file.

The following is a base configuration to run a SonarQube Cloud analysis on all your branches. If you already have existing workflows, you might want to just add some of these new steps to an existing one.

```yaml
Name: SonarCloudAnalysis
SchemaVersion: "1.0"

Triggers:
  - Type: PUSH
Actions:
  Analysis:
    Identifier: aws/build@v1.0.0
    Inputs:
      Sources:
        - WorkflowSource
    Compute:
      Type: EC2

    Configuration:
      Steps:
        - Name: Install SonarCloud scanner
          Run: dotnet tool install --global dotnet-sonarscanner
        - Name: Build and analyze
          Run: |
            dotnet sonarscanner begin /k:"manualorgcc_dotnetcc" /o:"manualorgcc" /d:sonar.token="${Secrets.SONAR_TOKEN}" /d:sonar.host.url="https://sonarcloud.io"
            <insert_your_clean_build_command>
            dotnet sonarscanner end /d:sonar.token="${Secrets.SONAR_TOKEN}"
```

Replace <*insert\_your\_clean\_build\_command*> with the actual one.

### Failing the workflow when the SonarQube Cloud Quality Gate fails <a href="#failing-the-workflow-when-the-sonarcloud-quality-gate-fails" id="failing-the-workflow-when-the-sonarcloud-quality-gate-fails"></a>

In order for the workflow to fail in CodeCatalyst when the Quality Gate fails on the SonarQube Cloud side, the SonarScanner needs to wait for the report and Quality Gate status to be processed by SonarQube Cloud. To enable this feature, set the `sonar.qualitygate.wait=true` parameter in your workflow definition.

```groovy
(...)
    Configuration:
      Steps:
        - Run: mvn verify org.sonarsource.scanner.maven:sonar-maven-plugin:sonar -Dsonar.branch.name=${WorkflowSource.BranchName} -Dsonar.qualitygate.wait=true
```

You can also set the `sonar.qualitygate.timeout` property to a maximum amount of time (in seconds) that the SonarScanner should wait for a report to be processed. The default is 300 seconds. Reaching this timeout will count as a failure and stop the CodeCatalyst workflow.

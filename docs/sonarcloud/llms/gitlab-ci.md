# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/gitlab-ci.md

# GitLab CI

You can integrate SonarQube Cloud analysis into your GitLab CI pipeline.

{% hint style="info" %}
A GitLab runner with a [Docker executor](https://docs.gitlab.com/runner/executors/#docker-executor) is required.
{% endhint %}

### Add environment variables <a href="#add-environment-variables" id="add-environment-variables"></a>

#### Define the SONAR\_TOKEN environment variable <a href="#define-the-sonartoken-environment-variable" id="define-the-sonartoken-environment-variable"></a>

Generate a token with the Execute analysis permission. See:

* From the Team plan: [scoped-organization-tokens](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/scoped-organization-tokens "mention").
* With the Free plan: [managing-tokens](https://docs.sonarsource.com/sonarqube-cloud/managing-your-account/managing-tokens "mention").

In GitLab, go to Settings and then CI/CD Variables to add the following variable and make sure it is available for your project:

* In the Key field, enter `SONAR_TOKEN`
* In the Value field, enter the token you generated on SonarQube Cloud
* Tick the Masked checkbox (this will prevent GitLab from showing the token in your build logs)

#### Define the SONAR\_HOST\_URL environment variable <a href="#define-the-sonarhosturl-environment-variable" id="define-the-sonarhosturl-environment-variable"></a>

In GitLab, go to Settings and then CI/CD Variables to add the following variable and make sure it is available for your project. You can define it for each of your GitLab projects or only once on the parent GitLab group.

* In the Key field, enter `SONAR_HOST_URL`
* In the Value field, enter `https://sonarcloud.io`
* No need to select the Masked checkbox this time

### Create or update the gitlab-ci.yml file <a href="#create-or-update-the-gitlab-ciyml-file" id="create-or-update-the-gitlab-ciyml-file"></a>

Choose the build technology relevant to your project:

<details>

<summary>Gradle</summary>

```yaml
plugins {
  id "org.sonarqube" version "6.3.1.5724"
}

sonarqube {
  properties {
    property "sonar.projectKey", "<YourProjectKey>"
    property "sonar.organization", "<YourOrganizationKey>"
  }
}
```

Create or update your .gitlab-ci.yml file with the following content:

```yaml
variables:
 SONAR_USER_HOME: "${CI_PROJECT_DIR}/.sonar"  # Defines the location of the analysis task cache
 GIT_DEPTH: "0"  # Tells git to fetch all the branches of the project, required by the analysis task
sonarcloud-check:
 image: gradle:alpine
 cache:
   key: "${CI_JOB_NAME}"
   paths:
     - .sonar/cache
 script: gradle sonarqube
 rules:
    - if: $CI_COMMIT_REF_NAME == 'main' || $CI_PIPELINE_SOURCE == 'merge_request_event'
```

</details>

<details>

<summary>Maven</summary>

Update your pom.xml file with the following properties:

```xml
<properties>
   <sonar.projectKey>your-project-key-here</sonar.projectKey>
   <sonar.organization>your-sonarcloud-organization-key-here</sonar.organization>
 </properties>
```

Create or update your .gitlab-ci.yml file with the following content:

```yaml
variables:
  SONAR_USER_HOME: "${CI_PROJECT_DIR}/.sonar"  # Defines the location of the analysis task cache
  GIT_DEPTH: "0"  # Tells git to fetch all the branches of the project, required by the analysis task
sonarcloud-check:
  image: maven:3.9.3-eclipse-temurin-17
  cache:
    key: "${CI_JOB_NAME}"
    paths:
      - .sonar/cache
  script:
    - mvn verify org.sonarsource.scanner.maven:sonar-maven-plugin:sonar
  rules:
    - if: $CI_COMMIT_REF_NAME == 'main' || $CI_PIPELINE_SOURCE == 'merge_request_event'
```

</details>

<details>

<summary>Other (for JS, TS, Go, Python, PHP, …)</summary>

Create or update your .gitlab-ci.yml file with the following content.

```yaml
variables:
 SONAR_USER_HOME: "${CI_PROJECT_DIR}/.sonar"  # Defines the location of the analysis task cache
 GIT_DEPTH: "0"  # Tells git to fetch all the branches of the project, required by the analysis task
sonarcloud-check:
 image:
   name: sonarsource/sonar-scanner-cli:latest
   entrypoint: [""]
 cache:
   key: "${CI_JOB_NAME}"
   paths:
     - .sonar/cache
 script:
   - sonar-scanner
 rules:
    - if: $CI_COMMIT_REF_NAME == 'main' || $CI_PIPELINE_SOURCE == 'merge_request_event'
```

Create a `sonar-project.properties` file in the root directory of the project:

```properties
sonar.projectKey=your-project-key-here
sonar.organization=your-sonarcloud-organization-key-here

# This is the name and version displayed in the SonarQube Cloud UI.
# sonar.projectName=Sample Project
# sonar.projectVersion=1.0

# Path is relative to the sonar-project.properties file. Replace "\" by "/" on Windows.
# sonar.sources=.

# Encoding of the source code. Default is default system encoding
# sonar.sourceEncoding=UTF-8
```

</details>

<details>

<summary>.NET</summary>

Create or update your .gitlab-ci.yml file with the following content:

```yaml
sonarqube-check:
  image: mcr.microsoft.com/dotnet/sdk:latest
  variables:
    SONAR_USER_HOME: "${CI_PROJECT_DIR}/.sonar"  # Defines the location of the analysis task cache
    GIT_DEPTH: "0"  # Tells git to fetch all the branches of the project, required by the analysis task
  cache:
    key: "${CI_JOB_NAME}"
    paths:
      - .sonar/cache
  script: 
    - dotnet tool install --global dotnet-sonarscanner
    - export PATH="$PATH:$HOME/.dotnet/tools"
    - dotnet sonarscanner begin /k:"<YourProjectKey>" /o:"<YourOrganizationKey>" /d:sonar.token="$SONAR_TOKEN"
 #Replace <YourProjectKey> with your project key and <YourOrganizationKey> with your organization key
    - dotnet build
    - dotnet sonarscanner end /d:sonar.token="$SONAR_TOKEN"
  allow_failure: false
  only:
    - merge_requests
    - main
    - develop
```

</details>

#### Failing the pipeline job when the SonarQube Cloud Quality Gate fails <a href="#failing-the-pipeline-job-when-the-sonarqube-cloud-quality-gate-fails" id="failing-the-pipeline-job-when-the-sonarqube-cloud-quality-gate-fails"></a>

In order for the pipeline to stop on GitLab CI side when the Quality Gate fails on SonarQube Cloud side, the SonarScanner needs to wait for the report and Quality Gate status to be processed by SonarQube Cloud. To enable this feature, you can set the `sonar.qualitygate.wait=true` parameter in your sonar-project.properties or .gitlab-ci.yml file.

You can also set the `sonar.qualitygate.timeout` property to a maximum amount of time (in seconds) that the SonarScanner should wait for a report to be processed. The default is 300 seconds. Reaching this timeout will count as a failure and stop the GitLab CI pipeline.

It is also possible to allow a job to fail without impacting the rest of the CI suite with the `allow_failure: true` parameter of GitLab CI. The failing job won’t stop the pipeline but will be displayed as in a warning state.

### Merge request decoration <a href="#merge-request-decoration" id="merge-request-decoration"></a>

The decoration of your merge requests is automatically configured as soon as you import a project and set up your GitLab CI.

The same access token used for connecting your GitLab group to SonarQube Cloud is used to post comments on the merge request. It makes it all the more important to use a technical GitLab account to generate the token.

### Analyzing Monorepo Projects: Build Configuration <a href="#analyzing-monorepo-projects-build-configuration" id="analyzing-monorepo-projects-build-configuration"></a>

The example below shows how you could set up a yml file for multiple projects in a monorepo. If you want to analyze a monorepo that contains more than one project ensure that you specify the paths to each sub-project for analysis in your build file.

{% hint style="info" %}
To ensure that your monorepo works as expected, you need to build each project in the monorepo separately with a valid token. Each project of the monorepo can be configured with its own properties file. Gitlab only accepts one SONAR\_TOKEN (in the CI/CD Variables configuration) per Gitlab project so you do not need to pass tokens for each project within your monorepo.

See the section on environment variables at the top of this page for more information on setting up your token.
{% endhint %}

Below is a sample .gitlab-ci.yml file that assumes your build requires the Sonar Scanner CLI, see the examples above if your setup uses an alternative configuration.

```yaml
variables:
  SONAR_USER_HOME: "${CI_PROJECT_DIR}/.sonar"  # Defines the location of the analysis task cache
  GIT_DEPTH: "0"  # Tells git to fetch all the branches of the project, required by the analysis task


sonarcloud-check-project-1:
  image:
    name: sonarsource/sonar-scanner-cli:latest
    entrypoint: [""]
  cache:
    key: "${CI_JOB_NAME}"
    paths:
      - .sonar/cache
  script:
    - sonar-scanner -Dsonar.sources=project-1 -Dsonar.organization=... -Dsonar.projectKey=...
  rules:
    - if: $CI_COMMIT_REF_NAME == 'main' || $CI_PIPELINE_SOURCE == 'merge_request_event'

sonarcloud-check-project-2:
  image:
    name: sonarsource/sonar-scanner-cli:latest
    entrypoint: [""]
  cache:
    key: "${CI_JOB_NAME}"
    paths:
      - .sonar/cache
  script:
    - sonar-scanner -Dsonar.sources=project-2 -Dsonar.organization=... -Dsonar.projectKey=...
  rules:
    - if: $CI_COMMIT_REF_NAME == 'main' || $CI_PIPELINE_SOURCE == 'merge_request_event'
```

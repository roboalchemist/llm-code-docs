# Source: https://docs.sonarsource.com/sonarqube-community-build/devops-platform-integration/gitlab-integration/adding-analysis-to-gitlab-ci-cd.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/devops-platform-integration/gitlab-integration/adding-analysis-to-gitlab-ci-cd.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/devops-platform-integration/gitlab-integration/adding-analysis-to-gitlab-ci-cd.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/devops-platform-integration/gitlab-integration/adding-analysis-to-gitlab-ci-cd.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/devops-platform-integration/gitlab-integration/adding-analysis-to-gitlab-ci-cd.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/devops-platform-integration/gitlab-integration/adding-analysis-to-gitlab-ci-cd.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/devops-platform-integration/gitlab-integration/adding-analysis-to-gitlab-ci-cd.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/devops-platform-integration/gitlab-integration/adding-analysis-to-gitlab-ci-cd.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/devops-platform-integration/gitlab-integration/adding-analysis-to-gitlab-ci-cd.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/devops-platform-integration/gitlab-integration/adding-analysis-to-gitlab-ci-cd.md

# Source: https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/gitlab-integration/adding-analysis-to-gitlab-ci-cd.md

# Adding analysis to GitLab CI/CD pipeline

Once you have created your project in SonarQube, you can add the SonarQube analysis to your GitLab CI/CD pipeline:

1. Configure the project analysis parameters.
2. Add the analysis to your GitLab CI/CD pipeline.
3. Commit and push your code to start the analysis.

You can fail the pipeline when the quality gate fails (see below). If you use a monorepo, see [#monorepo](#monorepo "mention"). To manage other project-level features, see [setting-up-at-project-level](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/gitlab-integration/setting-up-at-project-level "mention").

For more information on configuring your build with GitLab CI/CD, see the [GitLab CI/CD configuration reference](https://docs.gitlab.com/ee/administration/cicd/).

{% hint style="info" %}
A GitLab runner with a [Docker executor](https://docs.gitlab.com/runner/executors/#docker-executor) is required.
{% endhint %}

### Configuring the project analysis parameters <a href="#configuring-analysis-parameters" id="configuring-analysis-parameters"></a>

For general information, see [analysis-parameters](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/analysis-parameters "mention") and the respective SonarScanner section: [sonarscanner-for-maven](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/sonarscanner-for-maven "mention"), [sonarscanner-for-gradle](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/sonarscanner-for-gradle "mention"), [using](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/dotnet/using "mention"), [sonarscanner](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/sonarscanner "mention"), and [configuring](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/npm/configuring "mention").

With GitLab CI/CD, you can securely set `sonar.token` and `sonar.host.url` properties through [CI/CD variables](https://docs.gitlab.com/ee/ci/variables/#creating-a-custom-environment-variable): see **Setting the authentication to the SonarQube Server** below.

In addition, starting from the [Developer edition](https://www.sonarsource.com/plans-and-pricing/developer/), SonarScanners running in GitLab CI/CD can automatically detect branches and merge requests being built so you don’t need to specifically pass them as parameters to the scanner. See [introduction](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/branch-analysis/introduction "mention") to branch analysis and [introduction](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/pull-request-analysis/introduction "mention") to pull request analysis for more information.

### Configuring your .gitlab-ci-yml file <a href="#configuring-yml-file" id="configuring-yml-file"></a>

This section shows you how to configure your GitLab CI/CD .gitlab-ci.yml file. The `allow_failure` parameter in the examples allows a job to fail without impacting the rest of the CI suite.

By default, GitLab will build all branches but not merge requests. To build merge requests, you need to use rules in your .gitlab-ci.yml. See the example configurations below for more information.

Select the scanner you’re using below to expand an example configuration:

<details>

<summary>SonarScanner for Gradle</summary>

```yaml
sonarqube-check:
  image: gradle:8.10.0-jdk17-jammy
  variables:
    SONAR_USER_HOME: "${CI_PROJECT_DIR}/.sonar"  # Defines the location of the analysis task cache
    GIT_DEPTH: "0"  # Tells git to fetch all the branches of the project, required by the analysis task
  cache:
    key: "${CI_JOB_NAME}"
    paths:
      - .sonar/cache
  script: gradle sonarqube -Dsonar.qualitygate.wait=true
  allow_failure: false
  rules:
    - if: $CI_COMMIT_REF_NAME == 'main' || $CI_PIPELINE_SOURCE == 'merge_request_event'
```

</details>

<details>

<summary>SonarScanner for Maven</summary>

```yaml
sonarqube-check:
  image: maven:3.9.3-eclipse-temurin-17
  variables:
    SONAR_USER_HOME: "${CI_PROJECT_DIR}/.sonar"  # Defines the location of the analysis task cache
    GIT_DEPTH: "0"  # Tells git to fetch all the branches of the project, required by the analysis task
  cache:
    key: "${CI_JOB_NAME}"
    paths:
      - .sonar/cache
  script:
    - mvn org.sonarsource.scanner.maven:sonar-maven-plugin:sonar-Dsonar.qualitygate.wait=true
  allow_failure: false
  rules:
    - if: $CI_COMMIT_REF_NAME == 'main' || $CI_PIPELINE_SOURCE == 'merge_request_event'
```

</details>

<details>

<summary>SonarScanner CLI</summary>

```yaml
sonarqube-check:
  image:
    name: sonarsource/sonar-scanner-cli:latest
    entrypoint: [""]
  variables:
    SONAR_USER_HOME: "${CI_PROJECT_DIR}/.sonar"  # Defines the location of the analysis task cache
    GIT_DEPTH: "0"  # Tells git to fetch all the branches of the project, required by the analysis task
  cache:
    key: "${CI_JOB_NAME}"
    paths:
      - .sonar/cache
  script:
    - sonar-scanner -Dsonar.qualitygate.wait=true
  allow_failure: false
  rules:
    - if: $CI_COMMIT_REF_NAME == 'main' || $CI_PIPELINE_SOURCE == 'merge_request_event'
```

**Project key**\
A project key has to be provided through `sonar-project.properties` or through the command line parameter. For more information, see the [sonarscanner](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/sonarscanner "mention") documentation.

**Self-signed certificates**\
If you secure your SonarQube Server instance with a self-signed certificate, you may need to build a custom image based on `sonarsource/sonar-scanner-cli`. See the section **Advanced docker configuration** within the [sonarscanner](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/sonarscanner "mention") documentation.

</details>

<details>

<summary>SonarScanner for .NET</summary>

Configure your .gitlab-ci.yml file for .NET.

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
      - "dotnet tool install --global dotnet-sonarscanner"
      - "export PATH=\"$PATH:$HOME/.dotnet/tools\""
      - "dotnet sonarscanner begin /k:\"projectKey" /d:sonar.token=\"$SONAR_TOKEN\" /d:\"sonar.host.url=$SONAR_HOST_URL\" "  #Replace "projectKey" with your project key
      - "dotnet build"
      - "dotnet sonarscanner end /d:sonar.token=\"$SONAR_TOKEN\""
  allow_failure: false
  only:
    - merge_requests
    - main
    - develop
```

</details>

{% hint style="info" %}
For C/C++/Objective-C configuration examples, you can refer to the [sonarsource-cfamily-examples](https://github.com/orgs/sonarsource-cfamily-examples/repositories?q=sq+gitlab) repository.
{% endhint %}

{% hint style="warning" %}
The errors "*Missing blame information…*" and "*Could not find ref…*" can be caused by checking out with a partial or shallow clone, or when using Git submodules. You should disable git shallow clone to make sure the scanner has access to all of your history when running analysis with GitLab CI/CD.

For more information, see [Git shallow clone](https://docs.gitlab.com/ee/user/project/repository/monorepos/#shallow-cloning).
{% endhint %}

### Failing the pipeline when the quality gate fails <a href="#failing-pipeline" id="failing-pipeline"></a>

You can configure the SonarScanner to wait for the quality gate result. This setting will force the pipeline to fail if the quality gate fails.

To do so:

1. Set the `sonar.qualitygate.wait` analysis parameter to `true`.
2. You can set the `sonar.qualitygate.timeout` analysis parameters to the number of seconds that the scanner should wait for a report to be processed. The default is 300 seconds.

See the configuration examples in [#configuring-yml-file](#configuring-yml-file "mention")file above.

### If you use a monorepo <a href="#monorepo" id="monorepo"></a>

The monorepo feature is supported starting in the [Enterprise edition](https://www.sonarsource.com/plans-and-pricing/enterprise/) provided the GitLab integration with SonarQube Server has been properly set up, see [global-setup](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/gitlab-integration/global-setup "mention") for more details.

To add the SonarQube Server analysis to your GitLab’s monorepo CI/CD pipeline:

1. If not already done, create the SonarQube Server projects related to your monorepo: see [monorepos](https://docs.sonarsource.com/sonarqube-server/project-administration/monorepos "mention").
2. For each project, set up integration features: see [setting-up-at-project-level](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/gitlab-integration/setting-up-at-project-level "mention").
3. For each project in the monorepo:
   * Set up the authentication to SonarQube Server (`sonar.token` and `sonar.host.url` properties). See the [#setting-up-the-authentication-to-the-sonarqube-server](#setting-up-the-authentication-to-the-sonarqube-server "mention") expandable below, for instructions.
   * Set the other necessary analysis parameters; see the [#configuring-analysis-parameters](#configuring-analysis-parameters "mention") article above for details. The mandatory parameter is: `sonar.projectKey` property.
4. Add a CI/CD YAML syntax reference ( .gitlab-ci.yml) in the home directory of the monorepo: Define a job for each monorepo project in .gitlab-ci.yml.
5. You can fail the pipeline when the quality gate fails: see above.

<details>

<summary>Setting up the authentication to the SonarQube Server</summary>

You have to create the Sonar tokens used to authenticate to the SonarQube Server during the analysis of the monorepo projects and store them securely in the pipeline environment. You can either use one single global-level token for the monorepo or use a project-level token for each project in the monorepo. Note that the user account used to generate the token must have the Execute analysis permission.

Proceed as follows:

1. Generate your tokens in SonarQube Server, see [managing-tokens](https://docs.sonarsource.com/sonarqube-server/user-guide/managing-tokens "mention"):
   * For project tokens, create a token for each project (you need the Administer permission on the project): Go to the Security page of your SonarQube Server account and create a Project analysis token.
   * For a global token, ask your administrator (The procedure is similar but you need the global Administer system permission.).
2. Create a [custom environment variable](https://docs.gitlab.com/ee/ci/variables/) in GitLab and set the Key as follows:
   * If you use a global token: enter `SONAR_TOKEN`.
   * Otherwise: enter `SONAR_TOKEN_1` (or another unique identifier within the monorepo) for the token of your first project in the monorepo
3. In the Value field, enter the corresponding token value.
4. If you use project-level tokens, repeat steps 2 to 3 for each additional project in the monorepo.
5. Create a custom environment variable in GitLab with:
   * Key: `SONAR_HOST_URL`
   * Value: `SonarQube Server URL`

</details>

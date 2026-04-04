# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/github-actions-for-sonarcloud.md

# Github Actions

To configure an analysis of your project using GitHub Actions, you will use the SonarQube Scan GitHub Action.

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

From SonarQube Scan GitHub Action version 5.0.0 (`sonarqube-scan-action`):

* If your runner is [GitHub-hosted](https://docs.github.com/en/actions/using-github-hosted-runners/using-github-hosted-runners/about-github-hosted-runners), all required utilities should be already provided by default.
* If your runner is [self-hosted](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners), you need to ensure that the following utilities are installed and available in the `PATH`: `unzip`, `wget` or `curl`.

<details>

<summary>in v7, the SonarQube Scan GitHub Action uses Scanner CLI v8</summary>

The SonarQube Scan GitHub Action version 7 uses the Scanner CLI v8. Please see this [release note for the SonarQube Scan GitHub Action](https://github.com/SonarSource/sonarqube-scan-action/releases/tag/v7.0.0).

* The main change on Scanner CLI v8 is related to the embedded JRE version which is now Java 21. Please see [this release note for the SonarScanner CLI](https://github.com/SonarSource/sonar-scanner-cli/releases/tag/8.0.0.6341).&#x20;

</details>

<details>

<summary>In v6, the SonarQube Scan GitHub Action handles arguments differently</summary>

The `args` input is parsed differently in `v6`. When updating to `v6`, you might have to update your workflow to change how arguments are quoted. See [this release note](https://github.com/SonarSource/sonarqube-scan-action/releases/tag/v6.0.0) for more information.

</details>

<details>

<summary>In v5, SonarQube Scan GitHub Action is not based on Docker</summary>

`v3.1.0` and below of the GitHub Action are based on Docker: at every execution of the action, a dedicated docker container is spawned.

The advantage of using container are primarily:

* **isolation**, since the SonarScanner gets only access to the directory where the project is checked out
* **full control of the environment** where the SonarScanner is executed, in terms of required utilities such as `wget` and `keytool`

The use of Docker comes, however, with multiple disadvantages:

* issues with analyzers requiring access to a system-level directories, such as cache of dependencies in Java or Dart
* issues with DockerHub rate limit on peak workload scenarios
* requirement by GitHub to run as root user
* support for Docker-based actions limited to Linux - no Windows nor MacOS

`v5` doesn't have the Docker dependency, making the action [composite](https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-composite-action). The action now runs in the environment of the runner executing the GitHub workflow.

</details>

### Analysis setup overview

You should follow the in-product tutorial when creating a new project. When it’s time to **Choose your Analysis Method** during setup, simply select **With GitHub Actions**. You can also access the tutorials for an existing project by going to *Your Project* > **Administration** > **Analysis Method**.

The tutorial will walk you through the precise steps to set up the analysis but the basic steps are these:

1. Define the `SONAR_TOKEN` environment variable in your repository by setting up a GitHub Secret. The `SONAR_TOKEN` identifies and authenticates you to SonarQube Cloud. The tutorial will provide the precise value for your specific account. To generate the token, see:
   * From the Team plan: [scoped-organization-tokens](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/scoped-organization-tokens "mention").
   * With the Free plan: [managing-tokens](https://docs.sonarsource.com/sonarqube-cloud/managing-your-account/managing-tokens "mention").
2. Set the essential analysis parameters, `sonar.projectKey`, `sonar.organization`, and `sonar.host.url`. The tutorial will be populated with the correct values for your specific account. These parameters are set differently depending on your project type:
   * In the `pom.xml` for Java Maven projects.
   * In the `build.gradle` file for Java Gradle projects.
   * In the SonarScanner command line for .NET projects.
   * In the `sonar-project.properties` file for other types of projects. You can also add additional analysis parameters to further specify your analysis details (See the [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") page).
3. Create the `.github/workflows/build.yml` file that defines the steps of your build. In addition to the usual steps that build your project, you need to invoke the SonarScanner to perform the analysis of your code. This is done differently depending on your project type:
   * A Maven plugin for Java Maven projects.
   * A Gradle plugin for Java Gradle projects.
   * A dedicated .NET scanner for .NET projects.
   * The SonarQube Cloud GitHub Action for other projects. The tutorial will provide the specific details for your project type.

The example below shows how you could set up a yml file for a single project.

### Setting up your workflow file

The workflow, usually declared in `.github/workflows/build.yml`, looks something like this:

```yaml
name: My Test Single Project
on:
  push:
    branches:
      - main
  pull_request:
    types: [opened, synchronize, reopened]
jobs:
  sonarqube:
    name: SonarQube
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0  
      - name: SonarQubeScan
        uses: SonarSource/sonarqube-scan-action@v7
        env: 
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
```

Users have reported that when working with GitHub Actions reusable workflows, your `SONAR_TOKEN` is *not intrinsically* passed to the reusable workflow. Even though your `SONAR_TOKEN` is defined in the source repository, GitHub Actions will output the `SONAR_TOKEN` value with asterisks (which make it look like it is working as expected), when in fact it is not reusing the value.

When setting up your GitHub reusable workflow, we recommend using the [GitHub feature](https://docs.github.com/en/actions/using-workflows/reusing-workflows#using-inputs-and-secrets-in-a-reusable-workflow) **secret: inherit** to completely remove the intrinsic sending of your `SONAR_TOKEN`.

For C, C++, and Objective-C projects relying on Build Wrapper to generate the compilation database (see the CFamily [prerequisites](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/c-family/prerequisites "mention") page), use the `sonarqube-scan-action/install-build-wrapper` sub-action to install the Build Wrapper.

### Failing the workflow when the quality gate fails <a href="#failing-workflow-on-quality-gate-failure" id="failing-workflow-on-quality-gate-failure"></a>

SonarQube Cloud adds the quality gate status as a GitHub check. You can define a branch protection rule on your branch in GitHub and add this check to the [required status checks before merging](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches#require-status-checks-before-merging). This way, users won’t be able to merge a pull request into the protected branch as long as the quality gate status is red.

### Analyzing Monorepo Projects: Build Configuration <a href="#analyzing-monorepo-projects-build-configuration" id="analyzing-monorepo-projects-build-configuration"></a>

The example below shows how you could set up a yml file for multiple projects in a monorepo. If you want to analyze a monorepo that contains more than one project ensure that you specify the paths to each sub-project for analysis in your build file.

To ensure that your monorepo works as expected, you need to build each project in the monorepo separately with a unique project key for each one.

**GitHub Actions .yml file**

```yaml
name: My Test Monorepo Project
on:
  push:
      branches:
      - main
      paths:
      - 'lambdas/test/**'
  pull_request:
    types: [opened, synchronize, reopened]
jobs:
  sonarqubeScan1:
    name: SonarQubeScan1
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0  
      - name: SonarQube Scan
        uses: SonarSource/sonarqube-scan-action@v7
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
        with:
          projectBaseDir: repo1/
          
  sonarqubeScan2:
    name: SonarQubeScan2
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0  
      - name: SonarQube Scan
        uses: SonarSource/sonarqube-scan-action@v7
        env: 
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
        with:
          projectBaseDir: repo2/
```

### Managing certificates for the SonarQube Cloud scan GitHub Action <a href="#certificate-sonarqube-scan-action" id="certificate-sonarqube-scan-action"></a>

If you use the [sonarqube-scan-action](https://github.com/SonarSource/sonarqube-scan-action) for your GitHub Action and SonarQube Cloud is behind a secured proxy with certificates that need to be recognized by the GitHub runner, you’ll need to set the `SONAR_ROOT_CERT` environment variable in GitHub.

### Troubleshooting <a href="#tbs" id="tbs"></a>

#### Scanner cannot resolve file paths in test coverage report <a href="#scanner-cannot-resolve-file-paths-in-test-coverage-report" id="scanner-cannot-resolve-file-paths-in-test-coverage-report"></a>

When using GitHub Action, the SonarScanner fails to resolve the paths within the test coverage report and raises the warning "Could not resolve \<n> file paths in \<file>".

You may resolve this problem by switching off `relative_paths=True` in the coverage settings.

#### "Container action is only supported on Linux" error <a href="#container-action-is-only-supported-on-linux-error" id="container-action-is-only-supported-on-linux-error"></a>

You may encounter this error if you use the SonarQube Scan GitHub Action before version 4, i.e. `sonarcloud-github-action`. This action is based on Docker and is only supported on Linux runners. In that case, move to `sonarqube-scan-action` (see [#prerequisites](#prerequisites "mention")).

#### "Container action is only supported on Linux" error <a href="#container-action-is-only-supported-on-linux-error" id="container-action-is-only-supported-on-linux-error"></a>

You may encounter this error if you use the SonarQube Scan GitHub Action before version 4, i.e. `sonarcloud-github-action`. This action is based on Docker and is only supported on Linux runners. In that case, move to `sonarqube-scan-action` (see *Preqrequisites* above).

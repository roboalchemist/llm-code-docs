# Source: https://docs.sonarsource.com/sonarqube-community-build/devops-platform-integration/github-integration/adding-analysis-to-github-actions-workflow.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/devops-platform-integration/github-integration/adding-analysis-to-github-actions-workflow.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/devops-platform-integration/github-integration/adding-analysis-to-github-actions-workflow.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/devops-platform-integration/github-integration/adding-analysis-to-github-actions-workflow.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/devops-platform-integration/github-integration/adding-analysis-to-github-actions-workflow.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/devops-platform-integration/github-integration/adding-analysis-to-github-actions-workflow.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/devops-platform-integration/github-integration/adding-analysis-to-github-actions-workflow.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/devops-platform-integration/github-integration/adding-analysis-to-github-actions-workflow.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/devops-platform-integration/github-integration/adding-analysis-to-github-actions-workflow.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/devops-platform-integration/github-integration/adding-analysis-to-github-actions-workflow.md

# Source: https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/github-integration/adding-analysis-to-github-actions-workflow.md

# Adding analysis to GitHub Actions workflow

Once you have create your project in SonarQube Server, you can add the SonarQube Server analysis to your GitHub Actions workflow:

1. Configure the project analysis parameters.
2. Add the analysis to your GitHub Actions workflows.
3. Commit and push your code to start the analysis.

If you use a monorepo, see the section [#monorepo](#monorepo "mention"), below.

<details>

<summary>Considerations about upgrading to GitHub Action v7</summary>

The SonarQube Scan GitHub Action version 7 uses the Scanner CLI v8. Please see this [release note for the SonarQube Scan GitHub Action](https://github.com/SonarSource/sonarqube-scan-action/releases/tag/v7.0.0).

* The main change on Scanner CLI v8 is related to the embedded JRE version which is now Java 21. Please see [this release note for the SonarScanner CLI](https://github.com/SonarSource/sonar-scanner-cli/releases/tag/8.0.0.6341).

</details>

<details>

<summary>Considerations about upgrading to GitHub Action v6</summary>

When updating to SonarQube Scan GitHub action `v6`, you might have to update your workflow to change how arguments are quoted because the `args` input is parsed differently. See [this release note](https://github.com/SonarSource/sonarqube-scan-action/releases/tag/v6.0.0) for more information.

</details>

<details>

<summary>Considerations about upgrading to GitHub Action v5</summary>

`v3.1.0` and below of the GitHub Action are based on Docker: at every execution of the action, a dedicated docker container is spawned.

The advantage of using container are primarily:

* **Isolation**, since the SonarScanner gets only access to the directory where the project is checked out.
* **Full control of the environment** where the SonarScanner is executed, in terms of required utilities such as `wget` and `keytool`.

The use of Docker comes, however, with multiple disadvantages regarding SonarQube analysis:

* Issues with analyzers requiring access to a system-level directory, such as cache of dependencies in Java or Dart.
* Issues with DockerHub rate limit on peak workload scenarios.
* Requirement by GitHub to run as root user.
* Support for Docker-based actions limited to Linux - no support of Windows nor MacOS.

`v5` doesn't have the Docker dependency, making the action [composite](https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-composite-action). The action now runs in the environment of the runner executing the GitHub workflow.

</details>

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

<details>

<summary>From GitHub Action version v5</summary>

* If your runner is [GitHub-hosted](https://docs.github.com/en/actions/using-github-hosted-runners/using-github-hosted-runners/about-github-hosted-runners), all required utilities should be already provided by default.
* If your runner is [self-hosted](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners), ensure that the following utilities are installed and available in the `PATH`: `unzip`, `wget` or `curl`.

</details>

<details>

<summary>If your SonarQube uses certificates</summary>

If you use the [sonarqube-scan-action](https://github.com/SonarSource/sonarqube-scan-action) for your GitHub Action and your SonarQube Server has certificates that need to be recognized by the GitHub runner, you’ll need to set the `SONAR_ROOT_CERT` environment variable in GitHub , see [manage-tls-certificates](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/scanner-environment/manage-tls-certificates "mention") for more information.

</details>

### Configuring the project analysis parameters <a href="#analysis-parameters" id="analysis-parameters"></a>

For general information, see [analysis-parameters](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/analysis-parameters "mention") and the respective SonarScanner section: [sonarscanner-for-maven](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/sonarscanner-for-maven "mention"), [sonarscanner-for-gradle](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/sonarscanner-for-gradle "mention"), [using](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/dotnet/using "mention") for .NET, the [sonarscanner](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/sonarscanner "mention"), or the [configuring](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/npm/configuring "mention") for NPM pages.

Specific to GitHub Actions is the setting of `sonar.token` and `sonar.host.url`: With GitHub Actions, you can configure these parameters in GitHub. This may be done at the global level by the system administrator, or at the project level by the Project Administrator as explained below . It makes sense to store the server URL at the global level.

In addition, starting from the [Developer edition](https://www.sonarsource.com/plans-and-pricing/developer/), SonarScanners running in GitHub Actions can automatically detect branches and pull requests being built so you don’t need to specifically pass them as parameters to the scanner. See [introduction](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/branch-analysis/introduction "mention") to branch analysis and [introduction](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/pull-request-analysis/introduction "mention") to pull request analysis for more information.

#### Storing the authentication token in GitHub for your project <a href="#storing-the-authentication-token-in-github-for-your-project" id="storing-the-authentication-token-in-github-for-your-project"></a>

The authentication token used in GitHub Actions workflows should be securely stored in a GitHub secret: see GitHub’s documentation on [Encrypted secrets](https://docs.github.com/en/actions/reference/encrypted-secrets) for more information.

Proceed as follows

1. In the SonarQube Community Build UI, generate a SonarQube Community Build token for your project.
2. Create a repository secret in GitHub with:
   * Name: SONAR\_TOKEN
   * Value: the token you generated in the previous step.

#### Storing the SonarQube Server URL in GitHub for your project <a href="#storing-the-sonarqube-server-url-in-github-for-your-project" id="storing-the-sonarqube-server-url-in-github-for-your-project"></a>

Create an [organization variable](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/store-information-in-variables) in GitHub with:

* Name: SONAR\_HOST\_URL
* Value: SonarQube Server URL

### Configuring the build.yml file <a href="#configure-build-yml" id="configure-build-yml"></a>

This section shows you how to configure your `.github/workflows/build.yml` file.

GitHub Actions can build specific branches and pull requests if you use `on.push.branches` and `on.pull-requests` configurations as shown in the examples below.

Click the scanner you’re using below to expand the example configuration:

{% hint style="warning" %}
The errors "*Missing blame information…*" and "*Could not find ref…*" can be caused by checking out with a partial or shallow clone, or when using Git submodules. You should disable git shallow clone to make sure the scanner has access to all of your history when running analysis with GitHub Actions.

For more information, see the [GitHub Actions Checkout README](https://github.com/actions/checkout).
{% endhint %}

<details>

<summary>SonarScanner for Gradle</summary>

**Note:** A project key might have to be provided through a `build.gradle` file, or through the command line parameter. For more information, see the [sonarscanner-for-gradle](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/sonarscanner-for-gradle "mention") documentation.

Add the following to your `build.gradle` file:

```yaml
plugins {
  id "org.sonarqube" version "<FULL_VERSION_NUMBER>"
}
```

We recommend using the latest version of [SonarScanner for Gradle](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/sonarscanner-for-gradle).

Write the following in your workflow YAML file:

```yaml
name: Build
on:
  push:
    branches:
      - main # the name of your main branch
  pull_request:
    types: [opened, synchronize, reopened]
jobs:
  build:
    name: Build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0  # Shallow clones should be disabled for a better relevancy of analysis
      - name: Set up JDK 17
        uses: actions/setup-java@v1
        with:
          java-version: 17
      - name: Cache SonarQube packages
        uses: actions/cache@v4
        with:
          path: ~/.sonar/cache
          key: ${{ runner.os }}-sonar
          restore-keys: ${{ runner.os }}-sonar
      - name: Cache Gradle packages
        uses: actions/cache@v4
        with:
          path: ~/.gradle/caches
          key: ${{ runner.os }}-gradle-${{ hashFiles('**/*.gradle') }}
          restore-keys: ${{ runner.os }}-gradle
      - name: Build and analyze
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
          SONAR_HOST_URL: ${{ vars.SONAR_HOST_URL }}
        run: ./gradlew build sonar --info
```

</details>

<details>

<summary>SonarScanner for Maven</summary>

**Note:** A project key might have to be provided through the command line parameter. For more information, see the [sonarscanner-for-maven](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/sonarscanner-for-maven "mention") documentation.

Write the following in your workflow YAML file:

```yaml
name: Build
on:
  push:
    branches:
      - main # the name of your main branch
  pull_request:
    types: [opened, synchronize, reopened]
jobs:
  build:
    name: Build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0  # Shallow clones should be disabled for a better relevancy of analysis
      - name: Set up JDK 17
        uses: actions/setup-java@v1
        with:
          java-version: 17
      - name: Cache SonarQube packages
        uses: actions/cache@v4
        with:
          path: ~/.sonar/cache
          key: ${{ runner.os }}-sonar
          restore-keys: ${{ runner.os }}-sonar
      - name: Cache Maven packages
        uses: actions/cache@v4
        with:
          path: ~/.m2
          key: ${{ runner.os }}-m2-${{ hashFiles('**/pom.xml') }}
          restore-keys: ${{ runner.os }}-m2
      - name: Build and analyze
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
          SONAR_HOST_URL: ${{ vars.SONAR_HOST_URL }}
        run: mvn -B verify org.sonarsource.scanner.maven:sonar-maven-plugin:sonar
```

</details>

<details>

<summary>SonarScanner for .NET</summary>

Write the following in your workflow YAML file:

```yaml
name: Build
on:
  push:
    branches:
      - main # the name of your main branch
  pull_request:
    types: [opened, synchronize, reopened]
jobs:
  build:
    name: Build
    runs-on: windows-latest
    steps:
      - name: Set up JDK 17
        uses: actions/setup-java@v1
        with:
          java-version: 1.17
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0  # Shallow clones should be disabled for a better relevancy of analysis
      - name: Cache SonarQube packages
        uses: actions/cache@v4
        with:
          path: ~\.sonar\cache
          key: ${{ runner.os }}-sonar
          restore-keys: ${{ runner.os }}-sonar
      - name: Cache SonarQube scanner
        id: cache-sonar-scanner
        uses: actions/cache@v4
        with:
          path: .\.sonar\scanner
          key: ${{ runner.os }}-sonar-scanner
          restore-keys: ${{ runner.os }}-sonar-scanner
      - name: Install SonarQube scanner
        if: steps.cache-sonar-scanner.outputs.cache-hit != 'true'
        shell: powershell
        run: |
          New-Item -Path .\.sonar\scanner -ItemType Directory
          dotnet tool update dotnet-sonarscanner --tool-path .\.sonar\scanner
      - name: Build and analyze
        shell: pwsh
        run: |
          # Fail fast and propagate errors to the runner
          # https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_preference_variables?view=powershell-7.5
          $ErrorActionPreference = "Stop"
          $PSNativeCommandUseErrorActionPreference = $true
          .\.sonar\scanner\dotnet-sonarscanner begin /k:"example" /d:sonar.token="${{ secrets.SONAR_TOKEN }}" /d:sonar.host.url="${{ vars.SONAR_HOST_URL }}"
          dotnet build
          .\.sonar\scanner\dotnet-sonarscanner end /d:sonar.token="${{ secrets.SONAR_TOKEN }}"
```

</details>

<details>

<summary>SonarScanner CLI</summary>

You can easily set up a basic configuration using the [SonarQube Scan](https://github.com/marketplace/actions/official-sonarqube-scan) GitHub action, for all languages, including C, C++, Objective-C, and Dart.

You’ll find the GitHub Actions and configuration instructions page on the GitHub Marketplace.

</details>

### Preventing pull request merges when the quality gate fails <a href="#prevent-pull-request-merge" id="prevent-pull-request-merge"></a>

In GitHub, you can block pull requests from being merged if it is failing the quality gate. To do this:

1. In GitHub, go to your repository **Settings** > **Branches** > **Branch protection rules** and select either the **Add rule** or **Edit** button if you already have a rule on the branch you wish to protect.
2. Complete the **Branch protection rule** form:
   * Define the **Branch name pattern** (the name of the branch you wish to protect)
   * Select **Require status checks to pass before merging** to open supplementary form fields.
   * In the **Search for status checks in the last week** for this repository field, select **Require branches to be up to date before merging**, then find `SonarQube Code Analysis` and add it to the list of required checks.

### Failing the workflow when the quality gate fails <a href="#fail-workflow-on-quality-gate-failure" id="fail-workflow-on-quality-gate-failure"></a>

You can use the [SonarQube Server quality gate check GitHub Action](https://github.com/marketplace/actions/sonarqube-quality-gate-check) to ensure your code meets your quality standards by failing your workflow when your quality gate fails.

If you do not want to use the SonarQube Server quality gate Check Action, you can instruct the scanner to wait for the SonarQube Server quality gate status at the end of the analysis. To enable this, pass the `-Dsonar.qualitygate.wait=true` parameter to the scanner in the workflow YAML file.

This will make the analysis step poll SonarQube Server regularly until the quality gate is computed. This will increase your workflow duration. Note that, if the quality gate is red, this will make the analysis step fail, even if the actual analysis itself is successful. We advise only using this parameter when necessary (for example, to block a deployment workflow if the quality gate is red). It should not be used to report the quality gate status in a pull request, as this is already done with pull request decoration.

You can set the `sonar.qualitygate.timeout` property to an amount of time (in seconds) that the scanner should wait for a report to be processed. The default is 300 seconds.

### If you use a monorepo <a href="#monorepo" id="monorepo"></a>

The monorepo feature is supported starting in the [Enterprise edition](https://www.sonarsource.com/plans-and-pricing/enterprise/) provided the GitHub integration with SonarQube Server has been properly set up. See [global-setup](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/gitlab-integration/global-setup "mention") for more details.

To add the SonarQube Server analysis to your monorepo workflow:

#### Step 1: Configure the analysis parameters for each project <a href="#step-1-configure-the-analysis-parameters-for-each-project" id="step-1-configure-the-analysis-parameters-for-each-project"></a>

For each project in the monorepo, set the analysis parameters: See **Configuring the project analysis parameters** above. Specific to the monorepo set up is the setting of the `sonar.token` property explained below.

You must create the Sonar tokens used to authenticate to the SonarQube Server during the analysis of the monorepo projects and store them securely in GitHub secrets. You can either use one single global-level token for the monorepo or a project-level token for each project in the monorepo.

Proceed as follows:

1. Generate the token in SonarQube Server:
   * For project tokens, create a token for each project you need the Administer permission on the project. Go to the **Security** page of your SonarQube Server account and create a **Project analysis token**.
   * For a global token, ask your administrator. The procedure is similar but you need the global Administer system permission.
2. In your GitHub repository, go to **Settings** > **Secrets**.
3. Select **New repository secret**.
4. In the **Name** field:
   * If you use a global token: enter `SONAR_TOKEN`.
   * Otherwise: enter `SONAR_TOKEN_1` (or another unique identifier within the monorepo) for the token of your first project in the monorepo.
5. In the **Value** field, enter the corresponding token value.
6. Select **Add secret**.
7. If you use project-level tokens, repeat steps 3 to 6 for each additional project in the monorepo.

#### Step 2: Configure the build.yml file of the monorepo <a href="#step-2-configure-the-buildyml-file-of-the-monorepo" id="step-2-configure-the-buildyml-file-of-the-monorepo"></a>

In the `build.yml` file of your monorepo:

* Define the paths to the projects.
* Add a job for each project in the monorepo.

See the file example below.

{% hint style="info" %}
You can fail a job inside the monorepo workflow when the quality gate fails and/or prevent pull request merges when the quality gate fails: see **Failing the workflow when the quality gate fails** above.
{% endhint %}

{% tabs %}
{% tab title="MAVEN" %}

```yaml
name: Build

on:
  push:
    branches:
      - main # or another name representing the main branch
    paths:
      - 'PROJECT1_PATH/**' # monorepo projects paths from the monorepo root directory
      - 'PROJECT2_PATH/**'
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  sonarQubeScan1:
    name: sonarQubeScan1
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0  # Shallow clones should be disabled for a better relevancy of analysis
      - name: Set up JDK 17
        uses: actions/setup-java@v1
        with:
          java-version: 17
      - name: Cache SonarQube packages
        uses: actions/cache@v4
        with:
          path: ~/.sonar/cache
          key: ${{ runner.os }}-sonar
          restore-keys: ${{ runner.os }}-sonar
      - name: Cache Maven packages
        uses: actions/cache@v4
        with:
          path: ~/.m2
          key: ${{ runner.os }}-m2-${{ hashFiles('**/pom.xml') }}
          restore-keys: ${{ runner.os }}-m2
      - name: SonarQube Scan 1
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN_1 }}  # analysis token associated to your project
          SONAR_HOST_URL: ${{ vars.SONAR_HOST_URL }}
        run: |
            cd PROJECT1_PATH/
            mvn -B verify org.sonarsource.scanner.maven:sonar-maven-plugin:sonar -Dsonar.projectKey=SONAR_PROJECT1_KEY -Dsonar.projectName='SONAR_PROJECT1_NAME' 
        # Replace variables with project path, key and name
  sonarQubeScan2:
    name: sonarQubeScan2
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0  # Shallow clones should be disabled for a better relevancy of analysis
      - name: Set up JDK 17
        uses: actions/setup-java@v1
        with:
          java-version: 17
      - name: Cache SonarQube packages
        uses: actions/cache@v4
        with:
          path: ~/.sonar/cache
          key: ${{ runner.os }}-sonar
          restore-keys: ${{ runner.os }}-sonar
      - name: Cache Maven packages
        uses: actions/cache@v4
        with:
          path: ~/.m2
          key: ${{ runner.os }}-m2-${{ hashFiles('**/pom.xml') }}
          restore-keys: ${{ runner.os }}-m2
      - name: SonarQube Scan 2
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN_2 }} # analysis token associated to your project
          SONAR_HOST_URL: ${{ vars.SONAR_HOST_URL }}
        run: |
            cd PROJECT2_PATH/
            mvn -B verify org.sonarsource.scanner.maven:sonar-maven-plugin:sonar -Dsonar.projectKey=SONAR_PROJECT2_KEY -Dsonar.projectName='SONAR_PROJECT2_NAME'
        # Replace variables with project path, key and name
  # Add other scan jobs if you wish to scan more projects in the monorepo   
```

{% endtab %}

{% tab title="GRADLE" %}

```yaml
name: Build

on:
  push:
    branches:
      - main # or another name representing the main branch
    paths:
      - 'PROJECT1_PATH/**' # monorepo projects paths from the monorepo root directory
      - 'PROJECT2_PATH/**'
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  sonarQubeScan1:
    name: sonarQube Scan 1
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0  # Shallow clones should be disabled for a better relevancy of analysis
      - name: Set up JDK 17
        uses: actions/setup-java@v1
        with:
          java-version: 17
      - name: Cache SonarQube packages
        uses: actions/cache@v4
        with:
          path: ~/.sonar/cache
          key: ${{ runner.os }}-sonar
          restore-keys: ${{ runner.os }}-sonar
      - name: Cache Gradle packages
        uses: actions/cache@v4
        with:
          path: ~/.gradle/caches
          key: ${{ runner.os }}-gradle-${{ hashFiles('**/*.gradle') }}
          restore-keys: ${{ runner.os }}-gradle
      - name: sonarQube Scan 1
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN_1 }}  # analysis token associated to your project
          SONAR_HOST_URL: ${{ vars.SONAR_HOST_URL }}
        run: |
            cd PROJECT1_PATH/
            ./gradlew build sonar --info
        #Replace variable with the project path
  sonarQubeScan2:
    name: sonarQubeScan2
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0  # Shallow clones should be disabled for a better relevancy of analysis
      - name: Set up JDK 17
        uses: actions/setup-java@v1
        with:
          java-version: 17
      - name: Cache SonarQube packages
        uses: actions/cache@v4
        with:
          path: ~/.sonar/cache
          key: ${{ runner.os }}-sonar
          restore-keys: ${{ runner.os }}-sonar
      - name: Cache Gradle packages
        uses: actions/cache@v4
        with:
          path: ~/.gradle/caches
          key: ${{ runner.os }}-gradle-${{ hashFiles('**/*.gradle') }}
          restore-keys: ${{ runner.os }}-gradle
      - name: sonarQube Scan 2
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN_2 }}  # analysis token associated to your project
          SONAR_HOST_URL: ${{ vars.SONAR_HOST_URL }}
        run: |
            cd PROJECT2_PATH/
            ./gradlew build sonar --info
        #Replace variable with the project path
  # Add other scan jobs if you wish to scan more projects in the monorepo
```

{% endtab %}

{% tab title=".NET" %}

```yaml
name: Build

on:
  push:
    branches:
      - main # or another name representing the main branch
    paths:
      - 'PROJECT1_PATH/**' # monorepo projects paths from the monorepo root directory
      - 'PROJECT2_PATH/**'
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  sonarQubeScan1:
    name: sonarQube Scan 1
    runs-on: windows-latest
    
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0  # Shallow clones should be disabled for a better relevancy of analysis
      - name: Set up JDK 17
        uses: actions/setup-java@v1
        with:
          java-version: 17
      - name: Cache SonarQube packages
        uses: actions/cache@v4
        with:
          path: ~\.sonar\cache
          key: ${{ runner.os }}-sonar
          restore-keys: ${{ runner.os }}-sonar
      - name: Cache SonarQube scanner
        id: cache-sonar-scanner
        uses: actions/cache@v4
        with:
          path: .\.sonar\scanner
          key: ${{ runner.os }}-sonar-scanner
          restore-keys: ${{ runner.os }}-sonar-scanner
      - name: Install SonarQube scanner
        if: steps.cache-sonar-scanner.outputs.cache-hit != 'true'
        shell: powershell
        run: |
          New-Item -Path .\.sonar\scanner -ItemType Directory
          dotnet tool update dotnet-sonarscanner --tool-path .\.sonar\scanner
      - name: sonarQube Scan 1
        shell: powershell
        run: |
          .\.sonar\scanner\dotnet-sonarscanner begin /k:"SONAR_PROJECT1_KEY" /d:sonar.token="${{ secrets.SONAR_TOKEN_1 }}" /d:sonar.host.url="${{ vars.SONAR_HOST_URL }}"
          dotnet build PROJECT1_PATH\SLN_FILE.SLN
          .\.sonar\scanner\dotnet-sonarscanner end /d:sonar.token="${{ secrets.SONAR_TOKEN_1 }}"
        # Replace variables with the project key and the path to the project solution file
  sonarQubeScan2:
    name: sonarQube Scan 2
    runs-on: windows-latest
    
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0  # Shallow clones should be disabled for a better relevancy of analysis
      - name: Set up JDK 17
        uses: actions/setup-java@v1
        with:
          java-version: 17
      - name: Cache SonarQube packages
        uses: actions/cache@v4
        with:
          path: ~\.sonar\cache
          key: ${{ runner.os }}-sonar
          restore-keys: ${{ runner.os }}-sonar
      - name: Cache SonarQube scanner
        id: cache-sonar-scanner
        uses: actions/cache@v4
        with:
          path: .\.sonar\scanner
          key: ${{ runner.os }}-sonar-scanner
          restore-keys: ${{ runner.os }}-sonar-scanner
      - name: Install SonarQube scanner
        if: steps.cache-sonar-scanner.outputs.cache-hit != 'true'
        shell: powershell
        run: |
          New-Item -Path .\.sonar\scanner -ItemType Directory
          dotnet tool update dotnet-sonarscanner --tool-path .\.sonar\scanner
      - name: sonarQube Scan 2
        shell: pwsh
        run: |
          # Fail fast and propagate errors to the runner
          # https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_preference_variables?view=powershell-7.5
          $ErrorActionPreference = "Stop"
          $PSNativeCommandUseErrorActionPreference = $true
          .\.sonar\scanner\dotnet-sonarscanner begin /k:"SONAR_PROJECT2_KEY" /d:sonar.token="${{ secrets.SONAR_TOKEN_2 }}" /d:sonar.host.url="${{ vars.SONAR_HOST_URL }}"
          dotnet build PROJECT2_PATH\SLN_FILE.SLN
          .\.sonar\scanner\dotnet-sonarscanner end /d:sonar.token="${{ secrets.SONAR_TOKEN_2 }}"
        # Replace variables with the project key and the path to the project solution file
  # Add other scan jobs if you wish to scan more projects in the monorepo   
```

{% endtab %}

{% tab title="C, C++, OBJECTIVE-C" %}

```yaml
name: Build

on:
  push:
    branches:
      - main # or another name representing the main branch
    paths:
      - 'PROJECT1_PATH/**' # monorepo projects paths from the monorepo root directory
      - 'PROJECT2_PATH/**'
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  sonarQubeScan1:
    name: SonarQube Scan 1
    runs-on: ubuntu-latest
    env:
      BUILD_WRAPPER_OUT_DIR: build_wrapper_output_directory # Directory where Build Wrapper output will be placed
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0  # Shallow clones should be disabled for a better relevancy of analysis
      - name: Install Build Wrapper
        uses: SonarSource/sonarqube-scan-action/install-build-wrapper@v4
        env:
          SONAR_HOST_URL: ${{vars.SONAR_HOST_URL}}
      - name: Run Build Wrapper for project 1
        run: |
          build-wrapper-linux-x86-64 --out-dir ${{ env.BUILD_WRAPPER_OUT_DIR }} <insert_your_clean_build_command_for_project1>
      - name: SonarQube Scan for project 1
        uses: SonarSource/sonarqube-scan-action@v7
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN_1 }}
          SONAR_HOST_URL: ${{vars.SONAR_HOST_URL}}
        with:
          args: >
            --define sonar.cfamily.compile-commands="${{ env.BUILD_WRAPPER_OUT_DIR }}/compile_commands.json" -Dsonar.projectBaseDir="PROJECT1_PATH/"
        #Replace variable with project path
  sonarQubeScan2:
    name: SonarQube Scan 2
    runs-on: ubuntu-latest
    env:
      BUILD_WRAPPER_OUT_DIR: build_wrapper_output_directory # Directory where build-wrapper output will be placed
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0  # Shallow clones should be disabled for a better relevancy of analysis
      - name: Install Build Wrapper
        uses: SonarSource/sonarqube-scan-action/install-build-wrapper@v4
        env:
          SONAR_HOST_URL: ${{vars.SONAR_HOST_URL}}
      - name: Run Build Wrapper for project 2
        run: |
          build-wrapper-linux-x86-64 --out-dir ${{ env.BUILD_WRAPPER_OUT_DIR }} <insert_your_clean_build_command_for_project2>
      - name: SonarQube Scan for project 2
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN_2 }}
          SONAR_HOST_URL: ${{vars.SONAR_HOST_URL}}
        with:
          args: >
            --define sonar.cfamily.build-wrapper-output="${{ env.BUILD_WRAPPER_OUT_DIR }}" -Dsonar.projectBaseDir="PROJECT2_PATH/"4
        #Replace variable with project path
  # Add other scan jobs if you wish to scan more projects in the monorepo  
```

{% endtab %}

{% tab title="OTHER" %}
The `projectBaseDir` parameter below retrieves a `sonar-project.properties` configuration file used to define the project’s analysis parameters (particularly the project key). For more information about this file, see **Configuring your project** in [SonarScanner CLI](https://app.gitbook.com/s/69lEOGGgOhCpumODGD9v/analyzing-source-code/scanners/sonarscanner "mention").

```yaml
name: Build

on:
  push:
    branches:
      - main # or another name representing the main branch
    paths:
      - 'PROJECT1_PATH/**' # monorepo projects paths from the monorepo root directory
      - 'PROJECT2_PATH/**'
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  sonarQubeScan1:
    name: sonarQubeScan1
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0  # Shallow clones should be disabled for a better relevancy of analysis
      - name: SonarQube Scan 1
        uses: SonarSource/sonarqube-scan-action@v7
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN_1 }}  # analysis token associated to your project
          SONAR_HOST_URL: ${{ vars.SONAR_HOST_URL }}
        with:
          projectBaseDir: PROJECT1_PATH/ # the path to your project from the monorepo root directory
      # If you wish to fail your job when the Quality Gate is red, uncomment the
      # following lines. This would typically be used to fail a deployment.
      # We do not recommend to use this in a pull request. Prefer using pull request
      # decoration instead.
      # - uses: SonarSource/sonarqube-quality-gate-action@v1
      #   timeout-minutes: 5
      #   env:
      #     SONAR_TOKEN: ${{ secrets.SONAR_TOKEN_1 }}
  sonarQubeScan2:
    name: sonarQubeScan2
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0  # Shallow clones should be disabled for a better relevancy of analysis
      - name: SonarQube Scan 2
        uses: SonarSource/sonarqube-scan-action@v7
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN_2 }}  # analysis token associated to your project
          SONAR_HOST_URL: ${{ vars.SONAR_HOST_URL }}
        with:
          projectBaseDir: PROJECT2_PATH/ # project path from the monorepo root directory
      # If you wish to fail your job when the Quality Gate is red, uncomment the
      # following lines. This would typically be used to fail a deployment.
      # We do not recommend to use this in a pull request. Prefer using pull request
      # decoration instead.
      # - uses: SonarSource/sonarqube-quality-gate-action@v1
      #   timeout-minutes: 5
      #   env:
      #     SONAR_TOKEN: ${{ secrets.SONAR_TOKEN_2 }}

  # Add other scan jobs if you wish to scan more projects in the monorepo   
```

{% endtab %}
{% endtabs %}

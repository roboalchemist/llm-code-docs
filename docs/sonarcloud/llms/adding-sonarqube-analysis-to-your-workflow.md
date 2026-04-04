# Source: https://docs.sonarsource.com/sonarqube-server/10.5/devops-platform-integration/github-integration/adding-sonarqube-analysis-to-your-workflow.md

# Adding analysis to GitHub Actions workflow

SonarScanners running in GitHub Actions can automatically detect branches and pull requests being built so you don’t need to specifically pass them as parameters to the scanner.

To analyze your projects with GitHub Actions, you need to:

1. Create your GitHub Secrets.
2. Configure your workflow YAML file.
3. Commit and push your code to start the analysis.

### Creating your GitHub secrets <a href="#creating-your-github-secrets" id="creating-your-github-secrets"></a>

You can create repository secrets from your GitHub repository. See GitHub’s documentation on [Encrypted secrets](https://docs.github.com/en/actions/reference/encrypted-secrets) for more information.

You need to set the following GitHub repository secrets to analyze your projects with GitHub Actions:

* **Sonar Token**: Generate a SonarQube [generating-and-using-tokens](https://docs.sonarsource.com/sonarqube-server/10.5/user-guide/user-account/generating-and-using-tokens "mention") and, in GitHub, create a new repository secret in GitHub with `SONAR_TOKEN` as the **Name** and the token you generated as the **Value**.
* **Sonar Host URL**: In GitHub, create a new repository secret with `SONAR_HOST_URL` as the **Name** and your SonarQube server URL as the **Value**.

### Configuring your .github/workflows/build.yml file <a href="#configuring-your-github-workflows-build-yml-file" id="configuring-your-github-workflows-build-yml-file"></a>

This section shows you how to configure your `.github/workflows/build.yml` file.

You’ll set up your build according to your SonarQube edition:

* **Community Edition**: Community Edition doesn’t support multiple branches, so you should only analyze your main branch. You can restrict analysis to your main branch by setting it as the only branch in your `on.push.branches` configuration in your workflow YAML file, and not using `on.pull_request`.
* **Developer Edition and above**: GitHub Actions can build specific branches and pull requests if you use `on.push.branches` and `on.pull-requests` configurations as shown in the examples below.

Click the scanner you’re using below to expand the example configuration:

<details>

<summary>SonarScanner for Gradle</summary>

**Note:** A project key might have to be provided through a `build.gradle` file, or through the command line parameter. For more information, see the [sonarscanner-for-gradle](https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/scanners/sonarscanner-for-gradle "mention") documentation.

Add the following to your `build.gradle` file:

```css-79elbk
plugins {
  id "org.sonarqube" version "3.5.0.2730"
}
```

Write the following in your workflow YAML file:

```css-79elbk
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
      - uses: actions/checkout@v2
        with:
          fetch-depth: 0  # Shallow clones should be disabled for a better relevancy of analysis
      - name: Set up JDK 17
        uses: actions/setup-java@v1
        with:
          java-version: 17
      - name: Cache SonarQube packages
        uses: actions/cache@v1
        with:
          path: ~/.sonar/cache
          key: ${{ runner.os }}-sonar
          restore-keys: ${{ runner.os }}-sonar
      - name: Cache Gradle packages
        uses: actions/cache@v1
        with:
          path: ~/.gradle/caches
          key: ${{ runner.os }}-gradle-${{ hashFiles('**/*.gradle') }}
          restore-keys: ${{ runner.os }}-gradle
      - name: Build and analyze
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
          SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}
        run: ./gradlew build sonar --info
```

</details>

<details>

<summary>SonarScanner for Maven</summary>

**Note:** A project key might have to be provided through the command line parameter. For more information, see the [sonarscanner-for-maven](https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/scanners/sonarscanner-for-maven "mention") documentation.

Write the following in your workflow YAML file:

```css-79elbk
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
      - uses: actions/checkout@v2
        with:
          fetch-depth: 0  # Shallow clones should be disabled for a better relevancy of analysis
      - name: Set up JDK 17
        uses: actions/setup-java@v1
        with:
          java-version: 17
      - name: Cache SonarQube packages
        uses: actions/cache@v1
        with:
          path: ~/.sonar/cache
          key: ${{ runner.os }}-sonar
          restore-keys: ${{ runner.os }}-sonar
      - name: Cache Maven packages
        uses: actions/cache@v1
        with:
          path: ~/.m2
          key: ${{ runner.os }}-m2-${{ hashFiles('**/pom.xml') }}
          restore-keys: ${{ runner.os }}-m2
      - name: Build and analyze
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
          SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}
        run: mvn -B verify org.sonarsource.scanner.maven:sonar-maven-plugin:sonar
```

</details>

<details>

<summary>SonarScanner for .NET</summary>

Write the following in your workflow YAML file:

```css-79elbk
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
      - uses: actions/checkout@v2
        with:
          fetch-depth: 0  # Shallow clones should be disabled for a better relevancy of analysis
      - name: Cache SonarQube packages
        uses: actions/cache@v1
        with:
          path: ~\.sonar\cache
          key: ${{ runner.os }}-sonar
          restore-keys: ${{ runner.os }}-sonar
      - name: Cache SonarQube scanner
        id: cache-sonar-scanner
        uses: actions/cache@v1
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
        shell: powershell
        run: |
          .\.sonar\scanner\dotnet-sonarscanner begin /k:"example" /d:sonar.token="${{ secrets.SONAR_TOKEN }}" /d:sonar.host.url="${{ secrets.SONAR_HOST_URL }}"
          dotnet build
          .\.sonar\scanner\dotnet-sonarscanner end /d:sonar.token="${{ secrets.SONAR_TOKEN }}"
```

</details>

<details>

<summary>SonarScanner CLI</summary>

You can easily set up a basic configuration using the SonarQube Scan GitHub Actions:

* To analyze C and C++ code, use the [SonarQube Scan for C and C++](https://github.com/marketplace/actions/sonarqube-scan-for-c-and-c) GitHub Action. It contains steps required for [c-family](https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/languages/c-family "mention"), making the workflow simpler.
* To analyze other languages, use the [SonarQube Scan](https://github.com/marketplace/actions/official-sonarqube-scan) GitHub action

You’ll find the GitHub Actions and configuration instructions page on the GitHub Marketplace.

</details>

{% hint style="warning" %}
The errors "*Missing blame information…*" and "*Could not find ref…*" can be caused by checking out with a partial or shallow clone, or when using Git submodules. You should disable git shallow clone to make sure the scanner has access to all of your history when running analysis with GitHub Actions.

For more information, see the [GitHub Actions Checkout README](https://github.com/actions/checkout).
{% endhint %}

### Failing the workflow when the quality gate fails <a href="#failing-the-workflow-when-the-quality-gate-fails" id="failing-the-workflow-when-the-quality-gate-fails"></a>

You can use the [SonarQube quality gate check GitHub Action](https://github.com/marketplace/actions/sonarqube-quality-gate-check) to ensure your code meets your quality standards by failing your workflow when your [quality-gates](https://docs.sonarsource.com/sonarqube-server/10.5/user-guide/quality-gates "mention") fails.

If you do not want to use the SonarQube quality gate Check Action, you can instruct the scanner to wait for the SonarQube quality gate status at the end of the analysis. To enable this, pass the `-Dsonar.qualitygate.wait=true` parameter to the scanner in the workflow YAML file.

This will make the analysis step poll SonarQube regularly until the quality gate is computed. This will increase your workflow duration. Note that, if the quality gate is red, this will make the analysis step fail, even if the actual analysis itself is successful. We advise only using this parameter when necessary (for example, to block a deployment workflow if the quality gate is red). It should not be used to report the quality gate status in a pull request, as this is already done with pull request decoration.

You can set the `sonar.qualitygate.timeout` property to an amount of time (in seconds) that the scanner should wait for a report to be processed. The default is 300 seconds.

### Preventing pull request merges when the quality gate fails <a href="#preventing-pull-request-merges-when-the-quality-gate-fails" id="preventing-pull-request-merges-when-the-quality-gate-fails"></a>

In GitHub, you can block pull requests from being merged if it is failing the quality gate. To do this:

1. In GitHub, go to your repository **Settings** > **Branches** > **Branch** protection rules and select either the **Add rule** or **Edit** button if you already have a rule on the branch you wish to protect.
2. Complete the **Branch protection rule** form:
   * Define the **Branch name pattern** (the name of the branch you wish to protect)
   * Select **Require status checks to pass before merging** to open supplementary form fields.
   * In the **Search for status checks in the last week for this repository** field, select **Require branches to be up to date before merging**, then find `SonarQube Code Analysis` and add it to the list of required checks.

![Define the ’SonarQube Code\` value as the status check to perform before permitting a PR merge.](https://3691828591-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Feu7dHWcqP9Cr3eUAzwWg%2Fuploads%2Fgit-blob-e4025ef1616884963e675c99ac6fa7d2195c0e65%2Fd5601ff95b1002b3c32bec6065f7ff918baa6b50.png?alt=media)

Define the ’SonarQube Code\` value as the status check to perform before permitting a PR merge.

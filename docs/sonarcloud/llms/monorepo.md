# Source: https://docs.sonarsource.com/sonarqube-server/10.5/devops-platform-integration/github-integration/monorepo.md

# If you're using a monorepo

In a monorepo setup, multiple SonarQube projects, each corresponding to a separate project within the monorepo, are all bound to the same GitHub repository. If the [setting-up-global-integration](https://docs.sonarsource.com/sonarqube-server/10.5/devops-platform-integration/github-integration/setting-up-global-integration "mention") has been properly set up, then you can easily import the projects managed in a GitHub monorepo from the SonarQube UI and thus, benefit from the integration features, such as the pull request decoration.

The monorepo feature is supported starting in the [Enterprise Edition](https://www.sonarsource.com/plans-and-pricing/enterprise/).

### Analysis setup roadmap <a href="#analysis-setup-roadmap" id="analysis-setup-roadmap"></a>

To manage the analysis of your projects in a monorepo:

1. Create the SonarQube projects related to your monorepo by importing the GitHub monorepo: see [monorepos](https://docs.sonarsource.com/sonarqube-server/10.5/project-administration/monorepos "mention").
2. Add the analysis to your GitHub Actions’ monorepo workflow: see below.
3. You can fail a job inside the monorepo workflow when the quality gate fails and/or prevent pull request merges when the quality gate fails: see [adding-sonarqube-analysis-to-your-workflow](https://docs.sonarsource.com/sonarqube-server/10.5/devops-platform-integration/github-integration/adding-sonarqube-analysis-to-your-workflow "mention").

### Adding the analysis to your monorepo workflow <a href="#add-analysis-to-workflow" id="add-analysis-to-workflow"></a>

To add the SonarQube analysis to your GitHub Actions’ monorepo workflow:

1. For each project in the monorepo, set the necessary analysis parameters: see [analysis-parameters](https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/analysis-parameters "mention") and the respective SonarScanner page ([sonarscanner-for-gradle](https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/scanners/sonarscanner-for-gradle "mention"), [sonarscanner-for-dotnet](https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/scanners/sonarscanner-for-dotnet "mention"), [sonarscanner-for-maven](https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/scanners/sonarscanner-for-maven "mention"), [sonarscanner](https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/scanners/sonarscanner "mention")) for more information. The mandatory parameter is the `sonar.projectKey` property.
2. Set up the authentication to the SonarQube Server: see below.
3. Add a workflow file (`build.yml`) in the home directory of the monorepo: see below.

#### Setting up the authentication to the SonarQube Server <a href="#setting-up-the-authentication-to-the-sonarqube-server" id="setting-up-the-authentication-to-the-sonarqube-server"></a>

You have to create the Sonar tokens used to authenticate to the SonarQube Server during the analysis of the monorepo projects and store them securely in GitHub secrets. You can either use one single global-level token for the monorepo or use a project-level token for each project in the monorepo.

Note that the Sonar Host URL must be stored in a GitHub secret as described in **Creating your GitHub secrets** in [adding-sonarqube-analysis-to-your-workflow](https://docs.sonarsource.com/sonarqube-server/10.5/devops-platform-integration/github-integration/adding-sonarqube-analysis-to-your-workflow "mention").

Proceed as follows:

1. Generate the [generating-and-using-tokens](https://docs.sonarsource.com/sonarqube-server/10.5/user-guide/user-account/generating-and-using-tokens "mention")(s) in SonarQube:
   * For project tokens, create a token for each project (you need the Administer permission on the project): Go to the **Security** page of your SonarQube account and create a **Project analysis token**.
   * For a global token, ask your administrator (The procedure is similar but you need the global Administer system permission.).
2. In your GitHub repository, go to **Settings > Secrets**.
3. Select **New repository secret**.
4. In the **Name** field:
   * If you use a global token: enter SONAR\_TOKEN.
   * Otherwise: enter SONAR\_TOKEN\_1 (or another unique identifier within the monorepo) for the token of your first project in the monorepo.
5. In the **Value** field, enter the corresponding token value.
6. Select **Add secret**.
7. If you use project-level tokens, repeat steps 3 to 6 for each additional project in the monorepo.

#### Configuring the build.yml file <a href="#configuring-the-buildyml-file" id="configuring-the-buildyml-file"></a>

In the `build.yml` file of your monorepo:

* Define the paths to the projects.
* Add a job for each project in the monorepo.

See the file example below.

{% tabs %}
{% tab title="MAVEN" %}

```css-79elbk
name: Build

on:
  push:
    branches:
      - master # main branch name
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
      - uses: actions/checkout@v4
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
      - name: SonarQube Scan 1
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN_1 }}  # analysis token associated to your project
          SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}
        run: |
            cd PROJECT1_PATH/
            mvn -B verify org.sonarsource.scanner.maven:sonar-maven-plugin:sonar -Dsonar.projectKey=SONAR_PROJECT1_KEY -Dsonar.projectName='SONAR_PROJECT1_NAME' 
        # Replace variables with project path, key and name
  sonarQubeScan2:
    name: sonarQubeScan2
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
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
      - name: SonarQube Scan 2
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN_2 }} # analysis token associated to your project
          SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}
        run: run: |
            cd PROJECT2_PATH/
            mvn -B verify org.sonarsource.scanner.maven:sonar-maven-plugin:sonar -Dsonar.projectKey=SONAR_PROJECT2_KEY -Dsonar.projectName='SONAR_PROJECT2_NAME'
        # Replace variables with project path, key and name
  # Add other scan jobs if you wish to scan more projects in the monorepo   
```

{% endtab %}

{% tab title="GRADLE" %}

```css-79elbk
name: Build

on:
  push:
    branches:
      - master # main branch name
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
      - uses: actions/checkout@v4
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
      - name: sonarQube Scan 1
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN_1 }}  # analysis token associated to your project
          SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}
        run: |
            cd PROJECT1_PATH/
            ./gradlew build sonar --info
        #Replace variable with the project path
  sonarQubeScan2:
    name: sonarQubeScan2
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
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
      - name: sonarQube Scan 2
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN_2 }}  # analysis token associated to your project
          SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}
        run: |
            cd PROJECT2_PATH/
            ./gradlew build sonar --info
        #Replace variable with the project path
  # Add other scan jobs if you wish to scan more projects in the monorepo
```

{% endtab %}

{% tab title=".NET" %}

```css-79elbk
name: Build

on:
  push:
    branches:
      - master # main branch name
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
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Shallow clones should be disabled for a better relevancy of analysis
      - name: Set up JDK 17
        uses: actions/setup-java@v1
        with:
          java-version: 17
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
      - name: sonarQube Scan 1
        shell: powershell
        run: |
          .\.sonar\scanner\dotnet-sonarscanner begin /k:"SONAR_PROJECT1_KEY" /d:sonar.token="${{ secrets.SONAR_TOKEN_1 }}" /d:sonar.host.url="${{ secrets.SONAR_HOST_URL }}"
          dotnet build PROJECT1_PATH\SLN_FILE.SLN
          .\.sonar\scanner\dotnet-sonarscanner end /d:sonar.token="${{ secrets.SONAR_TOKEN_1 }}"
        # Replace variables with the project key and the path to the project solution file
  sonarQubeScan2:
    name: sonarQube Scan 2
    runs-on: windows-latest
    
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Shallow clones should be disabled for a better relevancy of analysis
      - name: Set up JDK 17
        uses: actions/setup-java@v1
        with:
          java-version: 17
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
      - name: sonarQube Scan 2
        shell: powershell
        run: |
          .\.sonar\scanner\dotnet-sonarscanner begin /k:"SONAR_PROJECT2_KEY" /d:sonar.token="${{ secrets.SONAR_TOKEN_2 }}" /d:sonar.host.url="${{ secrets.SONAR_HOST_URL }}"
          dotnet build PROJECT2_PATH\SLN_FILE.SLN
          .\.sonar\scanner\dotnet-sonarscanner end /d:sonar.token="${{ secrets.SONAR_TOKEN_2 }}"
        # Replace variables with the project key and the path to the project solution file
  # Add other scan jobs if you wish to scan more projects in the monorepo   
```

{% endtab %}

{% tab title="C, C++, OBJECTIVE-C" %}

```css-79elbk
name: Build

on:
  push:
    branches:
      - master # main branch name
    paths:
      - 'PROJECT1_PATH/**' # monorepo projects paths from the monorepo root directory
      - 'PROJECT2_PATH/**'
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  sonarQubeScan1:
    name: sonarQube Scan 1
    runs-on: ubuntu-latest
    env:
      BUILD_WRAPPER_OUT_DIR: build_wrapper_output_directory # Directory where build-wrapper output will be placed
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Shallow clones should be disabled for a better relevancy of analysis
      - name: Install sonar-scanner and build-wrapper
        env:
          SONAR_HOST_URL: ${{secrets.SONAR_HOST_URL}}
        uses: SonarSource/sonarqube-github-c-cpp@v1
      - name: Run build-wrapper for project 1
        run: |
          build-wrapper-linux-x86-64 --out-dir ${{ env.BUILD_WRAPPER_OUT_DIR }} <insert_your_clean_build_command_for_project1>
      - name: Run sonar-scanner for project 1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN_1 }}
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN_1 }}
          SONAR_HOST_URL: ${{secrets.SONAR_HOST_URL}}
        run: |
          sonar-scanner --define sonar.cfamily.build-wrapper-output="${{ env.BUILD_WRAPPER_OUT_DIR }}" -Dsonar.projectBaseDir="PROJECT1_PATH/"
        #Replace variable with project path
  sonarQubeScan2:
    name: sonarQube Scan 2
    runs-on: ubuntu-latest
    env:
      BUILD_WRAPPER_OUT_DIR: build_wrapper_output_directory # Directory where build-wrapper output will be placed
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Shallow clones should be disabled for a better relevancy of analysis
      - name: Install sonar-scanner and build-wrapper
        env:
          SONAR_HOST_URL: ${{secrets.SONAR_HOST_URL}}
        uses: SonarSource/sonarqube-github-c-cpp@v1
      - name: Run build-wrapper for project 2
        run: |
          build-wrapper-linux-x86-64 --out-dir ${{ env.BUILD_WRAPPER_OUT_DIR }} <insert_your_clean_build_command_for_project2>
      - name: Run sonar-scanner for project 2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN_2 }}
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN_2 }}
          SONAR_HOST_URL: ${{secrets.SONAR_HOST_URL}}
        run: |
          sonar-scanner --define sonar.cfamily.build-wrapper-output="${{ env.BUILD_WRAPPER_OUT_DIR }}" -Dsonar.projectBaseDir="PROJECT2_PATH/"4
        #Replace variable with project path
  # Add other scan jobs if you wish to scan more projects in the monorepo   
```

{% endtab %}

{% tab title="OTHER" %}

```css-79elbk
name: Build

on:
  push:
    branches:
      - master # main branch name
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
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Shallow clones should be disabled for a better relevancy of analysis
      - name: SonarQube Scan 1
        uses: sonarsource/sonarqube-scan-action@master
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN_1 }}  # analysis token associated to your project
          SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}
        with:
          projectBaseDir: PROJECT1_PATH/ # the path to your project from the monorepo root directory
      # If you wish to fail your job when the Quality Gate is red, uncomment the
      # following lines. This would typically be used to fail a deployment.
      # We do not recommend to use this in a pull request. Prefer using pull request
      # decoration instead.
      # - uses: sonarsource/sonarqube-quality-gate-action@master
      #   timeout-minutes: 5
      #   env:
      #     SONAR_TOKEN: ${{ secrets.SONAR_TOKEN_1 }}
  sonarQubeScan2:
    name: sonarQubeScan2
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Shallow clones should be disabled for a better relevancy of analysis
      - name: SonarQube Scan 2
        uses: sonarsource/sonarqube-scan-action@master
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN_2 }}  # analysis token associated to your project
          SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}
        with:
          projectBaseDir: PROJECT2_PATH/ # project path from the monorepo root directory
      # If you wish to fail your job when the Quality Gate is red, uncomment the
      # following lines. This would typically be used to fail a deployment.
      # We do not recommend to use this in a pull request. Prefer using pull request
      # decoration instead.
      # - uses: sonarsource/sonarqube-quality-gate-action@master
      #   timeout-minutes: 5
      #   env:
      #     SONAR_TOKEN: ${{ secrets.SONAR_TOKEN_2 }}

  # Add other scan jobs if you wish to scan more projects in the monorepo   
```

{% endtab %}
{% endtabs %}

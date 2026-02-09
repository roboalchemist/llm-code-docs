# Source: https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/scanners/sonarscanner-for-jenkins.md

# SonarScanner for Jenkins

<details>

<summary>SonarScanner for Jenkins — 2.18 | <a href="https://sonarsource.atlassian.net/jira/software/c/projects/SONARJNKNS/issues">Issue Tracker</a></summary>

**2.18** <sup><sub>**2025-01-28**<sub></sup>\ <sup>Minor updates</sup>\
[Download](https://plugins.jenkins.io/sonar/)\
\
[Release notes](https://sonarsource.atlassian.net/issues/?jql=project%20%3D%2010138%20AND%20fixVersion%20%3D%2015464)

***

**2.17.3** <sup><sub>**2024-11-18**<sub></sup>\ <sup>Update dependencies to improve security</sup>\
[Download](https://plugins.jenkins.io/sonar/)\
\
[Release notes](https://sonarsource.atlassian.net/issues/?jql=project%20%3D%2010138%20AND%20fixVersion%20%3D%2016121)

***

**2.17.2** <sup><sub>**2024-02-19**<sub></sup>\ <sup>Fix withSonarQubeEnv step hanging when the workspace contains a symlink</sup>\
[Download](https://plugins.jenkins.io/sonar/)\
\
[Release notes](https://sonarsource.atlassian.net/issues/?jql=project%20%3D%2010138%20AND%20fixVersion%20%3D%2015473)

***

**2.16.1** <sup><sub>**2023-10-10**<sub></sup>\ <sup>Bug fixes</sup>\
[Download](https://plugins.jenkins.io/sonar/)\
\
[Release notes](https://sonarsource.atlassian.net/issues/?jql=project%20%3D%2010138%20AND%20fixVersion%20%3D%2015332)

***

**2.16** <sup><sub>**2023-09-27**<sub></sup>\ <sup>Use the sonar.token property</sup>\
[Download](https://plugins.jenkins.io/sonar/)\
\
[Release notes](https://sonarsource.atlassian.net/issues/?jql=project%20%3D%2010138%20AND%20fixVersion%20%3D%2013951)

***

**2.15** <sup><sub>**2022-11-22**<sub></sup>\ <sup>Fixed out of memory when querying deleted projects</sup>\
[Download](https://plugins.jenkins.io/sonar/)\
\
[Release notes](https://sonarsource.atlassian.net/issues/?jql=project%20%3D%2010138%20AND%20fixVersion%20%3D%2013860)

***

**2.14** <sup><sub>**2021-11-18**<sub></sup>\ <sup>Prepare SonarQube Scanner for core Guava upgrade</sup>\
[Download](https://plugins.jenkins.io/sonar/)\
\
[Release notes](https://sonarsource.atlassian.net/issues/?jql=project+%3D+10138+AND+fixVersion+%3D+12438)

***

**2.13.1** <sup><sub>**2021-04-30**<sub></sup>\ <sup>Update dependencies</sup>\
[Download](https://plugins.jenkins.io/sonar/)\
\
[Release notes](https://sonarsource.atlassian.net/issues/?jql=project+%3D+10138+AND+fixVersion+%3D+12437)

***

**2.12** <sup><sub>**2020-09-07**<sub></sup>\ <sup>Improve use of SonarQube configuration, bug fixes</sup>\
[Download](https://plugins.jenkins.io/sonar/)\
\
[Release notes](https://sonarsource.atlassian.net/issues/?jql=project+%3D+10138+AND+fixVersion+%3D+12435)

***

**2.11** <sup><sub>**2020-01-06**<sub></sup>\ <sup>Improvements for Jenkins Configuration as Code</sup>\
[Download](https://plugins.jenkins.io/sonar/)\
\
[Release notes](https://sonarsource.atlassian.net/issues/?jql=project+%3D+10138+AND+fixVersion+%3D+12434)

***

**2.10** <sup><sub>**2019-10-19**<sub></sup>\ <sup>Add webhook validation based on a shared secret</sup>\
[Download](https://plugins.jenkins.io/sonar/)\
\
[Release notes](https://sonarsource.atlassian.net/issues/?jql=project+%3D+10138+AND+fixVersion+%3D+12433)

</details>

This plugin lets you centralize the configuration of SonarQube server connection details in Jenkins global configuration.

Then you can trigger SonarQube analysis from Jenkins using standard Jenkins Build Steps or [Jenkins Pipeline DSL](https://jenkins.io/solutions/pipeline/) to trigger analysis with:

* [sonarscanner](https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/scanners/sonarscanner "mention")
* [sonarscanner-for-maven](https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/scanners/sonarscanner-for-maven "mention")
* [sonarscanner-for-gradle](https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/scanners/sonarscanner-for-gradle "mention")
* [sonarscanner-for-dotnet](https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/scanners/sonarscanner-for-dotnet "mention")

Once the job is complete, the plugin will detect that a SonarQube analysis was made during the build and display a badge and a widget on the job page with a link to the SonarQube dashboard as well as quality gate status.

### Installation <a href="#installation" id="installation"></a>

1. [Install the Jenkins Extension for SonarQube via the Jenkins Update Center](https://plugins.jenkins.io/sonar).
2. Configure your SonarQube server(s):
   1. Log into Jenkins as an administrator and go to **Manage Jenkins > Configure System**.
   2. Scroll down to the SonarQube configuration section, click **Add SonarQube**, and add the values you’re prompted for.
   3. The server [generating-and-using-tokens](https://docs.sonarsource.com/sonarqube-server/8.9/user-guide/user-account/generating-and-using-tokens "mention") should be created as a **Secret Text** credential.

### Analyzing a .NET solution <a href="#analyzing-dotnet-solution" id="analyzing-dotnet-solution"></a>

#### Global configuration <a href="#global-configuration" id="global-configuration"></a>

This step is mandatory if you want to trigger any of your analyses with the SonarScanner for .NET. You can define as many scanner instances as you wish. Then for each Jenkins job, you will be able to choose which launcher to use to run the SonarQube analysis.

1. Log into Jenkins as an administrator and go to **Manage Jenkins > Global Tool Configuration**
2. Click on **Add SonarScanner for MSBuild**
3. Add an installation of the latest available version. Check **Install automatically** to have the SonarScanner for MSBuild automatically provisioned on your Jenkins executors

If you do not see any available version under Install from GitHub, first go to Manage Jenkins > Manage Plugins > Advanced and click on Check now

#### Job configuration <a href="#job-configuration" id="job-configuration"></a>

1. Configure the project, and go to the **Build** section.
2. Add the SonarQube for MSBuild - Begin Analysis to your build
3. Configure the SonarQube Project Key, Name, and Version in the SonarScanner for MSBuild - Begin Analysis build step
4. Add the MSBuild build step or the Execute Windows batch command to execute the build with MSBuild 14 (see compatibility) to your build.
5. Add the SonarQube for MSBuild - End Analysis build steps to your build

### Analyzing a Java project with Maven or Gradle <a href="#maven-or-gradle" id="maven-or-gradle"></a>

#### Global configuration <a href="#global-configuration" id="global-configuration"></a>

1. Log into Jenkins as an administrator and go to Manage Jenkins > Configure System
2. Scroll to the SonarQube servers section and check Enable injection of SonarQube server configuration as build environment variables

#### Job configuration <a href="#job-configuration" id="job-configuration"></a>

1. **Configure** the project, and go to the **Build Environment** section.
2. Enable **Prepare SonarScanner environment** to allow the injection of SonarQube server values into this particular job. If multiple SonarQube instances are configured, you will be able to choose which one to use. Once the environment variables are available, use them in a standard Maven build step (Invoke top-level Maven targets) by setting the Goals to include, or a standard Gradle build step (Invoke Gradle script) by setting the Tasks to execute.

Maven goal:

```css-79elbk
$SONAR_MAVEN_GOAL
```

Gradle task:

```css-79elbk
sonarqube
```

In both cases, launching your analysis may require authentication. In that case, make sure that the global configuration defines a valid SonarQube token.

### Analyzing other project types <a href="#other-project-types" id="other-project-types"></a>

#### Global configuration <a href="#global-configuration" id="global-configuration"></a>

This step is mandatory if you want to trigger any of your SonarQube analyses with the SonarScanner. You can define as many scanner instances as you wish. Then for each Jenkins job, you will be able to choose which launcher to use to run the SonarQube analysis.

1. Log into Jenkins as an administrator and go to **Manage Jenkins > Global Tool Configuration**
2. Scroll down to the SonarScanner configuration section and click on Add SonarScanner. It is based on the typical Jenkins tool auto-installation. You can either choose to point to an already installed version of SonarScanner (uncheck ‘Install automatically’) or tell Jenkins to grab the installer from a remote location (check ‘Install automatically’)

If you don’t see a drop-down list with all available SonarScanner versions but instead see an empty text field then this is because Jenkins still hasn’t downloaded the required update center file (default period is 1 day). You may force this refresh by clicking the ‘Check Now’ button in Manage Plugins > Advanced tab.

#### Job configuration <a href="#job-configuration" id="job-configuration"></a>

1. **Configure** the project, and go to the **Build** section.
2. Add the SonarScanner build step to your build.
3. Configure the SonarQube analysis properties. You can either point to an existing sonar-project.properties file or set the analysis properties directly in the **Analysis properties** field.

### Using a Jenkins pipeline <a href="#jenkins-pipeline" id="jenkins-pipeline"></a>

We provide a `withSonarQubeEnv` block that allows you to select the SonarQube server you want to interact with. Connection details you have configured in Jenkins global configuration will be automatically passed to the scanner.

If needed you can override the `credentialsId` if you don’t want to use the one defined in global configuration (for example if you define credentials at the folder level).

If you only need the SonarQube environment variables to be expanded in the build context then you can override the `envOnly` flag.

```css-79elbk
withSonarQubeEnv('My SonarQube Server', envOnly: true) {
  // This expands the evironment variables SONAR_CONFIG_NAME, SONAR_HOST_URL, SONAR_AUTH_TOKEN that can be used by any script.
  println ${env.SONAR_HOST_URL} 
}
```

Here are some examples for every scanner, assuming you run on Unix slaves and you have configured a server named "My SonarQube Server" as well as the required tools. If you run on Windows slaves, just replace `sh` with `bat`.

SonarScanner:

```css-79elbk
node {
  stage('SCM') {
    git 'https://github.com/foo/bar.git'
  }
  stage('SonarQube analysis') {
    def scannerHome = tool 'SonarScanner 4.0';
    withSonarQubeEnv('My SonarQube Server') { // If you have configured more than one global server connection, you can specify its name
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
}
```

SonarScanner for Gradle:

```css-79elbk
node {
  stage('SCM') {
    git 'https://github.com/foo/bar.git'
  }
  stage('SonarQube analysis') {
    withSonarQubeEnv() { // Will pick the global server connection you have configured
      sh './gradlew sonarqube'
    }
  }
}
```

SonarScanner for Maven:

```css-79elbk
node {
  stage('SCM') {
    git 'https://github.com/foo/bar.git'
  }
  stage('SonarQube analysis') {
    withSonarQubeEnv(credentialsId: 'f225455e-ea59-40fa-8af7-08176e86507a', installationName: 'My SonarQube Server') { // You can override the credential to be used
      sh 'mvn org.sonarsource.scanner.maven:sonar-maven-plugin:3.7.0.1746:sonar'
    }
  }
}
```

SonarScanner for .NET:

```css-79elbk
node {
  stage('SCM') {
    git 'https://github.com/foo/bar.git'
  }
  stage('Build + SonarQube analysis') {
    def sqScannerMsBuildHome = tool 'Scanner for .Net Framework'
    withSonarQubeEnv('My SonarQube Server') {
      bat "${sqScannerMsBuildHome}\\SonarScanner.MSBuild.exe begin /k:myKey"
      bat 'MSBuild.exe /t:Rebuild'
      bat "${sqScannerMsBuildHome}\\SonarScanner.MSBuild.exe end"
    }
  }
}
```

### Pause pipeline until the Quality Gate is computed <a href="#pause-pipeline" id="pause-pipeline"></a>

The `waitForQualityGate` step will pause the pipeline until SonarQube analysis is completed and returns Quality Gate status.

#### Prerequisites: <a href="#prerequisites" id="prerequisites"></a>

* Configure a webhook in your SonarQube server pointing to `<your Jenkins instance>/sonarqube-webhook/`
* Use `withSonarQubeEnv` step in your pipeline (so that SonarQube taskId is correctly attached to the pipeline context).

Scripted pipeline example:

```css-79elbk
node {
  stage('SCM') {
    git 'https://github.com/foo/bar.git'
  }
  stage('SonarQube analysis') {
    withSonarQubeEnv('My SonarQube Server') {
      sh 'mvn clean package sonar:sonar'
    } // submitted SonarQube taskId is automatically attached to the pipeline context
  }
}
  
// No need to occupy a node
stage("Quality Gate"){
  timeout(time: 1, unit: 'HOURS') { // Just in case something goes wrong, pipeline will be killed after a timeout
    def qg = waitForQualityGate() // Reuse taskId previously collected by withSonarQubeEnv
    if (qg.status != 'OK') {
      error "Pipeline aborted due to quality gate failure: ${qg.status}"
    }
  }
}
```

Thanks to the webhook, the step is implemented in a very lightweight way: no need to occupy a node doing polling, and it doesn’t prevent Jenkins to restart (the step will be restored after restart). Note that to prevent race conditions, when the step starts (or is restarted) a direct call is made to the server to check if the task is already completed.

Declarative pipeline example:

```css-79elbk
pipeline {
    agent any
    stages {
        stage('SCM') {
            steps {
                git url: 'https://github.com/foo/bar.git'
            }
        }
        stage('build && SonarQube analysis') {
            steps {
                withSonarQubeEnv('My SonarQube Server') {
                    // Optionally use a Maven environment you've configured already
                    withMaven(maven:'Maven 3.5') {
                        sh 'mvn clean package sonar:sonar'
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

If you want to run multiple analyses in the same pipeline and use `waitForQualityGate` you have to do everything in order:

```css-79elbk
pipeline {
    agent any
    stages {
        stage('SonarQube analysis 1') {
            steps {
                sh 'mvn clean package sonar:sonar'
            }
        }
        stage("Quality Gate 1") {
            steps {
                waitForQualityGate abortPipeline: true
            }
        }
        stage('SonarQube analysis 2') {
            steps {
                sh 'gradle sonarqube'
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

#### Configuring a webhook secret <a href="#configuring-a-webhook-secret" id="configuring-a-webhook-secret"></a>

If you want to verify the webhook payload that is sent to Jenkins, you can add a secret to your webhook on SonarQube.

To set the secret:

1. In Jenkins, navigate to **Manage Jenkins > Configure System > SonarQube Server > Advanced > Webhook Secret** and click the **Add** button.
2. Select **Secret text** and give the secret an ID.
3. Select the secret from the dropdown menu.

If you want to override the webhook secret on a project level, you can add the secret to Jenkins and then reference the secret ID when calling `waitForQualityGate`.

```css-79elbk
waitForQualityGate(webhookSecretId: 'yourSecretID')  
```

if your pipeline is declarative or

```css-79elbk
waitForQualityGate webhookSecretId: 'yourSecretID'
```

if your pipeline is scripted.

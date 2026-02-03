# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/scanners/scanner-environment/general-requirements.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/scanner-environment/general-requirements.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/scanner-environment/general-requirements.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/scanners/general-requirements.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/scanners/scanner-environment/general-requirements.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/scanners/scanner-environment/general-requirements.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/scanners/scanner-environment/general-requirements.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/scanners/scanner-environment/general-requirements.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/scanners/scanner-environment/general-requirements.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/scanners/scanner-environment/general-requirements.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/scanners/scanner-environment/general-requirements.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/scanners/scanner-environment/general-requirements.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/scanner-environment/general-requirements.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/scanner-environment/general-requirements.md

# General requirements

### Operating system

The supported operating systems are:

* Linux (x64, AArch64)
* Windows (x64)
* macOS (x64, AArch64)
* IBM z/OS (see the[ requirements](#requirements-for-analysis-on-z-os) for more information)

### Java runtime environment (JRE)

A JRE (Open JRE or Open JDK) is required for the scanner engine used by all SonarScanners.

The required JRE can be auto-provisioned by a scanner at analysis time. Depending on your SonarScanner, JRE may be auto-provisioned. JRE auto-provisioning is currently supported by:

* SonarScanner CLI, from version 6.0.
* SonarScanner for .NET, from version 7.0.
* SonarScanner for NPM, from version 4.0.
* SonarScanner for Maven, from version 5.0
* SonarScanner for Gradle, from version 6.0

See [#if-jre-auto-provisioning-is-not-supported](#if-jre-auto-provisioning-is-not-supported "mention") for actions you may need to take if JRE auto-provisioning is not supported.

#### Required Java versions

Following are the minimum Java versions required on your CI/CD host depending on your context.

| Scanner                 | Enabled JRE auto-provisioning                                     | Disabled JRE auto-provisioning        |
| ----------------------- | ----------------------------------------------------------------- | ------------------------------------- |
| SonarScanner for Maven  | Java 11                                                           | Java 21, Java 17 has been deprecated. |
| SonarScanner for Gradle | Java 11                                                           | Java 21, Java 17 has been deprecated. |
| SonarScaner CLI         | <p>Java 11 (from version 7.2)<br>Java 17 (before version 7.2)</p> | Java 21, Java 17 has been deprecated. |
| SonarScanner for .NET   | None                                                              | Java 21, Java 17 has been deprecated. |
| SonarScanner for NPM    | None                                                              | Java 21, Java 17 has been deprecated. |
| SonarScanner for Python | None                                                              | Java 21, Java 17 has been deprecated. |

{% hint style="warning" %}
**Deprecation note**: Java 17 is deprecated as a supported scanner runtime environment and its support ends with SonarQube Server 2026.3 (July 2026), SonarQube Community Build and SonarQube Cloud in July 2026. There is no impact for this change if you use JRE auto-provisioning, enabled by default on scanners that support it, because it keeps Java version requirements always up to date. If you disabled JRE auto-provisioning or your scanner doesn’t support it, you need to update to Java 21 or newer.
{% endhint %}

Additional requirements may exist for specific scanners or languages. Check the respective SonarScanner and language pages for more details. In particular, to analyze JavaScript, TypeScript, or CSS, additional requirements exist, see [javascript-typescript-css](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/javascript-typescript-css "mention").

{% hint style="info" %}

* The requirement on the JRE refers only to the version of Java used by the scanner itself to run. It does not restrict the versions of Java that can be analyzed by the scanner. In addition, the required version changes with successive versions of the scanner.
* In rare cases, you may want to disable the auto-provisioning. To do so, set the `sonar.scanner.skipJreProvisioning` to `true`. See [#jre-autoprovisioning](https://docs.sonarsource.com/sonarqube-cloud/analysis-parameters#jre-autoprovisioning "mention") for more information.
  {% endhint %}

### If JRE auto-provisioning is not supported <a href="#jre-autoprov-not-supported" id="jre-autoprov-not-supported"></a>

This section describes the actions you may need to take depending on your environment in order to make sure the required Java version is used for the analysis.

#### GitHub Actions <a href="#github-actions" id="github-actions"></a>

The GitHub Action for SonarQube Cloud can be configured for different target build technologies. You can find samples for .NET, Gradle, Maven and a generic one, all running with JDK11, in this Sonar GitHub repository:[ sonarcloud-github-action.samples](https://github.com/SonarSource/sonarcloud-github-action-samples)

{% hint style="info" %}
If you follow these examples, we recommend using the minimum recommended version mentioned at the top of this page.
{% endhint %}

#### Maven / Gradle <a href="#maven-gradle" id="maven-gradle"></a>

If your whole Maven or Gradle build doesn’t run on Java 17 or later, we suggest first to try to base the whole build on this version of Java. If it’s not compatible, then you can override the `JAVA_HOME` environment variable just before the analysis step, as shown here:

```java
# Maven
mvn verify ...
export JAVA_HOME=/path/to/java17
mvn org.sonarsource.scanner.maven:sonar-maven-plugin:sonar ...
```

```java
# Gradle
gradle build ...
export JAVA_HOME=/path/to/java17
gradle sonarqube ...
```

#### Azure DevOps <a href="#azure-devops" id="azure-devops"></a>

All VM images available in Azure Pipelines for Microsoft-hosted agents already contain Java 17. There is no further action required. For self-hosted agents, you must ensure that you are using Java 17. You can either modify your build pipeline to ensure that it runs with Java 17 by default, or override the `JAVA_HOME` environment variable just before running the analysis.

**Xamarin**

For the specific case of Xamarin, which only allows Java 8, you will need to specify a Java 8 path separately when invoking MSBuild (using, for example, `XAMARIN_JAVA_HOME`), and then leave the `JAVA_HOME` environment variable for the scanner only.

```java
env:JAVA_HOME=/path/to/java17
env:XAMARIN_JAVA_HOME=/path/to/java8
msbuild.exe  /p:JavaSdkDirectory=$env:XAMARIN_JAVA_HOME
```

#### Dockerfile <a href="#dockerfile" id="dockerfile"></a>

Multiple base images can be used to run your build with Java 17, here are some examples:

* `openjdk:17-jdk-slim`
* `gradle:8.10.0-jdk17-jammy`

If your build is not compatible with Java 17, then you can override the `JAVA_HOME` environment variable to point to Java 17 immediately before running the scanners.

#### Jenkins <a href="#jenkins" id="jenkins"></a>

You can easily define a new JDK version by navigating to **Manage Jenkins** > **Global Tool Configuration** if you have the JDK Tool Plugin installed.

**Declarative pipelines**

If you are using a declarative pipeline with different stages, you can add a ‘tools’ section to the stage in which the code scan occurs. This will make the scanner use the JDK version that is specified.

```java
stage('SonarCloud analysis') {
    tools {
        jdk "jdk17" // the name you have given the JDK installation in Global Tool Configuration
    }
    environment {
        scannerHome = tool 'SonarCloud Scanner' // the name you have given the Sonar Scanner (in Global Tool Configuration)
    }
    steps {
        withSonarQubeEnv(installationName: 'SonarCloud') {
            sh "${scannerHome}/bin/sonar-scanner -X"
        }
    }
}
```

If you are analyzing a Java 11 project, you probably want to continue using Java 11 to build your project. The following example allows you to continue building in Java 11, but will use Java 17 to scan the code:

```java
stage('Build') {
 tools {
        jdk "jdk11" // the name you have given the JDK installation using the JDK manager (Global Tool Configuration)
    }
    steps {
        sh 'mvn compile'
    }
}
stage('SonarCloud analysis') {
    tools {
        jdk "jdk17" // the name you have given the JDK installation using the JDK manager (Global Tool Configuration)
    }
    environment {
        scannerHome = tool 'SonarCloud Scanner' // the name you have given the Sonar Scanner (Global Tool Configuration)
    }
    steps {
        withSonarQubeEnv(installationName: 'SonarCloud') {
            sh 'mvn org.sonarsource.scanner.maven:sonar-maven-plugin:sonar'
        }
    }
}
```

This example is for Maven but it can be easily modified to use Gradle.

**Classical pipelines**

**Set Job JDK version**

* Set the JDK version to be used by jobs in the **General** section of your configuration. This option is only visible if you have configured multiple JDK versions under **Manage Jenkins** > **Global Tool Configuration**.

**Set ‘Execute SonarQube Scanner’ JDK version**

* If you are using the "Execute SonarQube Scanner" step in your configuration, you can set the JDK for this step in the configuration dialog. By using this approach, you can use JDK 17 only for the code scanning performed by SonarQube Cloud. All the other steps in the job will use the globally configured JDK.

**Java 11 projects**

* Jenkins does not offer functionality to switch JDKs when using a **Freestyle project** or **Maven project** configuration. To build your project using Java 11, you will have to manually set the `JAVA_HOME` variable to Java 17 when running the analysis.
* This can be done by using the **Tool Environment Plugin**. This plugin lets you expose the location of the JDK you added under **Manage Jenkins** > **Global Tool Configuration**.
* The location of the JDK can then be used to set the `JAVA_HOME` variable in a post step command, like this:

```java
export JAVA_HOME=$OPENJDK_17_HOME/Contents/Home
mvn $SONAR_MAVEN_GOAL
```

### Requirements for analysis on z/OS

Analysis is available on z/OS with the SonarScanner CLI.

This guide lists the minimum requirements for running the SonarScanner CLI on an IBM z/OS environment.

* Use sonar-scanner-cli 7.3+ in its generic package form, labeled **Any (Requires a pre-installed JVM)** on the [SonarScanner CLI](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-cli) page.
* Bash must be installed and used for execution. Use of other shells (e.g., ksh, zsh) is not guaranteed to work.
* The [minimum required](#required-java-versions) Java version.

{% hint style="info" %}
COBOL is the only officially supported language for analysis on z/OS.
{% endhint %}

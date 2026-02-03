# Source: https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/scanners/sonarscanner-for-ant.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/scanners/sonarscanner-for-ant.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/scanners/sonarscanner-for-ant.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/scanners/sonarscanner-for-ant.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/analyzing-source-code/scanners/sonarscanner-for-ant.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/scanners/sonarscanner-for-ant.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code/scanners/sonarscanner-for-ant.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/scanners/sonarscanner-for-ant.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/scanners/sonarscanner-for-ant.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/scanners/sonarscanner-for-ant.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/scanners/sonarscanner-for-ant.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/scanners/sonarscanner-for-ant.md

# SonarScanner for Ant (Deprecated)

<details>

<summary>SonarScanner for Ant — 2.7.1 | <a href="https://sonarsource.atlassian.net/jira/software/c/projects/ANTTASK/issues">Issue Tracker</a></summary>

**2.7.1** <sup><sub>**2021-04-30**<sub></sup>\ <sup>Update dependencies</sup>\
[Download](https://binaries.sonarsource.com/Distribution/sonarqube-ant-task/sonarqube-ant-task-2.7.1.1951.jar)\
\
[Release notes](https://sonarsource.atlassian.net/issues/?jql=project+%3D+10136+AND+fixVersion+%3D+12372)

***

**2.7** <sup><sub>**2019-10-01**<sub></sup>\ <sup>Support SONAR\_HOST\_URL environment variable to configure the server URL</sup>\
[Download](https://binaries.sonarsource.com/Distribution/sonarqube-ant-task/sonarqube-ant-task-2.7.0.1612.jar)\
\
[Release notes](https://sonarsource.atlassian.net/issues/?jql=project+%3D+10136+AND+fixVersion+%3D+12371)

</details>

{% hint style="warning" %}
SonarScanner for Ant is deprecated. You can start using the SonarScanner instead by following the instructions below.
{% endhint %}

The SonarScanner for Ant provides a `task` to allow the integration of a SonarQube Server analysis into an Apache Ant build script.

### Moving from SonarScanner for Ant to SonarScanner CLI <a href="#moving-from-sonarscanner-for-ant-to-sonarscanner" id="moving-from-sonarscanner-for-ant-to-sonarscanner"></a>

The SonarScanner for Ant is an Ant Task that is a wrapper of the [sonarscanner](https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/scanners/sonarscanner "mention"), which works by invoking the SonarScanner CLI and passing to it all [analysis-parameters](https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/analysis-parameters "mention") named following a `sonar.*` convention. It is now deprecated. We recommend using the SonarScanner CLI directly.

If you’re still using the SonarScanner for Ant, follow these steps to remove the wrapper from your build file, create a `sonar-project.properties` in your project, and run the analysis.

#### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

The [sonarscanner](https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/scanners/sonarscanner "mention") is installed on your machine.

#### Configuring your sonar properties <a href="#configuring-your-sonar-properties" id="configuring-your-sonar-properties"></a>

1. Create a `sonar-project.properties` in your project.
2. Move the `sonar.*` properties from your `build.xml` file to the `sonar-project.properties` file. For example:

```css-79elbk
sonar.host.url="sonarHostUrl"
sonar.projectKey="projectKey"
sonar.projectName="projectName"
sonar.projectVersion="1.0"
sonar.sources="src"
sonar.java.binaries="build" 
sonar.java.libraries="lib/*.jar"
```

See [sonarscanner](https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/scanners/sonarscanner "mention") for more information on how to configure project properties.

### Running the analysis <a href="#running-the-analysis" id="running-the-analysis"></a>

Create a [managing-tokens](https://docs.sonarsource.com/sonarqube-server/10.8/user-guide/managing-tokens "mention") and run the analysis using `sonar-scanner -Dsonar.token=myAuthenticationToken`.

Alternatively, instead of passing the token in your command line, you can create the `SONAR_TOKEN` environment variable and set the token as its value before you launch the analysis.

See [sonarscanner](https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/scanners/sonarscanner "mention") for more information.

#### \[Archived] sample project <a href="#archived-sample-project" id="archived-sample-project"></a>

For comparison purposes, a sample SonarScanner for Ant project is available here: <https://github.com/SonarSource/sonar-scanning-examples/tree/master/sonar-scanner-ant/ant-basic>

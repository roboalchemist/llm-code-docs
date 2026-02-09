# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/test-coverage/java-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/test-coverage/java-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/test-coverage/java-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/test-coverage/java-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/analyzing-source-code/test-coverage/java-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/test-coverage/java-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code/test-coverage/java-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/test-coverage/java-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/test-coverage/java-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/test-coverage/java-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/test-coverage/java-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/test-coverage/java-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/test-coverage/java-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/test-coverage/java-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/test-coverage/java-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/test-coverage/java-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/test-coverage/java-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/test-coverage/java-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/test-coverage/java-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/java-test-coverage.md

# Java test coverage

SonarQube Cloud supports the reporting of test coverage as part of the analysis of your Java project.

However, SonarQube Cloud does not produce the coverage report itself. Instead, you must set up a third-party tool to produce the report as part of your build process. You then need to configure your analysis to tell the SonarScanner where the report is located so that it can pick it up and send it to SonarQube Cloud, where it will be displayed on your project dashboard along with the other analysis metrics.

For Java projects, SonarQube Cloud directly supports the JaCoCo coverage tool (see [generic-test-data](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/generic-test-data "mention") for information on integrating other coverage tools).

### Follow the tutorial <a href="#follow-the-tutorial" id="follow-the-tutorial"></a>

When you import your Java project into SonarQube Cloud you will be guided through the setup process by an in-product tutorial. Follow the tutorial specific to your CI. When it asks, **What option best describes your build?**, choose **Maven** or **Gradle**, depending on which you are using. When you are done with the tutorial, you should have a functioning CI-based analysis setup for your Java project. The next step is to adjust it to get coverage working.

### Adjust your setup <a href="#adjust-your-setup" id="adjust-your-setup"></a>

To enable coverage you need to:

* Adjust your build process so that JaCoCo report generation step runs *before* the SonarScanner step.
* Make sure that JacCoCo writes its report file to a defined path in the build environment.
* Configure the scanning step of your build so that the SonarScanner picks up the report file from that defined path.

### Add coverage in a single-module Maven project <a href="#add-coverage-in-a-single-module-maven-project" id="add-coverage-in-a-single-module-maven-project"></a>

To add coverage to your Maven project you need to use the [`jacoco-maven-plugin`](https://mvnrepository.com/artifact/org.jacoco/jacoco-maven-plugin) and its `report` goal to create a code coverage report.

Typically, you would create a specific Maven profile for executing the unit tests with instrumentation and producing the coverage report only on demand.

In the most basic case, we will need to execute two goals: `jacoco:prepare-agent`, which allows coverage info to be collected during unit tests execution, and `jacoco:report`, which uses data collected during unit test execution to generate a report. By default, the tool generates XML, HTML, and CSV versions of the report. Here, we explicitly specify XML, since that is the only one we need for SonarQube Cloud.

**`${project.basedir}/pom.xml`**

```xml
<profile>
  <id>coverage</id>
  <build>
   <plugins>
    <plugin>
      <groupId>org.jacoco</groupId>
     <artifactId>jacoco-maven-plugin</artifactId>
      <version>0.8.7</version>
      <executions>
        <execution>
          <id>prepare-agent</id>
          <goals>
            <goal>prepare-agent</goal>
          </goals>
        </execution>
        <execution>
          <id>report</id>
          <goals>
            <goal>report</goal>
          </goals>
          <configuration>
            <formats>
              <format>XML</format>
            </formats>
          </configuration>
        </execution>
      </executions>
    </plugin>
   </plugins>
  </build>
</profile>
```

By default the generated report will be saved under `target/site/jacoco/jacoco.xml`. This location will be checked automatically by the scanner, so no further configuration is required.

Just launch: `mvn org.sonarsource.scanner.maven:sonar-maven-plugin:sonar -Pcoverage` as usual and the report will be picked up.

If you need to change the directory where the report is generated, you can set the property either on the command line using Maven’s `-D` switch.

```css-79elbk
mvn -Dsonar.coverage.jacoco.xmlReportPaths=
      ../app-it/target/site/jacoco-aggregate/jacoco.xml
    org.sonarsource.scanner.maven:sonar-maven-plugin:sonar -Pcoverage
```

or in your `pom.xml`:

**`${project.basedir}/pom.xml`**

```xml
<properties>
  <sonar.coverage.jacoco.xmlReportPaths>
    ../app-it/target/site/jacoco-aggregate/jacoco.xml
  </sonar.coverage.jacoco.xmlReportPaths>
</properties>
```

Wildcards and a comma-delimited list of paths are supported. See [test-execution-parameters](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/test-execution-parameters "mention")for more details. The path can be either absolute or relative to the project root.

### Add coverage in a multi-module Maven project <a href="#add-coverage-in-a-multi-module-maven-project" id="add-coverage-in-a-multi-module-maven-project"></a>

For multi-module Maven projects, you configure the **`jacoco-maven-plugin`** in a profile in the parent pom just as in the single module case, above. By default, a separate coverage report will be generated for each module.

If you want to aggregate all the module-specific reports into one project-level report, the easiest solution is to create a special Maven module (alongside the ones you already have), that contains nothing except a `pom.xml` that uses the `report-aggregate` goal. Here is an example:

**`${project.basedir}/report-aggregate-module/pom.xml`**

```xml
<project>
  <artifactId>my-project-report-aggregate</artifactId>
  <name>My Project</name>
  <description>Aggregate Coverage Report</description>
  <dependencies>
    <dependency>
      <groupId>${project.groupId}</groupId>
      <artifactId>my-module-1</artifactId>
      <version>${project.version}</version>
    </dependency>
    <dependency>
      <groupId>${project.groupId}</groupId>
      <artifactId>my-module-2</artifactId>
      <version>${project.version}</version>
    </dependency>
  </dependencies>
  <build>
    <plugins>
      <plugin>
        <groupId>org.jacoco</groupId>
        <artifactId>jacoco-maven-plugin</artifactId>
        <executions>
          <execution>
            <id>report-aggregate</id>
            <phase>verify</phase>
            <goals>
              <goal>report-aggregate</goal>
            </goals>
          </execution>
        </executions>
      </plugin>
    </plugins>
  </build>
</project>
```

When you invoke `maven clean verify` in the`report-aggregate-module` directory the aggregated report will be generated and placed inside that directory at the standard location `target/site/jacoco-aggregate/jacoco.xm`l. Then, in the top level `pom.xml` you set `sonar.coverage.jacoco.xmlReportPaths`to this location:

```xml
<properties>
  <sonar.coverage.jacoco.xmlReportPaths>
    ${maven.multiModuleProjectDirectory}/report-aggregate/target/site/
      jacoco-aggregate/jacoco.xml
  </sonar.coverage.jacoco.xmlReportPaths>
</properties>
```

Wildcards and a comma-delimited list of paths are supported. See [test-coverage-parameters](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/test-coverage-parameters "mention") for details.

### Adding coverage in a Gradle project <a href="#adding-coverage-in-a-gradle-project" id="adding-coverage-in-a-gradle-project"></a>

To set up code coverage for your Gradle files, you just need to apply the JaCoCo plugin together with the SonarScanner for Gradle to the `build.gradle` file of your project as the JaCoCo is already integrated into the default gradle distribution.

**`${project.basedir}/build.gradle`**

```properties
plugins {
    id "jacoco"
    id "org.sonarqube" version "<FULL_VERSION_NUMBER>"
}
 
jacocoTestReport {
    reports {
        xml.required = true
    }
}
```

We recommend using the latest version of [sonarscanner-cli](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-cli "mention").

Your report will be automatically saved in the `build/reports/jacoco` directory. The sonarqube plugin automatically detects this location so no further configuration is required. To import coverage, launch:

`gradle test jacocoTestReport sonarqube`

For more details, see the [Gradle JaCoCo Plugin documentation](https://docs.gradle.org/current/userguide/jacoco_plugin.html).

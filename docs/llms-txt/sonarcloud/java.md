# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/languages/java.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/languages/java.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/languages/java.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/languages/java.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/languages/java.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/analyzing-source-code/languages/java.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/languages/java.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code/languages/java.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/languages/java.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/languages/java.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/languages/java.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/languages/java.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/languages/java.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/languages/java.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/languages/java.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/languages/java.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/languages/java.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/languages/java.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/languages/java.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/java.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/java.md

# Java

### Supported versions <a href="#supported-versions" id="supported-versions"></a>

The level of support for a language is defined as follows:

* Fully supported: Analysis will complete. All the language features are understood and examined.
* Supported: Most language features are understood and examined but the version includes unsupported features. Analysis might break or provide incomplete results.

LTS 8, 11, 17, 21 and all intermediary versions up to Java 24 are fully supported.

### Supported frameworks and tools <a href="#supported-frameworks-and-tools" id="supported-frameworks-and-tools"></a>

#### Web/Application Frameworks <a href="#webapplication-frameworks" id="webapplication-frameworks"></a>

Struts, Spring, JSP

#### Test Frameworks <a href="#test-frameworks" id="test-frameworks"></a>

JUnit 4/5, AssertJ, Mockito, Spring Test, TestNG

#### ORMs <a href="#orms" id="orms"></a>

Hibernate, Spring JDBC Template, JDO, VertX SQL

### Language-Specific properties <a href="#language-specific-properties" id="language-specific-properties"></a>

To discover and update the Java-specific properties, navigate in SonarQube Cloud to *Your Project* > **Administration** > **General Settings** > **Languages** > **Java**. See the [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") page for more information about specific properties.

### Java analysis and bytecode <a href="#java-analysis-and-bytecode" id="java-analysis-and-bytecode"></a>

Compiled `.class` files are required for Java projects with more than one Java file. If not provided properly, analysis will fail with the message:

```css-79elbk
Your project contains .java files, please provide compiled classes with sonar.java.binaries property, or exclude them from the analysis with sonar.exclusions property.
```

If only some `.class` files are missing, you’ll see warnings like this:

```css-79elbk
Class 'XXXXXX' is not accessible through the ClassLoader.
```

If you are not using Maven or Gradle for analysis, you must manually provide bytecode to the analysis. You can also analyze test code, and for that, you need to provide tests binaries and test libraries properties.

Note that manually providing the `sonar.java.binaries` is very error-prone. We recommend using the [sonarscanner-for-gradle](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-gradle "mention") if you’re building with Gradle, or the [sonarscanner-for-maven](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-maven "mention") if you’re using Maven.  If you analyze Java code outside of these build systems, use the [sonarscanner-cli](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-cli "mention").

| **Key**                          | **Value**                                                                                                                                                                                                                                           |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sonar.java.binaries` (required) | Comma-separated paths to directories containing the compiled bytecode files corresponding to your source files.                                                                                                                                     |
| `sonar.java.libraries`           | <p>Comma-separated paths to files with third-party libraries (JAR or Zip files) used by your project.<br>Wildcards can be used:<br><code>sonar.java.libraries=path/to/Library.jar,directory/\*\*/\*.jar</code></p>                                  |
| `sonar.java.test.binaries`       | Comma-separated paths to directories containing the compiled bytecode files corresponding to your test files.                                                                                                                                       |
| `sonar.java.test.libraries`      | <p>Comma-separated paths to files with third-party libraries (JAR or Zip files) used by your tests. (For example, this should include the junit jar).<br>Wildcards can be used:<br><code>sonar.java.test.libraries=directory/\*\*/\*.jar</code></p> |

Note that the Android development toolchain Jack does not provide `.class` files.

### Project-specific JDK <a href="#project-specific-jdk" id="project-specific-jdk"></a>

In some situations, you might have to analyze a project built with a different version of Java than the one executing the analysis. The most common case is to run the analysis with **Java 17**, while the project itself uses **Java 11** or before for its build. As an example, if your project is built with Java 8 JDK, and analyzed with the default Java 17 JDK, the use of a class like `java.lang.SecurityManager` would be flagged as deprecated code (since Java 17), which is not the case in Java 8.

When your project is built with a different JDK than the one used to run the analysis, you should manually set the sonar.java.jdkHome property so it points to the correct JDK. By doing this you will specify which JDK classes the analyzer must refer to during the analysis.

When setting `sonar.java.jdkHome`, you need to provide the path to the JDK directory used by the project being analyzed, if different from the Java runtime executing the analysis. For example, for a Java 11 project, by setting it as follows: `sonar.java.jdkHome=/usr/lib/jvm/jdk11/`

```properties
# Here maven uses the default version of Java on the system but we specify that we want to analyze a Java 11 project.
mvn org.sonarsource.scanner.maven:sonar-maven-plugin:sonar \
  # other analysis parameters
  -Dsonar.java.jdkHome=/usr/lib/jvm/jdk11/
  # other analysis parameters
```

This option can of course be added to your `sonar.properties` configuration.

### JDK preview features <a href="#jdk-preview-features" id="jdk-preview-features"></a>

To enable the [JDK preview features](https://openjdk.org/jeps/12) in SonarQube Cloud, you can set the `sonar.java.enablePreview`\* *analysis* \*parameter to `true` (default is`false`).

### Turning issues off <a href="#turning-issues-off" id="turning-issues-off"></a>

The best way to deactivate an individual issue you don’t intend to fix is to mark it as accepted or false positive through the SonarQube Cloud UI.

If you need to deactivate a rule (or all rules) for an entire file, then issue exclusions are the way to go. But if you only want to [deactivate a rule](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/editing-a-custom-quality-profile#deactivating-rules-in-a-quality-profile) across a subset of a file - all the lines of a method or a class - you can use `@SuppressWarnings("all")` or `@SuppressWarnings` with rule keys: `@SuppressWarnings("java:S2077")` or `@SuppressWarnings({"java:S1118", "java:S3546"})`.

### Handling the Java version <a href="#handling-the-java-version" id="handling-the-java-version"></a>

Java analysis is able to react to the Java version used for sources. This feature allows the deactivation of rules that target higher versions of Java than the one in use in the project so that false positives aren’t generated from irrelevant rules.

The feature relies entirely on the `sonar.java.source` property, which is automatically filled by most of the scanners used for analyses (Maven, Gradle). Java version-specific rules are not disabled when `sonar.java.source` is not provided. Concretely, rules that are designed to target specific Java versions (tagged "java8" or "java11") are activated by default in the Sonar Way Java profile. From a user perspective, the feature is fully automatic, but it means that you probably want your projects to be correctly configured.

When using SonarScanner to perform analyses of project, the property `sonar.java.source` can be set manually in `sonar-project.properties`. Accepted formats are:

* "1.X" (for instance 1.6 for Java 6, 1.7 for Java 7, 1.8 for Java 8, etc.)
* "X" (for instance 8 for Java 8, 11 for Java 11, etc. )

Example: `sonar.java.source=11`

If the property is provided, the analysis will take the source version into account, and execute related rules accordingly. At run time, each of these rules will be executed – or not – depending upon the Java version used by sources within the project. For instance, on a correctly configured project built with Java 11, rules targeting Java 17 and Java 21 will never raise issues, even though they are enabled in the associated rule profile.

### Analyzing JSP and Thymeleaf for XSS vulnerabilities <a href="#analyzing-jsp-and-thymeleaf-for-xss-vulnerabilities" id="analyzing-jsp-and-thymeleaf-for-xss-vulnerabilities"></a>

On SonarQube Cloud, you can benefit from advanced security rules including XSS vulnerability detection. Java analysis supports analysis of Thymeleaf and JSP views when used with Java Servlets or Spring. To benefit from this analysis you need to make your views part of the project sources using `sonar.sources` property. In practice this usually means adding the following in your Maven `pom.xml` file:

```xml
<properties>
    <sonar.sources>src/main/java,src/main/webapp</sonar.sources>
 </properties>
```

or, if you use Gradle:

```groovy
sonarqube {
    properties {
        property "sonar.sources", "src/main/java,src/main/webapp"
    }
}
```

where `src/main/webapp` is the directory that contains `.jsp` or Thymeleaf’s `.html` files.

### Implementation-related rule tags <a href="#implementation-related-rule-tags" id="implementation-related-rule-tags"></a>

* [symbolic-execution](https://rules.sonarsource.com/java/tag/symbolic-execution): This tag is for rules that reason about the state of the program using data flow analysis. They usually work together to find path-sensitive bugs and vulnerabilities. As soon as an issue is raised, the symbolic execution (SE) analysis of the current path will stop. For that reason, it is not recommended to evaluate these rules independently of each other as it can give a false sense of undetected issues. It is important to keep in mind that SE can never achieve perfection, so we are always working on improving these rules. Finally, note that the Java rules relying on the SE engine operate cross-procedurally in certain circumstances. In particular, all non-overridable methods defined in the same file as the method under analysis and called from within the method’s body, will be explored and learned from. Behaviors of overridable methods will be approximated.

### Related pages <a href="#related-pages" id="related-pages"></a>

* See the Test coverage[overview](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/overview "mention") page (JaCoCo, Surefire)
* [external-analyzer-reports](https://docs.sonarsource.com/sonarqube-cloud/enriching/external-analyzer-reports "mention") ([SpotBugs](https://spotbugs.github.io/), [FindBugs](http://findbugs.sourceforge.net/), [FindSecBugs](https://github.com/find-sec-bugs/find-sec-bugs/wiki/Maven-configuration), [PMD](http://maven.apache.org/plugins/maven-pmd-plugin/usage.html), [Checkstyle](http://maven.apache.org/plugins/maven-checkstyle-plugin/checkstyle-mojo))

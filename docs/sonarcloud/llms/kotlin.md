# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/languages/kotlin.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/languages/kotlin.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/languages/kotlin.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/languages/kotlin.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/languages/kotlin.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/analyzing-source-code/languages/kotlin.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/languages/kotlin.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code/languages/kotlin.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/languages/kotlin.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/languages/kotlin.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/languages/kotlin.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/languages/kotlin.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/languages/kotlin.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/languages/kotlin.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/languages/kotlin.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/languages/kotlin.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/languages/kotlin.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/languages/kotlin.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/languages/kotlin.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/kotlin.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/kotlin.md

# Kotlin

### Supported versions <a href="#supported-versions" id="supported-versions"></a>

The level of support for a language is defined as follows:

* Fully supported: Analysis will complete. All the language features are understood and examined.
* Supported: Most language features are understood and examined but the version includes unsupported features. Analysis might break or provide incomplete results.

Version 2.2 is fully supported.

Versions 1.3 to 2.1 are supported.

### Language-specific properties <a href="#language-specific-properties" id="language-specific-properties"></a>

To discover and update the Kotlin-specific properties, navigate in SonarQube Cloud to *Your Project* > **Administration** > **General Settings** > **Languages** > **Kotlin**. See the [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") page for more information about specific properties.

### Kotlin analysis and bytecode <a href="#kotlin-analysis-and-bytecode" id="kotlin-analysis-and-bytecode"></a>

If you are not using the SonarScanner for Gradle or SonarScanner for Maven, it is strongly recommended to provide the paths of all dependency binaries used by the project in order to improve analysis accuracy. You can provide these using the `sonar.java.libraries` property (note that this property is shared with the Java analyzer and as such has `java` in its name). This is a list of comma-separated paths to files with third-party libraries (JAR or Zip files) used by your project. Wildcards can be used: `sonar.java.libraries=path/to/Library.jar,directory/**/*.jar`

Note that if you use the SonarScanner for Gradle or SonarScanner for Maven to scan your code, these scanners will auto-detect the value for this property. Therefore, you don’t need to provide it.

### Specifying the Kotlin source code version <a href="#specifying-the-kotlin-source-code-version" id="specifying-the-kotlin-source-code-version"></a>

You can explicitly define which Kotlin version the analyzer should analyze your code based on. Provide the desired version in the format `X.Y` as value to the `sonar.kotlin.source.version` property, for example, `1.7`.

### Skipping unchanged files <a href="#skipping-unchanged-files" id="skipping-unchanged-files"></a>

Starting from November 2022, and by default, the Kotlin analyzer optimizes the analysis of unchanged files in pull requests. In practice, this means that the analyzer does not perform an analysis on any file that is the same as on the PR’s target branch. As long as the project is configured in such a way that the analyzer is able to find the project’s binaries, this should not impact the analysis results.

If you wish to disable this optimization, you can set the value of the analysis parameter `sonar.kotlin.skipUnchanged` to `false`. Leaving the parameter unset lets the server decide whether the optimization should be enabled.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [external-analyzer-reports](https://docs.sonarsource.com/sonarqube-cloud/enriching/external-analyzer-reports "mention") (AndroidLint, Detekt, and Ktlint)
* Test coverage [overview](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/overview "mention") (JaCoCo)

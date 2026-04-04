# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/languages/go.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/languages/go.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/languages/go.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/languages/go.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/languages/go.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/analyzing-source-code/languages/go.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/languages/go.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code/languages/go.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/languages/go.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/languages/go.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/languages/go.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/languages/go.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/languages/go.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/languages/go.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/languages/go.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/languages/go.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/languages/go.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/languages/go.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/languages/go.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/go.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/go.md

# Go

### Supported versions <a href="#supported-versions" id="supported-versions"></a>

The level of support for a language is defined as follows:

* Fully supported: Analysis will complete. All the language features are understood and examined.
* Supported: Most language features are understood and examined but the version includes unsupported features. Analysis might break or provide incomplete results.

Versions 1.0 to 1.25 are supported.

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

* SonarScanner should run on a x86-64 Windows, macOS or Linux 64bits machine.
* You need the [Go](https://golang.org/) installation on the scan machine only if you want to import coverage data.

### Language-specific properties <a href="#language-specific-properties" id="language-specific-properties"></a>

To discover and update the Go-specific properties, navigate in SonarQube Cloud to *Your Project* > **Administration** > **General Settings** > **Languages** > **Go**. See the [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") page for more information about specific properties.

By default, all the `vendor` directories are excluded from the analysis. However, you can change the property `sonar.go.exclusions` to a different pattern if you want to force their analysis (not recommended).

If you modify the `sonar.go.exclusions` or the `sonar.sources` property, be sure that `go.mod` files are included in your scan. If the `go.mod` files are excluded, the analysis results are less precise.

### sonar-project.properties Sample <a href="#sonarprojectproperties-sample" id="sonarprojectproperties-sample"></a>

Here is a first version of a `sonar-project.properties` file, valid for a simple `Go` project:

```properties
sonar.projectKey=com.company.projectkey1
sonar.projectName=My Project Name

sonar.tests=.
sonar.test.inclusions=**/*_test.go
```

### Related pages <a href="#related-pages" id="related-pages"></a>

* [test-coverage](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage "mention")
* [external-analyzer-reports](https://docs.sonarsource.com/sonarqube-cloud/enriching/external-analyzer-reports "mention")(GoVet, GoLint, GoMetaLinter)

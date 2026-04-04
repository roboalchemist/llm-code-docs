# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/test-coverage/go-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/test-coverage/go-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/test-coverage/go-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/test-coverage/go-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/test-coverage/go-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/test-coverage/go-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/test-coverage/go-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/go-test-coverage.md

# Go test coverage

SonarQube Cloud supports the reporting of test coverage information as part of the analysis of your Go project.

However, SonarQube Cloud does not produce the coverage report itself. Instead, you must set up a third-party tool to produce the report as part of your build process. You then need to configure your analysis to tell the SonarScanner where the report is located so that it can pick it up and send it to SonarQube Cloud, where it will be displayed on your project dashboard along with the other analysis metrics.

For Go projects, SonarQube Cloud supports the standard Go test tooling.

### Use CI-based, not automatic analysis <a href="#use-ci-based-not-automatic-analysis" id="use-ci-based-not-automatic-analysis"></a>

Usually, when you import a new Go project, automatic analysis starts immediately. But, since coverage is not yet supported under automatic analysis, *you will need to use CI-based analysis instead*. This requires disabling automatic analysis. Here are the steps you need to follow:

If you have not yet imported your Go project, just add an empty file called `sonar-project.properties` to the root of your repository, and *then* perform the import. SonarQube Cloud will assume that you want to set up a CI-based analysis and display the onboarding tutorial.

If you have already imported your project, then SonarQube Cloud has already run at least once using automatic analysis. You can still convert your project to use a CI-based approach:

1. Go to **Administration** > **Analysis Method** and switch SonarQube Cloud’s automatic analysis to **Off**.
2. On the same screen, under **Supported analysis methods**, find your preferred CI and select **Follow the tutorial**.

### Follow the tutorial <a href="#follow-the-tutorial" id="follow-the-tutorial"></a>

At this point, you should be in the onboarding tutorial specific to your CI. Follow the tutorial and when it asks, **What option best describes your build?**, choose **Other (for JS, TS, Go, Python, PHP, …)**. When you are done with the tutorial, you should have a functioning CI-based analysis setup for your Go project. The next step is to adjust it to get coverage working.

### Adjust your setup <a href="#adjust-your-setup" id="adjust-your-setup"></a>

To enable coverage you need to:

* adjust your build process so that the coverage tool runs *before* the scanner report generation step runs.
* make sure that the coverage tool writes its report file to a defined path in the build environment.
* configure the scanning step of your build so that the scanner picks up the report file from that defined path.

### Add coverage to your build process <a href="#add-coverage-to-your-build-process" id="add-coverage-to-your-build-process"></a>

The first step is to generate the coverage reports.

The simplest way to generate a report is to run your test with the `-coverprofile=<location>` flag.

This will tell the Go tooling to generate a coverage report file at a specific location. For example, `go test -coverprofile=coverage.out` should generate a `coverage.out` report in the working directory.

### Add the coverage analysis parameter <a href="#add-the-coverage-analysis-parameter" id="add-the-coverage-analysis-parameter"></a>

The next step is to add `sonar.go.coverage.reportPaths` to your analysis parameters. This parameter must be set to the path of the report file produced by your coverage tool. In this example, that path is set to the default produced by Coverage.py. It is set in the `sonar-project.properties` file, located in the project root:

```properties
sonar.projectKey=<sonar-project-key>
sonar.organization=<sonar-organization>

sonar.go.coverage.reportPaths=coverage.xml
```

Wildcards and a comma-delimited list of paths are supported. See [test-coverage-parameters](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/test-coverage-parameters "mention") for details.

{% hint style="info" %}
This property is usually set in the `sonar-project.properties` file, located in the project root. Alternatively, you can also set it in the command line of the scanner invocation or in the SonarQube Cloud interface under*Your Organization* > *Your Project* > **Administration** > **General Settings** > **Languages** > **Go** > **Tests and Coverage** > **Path to coverage report(s)**.
{% endhint %}

### Troubleshooting

**Missing code coverage for commented-out lines**

Users have reported receiving warnings about missing code coverage for lines that are commented out.

When you don’t provide any Go test coverage information, SonarQube considers that all executable lines of code should be covered by unit tests. Comments are not considered executable lines, and therefore, SonarQube does not expect these lines to be covered by unit tests. Once Go test coverage data is imported into SonarQube, SonarQube fully trusts and displays this data.

This warning appears because the standard Go tooling considers that commented code should be covered. This is a known bug, referenced [here](https://github.com/golang/go/issues/22545). To resolve this, we recommend removing the commented code to eliminate the warning.

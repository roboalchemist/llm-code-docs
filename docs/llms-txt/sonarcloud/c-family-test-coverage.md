# Source: https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/test-coverage/c-family-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/test-coverage/c-family-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/test-coverage/c-family-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/analyzing-source-code/test-coverage/c-family-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/test-coverage/c-family-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code/test-coverage/c-family-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/test-coverage/c-family-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/test-coverage/c-family-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/test-coverage/c-family-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/test-coverage/c-family-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/test-coverage/c-family-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/test-coverage/c-family-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/test-coverage/c-family-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/test-coverage/c-family-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/test-coverage/c-family-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/test-coverage/c-family-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/test-coverage/c-family-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/test-coverage/c-family-test-coverage.md

# C / C++ / Objective-C test coverage

SonarQube Server supports the reporting of test coverage information as part of the analysis of your C/C++/Objective-C project.

However, SonarQube Server does not generate the coverage report itself. Instead, you must set up a third-party tool to produce the report as part of your build process. You then need to configure your analysis to tell the SonarScanner where the report is located so that it can pick it up and send it to SonarQube Server, where it will be displayed on your project dashboard along with the other analysis metrics.

### Adjust your setup <a href="#adjust-your-setup" id="adjust-your-setup"></a>

To enable coverage, you need to:

* Adjust your build process so that the coverage tool generates the report(s). This is done just after your unit tests as part of the clean build required to run analysis.
* Make sure that the coverage tool writes its report file to a defined path in the build environment.
* Configure the scanning step of your build so that the scanner picks up the report file from that defined path.

### Add coverage to your build process <a href="#build-process" id="build-process"></a>

For C/C++/Objective-C projects, SonarQube Server supports a number of coverage tools. Each has an associated analysis parameter that must be set to the location of the coverage report that is produced by the tool. The parameters are:

* `sonar.cfamily.llvm-cov.reportPath`
* `sonar.cfamily.vscoveragexml.reportsPath`
* `sonar.cfamily.gcov.reportsPath`
* `sonar.cfamily.bullseye.reportPath`
* `sonar.cfamily.cobertura.reportPaths`
* `sonar.coverageReportPaths`

Assuming that you have already set up your project, you will have seen the example projects (*without coverage*) referenced in the in-product tutorials: [sonarsource-cfamily-examples](https://github.com/orgs/sonarsource-cfamily-examples/).

In the same GitHub organization, you will also find example repositories that provide guidance on how to *add coverage* to an already-configured project. These examples do not explicitly describe every possible combination of tooling and platform but do cover the most significant variants. You may need to adapt them slightly:

* [Visual Studio Coverage example on GitHub Actions](https://github.com/sonarsource-cfamily-examples/windows-msbuild-vscoverage-gh-actions-sc)
* [Visual Studio Coverage example on Azure DevOps](https://github.com/sonarsource-cfamily-examples/windows-msbuild-vscoverage-azure-sc)
* [XCode Coverage example](https://github.com/sonarsource-cfamily-examples/macos-xcode-coverage-gh-actions-sc)
* [llvm-cov example](https://github.com/sonarsource-cfamily-examples/linux-cmake-llvm-cov-gh-actions-sc)
* [gcovr example](https://github.com/sonarsource-cfamily-examples/linux-cmake-gcovr-gh-actions-sc)
* [gcov example](https://github.com/sonarsource-cfamily-examples/linux-autotools-gcov-travis-sc)

Note that these examples do not include every possible combination of tooling and platform, so you may need to adapt them slightly to your situation:

* [windows-msbuild-vscoverage-gh-actions-sc](https://github.com/sonarsource-cfamily-examples/windows-msbuild-vscoverage-gh-actions-sc)
* [windows-msbuild-vscoverage-azure-sc](https://github.com/sonarsource-cfamily-examples/windows-msbuild-vscoverage-azure-sc)
* [windows-msbuild-opencppcoverage-actions-sc](https://github.com/sonarsource-cfamily-examples/windows-msbuild-vscoverage-azure-sc)
* [macos-xcode-coverage-gh-actions-sc](https://github.com/sonarsource-cfamily-examples/macos-xcode-coverage-gh-actions-sc)
* [linux-cmake-llvm-cov-gh-actions-sc](https://github.com/sonarsource-cfamily-examples/linux-cmake-llvm-cov-gh-actions-sc)
* [linux-cmake-gcovr-gh-actions-sc](https://github.com/sonarsource-cfamily-examples/linux-cmake-gcovr-gh-actions-sc)
* [linux-autotools-gcov-travis-sc](https://github.com/sonarsource-cfamily-examples/linux-autotools-gcov-travis-sc)

These examples include the major free-to-use coverage tools for C/C++/Objective-C (VS Coverage, XCode Coverage, LLVM-COV, GCOVR, GCOV and OpenCppCoverage). For information on the popular commercial Bullseye product, see [BullseyeCoverage - C++ Code Coverage Tool](https://www.bullseye.com/).

### Coverage parameters can be set in multiple places <a href="#coverage-parameters" id="coverage-parameters"></a>

As with other analysis parameters, the coverage-related parameters for C/C++/Objective-C projects can be set in multiple places:

* On the command line of the scanner invocation use the `-D` or `--define` switch. This is what is done in the examples above, inside the `build.yml` files of each example.
* In the `sonar-project.properties` file.
* In the SonarQube Server interface under *Your Project* > **Project Settings** > **General Settings** > **Languages** > **C/C++/Objective-C** > **Coverage** for project-level settings, and **Administration** > **Configuration** > **General Settings** > **Languages** > **C/C++/Objective-C** > **Coverage** for global settings (applying to all projects).

### Related pages <a href="#related-pages" id="related-pages"></a>

[test-coverage-parameters](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/test-coverage/test-coverage-parameters "mention").

# Source: https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/c-c-objective-c-test-coverage.md

# C / C++ / Objective-C test coverage

SonarQube Cloud supports the reporting of test coverage information as part of the analysis of your C/C++/Objective-C project.

However, SonarQube Cloud does not produce the coverage report itself. Instead, you must set up a third-party tool to produce the report as part of your build process. You then need to configure your analysis to tell the SonarScanner where the report is located so that it can pick it up and send it to SonarQube Cloud, where it will be displayed on your project dashboard along with the other analysis metrics.

### Follow the tutorial <a href="#follow-the-tutorial" id="follow-the-tutorial"></a>

After you import your repository SonarQube Cloud will direct you to the onboarding tutorial specific to your CI. Follow the tutorial and when it asks, **What option best describes your build?**, choose **C/C++/Objective-C**. When you are done with the tutorial, you should have a functioning CI-based analysis setup for your project. The next step is to adjust it to get coverage working.

### Adjust your setup <a href="#adjust-your-setup" id="adjust-your-setup"></a>

To enable coverage you need to:

* Adjust your build process so that the coverage tool generates the report(s) just after your unit as part of the clean build required to run analysis.
* Make sure that the coverage tool writes its report file to a defined path in the build environment.
* Configure the scanning step of your build so that the scanner picks up the report file from that defined path.

### Add coverage to your build process <a href="#add-coverage-to-your-build-process" id="add-coverage-to-your-build-process"></a>

For C/C++/Objective-C projects SonarQube Cloud supports a number of coverage tools. Each has an associated analysis parameter that must be set to the location of the coverage report that is produced by the tool. The parameters are:

* `sonar.cfamily.llvm-cov.reportPath`
* `sonar.cfamily.vscoveragexml.reportsPath`
* `sonar.cfamily.gcov.reportsPath`
* `sonar.cfamily.bullseye.reportPath`
* `sonar.coverageReportPaths`

Assuming that you have already set up your project, you will have seen the example projects (*without coverage*) referenced in the in-product tutorials: [sonarsource-cfamily-examples](https://github.com/orgs/sonarsource-cfamily-examples/).

To help you add coverage to your project, we also provide, in the same GitHub organization, a few example repositories *with coverage*.

Note that these examples do not include every possible combination of tooling and platform, so you may need to adapt them slightly to your situation:

* [windows-msbuild-vscoverage-gh-actions-sc](https://github.com/sonarsource-cfamily-examples/windows-msbuild-vscoverage-gh-actions-sc)
* [windows-msbuild-vscoverage-azure-sc](https://github.com/sonarsource-cfamily-examples/windows-msbuild-vscoverage-azure-sc)
* [windows-msbuild-opencppcoverage-actions-sc](https://github.com/sonarsource-cfamily-examples/windows-msbuild-vscoverage-azure-sc)
* [macos-xcode-coverage-gh-actions-sc](https://github.com/sonarsource-cfamily-examples/macos-xcode-coverage-gh-actions-sc)
* [linux-cmake-llvm-cov-gh-actions-sc](https://github.com/sonarsource-cfamily-examples/linux-cmake-llvm-cov-gh-actions-sc)
* [linux-cmake-gcovr-gh-actions-sc](https://github.com/sonarsource-cfamily-examples/linux-cmake-gcovr-gh-actions-sc)
* [linux-autotools-gcov-travis-sc](https://github.com/sonarsource-cfamily-examples/linux-autotools-gcov-travis-sc)

These examples include the major free-to-use coverage tools for C/C++/Objective-C (VS Coverage, XCode Coverage, LLVM-COV, GCOVR, GCOV and OpenCppCoverage). For information on the popular commercial Bullseye product, see [BullseyeCoverage - C++ Code Coverage Tool](https://www.bullseye.com/).

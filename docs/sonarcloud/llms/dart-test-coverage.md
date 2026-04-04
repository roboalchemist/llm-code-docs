# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/test-coverage/dart-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/test-coverage/dart-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/test-coverage/dart-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/test-coverage/dart-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/test-coverage/dart-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/test-coverage/dart-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/test-coverage/dart-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/test-coverage/dart-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/test-coverage/dart-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/dart-test-coverage.md

# Dart test coverage

SonarQube Cloud supports the reporting of test coverage information as part of the analysis of your Flutter or Dart project.

However, SonarQube Cloud does not produce the coverage report itself. Instead, you’ll need to set up a coverage tool to produce an [LCOV report](https://github.com/linux-test-project/lcov) as part of your build process, then configure your analysis to tell the SonarScanner where the report is located so that it can pick it up and send it to SonarQube Cloud. The report will be displayed on your project dashboard along with the other analysis metrics.

### Follow the in-product tutorial <a href="#follow-the-in-product-tutorial" id="follow-the-in-product-tutorial"></a>

After you import your repository, SonarQube Cloud directs you to the onboarding tutorial specific to your CI. Follow the tutorial, and when asked **What option best describes your build?**, choose **Flutter or Dart**. When you’re done with the tutorial, you should have a functioning CI-based analysis setup for your project. The next step is to adjust it to get coverage working.

### Adjust your setup <a href="#adjust-your-setup" id="adjust-your-setup"></a>

To enable coverage for Dart, you need to:

* Adjust your build process so that the coverage tool generates the report(s) just after your unit as part of the clean build required to run analysis.
* Make sure that the coverage tool writes its report file to a defined path in the build environment.
* Configure the scanning step of your build so that the scanner picks up the report file from that defined path.

### Adding coverage to your build process <a href="#adding-coverage-to-your-build-process" id="adding-coverage-to-your-build-process"></a>

For Flutter or Dart projects, SonarQube Cloud supports [LCOV reports](https://github.com/linux-test-project/lcov). The location of the coverage report produced by the tool must be set in the associated analysis parameter `sonar.dart.lcov.reportPaths`.

Multiple options are available to generate coverage reports, depending on the type of project and the tools used to run test. For example:

* the [Flutter command-line tool](https://docs.flutter.dev/reference/flutter-cli), when dealing with Flutter projects
* the [Dart coverage package](https://pub.dev/documentation/coverage/latest/), when dealing with generic Dart projects

```dart
# example for a Flutter project
flutter test --coverage

# example for a Dart project
dart pub global activate coverage
dart pub global run coverage:test_with_coverage
```

To produce data for branch coverage when using the Dart coverage package, you can provide the `--branch-coverage` parameter to the `coverage:test_with_coverage` target. You’ll find more information and options in the [Dart coverage package documentation](https://pub.dev/documentation/coverage/latest/).

### Related pages <a href="#related-pages" id="related-pages"></a>

* [dart](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/dart "mention")
* [test-coverage-parameters](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/test-coverage-parameters "mention")

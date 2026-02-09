# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/languages/dart.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/languages/dart.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/languages/dart.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/languages/dart.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/languages/dart.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/languages/dart.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/languages/dart.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/languages/dart.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/dart.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/dart.md

# Dart

### Supported versions <a href="#supported-versions" id="supported-versions"></a>

The level of support for a language is defined as follows:

* Fully supported: Analysis will complete. All the language features are understood and examined.
* Supported: Most language features are understood and examined but the version includes unsupported features. Analysis might break or provide incomplete results.

Version 2 is supported.

Versions 3 to 3.8 are fully supported.

### Language-specific properties <a href="#language-specific-properties" id="language-specific-properties"></a>

To discover and update the Dart-specific properties, navigate in SonarQube Cloud to *Your Project* > **Administration** > **General Settings** > **Languages** > **Dart**. See the [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") page for more information about specific properties.

### Preparing the analysis <a href="#preparing-the-analysis" id="preparing-the-analysis"></a>

Before performing the analysis, we highly recommend:

* retrieving all project dependencies declared in `pubspec.yaml`, for example, by running `flutter pub get` for Flutter projects, `dart pub get` for Dart projects, etc.
* performing a full and successful build of your Flutter or Dart project

Otherwise, you might get incomplete and potentially incorrect analysis results. Running `flutter pub get` or `dart pub get` alone may not be enough to produce a correct analysis, for example, when you analyze generated code.

### Analyzing generated code <a href="#analyzing-generated-code" id="analyzing-generated-code"></a>

When code generation is done via [automated source code generation](https://github.com/dart-lang/source_gen), the analysis of generated code can only happen after the execution of `source_gen`, which requires a full build of the Flutter or Dart project containing the builders.

When code generation is done via lower-level packages such as [build](https://pub.dev/packages/build), the analysis should only happen once the source has been generated and persisted on disk.

{% hint style="info" %}
When a `Generated` comment is present in the file, SonarQube ignores the *entire* \*\* *file*, even if only parts of it were generated. It’s possible to enable or disable analysis of *files containing generated code* at the project level in *Your project* > **Administration** > **General Settings** > **Languages** > *Your language* > **Analyze generated code**.
{% endhint %}

{% hint style="warning" %}
Sonar provides the [`sonarcloud-github-action` action](https://github.com/marketplace/actions/sonarcloud-scan) and the [`sonarqube-scan-action` action](https://github.com/marketplace/actions/official-sonarqube-scan) to ease the configuration of the analysis in GitHub.

However, up to `v3`, the two GitHub Actions run the analysis in a Docker container, which has only access to the directory where the project is checked out.

That means that the action doesn’t have access to the directory where dependencies have been retrieved, after running `flutter pub get`, `dart pub get`, or a similar command, which may result in an incomplete and potentially incorrect analysis.

Therefore, we suggest:

* either using `sonarqube-scan-action@v6` or above, which includes a unique entrypoint for both SonarQube Server and Cloud and is based on a [composite action](https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-composite-action)
* or [sonarscanner-cli](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-cli "mention") directly (see the "Running SonarScanner CLI from the zip file" section).
  {% endhint %}

### Related pages <a href="#related-pages" id="related-pages"></a>

* [dart-test-coverage](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/dart-test-coverage "mention")

# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/test-coverage/javascript-typescript-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/test-coverage/javascript-typescript-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/test-coverage/javascript-typescript-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/test-coverage/javascript-typescript-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/analyzing-source-code/test-coverage/javascript-typescript-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/test-coverage/javascript-typescript-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code/test-coverage/javascript-typescript-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/test-coverage/javascript-typescript-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/test-coverage/javascript-typescript-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/test-coverage/javascript-typescript-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/test-coverage/javascript-typescript-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/test-coverage/javascript-typescript-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/test-coverage/javascript-typescript-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/test-coverage/javascript-typescript-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/test-coverage/javascript-typescript-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/test-coverage/javascript-typescript-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/test-coverage/javascript-typescript-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/test-coverage/javascript-typescript-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/test-coverage/javascript-typescript-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/javascript-typescript-test-coverage.md

# JavaScript / TypeScript test coverage

SonarQube Cloud supports the reporting of test coverage information as part of the analysis of your JS/TS project.

However, SonarQube Cloud does not produce the coverage report itself. Instead, you must set up a third-party tool to produce the report as part of your build process. You then need to configure your analysis to tell the SonarScanner where the report is located so that it can pick it up and send it to SonarQube Cloud, where it will be displayed on your project dashboard along with the other analysis metrics.

For JS/TS projects, SonarQube Cloud directly supports all coverage tools that produce reports in the LCOV format. Additionally, a generic coverage format is also supported if you wish to use an unsupported tool (though you will have to convert its output to the generic format yourself).

In this section, we discuss the directly supported JS/TS LCOV coverage feature. For information on the generic format, see [generic-test-data](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/generic-test-data "mention").

### Use CI-based, not automatic analysis <a href="#use-ci-based-not-automatic-analysis" id="use-ci-based-not-automatic-analysis"></a>

Usually, when you import a new JS/TS project, automatic analysis starts immediately. But, since coverage is not yet supported under automatic analysis, **you will need to use CI-based analysis instead.** This requires disabling automatic analysis. Here are the steps:

**If you have not yet imported your project**, just add an empty file called `sonar-project.properties` to the root of your repository, and *then* perform the import. SonarQube Cloud will assume that you want to set up a CI-based analysis and display the onboarding tutorial.

**If you have already imported your project,** then SonarQube Cloud has already run at least once using automatic analysis. Don’t worry, you can still convert your project to use a CI-based approach. Simply go to **Administration > Analysis Method** and switch **SonarQube Cloud Automatic Analysis** to **OFF**. Then, on the same screen, under **Supported analysis methods** find your preferred CI and click **Follow the tutorial**.

### Follow the tutorial <a href="#follow-the-tutorial" id="follow-the-tutorial"></a>

At this point, you should be in the onboarding tutorial specific to your CI. Follow the tutorial and when it asks, **What option best describes your build?**, choose **Other (for JS, TS, Go, Python, PHP, …)**. When you are done with the tutorial, you should have a functioning CI-based analysis setup for your JS/TS project. The next step is to adjust it to get coverage working.

### Adjusting your setup <a href="#adjusting-your-setup" id="adjusting-your-setup"></a>

To enable coverage you need to:

* Adjust your build process so that the coverage tool runs *before* the scanner step.
* Make sure that the coverage tool writes its report file to a defined path in the build environment.
* Configure the scanning step of your build so that the scanner picks up the report file from that defined path.

### Adding coverage to your build process <a href="#adding-coverage-to-your-build-process" id="adding-coverage-to-your-build-process"></a>

The details of setting up coverage within your build process depend on which tools you are using.

The following illustrates how to do this for a JS/TS project that uses Yarn and Jest in the GitHub Actions CI. Simply add the following to your `build.yml` file:

**`.github/workflows/build.yml`**

```yaml
- name: Install dependencies
   run: yarn
- name: Test and coverage
   run: yarn jest --coverage
```

The resulting file should look something like this:

**`.github/workflows/build.yml`**

```yaml
name: Build
on:
 push:
   branches:
     - main
 pull_request:
   types: [opened, synchronize, reopened]
jobs:
  sonarqube:
    name: SonarQube
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0 
      - name: Install dependencies
        run: yarn
      - name: Test and coverage
        run: yarn jest --coverage
      - name: SonarQube Scan
        uses: SonarSource/sonarqube-scan-action@v7
        env:
          SONAR_TOKEN: ${{ secrets. SONARCLOUD_TOKEN }}
```

First, you install all your project dependencies and then invoke `jest` with the `——coverage` option to run your tests and write out the coverage data to a file.

If, as here, you do not specify an output file, the default `./coverage/lcov.info` is used.

If you are using a different package manager or a different testing tool these details will be different.

*The essential requirements are that the tool produces its report in the LCOV format and writes it to a place from which the scanner can then pick it up.*

### Adding the coverage analysis parameter <a href="#adding-the-coverage-analysis-parameter" id="adding-the-coverage-analysis-parameter"></a>

The next step is to add `sonar.javascript.lcov.reportPaths` to your analysis parameters. This parameter must be set to the path of the report file produced by your coverage tool. The path can be either absolute or relative to the project root. In this example, that path is set to the default produced by Jest: `./coverage/lcov.info`. It is set in the `sonar-project.properties` file, located in the project root:

**`sonar-project.properties`**

```properties
sonar.projectKey=<project-key>
...
sonar.javascript.lcov.reportPaths=./coverage/lcov.info
```

Wildcards and a comma-delimited list of paths are supported. See [test-coverage-parameters](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/test-coverage-parameters "mention") for more details.

{% hint style="warning" %}
This property is usually set in the `sonar-project.properties` file, located in the project root. Alternatively, you can also set it in the command line of the scanner invocation or in the SonarQube Cloud interface under

***Your Organization*** > ***Your Project*** > **Administration** > **General Settings** > **Languages** > **JavaScript / TypeScript** > **Tests and Coverage** > **LCOV Files**
{% endhint %}

The parameter `sonar.typescript.lcov.reportPaths` was formerly used for TypeScript coverage. This parameter has been deprecated. The parameter `sonar.javascript.lcov.reportPaths` is now used for both JavaScript and TypeScript.

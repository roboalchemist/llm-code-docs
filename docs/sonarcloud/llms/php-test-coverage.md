# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/test-coverage/php-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/test-coverage/php-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/test-coverage/php-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/test-coverage/php-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/analyzing-source-code/test-coverage/php-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/test-coverage/php-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code/test-coverage/php-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/test-coverage/php-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/test-coverage/php-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/test-coverage/php-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/test-coverage/php-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/test-coverage/php-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/test-coverage/php-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/test-coverage/php-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/test-coverage/php-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/test-coverage/php-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/test-coverage/php-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/test-coverage/php-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/test-coverage/php-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/php-test-coverage.md

# PHP test coverage

SonarQube Cloud supports the reporting of test coverage information as part of the analysis of your PHP project.

However, SonarQube Cloud does not produce the coverage report itself. Instead, you must set up a third-party tool to produce the report as part of your build process. You then need to configure your analysis to tell the SonarScanner where the report is located so that it can pick it up and send it to SonarQube Cloud, where it will be displayed on your project dashboard along with the other analysis metrics.

For PHP projects, we recommend PHPUnit for testing and coverage reporting.

### Use CI-based, not automatic analysis <a href="#use-ci-based-not-automatic-analysis" id="use-ci-based-not-automatic-analysis"></a>

Usually, when you import a new PHP project, automatic analysis starts immediately. But, since coverage is not yet supported under automatic analysis, *you will need to use CI-based analysis instead.* This requires disabling automatic analysis. Here are the steps you need to follow:

**If you have not yet imported your PHP project**, just add an empty file called `sonar-project.properties` to the root of your repository, and *then* perform the import. SonarQube Cloud will assume that you want to set up a CI-based analysis and display the onboarding tutorial.

**If you have already imported your project,** then SonarQube Cloud has already run at least once using automatic analysis. Don’t worry, you can still convert your project to use a CI-based approach. Simply go to **Administration** > **Analysis Method** and switch **SonarQube Cloud Automatic Analysis** to **OFF**. Then, on the same screen, under **Supported analysis methods** find your preferred CI and select **Follow the tutorial**.

### Follow the tutorial <a href="#follow-the-tutorial" id="follow-the-tutorial"></a>

At this point, you should be in the onboarding tutorial specific to your CI. Follow the tutorial and when it asks, **What option best describes your build?**, choose **Other (for JS, TS, Go, Python, PHP, …)**. When you are done with the tutorial, you should have a functioning CI-based analysis setup for your PHP project. The next step is to adjust it to get coverage working.

### Adjust your setup <a href="#adjust-your-setup" id="adjust-your-setup"></a>

To enable coverage you need to:

* Adjust your build process so that the coverage tool runs *before* the scanner report generation step runs.
* Make sure that the coverage tool writes its report file to a defined path in the build environment.
* Configure the scanning step of your build so that the scanner picks up the report file from that defined path.

### Add coverage to your build process <a href="#add-coverage-to-your-build-process" id="add-coverage-to-your-build-process"></a>

The details of setting up coverage within your build process depend on which tools you are using. In our example below we use:

* Composer, as a package manager
* PHPUnit with Xdebug, to execute the tests, and
* GitHub Actions to perform the build.

Simply add the following to your `ci.yml` file:

```yaml
- name: Setup PHP with Xdebug
          uses: shivammathur/setup-php@v2
          with:
            php-version: '8.1'
            coverage: xdebug
            
        - name: Install dependencies with composer
          run: composer update --no-ansi --no-interaction --no-progress
          
        - name: Run tests with phpunit/phpunit
          run: vendor/bin/phpunit --coverage-clover=coverage.xml
```

The resulting file should look something like this:

**`.github/workflows/CI.yml`**

```yaml
name: CI

on:
  - pull_request
  - push
  
jobs:
  tests:
      name: Tests

      runs-on: ubuntu-latest
      
      steps:
        - name: Checkout
          uses: actions/checkout@v6
          with:
            fetch-depth: 0
          
        - name: Setup PHP with Xdebug
          uses: shivammathur/setup-php@v2
          with:
            php-version: '8.1'
            coverage: xdebug
            
        - name: Install dependencies with composer
          run: composer update --no-ansi --no-interaction --no-progress
          
        - name: Run tests with phpunit/phpunit
          run: vendor/bin/phpunit --coverage-clover=coverage.xml
          
        - name: SonarQube Scan
          uses: SonarSource/sonarqube-scan-action@v7
          env:
            SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
```

First you install all your project dependencies using Composer as a package manager and then invoke *PHPUnit with XDebug* to run your tests and generate a coverage report file.

**The essential requirements are that the tool produces its report in the clover.xml format and writes it to a place from which the scanner can then pick it up.**

### Add the coverage analysis parameter <a href="#add-the-coverage-analysis-parameter" id="add-the-coverage-analysis-parameter"></a>

The next step is to add `sonar.php.coverage.reportPaths` to your analysis parameters. This parameter must be set to the path of the report file on GitHub Actions produced by your coverage tool. In this example, that path is set to the default produced by GitHub Actions. It is set in the `sonar-project.properties` file, located in the project root:

**`sonar-project.properties`**

```properties
sonar.projectKey=<sonar-project-key>
sonar.organization=<sonar-organization>

sonar.php.coverage.reportPaths=coverage.xml
```

Wildcards and a comma-delimited list of paths are supported. See [test-coverage-parameters](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/test-coverage-parameters "mention") for details.

{% hint style="warning" %}
This property is usually set in the `sonar-project.properties` file, located in the project root. Alternatively, you can also set it in the command line of the scanner invocation or in the SonarQube Cloud interface under:

*Your Organization* > ***Your Project*** > **Administration** > **General Settings** > **Languages** > **PHP** > **PHP Unit** > **Coverage Reports**
{% endhint %}

# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/test-coverage/python-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/test-coverage/python-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/test-coverage/python-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/test-coverage/python-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/analyzing-source-code/test-coverage/python-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/test-coverage/python-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code/test-coverage/python-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/test-coverage/python-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/test-coverage/python-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/test-coverage/python-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/test-coverage/python-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/test-coverage/python-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/test-coverage/python-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/test-coverage/python-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/test-coverage/python-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/test-coverage/python-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/test-coverage/python-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/test-coverage/python-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/test-coverage/python-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/python-test-coverage.md

# Python test coverage

SonarQube Cloud supports the reporting of test coverage information as part of the analysis of your Python project.

However, SonarQube Cloud does not produce the coverage report itself. Instead, you must set up a third-party tool to produce the report as part of your build process. You then need to configure your analysis to tell the SonarScanner where the report is located so that it can pick it up and send it to SonarQube Cloud, where it will be displayed on your project dashboard along with the other analysis metrics.

### Use CI-based, not automatic analysis <a href="#use-ci-based-not-automatic-analysis" id="use-ci-based-not-automatic-analysis"></a>

Usually, when you import a new Python project, automatic analysis starts immediately. But, since coverage is not yet supported under automatic analysis, *you will need to use CI-based analysis instead*. This requires disabling automatic analysis. Here are the steps you need to follow:

**If you have not yet imported your python project**, just add an empty file called `sonar-project.properties` to the root of your repository, and *then* perform the import. SonarQube Cloud will assume that you want to set up a CI-based analysis and display the onboarding tutorial.

**If you have already imported your project**, then SonarQube Cloud has already run at least once using automatic analysis. Don’t worry, you can still convert your project to use a CI-based approach. Simply go to **Administration** > **Analysis Method** and switch **SonarQube Cloud Automatic Analysis** to **OFF**. Then, on the same screen, under **Supported analysis methods** find your preferred CI and select **Follow the tutorial**.

### Follow the tutorial <a href="#follow-the-tutorial" id="follow-the-tutorial"></a>

At this point, you should be in the onboarding tutorial specific to your CI. Follow the tutorial and when it asks, **What option best describes your build?**, choose **Other (for JS, TS, Go, Python, PHP, …)**. When you are done with the tutorial, you should have a functioning CI-based analysis setup for your Python project. The next step is to adjust it to get coverage working.

### Adjust your setup <a href="#adjust-your-setup" id="adjust-your-setup"></a>

To enable coverage you need to:

* Adjust your build process so that the coverage tool runs *before* the scanner report generation step runs.
* Make sure that the coverage tool writes its report file to a defined path in the build environment.
* Configure the scanning step of your build so that the scanner picks up the report file from that defined path.

### Add coverage to your build process <a href="#add-coverage-to-your-build-process" id="add-coverage-to-your-build-process"></a>

The details of setting up coverage within your build process depend on which tools you are using. In our example we use:

* Tox, to configure the tests
* Pytest, to execute the tests
* Coverage, (the Coverage.py tool,) to measure code coverage, and
* GitHub Actions, to perform the build.

In this example, we invoke `pytest` and use the `pytest-cov` plugin which, in turn, uses Coverage.py. Simply add the text below to the `tox.ini` file at the root of your project:

**`Tox.ini (Coverage.py and Pytest)`**

```ini
[tox]
envlist = py39
skipsdist = True
 
[testenv]
deps =
    pytest
    pytest-cov
commands = pytest --cov=my_project --cov-report=xml --cov-config=tox.ini --cov-branch
 
```

Alternatively, in this example, we start the test by invoking the Coverage.py tool (the command `coverage`) with the `pytest` invocation as an argument.

**`Alternative tox.ini (Coverage.py only)`**

```python
[tox]
envlist = py39
skipsdist = True
 
[testenv]
deps =
    pytest
    coverage
commands =
    coverage run -m pytest
    coverage xml
 
[coverage:run]
relative_files = True
source = my_project/
branch = True
```

Note that we specify `relative_files = True` in the `tox.ini` file to ensure that GitHub Actions will correctly parse your coverage results.

The following shows how to configure the GitHub Actions build file for your Python project so that it works in conjunction with the `tox.ini` configuration file described above to generate code coverage. Your `build.yml` file should look something like this:

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
    name: SonarQube Cloud
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0
      - name: Setup Python
        uses: actions/setup-python@v6
        with:
          python-version: ${{ matrix.python }}
      - name: Install tox and any other packages
        run: pip install tox
      - name: Run tox
        run: tox -e py
      - name: SonarQube Scan
        uses: SonarSource/sonarqube-scan-action@v7
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
```

First of all, install all of your project dependencies and then invoke `tox` to run your tests and generate a coverage report file.

If, as here, you do not specify an output file, the scanner will look for report paths located under the default `.coverage-reports/*coverage-*.xml.`

If you are using a different package manager and/or a different testing tool these details will be different.

**The essential requirements are that the tool produces its report in the Cobertura XML format and writes it to a place from which the scanner can then pick it up.**

### Add the coverage analysis parameter <a href="#add-the-coverage-analysis-parameter" id="add-the-coverage-analysis-parameter"></a>

The next step is to add `sonar.python.coverage.reportPaths` to your analysis parameters. This parameter must be set to the path of the report file produced by your coverage tool. In this example, that path is set to the default produced by Coverage.py. It is set in the `sonar-project.properties` file, located in the project root:

**`sonar-project.properties`**

```properties
sonar.projectKey=<sonar-project-key>
sonar.organization=<sonar-organization>
 
sonar.python.coverage.reportPaths=coverage.xml
```

Wildcards and a comma-delimited list of paths are supported. See [test-coverage-parameters](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/test-coverage-parameters "mention") for details.

{% hint style="warning" %}
This property is usually set in the `sonar-project.properties` file, located in the project root. Alternatively, you can also set it in the command line of the scanner invocation or in the SonarQube Cloud interface under

***Your Organization*** > ***Your Project*** > **Administration** > **General Settings** > **Languages** > **Python** > **Tests and Coverage** > **Path to coverage report(s)**
{% endhint %}

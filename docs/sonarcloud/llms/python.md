# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/languages/python.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/languages/python.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/languages/python.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/languages/python.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/languages/python.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/analyzing-source-code/languages/python.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/languages/python.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code/languages/python.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/languages/python.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/languages/python.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/languages/python.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/languages/python.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/languages/python.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/languages/python.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/languages/python.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/languages/python.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/languages/python.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/languages/python.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/languages/python.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/python.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/python.md

# Python

### Supported versions <a href="#supported-versions" id="supported-versions"></a>

The level of support for a language is defined as follows:

* Fully supported: Analysis will complete. All the language features are understood and examined.
* Supported: Most language features are understood and examined but the version includes unsupported features. Analysis might break or provide incomplete results.

Versions 3.0 to 3.14 are fully supported.

Version 2.7 is supported.

### Supported tools and frameworks <a href="#supported-tools-and-frameworks" id="supported-tools-and-frameworks"></a>

Django, FastAPI, Flask, Jupyter Notebooks, Numpy, Pandas, PySpark, PyTorch, Tensorflow and Scikit-learn.

### Language-specific properties <a href="#language-specific-properties" id="language-specific-properties"></a>

To discover and update the Python-specific properties, navigate in SonarQube Cloud to *Your Project* > **Administration** > **General Settings** > **Languages** > **Python**. See the [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") page for more information about specific properties.

### Handling project python version <a href="#handling-project-python-version" id="handling-project-python-version"></a>

Python code is analyzed by default as compatible with python 2 and python 3. Some issues will be automatically silenced to avoid raising False Positives. In order to get a more precise analysis you can specify the python versions your code supports via the `sonar.python.version` parameter.

Accepted format are a comma separated list of versions having the format "X.Y"

Examples:

* `sonar.python.version=2.7`
* `sonar.python.version=3.8`
* `sonar.python.version=2.7, 3.7, 3.8, 3.9`

### Jupyter Notebooks <a href="#jupyter-notebooks" id="jupyter-notebooks"></a>

Jupyter Notebooks are an open document format based on JSON. They are used for all sorts of data science tasks: data cleaning and transformation, data visualization, statistical modeling, machine learning, deep learning, etc.

#### Supported versions <a href="#supported-versions" id="supported-versions"></a>

SonarQube Cloud can analyze Jupyter Notebooks nbformat.v4 and later.

#### Specific properties <a href="#specific-properties" id="specific-properties"></a>

Discover and update the Jupyter Notebooks-specific [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") in **Administration** > **General Settings** > **Languages** > **Python** > **Jupyter Notebooks**.

#### Managing rules <a href="#managing-rules" id="managing-rules"></a>

Jupyter Notebook rules can be enabled and disabled in your quality profile. See the [quality-profile-association](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/quality-profile-association "mention") pages for more details.

#### Jupyter Notebooks in SonarQube for IDE for VSCode <a href="#jupyter-notebooks-in-sonarqube-for-ide-for-vscode" id="jupyter-notebooks-in-sonarqube-for-ide-for-vscode"></a>

You can analyze your Jupyter Notebooks projects directly in VS Code; see the [Scan my project #Jupyter Notebooks](https://app.gitbook.com/s/6LPRABg3ubAJhpfR5K0Y/using/scan-my-project#jupyter-notebooks "mention") article in the SonarQube for VS Code docs. Note that [Connected mode](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/connected-mode) will be ignored when working with Jupyter Notebooks (if using connected mode with Jupyter Notebooks is important to you, please [submit the idea on SonarQube Cloud’s portal](https://portal.productboard.com/sonarsource/1-sonarcloud/tabs/1-under-consideration/sonarcloud/tabs/under-consideration) in Productboard).

#### Important notes <a href="#important-notes" id="important-notes"></a>

* Only Python code is analyzed in Jupyter Notebooks.
* Only primary locations are shown (see the [issues](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues "mention") pages to learn more about primary vs secondary locations).
* Analysis does not measure code duplication at this time.

### Parallel code scan

By default, the Python analyzer tries to parallelize the analysis of files; it uses 90% of the cores available, up until 6.

If required, it is possible to customize the number of scheduled parallel jobs by configuring the property `sonar.python.analysis.threads n` at the scanner level, where `n` is an integer indicating the number of threads allocated for the analysis.

You should consider setting the `sonar.python.analysis.threads` property only when the automatic detection of the number of logical CPUs cannot detect the desired number.

A typical example is when the analysis should not consume all the available computing resources to leave room for other tasks running in parallel on the same machine.

When setting the `sonar.python.analysis.threads` property, you should set it to a value less or equal to the number of logical CPUs available. Over-committing does not accelerate the analysis and can even slow it down.

You can disable parallel code scan for Python by setting the property `sonar.python.analysis.parallel` to `false`. This can be useful when debugging an analysis.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [external-analyzer-reports](https://docs.sonarsource.com/sonarqube-cloud/enriching/external-analyzer-reports "mention") ([Pylint](https://pylint.pycqa.org/), [Bandit](https://github.com/PyCQA/bandit/blob/master/README.rst), [Flake8](https://flake8.pycqa.org/en/latest/))
* Test coverage [overview](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/overview "mention") (the [Coverage.py tool](https://coverage.readthedocs.io/en/7.3.2/) provided by [Ned Batchelder](https://nedbatchelder.com/), [Nose](https://nose.readthedocs.io/), [pytest](https://docs.pytest.org/en/latest/))

# Source: https://docs.sonarsource.com/sonarqube-for-eclipse/using/scan-my-project.md

# Source: https://docs.sonarsource.com/sonarqube-for-visual-studio/using/scan-my-project.md

# Source: https://docs.sonarsource.com/sonarqube-for-intellij/using/scan-my-project.md

# Source: https://docs.sonarsource.com/sonarqube-for-vs-code/using/scan-my-project.md

# Scan my project

SonarQube for IDE, a core component of the [SonarQube solution](https://www.sonarsource.com/), is a developer’s first line of defense to find and fix coding issues in real-time. The results of a SonarQube for IDE scan provide rich contextual guidance to help you improve your skills while enhancing productivity to help you resolve issues in code.

SonarQube for IDE scans your project to provide instant feedback against hundreds of language-specific rules. When running in connected mode with SonarQube Server or SonarQube Cloud, you can benefit from additional rules that identify security vulnerabilities and security hotspots as well as take advantage of team features that help your organization achieve high-quality code.

Every organization has custom policies and procedures; the SonarQube for IDE analyzer offers a level of customization to help you achieve those practices.

### Overview <a href="#overview" id="overview"></a>

SonarQube for VS Code will automatically analyze all open files. Scanning a full project, including unopened files, is only available in the search for Security hotspots; please see the documentation on [#reporting-security-hotspots-in-the-whole-folder](https://docs.sonarsource.com/sonarqube-for-vs-code/security-hotspots#reporting-security-hotspots-in-the-whole-folder "mention") for the full details.

### First steps <a href="#first-steps" id="first-steps"></a>

SonarQube for VS Code will only analyze open files when a file is opened or saved. It is not possible to manually trigger an analysis.

### Scanning while in Connected Mode <a href="#scanning-while-in-connected-mode" id="scanning-while-in-connected-mode"></a>

When running in [connected-mode](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/connected-mode "mention"), SonarQube for IDE will sync with the SonarQube (Server, Cloud) or SonarQube Community Build quality profile to download issues and suppress those marked as *safe* or *won’t fix* on the server. The analyzer properties and rules will be respected and SonarQube for IDE will use locally what is defined on the server.

{% hint style="info" %}
When running in connected mode with SonarQube Server 10.4 or newer, **Won’t Fix** becomes **Accept**.
{% endhint %}

### Specify additional analyzer properties <a href="#specify-additional-analyzer-properties" id="specify-additional-analyzer-properties"></a>

It is possible to specify extra analyzer properties that will be used for analysis.

```json
// <project>/.vscode/settings.json
{
    "sonarlint.analyzerProperties": {
        "sonar.javascript.node.maxspace": "4096"
    }
}
```

### Language-specific information <a href="#language-specific-information" id="language-specific-information"></a>

#### C and C++ analysis <a href="#c-and-c-analysis" id="c-and-c-analysis"></a>

Please see the specific requirements for supported compilers and language standards described on the [running-an-analysis](https://docs.sonarsource.com/sonarqube-for-vs-code/getting-started/running-an-analysis "mention") page.

#### Jupyter Notebooks <a href="#jupyter-notebooks" id="jupyter-notebooks"></a>

<details>

<summary>Jupyter Notebooks in VS Code</summary>

SonarQube for VS Code v3.16+ supports analysis of Python code inside Jupyter notebooks. When opening an `.ipynb` file, SonarQube Server, or SonarQube Community Build analyze the Python code and Python cells inside your Jupyter Notebooks.

There is nothing special to do to run a SonarQube for IDE analysis; simply open a Jupyter Notebook file. As with any Jupyter Notebook, you must set up your [VS Code environment](https://code.visualstudio.com/docs/datascience/jupyter-notebooks#_setting-up-your-environment) to run a project. The usual Quick Fix and issue investigation options you are accustomed to are available.

**Managing rules**

IPython Notebooks is a new rules category in the SonarQube for IDE explorer. Go to **RULES** > **IPython Notebooks** in the **SONARQUBE SETUP** view container to enable/disable rules, just as you would any rule for other languages.

The following rules have been disabled by default for Jupyter documents because they tend to be noisy in the notebook environment:

* [ipython:S905](https://rules.sonarsource.com/python/RSPEC-905), [ipython:S1481](https://rules.sonarsource.com/python/RSPEC-1481), [ipython:S2201](https://rules.sonarsource.com/python/RSPEC-2201), [ipython:S5754](https://rules.sonarsource.com/python/RSPEC-5754)

**Connected mode**

[connected-mode](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/connected-mode "mention") will be ignored when working with Jupyter Notebooks. You will only have local analysis; this is because analysis of Jupyter Notebooks is not yet supported by SonarQube (Server, Cloud) or SonarQube Community Build.

**Magic commands**

All Magic commands are ignored by SonarQube for VS Code (for example, `%matplotlib inline` and `%%timeit`). When a line magic command is found, that line will be ignored. Similarly, when a cell magic command is found, the entire cell will be ignored. The next image below shows a normal Jupyter cell; the second image illustrates the same cell with a cell magic command. Note how SonarQube for VS Code ignores issues in the cell with the magic command.

<div align="left"><img src="https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fgit-blob-d48f2e7a026040bd55fdcd3c5cc3187a78144b38%2Ff33c93e584cdf608aebbcc5c9fe90981d1b0950a.png?alt=media" alt="" width="563"></div>

</details>

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/languages/c-family/understanding-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/languages/c-family/understanding-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/languages/c-family/understanding-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/languages/c-family/understanding-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/languages/c-family/understanding-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/languages/c-family/understanding-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/languages/c-family/understanding-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/languages/c-family/understanding-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/languages/c-family/understanding-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/c-family/understanding-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/c-family/understanding-the-analysis.md

# Understanding the analysis

### Analysis scope <a href="#analysis-scope" id="analysis-scope"></a>

For complete details, see the [setting-analysis-scope](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope "mention") pages. You can specifically set the CFamily analysis scope by changing the file extensions specified using the following SonarScanner properties: `sonar.c.file.suffixes, sonar.cpp.file.suffixes`, and `sonar.objc.file.suffixes`.

The files that are ultimately analyzed depend on the selected analysis mode:

* In Automatic analysis mode, every non-header source file within the CFamily analysis scope is analyzed individually. That’s why the `sonar.sources` property should be set to prevent the analysis of third-party code.
* In Compilation Database mode, the analyzed files represent the intersection between the CFamily analysis scope and the \`file\` entry in the `compile_commands.json`. This implies that only compiled files within the CFamily scope are analyzed. Therefore, ensuring that the `compile_commands.json` accurately encompasses the entire project is advisable.
* In both modes, header files get analyzed in the context of the source files in which they are included. This means header files not included in any source file will not be analyzed.

### Measures for header files <a href="#measures-for-header-files" id="measures-for-header-files"></a>

Each time a header file is analyzed as part of a compilation unit, the measures are computed for this header: statements, functions, classes, cyclomatic complexity, and cognitive complexity. Each measure may be computed more than once for a given header. In that case, the largest value is stored for each measure.

### Language-specific rule tags <a href="#languagespecific-rule-tags" id="languagespecific-rule-tags"></a>

On top of the [built-in-rule-tags](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/built-in-rule-tags "mention"), a few additional rule tags are specific to C/C++/Objective-C rules.

#### C++ standard version-related rule tags <a href="#c-standard-versionrelated-rule-tags" id="c-standard-versionrelated-rule-tags"></a>

Some rules are relevant only since a specific version of the C++ standard. These rules will run only when analyzing a C++ code compiled against a later or equal standard version. The following tags are used to mark these rules for the corresponding C++ standard version:

* `since-c++11`
* `since-c++14`
* `since-c++17`
* `since-c++20`
* `since-c++23`

C++ rules not carrying any of these four tags started running since C++98.

#### Implementation-related rule tags <a href="#implementationrelated-rule-tags" id="implementationrelated-rule-tags"></a>

* `full-project`: This tag is for rules that do cross-compilation unit analysis. For these rules to work properly, it is important to analyze the entire project. Excluding part of the project from the analysis will impact the accuracy of these rules: it might lead to false positives or negatives.
* `symbolic-execution`: this tag is for rules that reason about the program’s state. They usually work together to find path-sensitive bugs and vulnerabilities. Once a fatal state of the program is reached, one issue will be raised, and the symbolic execution analysis of the current path will stop. For that reason, evaluating these rules independently of each other is not recommended as it might give a false sense of undetected issues. It is important to keep in mind that Sonar is always working on improving these rules, as symbolic execution can never be perfect.

#### External standard rule tags <a href="#external-standard-rule-tags" id="external-standard-rule-tags"></a>

The following tags indicate how a rule relates to the MISRA guidelines:

* `based-on-misra`: This tag is for rules that address the same issues as MISRA rules but only partially correspond to what MISRA specifies (usually to make them less strict).
* `misra-c++2008`
* `misra-c++2023`
* `misra-c2004`
* `misra-c2012`

The following tags represent the category of the rule according to the [MISRA compliance 2020](https://www.misra.org.uk/app/uploads/2021/06/MISRA-Compliance-2020.pdf) document and indicate whether violations of the rule are permitted (see Chapter 5: "The guideline re-categorization plan"):

* `misra-mandatory`
* `misra-required`
* `misra-advisory`

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/user-guide/clean-code/code-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/user-guide/clean-code/code-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/user-guide/clean-code/code-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/core-concepts/clean-code/code-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/core-concepts/clean-code/code-analysis.md

# Code analysis based on Clean Code

The Sonar automated code review aims to identify any issue in your code that prevents it from being Clean Code.

Each Clean Code attribute is evaluated, for a given language, based on a series of rules:

* Each rule:
  * Is associated with the Clean Code attribute it evaluates.
  * Is associated with the software quality(ies) to which this Clean Code attribute contributes.\
    Each associated software quality (security, reliability, or maintainability) is assigned a severity (critical, high, medium, low, or info). This severity determines how much that software quality is impacted when the rule is broken.
* When a rule is broken, an issue is raised. The issue affects one or more software qualities with varying severity as inherited from the rule.

The figure below shows the Clean-Code-based analysis principles of the Sonar solution.

![](https://312504542-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiJj3TXBdWssTGGg8qK5I%2Fuploads%2Fgit-blob-03e390a9a928acccbbae45afb72b5f26b7ef226b%2F825606b23737ebed089bd0bfa7fea4e5d21d4e87.png?alt=media)

Check the [definition](https://docs.sonarsource.com/sonarqube-server/10.8/core-concepts/clean-code/definition "mention") page for details about Clean Code attributes, and the [software-qualities](https://docs.sonarsource.com/sonarqube-server/10.8/core-concepts/clean-code/software-qualities "mention") page to better understand software qualities.

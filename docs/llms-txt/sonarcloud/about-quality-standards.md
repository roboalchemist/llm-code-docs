# Source: https://docs.sonarsource.com/sonarqube-server/10.7/core-concepts/clean-as-you-code/about-quality-standards.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/core-concepts/clean-as-you-code/about-quality-standards.md

# About quality standards

In the Sonar solution, each of your projects has a set quality standard, made up of a quality profile and a quality gate:

* A quality profile determines the set of [overview](https://docs.sonarsource.com/sonarqube-server/10.8/user-guide/rules/overview "mention") that apply during analysis.
* A quality gate consists of a set of conditions against which the code is measured during analysis. Depending on the result, the code will pass or fail the quality gate, giving developers indications on whether to fix issues or merge the code.

#### Quality profile <a href="#quality-profile" id="quality-profile"></a>

We recommend using the built-in quality profile, called Sonar way. For details, see the [quality-profiles](https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/analysis-functions/quality-profiles "mention") page.

#### Quality gate <a href="#quality-gate" id="quality-gate"></a>

By default, SonarQube Server and SonarQube Cloud implement a recommended quality gate called the Sonar way. For details, see the section about Sonar Way and Clean as You code on the [quality-gates](https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/analysis-functions/quality-gates "mention") page.

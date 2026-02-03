# Source: https://docs.sonarsource.com/sonarqube-cloud/discovering-sonarcloud/developing-with-sonar.md

# Developing with Sonar

The SonarQube solution helps developers perform automated code analysis and reviews at every stage of the development process:

* SonarQube for IDE provides immediate feedback in your IDE as you write code so you can find, focus on, and fix anticipated issues before a commit.
* SonarQube Cloud’s PR analysis fits into your cloud-based CI/CD workflows so that you merge high-quality code every time.
* Quality gates keep code with issues from being released to production. See [about-new-code](https://docs.sonarsource.com/sonarqube-cloud/standards/about-new-code "mention") for more details.

Organizations start with a set of default rules called the Sonar Way Quality Profile. Quality profiles define the set of [rules](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/rules "mention") to be applied during code review and analysis. The Sonar Way can be customized per project to satisfy different technical requirements. See [understanding-quality-profiles](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/understanding-quality-profiles "mention") for more information.

A quality gate is an indicator of code quality that can be configured to give a green or red light on the current release-worthiness of your code. It indicates whether your code complies with the quality standards and can move forward. See [introduction-to-quality-gates](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/introduction-to-quality-gates "mention") for more information.

* A **Passed** (green) quality gate means the code meets your standard and is ready to be merged.
* A **Failed** (red) quality gate means there are issues to address.

SonarQube Cloud provides feedback through its UI, email, and in decorations on pull or merge requests to notify your team that there are issues to address. SonarQube Cloud also provides in-depth guidance on the issues telling you why each issue is a problem and how to fix it, adding a valuable layer of education for developers of all experience levels.

Feedback can also be obtained during automated code review in [connected-mode](https://docs.sonarsource.com/sonarqube-cloud/improving/connected-mode "mention") when running in Connected Mode. SonarQube for IDE helps developers find, focus on, and fix anticipated issues before a commit. Together, SonarQube for IDE and SonarQube Cloud help developers address issues effectively, so only high-quality code that passes the quality gate is promoted.

Explore [featured public projects](https://sonarcloud.io/explore/projects) on SonarQube Cloud and experience how other organizations leverage the platform to improve their code.

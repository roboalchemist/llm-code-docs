# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/codemagic.md

# Codemagic

Once your project is created and initiated from the repository you selected, follow [this tutorial](https://blog.codemagic.io/sonarqube-integration-with-codemagic/#connecting-with-sonarcloud) to set up your project.

SonarQube Cloud is integrated with Codemagic to automatically configure pull-request and branch information. All you have to do is configure the `sonar.host.url`, `sonar.organization`, and `sonar.projectKey` parameters.

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/circleci.md

# CircleCI

Once your project is created and initiated from the repository you selected, follow our [official Orb Quick Start Guide](https://circleci.com/orbs/registry/orb/sonarsource/sonarcloud) to set up your project using Maven, Gradle, and other build technologies. Check also [our Orb’s readme](https://github.com/SonarSource/sonarcloud-circleci-orb/blob/master/README.md).

Limitations:

* Make (for C/C++ projects) and MSBuild are not yet supported.
* The Orb is currently available only for Linux and x64 architecture.

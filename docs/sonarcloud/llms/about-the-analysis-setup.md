# Source: https://docs.sonarsource.com/sonarqube-server/10.7/core-concepts/clean-as-you-code/about-the-analysis-setup.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/core-concepts/clean-as-you-code/about-the-analysis-setup.md

# About the analysis setup

To successfully practice the Clean as You Code methodology, we recommend deploying the analysis at three different levels:

![](https://312504542-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiJj3TXBdWssTGGg8qK5I%2Fuploads%2Fgit-blob-22103f609707231e15ef3a4fbb29ad8fa1c973ee%2Fe8668727e4529f3d2348b4466350feab07eb213d.png?alt=media)

* The first base layer is code analysis in your [Intellij](https://app.gitbook.com/o/2ibCvzwZt86Nlk2zloB7/s/NvI4wotPmITyM0mnsmtp/ "mention"). This allows issues to be fixed as soon as they are introduced.
* The pull request analysis layer ensures that all code to be merged is clean.
* The branch analysis layer guarantees that the main branch or another branch is ready for release or deployment.

Each layer has advantages in terms of speed and depth of analysis. We recommend implementing all three for the most comprehensive experience.

For setup instructions, see [setting-up-clean-as-you-code](https://docs.sonarsource.com/sonarqube-server/10.8/project-administration/setting-up-clean-as-you-code "mention").

# Source: https://docs.sonarsource.com/sonarqube-cloud/discovering-sonarcloud/what-sonarcloud-can-do.md

# What SonarQube Cloud can do

SonarQube Cloud’s code review and analysis is designed to help you achieve a state of high-quality code, that is, code with attributes that contribute to making your software reliable, maintainable, and secure.

To do this, SonarQube Cloud identifies both *issues* and *security hotspots* in your code.

Explore [featured public projects](https://sonarcloud.io/explore/projects) on SonarQube Cloud and experience how other organizations leverage the platform to improve their code.

### Issues <a href="#what-sonar-can-do" id="what-sonar-can-do"></a>

In SonarQube Cloud terminology, an issue is a problem in your code that requires fixing. When scanning for issues, the automated code review algorithms are purposely conservative. They are designed to minimize the number of false positives, that is, things wrongly identified as problems. If the code analysis identifies an issue, you can be quite confident that it really is something that should be fixed. SonarQube Cloud will not overwhelm the developer with false alarms concerning issues.

For details, see the Issues [introduction](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/introduction "mention") page.

### Security hotspots <a href="#security-hotspots" id="security-hotspots"></a>

Security hotspots are areas of the code that may cause security issues and therefore need to be reviewed. By design, automated code review is more permissive when identifying security hotspots than when identifying vulnerabilities and other issues. An issue is almost always a real problem, while a security hotspot can often be a false alarm (but it is still worth checking). By separating hotspots from issues, SonarQube Cloud maintains the accuracy of its issue detection while still providing developers with useful warnings under the less stringent criteria of the hotspot

### Where SonarQube Cloud fits In <a href="#where-sonarcloud-fits-in" id="where-sonarcloud-fits-in"></a>

SonarQube Cloud is designed to be integrated into your CI/CD workflow in order to intervene early when coding, allowing you to remediate fresh issues rapidly and prevent them from reaching production. It does so in three different places: In the IDE, in the pull request, and in the codebase.

#### In the IDE <a href="#in-the-ide" id="in-the-ide"></a>

SonarQube Cloud’s companion product, [connected-mode](https://docs.sonarsource.com/sonarqube-cloud/improving/connected-mode "mention"), provides developers with immediate feedback through its automated code review, right in the IDE, catching issues before they even get to the repository. SonarQube for IDE is the first line of defense to find and fix issues in real time, ensuring the quality of the code and enhancing productivity.

Supporting 25 languages and the most popular IDEs, SonarQube for IDE leverages over 5,000 language-specific rules to instantly highlight common coding mistakes and vulnerabilities. In parallel, SonarQube for IDE provides rich contextual educational guidance to help developers improve their skills while resolving the issue.

Sonar’s IDE extensions are available for IntelliJ (and other JetBrains IDEs including IntelliJ IDEA, CLion, WebStorm, PHPStorm, PyCharm, Rider, Android Studio & RubyMine), Visual Studio, VS Code, and Eclipse, and can be installed directly from your IDE’s plugin marketplace.

Much like a spellchecker, automated code review in SonarQube for IDE highlights problems in your code using error squiggles, provides quick fixes, and gives you detailed information about issues found in your code.

In Connected Mode, SonarQube for IDE becomes part of the full SonarQube solution that integrates code review and analysis throughout your development process from IDE to CI pipeline to DevOps platform, helping to make sure that only high-quality code makes it into your project. For more information, see the Connected Mode pages in the SonarQube for IDE docs:

* [Connected mode](https://docs.sonarsource.com/sonarqube-for-intellij/connect-your-ide/connected-mode) - SonarQube for IntelliJ
* [Connected mode](https://docs.sonarsource.com/sonarqube-for-visual-studio/connect-your-ide/connected-mode) - SonarQube for Visual Studio
* [Connected mode](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/connected-mode) - SonarQube for VS Code
* [Connected mode](https://docs.sonarsource.com/sonarqube-for-eclipse/connect-your-ide/connected-mode) - SonarQube for Eclipse

#### In the pull request <a href="#in-the-pull-request" id="in-the-pull-request"></a>

Pull requests (on some platforms, called "merge requests") are a mechanism to allow developers to collaborate more effectively. They enable a developer to ask others to review their work (usually their *personal feature branch*) prior to it being merged into the main body of the code, or *main branch*. In the DevOps platform, the pull request is displayed in a dedicated interface that allows the reviewer to see the changes proposed and to either approve or deny the merge.

SonarQube Cloud annotates the pull requst interface of the repository service, providing the results of its code review and analysis on the pull request branch right in the interface and granting or denying approval of the pull request depending on quality gate criteria. In effect, this augments human code review with automatic code review. This feature is often called pull request decoration because it "decorates" the pull request interface with additional information.

#### In the codebase <a href="#in-the-codebase" id="in-the-codebase"></a>

Code review and analysis at the IDE and pull request level helps to identify problems before they are merged into the main codebase. However, there are some types of issues and hotspots that can only be found after the code is merged. To find these types of problems, SonarQube Cloud needs to analyze the entire codebase as a single unit and (in the case of some languages) also analyze the results of compiling the code. To do this, SonarQube Cloud offers two approaches: *automatic analysis* and *CI-based analysis*.

### Automatic analysis <a href="#automatic-analysis" id="automatic-analysis"></a>

With automatic analysis, SonarQube Cloud detects every change to your pull requests or main branch and analyzes the new state of the code in your repository. It uses the same set of analysis methods as CI-based analysis (see below) but it is subject to the following restrictions:

* It only works with GitHub (as of today).
* It does not work on repositories that were imported as monorepos into SonarQube Cloud.
* It does not work on all SonarQube Cloud supported languages.

However, if you are using GitHub and the project you imported is in a language that is supported by automatic analysis, then no configuration is needed for analysis to occur so you can start improving your code quality right away. For details, see the [automatic-analysis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/automatic-analysis "mention") page.

Because automatic analysis does not work with providers other than GitHub or with certain compiled languages, there are many cases where you will need to configure CI-based analysis instead.

### CI-based analysis <a href="#ci-based-analysis" id="ci-based-analysis"></a>

A CI-based analysis refers to the configuration of SonarQube Cloud so that it performs code review and analysis as part of your regular continuous integration (CI) process, in other words, your build process.

To enable CI-based analysis you have to install and configure a piece of software called a *scanner*. SonarQube Cloud offers scanner extensions and integrations for all of the leading *continuous integration* (CI) systems used today.

Typically, the scanner is configured to run as part of your continuous integration pipeline so that whenever you push changes to your repository, the scanner is invoked and performs a scan on the code.

The details of how SonarQube Cloud is integrated with your CI/CD process depend on which build tools and the continuous integration system you use. SonarQube Cloud provides custom integrations for the following:

* GitHub Actions
* Bitbucket Pipelines
* Azure Pipelines
* make
* npm
* Maven
* Gradle
* .NET
* Jenkins
* TravisCI
* CircleCI

Additionally, SonarQube Cloud also offers a stand-alone command-line tool (called SonarScanner) that you can install and integrate into your build process manually. For an overview on the SonarScanner, see the [overview-of-integrated-cis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/overview-of-integrated-cis "mention") page.

The results of the scan are sent automatically to SonarQube Cloud where they are processed and made available in the dashboard, that is, the SonarQube Cloud interface itself. There you will find all the results of all code analyzed in your repositories. You can sort and filter the results according to a wide range of criteria in order to get a clear picture of the state of your code.

Additionally, the outcome of the SonarQube Cloud analysis (in both automatic and CI-based analyses) can be used to control subsequent build actions such as automatic deployment, etc.

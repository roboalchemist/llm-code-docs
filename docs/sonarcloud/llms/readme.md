# Source: https://docs.sonarsource.com/sonarqube-mcp-server/readme.md

# Source: https://docs.sonarsource.com/sonarqube-community-build/readme.md

# Source: https://docs.sonarsource.com/sonarqube-for-eclipse/readme.md

# Source: https://docs.sonarsource.com/sonarqube-for-visual-studio/readme.md

# Source: https://docs.sonarsource.com/sonarqube-for-intellij/readme.md

# Source: https://docs.sonarsource.com/sonarqube-for-vs-code/readme.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/readme.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/readme.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/readme.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/readme.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/readme.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/readme.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/readme.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/readme.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/readme.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/readme.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/readme.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/readme.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/readme.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/readme.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/readme.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/readme.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/readme.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/readme.md

# Source: https://docs.sonarsource.com/sonarqube-server/readme.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/readme.md

# Homepage

### What is SonarQube Cloud? <a href="#achieving-high-quality-code" id="achieving-high-quality-code"></a>

SonarQube Cloud is an industry standard Software-as-a-Service (SaaS) automated code review and static analysis tool designed to detect coding issues in more than [30+ languages, frameworks, and IaC platforms](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/overview). By integrating directly with your [CI pipeline](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/overview-of-integrated-cis) or one of the supported [DevOps platforms](https://docs.sonarsource.com/sonarqube-cloud/getting-started/sign-up), your code is checked against an extensive set of rules that cover many attributes of code, such as maintainability, reliability, and security issues, on each merge/pull request.

SonarQube Cloud extends your DevOps experience by performing automated code checks within minutes. Please have a look at the Discovering SonarQube Cloud section to learn more about [what-sonarcloud-can-do](https://docs.sonarsource.com/sonarqube-cloud/discovering-sonarcloud/what-sonarcloud-can-do "mention"). For on-premise code repositories, see the SonarQube Server [Server 2025.4 LTA](https://app.gitbook.com/o/2ibCvzwZt86Nlk2zloB7/s/yDv2XwTC1xoOKBYeCK45/ "mention") documentation.

Additionally, you can explore [featured public projects](https://sonarcloud.io/explore/projects) on SonarQube Cloud and experience how other organizations leverage the platform to improve their code.

### Achieving high quality code <a href="#achieving-high-quality-code" id="achieving-high-quality-code"></a>

SonarQube sets high standards for all code that results in secure, reliable, and maintainable software that is essential to maintaining a healthy codebase. This applies to all code: source code, test code, infrastructure as code, glue code, scripts, and more.

All new code, whether added or recently modified, should adhere to quality standards. SonarQube achieves this by providing automated code reviews that alert you to potential issues within your new code. This helps you maintain high standards and focus on code quality, ultimately leading to a healthier codebase over time.

SonarQube Cloud comes with a built-in quality profile designed for each supported language, called the Sonar way profile. The Sonar way activates a set of rules that should be applicable to most projects and is a starting point to help you implement good practices in your organization.

### The SonarQube solution <a href="#the-sonarqube-solution" id="the-sonarqube-solution"></a>

SonarQube is designed to help you achieve a state of high quality code. By linking SonarQube for IDE with SonarQube Cloud or SonarQube Server, the automated code analysis and reviews are performed at every stage of the development process. We call this the SonarQube solution. This means your project settings, new code definitions, and the quality profiles managed in SonarQube Cloud are applied locally to an analysis in the IDE.

* [SonarQube for IDE](https://app.gitbook.com/o/2ibCvzwZt86Nlk2zloB7/s/6LPRABg3ubAJhpfR5K0Y/) brings automated code reviews directly into your development environment, helping you catch issues as you write code. By providing immediate feedback, it enables engineers to identify and fix problems before they even commit, ensuring cleaner, higher-quality code from the start.
* Then, [SonarQube Server](https://app.gitbook.com/s/yDv2XwTC1xoOKBYeCK45/analyzing-source-code/pull-request-analysis) and [SonarQube Cloud](https://docs.sonarsource.com/sonarqube-cloud/improving/pull-request-analysis) deliver powerful static code analysis by thoroughly reviewing each pull request before it’s merged. This proactive approach adds an essential layer of protection, ensuring code quality and preventing issues from entering your codebase.
* Finally, [SonarQube Server](https://app.gitbook.com/s/yDv2XwTC1xoOKBYeCK45/quality-standards-administration) and [SonarQube Cloud](https://docs.sonarsource.com/sonarqube-cloud/standards) seamlessly integrate into your CI/CD pipeline, analyzing code on every build. By leveraging quality profiles and quality gates, they automatically block code with issues from being released to production, ensuring only maintainable, reliable, and secure code makes it through.

The SonarQube solution helps you incorporate a proper methodology by helping engineers pay attention to new code. Focusing on writing high quality new code during development ensures that all code released for production will be incrementally improved over time.

### Connected Mode <a href="#connected-mode" id="connected-mode"></a>

Connected mode joins SonarQube Cloud with SonarQube for IDE to deliver the full SonarQube solution. While in connected mode, SonarQube Cloud sends notifications to SonarQube for IDE when a quality gate changes or a new issue is assigned to the user. Smart notifications can be enabled or disabled from the SonarQube for IDE UI while creating or editing the connection settings. In addition, SonarQube for IDE helps the engineer focus on writing high quality code by using the new code definition on the server.

Be sure to check out all of the [#connected-mode-benefits](https://docs.sonarsource.com/sonarqube-cloud/improving/connected-mode#connected-mode-benefits "mention").

### Getting started <a href="#getting-started" id="getting-started"></a>

Now that you’ve heard about how [SonarQube Cloud](https://www.sonarsource.com/products/sonarcloud/) can help you write high quality code, you are ready to try out SonarQube Cloud for yourself. After signing up for SonarQube Cloud using the login from your DevOps platform account (see [sign-up](https://docs.sonarsource.com/sonarqube-cloud/getting-started/sign-up "mention")), you can import your organizations and repositories to set up a [first analysis](https://docs.sonarsource.com/sonarqube-cloud/getting-started/first-analysis).

The [ci-based-analysis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis "mention") pages explain how to connect your scanner to your CI pipeline and provides instructions for analyzing your project’s branches and pull requests.

Here's a page with everything you need to learn [what-sonarcloud-can-do](https://docs.sonarsource.com/sonarqube-cloud/discovering-sonarcloud/what-sonarcloud-can-do "mention").

### Learn more <a href="#learn-more" id="learn-more"></a>

Check out the entire suite of Sonar products on the main website: [SonarQube Server](https://www.sonarsource.com/products/sonarqube/), [SonarQube Cloud](https://www.sonarsource.com/products/sonarcloud/), and [SonarQube for IDE](https://www.sonarsource.com/products/sonarlint/).

Then, have a look at how to fix issues detected by SonarQube for [IntelliJ](https://app.gitbook.com/s/NvI4wotPmITyM0mnsmtp/using/fixing-issues), [Visual Studio](https://app.gitbook.com/s/5CSDwdOaYoOAGYNiRqgl/using/fixing-issues), [VS Code](https://app.gitbook.com/s/6LPRABg3ubAJhpfR5K0Y/using/fixing-issues), and [Eclipse](https://app.gitbook.com/s/kadXEH8HkykK7lKaDvVq/using/fixing-issues) when combined with managing your code issues in [SonarQube Server](https://app.gitbook.com/s/yDv2XwTC1xoOKBYeCK45/user-guide/issues/introduction) and [SonarQube Cloud](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/introduction), and browse a full list of [Sonar Rules and Rule Descriptions](http://rules.sonarsource.com/) available for static code analysis.

#### More getting started resources <a href="#more-getting-started-resources" id="more-getting-started-resources"></a>

* [sign-up](https://docs.sonarsource.com/sonarqube-cloud/getting-started/sign-up "mention")
* [advanced-setup](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup "mention") and [automatic-analysis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/automatic-analysis "mention")
* [managing-quality-profiles](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles "mention")
* [managing-portfolios](https://docs.sonarsource.com/sonarqube-cloud/managing-portfolios "mention")

And if you need help, visit our [online community](https://community.sonarsource.com/c/sc/9) to search for answers and reach out with questions!

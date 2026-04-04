# Source: https://docs.sonarsource.com/sonarqube-mcp-server/quickstart-guide.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/quickstart-guide.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/quickstart-guide.md

# Source: https://docs.sonarsource.com/sonarqube-server/quickstart-guide.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/quickstart-guide.md

# Quickstart guide

By completing this guide you will:

1. [Set up your SonarQube Cloud account](#set-up-your-sonarqube-cloud-account)
   1. Set up your Organization
   2. Upgrade to Enterprise
      1. SSO via SAML
2. [Onboard projects](#onboard-your-projects)
3. [Configure CI analysis](#configure-your-ci-analysis)
4. [Integrate with SonarQube for IDE](#connect-with-sonarqube-for-ide)
5. [Review quality gates](#review-your-quality-gates)
   1. Review pull/merge request analysis for failed quality gates.
   2. Configure pull request decoration on your DevOps platform

### Set up your SonarQube Cloud account

We use an [organization-based structure](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/ressources-structure/organization) that mirrors the structure on your chosen DevOps platforms.

Create an organization based on:

* [GitHub](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-github-organization)
* [BitBucket Cloud](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-bitbucket-workspace)
* [GitLab](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-gitlab-group)
* [Azure DevOps](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-azure-devops-organization)

Consider upgrading to [Enterprise](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans) so you can begin [setting-up-sso](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/setting-up-sso "mention").

### Onboard your projects

Import repositories from your DevOps platform to create projects:

* [GitHub](https://docs.sonarsource.com/sonarqube-cloud/getting-started/github)
* [Bitbucket Cloud](https://docs.sonarsource.com/sonarqube-cloud/getting-started/bitbucket-cloud)
* [GitLab](https://docs.sonarsource.com/sonarqube-cloud/getting-started/gitlab)
* [Azure DevOps](https://docs.sonarsource.com/sonarqube-cloud/getting-started/azure-devops)

### Configure your CI analysis

Set up analysis for your imported projects:

* [GitHub](https://docs.sonarsource.com/sonarqube-cloud/getting-started/github#set-up-your-analysis)
* [Bitbucket Cloud](https://docs.sonarsource.com/sonarqube-cloud/getting-started/bitbucket-cloud#set-up-your-analysis)
* [GitLab](https://docs.sonarsource.com/sonarqube-cloud/getting-started/gitlab#set-up-your-analysis)
* [Azure DevOps](https://docs.sonarsource.com/sonarqube-cloud/getting-started/azure-devops#set-up-your-analysis)

Now that you can review the [main branch’s analysis](https://docs.sonarsource.com/sonarqube-cloud/improving/main-branch-analysis) on any of your imported projects.

### Connect with SonarQube for IDE

Have your developers install [connected-mode](https://docs.sonarsource.com/sonarqube-cloud/improving/connected-mode "mention") to leverage the power of SonarQube in their IDE.

### Review your quality gates

The purpose of [quality-gates](https://docs.sonarsource.com/sonarqube-cloud/improving/quality-gates "mention") is to tell you whether your code is good enough to be pushed to the next step:

* For the main branch and other long-lived branches, the quality gate answers the question: "Can I release my code today?"
* For pull requests (and short-lived branches), the quality gate answers the question: "Can I merge this pull request?"

By setting up [pull-request-analysis](https://docs.sonarsource.com/sonarqube-cloud/improving/pull-request-analysis "mention"), you ensure pull requests are analyzed when they are opened and every time a change is pushed to the pull request branch. You can also configure [pull request decoration](https://docs.sonarsource.com/sonarqube-cloud/improving/pull-request-analysis#pull-request-decoration) to allow your developers to view the analysis from SonarQube Cloud directly on the PRs they submit.

By keeping an eye on the quality gates, the decision makers can quickly judge the status of code and decide what to do next.

### Develop with Sonar

Now that you have seen the benefits of using [SonarQube Cloud](https://docs.sonarsource.com/sonarqube-cloud/discovering-sonarcloud/what-sonarcloud-can-do) with your DevOPs platforms, managers and tech leads can check out the [security reports](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/security-reports) and [portfolios](https://docs.sonarsource.com/sonarqube-cloud/managing-portfolios) features to begin monitoring the security and releasability of projects.

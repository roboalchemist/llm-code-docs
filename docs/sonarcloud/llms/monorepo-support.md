# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/monorepo-support.md

# Monorepo support

SonarQube Cloud supports repositories that use the monorepo strategy.

### What is a monorepo? <a href="#monorepo-support" id="monorepo-support"></a>

Traditionally, software projects have been organized so that each project is stored within a single, distinct repository of its own.

As software projects have become more complex and interconnected, some organizations have moved to having all their projects in a single large repository. This is called the **monorepo strategy**.

In a typical monorepo, each project occupies its own directory within the repository and each is independently buildable and deployable, though the exact setup depends on how the procedures that build each project are defined. In general, there are many ways that multiple projects can be arranged within a single repository.

Fortunately, SonarQube Cloud’s support for the monorepo strategy does not depend on the specifics of the monorepo setup. SonarQube Cloud relies on the fact that each build procedure can be configured to perform the analysis for its particular project in the repository and send the result to the corresponding SonarQube Cloud project.

### About the monorepo support in SonarQube Cloud <a href="#monorepos-on-sonarcloud" id="monorepos-on-sonarcloud"></a>

In a standard setup, each SonarQube Cloud project corresponds to a single repository. In a monorepo setup, multiple SonarQube Cloud projects, each corresponding to a separate monorepo project, are all bound to the same repository. This way:

* The analysis setup of each project in the monorepo is easier.
* When you do an analysis, information from SonarQube Cloud that appears in the pull request view is clearly distinguished by project name.
* The monorepo associated with a project is shown in the SonarQube Cloud UI.

See the [binding-with-dop](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/ressources-structure/binding-with-dop "mention") page for information about project binding.

Currently, monorepo support is available for GitHub, Bitbucket Cloud, Azure DevOps and GitLab repositories. Note that the analysis of a monorepo configuration is only supported for the CI-based analysis , not for the automatic analysis.

### Setting up the analysis of your monorepo <a href="#set-up-overview" id="set-up-overview"></a>

Once you have set up your monorepo in SonarQube Cloud, you can add the SonarQube Cloud analysis to your monorepo’s CI pipeline.

#### Before your start

A wizard will guide you through setting up your monorepo in SonarQube Cloud. However, you will need to manually create each project within the monorepo during this process, as SonarQube Cloud cannot detect projects within a monorepo. To create the projects of a monorepo, you need the **Create Projects** permission in your organization.

Each SonarQube Cloud project must have a key unique across SonarQube Cloud (see [#project-identification](https://docs.sonarsource.com/sonarqube-cloud/analysis-parameters/parameters-not-settable-in-ui#project-identification "mention")). This is the key that you will use when you configure your CI service. We recommend using a pattern that includes your organization name, the monorepo name, and an internal reference to the project within the monorepo (for example, `myorg_mymonorepo_myproject`).

#### Step 1: Set up your monorepo in SonarQube Cloud <a href="#create-projects" id="create-projects"></a>

During this step, you will import your monorepo to SonarQube Cloud. Each project within the monorepo must be created manually.

Proceed as follows:

1. Select the ✚ (plus) menu on the top right of the SonarQube Cloud interface and select **Analyze new project**. The **Analyze projects** page opens.

<figure><img src="broken-reference" alt="Select the monorepo link to the right of the Organization field to open the monorepo setup wizard."><figcaption></figcaption></figure>

2. Select **Setup a monorepo** (it is a small text link to the right of the **Organization** field). The **Analyze monorepo projects** page opens.
3. In **Organization**, select your organization.
4. In **Repository**, select the monorepo that you want to import.
5. Create the projects within your monorepo. For each project within your monorepo:
   1. Select the **Add new project** button.
   2. Review the proposed project name and key.

<div align="center"><figure><img src="broken-reference" alt="Select the Add new project button to create each project within your monorepo."><figcaption></figcaption></figure></div>

5. Once you’ve completed the project list, select the **Set up monorepo** button. The **Set up new code** page opens.
6. Select the New Code Definition (NCD) you want to apply by default to the SonarQube Cloud projects in the monorepo. More information about defining your NCD is on the [Defining new code](https://app.gitbook.com/s/eu7dHWcqP9Cr3eUAzwWg/project-administration/clean-as-you-code-settings/defining-new-code "mention") page.
7. Select the **Create projects** button.

{% hint style="info" %}
If you select a repository that is already bound to SonarQube Cloud, then this creates new projects as part of a monorepo setup and converts the existing project, which is bound to the selected repository, to the monorepo.
{% endhint %}

#### Step 2: Add the SonarQube Cloud analysis to your monorepo’s CI pipeline <a href="#configure-ci-pipeline" id="configure-ci-pipeline"></a>

To perform the configuration, follow the procedure for your CI service:

* [github-actions-for-sonarcloud](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/github-actions-for-sonarcloud "mention")
* [bitbucket-pipelines-for-sonarcloud](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/bitbucket-pipelines-for-sonarcloud "mention")
* [introduction](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/introduction "mention") to Azure pipelines&#x20;
* [gitlab-ci](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/gitlab-ci "mention")
* [circleci](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/circleci "mention")
* [other-cis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/other-cis "mention")

In the build procedure for each monorepo project, make sure to specify the SonarQube Cloud project key that you designated for it. This provides the binding between the project within the monorepo and the corresponding project in SonarQube Cloud. This enables SonarQube Cloud to correctly process the analysis results and to dispatch pull request decorations back to the DevOps platform for each project individually; see the [pull-request-analysis](https://docs.sonarsource.com/sonarqube-cloud/improving/pull-request-analysis "mention") page for information on decorating your pull request.

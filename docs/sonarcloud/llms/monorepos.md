# Source: https://docs.sonarsource.com/sonarqube-server/10.5/project-administration/monorepos.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/project-administration/monorepos.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/project-administration/monorepos.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/project-administration/monorepos.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/project-administration/monorepos.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/project-administration/monorepos.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/project-administration/monorepos.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/project-administration/monorepos.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/project-administration/monorepos.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/project-administration/monorepos.md

# Source: https://docs.sonarsource.com/sonarqube-server/project-administration/monorepos.md

# Managing monorepo projects

The monorepo feature is supported starting in [Enterprise Edition](https://www.sonarsource.com/plans-and-pricing/enterprise/). It requires that the DevOps platform integration with GitHub, GitLab, Azure DevOps, or Bitbucket has been properly set up.

{% hint style="warning" %}
The blocking of pull request merge when the quality gate fails is not supported for monorepos.
{% endhint %}

### What is a monorepo? <a href="#what-is-a-monorepo" id="what-is-a-monorepo"></a>

Traditionally, software projects have been organized so that each project is stored within a single, distinct repository of its own.

As software projects have become more complex and interconnected, some organizations have moved to having all their projects in a single large repository. This is called the monorepo strategy.

In a typical monorepo, each project occupies its own directory within the repository and each is independently buildable and deployable, though the exact setup depends on how the procedures that build each project are defined. In general, there are many ways that multiple projects can be arranged within a single repository.

Fortunately, SonarQube Server’s support for the monorepo strategy does not depend on the specifics of the monorepo setup. SonarQube Server relies on the fact that each build procedure can be configured to perform the analysis for its particular project in the repository and send the result to the corresponding SonarQube Server project.

### About the monorepo support in SonarQube Server <a href="#create-projects" id="create-projects"></a>

In a monorepo setup, multiple SonarQube Server projects, each corresponding to a separate monorepo project, are all bound to the same repository. This way:

* The analysis setup of each project in the monorepo is easier.
* The quality gate status report of pull requests in your DevOps platform is clearly distinguished by project name.
* The monorepo associated with a project is shown in the SonarQube Server UI.

### Setting up the analysis of your monorepo

Once you have set up your monorepo in SonarQube Server, you can add the SonarQube analysis to your monorepo’s CI pipeline.

#### Before your start

A wizard will guide you through setting up your monorepo in SonarQube Server. However, you will need to manually create each project within the monorepo during this process, as SonarQube Server cannot detect projects within a monorepo. To create the projects of a monorepo, you need the **Create Projects** permission in SonarQube Server.

Each SonarQube Server project must have a key unique across SonarQube Server. This is the key that you will use when you configure your CI service. We recommend using a pattern that includes the monorepo name, and an internal reference to the project within the monorepo (for example, `mymonorepo_myproject`).

#### Step 1: Set up your monorepo in SonarQube Server

During this step, you will import your monorepo to SonarQube Server. Each project within the monorepo must be created manually.

Proceed as follows:

1. In the top navigation bar of SonarQube Server, select **Projects**.
2. In the top right corner, select **Create Project > From \[DevOps platform]**. The **Project onboarding** page opens.
3. Select **Set up a monorepo**. The **Monorepo project onboarding** page opens. The **Create new projects** section opens with a first project.
4. Check and complete the proposed project name and key.
5. Select **Add new project** to add additional projects.
6. Once you’ve completed the project list, select **Next**. The **Set up new code** page opens.
7. Select the new code definition to be applied by default to the SonarQube Server projects in the monorepo. Once the projects have been created, you can change the new code definition applying to a given project, see below.
8. Select **Create projects**. The **Projects** page opens and displays the newly created projects at the top.

{% hint style="info" %}
If you configure in the **Monorepo project onboarding** page a repository already bound to a standard project then this standard project will be converted to a monorepo project.
{% endhint %}

#### Step 2: Add the SonarQube analysis to your monorepo’s CI pipeline

To perform the configuration, follow the procedure for your CI service:

* GitLab CI/CD: [#monorepo](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/gitlab-integration/adding-analysis-to-gitlab-ci-cd#monorepo "mention")
* GitHub Actions workflow:[#monorepo](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/github-integration/adding-analysis-to-github-actions-workflow#monorepo "mention")
* Azure Pipelines: [monorepo-projects](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/monorepo-projects "mention")
* Bitbucket Pipelines: [#monorepo](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-cloud-integration/bitbucket-pipelines#monorepo "mention")

### Removing a project from a monorepo <a href="#remove-project" id="remove-project"></a>

You can remove a project from a monorepo provided you are an administrator of the project:

1. Go to the project page.
2. Select **Project settings > General settings > \[DevOps platform] Integration** and uncheck **Enable monorepo support**.\
   Re-selecting the option brings the project back to its monorepo.

{% hint style="info" %}
You can delete a project belonging to a monorepo the same way as you delete any SonarQube Server project (**Project settings > Deletion**).
{% endhint %}

### Modifying the new code definition of a project in a monorepo <a href="#modify-project-new-code-def" id="modify-project-new-code-def"></a>

You can set up a different new code definition for each project in the monorepo provided you are an administrator of the project.

To set up a new code definition for a given project:

1. Open your project in SonarQube Server.
2. Go to **Project Settings > New Code**.

### Related pages

[setting-up-at-global-level](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/github-integration/setting-up-at-global-level "mention")\
[global-setup](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/gitlab-integration/global-setup "mention")\
[setting-up-integration-at-global-level](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/setting-up-integration-at-global-level "mention")\
[bitbucket-cloud-integration](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-cloud-integration "mention")

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/user-guide/issues/in-devops-platform/azure-devops.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/user-guide/issues/in-devops-platform/azure-devops.md

# Source: https://docs.sonarsource.com/sonarqube-server/user-guide/issues/in-devops-platform/azure-devops.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/devops-platform-integration/azure-devops.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/in-devops-platform/azure-devops.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/getting-started/azure-devops.md

# Analyzing Azure DevOps projects

If your code is on Azure DevOps, you can benefit from SonarQube Cloud’s integration with Azure DevOps.

### Key features of Azure DevOps integration <a href="#azure-devops-integration-features" id="azure-devops-integration-features"></a>

SonarQube Cloud’s integration with Azure DevOps allows you to maintain code quality and security in your Azure DevOps repositories. It is compatible with Azure DevOps Services.

With this integration, you’ll be able to:

* Sign in to SonarQube Cloud with your Azure DevOps credentials.
* Import your Azure DevOps repositories into SonarQube Cloud to easily set up SonarQube Cloud projects.
* Integrate smoothly SonarQube Cloud analysis into your Azure build pipeline with the Azure DevOps extension for SonarQube. This includes multi-branch analysis features.
* Report the analysis’ quality gate status right in Azure Pipeline’s Build Summary page.
* Prevent pull request merges when the quality gate fails.
* View issues detected on a pull request in Azure DevOps.\
  Each issue will be a comment on the Azure DevOps pull request. If you change the status of an issue in SonarQube Cloud, that status change is immediately reflected in the Azure DevOps interface.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-f35ec737721acd79df927d68c27678df0f6d3242%2F1b0a1eaa4e44b0ef6c364ebaccb8c00a393d51b6.png?alt=media" alt="SonarQube Cloud and Azure DevOps integration overview."><figcaption></figcaption></figure></div>

### Sign up to SonarQube Cloud <a href="#sign-up" id="sign-up"></a>

Go to the [SonarQube Cloud](https://www.sonarsource.com/products/sonarcloud/) product page and choose **Set up** or **Login**, then select **Azure DevOps** from the list of DevOps cloud platforms.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-d9d3b7d58e360ead189fa859e7028306dca5ce4e%2F02a3d8158543ac0ef0b6ea23ed89ad43f2d3135b.png?alt=media" alt="Login screen to sign up in SonarQube Cloud using Azure DevOps."><figcaption></figcaption></figure></div>

You will be taken to the Microsoft login page. Sign in using your Microsoft credentials.

Setting up a new SonarQube Cloud account with your Azure DevOps service requires that you be logged into both instances because there is some back-and-forth involved between the two platforms.

With an existing Azure DevOps service, you will start by opening a new SonarQube Cloud account, creating a SonarQube Cloud Organization, and connecting it to Azure with an Azure Personal Access Token. With your PAT in place, importing your repositories and configuring the analysis are the next steps to get things going.

Once you have successfully logged in, you will see the SonarQube Cloud welcome screen. See below for full, step-by-step instructions.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-a7ccad59058593c48e9da0975bb7cb989e6755dd%2Fd86291d78c09ae2237752828d238a03a262099ed.png?alt=media" alt="Azure welcome to SonarQube Cloud for the first time."><figcaption></figcaption></figure></div>

### Set up your organization <a href="#set-up-your-organization" id="set-up-your-organization"></a>

In this step, you will create a SonarQube Cloud organization by importing your Azure DevOps organization (you must be an admin of the Azure DevOps organization). For more information, see [importing-azure-devops-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-azure-devops-organization "mention").

SonarQube Cloud is set up to mirror the way that code is organized in Azure DevOps (and other repository providers):

* Each *SonarQube Cloud project* corresponds one-to-one with an *Azure DevOps project*, which resides in its own Git repository.
* *Azure DevOps projects* are grouped into *Azure DevOps organizations*.
* Each *SonarQube Cloud organization* corresponds one-to-one with an *Azure DevOps organization*.

You will be presented with a screen like this:

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-cdd8d663707aaa94dfbead5de0bef28247187b0c%2F4700bc4b2153269af664ad7903c18a1f89454d7e.png?alt=media" alt="Enter your Azure organization."><figcaption></figcaption></figure></div>

#### Check the organization name and key <a href="#check-the-organization-name-and-key" id="check-the-organization-name-and-key"></a>

SonarQube Cloud will suggest a *key* for your SonarQube Cloud organization. This is a name unique across all organizations within SonarQube Cloud. You can accept the suggestion or change it manually. The interface will prevent you from changing it to an already existing key.

#### Create and enter the Azure PAT <a href="#create-and-enter-the-azure-pat" id="create-and-enter-the-azure-pat"></a>

1. Create the Personal Access Token (PAT) on the Azure DevOps organization as described in **Step 1** of [importing-azure-devops-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-azure-devops-organization "mention").
2. Copy-paste the PAT to **Personal Access Token**.

#### Choose a plan <a href="#choose-a-plan" id="choose-a-plan"></a>

Next, you will be asked to choose a SonarQube Cloud subscription plan. See [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") for a comparison between the different plans.

If you want to analyze more than 50k lines of private code, then you need to select the Team or Enterprise plan. Monthly plans offer a 14-day free trial period. Once the 14 days have elapsed, the cost is based on the number of lines of code analyzed. For more information, see [#loc-based-pricing](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans#loc-based-pricing "mention").

Once you have chosen a plan and clicked **Create Organization,** your SonarQube Cloud organization will be created!

### Set up your analysis <a href="#set-up-your-analysis" id="set-up-your-analysis"></a>

#### Import repositories <a href="#import-repositories" id="import-repositories"></a>

The next step is to import the projects (that is, individual git repositories) that you want to analyze (from your Azure DevOps organization) into your newly created SonarQube Cloud organization. A corresponding SonarQube Cloud project will be created for each git repository.

SonarQube Cloud will present a list of the repositories in your Azure DevOps organization. Choose those that you want to import and analyze, then select **Set Up** to continue.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-f3fcd8e4b12af8d629cef691796257de96ee1c36%2Ffad2f3b917f93c585de3273b07775b74ef0a7779.png?alt=media" alt="Choose which repositories to import from Azure."><figcaption></figcaption></figure></div>

The selected projects will be imported.

### Choose your new code definition <a href="#choose-your-new-code-definition" id="choose-your-new-code-definition"></a>

The next step is to set the new code definition (NCD) for your projects. The NCD is a mandatory step and it defines which part of your code is considered new code. This helps you to focus your attention on the most recent changes to your code.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-d84ef145f4ef427038951343d8107176668d8035%2F125a360a0f7fb763d73094acf30220e68a7ec0ca.png?alt=media" alt="et up your project by selecting your New Code Definition."><figcaption></figcaption></figure></div>

{% hint style="info" %}
Note that the new code definition you apply at this stage will apply to all of the projects you have selected for analysis. You can change your new code definition later on a per-project basis.

To do this, go to *Your Organization* > *Your Project* > **Administration** > **New Code**.
{% endhint %}

For more information, see [about-new-code](https://docs.sonarsource.com/sonarqube-cloud/standards/about-new-code "mention").

#### Configure analysis <a href="#configure-analysis" id="configure-analysis"></a>

With Azure DevOps projects the actual analysis is performed in your build environment (cloud CI, local machine, etc.). This means that you must configure your build process to perform the analysis on each build and communicate the results to SonarQube Cloud.

{% hint style="info" %}
We refer to this analysis method as *CI-based analysis* (though it may take place in a cloud CI or a manually configured build environment) to contrast it with *automatic analysis* which works by SonarQube Cloud directly accessing your repository and performing the analysis itself.

However, automatic analysis is currently available only for GitHub projects and only for a subset of languages. It is currently not available for Azure DevOps projects.
{% endhint %}

SonarQube Cloud will guide you through a tutorial on how to set up your build environment to perform analysis.

The first step is to select your build environment. SonarQube Cloud will present this page:

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-4c5572dd7c331d86df4c3864ff4bc78696255d1b%2F39fdccf44089a9c24f4eb7c27a9221e17e4883dd.png?alt=media" alt="Choose your preferred CI tool as the analysis method."><figcaption></figcaption></figure></div>

If you have no particular preference and are setting up a new project on Azure DevOps, we recommend using Azure DevOps Pipelines as your CI.

SonarQube Cloud’s in-product tutorial assumes that the user has experience setting up pipelines in Azure DevOps and will walk you through most of the process. You can check Azure pipelines [introduction](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/introduction "mention") documentation if more information is needed to set up your YAML file.

### See your analysis results <a href="#see-your-analysis-results" id="see-your-analysis-results"></a>

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-d3a53f49632ed7b9011111b675ee37c80876aaaa%2Fded5daf07b7d42658dc7452779e48ff0bf5b4c6f.png?alt=media" alt="The first page of a newly imported project."><figcaption></figcaption></figure></div>

Your next steps are to check the results of your first analysis. Your next steps are to check the results of your first analysis and set your new code definition, See [about-new-code](https://docs.sonarsource.com/sonarqube-cloud/standards/about-new-code "mention") for details.

{% hint style="info" %}
If you log into SonarQube Cloud using an email address that you previously used to log into another DevOps platform, you need to be aware that SonarQube Cloud will automatically associate your email address with the new DevOps platform.

For example, if you log in through Azure DevOps and previously used GitHub, GitHub issues will no longer be assigned to your email address and you will stop receiving GitHub email notifications (via your SonarQube Cloud organization). If you then decide to switch back to GitHub, the Azure DevOps email notifications will be discontinued.
{% endhint %}

### Related pages <a href="#related-pages" id="related-pages"></a>

* [importing-azure-devops-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-azure-devops-organization "mention")
* [setting-up-project](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/setting-up-project "mention")
* [azure-devops](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/devops-platform-integration/azure-devops "mention")
* [azure-pipelines](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines "mention")

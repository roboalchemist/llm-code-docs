# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/authentication/github.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/instance-administration/authentication/github.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/instance-administration/authentication/github.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/instance-administration/authentication/github.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/instance-administration/authentication/github.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/instance-administration/authentication/github.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/instance-administration/authentication/github.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/instance-administration/authentication/github.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/instance-administration/authentication/github.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/instance-administration/authentication/github.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/authentication/github.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/authentication/github.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/authentication/github.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/authentication/github.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/authentication/github.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/user-guide/issues/in-devops-platform/github.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/github.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/authentication/github.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/authentication/github.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/user-guide/issues/in-devops-platform/github.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/github.md

# Source: https://docs.sonarsource.com/sonarqube-server/user-guide/issues/in-devops-platform/github.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/devops-platform-integration/github.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/in-devops-platform/github.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/getting-started/github.md

# Analyzing GitHub projects

If your code is on GitHub, go to the [SonarQube Cloud](https://www.sonarsource.com/products/sonarcloud/) product page and choose **Sign up** for new users, or **Login** for existing users, then select **GitHub** from the list of DevOps cloud platforms.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-d9d3b7d58e360ead189fa859e7028306dca5ce4e%2F02a3d8158543ac0ef0b6ea23ed89ad43f2d3135b.png?alt=media" alt="Sign up to SonarQube Cloud using GitHub."><figcaption></figcaption></figure></div>

Once you have successfully logged in, you will be prompted to connect your GitHub organization with SonarQube Cloud and create your SonarQube Cloud organization.

### Set up your organization <a href="#set-up-your-organization" id="set-up-your-organization"></a>

You must be an owner of the GitHub organization.

For a complete setup overview, see [setup-overview](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setup-overview "mention").

#### Connect your GitHub organization with SonarQube Cloud <a href="#connect-your-github-organization-with-sonarqube-cloud" id="connect-your-github-organization-with-sonarqube-cloud"></a>

After selecting **Analyze new project**, you will be presented with a step-by-step tutorial to install the SonarQube Cloud application on GitHub. This allows SonarQube Cloud to access your GitHub organization or personal account. You can select specific repositories to be connected to SonarQube Cloud or just select all and can always change this setting later.

#### Create your SonarQube Cloud organization <a href="#create-your-sonarqube-cloud-organization" id="create-your-sonarqube-cloud-organization"></a>

SonarQube Cloud is set up to mirror the way that code is organized in GitHub (and other repository providers):

* Each *SonarQube Cloud project* corresponds one-to-one with a *GitHub project* that resides in its own GitHub repository.
* GitHub projects are grouped into *GitHub organizations* or *personal accounts*.
* Each *SonarQube Cloud organization* corresponds one-to-one with a *GitHub organization* or *personal account*.

SonarQube Cloud will suggest an Actions secret *name* and *key* for your SonarQube Cloud organization. The key is unique across all organizations within SonarQube Cloud. You can accept the suggestion or change it manually. The interface will prevent you from changing it to an already existing key.

{% hint style="warning" %}
SonarQube Cloud does not support linking an organization to more than one DevOps platform. If you want to link to more than one, you will need to create a separate organization to link to each DevOps service.
{% endhint %}

For more information, see [importing-github-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-github-organization "mention").

#### Choose a plan <a href="#choose-a-plan" id="choose-a-plan"></a>

Next, you will be asked to choose a SonarQube Cloud subscription plan. See [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") for a comparison between the different plans.

If you want to analyze more than 50k lines of private code, then you need to select the Team or Enterprise plan. Monthly plans offer a 14-day free trial period. Once the 14 days have elapsed, the cost is based on the number of lines of code analyzed. For more information, see [#loc-based-pricing](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans#loc-based-pricing "mention").

Once you have chosen a plan and selected **Create Organization,** your SonarQube Cloud organization is created!

### Set up your analysis <a href="#set-up-your-analysis" id="set-up-your-analysis"></a>

#### Import repositories <a href="#import-repositories" id="import-repositories"></a>

The next step is to import the projects (that is, individual Git repositories) that you want to analyze from your GitHub organization into your newly created SonarQube Cloud organization. A corresponding, one-to-one SonarQube Cloud project will be created for each imported repository.

SonarQube Cloud will present a list of the repositories in your GitHub organization; choose the projects you want to import and select **Set Up** to get started.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-d25914d7114c473fb5657d98964492e207514aff%2Fdb48a1e4aa093ef61408cd5d6096781bb1def8ac.png?alt=media" alt="Select the repos you want to import from GitHub."><figcaption></figcaption></figure></div>

The selected projects will be imported.

### Choose your new code definition <a href="#choose-your-new-code-definition" id="choose-your-new-code-definition"></a>

The next step is to set the new code definition (NCD) for your project. The NCD is a mandatory step and it defines which part of your code is considered *new code*. This helps you to focus your attention on the most recent changes to your code.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-bd48e40f19a2c940068640613001a57bdf2b7b86%2F19ee5f3a0355ad363ac36546fa46e6daa2e69862.png?alt=media" alt="Set up your project and select your New Code Definition."><figcaption></figcaption></figure></div>

{% hint style="info" %}
Note that the new code definition you apply at this stage will apply to all of the projects you have selected for analysis. You can change your new code definition later on a per-project basis.

To do this, go to *Your Project* > **Administration** > **New Code.**
{% endhint %}

For more information, check out the [about-new-code](https://docs.sonarsource.com/sonarqube-cloud/standards/about-new-code "mention") page.

### Analysis methods <a href="#analysis-methods" id="analysis-methods"></a>

For GitHub repositories, there are two analysis methods available: **Automatic analysis** and **CI-based analysis**.

SonarQube Cloud will first check your imported repository to see if it qualifies for automatic analysis. If it does, the analysis will start automatically and the results will appear shortly. Otherwise, proceed with CI-based analysis.

#### Automatic analysis <a href="#automatic-analysis" id="automatic-analysis"></a>

SonarQube Cloud can automatically analyze your code simply by reading it from your GitHub repository, without the need to configure a CI-based analysis. After configuring SonarQube Cloud with your GitHub organization, you will see a screen like this:

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-906f07c6265566e70e89206f87896a228b314de3%2F4d65f01737bf18f16285e9a8cb79b2c2912bcf67.png?alt=media" alt="Configure all GitHub steps to connect your repository to SonarQube Cloud."><figcaption></figcaption></figure></div>

Note that automatic analysis is only available for GitHub repositories. It is available for most of the languages that SonarQube Cloud supports, see [languages](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages "mention"), with the following exceptions:

Partial support

* C#
* Java

Not yet supported

* Objective-C
* PL/SQL
* TSQL

See the [automatic-analysis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/automatic-analysis "mention") page for more details.

#### CI-based analysis <a href="#ci-based-analysis" id="ci-based-analysis"></a>

If automatic analysis is not recommended for your project, you will need to set up a CI-based analysis. This will be the case, for example, with projects that use PL/SQL, TSQL or Objective-C.

In a CI-based analysis scenario, scanning and analysis do not occur in SonarQube Cloud itself (as they do with automatic analysis) but rather in your build environment, as part of your build process. This means you have to configure your build process to perform the analysis on each build and communicate the results to SonarQube Cloud.

The first step is to select your build environment. SonarQube Cloud will present this page:

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-71ac3a532a36c130f9da43a99788a2690d0828fd%2Fb576064a82db311e31a01b74d90e15987d927a84.png?alt=media" alt="Choose your preferred CI tool as the SonarCloud analysis method."><figcaption></figcaption></figure></div>

Select the best CI option from the choices and SonarQube Cloud will guide you through a tutorial on how to set all this up.

If you need to move from automatic analysis to CI-based analysis (for example, some projects start with automatic analysis because of their languages, and then need to move to CI-based analysis because of their size), you can [deactivate automatic analysis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/automatic-analysis#deactivating-automatic-analysis) and set up a CI-based analysis by going to **Administration** > **Analysis Method.**

### Your analysis results <a href="#your-analysis-results" id="your-analysis-results"></a>

Once it is complete, you can view the results of your first analysis. See [github-actions-for-sonarcloud](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/github-actions-for-sonarcloud "mention") to integrate SonarQube Cloud into your GitHub pipeline.

In addition, with the Enterprise plan, SonarQube Cloud displays some analysis result data directly in GitHub when finding issues that impact the security of your software. See the [github](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/devops-platform-integration/github "mention") for more details.

{% hint style="warning" %}
If you log into SonarQube Cloud using an email address that you previously used to log into another DevOps platform, you need to be aware that SonarQube Cloud will automatically associate your email address with the new DevOps platform.

For example, if you log in through GitHub and previously used Bitbucket Cloud, Bitbucket Cloud issues will no longer be assigned to your email address and you will stop receiving Bitbucket Cloud email notifications. If you then decide to switch back to Bitbucket Cloud, the GitHub email notifications will be discontinued.
{% endhint %}

### Related pages <a href="#related-pages" id="related-pages"></a>

* [setup-overview](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setup-overview "mention")
* [importing-github-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-github-organization "mention")
* [setting-up-project](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/setting-up-project "mention")
* [github](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/devops-platform-integration/github "mention")
* [github-actions-for-sonarcloud](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/github-actions-for-sonarcloud "mention")

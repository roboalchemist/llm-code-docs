# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/authentication/bitbucket-cloud.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/instance-administration/authentication/bitbucket-cloud.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/instance-administration/authentication/bitbucket-cloud.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/instance-administration/authentication/bitbucket-cloud.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/instance-administration/authentication/bitbucket-cloud.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/instance-administration/authentication/bitbucket-cloud.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/instance-administration/authentication/bitbucket-cloud.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/instance-administration/authentication/bitbucket-cloud.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/instance-administration/authentication/bitbucket-cloud.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/instance-administration/authentication/bitbucket-cloud.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/authentication/bitbucket-cloud.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/authentication/bitbucket-cloud.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/authentication/bitbucket-cloud.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/authentication/bitbucket-cloud.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/authentication/bitbucket-cloud.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/bitbucket-cloud.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/authentication/bitbucket-cloud.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/authentication/bitbucket-cloud.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/bitbucket-cloud.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/devops-platform-integration/bitbucket-cloud.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/in-devops-platform/bitbucket-cloud.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/getting-started/bitbucket-cloud.md

# Analyzing Bitbucket Cloud projects

If your code is on Bitbucket Cloud, go to the [SonarQube Cloud](https://www.sonarsource.com/products/sonarcloud/) product page and choose **Set up** or **Login**, then select **Bitbucket** from the list of DevOps cloud platforms.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-d9d3b7d58e360ead189fa859e7028306dca5ce4e%2F02a3d8158543ac0ef0b6ea23ed89ad43f2d3135b.png?alt=media" alt="Sign up to SonarQube Cloud using Bitbucket."><figcaption></figcaption></figure></div>

You will be taken to the Bitbucket login page. Sign in using your Bitbucket credentials.

### Welcome to SonarQube Cloud <a href="#welcome-to-sonarcloud" id="welcome-to-sonarcloud"></a>

Once you have successfully logged in, you will see the SonarQube Cloud welcome screen.

Select **Import projects from Bitbucket**.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-930fc26eb05a6ce04052bf9235716c60fa58ec2e%2F0ed1da1531d77625e898bdc624bb1d2cfe839613.png?alt=media" alt="Welcome to SonarQube Cloud for the first time."><figcaption></figcaption></figure></div>

### Set up your organization <a href="#set-up-your-organization" id="set-up-your-organization"></a>

You must be an administrator of the Bitbucket workspace.

For a complete setup overview, see [setup-overview](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setup-overview "mention").

#### Connect your Bitbucket Cloud workspace to SonarQube Cloud <a href="#connect-your-bitbucket-cloud-workspace-to-sonarqubecloud" id="connect-your-bitbucket-cloud-workspace-to-sonarqubecloud"></a>

When prompted, grant access to the SonarQube Cloud application to read your Bitbucket Cloud workspace. SonarQube Cloud requests access for:

* reading your account information.
* reading your repositories and their pull requests.
* reading your team membership information.

{% hint style="info" %}
You must be an administrator of the workspace that contains the repository you want to analyze. You will already be an administrator of your default workspace. For any other workspace, you have to add your Bitbucket account to a user group with the **Administer workspace** user right enabled.
{% endhint %}

{% hint style="info" %}
To avoid exceeding [Bitbucket Cloud API rate limits](https://support.atlassian.com/bitbucket-cloud/docs/api-request-limits/), it is recommended to use a dedicated Bitbucket user for SonarQube Cloud integration.
{% endhint %}

#### Create your SonarQube Cloud organization <a href="#create-your-sonarqubecloud-organization" id="create-your-sonarqubecloud-organization"></a>

SonarQube Cloud is set up to mirror the way that code is organized in Bitbucket Cloud (and other repository providers):

* Each *SonarQube Cloud project* corresponds one-to-one with a *Bitbucket Git repository*.
* *Bitbucket projects* are grouped into *Bitbucket workspaces*.
* Each *SonarQube Cloud organization* corresponds one-to-one with a *Bitbucket workspace*.

{% hint style="info" %}
Bitbucket Git repositories are grouped into Bitbucket projects. Bitbucket projects cannot be linked to SonarQube projects; instead the link is on the Git repository level.
{% endhint %}

In this step, you will create a SonarQube Cloud organization that corresponds to your Bitbucket workspace.

SonarQube Cloud will suggest a *key* for your SonarQube Cloud organization. This is a name unique across all organizations within SonarQube Cloud. You can accept the suggestion or change it manually. The interface will prevent you from changing it to an already existing key.

{% hint style="warning" %}
SonarQube Cloud does not support linking an organization to more than one DevOps platform. If you want to link to more than one, you will need to create a separate organization to link to each DevOps service.
{% endhint %}

For more information, see [importing-bitbucket-workspace](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-bitbucket-workspace "mention").

#### Choose a plan <a href="#choose-a-plan" id="choose-a-plan"></a>

Next, you will be asked to choose a SonarQube Cloud subscription plan. See [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") for a comparison between the different plans.

If you want to analyze more than 50k lines of private code, then you need to select the Team or Enterprise plan. Monthly plans offer a 14-day free trial period. Once the 14 days have elapsed, the cost is based on the number of lines of code analyzed. For more information, see [#loc-based-pricing](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans#loc-based-pricing "mention").

Once you have chosen a plan and clicked **Create Organization**, your SonarQube Cloud organization will be created!

### Set up your analysis <a href="#set-up-your-analysis" id="set-up-your-analysis"></a>

#### Import repositories <a href="#import-repositories" id="import-repositories"></a>

The next step is to import the projects (that is, individual Git repositories) that you want to analyze from your Bitbucket workspace into your newly created SonarQube Cloud organization. A corresponding SonarQube Cloud project will be created for each.

SonarQube Cloud will present a list of the repositories in your Bitbucket workspace. The selected projects will be imported.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-ee064195c84d6d507a27a7c8338130f9df7e5dd2%2F0b25a512cc89e6f5723e3b0d2727ce4f0b377a03.png?alt=media" alt="Choose the Bitbucket repositories you want to import into SonarQube Cloud."><figcaption></figcaption></figure></div>

### Choose your new code definition <a href="#choose-your-new-code-definition" id="choose-your-new-code-definition"></a>

The next step is to set the **New Code Definition** (NCD) for your project(s). The NCD is a mandatory step and it defines which part of your code is considered *new code*. This helps you to focus your attention on the most recent changes to your code.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-d84ef145f4ef427038951343d8107176668d8035%2F125a360a0f7fb763d73094acf30220e68a7ec0ca.png?alt=media" alt="Set up your projects by selecting your New Code Definition."><figcaption></figcaption></figure></div>

{% hint style="info" %}
Note that the new code definition you apply at this stage will apply to all of the projects you have selected for analysis. You can change your new code definition later on a per-project basis.

To do this, go to *Your Project* > **Administration** > **New Code.**
{% endhint %}

For more information, check out the [about-new-code](https://docs.sonarsource.com/sonarqube-cloud/standards/about-new-code "mention") page.

#### Configure analysis <a href="#configure-analysis" id="configure-analysis"></a>

With Bitbucket Cloud projects, the actual analysis is performed in your build environment (cloud CI, local machine, etc.). This means you have to configure your build process to perform the analysis on each build and communicate the results up to SonarQube Cloud.

{% hint style="info" %}
We refer to this analysis method as *CI-based analysis* (though it may take place in a cloud CI or a manually configured build environment) to contrast it with *automatic analysis* which works by SonarQube Cloud directly accessing your repository and performing the analysis itself. However, [automatic-analysis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/automatic-analysis "mention") is currently available only for GitHub projects; it is currently not available for Bitbucket Cloud projects.
{% endhint %}

SonarQube Cloud will guide you through a tutorial on how to set up your build environment to perform analysis.

The first step is to select your build environment. SonarQube Cloud will present this page:

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-729aea3e00de18f09163ea00be8258142ccd352d%2Fae75d50c081033b17b45f8262f45598015c482e1.png?alt=media" alt="Choose your preferred CI tool as the SonarQube Cloud analysis method."><figcaption></figcaption></figure></div>

If you have no particular preference and are setting up a new project on Bitbucket Cloud, we recommend using Bitbucket Pipelines as your CI.

Follow the in-product tutorial to correctly set up your analysis.

### See your analysis results <a href="#see-your-analysis-results" id="see-your-analysis-results"></a>

Once it is complete, you can view the results of your first analysis. SonarQube Cloud also displays some result data directly in the Bitbucket cloud interface itself.

In addition, please see the page on [bitbucket-pipelines-for-sonarcloud](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/bitbucket-pipelines-for-sonarcloud "mention") to integrate SonarQube Cloud into your Bitbucket pipeline.

{% hint style="warning" %}
If you log into SonarQube Cloud using an email address that you previously used to log into another DevOps platform, you need to be aware that SonarQube Cloud will automatically associate your email address with the new DevOps platform.

For example, if you log in through Bitbucket Cloud and previously used GitHub, GitHub issues will no longer be assigned to your email address and you will stop receiving GitHub email notifications. If you then decide to switch back to GitHub, the Bitbucket Cloud email notifications will be discontinued.
{% endhint %}

### Sample projects <a href="#sample-projects" id="sample-projects"></a>

You can take a look at these various projects: [Sample projects analyzed on SonarQube Cloud](https://bitbucket.org/account/user/sonarsource/projects/SAMPLES).

### Related pages <a href="#related-pages" id="related-pages"></a>

* [importing-bitbucket-workspace](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-bitbucket-workspace "mention")
* [setting-up-project](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/setting-up-project "mention")
* [bitbucket-cloud](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/devops-platform-integration/bitbucket-cloud "mention")
* [bitbucket-pipelines-for-sonarcloud](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/bitbucket-pipelines-for-sonarcloud "mention")

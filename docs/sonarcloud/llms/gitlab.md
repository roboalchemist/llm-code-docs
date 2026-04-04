# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/authentication/gitlab.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/instance-administration/authentication/gitlab.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/instance-administration/authentication/gitlab.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/instance-administration/authentication/gitlab.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/instance-administration/authentication/gitlab.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/instance-administration/authentication/gitlab.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/instance-administration/authentication/gitlab.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/instance-administration/authentication/gitlab.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/instance-administration/authentication/gitlab.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/instance-administration/authentication/gitlab.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/authentication/gitlab.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/authentication/gitlab.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/authentication/gitlab.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/authentication/gitlab.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/authentication/gitlab.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/user-guide/issues/in-devops-platform/gitlab.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/gitlab.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/authentication/gitlab.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/authentication/gitlab.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/user-guide/issues/in-devops-platform/gitlab.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/gitlab.md

# Source: https://docs.sonarsource.com/sonarqube-server/user-guide/issues/in-devops-platform/gitlab.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/devops-platform-integration/gitlab.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/in-devops-platform/gitlab.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/getting-started/gitlab.md

# Analyzing GitLab projects

If your code is on GitLab, go to the [SonarQube Cloud](https://www.sonarsource.com/products/sonarcloud/) product page and choose **Set up** or **Login**, then select **GitLab** from the list of DevOps cloud platforms.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-d9d3b7d58e360ead189fa859e7028306dca5ce4e%2F02a3d8158543ac0ef0b6ea23ed89ad43f2d3135b.png?alt=media" alt="Sign up to SonarQube Cloud using GitLab."><figcaption></figcaption></figure></div>

You will be taken to the GitLab login page. Sign in using your GitLab credentials.

### Welcome to SonarQube Cloud <a href="#welcome-to-sonarcloud" id="welcome-to-sonarcloud"></a>

Once you have successfully logged in, you will see the SonarQube Cloud welcome screen. Select **Analyze your first projects** > **Import an organization from GitLab**.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-73bf4ab16051d1200d85ba9b4614aea9b10bf7bf%2Fa05d21b92df3a42990758612461979aa51c889f5.png?alt=media" alt="Welcome to SonarQube Cloud for the first time."><figcaption></figcaption></figure></div>

### Set up your organization <a href="#set-up-your-organization" id="set-up-your-organization"></a>

You must be an owner of the GitLab group to be imported.

For a complete setup overview, see [setup-overview](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setup-overview "mention").

#### About SonarQube Cloud organizations <a href="#about-sonarqube-cloud-organizations" id="about-sonarqube-cloud-organizations"></a>

SonarQube Cloud is set up to mirror the way that code is organized in GitLab (and other repository providers):

* Each *SonarQube Cloud project* corresponds one-to-one with a *GitLab project*, which resides in its own Git repository.
* *GitLab projects* are grouped into \*GitLab groups \*or under a [personal namespace](https://docs.gitlab.com/ee/user/namespace/).
* Each *SonarQube Cloud organization* corresponds one-to-one with a \*GitLab group \*or personal namespace.

{% hint style="info" %}
**SonarQube Cloud supports one DevOps platform at a time.**

SonarQube Cloud does not support linking an organization to more than one DevOps platform. If you want to link to more than one, you will need to create a separate organization to link to each DevOps service.
{% endhint %}

#### Connect your GitLab group with SonarQube Cloud <a href="#connect-your-gitlab-group-with-sonarqube-cloud" id="connect-your-gitlab-group-with-sonarqube-cloud"></a>

First, select either

* **Import any GitLab group**, if you want to import a GitLab group other than your personal one, or
* **Import my personal namespace**, if you want to import only the repositories that are under your personal namespace.

If you select the first option, you will need your GitLab group key and a personal access token.

If you select the second option, you will just need a personal access token.

**Group key**

For the group key, you can provide *either* the *ID* of the group or the *key* of the group. The group ID can be found under the group name on the group page. The group key is the last element in the path of the group and is found in the URL. For example, `gitlab.com/my-group`.

Note that the user that is logged into SonarQube Cloud must be an *owner* of the GitLab group.

{% hint style="info" %}
We currently only support the importing of GitLab parent groups. Subgroups are not supported.
{% endhint %}

**Personal access token**

To create the token, go to **User settings** > **Personal Access Tokens** in GitLab, or while logged in to GitLab, click the [Personal Access Token](https://gitlab.com/-/profile/personal_access_tokens) hyperlink in the SonarQube Cloud **Create an organization** tutorial.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-cdbbc9575df3cbcaf5f589d1368e3ca23462ba30%2F02a0fcbbee5af7f309cea57733c0941c303aa864.png?alt=media" alt="Generate a GitLab access token."><figcaption></figcaption></figure></div>

When creating your access token on the GitLab **User settings** > **Personal Access Tokens** page, make sure to select **api scope**. Then click **Create personal access token**.

When the personal access token is displayed at the top of the page, copy the token and paste it into the field on the SonarQube Cloud setup page.

{% hint style="warning" %}
**An api scope is required**

SonarQube Cloud requires that the access token have `api` scope. This gives SonarQube Cloud more access rights than strictly necessary, but due to the lack of more fine-grained access control in GitLab, it is the only viable option.

To mitigate this potential security concern, we strongly encourage you to add a technical user to your organization, log in to SonarQube Cloud using that technical user, and use the access token of that technical user to connect your GitLab group to SonarQube Cloud.

SonarQube Cloud will always limit its actions to those required for effective integration with GitLab and will never use the full access right provided by the `api` scope.
{% endhint %}

#### Import organization details <a href="#import-organization-details" id="import-organization-details"></a>

In this step, you will create a SonarQube Cloud organization that corresponds to your GitLab group. For more information, see [importing-gitlab-group](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-gitlab-group "mention").

SonarQube Cloud will suggest a *key* for your SonarQube Cloud organization. This is a name unique across all organizations within SonarQube Cloud. You can accept the suggestion or change it manually. The interface will prevent you from changing it to an already existing key.

#### Choose a plan <a href="#choose-a-plan" id="choose-a-plan"></a>

Next, you will be asked to choose a SonarQube Cloud subscription plan. See [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") for a comparison between the different plans.

If you want to analyze more than 50k lines of private code, then you need to select the Team or Enterprise plan. Monthly plans offer a 14-day free trial period. Once the 14 days have elapsed, the cost is based on the number of lines of code analyzed. For more information, see [#loc-based-pricing](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans#loc-based-pricing "mention").

{% hint style="info" %}
A plan is always associated one-to-one with a SonarQube Cloud organization and therefore, with a single GitLab group. If you want to onboard multiple GitLab groups, you must sign up for a separate SonarQube Cloud plan for each group.
{% endhint %}

Once you have chosen a plan and selected **Create Organization,** your SonarQube Cloud organization will be created!

### Set up your analysis <a href="#set-up-your-analysis" id="set-up-your-analysis"></a>

#### Import repositories <a href="#import-repositories" id="import-repositories"></a>

The next step is to import the projects (that is, individual Git repositories) that you want to analyze from your GitLab group into your newly created SonarQube Cloud organization, creating a corresponding SonarQube Cloud project for each.

SonarQube Cloud will present a list of the repositories in your GitLab group. Select those that you want to import and analyze and click **Set Up**.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-08049856209763306faf58067c8a6fe41e1f6e3a%2F425d2cd10be0394fad67a0456c60edd60545f040.png?alt=media" alt="Import repositories from GitLab into SonarQube Cloud."><figcaption></figcaption></figure></div>

The selected projects will be imported.

### Choose your new code definition <a href="#choose-your-new-code-definition" id="choose-your-new-code-definition"></a>

The next step is to set the **New Code Definition** (NCD) for your project(s). The NCD is a mandatory step and it defines which part of your code is considered *new code*. This helps you to focus your attention on the most recent changes to your code.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-431bd6e48ad4893c07c33575e75a096878846685%2Fc0d3bd16dc8718a19ce2395dbb361c1ef93ca79e.png?alt=media" alt="Set up your project by selecting a New Code Defintition."><figcaption></figcaption></figure></div>

{% hint style="info" %}
Note that the new code definition you apply at this stage will apply to all of the projects you have selected for analysis. You can change your new code definition later on a per-project basis.

To do this, go to *Your Project* > **Administration** > **New Code.**
{% endhint %}

For more information, see the [about-new-code](https://docs.sonarsource.com/sonarqube-cloud/standards/about-new-code "mention") page.

#### Configure analysis <a href="#configure-analysis" id="configure-analysis"></a>

With GitLab projects, the actual analysis is performed in your build environment (for example, on a cloud CI or your local machine). This means you have to configure your build process to perform the analysis on each build and communicate the results up to SonarQube Cloud.

{% hint style="info" %}
We refer to this analysis method as *CI-based analysis* (though it may take place in a cloud CI or a manually configured build environment) to contrast it with *automatic analysis* which works by SonarQube Cloud directly accessing your repository and performing the analysis itself. However, [automatic-analysis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/automatic-analysis "mention") is currently available only for GitHub projects and only for a subset of languages.
{% endhint %}

SonarQube Cloud will guide you through a tutorial on how to set up your build environment to run your analysis.

The first step is to select your build environment. SonarQube Cloud will present this page:

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-36ffacb339514f7b1410e1538224f4750853c7c7%2F148c4ada4049a0748d2f44fc698f6700cdcfa455.png?alt=media" alt="Choose Gitlab as your analysis method."><figcaption></figcaption></figure></div>

If you have no particular preference and are setting up a new project on GitLab, we recommend using GitLab CI/CD as your CI.

Follow the tutorial to set up your analysis.

### See your analysis results <a href="#see-your-analysis-results" id="see-your-analysis-results"></a>

Once it is complete, you can view the results of your first analysis.

In addition, please see the page on [gitlab-ci](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/gitlab-ci "mention") to integrate SonarQube Cloud into your GitLab pipelines.

{% hint style="warning" %}
**Email notifications**

If you log into SonarQube Cloud using an email address that you previously used to log into another DevOps platform, you need to be aware that SonarQube Cloud will automatically *associate your email address with the new DevOps platform*.

For example, if you log in through GitLab and previously used GitHub, GitHub issues will no longer be assigned to your email address and you will stop receiving GitHub email notifications. If you then decide to switch back to GitHub, the GitLab email notifications will be discontinued.
{% endhint %}

### Related pages <a href="#related-pages" id="related-pages"></a>

* [importing-gitlab-group](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-gitlab-group "mention")
* [setting-up-project](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/setting-up-project "mention")
* [gitlab](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/devops-platform-integration/gitlab "mention")
* [gitlab-ci](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/gitlab-ci "mention")

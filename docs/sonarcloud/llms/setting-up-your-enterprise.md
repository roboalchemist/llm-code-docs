# Source: https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/setting-up-your-enterprise.md

# Setting up your enterprise

With the Enterprise license, you can group together SonarQube Cloud organizations from different DevOps platforms into an enterprise and benefit from many features.

This page explains how to set up your enterprise from scratch.

{% hint style="info" %}
Currently, Sonar restricts each enterprise to a maximum of 200 organizations.
{% endhint %}

### Step 1: Prepare the enterprise onboarding <a href="#prepare-onboarding" id="prepare-onboarding"></a>

#### Prepare the organizations to be added <a href="#prepare-the-organizations-to-be-added" id="prepare-the-organizations-to-be-added"></a>

You must add at least one organization to be able to complete your enterprise setup. You can add any existing organization that is under your administration. Once an organization is added to your enterprise, it’s assigned the Enterprise plan.

{% hint style="warning" %}
If you add a Team plan organization to your enterprise, the organization’s Team plan subscription will be automatically cancelled and the organization will be moved to the Enterprise plan without a refund. Therefore, we recommend adding your organizations before their next billing date to avoid double charges.
{% endhint %}

To create a new organization to be added to your enterprise, import the DevOps platform organization and select the Free plan. For instructions to import your DevOps organization, please see:

* [importing-github-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-github-organization "mention")
* [importing-gitlab-group](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-gitlab-group "mention")
* [importing-bitbucket-workspace](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-bitbucket-workspace "mention")
* [importing-azure-devops-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-azure-devops-organization "mention")

#### Request a license <a href="#request-a-license" id="request-a-license"></a>

[Contact our team](https://www.sonarsource.com/products/sonarcloud/contact-enterprise-sales/) to request an Enterprise license. Provide the maximum number of Lines of Code (LOC) you want to have in your enterprise. For more information, see [#loc-based-pricing](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans#loc-based-pricing "mention") for more information.

### Step 2: Create the SonarQube Cloud enterprise <a href="#create-enterprise" id="create-enterprise"></a>

You must be an Admin of the organization you wish to add to the enterprise. Once you’ve created the enterprise, you become an Enterprise Admin automatically.

To create your enterprise:

1\. Log in to SonarQube Cloud with your organization’s administrator account.

2\. Select the **+** icon in the top right corner of SonarQube Cloud UI and select **Create new enterprise** in the menu. The **Create an enterprise** page opens.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-021483263ba9007800ad35e087b78475e7adf385%2Fe73b8759429c8dc9a840394e1909e3918a008991.png?alt=media" alt="Create your SonarQube Cloud Enterprise by adding your License key and existing Organizations."><figcaption></figcaption></figure></div>

3\. In **License key**, enter the key you received from Sonar.

4\. Enter the name and key of your enterprise.

5\. In **Add organization**, select the first organization to be added to your enterprise to complete the setup.

6\. Select the **Create enterprise** button. The enterprise is created.

7\. To add other organizations, select **Add organization**.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-cffb716385b26cabe869d715349e06d5fe7858a9%2F359ce2ce48e4f974db9573441fef91199ef81f96.png?alt=media" alt="It&#x27;s easy to add Organizations to your Enterprise; simply select the Add organization button."><figcaption></figcaption></figure></div>

### Step 3: Set the enterprise permissions of users <a href="#set-permissions" id="set-permissions"></a>

As an Enterprise Admin, you can grant the Administer Enterprise and Create Portfolios permissions. For more information, check out the [managing-the-enterprise-related-permissions](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/managing-the-enterprise-related-permissions "mention") page.

To set the enterprise-related permissions of users, follow the instructions to [retrieving-and-viewing-your-enterprise](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/retrieving-and-viewing-your-enterprise "mention"). Once inside of your enterprise:

1. Navigate to **Administration** > **Enterprise Permissions**.
2. If necessary, filter the list of users.
3. For each user, select or unselect the permissions in the table.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-d15474f47ca4e036d78c36391b3a5f44d15e1c38%2Ffedcc99bafd2e2c554eb681cf1621535cdf5319d.png?alt=media" alt="When administering your Enterprise, it&#x27;s possible to filter users by their assigned roles and allocate privileges accordingly."><figcaption></figcaption></figure></div>

### Step 4: Complete the enterprise onboarding <a href="#complete-onboarding" id="complete-onboarding"></a>

For each organization in your enterprise:

* If not already done, verify the group's default permissions on new projects. See the [templates](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/manage-org-projects/manage-project-permissions/templates "mention") page for more information.
* You can set project configurations at the organization level. The details are outlined in the [setting-config-at-org-level](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setting-config-at-org-level "mention") pages.

By default, all organizations share the enterprise LOC limit. You can allocate an individual LOC limit to one or several organizations within your enterprise; please check the [managing-the-lines-of-code-within-your-enterprise](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/managing-the-lines-of-code-within-your-enterprise "mention") page.

With the Enterprise license, you can now:

* Transition your enterprise to [Single Sign-On](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso).&#x20;
* Restrict access to your SonarQube Cloud by configuring an [IP allow list](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/ip-allow-lists).

### Related pages <a href="#related-pages" id="related-pages"></a>

* [viewing-billing-usage-info](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/viewing-billing-usage-info "mention")
* [setting-up-sso](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/setting-up-sso "mention")
* [onboarding-new-org](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/onboarding-new-org "mention")
* [managing-enterprise](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise "mention")
* [enterprise-security](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security "mention")

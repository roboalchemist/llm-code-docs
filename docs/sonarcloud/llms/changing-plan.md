# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/changing-plan.md

# Changing your subscription plan

This page explains how to upgrade to or downgrade from a subscription plan, and how to change the Lines of Code (LOC) limit of your organization or enterprise.

### Changing the LOC limit of your subscription <a href="#changing-loc" id="changing-loc"></a>

If you have a monthly subscription, you can change your LOC (Lines of Code) limit in the UI. Otherwise, [contact our team](https://www.sonarsource.com/company/contact/). For more information about the LOC, see [#loc-based-pricing](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/subscription-plans#loc-based-pricing "mention").

{% hint style="info" %}
You cannot change the LOC of a legacy paid plan. You can only migrate your legacy paid plan organization to Free or upgrade it to Team or Enterprise. See above.
{% endhint %}

To change the LOC limit of your monthly subscription:

<details>

<summary>Yearly or custom subscription</summary>

[Contact our team](https://www.sonarsource.com/company/contact/).

</details>

<details>

<summary>Monthly subscription</summary>

1. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more details.
2. Select the **Billing & Upgrade** tab.
3. In the **Current plan** section, select **Modify plan**.
4. In **Plan Details** > **How many lines of code?**, change the LOC.
5. Select **Update**.

</details>

Note that:

* If you increase the LOC limit, the change takes effect immediately and you will be charged on the next billing date with the pro-rated amount for the rest of the current billing period.
* If you decrease the LOC limit, the change will take effect on the next billing cycle.

### Upgrading from Free to Team <a href="#upgrading-free-to-team" id="upgrading-free-to-team"></a>

<details>

<summary>Monthly subscription</summary>

1. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more details.
2. Select the **Billing & Upgrade** tab.
3. In **Current plan**, select **Modify plan**. The **Upgrade to the Team plan** page opens.
4. In **Plan details**, select the Lines of Code (LOC threshold) you want to purchase for the organization. See **LOC-based pricing** in [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") for more information.
5. Select **Continue to billing information**.
6. Enter your billing information.
7. Select **Continue to payment information**.
8. Enter your credit card information.
9. Select **Upgrade**.

</details>

<details>

<summary>Yearly or custom subscription</summary>

1. Select the Lines of Code (LOC threshold) you want to purchase for the organization. See **LOC-based pricing** in [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") for more details.
2. [Contact our team](https://www.sonarsource.com/company/contact/) to purchase a yearly or custom coupon for the selected LOC.
3. Once you have your coupon, retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more information.
4. Select the **Billing & Upgrade** tab.
5. In **Already have a coupon?**, select the **apply it directly here** link.
6. Enter the coupon and select **Apply coupon**.

</details>

### Upgrading to the Enterprise plan <a href="#upgrading-to-enterprise" id="upgrading-to-enterprise"></a>

See [setting-up-your-enterprise](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/setting-up-your-enterprise "mention") for more information.

### Downgrading from Enterprise <a href="#downgrading-from-enterprise" id="downgrading-from-enterprise"></a>

When you downgrade an organization, the downgrade will take effect on the next billing cycle.

Before downgrading, see [#feature-loss-on-downgrade](#feature-loss-on-downgrade "mention").

When you remove an organization from your enterprise, the organization is automatically downgraded to the plan of your choice. See [#removing-org-from-enterprise](https://docs.sonarsource.com/sonarqube-cloud/managing-enterprise/adding-organizations-to-your-enterprise#removing-org-from-enterprise "mention").

### Downgrading from Team <a href="#downgrading-from-team" id="downgrading-from-team"></a>

When you downgrade an organization, the downgrade will take effect on the next billing cycle.

Before downgrading, see [#feature-loss-on-downgrade](#feature-loss-on-downgrade "mention").

To downgrade from Team:

1. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more details.
2. Select the **Billing & Upgrade** tab.
3. In the **Current plan** section, select **Modify plan**.
4. On the new page, click the **visit our compare plan page** link. A new page displays a summary of the different plans.
5. In the **Free** column, select **Downgrade to Free**.\
   SonarQube Cloud checks if your organization complies with the Free plan’s limit (maximum number of members). If not, a warning is displayed, and you are guided through the steps necessary to make your organization comply with this limit. Once this is done, you will be able to proceed to the next step.
6. Select **Next step**.
7. You can now review the plan changes: what you will gain and what you will lose. Select **Next step**.
8. If you agree to downgrade, enter your organization name and select **Downgrade organization**. Otherwise, select **Cancel download**.

### Moving from OSS to Free <a href="#moving-from-oss-to-free" id="moving-from-oss-to-free"></a>

If you want to change your OSS plan organization, you can only move it to Free. In that case, you will be able to analyze private projects but you will loose access to the advanced features listed in [#oss-plan](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/subscription-plans#oss-plan "mention").

To move your organization from OSS to Free:

1. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more details.
2. Select the **Billing & Upgrade** tab.
3. In **Current plan**, select **Modify plan**.&#x20;
4. Select the Free plan.

### Changing your legacy paid plan <a href="#changing-legagy-plan" id="changing-legagy-plan"></a>

The legacy paid plan has been replaced by the new Team plan. It will soon no longer be supported.

Before migrating, determine the number of private lines (LOC) your organization needs and check the features of each plan. For more information, see [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention").

To migrate your organization to another plan:

1. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more details.
2. Select the **Billing & Upgrade** tab.
3. In **Current plan**, select **Modify plan** and follow the instructions to select your new plan.

If your organization doesn’t comply with the new plan’s limits (maximum number of members and maximum LOC), a warning is displayed, and you are guided through the steps necessary to make your organization comply with these limits.

### Terminating a monthly subscription <a href="#terminating" id="terminating"></a>

A monthly subscription is automatically renewed. To terminate it, you can delete it (see [deleting-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/deleting-organization "mention")) or downgrade it to Free (see [#downgrading-from-team](#downgrading-from-team "mention")).

### Reviewing the feature loss before a downgrade <a href="#feature-loss-on-downgrade" id="feature-loss-on-downgrade"></a>

When you downgrade:

* The maximum number of LOC you can analyze in your private projects will decrease if you downgrade from Team to Free. If your currently LOC used is over the maximum LOC of the target plan, you won’t be able to analyze all your current private projects anymore. This means also automatic project provisioning through your CI/CD pipeline will create public projects.
* You may lose access to features: see the table below. In particular, be aware of the downgrade impacts explained in the **If you lose it during the downgrade** column.

<table><thead><tr><th width="122.3004150390625">Feature</th><th width="108.4871826171875">Available from</th><th>If you lose it during a downgrade</th></tr></thead><tbody><tr><td>AI CodeFix</td><td>Team</td><td>As a developer, you can’t use the AI CodeFix feature to resolve your code issues anymore. See <a data-mention href="../../ai-capabilities/ai-codefix">ai-codefix</a> overview page for details about the feature.</td></tr><tr><td>Custom quality profiles</td><td>Team</td><td>You can’t manage custom quality profiles anymore. Only the built-in quality profile (Sonar way) can be used. Your existing custom quality profiles are not deleted, but they are removed from your project settings, and you can’t use them anymore. If you upgrade your plan, you regain access to them. See <a data-mention href="../../standards/managing-quality-profiles/understanding-quality-profiles">understanding-quality-profiles</a> for more details.</td></tr><tr><td>Custom quality gates</td><td>Team</td><td>You can’t manage custom quality gates anymore. Only the built-in quality gate (Sonar way) can be used. Your existing custom quality gates are not deleted, but they are removed from your project settings, and you can’t use them anymore. If you upgrade your plan, you regain access to them. See <a data-mention href="../../standards/managing-quality-gates/introduction-to-quality-gates">introduction-to-quality-gates</a> for more details.</td></tr><tr><td>Enterprise languages</td><td>Enterprise</td><td>The following languages can no longer be analyzed: APEX, ABAP, COBOL, JCL, PL/I, and RPG.</td></tr><tr><td>Feedback on all branches</td><td>Team</td><td><p>The <a data-mention href="../../enriching/branch-analysis">branch-analysis</a> is now limited to the main branch, and the pull request analysis is now limited to pull requests where the target branch is the main branch.</p><p>Note that it’s still possible to analyze any branch and any pull request. SonarQube Cloud stores the analysis results in its database but you can’t access them. If you upgrade your plan, you (re)gain access to all your previous analyses.</p></td></tr><tr><td>GitHub advanced security integration</td><td>Enterprise</td><td>The report of the security issues inside the <a data-mention href="../../managing-your-projects/administering-your-projects/devops-platform-integration/github">github</a> interface as code scanning alerts is not supported anymore.</td></tr><tr><td>GitHub member sync</td><td>Team</td><td>You cannot access the GitHub member synchronization feature anymore. See <a data-mention href="../about-sonarqube-cloud-solution/user-management/devops-platform-authentication">devops-platform-authentication</a> for more details.</td></tr><tr><td>Groups (member management)</td><td>Team</td><td><p>You can’t manage custom groups anymore. This means that only the built-in groups are used (Owners and Members). The permissions of the built-in groups are set back to their default values and you cannot change them. See <a data-mention href="../../about-sonarqube-cloud-solution/user-management/user-group-concept#built-in-groups">#built-in-groups</a> for more details.<br></p><p><strong>Warning</strong>: Your existing custom groups are deleted. The Owners group is recreated by adding all users with administration permissions who belonged to the Owners group or a deleted custom group.</p></td></tr><tr><td>Management reporting</td><td>Enterprise</td><td>You have no access to the Enterprise reporting features anymore (portfolios, security and project reports). See <a data-mention href="../../getting-started-with-enterprise/viewing-enterprise-reports/introduction">introduction</a> to Viewing the enterprise reports for details.</td></tr><tr><td>Permission templates</td><td>Team</td><td><p>You can’t manage permission templates anymore.</p><p><strong>Warning</strong>: Your existing permission templates are deleted.</p></td></tr><tr><td>Projects Management</td><td>Enterprise</td><td><p>As an organization admin, you lose access to:</p><p>• The Projects Management page, which allows you to manage projects in a centralized manner.</p><p>• Organization-wide project configuration of: long-lived branch patterns, analysis scope adjustment, and automatic analysis disabling.</p></td></tr><tr><td>Scoped Organization Tokens (SOT)</td><td>Team</td><td>All SOTs are systematically deleted. See <a data-mention href="../managing-organization/scoped-organization-tokens">scoped-organization-tokens</a>for more details.</td></tr><tr><td>Single Sign-On (SSO)</td><td>Enterprise</td><td>You’ll have to delete all SSO accounts before the downgrade. See <a data-mention href="../managing-enterprise/enterprise-security/sso/about">about</a> for more details.</td></tr><tr><td>Quality profile admin delegation</td><td>Enterprise</td><td>As a user with the Quality Profiles Administration permission, you can no longer authorize users or groups to manage a specific custom quality profile. See <a data-mention href="../../standards/managing-quality-profiles/authorizing-other-users-to-manage-quality-profile">authorizing-other-users-to-manage-quality-profile</a> for more details.</td></tr><tr><td>Unlimited team members</td><td>Team</td><td>The number of members in your organization is now limited to 5.</td></tr><tr><td>Webhooks</td><td>Team</td><td>You can’t manage <a data-mention href="../../advanced-setup/webhooks">webhooks</a> anymore.<br>Your existing webhooks are not deleted but SonarQube Cloud will not invoke them anymore (you can still delete them). If you upgrade your organization, you regain access to them.</td></tr></tbody></table>

### Related pages <a href="#related-pages" id="related-pages"></a>

* [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention")
* [billing-model](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/billing-model "mention")
* [signing-up-for-plan](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/signing-up-for-plan "mention")
* [updating-billing-payment-details](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/updating-billing-payment-details "mention")
* [viewing-billing-and-usage](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/viewing-billing-and-usage "mention")
* [viewing-taxes-and-invoices](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/viewing-taxes-and-invoices "mention")

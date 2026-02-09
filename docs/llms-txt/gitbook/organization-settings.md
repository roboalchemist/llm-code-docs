# Source: https://gitbook.com/docs/documentation/ja-gitbook-documentation/akaunto/organization-settings.md

# Source: https://gitbook.com/docs/documentation/zh/zhang-hu-guan-li/organization-settings.md

# Source: https://gitbook.com/docs/documentation/fr/gestion-du-compte/organization-settings.md

# Source: https://gitbook.com/docs/account-management/organization-settings.md

# Organization settings

{% hint style="info" %}
Only Admins in an organization can access organization settings.
{% endhint %}

View and manage the settings for your GitBook organization. These include member management, sign-in methods, merge rules, billing and plans.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FuslrejntFsDDPniNzkHX%2F22_01_06_organization_settings%402x.png?alt=media&#x26;token=091849b3-8e2b-4aee-a146-7409e6a17495" alt="A GitBook screenshot showing the organization settings page"><figcaption><p>Your organization settings page.</p></figcaption></figure>

### How to access the settings for an organization

Click on your organization’s name in the top-left corner of the app, then click on **Settings**. This will take you to the general tab of that organization’s settings page, and you’ll see additional tabs containing further settings on the left-hand side.

<details>

<summary>General</summary>

**Organization profile**

You can update the logo and the name of the organization.

**GitBook AI features**

[GitBook’s AI](https://gitbook.com/docs/creating-content/searching-your-content/gitbook-ai)-powered search lets your team members ask questions about your content in natural language. You can also enable GitBook AI for published content in the space [customization ](https://gitbook.com/docs/publishing-documentation/customization)panel.

**Publishing**

Each published GitBook space that lives within your organization’s library will have a domain in two parts:

1. `[something].gitbook.com` (this is the GitBook subdomain) **or** your own custom subdomain
2. `/[spaceURL]` (this is set within the settings for the space itself)

You can update the GitBook subdomain here, as well as the default content, which is the space that visitors will see if they navigate to your GitBook subdomain directly.

Note: GitBook subdomains are a legacy feature, and you may not have access to change your subdomain at the time of reading this doc. Please refer to [custom domain setup](https://gitbook.com/docs/publishing-documentation/custom-domain) and [site sections](https://gitbook.com/docs/publishing-documentation/site-structure/site-sections) to learn more about structuring your docs with custom URLs.

**Actions**

From this section you can delete the organization. **Note: there is no turning back if you delete an organization!** All associated data will be deleted as well. If you want to keep any spaces or collections owned by the organization, make sure to first [move](https://gitbook.com/docs/creating-content/content-structure/space#move-a-space) them to another library.

</details>

<details>

<summary>Members</summary>

**Members tab**

[Members](https://gitbook.com/docs/account-management/member-management) can be added to and removed from the organization as needed. You can also update the [role](https://gitbook.com/docs/account-management/member-management/roles) for each member.

**Teams tab**

[Teams](https://gitbook.com/docs/account-management/member-management/teams) are a way to group members within an organization. You can then grant access to certain things to anyone who is a member of a given team.

</details>

<details>

<summary>SSO</summary>

**Email domains**

For any domains that you specify, anyone with an email address on those domains will immediately be able to access the organization upon signing up for a GitBook account. You can decide what [role](https://gitbook.com/docs/account-management/member-management/roles) these members should have by default.

**SAML**

For organizations on our Enterprise plan, you can configure your SSO with any SAML solution, to give your members access to GitBook through an identity provider (IdP) of your choice. [Contact sales](mailto:sales@gitbook.com) if you’re interested in upgrading to Enterprise!

</details>

<details>

<summary>Integrations</summary>

You can check which integrations are installed for your organization and [install new integrations](https://gitbook.com/docs/integrations/install-an-integration) from this page.

</details>

<details>

<summary>Billing</summary>

From this page you can view your current plan and switch from one plan to another. The toggle at the top of the page enables you to switch between viewing our annual prices (2 months free) or monthly, and you can then use the upgrade/downgrade button under the name of each plan to select your new plan.

Please see our [billing policy](https://gitbook.com/docs/account-management/plans/billing-policy) for information about how charges are calculated when you make a change during the middle of a billing period.

The Manage Billing button takes you to our payment provider, Stripe. Here you can securely manage your payment method and billing information. You can also [cancel your plan](https://gitbook.com/docs/account-management/cancelling-a-plan). If a plan has been cancelled but you change your mind before the end of the billing period, you can renew the plan to have it continue without any lapse in service.

</details>

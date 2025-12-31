# Source: https://jam.dev/docs/administration/sso.md

# SSO

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FAQ01ub0ovCISyFzEW9mY%2FSetting_%20SSO.png?alt=media&#x26;token=2b005be2-d949-439b-aa0c-75e7c4de63cf" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Available to workspaces on our [Enterprise](https://jam.dev/pricing) plans.
{% endhint %}

### Overview

Connect your identity provider to Jam for streamlined authentication and automated team management. Your team gets secure, centralized access control while you eliminate manual user provisioning overhead.

### How It Works

**SSO (Single Sign-On):** Connects your identity provider to Jam for authentication. Team members log in using their corporate credentials instead of separate Jam passwords.

**Directory Sync:** Automatically syncs user changes from your identity provider to Jam. When you add, remove, or modify users in your IdP, those changes reflect in your Jam workspace automatically.<br>

### Configure

{% tabs %}
{% tab title="SSO Setup" %}
**Configure Single Sign-On**

1. Go to Team Settings → General → Access
2. Click Setup next to Identity Provider
3. Follow the step-by-step walkthrough for your IdP
4. Complete the configuration in your identity provider

You should now see your IdP listed in the Access section. Team members can log in using SSO.

{% hint style="warning" %}
SSO is configured for a single domain by default. Need multiple domains? [Contact](https://jam.dev/help) our team to enable additional domains.
{% endhint %}
{% endtab %}

{% tab title="Directory Sync Setup" %}
**Configure Directory Sync**

1. Go to Team Settings → General → Access
2. Click Setup next to Active Directory
3. Follow the step-by-step walkthrough for your IdP
4. Select which user groups to sync (optional)

You should now see your IdP listed in the Access section. New users added to your IdP will automatically join your Jam team.

{% hint style="info" %}
Provisioned users get the Creator role by default. You'll need to adjust roles manually in Jam settings.
{% endhint %}
{% endtab %}
{% endtabs %}

#### User Management

How you manage team members depends on your Directory Sync configuration:

{% tabs %}
{% tab title="With Directory Sync" %}

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FrnmRRd1YEDhVzKTceY3N%2FSetting_%20Directoy%20Sync%20On.png?alt=media&#x26;token=fd7956ad-4d01-4c8c-8a5b-4c5a13cf1800" alt=""><figcaption></figcaption></figure>

**Automated Management**

* User provisioning: Happens in your identity provider
* New user notifications: Users get email notifications when provisioned
* Role management: Handle manually in Jam team settings
* User removal: Remove from IdP to revoke Jam access automatically
* Group sync: Manage access via user groups in your IdP

Access the directory sync management page through Team Settings → Team → Manage Members.

{% hint style="warning" %}
User groups cannot be mapped to specific Jam roles automatically. Role assignment requires manual configuration.
{% endhint %}
{% endtab %}

{% tab title="Without Directory Sync" %}

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FsFSgTIQtIiAFS7pnsSJx%2FSetting_%20Directoy%20Sync%20Off.png?alt=media&#x26;token=90b3452d-1256-47ec-b6e9-a98591c51287" alt=""><figcaption></figcaption></figure>

**Manual Management**

* User provisioning: Add users directly in Jam team settings
* Role management: Assign and modify roles in Jam
* User removal: Remove users manually from team settings

All user management happens within your Jam workspace settings.
{% endtab %}
{% endtabs %}

### FAQs

<details>

<summary>Can I use SSO without Directory Sync?</summary>

Yes. SSO handles authentication while Directory Sync manages user provisioning. You can enable either feature independently.

</details>

<details>

<summary>What identity providers are supported?</summary>

Jam supports all major identity providers including Okta, Azure AD, Google Workspace, and SAML-compatible providers.

</details>

<details>

<summary>Can I map user groups to specific Jam roles?</summary>

Not automatically. While you can sync user groups from your IdP, role assignment in Jam requires manual configuration.

</details>

<details>

<summary>What happens when I remove a user from my identity provider?</summary>

With Directory Sync enabled, users automatically lose access to their Jam account when removed from your IdP.

</details>

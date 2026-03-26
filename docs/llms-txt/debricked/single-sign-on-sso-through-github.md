# Source: https://docs.debricked.com/tools-and-integrations/single-sign-on-sso/single-sign-on-sso-through-github.md

# Single Sign-On (SSO) through  Github (OIDC)

As the company administrator, you can choose to enable single sign-on for the users to log in via GitHub.

### Enable Single Sign on via GitHub <a href="#howtoenablesinglesignonviagithub" id="howtoenablesinglesignonviagithub"></a>

1. Go to **Admin tools** on the left side menu.
2. Type your password to enter the administrative mode.
3. In the **User permissions** tab, toggle the **SSO with GitHub** to enable the feature.
4. Click **+Add organizations** to add your organization. Everyone who is part of the organization will be able to create their account or log in via the GitHub SSO.

### **Whitelist email domains** <a href="#howtowhitelistemaildomains" id="howtowhitelistemaildomains"></a>

As the company administrator, you are able to filter which users in your organization can use SSO by whitelisting email domains.

To whitelist a new email domain:

1. Go to **Admin tools** on the left side menu.
2. Type your password to enter the administrative mode.
3. In the **User permissions** tab, under **Whitelist** user domains, enter all domains (starting with “@”, for example, “@debricked.com”) and click **Save**. From now on, only users with those email domains will have access to SSO.

### **User management using SSO** <a href="#usermanagementusingsso" id="usermanagementusingsso"></a>

Keep in mind that all the users who are part of the organization on GitHub are able to join your company account on OpenText Core SCA. If a user has a different email address on GitHub than the OpenText Core SCA account, a new account will be created when the user logs in to OpenText Core SCA for the first time. If the user wants to use SSO, the company admin may remove their other account.

### **Access control** <a href="#accesscontrol" id="accesscontrol"></a>

It is currently not possible to prevent a user from logging in using a specific method if they signed up through an invite email and the SSO is enabled.&#x20;

However, since accounts with email login can only be created via invites from an admin, if the admin does not invite users and instead enables SSO, then only SSO may be used.

# Source: https://developer.1password.com/docs/service-accounts/manage-service-accounts

On this page

# Manage service accounts

## Manage active service accounts[â€‹](#manage-active-service-accounts "Direct link to Manage active service accounts") 

Owners and administrators can manage all service accounts created by their team. Other team members with the [permission to create service accounts](#manage-who-can-create-service-accounts) can manage their own service accounts, but not service accounts created by other people.

You can view and manage a service account from its overview page on 1Password.com. The service account overview page shows information about the service account, such as the vaults it can access, vault permissions, and recent activity.

To manage a service account, go to the service account overview:

1.  [Sign in](https://start.1password.com/signin) to your account on 1Password.com.
2.  Select [**Developer**](https://start.1password.com/developer-tools) in the sidebar.
3.  Select **Service accounts** at the top of the page, then choose the service account you want to manage.

### Create a usage report for a service account[â€‹](#create-a-usage-report-for-a-service-account "Direct link to Create a usage report for a service account") 

To create a [usage report](https://support.1password.com/reports#create-a-usage-report-for-a-team-member-service-account-or-vault) for a service account:

1.  [Sign in](https://start.1password.com/signin) to your account on 1Password.com.
2.  Select [**Developer**](https://start.1password.com/developer-tools) in the sidebar.
3.  Select **Service accounts** at the top of the page, then choose a service account.
4.  On the service account overview page, select **View Item Usage Report**.

Usage reports for service accounts include information on the number of vaults and items a service account can access, an overview of vaults where a service account has accessed items, when those items were last accessed, and the action performed.

### Change a service account\'s name[â€‹](#change-name "Direct link to Change a service account's name") 

To change a service account\'s name:

1.  [Sign in](https://start.1password.com/signin) to your account on 1Password.com.
2.  Select [**Developer**](https://start.1password.com/developer-tools) in the sidebar.
3.  Select **Service accounts** at the top of the page, then choose a service account.
4.  Select **Edit Details**.
5.  Type a new name, then select **Save**.

### Rotate a service account token[â€‹](#rotate-token "Direct link to Rotate a service account token") 

Rotating a service account token generates a new token with the same permissions. You can also specify an expiration for the current token, so you have time to update to the new token without any interruption in service.

Take note of any places where you may need to update a service account token before you rotate it. This helps you set a more reasonable expiration time.

To rotate a service account token:

1.  [Sign in](https://start.1password.com/sign-in/) to your account on 1Password.com.
2.  Select [**Developer**](https://start.1password.com/developer-tools) in the sidebar.
3.  Select **Service accounts** at the top of the page, then choose a service account.
4.  Under the Token section, select **Rotate Token**.
5.  Select a value for **Expire existing token** to set when the token will expire.\
    [For example, you can set the existing token to expire **now** (immediately), in **1 hour**, or in **3 days**.]
6.  Enter the service account name to confirm.
7.  Select **Rotate Token**.
8.  Select **Save in 1Password** to save the new token value in 1Password.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)]caution

If your [sign-in address](https://support.1password.com/1password-glossary#sign-in-address) changes, make sure to rotate your service account tokens. Your tokens will redirect to the new sign-in address for 30 days.

### Revoke a service account token[â€‹](#revoke-token "Direct link to Revoke a service account token") 

Revoking a service account token immediately removes its access to 1Password vaults. You might want to revoke a token if it becomes compromised or unnecessary.

To revoke a service account token:

1.  [Sign in](https://start.1password.com/signin) to your account on 1Password.com.
2.  Select [**Developer**](https://start.1password.com/developer-tools) in the sidebar.
3.  Select **Service accounts** at the top of the page, then choose a service account.
4.  Under the Token section, select **Revoke Token**.
5.  Enter the service account name to confirm, then select **Revoke Token**.

## Manage service account settings[â€‹](#manage-service-account-settings "Direct link to Manage service account settings") 

With 1Password Teams and 1Password Business, you can manage who on your team can create service accounts and which vaults the service accounts can access.

### Manage who can create service accounts[â€‹](#manage-who-can-create-service-accounts "Direct link to Manage who can create service accounts") 

By default, only [owners and administrators](https://support.1password.com/groups/) can create and manage service accounts in 1Password Teams and 1Password Business.

To allow other groups to create service accounts, an owner or administrator can:

1.  [Sign in](https://start.1password.com/signin) to your account on 1Password.com.
2.  Select [**Developer**](https://start.1password.com/developer-tools) in the sidebar.
3.  Select **Permissions** at the top of the Developer page, then select **Service Account**.
4.  Select **Manage groups**, choose the groups you want to allow to create service accounts, then select **Update Groups**.

Team members in the selected groups will be able to create service accounts.

To manage which individual team members can create service accounts, change from the Groups tab to the People tab. Select **Manage People**, choose the team members you want to allow to create service accounts, then select **Update People**.

Each team member with permission to create service accounts will only be able to manage their own service accounts, not service accounts created by other people.

### Manage which vaults team members can grant access to[â€‹](#manage-which-vaults-team-members-can-grant-access-to "Direct link to Manage which vaults team members can grant access to") 

Team members can only grant service accounts access to a vault if they have the appropriate permissions in the vault:

  Account type         Permission
  -------------------- ------------------
  1Password Teams      `Allow Managing`
  1Password Business   `Manage Vault`

You can manage team members\' permissions in vaults [with 1Password CLI](/docs/cli/grant-revoke-vault-permissions) or [on 1Password.com](https://support.1password.com/create-share-vaults-teams#manage-permissions).

### Manage service account access to vaults[â€‹](#manage-service-account-access-to-vaults "Direct link to Manage service account access to vaults") 

Team administrators can control service account access to 1Password vaults by turning access to a vault off or on.

A vault\'s service account access setting applies to all service accounts. If you turn off service account access in a vault, existing service accounts will lose access to that vault and new service accounts can\'t be granted access. After you create a service account, you can\'t add additional vaults or edit any vault permissions it has.

To turn service account access on or off for a vault:

1.  [Sign in](https://start.1password.com/signin) to your account on 1Password.com.
2.  Choose the vault you want to change service account access to.
3.  Select **Manage**.
4.  Under Service Account Access, select the toggle to turn access on or off.

## Get help[â€‹](#get-help "Direct link to Get help") 

### If you need to change a service account\'s permissions or vault access[â€‹](#if-you-need-to-change-a-service-accounts-permissions-or-vault-access "Direct link to If you need to change a service account's permissions or vault access") 

After you create a service account, you can\'t give it access to additional vaults, change its permissions in the vaults it can access, or change its ability to create new vaults. If you want to edit a service account\'s vault access or permissions, you\'ll need to create a new service account. You can [create a service account](/docs/service-accounts/get-started#create-a-service-account) on 1Password.com or with 1Password CLI.
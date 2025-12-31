# Source: https://gitbook.com/docs/help-center/integrations/integrations-troubleshooting/git-sync/why-am-i-getting-a-git-authentication-failed-message.md

# Why am I getting a Git authentication failed message?

This message will appear if you are attempting to push to a public GitHub repository that hasn't granted GitBook access.

In those cases, it is possible to sync from GitHub to GitBook but not the other way. You may also see an issue where your repositories are not listed correctly.

### Resolve the authentication issue and enable GitBook to GitHub sync

To enable GitBook to GitHub sync, you will have to grant access to the repository in your integration settings in GitHub by following these steps:

1. Click the dropdown menu next to your Avatar in the GitHub Dashboard
2. Select **Manage Organization** from the dropdown menu.
3. In the left-hand sidebar, scroll to the i**ntegrations** section and click the **applications** button.
4. Locate the GitBook option in the list of applications and click the **configure** button.
5. In the **repository access** section, you can select which repositories you want the GitBook integration to have access to.
6. Once you have chosen the desired repositories, click the **save** button to apply your changes.

### GitLab repositories

Make sure that your access token has been configured with the following access:

* `api`
* `read_repository`
* `write_repository`

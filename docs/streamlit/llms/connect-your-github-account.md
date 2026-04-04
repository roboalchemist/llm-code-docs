# Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/connect-your-github-account

# Connect your GitHub account

Connecting GitHub to your Streamlit Community Cloud account allows you to deploy apps directly from the files you store in your repositories. It also lets the system check for updates to those files and automatically update your apps. When you first connect your GitHub account to your Community Cloud account, you'll be able to deploy apps from your public repositories to Community Cloud. If you want to deploy from private repositories, you can give Community Cloud additional permissions to do so. For more information about these permissions, see [GitHub OAuth scope](https://docs.streamlit.io/deploy/streamlit-community-cloud/status#github-oauth-scope).

## Prerequisites

- You must have a Community Cloud account. See [Create your account](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/create-your-account).
- You must have a GitHub account.

## Add access to public repositories

1. In the upper-left corner, click "Workspaces **warning**".
2. From the drop down, click "Connect GitHub account".
3. Enter your GitHub credentials and follow GitHub's authentication prompts.
4. Click "Authorize streamlit".

This adds the "Streamlit" OAuth application to your GitHub account. This allows Community Cloud to work with your public repositories and create codespaces for you. In the next section, you can allow Community Cloud to access your private repositories, too. For more information about using and reviewing the OAuth applications on your account, see [Using OAuth apps](https://docs.github.com/en/apps/oauth-apps/using-oauth-apps/authorizing-oauth-apps#oauth-apps-and-organizations).

## Organization access

To deploy apps from repositories owned by a GitHub organization, Community Cloud must have permission to access the organization's repositories. If you are a member of a GitHub organization when you connect your GitHub account, your OAuth prompts will include a section labeled "Organization access".

If you have already connected your GitHub account and need to add access to an organization, follow the steps in [Manage your GitHub connection](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-account/manage-your-github-connection) to disconnect your GitHub account and start over. Alternatively, if you are not the owner of an organization, you can ask the owner to create a Community Cloud account for themselves and add permission directly.

### Organizations you own

For any organization you own, if authorization has not been previously granted or denied, you can click "Grant" before you click "Authorize streamlit".

### Organizations owned by others

For an organization you don't own, if authorization has not been previously granted or denied, you can click "Request" before you click "Authorize streamlit".

If someone has already started the process of authorizing Streamlit for your organization, the OAuth prompt will show the current status.

#### Approved access

If an organization has already granted Streamlit access, the OAuth prompt shows a green check (check).

#### Pending access

If a request has been previously sent but not yet approved, the OAuth prompt shows "Access request pending". Follow up with the organization's owner to accept the request in GitHub.

#### Denied access

If a request has been previously sent and denied, the OAuth prompt shows a red X (close). In this case, the organization owner will need to authorize Streamlit from GitHub. See GitHub's documentation on [OAuth apps and organizations](https://docs.github.com/en/apps/oauth-apps/using-oauth-apps/authorizing-oauth-apps#oauth-apps-and-organizations).

## What's next?

Now that you have your account you can [Explore your workspace](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/explore-your-workspace). Or if you're ready to go, jump right in and [Deploy your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app).
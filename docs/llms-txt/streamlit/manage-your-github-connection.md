# Manage your GitHub connection

If you have created an account but not yet connected GitHub, see [Connect your GitHub account](/deploy/streamlit-community-cloud/get-started/connect-your-github-account).

If you have already connected your GitHub account but still need to allow Streamlit Community Cloud to access private repositories, see [Optional: Add access to private repositories](/deploy/streamlit-community-cloud/get-started/connect-your-github-account#optional-add-access-to-private-repositories).

## Add access to an organization

If you are in an organization, you can grant or request access to that organization when you connect your GitHub account. For more information, see [Organization access](/deploy/streamlit-community-cloud/get-started/connect-your-github-account#organization-access).

If your GitHub account is already connected, you can remove permissions in your GitHub settings and force Streamlit to reprompt for GitHub authorization the next time you sign in to Community Cloud.

### Revoke and reauthorize

1. From your workspace, click on your workspace name in the upper-right corner. To sign out of Community Cloud, click "Sign out".
2. Go to your GitHub application settings at [github.com/settings/applications](https://github.com/settings/applications).
3. Find the "Streamlit" application, and click on the three dots (more_horiz) to open the overflow menu.
4. Click "Revoke".
5. Click "I understand, revoke access".
6. Return to [share.streamlit.io](https://share.streamlit.io/) and sign in. You will be prompted to authorize GitHub as explained in [Connect GitHub](/deploy/streamlit-community-cloud/get-started/connect-your-github-account#organization-access).

### Granting previously denied access

If an organization owner has restricted Streamlit's access or restricted all OAuth applications, they may need to directly modify their permissions in GitHub. If an organization has restricted Streamlit's access, a red X (close) will appear next to the organization when you are prompted to authorize with your GitHub account.

See GitHub's documentation on [OAuth apps and organizations](https://docs.github.com/en/apps/oauth-apps/using-oauth-apps/authorizing-oauth-apps#oauth-apps-and-organizations).

## Rename your GitHub account or repositories

Community Cloud identifies apps by their GitHub coordinates (owner, repository, branch, entrypoint file path). If you rename your account or repository from which you've deployed an app, you will lose access to administer the app. To learn more, see [Rename your app in GitHub](/deploy/streamlit-community-cloud/manage-your-app/rename-your-app).
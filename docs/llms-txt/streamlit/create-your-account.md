# Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/create-your-account

# Create your account - Streamlit Docs

Create your account
==================

Before you can start deploying apps for the world to see, you need to sign up for your Streamlit Community Cloud account.

Each Community Cloud account is associated with an email. Two accounts can't have the same email. When sharing a private app, you will assign viewing privileges by email. Additionally, two accounts can't have the same source control (GitHub account). If you try to create a second Community Cloud account with the same source control, Community Cloud will merge the accounts.

### Sign up

Community Cloud allows you to sign in using one of the three following methods:

1.  Emailed, one-use codes
2.  Google
3.  GitHub

#### Important

Even when you sign in through GitHub, the authentication flow returns your email address to Community Cloud. Changing the email on your GitHub account can affect your Community Cloud account if you sign in through GitHub.

1.  Click "Continue with Google".
2.  Enter your Google credentials, and follow GitHub's authentication prompts.

This adds the "Streamlit Community Cloud" OAuth application to your GitHub account. This application is only used to pass your email when you sign in to Community Cloud. On the next page, you'll perform additional steps to allow Community Cloud to access your repositories. For more information about using and reviewing the OAuth applications on your account, see [Using OAuth apps](https://docs.github.com/en/apps/oauth-apps/using-oauth-apps) in GitHub's docs.

#### Finish up

Congratulations on creating your Streamlit Community Cloud account! A warning icon (warning) next to "Workspaces" in the upper-left corner is expected; this indicates that your account is not yet connected to GitHub. Even if you created your account by signing in through GitHub, your account does not yet have permission to access your repositories. Continue to the next page to connect your GitHub account.
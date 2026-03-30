# Source: https://help.aikido.dev/code-scanning/connect-your-source-code/connect-gitlab-account-to-aikido/code-scanning-with-a-personal-access-token.md

# Code Scanning With a Personal Access Token

### ⚠️ Disclaimer

For **Gitlab Premium & Gitlab Ultimate** users we recommend using [Gitlab Service Accounts](https://help.aikido.dev/pr-and-release-gating/gitlab-mr-gating/gitlab-server-ci-mr-gating-via-aikido-dashboard-with-a-service-account-token). In case you would use this approach, make sure to setup an integration user that is called AikidoSec.

### Introduction

You can use personal access tokens which Aikido uses to perform the code scanning. You can update this token on [this page](https://app.aikido.dev/onboarding/gitlab/update-workspace-access-token).

### Creating a Personal Access Token <a href="#creating-a-personal-access-token" id="creating-a-personal-access-token"></a>

Gitlab cloud supports several different personal access tokens, which all work the same way. We usually recommend to create a group PAT, but for Gitlab cloud this is only possible for premium customers.

1. Navigate to the "Personal Access Token" settings page
   1. For a group access token: Go to you group page > Settings > Access Tokens
   2. For a personal access token: Go to your profile page > User settings > Access Tokens

      ![Group Access Tokens page with no active tokens and an option to add new token.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-4c2148c4eecfd757dcd7b52f5f1d69ccfc08a14b%2Fgitlab-server-ci-mr-gating-via-aikido-dashboard-with-a-personal-access-token-pat_9e58d61d-ee8e-4c49-8f0d-e3e081aff7d0.png?alt=media)
2. Click on "**Add new token**"
3. Enter a name for the token, remove the expiration date and select the **read\_api, read\_user and read\_repository** scope<br>

   <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FdjJx3d6Rn5VxNydgX3jf%2FScherm%C2%ADafbeelding%202025-12-11%20om%2012.11.34.png?alt=media&#x26;token=a73926ff-63d5-4390-a79d-882659b5ac34" alt=""><figcaption></figcaption></figure>
4. Click on "**Create token**"
5. Copy the token and enter it into the input field on the update access token page of Aikido<br>

   <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FUrQEqurtCGh5y4ZdSQFB%2FScherm%C2%ADafbeelding%202025-12-11%20om%2012.15.09.png?alt=media&#x26;token=69832055-017e-4d4e-8989-00e3061e206a" alt=""><figcaption></figcaption></figure>

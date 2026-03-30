# Source: https://help.aikido.dev/aikido-autofix/configure/autofix-for-gitlab-cloud-with-personal-access-token.md

# AutoFix for Gitlab Cloud with Personal Access Token

> When the installation of the Gitlab Autofix integration does not work via the OAuth flow, you can also configure it to work with a Personal Access Token (PAT).

### Go to PAT management page in Aikido <a href="#go-to-pat-management-page-in-aikido" id="go-to-pat-management-page-in-aikido"></a>

**First**, go to the PAT management page in Aikdo, which can be [found here](https://app.aikido.dev/settings/integrations/gitlab/autofix/personal-access-token).

**Next**, follow the instructions below to generate an access token in Gitlab.

## Generate a "Group Access Token" in Gitlab <a href="#generate-a-group-access-token-in-gitlab" id="generate-a-group-access-token-in-gitlab"></a>

1. Navigate to '**Settings**' > '**Access tokens**', via the navigation of your Group's page

   Or use the shortcut link '**Generate Access Token here**' on the personal access token management page in Aikido.

   ![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-0fc8dc37da02d72f78b7bba57748ab5518334b62%2Fautofix-for-gitlab-cloud-with-personal-access-token_b7aaabca-d429-4cf9-b392-f7216b763827.png?alt=media)
2. You should end up on a page similar to this\
   You can navigate to this page yourself by opening your group's settings menu and selecting "**Access tokens**"

   ![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-c0bc11b4585c29e0ebe1f4fb8ac58ca61705362d%2Fautofix-for-gitlab-cloud-with-personal-access-token_5b98fb9f-55ab-4620-a02e-c191ee53d5a9.png?alt=media)
3. Click on "**Add** **new token**"
4. Enter a name for token, we suggest something like: "**Aikido Security Autofix**"
5. For the expiration, use custom defined and set it to 1 year from now, or remove it.
6. The token should have at least the role of "**Developer**"
7. Next you need to select the following permissions for the token: **api** and **write\_repository.**

   ![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-88f4970c1ee133ad4beebbe99060d2791f3bb5cb%2Fautofix-for-gitlab-cloud-with-personal-access-token_06499262-d7c4-4813-b6af-d800c0be6cc9.png?alt=media)
8. Click on "**Create group access token**".
9. Copy the token on the next screen and insert it on the personal access token management page in Aikido.

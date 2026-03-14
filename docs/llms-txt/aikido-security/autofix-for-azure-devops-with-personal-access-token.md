# Source: https://help.aikido.dev/aikido-autofix/configure/autofix-for-azure-devops-with-personal-access-token.md

# AutoFix for Azure DevOps with Personal Access Token

> When the installation of the Azure DevOps Autofix integration does not work via the OAuth flow, you can also configure it to work with a Personal Access Token (PAT).

> Please note that for the integration to work properly, you need to be able to have write access in all of the projects in your organization. This is usually a reserved permission for workspace admins.

**First**, go to the PAT management page in Aikido, which can be [found here](https://app.aikido.dev/settings/integrations/azure-devops/autofix/personal-access-token).

**Next**, follow the instructions below to generate a PAT in Azure DevOps.

## Generating a PAT <a href="#generating-a-pat" id="generating-a-pat"></a>

1. Navigate to '**User Settings**' > '**Personal Access Tokens**', via the header icon shown here

   ![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-dbdf98d9c26bf068a22f453cd3fa94fb3b0d392f%2Fautofix-for-azure-devops-with-personal-access-token_f8a540f7-125a-4b1e-a244-74b276d4d57e.png?alt=media)

   Or use the shortcut link '**Generate Access Token here**' on the personal access token management page in Aikido.

   ![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-0fc8dc37da02d72f78b7bba57748ab5518334b62%2Fautofix-for-azure-devops-with-personal-access-token_1cf64447-e410-41ee-90d3-f54530e55d9b.png?alt=media)
2. You should end up on a page similar to this

   ![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-d893201a3719b19f2dda8b241d48dce920cbdd3b%2Fautofix-for-azure-devops-with-personal-access-token_9e46833a-3d8c-484d-a9fe-d444b6b6da34.png?alt=media)
3. Make sure you have selected the same organization as the one in your Aikido workspace via the '**Access scope**' button on the top right
4. Click on "**New token**"
5. Next you need to select the following permissions for the token: **Code (Read & Write)** and **Graph (Read).**\
   If you don't see the **Graph** scope appear, you will have to click the blue link at the bottom "Show more scopes"

   ![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-c082c4b54615aecd91faf828a6f3ad7606f19195%2Fautofix-for-azure-devops-with-personal-access-token_49b6487f-4d4f-4e45-8609-17959ec311dc.png?alt=media)
6. For the expiration, use custom defined and set it to 1 year from now, this is the maximum duration that Azure DevOps allows the token to be valid for.
7. Click on '**Create**' to create the access token
8. Copy the token on the next screen and insert it on the personal access token management page in Aikido.

# Source: https://help.aikido.dev/pr-and-release-gating/azure-pr-gating/azure-pipelines-ci-pr-gating-via-aikido-dashboard-with-a-personal-access-token.md

# Azure DevOps: PR Gating via Aikido Dashboard with a Personal Access Token

{% hint style="info" %}
We recommend setting up this integration with a **newly created user** in Azure (e.g. called Aikido). The commenting feature uses the name of the user who has set up the integration.
{% endhint %}

{% hint style="warning" %}
Please note that for the integration to work properly, you must be able to manage service hooks in all projects within your organization. This is usually a reserved permission for Azure workspace admins.
{% endhint %}

**First**, go to the PAT management page in Aikido, which can be [found here](https://app.aikido.dev/settings/integrations/azure-devops/checks/personal-access-token).

**Next**, follow the instructions below to generate a PAT in Azure DevOps.

## Generating a PAT <a href="#generating-a-pat" id="generating-a-pat"></a>

1. Navigate to '**User Settings**' > '**Personal Access Tokens**', via the header icon shown here

   ![User settings menu highlighted near search and profile options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-dbdf98d9c26bf068a22f453cd3fa94fb3b0d392f%2Fazure-pipelines-ci-pr-gating-via-aikido-dashboard-with-a-personal-access-token_6a98aaa9-d4dd-439c-8523-1243b85bccd2.png?alt=media)

   Or use the shortcut link '**Generate Access Token here**' on the personal access token management page in Aikido.

   ![Input field for personal access token with option to generate or update token.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-0fc8dc37da02d72f78b7bba57748ab5518334b62%2Fazure-pipelines-ci-pr-gating-via-aikido-dashboard-with-a-personal-access-token_734148e7-1b81-4ffe-9987-0bcfc390e36e.png?alt=media)
2. You should end up on a page similar to this

   ![Azure DevOps: No personal access tokens created; option to generate a new token available.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-d893201a3719b19f2dda8b241d48dce920cbdd3b%2Fazure-pipelines-ci-pr-gating-via-aikido-dashboard-with-a-personal-access-token_d9e644dd-79a8-4d81-a3b2-9942a34c5ec9.png?alt=media)
3. Make sure you have selected the same organization as the one in your Aikido workspace via the '**Access scope**' button on the top right
4. Click on "**New token**"
5. Next you need to select the following permissions for the token: **Work Items (Read & Write)**, **Code (Read & Write)**, **Code (Status)** and **Build (Read)**

   ![Creating a custom personal access token with specific security and repository permissions.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-571c2d2b193e2f56b51ebb4f7f65cf5ccf969e6f%2Fazure-pipelines-ci-pr-gating-via-aikido-dashboard-with-a-personal-access-token_33865be9-0c62-4642-8ae7-b47280f0f4be.png?alt=media)
6. For the expiration, use custom defined and set it to 1 year from now, this is the maximum duration that Azure DevOps allows the token to be valid for.
7. Click on '**Create**' to create the access token
8. Copy the token on the next screen and insert it on the personal access token management page in Aikido.

{% hint style="info" %}
If you've added new repositories after the initial setup, you'll need to configure those repos as well.

To apply a default configuration automatically, see [Default PR/MR gating configuration for new repositories](https://help.aikido.dev/pr-and-release-gating/aikido-ci-gating-functionality/default-pr-mr-gating-configuration-for-new-repositories).
{% endhint %}

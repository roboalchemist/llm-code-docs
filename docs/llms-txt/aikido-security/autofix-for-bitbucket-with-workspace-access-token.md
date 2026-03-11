# Source: https://help.aikido.dev/aikido-autofix/configure/autofix-for-bitbucket-with-workspace-access-token.md

# AutoFix for Bitbucket with Workspace Access Token

> When the installation of the Bitbucket Autofix integration does not work via the OAuth flow or you don't want to have it linked to a user in Bitbucket, you can also configure it to work with a Workspace Access Token (WAT).

### Go to PAT management page in Aikido <a href="#go-to-pat-management-page-in-aikido" id="go-to-pat-management-page-in-aikido"></a>

**First**, go to the PAT management page in Aikdo, which can be [found here](https://app.aikido.dev/settings/integrations/bitbucket/autofix/workspace-access-token).

**Next**, follow the instructions below to generate an access token in Bitbucket.

## Generate a "Workspace Access Token" in Bitbucket <a href="#generate-a-group-access-token-in-gitlab" id="generate-a-group-access-token-in-gitlab"></a>

1. Navigate to '**Workspace Settings**' > '**Access tokens**', via the navigation of your Bitbucket workspace page
2. You should land on a page similar to this<br>

   <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fw6YDWP1S5sqDbyfhdyGq%2FScherm%C2%ADafbeelding%202025-10-17%20om%2011.38.15.png?alt=media&#x26;token=8d4ad5d9-d12c-49b1-b65f-4fb8a6692025" alt="" width="563"><figcaption></figcaption></figure>
3. Click on "**Create access token**"
4. Enter a name for token, we suggest something like: "**Aikido Security Autofix**"
5. For the expiration, we recommend to select "No expiry"
6. Next you need to select the following permissions for the token: "**Repositories:write**" and **"Pull requests:write"**.
7. The access token configuration modal should look like this<br>

   <figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F0gfOMsT3H3Nj9yiIkuN1%2FScherm%C2%ADafbeelding%202025-10-17%20om%2011.39.10.png?alt=media&#x26;token=dcbcb762-2a40-4054-a737-c0186cf79d76" alt="" width="375"><figcaption></figcaption></figure>
8. When you are done, click on "**Create**"
9. Copy the token on the next screen and insert it on the personal access token management page in Aikido.

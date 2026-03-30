# Source: https://pipedream.com/docs/apps/integrated-apps/service-now.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# ServiceNow

<Note>
  Since ServiceNow requires OAuth configuration in your instance, **you need to manually configure two OAuth apps in your ServiceNow instance** to grant access tokens and authenticate requests to the REST API.

  Please follow the steps below to set up the required OAuth applications.
</Note>

## Create External Client OAuth App

<Steps>
  <Step title="Access ServiceNow Developer Portal">
    Sign into your [ServiceNow Developer Portal](https://developer.servicenow.com/dev.do#!/home) account to create or access an instance.
  </Step>

  <Step title="Navigate to Application Registry">
    Go to **System OAuth > Application Registry**.

    ![Find the OAuth Client option under the ServiceNow application registry](https://res.cloudinary.com/pipedreamin/image/upload/v1715264549/marketplace/apps/servicenow/CleanShot_2024-05-09_at_10.18.36_ntausg.png)
  </Step>

  <Step title="Create New Application">
    Create a new app by selecting **New** in the top right corner.

    ![Create a new ServiceNow application under the OAuth Clients section in the Application Registry](https://res.cloudinary.com/pipedreamin/image/upload/v1715265062/marketplace/apps/servicenow/CleanShot_2024-05-09_at_10.30.51_jpi4ct.png)
  </Step>

  <Step title="Select OAuth API Endpoint">
    Choose **Create an OAuth API endpoint for external clients**.

    ![Create a new app, and make sure to choose the OAuth API endpoint for external clients option](https://res.cloudinary.com/pipedreamin/image/upload/v1715264615/marketplace/apps/servicenow/CleanShot_2024-05-09_at_10.19.09_pgezqf.png)
  </Step>

  <Step title="Configure Application Settings">
    Name your app `Pipedream`. Use the default settings but specify the **Redirect URL**:

    ```text  theme={null}
    https://api.pipedream.com/connect/oauth/oa_g2oiqA/callback
    ```
  </Step>

  <Step title="Create and Verify">
    Click **Create**. The app will appear in the Application Registry once created.

    ![You should see the Pipedream app listed in the ServiceNow Registry after making those changes](https://res.cloudinary.com/pipedreamin/image/upload/v1715264960/marketplace/apps/servicenow/CleanShot_2024-05-09_at_10.21.12_iwlxgq.png)
  </Step>
</Steps>

## Create OAuth Validator App

<Steps>
  <Step title="Copy Credentials">
    Copy the client ID and secret from the `Pipedream` app you created above.
  </Step>

  <Step title="Create OAuth Provider App">
    Go back to **System OAuth > Application Registry > New** and select **Connect to an OAuth Provider (simplified)**.
  </Step>

  <Step title="Configure Validator Settings">
    Name this app `Pipedream OAuth Validator` and add the previously copied client ID and secret.
  </Step>

  <Step title="Set Authorization Details">
    Set the grant type to **Authorization Code** and the **Token URL** to `oauth_token.do`.
  </Step>

  <Step title="Add Redirect URL">
    Use the same **Redirect URL** as before:

    ```text  theme={null}
    https://api.pipedream.com/connect/oauth/oa_g2oiqA/callback
    ```
  </Step>
</Steps>

## Connect to Pipedream

<Steps>
  <Step title="Access Pipedream Accounts">
    Visit [Pipedream's account page](https://pipedream.com/accounts), and click **Click Here to Connect An App**.
  </Step>

  <Step title="Search for ServiceNow">
    Search for **ServiceNow** and select it.
  </Step>

  <Step title="Enter Connection Details">
    Enter the client ID, client secret, and your instance name (e.g., `dev98042` from `https://dev98042.service-now.com/`).
  </Step>

  <Step title="Authorize Connection">
    Press **Connect**. A new window will prompt you to login to your ServiceNow instance, authorizing Pipedream's access to the ServiceNow REST API.
  </Step>
</Steps>

## Troubleshooting

<Note>
  **For Hardened or Mature Instances**: The standard instructions may not apply perfectly to customized or hardened ServiceNow instances. If you face a **504 Gateway Time-out** error or similar issues, consider these additional steps:

* Assign a dedicated role and service account for this integration
* Ensure the role has ACLs configured for the `oauth_credential` table and other necessary tables

  For detailed authorization flow reference, see [ServiceNow's OAuth documentation](https://docs.servicenow.com/bundle/orlando-platform-administration/page/administer/security/concept/c_OAuthAuthorizationCodeFlow.html).
</Note>

Built with [Mintlify](https://mintlify.com).

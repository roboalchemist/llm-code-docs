# Source: https://infisical.com/docs/integrations/app-connections/cloudflare.md

# Cloudflare Connection

> Learn how to configure a Cloudflare Connection for Infisical.

Infisical supports connecting to Cloudflare using API tokens and Account ID for secure access to your Cloudflare services.

## Configure API Token and Account ID for Infisical

<Steps>
  <Step title="Create API Token">
    Navigate to your Cloudflare dashboard and go to **Profile**.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/cloudflare/cloudflare-navigate-profile.png" alt="Navigate Cloudflare Profile" />

    Click **API Tokens > Create Token** to generate a new API token.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/cloudflare/cloudflare-create-token.png" alt="Create API Token" />
  </Step>

  <Step title="Configure Token Permissions">
    Configure your API token with the necessary permissions for your Cloudflare services.

    Depending on your use case, add one or more of the following permission sets to your API token:

    <Tabs>
      <Tab title="Secret Sync">
        <AccordionGroup>
          <Accordion title="Cloudflare Pages">
            Use the following permissions to grant Infisical access to sync secrets to Cloudflare Pages:

                        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/cloudflare/cloudflare-pages-configure-permissions.png" alt="Configure Token" />

            **Required Permissions:**

            * **Account** - **Cloudflare Pages** - **Edit**
            * **Account** - **Account Settings** - **Read**

            Add these permissions to your API token and click **Continue to summary**, then **Create Token** to generate your API token.
          </Accordion>

          <Accordion title="Cloudflare Workers">
            Use the following permissions to grant Infisical access to sync secrets to Cloudflare Workers:

                        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/cloudflare/cloudflare-workers-configure-permissions.png" alt="Configure Token" />

            **Required Permissions:**

            * **Account** - **Workers Scripts** - **Edit**
            * **Account** - **Account Settings** - **Read**

            Add these permissions to your API token and click **Continue to summary**, then **Create Token** to generate your API token.
          </Accordion>
        </AccordionGroup>
      </Tab>

      <Tab title="PKI">
        Use the following permissions to grant Infisical access to verify certificates using DNS TXT records with ACME:

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/cloudflare/cloudflare-dns-configure-permissions.png" alt="Configure Token" />

        **Required Permissions:**

        * **Account** - **Account Settings** - **Read**
        * **Zone** - **DNS** - **Edit**

        Add these permissions to your API token and click **Continue to summary**, then **Create Token** to generate your API token.
      </Tab>
    </Tabs>
  </Step>

  <Step title="Save Your API Token">
    After creation, copy and securely store your API token as it will not be shown again.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/cloudflare/cloudflare-generated-token.png" alt="Generated API Token" />

    <Warning>
      Keep your API token secure and do not share it. Anyone with access to this token can manage your Cloudflare resources based on the permissions granted.
    </Warning>
  </Step>

  <Step title="Get Account ID">
    From your Cloudflare Account Home page, click on the account information dropdown and select **Copy account ID**.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/cloudflare/cloudflare-account-id.png" alt="Account ID" />

    Save your Account ID for use in the next step.
  </Step>
</Steps>

## Setup Cloudflare Connection in Infisical

<Steps>
  <Step title="Navigate to App Connections">
    Navigate to the **App Connections** page in the desired project. <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/general/add-connection.png" alt="App Connections
    Tab" />
  </Step>

  <Step title="Add Connection">
    Select the **Cloudflare Connection** option from the connection options
    modal. <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/cloudflare/cloudflare-app-connection-select.png" alt="Select Cloudflare
    Connection" />
  </Step>

  <Step title="Input Credentials">
    Enter your Cloudflare API token and Account ID in the provided fields and
    click **Connect to Cloudflare** to establish the connection. <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/cloudflare/cloudflare-app-connection-form.png" alt="Connect to
    Cloudflare" />
  </Step>

  <Step title="Connection Created">
    Your **Cloudflare Connection** is now available for use in your Infisical
    projects. <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/cloudflare/cloudflare-app-connection-created.png" alt="Cloudflare Connection
    Created" />
  </Step>
</Steps>

<Info>
  API token connections require manual token rotation when your Cloudflare API
  token expires or is regenerated. Monitor your connection status and update the
  token as needed.
</Info>

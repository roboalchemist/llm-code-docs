# Source: https://infisical.com/docs/integrations/secret-syncs/vercel.md

# Source: https://infisical.com/docs/integrations/app-connections/vercel.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Vercel Connection

> Learn how to configure a Vercel Connection for Infisical.

Infisical supports connecting to Vercel using API Tokens.

## Setup Vercel Connection in Infisical

<Steps>
  <Step title="Move to API Tokens on Vercel">
    Navigate to the Vercel **Account Settings** page by clicking on your profile icon in the top-right corner.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/vercel/vercel-main-page.png" alt="Vercel API Tokens Tab" />
  </Step>

  <Step title="Open API Tokens Tab">
    Select the **API Tokens** tab from the left sidebar navigation menu.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/vercel/vercel-settings-page.png" alt="Vercel API Tokens Tab" />
  </Step>

  <Step title="Create the API Token">
    Click the **Create** button and provide a name for your token (e.g., "Infisical Integration").
    Choose appropriate scope permissions based on your requirements.

    <Note>
      If you configure an expiry date for your API token, you will need to manually rotate to a new token prior to expiration to avoid integration downtime. Consider setting a calendar reminder for this task.
    </Note>

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/vercel/vercel-create-token.png" alt="Vercel Create API Token" />
  </Step>

  <Step title="Copy the API Token">
    After creation, a modal with the API token will be displayed. Copy this token immediately and store it securely, as you won't be able to view it again after closing this dialog.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/vercel/vercel-copy-token.png" alt="Vercel Copy API Token" />
  </Step>

  <Step title="Token Created">
    You should now see your newly created token in the list of API tokens on the Vercel dashboard.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/vercel/vercel-token-created.png" alt="Vercel Connection Created" />
  </Step>

  <Step title="Setup Vercel Connection in Infisical">
    <Tabs>
      <Tab title="Infisical UI">
        1. Navigate to App Connections

           In your Infisical dashboard, navigate to the **Integrations** tab in the desired project, then select **App Connections**.
           <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/general/add-connection.png" alt="App Connections Tab" />
        2. Add Connection

           Click the **+ Add Connection** button and select the **Vercel Connection** option from the available integrations.
           <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/vercel/vercel-app-connection-option.png" alt="Select Vercel Connection" />
        3. Fill the Vercel Connection Modal

           Complete the Vercel Connection form by entering:

           * A descriptive name for the connection
           * The API Token you generated in steps 3-4
           * An optional description for future reference
             <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/vercel/vercel-app-connection-modal.png" alt="Vercel Connection Modal" />
        4. Connection Created

           After clicking Create, your **Vercel Connection** is established and ready to use with your Infisical project.
           <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/vercel/vercel-app-connection-created.png" alt="Vercel Connection Created" />
      </Tab>

      <Tab title="API">
        To create a Vercel Connection, make an API request to the [Create Vercel
        Connection](/api-reference/endpoints/app-connections/vercel/create) API endpoint.

        ### Sample request

        ```bash Request theme={"dark"}
        curl    --request POST \
                --url https://app.infisical.com/api/v1/app-connections/vercel \
                --header 'Content-Type: application/json' \
                --data '{
                    "name": "my-vercel-connection",
                    "projectId": "7ffbb072-2575-495a-b5b0-127f88caef78",
                    "method": "api-token",
                    "credentials": {
                        "apiToken": "...",
                    }
                }'
        ```

        ### Sample response

        ```bash Response theme={"dark"}
        {
            "appConnection": {
                "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
                "name": "my-vercel-connection",
                "projectId": "7ffbb072-2575-495a-b5b0-127f88caef78",
                "version": 123,
                "orgId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
                "createdAt": "2025-04-01T05:31:56Z",
                "updatedAt": "2025-04-01T05:31:56Z",
                "app": "vercel",
                "method": "api-token",
                "credentials": {}
            }
        }
        ```
      </Tab>
    </Tabs>
  </Step>
</Steps>

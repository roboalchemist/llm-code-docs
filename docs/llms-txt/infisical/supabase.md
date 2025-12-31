# Source: https://infisical.com/docs/integrations/secret-syncs/supabase.md

# Source: https://infisical.com/docs/integrations/app-connections/supabase.md

# Source: https://infisical.com/docs/integrations/secret-syncs/supabase.md

# Source: https://infisical.com/docs/integrations/app-connections/supabase.md

# Source: https://infisical.com/docs/integrations/secret-syncs/supabase.md

# Source: https://infisical.com/docs/integrations/cloud/supabase.md

# Source: https://infisical.com/docs/integrations/app-connections/supabase.md

# Source: https://infisical.com/docs/integrations/secret-syncs/supabase.md

# Source: https://infisical.com/docs/integrations/cloud/supabase.md

# Source: https://infisical.com/docs/integrations/app-connections/supabase.md

# Supabase Connection

> Learn how to configure a Supabase Connection for Infisical.

Infisical supports the use of [Personal Access Tokens](https://supabase.com/dashboard/account/tokens) to connect with Supabase.

## Create a Supabase Personal Access Token

<Steps>
  <Step title="Click the profile image in the top-right corner and select 'Account Preferences'">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/supabase/app-connection-user-settings.png" alt="Account Preferences" />
  </Step>

  <Step title="In the sidebar, select 'Access Tokens'">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/supabase/app-connection-api-keys.png" alt="Settings Page" />
  </Step>

  <Step title="In the access tokens page, click on 'Generate New Token'">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/supabase/app-connection-create-api-key.png" alt="Access Tokens Page" />
  </Step>

  <Step title="Enter a token name and click on 'Generate Token'">
    Provide a descriptive name for the token.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/supabase/app-connection-create-form.png" alt="Enter Name" />
  </Step>

  <Step title="Copy the generated token and save it">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/supabase/app-connection-key-generated.png" alt="Create Token" />
  </Step>
</Steps>

## Create a Supabase Connection in Infisical

<Tabs>
  <Tab title="Infisical UI">
    <Steps>
      <Step title="Navigate to App Connections">
        In your Infisical dashboard, navigate to the **App Connections** page in the desired project.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/general/add-connection.png" alt="App Connections Tab" />
      </Step>

      <Step title="Select Supabase Connection">
        Click **+ Add Connection** and choose **Supabase Connection** from the list of integrations.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/supabase/app-connection-option.png" alt="Select Supabase Connection" />
      </Step>

      <Step title="Fill out the Supabase Connection form">
        Complete the form by providing:

        * A descriptive name for the connection
        * An optional description
        * Supabase instance URL (e.g., `https://your-domain.com` or `https://api.supabase.com`)
        * The Access Token value from the previous step

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/supabase/app-connection-form.png" alt="Supabase Connection Modal" />
      </Step>

      <Step title="Connection created">
        After submitting the form, your **Supabase Connection** will be successfully created and ready to use with your Infisical project.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/supabase/app-connection-generated.png" alt="Supabase Connection Created" />
      </Step>
    </Steps>
  </Tab>

  <Tab title="API">
    To create a Supabase Connection via API, send a request to the [Create Supabase Connection](/api-reference/endpoints/app-connections/supabase/create) endpoint.

    ### Sample request

    ```bash Request theme={"dark"}
    curl    --request POST \
            --url https://app.infisical.com/api/v1/app-connections/supabase \
            --header 'Content-Type: application/json' \
            --data '{
                "name": "my-supabase-connection",
                "method": "access-token",
                "projectId": "7ffbb072-2575-495a-b5b0-127f88caef78",
                "credentials": {
                    "accessToken": "[Access Token]",
                    "instanceUrl": "https://api.supabase.com"
                }
            }'
    ```

    ### Sample response

    ```bash Response theme={"dark"}
    {
      "appConnection": {
          "id": "e5d18aca-86f7-4026-a95e-efb8aeb0d8e6",
          "name": "my-supabase-connection",
          "projectId": "7ffbb072-2575-495a-b5b0-127f88caef78",
          "description": null,
          "version": 1,
          "orgId": "6f03caa1-a5de-43ce-b127-95a145d3464c",
          "createdAt": "2025-04-23T19:46:34.831Z",
          "updatedAt": "2025-04-23T19:46:34.831Z",
          "isPlatformManagedCredentials": false,
          "credentialsHash": "7c2d371dec195f82a6a0d5b41c970a229cfcaf88e894a5b6395e2dbd0280661f",
          "app": "supabase",
          "method": "access-token",
          "credentials": {
            "instanceUrl": "https://api.supabase.com"
          }
      }
    }
    ```
  </Tab>
</Tabs>

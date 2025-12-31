# Source: https://infisical.com/docs/integrations/secret-syncs/checkly.md

# Source: https://infisical.com/docs/integrations/app-connections/checkly.md

# Source: https://infisical.com/docs/integrations/secret-syncs/checkly.md

# Source: https://infisical.com/docs/integrations/app-connections/checkly.md

# Source: https://infisical.com/docs/integrations/secret-syncs/checkly.md

# Source: https://infisical.com/docs/integrations/cloud/checkly.md

# Source: https://infisical.com/docs/integrations/app-connections/checkly.md

# Source: https://infisical.com/docs/integrations/secret-syncs/checkly.md

# Source: https://infisical.com/docs/integrations/cloud/checkly.md

# Source: https://infisical.com/docs/integrations/app-connections/checkly.md

# Checkly Connection

> Learn how to configure a Checkly Connection for Infisical.

Infisical supports the use of [API Keys](https://app.checklyhq.com/settings/user/api-keys) to connect with Checkly.

<Note>
  Checkly requires the account user to have Read/Write or Admin permissions
</Note>

## Create a Checkly API Token

<Steps>
  <Step title="Click the profile image in the top-right corner and select 'User Settings'">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/checkly/checkly-app-connection-profile.png" alt="Dashboard Page" />
  </Step>

  <Step title="In the user settings sidebar, select 'API Keys'">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/checkly/checkly-app-connection-api-keys.png" alt="User Settings Page" />
  </Step>

  <Step title="In the api keys page, click on 'Create API Key'">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/checkly/checkly-app-connection-create-api-key.png" alt="Api Keys Page" />
  </Step>

  <Step title="Enter a token name and click on 'Create API Key'">
    Provide a descriptive name for the token.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/checkly/checkly-app-connection-create-form.png" alt="Enter Name" />
  </Step>

  <Step title="Copy the generated key and save it">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/checkly/checkly-app-connection-key-generated.png" alt="Create Token" />
  </Step>
</Steps>

## Create a Checkly Connection in Infisical

<Tabs>
  <Tab title="Infisical UI">
    <Steps>
      <Step title="Navigate to App Connections">
        In your Infisical dashboard, navigate to the **App Connections** page in the desired project.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/general/add-connection.png" alt="App Connections Tab" />
      </Step>

      <Step title="Select Checkly Connection">
        Click **+ Add Connection** and choose **Checkly Connection** from the list of integrations.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/checkly/checkly-app-connection-option.png" alt="Select Checkly Connection" />
      </Step>

      <Step title="Fill out the Checkly Connection form">
        Complete the form by providing:

        * A descriptive name for the connection
        * An optional description
        * The API Key value from the previous step

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/checkly/checkly-app-connection-form.png" alt="Checkly Connection Modal" />
      </Step>

      <Step title="Connection created">
        After submitting the form, your **Checkly Connection** will be successfully created and ready to use with your Infisical project.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/checkly/checkly-app-connection-generated.png" alt="Checkly Connection Created" />
      </Step>
    </Steps>
  </Tab>

  <Tab title="API">
    To create a Checkly Connection via API, send a request to the [Create Checkly Connection](/api-reference/endpoints/app-connections/checkly/create) endpoint.

    ### Sample request

    ```bash Request theme={"dark"}
    curl    --request POST \
            --url https://app.infisical.com/api/v1/app-connections/checkly \
            --header 'Content-Type: application/json' \
            --data '{
                "name": "my-checkly-connection",
                "method": "api-key",
                "projectId": "7ffbb072-2575-495a-b5b0-127f88caef78",
                "credentials": {
                    "apiKey": "[API KEY]"
                }
            }'
    ```

    ### Sample response

    ```bash Response theme={"dark"}
    {
      "appConnection": {
          "id": "e5d18aca-86f7-4026-a95e-efb8aeb0d8e6",
          "name": "my-checkly-connection",
          "projectId": "7ffbb072-2575-495a-b5b0-127f88caef78",
          "description": null,
          "version": 1,
          "orgId": "6f03caa1-a5de-43ce-b127-95a145d3464c",
          "createdAt": "2025-04-23T19:46:34.831Z",
          "updatedAt": "2025-04-23T19:46:34.831Z",
          "isPlatformManagedCredentials": false,
          "credentialsHash": "7c2d371dec195f82a6a0d5b41c970a229cfcaf88e894a5b6395e2dbd0280661f",
          "app": "checkly",
          "method": "api-key",
          "credentials": {}
      }
    }
    ```
  </Tab>
</Tabs>

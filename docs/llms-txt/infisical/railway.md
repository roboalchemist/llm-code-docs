# Source: https://infisical.com/docs/integrations/secret-syncs/railway.md

# Source: https://infisical.com/docs/integrations/cloud/railway.md

# Source: https://infisical.com/docs/integrations/app-connections/railway.md

# Railway Connection

> Learn how to configure a Railway Connection for Infisical.

Infisical supports the use of [API Tokens](https://docs.railway.com/guides/public-api#creating-a-token) to connect with Railway.

## Create a Railway API Token

<Tabs>
  <Tab title="Team Token">
    A team token provides access to all resources within a team. It cannot be used to access personal resources in Railway.

    <Steps>
      <Step title="Click the profile image in the top-right corner and select 'Account Settings'">
                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/railway/railway-app-connection-account-settings.png" alt="Dashboard Page" />
      </Step>

      <Step title="In the personal settings sidebar, click on 'Tokens'">
                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/railway/railway-app-connection-account-settings-tokens.png" alt="Account Settings Page" />
      </Step>

      <Step title="Enter a token name and select a team">
        Make sure to provide a descriptive name and select the correct team.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/railway/railway-app-connection-team-token-form.png" alt="Enter Name and Select Team" />
      </Step>

      <Step title="Click on 'Create'">
                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/railway/railway-app-connection-team-token-create.png" alt="Create Token" />
      </Step>

      <Step title="Save the token">
        After clicking 'Create', your access token will be displayed. Save it securely for later use.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/railway/railway-app-connection-team-token-created.png" alt="Copy Token Modal" />
      </Step>
    </Steps>
  </Tab>

  <Tab title="Account Token">
    If no team is selected, the token will be associated with your personal Railway account and will have access to all your individual and team resources.

    <Steps>
      <Step title="Click the profile image in the top-right corner and select 'Account Settings'">
                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/railway/railway-app-connection-account-settings.png" alt="Dashboard Page" />
      </Step>

      <Step title="In the personal settings sidebar, click on 'Tokens'">
                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/railway/railway-app-connection-account-settings-tokens.png" alt="Account Settings Page" />
      </Step>

      <Step title="Enter a token name and select 'No workspace'">
        Provide a descriptive name and ensure no team is selected. This will create an account-level token.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/railway/railway-app-connection-account-token-form.png" alt="Enter Name" />
      </Step>

      <Step title="Click on 'Create'">
                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/railway/railway-app-connection-account-token-create.png" alt="Create Token" />
      </Step>

      <Step title="Save the token">
        After clicking 'Create', your access token will be shown. Save it for future use.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/railway/railway-app-connection-account-token-created.png" alt="Copy Token Modal" />
      </Step>
    </Steps>
  </Tab>

  <Tab title="Project Token">
    Project tokens are limited to a specific environment within a project and can only be used to authenticate requests to that environment.

    <Steps>
      <Step title="Open your Railway dashboard and click on a project">
                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/railway/railway-app-connection-project-token-dashboard.png" alt="Dashboard Page" />
      </Step>

      <Step title="On the project page, click 'Settings' in the top-right corner">
                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/railway/railway-app-connection-project-token-project.png" alt="Project Settings Page" />
      </Step>

      <Step title="In the left sidebar, scroll to the bottom and click on 'Tokens'">
                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/railway/railway-app-connection-project-token-settings.png" alt="Project Token Settings Page" />
      </Step>

      <Step title="Enter a token name and select an environment">
        Provide a descriptive name and select the appropriate environment for the token.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/railway/railway-app-connection-project-token-form.png" alt="Enter Name and Select environment" />
      </Step>

      <Step title="Click on 'Create'">
                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/railway/railway-app-connection-project-token-create.png" alt="Create Token" />
      </Step>

      <Step title="Save the token">
        After clicking 'Create', the access token will be displayed. Be sure to save it for later use.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/railway/railway-app-connection-project-token-created.png" alt="Copy Token Modal" />
      </Step>
    </Steps>
  </Tab>
</Tabs>

## Create a Railway Connection in Infisical

<Tabs>
  <Tab title="Infisical UI">
    <Steps>
      <Step title="Navigate to App Connections">
        In your Infisical dashboard, navigate to the **App Connections** page in the desired project.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/general/add-connection.png" alt="App Connections Tab" />
      </Step>

      <Step title="Select Railway Connection">
        Click **+ Add Connection** and choose **Railway Connection** from the list of integrations.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/railway/railway-app-connection-option.png" alt="Select Railway Connection" />
      </Step>

      <Step title="Fill out the Railway Connection form">
        Complete the form by providing:

        * A descriptive name for the connection
        * An optional description
        * The type of token you created earlier
        * The token value from the previous step

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/railway/railway-app-connection-form.png" alt="Railway Connection Modal" />
      </Step>

      <Step title="Connection created">
        After submitting the form, your **Railway Connection** will be successfully created and ready to use with your Infisical project.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/railway/railway-app-connection-generated.png" alt="Railway Connection Created" />
      </Step>
    </Steps>
  </Tab>

  <Tab title="API">
    To create a Railway Connection via API, send a request to the [Create Railway Connection](/api-reference/endpoints/app-connections/railway/create) endpoint.

    ### Sample request

    ```bash Request theme={"dark"}
    curl    --request POST \
            --url https://app.infisical.com/api/v1/app-connections/railway \
            --header 'Content-Type: application/json' \
            --data '{
                "name": "my-railway-connection",
                "method": "team-token",
                "projectId": "7ffbb072-2575-495a-b5b0-127f88caef78",
                "credentials": {
                    "apiToken": "[TEAM TOKEN]"
                }
            }'
    ```

    ### Sample response

    ```bash Response theme={"dark"}
    {
      "appConnection": {
          "id": "e5d18aca-86f7-4026-a95e-efb8aeb0d8e6",
          "name": "my-railway-connection",
          "projectId": "7ffbb072-2575-495a-b5b0-127f88caef78",
          "description": null,
          "version": 1,
          "orgId": "6f03caa1-a5de-43ce-b127-95a145d3464c",
          "createdAt": "2025-04-23T19:46:34.831Z",
          "updatedAt": "2025-04-23T19:46:34.831Z",
          "isPlatformManagedCredentials": false,
          "credentialsHash": "7c2d371dec195f82a6a0d5b41c970a229cfcaf88e894a5b6395e2dbd0280661f",
          "app": "railway",
          "method": "team-token",
          "credentials": {}
      }
    }
    ```
  </Tab>
</Tabs>

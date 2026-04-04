# Source: https://infisical.com/docs/integrations/secret-syncs/octopus-deploy.md

# Source: https://infisical.com/docs/integrations/app-connections/octopus-deploy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Octopus Deploy Connection

> Learn how to configure an Octopus Deploy Connection for Infisical.

Infisical supports the use of [API Keys](https://octopus.com/docs/octopus-rest-api/how-to-create-an-api-key) to connect with Octopus Deploy.

## Create Octopus Deploy API Key

Octopus Deploy supports two methods for creating API keys: via a user profile or via a service account.

<Tabs>
  <Tab title="Service Account API Key (Recommended)">
    <Steps>
      <Step title="Navigate to Service Accounts">
        From your Octopus Deploy dashboard, go to **Configuration** > **Users** and click on the **Create Service Accounts** button.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/octopus-deploy/service-account-nav.png" alt="Service Accounts" />
      </Step>

      <Step title="Create a new Service Account">
        Provide:

        * Username: A name for the service account
        * Display Name: A display name for the service account

        Then click **Save**.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/octopus-deploy/service-account-create.png" alt="Create Service Account" />
      </Step>

      <Step title="Create a Team">
        Navigate to **Configuration** > **Teams** and click **Add Team**.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/octopus-deploy/add-team.png" alt="Add Team" />

        Provide:

        * New Team Name: A name for the team
        * Team Description(optional): A description for the team
        * Select the team access type:
          * Accessible in the `current` space only
          * Accessible in all spaces(system team)

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/octopus-deploy/create-team.png" alt="Create Team" />
        Then click **Save**.
      </Step>

      <Step title="Add Service Account to Team">
        After creating the team, you will be redirected to the team details page. Click on the **Add Members** button.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/octopus-deploy/team-add-member.png" alt="Add Service Account to Team" />

        Select the service account you created in the previous step and click **Add**.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/octopus-deploy/team-add-member-select.png" alt="Add Service Account to Team" />
      </Step>

      <Step title="Add User Role to the team">
        After adding the service account to the team, Click on the **User Roles** tab and click **Include User Role** button.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/octopus-deploy/team-user-role.png" alt="Add User Role to Team" />

        Search for the **Project Contributor** role and click on the **Apply** button.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/octopus-deploy/team-apply-user-role.png" alt="Apply User Role to Team" />

        Click on the **Save** button.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/octopus-deploy/save-team-settings.png" alt="Save User Role to Team" />
      </Step>

      <Step title="Navigate to the API Keys section">
        After saving the team settings, we have to create an API key for the service account. Go back to **Configuration** > **Users** and find your service account. Click on the service account to view its details.

        Click on the **API Keys** section and click **New API Key**.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/octopus-deploy/service-account-api-key.png" alt="Create Service Account API Key" />
      </Step>

      <Step title="Generate an API Key">
        Provide a purpose for the key and set an expiry date, then click **Generate New**.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/octopus-deploy/service-account-api-key-generate.png" alt="Generate API Key" />
      </Step>

      <Step title="Copy the API Key securely">
        Make sure to copy the API key now, you won't be able to access it again.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/octopus-deploy/service-account-key-generated.png" alt="Service Account API Key Generated" />
      </Step>
    </Steps>
  </Tab>

  <Tab title="User Profile API Key">
    <Note>
      Infisical recommends using a service account for production integrations as they provide better security and are not tied to individual user accounts.
    </Note>

    <Steps>
      <Step title="Navigate to your user profile">
        From your Octopus Deploy dashboard, click on your profile in the bottom left corner and select **My profile**.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/octopus-deploy/app-connection-profile.png" alt="Octopus Deploy User Profile" />
      </Step>

      <Step title="Navigate to the My API Keys section">
        In your profile settings, go to the **My API Keys** tab and click **New API Key**.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/octopus-deploy/app-connection-api-keys.png" alt="API Keys Tab" />
      </Step>

      <Step title="Create a new API Key">
        Provide a purpose for the key. Set an expiry date, then click **Generate New**.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/octopus-deploy/app-connection-create-key.png" alt="Create API Key" />
      </Step>

      <Step title="Copy the API Key securely">
        Make sure to copy the API key now, you won't be able to access it again.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/octopus-deploy/app-connection-key-generated.png" alt="API Key Generated" />
      </Step>
    </Steps>
  </Tab>
</Tabs>

## Create an Octopus Deploy Connection in Infisical

<Tabs>
  <Tab title="Infisical UI">
    <Steps>
      <Step title="Navigate to App Connections">
        In your Infisical dashboard, navigate to the **Integrations** tab in the desired project, then select **App Connections**.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/general/add-connection.png" alt="App Connections Tab" />
      </Step>

      <Step title="Select Octopus Deploy Connection">
        Click **+ Add Connection** and choose **Octopus Deploy** Connection from the list of integrations.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/octopus-deploy/app-connection-option.png" alt="Select Octopus Deploy Connection" />
      </Step>

      <Step title="Fill out the Octopus Deploy Connection form">
        Complete the form by providing:

        * A descriptive name for the connection
        * An optional description
        * The Instance URL (e.g., [https://your-instance.octopus.app](https://your-instance.octopus.app))
        * The API Key from the previous step
          <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/octopus-deploy/app-connection-form.png" alt="Octopus Deploy Connection Modal" />
      </Step>

      <Step title="Connection created">
        After submitting the form, your **Octopus Deploy Connection** will be successfully created and ready to use with your Infisical project.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/octopus-deploy/app-connection-generated.png" alt="Octopus Deploy Connection Created" />
      </Step>
    </Steps>
  </Tab>

  <Tab title="API">
    To create an Octopus Deploy Connection via API, send a request to the [Create Octopus Deploy Connection](/api-reference/endpoints/app-connections/octopus-deploy/create) endpoint.

    ### Sample request

    ```bash Request theme={"dark"}
    curl    --request POST \
            --url https://app.infisical.com/api/v1/app-connections/octopus-deploy \
            --header 'Content-Type: application/json' \
            --data '{
                "name": "my-octopus-deploy-connection",
                "method": "api-key",
                "projectId": "abcdef12-3456-7890-abcd-ef1234567890",
                "credentials": {
                    "instanceUrl": "https://your-instance.octopus.app",
                    "apiKey": "[API KEY]"
                }
            }'
    ```

    ### Sample response

    ```json Response theme={"dark"}
    {
      "appConnection": {
          "id": "a1b2c3d4-5678-90ab-cdef-1234567890ab",
          "name": "my-octopus-deploy-connection",
          "description": null,
          "projectId": "abcdef12-3456-7890-abcd-ef1234567890",
          "version": 1,
          "orgId": "abcdef12-3456-7890-abcd-ef1234567890",
          "createdAt": "2025-10-13T10:15:00.000Z",
          "updatedAt": "2025-10-13T10:15:00.000Z",
          "isPlatformManagedCredentials": false,
          "credentialsHash": "d41d8cd98f00b204e9800998ecf8427e",
          "app": "octopus-deploy",
          "method": "api-key",
          "credentials": {
            "instanceUrl": "https://your-instance.octopus.app",
          }
      }
    }
    ```
  </Tab>
</Tabs>

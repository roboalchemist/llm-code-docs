# Source: https://infisical.com/docs/integrations/secret-syncs/laravel-forge.md

# Source: https://infisical.com/docs/integrations/cloud/laravel-forge.md

# Source: https://infisical.com/docs/integrations/app-connections/laravel-forge.md

# Laravel Forge Connection

> Learn how to configure a Laravel Forge Connection for Infisical.

Infisical supports the use of [API Tokens](https://forge.laravel.com/docs/api#create-a-new-api-token) to connect with Laravel Forge.

## Create Laravel Forge API Token

<Steps>
  <Step title="From your Laravel Forge dashboard, click on your user avatar and go to 'API'">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/laravel-forge/app-connection-profile.png" alt="Laravel Forge User Settings" />
  </Step>

  <Step title="Click 'Create Token'">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/laravel-forge/app-connection-create-api-token.png" alt="Applications Tab" />
  </Step>

  <Step title="Provide Token Information">
    Provide a name for your token and select the following permissions:

    * `user:view`
    * `organization:view`
    * `server:view`
    * `site:manage-environment`

    Then click 'Add token'.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/laravel-forge/api-token-create-form.png" alt="Token Form" />
  </Step>

  <Step title="Copy the token securely">
    Make sure to copy the token now—you won’t be able to access it again.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/laravel-forge/api-token-generated.png" alt="Token Generated" />
  </Step>
</Steps>

## Create a Laravel Forge Connection in Infisical

<Tabs>
  <Tab title="Infisical UI">
    <Steps>
      <Step title="Navigate to App Connections">
        In your Infisical dashboard, navigate to the **App Connections** page in the desired project.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/general/add-connection.png" alt="App Connections Tab" />
      </Step>

      <Step title="Select Laravel Forge Connection">
        Click **+ Add Connection** and choose **Laravel Forge** Connection from the list of integrations.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/laravel-forge/app-connection-option.png" alt="Select Laravel Forge Connection" />
      </Step>

      <Step title="Fill out the Laravel Forge Connection form">
        Complete the form by providing:

        * A descriptive name for the connection
        * An optional description
        * The API Token from the previous step
          <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/laravel-forge/app-connection-form.png" alt="Laravel Forge Connection Modal" />
      </Step>

      <Step title="Connection created">
        After submitting the form, your **Laravel Forge Connection** will be successfully created and ready to use with your Infisical project.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/laravel-forge/app-connection-generated.png" alt="Laravel Forge Connection Created" />
      </Step>
    </Steps>
  </Tab>

  <Tab title="API">
    To create a Laravel Forge Connection via API, send a request to the [Create Laravel Forge Connection](/api-reference/endpoints/app-connections/laravel-forge/create) endpoint.

    ### Sample request

    ```bash Request theme={"dark"}
    curl    --request POST \
            --url https://app.infisical.com/api/v1/app-connections/laravel-forge \
            --header 'Content-Type: application/json' \
            --data '{
                "name": "my-laravel-forge-connection",
                "method": "api-token",
                "projectId": "7ffbb072-2575-495a-b5b0-127f88caef78",
                "credentials": {
                    "apiToken": "[API TOKEN]"
                }
            }'
    ```

    ### Sample response

    ```bash Response theme={"dark"}
    {
      "appConnection": {
          "id": "a1b2c3d4-5678-90ab-cdef-1234567890ab",
          "name": "my-laravel-forge-connection",
          "description": null,
          "projectId": "7ffbb072-2575-495a-b5b0-127f88caef78",
          "version": 1,
          "orgId": "abcdef12-3456-7890-abcd-ef1234567890",
          "createdAt": "2025-10-13T10:15:00.000Z",
          "updatedAt": "2025-10-13T10:15:00.000Z",
          "isPlatformManagedCredentials": false,
          "credentialsHash": "d41d8cd98f00b204e9800998ecf8427e",
          "app": "laravel-forge",
          "method": "api-token",
          "credentials": {}
      }
    }
    ```
  </Tab>
</Tabs>

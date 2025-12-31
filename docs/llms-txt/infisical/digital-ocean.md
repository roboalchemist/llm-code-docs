# Source: https://infisical.com/docs/integrations/app-connections/digital-ocean.md

# DigitalOcean Connection

> Learn how to configure a DigitalOcean Connection for Infisical.

Infisical supports the use of [API Tokens](https://cloud.digitalocean.com/account/api/tokens) to connect with DigitalOcean.

## Create a DigitalOcean API Token

<Steps>
  <Step title="From the bottom left sidebar, select 'API'">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/digital-ocean/app-connection-profile.png" alt="DigitalOcean Dashboard" />
  </Step>

  <Step title="In the API section, click on 'Generate New Token'">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/digital-ocean/app-connection-create-api-key.png" alt="API Section" />
  </Step>

  <Step title="Provide a name and select custom scopes">
    Give your token a descriptive name and ensure custom scopes is selected.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/digital-ocean/app-connection-create-form.png" alt="Token Form" />
  </Step>

  <Step title="Select appropriate scopes and Click 'Generate Token'">
    ```
      read:account
      read:actions
      read:regions
      read:sizes
      read:app/projects
      update:app
    ```

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/digital-ocean/app-connection-create-form-roles.png" alt="Token Form" />
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/digital-ocean/app-connection-create-required-roles.png" alt="Token Form" />
  </Step>

  <Step title="Generate and copy the API token">
    Make sure to copy the token now—you won't be able to see it again.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/digital-ocean/app-connection-key-generated.png" alt="Token Generated" />
  </Step>
</Steps>

## Create a DigitalOcean Connection in Infisical

<Tabs>
  <Tab title="Infisical UI">
    <Steps>
      <Step title="Navigate to App Connections">
        In your Infisical dashboard, navigate to the **App Connections** page in the desired project.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/general/add-connection.png" alt="App Connections Tab" />
      </Step>

      <Step title="Select DigitalOcean Connection">
        Click **+ Add Connection** and choose **DigitalOcean Connection** from the list of integrations.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/digital-ocean/app-connection-option.png" alt="Select DigitalOcean Connection" />
      </Step>

      <Step title="Fill out the DigitalOcean Connection form">
        Complete the form by providing:

        * A descriptive name for the connection
        * An optional description
        * The API Token from the previous step

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/digital-ocean/app-connection-form.png" alt="DigitalOcean Connection Modal" />
      </Step>

      <Step title="Connection created">
        After submitting the form, your **DigitalOcean Connection** will be successfully created and ready to use with your Infisical project.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/digital-ocean/app-connection-generated.png" alt="DigitalOcean Connection Created" />
      </Step>
    </Steps>
  </Tab>

  <Tab title="API">
    To create a DigitalOcean Connection via API, send a request to the [Create DigitalOcean Connection](/api-reference/endpoints/app-connections/digital-ocean/create) endpoint.

    ### Sample request

    ```bash Request theme={"dark"}
    curl    --request POST \
            --url https://app.infisical.com/api/v1/app-connections/digital-ocean \
            --header 'Content-Type: application/json' \
            --data '{
                "name": "my-digitalocean-connection",
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
          "name": "my-digitalocean-connection",
          "projectId": "7ffbb072-2575-495a-b5b0-127f88caef78",
          "description": null,
          "version": 1,
          "orgId": "abcdef12-3456-7890-abcd-ef1234567890",
          "createdAt": "2025-07-19T10:15:00.000Z",
          "updatedAt": "2025-07-19T10:15:00.000Z",
          "isPlatformManagedCredentials": false,
          "credentialsHash": "d41d8cd98f00b204e9800998ecf8427e",
          "app": "digital-ocean",
          "method": "api-token",
          "credentials": {}
      }
    }
    ```
  </Tab>
</Tabs>

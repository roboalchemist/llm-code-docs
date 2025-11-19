# Source: https://infisical.com/docs/integrations/secret-syncs/netlify.md

# Source: https://infisical.com/docs/integrations/cloud/netlify.md

# Source: https://infisical.com/docs/integrations/app-connections/netlify.md

# Netlify Connection

> Learn how to configure a Netlify Connection for Infisical.

Infisical supports the use of [Personal Access Tokens](https://docs.netlify.com/api/get-started/#get-access-tokens) to connect with Netlify.

<Note>
  Netlify requires the token to have **full access** to enable secret management for your sites and services.
</Note>

## Create a Netlify Personal Access Token

<Steps>
  <Step title="From your Netlify dashboard, click on your user avatar and go to 'User settings'">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/netlify/app-connection-profile.png" alt="Netlify User Settings" />
  </Step>

  <Step title="In the left sidebar, click on 'Applications' and scroll to 'Personal Access Tokens'">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/netlify/app-connection-create-api-key.png" alt="Applications Tab" />
  </Step>

  <Step title="Click 'New access token'">
    Provide a name for your token and generate it.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/netlify/app-connection-create-form.png" alt="Token Form" />
  </Step>

  <Step title="Copy the token securely">
    Make sure to copy the token now—you won’t be able to access it again.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/netlify/app-connection-key-generated.png" alt="Token Generated" />
  </Step>
</Steps>

## Create a Netlify Connection in Infisical

<Tabs>
  <Tab title="Infisical UI">
    <Steps>
      <Step title="Navigate to App Connections">
        In your Infisical dashboard, navigate to the **App Connections** page in the desired project.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/general/add-connection.png" alt="App Connections Tab" />
      </Step>

      <Step title="Select Netlify Connection">
        Click **+ Add Connection** and choose **Netlify Connection** from the list of integrations.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/netlify/app-connection-option.png" alt="Select Netlify Connection" />
      </Step>

      <Step title="Fill out the Netlify Connection form">
        Complete the form by providing:

        * A descriptive name for the connection
        * An optional description
        * The API Token from the previous step

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/netlify/app-connection-form.png" alt="Netlify Connection Modal" />
      </Step>

      <Step title="Connection created">
        After submitting the form, your **Netlify Connection** will be successfully created and ready to use with your Infisical project.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/netlify/app-connection-generated.png" alt="Netlify Connection Created" />
      </Step>
    </Steps>
  </Tab>

  <Tab title="API">
    To create a Netlify Connection via API, send a request to the [Create Netlify Connection](/api-reference/endpoints/app-connections/netlify/create) endpoint.

    ### Sample request

    ```bash Request theme={"dark"}
    curl    --request POST \
            --url https://app.infisical.com/api/v1/app-connections/netlify \
            --header 'Content-Type: application/json' \
            --data '{
                "name": "my-netlify-connection",
                "method": "access-token",
                "projectId": "7ffbb072-2575-495a-b5b0-127f88caef78",
                "credentials": {
                    "accessToken": "[ACCESS TOKEN]"
                }
            }'
    ```

    ### Sample response

    ```bash Response theme={"dark"}
    {
      "appConnection": {
          "id": "a1b2c3d4-5678-90ab-cdef-1234567890ab",
          "name": "my-netlify-connection",
          "description": null,
          "projectId": "7ffbb072-2575-495a-b5b0-127f88caef78",
          "version": 1,
          "orgId": "abcdef12-3456-7890-abcd-ef1234567890",
          "createdAt": "2025-07-19T10:15:00.000Z",
          "updatedAt": "2025-07-19T10:15:00.000Z",
          "isPlatformManagedCredentials": false,
          "credentialsHash": "d41d8cd98f00b204e9800998ecf8427e",
          "app": "netlify",
          "method": "access-token",
          "credentials": {}
      }
    }
    ```
  </Tab>
</Tabs>

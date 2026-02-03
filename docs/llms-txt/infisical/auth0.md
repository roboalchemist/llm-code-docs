# Source: https://infisical.com/docs/integrations/app-connections/auth0.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Auth0 Connection

> Learn how to configure an Auth0 Connection for Infisical.

Infisical supports the use of [Client Credentials](https://auth0.com/docs/get-started/authentication-and-authorization-flow/client-credentials-flow) to connect with your Auth0 applications.

## Configure a Machine-to-Machine Application in Auth0

<Steps>
  <Step title="Auth0 Applications Dashboard">
    Navigate to the **Applications** page in Auth0 via the sidebar and click **Create Application**.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/auth0/auth0-dashboard-applications.png" alt="Applications Page" />
  </Step>

  <Step title="Create a Machine-to-Machine Application">
    Give your application a name and select **Machine-to-Machine** for the application type.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/auth0/auth0-select-m2m.png" alt="Create Machine-to-Machine Application" />
  </Step>

  <Step title="Configure Authorization">
    Depending on your connection use case, authorize your application for the applicable API and grant the relevant permissions. Once done, click **Authorize**.

    <Tabs>
      <Tab title="Secret Rotation">
        Select the **Auth0 Management API** option from the dropdown and grant the `update:client_keys` and `read:clients` permission.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/auth0/auth0-secret-rotation-api-selection.png" alt="Secret Rotation Authorization" />
      </Tab>
    </Tabs>
  </Step>

  <Step title="Application Client Credentials">
    On your application page, select the **Settings** tab and copy the **Domain**, **Client ID** and **Client Secret** for later.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/auth0/auth0-client-credentials.png" alt="Client Credentials" />
  </Step>

  <Step title="Application Audience">
    Next, select the **APIs** tab and copy the **API Identifier**.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/auth0/auth0-audience.png" alt="Application Audience" />
  </Step>
</Steps>

## Setup Auth0 Connection in Infisical

<Tabs>
  <Tab title="Infisical UI">
    1. Navigate to the **Integrations** tab in the desired project, then select **App Connections**.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/general/add-connection.png" alt="App Connections Tab" />

    2. Select the **Auth0 Connection** option.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/auth0/select-auth0-connection.png" alt="Select Auth0 Connection" />

    3. Select the **Client Credentials** method option and provide the details obtained from the previous section and press **Connect to Auth0**.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/auth0/client-credentials-create.png" alt="Create Auth0 Connection" />

    4. Your **Auth0 Connection** is now available for use.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/auth0/client_credentials_connection.png" alt="Assume Role Auth0 Connection" />
  </Tab>

  <Tab title="API">
    To create a Auth0 Connection, make an API request to the [Create Auth0
    Connection](/api-reference/endpoints/app-connections/auth0/create) API endpoint.

    ### Sample request

    ```bash Request theme={"dark"}
    curl    --request POST \
    --url https://app.infisical.com/api/v1/app-connections/auth0 \
    --header 'Content-Type: application/json' \
    --data '{
        "name": "my-auth0-connection",
        "method": "client-credentials",
        "projectId": "7ffbb072-2575-495a-b5b0-127f88caef78",
        "credentials": {
            "domain": "xxx-xxxxxxxxx.us.auth0.com",
            "clientId": "...",
            "clientSecret": "...",
            "audience": "https://xxx-xxxxxxxxx.us.auth0.com/api/v2/"
        }
    }'
    ```

    ### Sample response

    ```bash Response theme={"dark"}
    {
        "appConnection": {
            "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
            "name": "my-auth0-connection",
            "projectId": "7ffbb072-2575-495a-b5b0-127f88caef78",
            "version": 1,
            "orgId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z",
            "app": "auth0",
            "method": "client-credentials",
            "credentials": {
                "domain": "xxx-xxxxxxxxx.us.auth0.com",
                "clientId": "...",
                "audience": "https://xxx-xxxxxxxxx.us.auth0.com/api/v2/"
            }
        }
    }
    ```
  </Tab>
</Tabs>

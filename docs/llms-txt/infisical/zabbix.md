# Source: https://infisical.com/docs/integrations/secret-syncs/zabbix.md

# Source: https://infisical.com/docs/integrations/app-connections/zabbix.md

# Source: https://infisical.com/docs/integrations/secret-syncs/zabbix.md

# Source: https://infisical.com/docs/integrations/app-connections/zabbix.md

# Zabbix Connection

> Learn how to configure a Zabbix Connection for Infisical.

Infisical supports the use of [API Tokens](https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/users/api_tokens) to connect with Zabbix.

## Create Zabbix API Token

<Steps>
  <Step title="Navigate to 'API Tokens'">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/zabbix/zabbix-dashboard.png" alt="Dashboard Page" />
  </Step>

  <Step title="Click 'Create API Token'">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/zabbix/zabbix-api-token-list.png" alt="Click Create Token" />
  </Step>

  <Step title="Provide Token Information">
    Ensure that you give this token access to the correct app, then click 'Create Token'.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/zabbix/zabbix-api-token-form.png" alt="Create Token Page" />
  </Step>

  <Step title="Save Token">
    After clicking 'Create Token', a modal containing your access token will appear. Save this token for later steps.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/zabbix/zabbix-api-token-generated.png" alt="Copy Token Modal" />
  </Step>
</Steps>

## Create Zabbix Connection in Infisical

<Tabs>
  <Tab title="Infisical UI">
    <Steps>
      <Step title="Navigate to App Connections">
        In your Infisical dashboard, navigate to the **App Connections** page in the desired project.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/general/add-connection.png" alt="App Connections Tab" />
      </Step>

      <Step title="Select Zabbix Connection">
        Click the **+ Add Connection** button and select the **Zabbix Connection** option from the available integrations.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/zabbix/zabbix-app-connection-option.png" alt="Select Zabbix Connection" />
      </Step>

      <Step title="Fill out the Zabbix Connection Modal">
        Complete the Zabbix Connection form by entering:

        * A descriptive name for the connection
        * An optional description for future reference
        * The Zabbix URL for your instance
        * The API Token from earlier steps

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/zabbix/zabbix-app-connection-form.png" alt="Zabbix Connection Modal" />
      </Step>

      <Step title="Connection Created">
        After clicking Create, your **Zabbix Connection** is established and ready to use with your Infisical project.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/zabbix/zabbix-app-connection-generated.png" alt="Zabbix Connection Created" />
      </Step>
    </Steps>
  </Tab>

  <Tab title="API">
    To create a Zabbix Connection, make an API request to the [Create Zabbix Connection](/api-reference/endpoints/app-connections/zabbix/create) API endpoint.

    ### Sample request

    ```bash Request theme={"dark"}
    curl    --request POST \
            --url https://app.infisical.com/api/v1/app-connections/zabbix \
            --header 'Content-Type: application/json' \
            --data '{
                "name": "my-zabbix-connection",
                "method": "api-token",
                "projectId": "7ffbb072-2575-495a-b5b0-127f88caef78",
                "credentials": {
                    "apiToken": "[API TOKEN]",
                    "instanceUrl": "https://zabbix.example.com"
                }
            }'
    ```

    ### Sample response

    ```bash Response theme={"dark"}
    {
      "appConnection": {
          "id": "e5d18aca-86f7-4026-a95e-efb8aeb0d8e6",
          "name": "my-zabbix-connection",
          "projectId": "7ffbb072-2575-495a-b5b0-127f88caef78",
          "description": null,
          "version": 1,
          "orgId": "6f03caa1-a5de-43ce-b127-95a145d3464c",
          "createdAt": "2025-04-23T19:46:34.831Z",
          "updatedAt": "2025-04-23T19:46:34.831Z",
          "isPlatformManagedCredentials": false,
          "credentialsHash": "7c2d371dec195f82a6a0d5b41c970a229cfcaf88e894a5b6395e2dbd0280661f",
          "app": "zabbix",
          "method": "api-token",
          "credentials": {
            "instanceUrl": "https://zabbix.example.com"
          }
      }
    }
    ```
  </Tab>
</Tabs>

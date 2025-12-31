# Source: https://infisical.com/docs/integrations/secret-syncs/teamcity.md

# Source: https://infisical.com/docs/integrations/app-connections/teamcity.md

# Source: https://infisical.com/docs/integrations/secret-syncs/teamcity.md

# Source: https://infisical.com/docs/integrations/app-connections/teamcity.md

# Source: https://infisical.com/docs/integrations/secret-syncs/teamcity.md

# Source: https://infisical.com/docs/integrations/cloud/teamcity.md

# Source: https://infisical.com/docs/integrations/app-connections/teamcity.md

# Source: https://infisical.com/docs/integrations/secret-syncs/teamcity.md

# Source: https://infisical.com/docs/integrations/cloud/teamcity.md

# Source: https://infisical.com/docs/integrations/app-connections/teamcity.md

# TeamCity Connection

> Learn how to configure a TeamCity Connection for Infisical.

Infisical supports connecting to TeamCity using Access Tokens.

## Setup TeamCity Connection in Infisical

<Steps>
  <Step title="Navigate to your profile on TeamCity">
    Navigate to the TeamCity **Profile** page by clicking on your profile icon in the bottom-left corner.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/teamcity/teamcity-main-page.png" alt="TeamCity Main Page" />
  </Step>

  <Step title="Select Access Tokens Tab">
    Select the **Access Tokens** tab from the left sidebar navigation menu.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/teamcity/teamcity-token-page.png" alt="TeamCity Token Page" />
  </Step>

  <Step title="Create the Access Token">
    Click the **Create access token** button and provide a name for your token (e.g., "Infisical Integration"). You may set an expiration date or leave it blank for no expiry.
    The permission scope can either be **Same as current user** or **Limit per project**.

    If you're choosing **Limit per project**, make sure you select the relevant project and enable the permissions relevant to your use case:

    <Tabs>
      <Tab title="Secret Sync Permissions">
        * View build configuration settings
        * Edit project
      </Tab>
    </Tabs>

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/teamcity/teamcity-token-popup.png" alt="TeamCity Token Popup" />

    <Note>
      Setting your permission scope to **Same as current user** will allow your integration to access multiple projects as long as the current user has read and write access to them.
    </Note>

    <Note>
      If you configure an expiry date for your access token, you must manually rotate to a new token before the expiration date to prevent service interruption.
    </Note>
  </Step>

  <Step title="Copy the Access Token">
    After creation, a modal with the Access Token will be displayed. Copy this token immediately and store it securely, as you won't be able to view it again after closing this dialog.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/teamcity/teamcity-token-copy.png" alt="TeamCity Token Copy Popup" />
  </Step>

  <Step title="Token Created">
    You should now see your newly created token in the list of access tokens.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/teamcity/teamcity-token-created.png" alt="TeamCity Token Created" />
  </Step>

  <Step title="Setup TeamCity Connection in Infisical">
    <Tabs>
      <Tab title="Infisical UI">
        1. Navigate to App Connections

           In your Infisical dashboard, navigate to the **App Connections** page in the desired project.
           <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/general/add-connection.png" alt="App Connections Tab" />
        2. Add Connection

           Click the **+ Add Connection** button and select the **TeamCity Connection** option from the available integrations.
           <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/teamcity/teamcity-app-connection-option.png" alt="Select TeamCity Connection" />
        3. Fill the TeamCity Connection Modal

           Complete the TeamCity Connection form by entering:

           * A descriptive name for the connection
           * The Access Token you generated in steps 3-4
           * The URL of your TeamCity instance
           * An optional description for future reference

           <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/teamcity/teamcity-app-connection-modal.png" alt="TeamCity Connection Modal" />
        4. Connection Created

           After clicking Create, your **TeamCity Connection** is established and ready to use with your Infisical project.
           <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/teamcity/teamcity-app-connection-created.png" alt="TeamCity Connection Created" />
      </Tab>

      <Tab title="API">
        To create a TeamCity Connection, make an API request to the [Create TeamCity
        Connection](/api-reference/endpoints/app-connections/teamcity/create) API endpoint.

        ### Sample request

        ```bash Request theme={"dark"}
        curl    --request POST \
                --url https://app.infisical.com/api/v1/app-connections/teamcity \
                --header 'Content-Type: application/json' \
                --data '{
                    "name": "my-teamcity-connection",
                    "method": "access-token",
                    "projectId": "7ffbb072-2575-495a-b5b0-127f88caef78",
                    "credentials": {
                        "accessToken": "...",
                        "instanceUrl": "https://yourcompany.teamcity.com"
                    }
                }'
        ```

        ### Sample response

        ```bash Response theme={"dark"}
        {
          "appConnection": {
            "id": "e5d18aca-86f7-4026-a95e-efb8aeb0d8e6",
            "name": "my-teamcity-connection",
            "projectId": "7ffbb072-2575-495a-b5b0-127f88caef78",
            "description": null,
            "version": 1,
            "orgId": "6f03caa1-a5de-43ce-b127-95a145d3464c",
            "createdAt": "2025-04-23T19:46:34.831Z",
            "updatedAt": "2025-04-23T19:46:34.831Z",
            "isPlatformManagedCredentials": false,
            "credentialsHash": "7c2d371dec195f82a6a0d5b41c970a229cfcaf88e894a5b6395e2dbd0280661f",
            "app": "teamcity",
            "method": "access-token",
            "credentials": {
              "instanceUrl": "https://yourcompany.teamcity.com"
            }
          }
        }
        ```
      </Tab>
    </Tabs>
  </Step>
</Steps>

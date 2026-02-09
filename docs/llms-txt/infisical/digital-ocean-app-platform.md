# Source: https://infisical.com/docs/integrations/secret-syncs/digital-ocean-app-platform.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# DigitalOcean App Platform Sync

> Learn how to configure a DigitalOcean App Platform Sync for Infisical.

**Prerequisites:**

* Create a [DigitalOcean Connection](/integrations/app-connections/digital-ocean)

<Tabs>
  <Tab title="Infisical UI">
    <Steps>
      <Step title="Add Sync">
        Navigate to **Project** > **Integrations** and select the **Secret Syncs** tab. Click on the **Add Sync** button.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-syncs/general/secret-sync-tab.png" alt="Secret Syncs Tab" />
      </Step>

      <Step title="Select 'DigitalOcean App Platform'">
                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-syncs/digital-ocean-app-platform/select-option.png" alt="Select DigitalOcean" />
      </Step>

      <Step title="Configure source">
        Configure the **Source** from where secrets should be retrieved, then click **Next**.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-syncs/digital-ocean-app-platform/sync-source.png" alt="Configure Source" />

        * **Environment**: The project environment to retrieve secrets from.
        * **Secret Path**: The folder path to retrieve secrets from.

        <Tip>
          If you need to sync secrets from multiple folder locations, check out [secret imports](/documentation/platform/secret-reference#secret-imports).
        </Tip>
      </Step>

      <Step title="Configure destination">
        Configure the **Destination** to where secrets should be deployed, then click **Next**.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-syncs/digital-ocean-app-platform/sync-destination.png" alt="Configure Destination" />

        * **DigitalOcean Connection**: The DigitalOcean Connection to authenticate with.
        * **App**: The App Platform app to sync secrets to.
      </Step>

      <Step title="Configure Sync Options">
        Configure the **Sync Options** to specify how secrets should be synced, then click **Next**.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-syncs/digital-ocean-app-platform/sync-options.png" alt="Configure Options" />

        * **Initial Sync Behavior**: Determines how Infisical should resolve the initial sync.
          * **Overwrite Destination Secrets**: Removes any secrets at the destination endpoint not present in Infisical.

        <Note>
          Digital Ocean App Platform does not support importing secrets.
        </Note>

        * **Key Schema**: Template that determines how secret names are transformed when syncing, using `{{secretKey}}` as a placeholder for the original secret name and `{{environment}}` for the environment.

        <Note>
          We highly recommend using a Key Schema to ensure that Infisical only manages the specific keys you intend, keeping everything else untouched.
        </Note>

        * **Auto-Sync Enabled**: If enabled, secrets will automatically be synced from the source location when changes occur. Disable to enforce manual syncing only.
        * **Disable Secret Deletion**: If enabled, Infisical will not remove secrets from the sync destination. Enable this option if you intend to manage some secrets manually outside of Infisical.
      </Step>

      <Step title="Configure details">
        Configure the **Details** of your DigitalOcean Sync, then click **Next**.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-syncs/digital-ocean-app-platform/sync-details.png" alt="Configure Details" />

        * **Name**: The name of your sync. Must be slug-friendly.
        * **Description**: An optional description for your sync.
      </Step>

      <Step title="Review configuration">
        Review your DigitalOcean Sync configuration, then click **Create Sync**.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-syncs/digital-ocean-app-platform/sync-review.png" alt="Review Configuration" />
      </Step>

      <Step title="Sync created">
        If enabled, your DigitalOcean Sync will begin syncing your secrets to the destination endpoint.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-syncs/digital-ocean-app-platform/sync-created.png" alt="Sync Created" />
      </Step>
    </Steps>
  </Tab>

  <Tab title="API">
    To create a **DigitalOcean App Platform Sync**, make an API request to the [Create DigitalOcean Sync](/api-reference/endpoints/secret-syncs/digital-ocean-app-platform/create) API endpoint.

    ### Sample request

    ```bash Request theme={"dark"}
    curl    --request POST \
            --url https://app.infisical.com/api/v1/secret-syncs/digital-ocean-app-platform \
            --header 'Content-Type: application/json' \
            --data '{
                "name": "my-digitalocean-sync",
                "projectId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
                "description": "sync to do app",
                "connectionId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
                "environment": "dev",
                "secretPath": "/app-secrets",
                "isEnabled": true,
                "syncOptions": {
                    "initialSyncBehavior": "overwrite-destination",
                    "autoSyncEnabled": true,
                    "disableSecretDeletion": false
                },
                "destinationConfig": {
                    "appId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
                    "appName": "do-todo-app"
                }
            }'
    ```

    ### Sample response

    ```bash Response theme={"dark"}
    {
        "secretSync": {
            "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
            "name": "my-digitalocean-sync",
            "description": "sync to do app",
            "isEnabled": true,
            "version": 1,
            "folderId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
            "connectionId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
            "createdAt": "2025-07-19T12:00:00Z",
            "updatedAt": "2025-07-19T12:00:00Z",
            "syncStatus": "succeeded",
            "lastSyncJobId": "job-5678",
            "lastSyncMessage": null,
            "lastSyncedAt": "2025-07-19T12:00:00Z",
            "syncOptions": {
                "initialSyncBehavior": "overwrite-destination",
                "autoSyncEnabled": true,
                "disableSecretDeletion": false
            },
            "projectId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
            "connection": {
                "app": "digital-ocean",
                "name": "my-digitalocean-connection",
                "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a"
            },
            "environment": {
                "slug": "dev",
                "name": "Development",
                "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a"
            },
            "folder": {
                "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
                "path": "/app-secrets"
            },
            "destination": "digital-ocean",
            "destinationConfig": {
                "appId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
                "appName": "do-todo-app"
            }
        }
    }
    ```
  </Tab>
</Tabs>

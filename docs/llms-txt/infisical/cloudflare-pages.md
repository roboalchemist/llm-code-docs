# Source: https://infisical.com/docs/integrations/secret-syncs/cloudflare-pages.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Cloudflare Pages Sync

> Learn how to configure a Cloudflare Pages Sync for Infisical.

**Prerequisites:**

* Set up and add secrets to [Infisical Cloud](https://app.infisical.com)
* Create a [Cloudflare Connection](/integrations/app-connections/cloudflare)

<Tabs>
  <Tab title="Infisical UI">
    1. Navigate to **Project** > **Integrations** and select the **Secret Syncs** tab. Click on the **Add Sync** button.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-syncs/general/secret-sync-tab.png" alt="Secret Syncs Tab" />

    2. Select the **Cloudflare Pages** option.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-syncs/cloudflare-pages/select-cloudflare-pages-option.png" alt="Select Cloudflare Pages" />

    3. Configure the **Source** from where secrets should be retrieved, then click **Next**.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-syncs/cloudflare-pages/cloudflare-pages-sync-source.png" alt="Configure Source" />

    * **Environment**: The project environment to retrieve secrets from.
    * **Secret Path**: The folder path to retrieve secrets from.

    <Tip>
      If you need to sync secrets from multiple folder locations, check out [secret imports](/documentation/platform/secret-reference#secret-imports).
    </Tip>

    4. Configure the **Destination** to where secrets should be deployed, then click **Next**.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-syncs/cloudflare-pages/cloudflare-pages-sync-destination.png" alt="Configure Destination" />

    * **Cloudflare Connection**: The Cloudflare Connection to authenticate with.
    * **Cloudflare Pages Project**: Choose the Cloudflare Pages project you want to sync secrets to.
    * **Environment**: Select the deployment environment (preview or production).

    5. Configure the **Sync Options** to specify how secrets should be synced, then click **Next**.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-syncs/cloudflare-pages/cloudflare-pages-sync-options.png" alt="Configure Options" />

    * **Initial Sync Behavior**: Determines how Infisical should resolve the initial sync.
      * **Overwrite Destination Secrets**: Removes any secrets at the destination endpoint not present in Infisical.
    * **Key Schema**: Template that determines how secret names are transformed when syncing, using `{{secretKey}}` as a placeholder for the original secret name and `{{environment}}` for the environment.
    * **Auto-Sync Enabled**: If enabled, secrets will automatically be synced from the source location when changes occur. Disable to enforce manual syncing only.
    * **Disable Secret Deletion**: If enabled, Infisical will not remove secrets from the sync destination. Enable this option if you intend to manage some secrets manually outside of Infisical.

    6. Configure the **Details** of your Cloudflare Pages Sync, then click **Next**.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-syncs/cloudflare-pages/cloudflare-pages-sync-details.png" alt="Configure Details" />

    * **Name**: The name of your sync. Must be slug-friendly.
    * **Description**: An optional description for your sync.

    7. Review your Cloudflare Pages Sync configuration, then click **Create Sync**.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-syncs/cloudflare-pages/cloudflare-pages-sync-review.png" alt="Confirm Configuration" />

    8. If enabled, your Cloudflare Pages Sync will begin syncing your secrets to the destination endpoint.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-syncs/cloudflare-pages/cloudflare-pages-sync-created.png" alt="Sync Secrets" />
  </Tab>

  <Tab title="API">
    To create a **Cloudflare Pages Sync**, make an API request to the [Create Cloudflare Pages Sync](/api-reference/endpoints/secret-syncs/cloudflare-pages/create) API endpoint.

    ### Sample request

    ```bash Request theme={"dark"}
    curl --request POST \
      --url https://app.infisical.com/api/v1/secret-syncs/cloudflare-pages \
      --header 'Content-Type: application/json' \
      --data '{
        "name": "my-cloudflare-pages-sync",
        "projectId": "your-project-id",
        "description": "an example sync",
        "connectionId": "your-cloudflare-connection-id",
        "environment": "production",
        "secretPath": "/my-secrets",
        "isEnabled": true,
        "syncOptions": {
          "initialSyncBehavior": "overwrite-destination"
        },
        "destinationConfig": {
          "projectId": "your-cloudflare-pages-project-id",
          "projectName": "my-pages-project",
          "environment": "production"
        }
      }'
    ```

    ### Sample response

    ```bash Response theme={"dark"}
    {
      "secretSync": {
        "id": "your-sync-id",
        "name": "my-cloudflare-pages-sync",
        "description": "an example sync",
        "isEnabled": true,
        "version": 1,
        "folderId": "your-folder-id",
        "connectionId": "your-cloudflare-connection-id",
        "createdAt": "2024-05-01T12:00:00Z",
        "updatedAt": "2024-05-01T12:00:00Z",
        "syncStatus": "succeeded",
        "lastSyncJobId": "123",
        "lastSyncMessage": null,
        "lastSyncedAt": "2024-05-01T12:00:00Z",
        "syncOptions": {
          "initialSyncBehavior": "overwrite-destination"
        },
        "projectId": "your-project-id",
        "connection": {
          "app": "cloudflare",
          "name": "my-cloudflare-connection",
          "id": "your-cloudflare-connection-id"
        },
        "environment": {
          "slug": "production",
          "name": "Production",
          "id": "your-env-id"
        },
        "folder": {
          "id": "your-folder-id",
          "path": "/my-secrets"
        },
        "destination": "cloudflare-pages",
        "destinationConfig": {
          "projectId": "your-cloudflare-pages-project-id",
          "projectName": "my-pages-project",
          "environment": "production"
        }
      }
    }
    ```
  </Tab>
</Tabs>

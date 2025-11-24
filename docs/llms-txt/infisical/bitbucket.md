# Source: https://infisical.com/docs/integrations/secret-syncs/bitbucket.md

# Source: https://infisical.com/docs/integrations/cicd/bitbucket.md

# Source: https://infisical.com/docs/integrations/app-connections/bitbucket.md

# Source: https://infisical.com/docs/documentation/platform/secret-scanning/bitbucket.md

# Bitbucket Secret Scanning

> Learn how to configure secret scanning for Bitbucket.

## Prerequisites

* Create a [Bitbucket Connection](/integrations/app-connections/bitbucket) with Secret Scanning permissions

## Create a Bitbucket Data Source in Infisical

<Tabs>
  <Tab title="Infisical UI">
    1. Navigate to your Secret Scanning Project's Dashboard and click the **Add Data Source** button.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/secret-scanning/github/github-data-source-step-1.png" alt="Secret Scanning Dashboard" />

    2. Select the **Bitbucket** option.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/secret-scanning/bitbucket/step-2.png" alt="Select Bitbucket" />

    3. Configure which workspace and repositories you would like to scan. Then click **Next**.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/secret-scanning/bitbucket/step-3.png" alt="Data Source Configuration" />

       * **Bitbucket Connection** - the connection that has access to the repositories you want to scan.
       * **Workspace** - the Bitbucket workspace to scan secrets in.
       * **Scan Repositories** - select which repositories you would like to scan.
         * **All Repositories** - Infisical will scan all repositories associated with your connection.
         * **Select Repositories** - Infisical will scan the selected repositories.
       * **Auto-Scan Enabled** - whether Infisical should automatically perform a scan when a push is made to configured repositories.

    4. Give your data source a name and description (optional). Then click **Next**.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/secret-scanning/bitbucket/step-4.png" alt="Data Source Details" />

       * **Name** - the name of the data source. Must be slug-friendly.
       * **Description** (optional) - a description of this data source.

    5. Review your data source, then click **Create Data Source**.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/secret-scanning/bitbucket/step-5.png" alt="Data Source Review" />

    6. Your **Bitbucket Data Source** is now available and will begin a full scan if **Auto-Scan** is enabled.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/secret-scanning/bitbucket/step-6.png" alt="Data Source Created" />

    7. You can view repositories and scan results by clicking on your data source.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/secret-scanning/bitbucket/step-7.png" alt="Data Source Page" />

    8. In addition, you can review any findings from the **Findings Page**.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/secret-scanning/bitbucket/step-8.png" alt="Findings Page" />
  </Tab>

  <Tab title="API">
    To create a Bitbucket Data Source, make an API request to the [Create Bitbucket Data Source](/api-reference/endpoints/secret-scanning/data-sources/bitbucket/create) API endpoint.

    ### Sample request

    ```bash Request theme={"dark"}
    curl --request POST \
    --url https://us.infisical.com/api/v2/secret-scanning/data-sources/bitbucket \
    --header 'Content-Type: application/json' \
    --data '{
        "name": "my-bitbucket-source",
        "projectId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
        "description": "my bitbucket data source",
        "connectionId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
        "isAutoScanEnabled": true,
        "config": {
            "workspaceSlug": "my-workspace",
            "includeRepos": ["*"]
        }
    }'
    ```

    ### Sample response

    ```bash Response theme={"dark"}
    {
        "dataSource": {
            "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
            "externalId": "1234567890",
            "name": "my-bitbucket-source",
            "description": "my bitbucket data source",
            "isAutoScanEnabled": true,
            "projectId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z",
            "type": "bitbucket",
            "connectionId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
            "connection": {
                "app": "bitbucket",
                "name": "my-bitbucket-app",
                "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a"
            },
            "config": {
                "workspaceSlug": "my-workspace",
                "includeRepos": ["*"]
            }
        }
    }
    ```
  </Tab>
</Tabs>

# Source: https://infisical.com/docs/documentation/platform/secret-rotation/okta-client-secret.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Okta Client Secret

> Learn how to automatically rotate Okta Client Secrets.

## Prerequisites

* Create an [Okta Connection](/integrations/app-connections/okta).

## Create an Okta Client Secret Rotation in Infisical

<Tabs>
  <Tab title="Infisical UI">
    1. Navigate to your Secret Manager Project's Dashboard and select **Add Secret Rotation** from the actions dropdown.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-rotations-v2/generic/add-secret-rotation.png" alt="Secret Manager Dashboard" />

    2. Select the **Okta Client Secret** option.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-rotations-v2/okta-client-secret/select-okta.png" alt="Select Okta Client Secret" />

    3. Configure the rotation behavior, then click **Next**.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-rotations-v2/okta-client-secret/configuration.png" alt="Rotation Configuration" />

    * **Okta Connection** - the connection that will perform the rotation of the specified application's Client Secret.
    * **Rotation Interval** - the interval, in days, that once elapsed will trigger a rotation.
    * **Rotate At** - the local time of day when rotation should occur once the interval has elapsed.
    * **Auto-Rotation Enabled** - whether secrets should automatically be rotated once the rotation interval has elapsed. Disable this option to manually rotate secrets or pause secret rotation.

    4. Select the Okta application whose Client Secret you want to rotate. Then click **Next**.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-rotations-v2/okta-client-secret/parameters.png" alt="Rotation Parameters" />

    5. Specify the secret names that the client credentials should be mapped to. Then click **Next**.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-rotations-v2/okta-client-secret/mappings.png" alt="Rotation Secrets Mapping" />

    * **Client ID** - the name of the secret that the application Client ID will be mapped to.
    * **Client Secret** - the name of the secret that the rotated Client Secret will be mapped to.

    6. Give your rotation a name and description (optional). Then click **Next**.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-rotations-v2/okta-client-secret/details.png" alt="Rotation Details" />

    * **Name** - the name of the secret rotation configuration. Must be slug-friendly.
    * **Description** (optional) - a description of this rotation configuration.

    7. Review your configuration, then click **Create Secret Rotation**.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-rotations-v2/okta-client-secret/review.png" alt="Rotation Review" />

    8. Your **Okta Client Secret** credentials are now available for use via the mapped secrets.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-rotations-v2/okta-client-secret/created.png" alt="Rotation Created" />
  </Tab>

  <Tab title="API">
    To create an Okta Client Secret Rotation, make an API request to the [Create Okta Client Secret Rotation](/api-reference/endpoints/secret-rotations/okta-client-secret/create) API endpoint.

    You will first need the **Client ID** of the Okta application you want to rotate the secret for. This can be obtained from the applications dashboard.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-rotations-v2/okta-client-secret/client-id.png" alt="Okta Client ID" />

    ### Sample request

    ```bash Request theme={"dark"}
    curl --request POST \
    --url https://us.infisical.com/api/v2/secret-rotations/okta-client-secret \
    --header 'Content-Type: application/json' \
    --data '{
        "name": "my-okta-rotation",
        "projectId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
        "description": "my client secret rotation",
        "connectionId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
        "environment": "dev",
        "secretPath": "/",
        "isAutoRotationEnabled": true,
        "rotationInterval": 30,
        "rotateAtUtc": {
            "hours": 0,
            "minutes": 0
        },
        "parameters": {
            "clientId": "...",
        },
        "secretsMapping": {
            "clientId": "OKTA_CLIENT_ID",
            "clientSecret": "OKTA_CLIENT_SECRET"
        }
    }'
    ```

    ### Sample response

    ```bash Response theme={"dark"}
    {
        "secretRotation": {
            "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
            "name": "my-okta-rotation",
            "description": "my client secret rotation",
            "secretsMapping": {
                "clientId": "OKTA_CLIENT_ID",
                "clientSecret": "OKTA_CLIENT_SECRET"
            },
            "isAutoRotationEnabled": true,
            "activeIndex": 0,
            "folderId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
            "connectionId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z",
            "rotationInterval": 30,
            "rotationStatus": "success",
            "lastRotationAttemptedAt": "2023-11-07T05:31:56Z",
            "lastRotatedAt": "2023-11-07T05:31:56Z",
            "lastRotationJobId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
            "nextRotationAt": "2023-11-07T05:31:56Z",
            "connection": {
                "app": "okta",
                "name": "my-okta-connection",
                "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a"
            },
            "environment": {
                "slug": "dev",
                "name": "Development",
                "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a"
            },
            "projectId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
            "folder": {
                "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
                "path": "/"
            },
            "rotateAtUtc": {
                "hours": 0,
                "minutes": 0
            },
            "lastRotationMessage": null,
            "type": "okta-client-secret",
            "parameters": {
                "clientId": "..."
            }
        }
    }
    ```
  </Tab>
</Tabs>

# Source: https://docs.snyk.io/scan-with-snyk/snyk-iac/getting-started-with-cloud-scans/manage-cloud-environments/find-an-environment-id.md

# Find an environment ID

Certain actions, such as updating or deleting an environment using the Snyk API, require the environment ID.

To find the ID of an environment, you can use the following methods:

* [Web UI](#web-ui)
* [API](#api)

## Web UI

To find an environment ID using the [Web UI](https://app.snyk.io/):

1. Navigate to your Organization **Settings** > **Cloud environments**.
2. In the **Actions** column, select the three dots for the desired environment.
3. Select **Update**.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-66d2a6e5abe0dc87a3153356338b18d54cae6e05%2Fsnyk-cloud-update-env-ui.png?alt=media" alt="Update an environment from the Cloud environments page in Settings"><figcaption><p>Update an environment from the Cloud environments page in Settings</p></figcaption></figure>
4. In the **Environment ID** section, select **Copy** to copy the environment ID.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-da9cddf67d3b8cc3a87df0d7b3799668ac18c492%2Fsnyk-cloud-copy-env-id-ui.png?alt=media" alt="Copy the Environment ID"><figcaption><p>Copy the Environment ID</p></figcaption></figure>

## API

To find an environment ID using the API, send a request to the [`/cloud/environments`](https://apidocs.snyk.io/#get-/orgs/-org_id-/cloud/environments) endpoint in the following format:

```
curl -X GET \
  'https://api.snyk.io/rest/orgs/YOUR-ORGANIZATION-ID/cloud/environments?version=2022-12-21~beta' \
  -H 'Authorization: token YOUR-API-TOKEN'
```

In the output, look for the `data.id` property of the desired environment. In the shortened example that follows, the ID is `3b7ccff9-8900-4e54-0000-1234abcd1234`:

```
{
  "jsonapi": {
    "version": "1.0"
  },
  "data": {
    "id": "3b7ccff9-8900-4e54-0000-1234abcd1234",
    <trimmed for length>
  }
}
```

## Filtering environments

You can filter the list of environments using query parameters to make it easier to find a particular environment. For example, you can add `kind=google` to the API request to return only Google Cloud environments:

```
curl -X GET \
  'https://api.snyk.io/rest/orgs/YOUR-ORGANIZATION-ID/cloud/environments?kind=google&version=2022-12-21~beta' \
  -H 'Authorization: token YOUR-API-TOKEN'
```

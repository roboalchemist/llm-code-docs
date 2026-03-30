# Source: https://help.aikido.dev/aikido-autofix/connect-private-packages/poetry-private-packages.md

# Poetry - Private Packages

For Aikido to update dependencies that include private packages, it needs access to your private registries so it can generate accurate lockfile updates. For Poetry, you can provide a **Google Artifact Registry** configuration service key or provide **environment variables** in Aikido.

## Adding credentials with environment variables <a href="#adding-credentials-with-environment-variables" id="adding-credentials-with-environment-variables"></a>

When the credentials to connect to the private registry are static, you can provide them in environment variables. The environment variables should be created in the following format:

* `POETRY_HTTP_BASIC_[SOURCE_NAME]_USERNAME`
* `POETRY_HTTP_BASIC_[SOURCE_NAME]_PASSWORD`

Where the `[SOURCE_NAME]` is the name of the data source which you specified in your `pyproject.toml` file in uppercase. For example, set `POETRY_HTTP_BASIC_ARTIFACT_USERNAME` and `POETRY_HTTP_BASIC_ARTIFACT_PASSWORD` for the following project file:

```
[[tool.poetry.source]]
name = "artifact"
url = "https://repo-1234567890.d.codeartifact.eu-west-1.amazonaws.com/pypi/poetry/simple/"
```

You can configure the Poetry environment variables in Aikido by following the steps below:

1. Go to your account's settings page for AutoFix in Aikido, [here](https://app.aikido.dev/settings/integrations/autofix).
2. Click on "Connect Registry", the configuration modal will now be shown

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F9HOWiE03u297Gb1yCqFp%2Fimage.png?alt=media&#x26;token=0d4ac332-edcd-433d-b95a-3637d65fa0b2" alt=""><figcaption></figcaption></figure>

3. Select Poetry and  you can now add the `POETRY_HTTP_BASIC_[SOURCE_NAME]_USERNAME` and `POETRY_HTTP_BASIC_[SOURCE_NAME]_PASSWORD` environment variables:

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F6cJqsuxZ0zoCHTAuC2c4%2Fimage.png?alt=media&#x26;token=a1bdac57-bfeb-4ef4-b68a-6d81987bca23" alt=""><figcaption></figcaption></figure>

4. Click Connect Registry to save the environment variables.

If you are using AWS CodeArtifact in combination with Poetry, the password needs to be generated on-the-fly, see this [page](https://help.aikido.dev/aikido-autofix/connect-private-packages/aws-codeartifact-private-packages) on how to configure Poetry with AWS CodeArtifact.

When creating a PR via Autofix, Aikido will include these environment variables when running Poetry commands.

## Adding credentials for GCP Artifact Registry <a href="#adding-credentials-for-gcp-artifact-registry" id="adding-credentials-for-gcp-artifact-registry"></a>

For GCP Artifact registry, credentials can not be generated statically. In this case you can follow the steps below.

### 1. Create a Service Account in GCP <a href="#id-1-create-a-service-account" id="id-1-create-a-service-account"></a>

First, create a service account in your Google Cloud project:

1. Go to the Google Cloud Console.
2. Navigate to **IAM & Admin** > **Service Accounts**.
3. Click **Create Service Account**.
4. Fill in a **Service account name** such as `Aikido Artifact Registry Reader` and click **Create And Continue**.
5. Grant the service account with the **Artifact Registry Reader** role.

   ![Assigning the "Artifact Registry Reader" role to a service account in a Google Cloud project.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-470613549ee0a8658f15c041e95ba41c95f1daa0%2Fpoetry-private-packages_8d6db05a-1848-4c9e-8d0a-5bd824229aa9.jpg?alt=media)
6. Click **Continue** and **Done**.

### 2. Create a Key for the Service Account in GCP <a href="#id-2-create-a-key-for-the-service-account" id="id-2-create-a-key-for-the-service-account"></a>

1. On the **Service Accounts** page, find the service account you just created.
2. Click on the three dots on the right and select **Manage Keys**.
3. Click **Add Key** > **Create New Key**.
4. Choose **JSON** and click **Create**.
5. Save the JSON key file to a secure location.

### 3. Configuration in Aikido <a href="#id-3-configuration-in-aikido" id="id-3-configuration-in-aikido"></a>

Once the prerequisites are fulfilled, you can configure aikido to authenticate with your private registry when updating the dependencies by following the steps below:

1. Go to your account's settings page for the autofixer in Aikido, [here](https://app.aikido.dev/issues/fix/settings).
2. Click on "Connect Registry", the configuration modal will now be shown

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FkCcrE2CuwQc9tv6Dp5ZM%2Fimage.png?alt=media&#x26;token=23bda00c-f2d3-43f0-9041-5c9c8d21bcb5" alt=""><figcaption></figcaption></figure>

3. Select Poetry and find the `GCP service account key` section at the bottom of the modal:

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FdvCxiLp89f4OdVN9b8cL%2Fimage.png?alt=media&#x26;token=694875c4-0b54-45bf-99a6-2c5d6236fe10" alt=""><figcaption></figcaption></figure>

4. Paste your saved **JSON Key** content in the **Private registry service account key** field
5. Click **Connect Registry** to save the configuration.

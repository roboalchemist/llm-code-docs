# Source: https://docs.anyscale.com/reference/quickstart-sdk.md

# Get started with the Anyscale SDK

[View Markdown](/reference/quickstart-sdk.md)

# Get started with the Anyscale SDK

This page provides an introduction to working with the Anyscale Python SDK. See [Anyscale Python SDK overview](/reference.md#sdk).

## 1. Install the Python SDK[​](#1-install-the-python-sdk "Direct link to 1. Install the Python SDK")

Anyscale packages the Python SDK with the Anyscale CLI. Use the following command to install the latest version of the Anyscale CLI and SDK:

```
pip install -U anyscale
```

## 2. Authentication[​](#2-authentication "Direct link to 2. Authentication")

The Python SDK uses an API key to authenticate to Anyscale. See [Manage API keys](/auth/api-keys.md).

Run the following Anyscale CLI command to authenticate to your organization:

```
anyscale login
```

API keys issued by `anyscale login` expire after 7 days.

caution

Be sure to keep your API key private and secure to prevent unwanted access to your Anyscale resources.

## 3. Test it out[​](#3-test-it-out "Direct link to 3. Test it out")

To verify that everything is working, try creating a new Project using the SDK.

```
import anyscale

project_id: str = anyscale.project.create(
    name="my-project",
    parent_cloud_id="my-cloud-id",
    description="my-project-description"
)

print(f"Project created successfully: https://console.anyscale.com/projects/{project_id}")
```

If everything is working, you should see the success statement as output.

```
Project created successfully: https://console.anyscale.com/projects/prj_1234
```

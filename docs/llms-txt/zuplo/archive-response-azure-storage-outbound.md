# Source: https://www.zuplo.com/docs/policies/archive-response-azure-storage-outbound.md

# Archive Response to Azure Storage Policy

:::tip{title="Custom Policy Example"}

Zuplo is extensible, so we don't have a built-in policy for Archive Response to Azure Storage, instead we've a template here that shows you how you can use your superpower (code) to achieve your goals. To learn more about custom policies [see the documentation](/policies/custom-code-outbound).

:::

In this example shows how you can archive the body of outgoing responses to
Azure Blob Storage. This can be useful for auditing, logging, or archival
scenarios.

```ts title="modules/my-policy.ts"
import { HttpProblems, ZuploContext, ZuploRequest } from "@zuplo/runtime";

interface PolicyOptions {
  blobContainerPath: string;
  blobCreateSas: string;
}

export default async function (
  response: Response,
  request: ZuploRequest,
  context: ZuploContext,
  options: PolicyOptions,
) {
  // NOTE: policy options should be validated, but to keep the sample short,
  // we are skipping that here.

  // because we will read the body, we need to
  // create a clone of this response first, otherwise
  // there may be two attempts to read the body
  // causing a runtime error
  const clone = response.clone();

  // In this example we assume the body could be text, but you could also
  // response the blob() to handle binary data types like images.
  //
  // This example loads the entire body into memory. This is fine for
  // small payloads, but if you have a large payload you should instead
  // save the body via streaming.
  const body = await clone.text();

  // let's generate a unique blob name based on the date and requestId
  const blobName = `${Date.now()}-${context.requestId}.req.txt`;

  const url = `${options.blobContainerPath}/${blobName}?${options.blobCreateSas}`;

  const result = await fetch(url, {
    method: "PUT",
    body: body,
    headers: {
      "x-ms-blob-type": "BlockBlob",
    },
  });

  if (result.status > 201) {
    const text = await result.text();
    context.log.error("Error saving file to storage", text);
    return HttpProblems.internalServerError(request, context, {
      detail: text,
    });
  }

  // Continue the response
  return response;
}
```

## Configuration

The example below shows how to configure a custom code policy in the 'policies.json' document that utilizes the above example policy code.

```json title="config/policies.json"
{
  "name": "my-archive-response-azure-storage-outbound-policy",
  "policyType": "archive-response-azure-storage-outbound",
  "handler": {
    "export": "default",
    "module": "$import(./modules/YOUR_MODULE)",
    "options": {
      "blobCreateSas": "$env(BLOB_CREATE_SAS)",
      "blobContainerPath": "$env(BLOB_CONTAINER_PATH)"
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `archive-response-azure-storage-outbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `default`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(./modules/YOUR_MODULE)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `blobCreateSas` <code className="text-green-600">&lt;string&gt;</code> - The Azure shared access token with permission to write to the bucket
- `blobContainerPath` <code className="text-green-600">&lt;string&gt;</code> - The path to the Azure blob container

## Using the Policy

## Using the Policy

In order to use this policy, you'll need to setup Azure storage. You'll find
instructions on how to do that below.

### Setup Azure

First, let's set up Azure. You'll need a container in Azure storage
([docs](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal)).
Once you have your container you'll need the URL - you can get it on the
`properties` tab of your container as shown below.

![Azure](../../public/media/guides/archiving-requests-to-storage/Untitled.png)

This URL will be the `blobPath` in our policy options.

Next, we'll need a SAS (Shared Access Secret) to authenticate with Azure. You
can generate one of these on the `Shared access tokens` tab.

Note, you should minimize the permissions - and select only the `Create`
permission. Choose a sensible start and expiration time for your token. Note, we
don't recommend restricting IP addresses because Zuplo runs at the edge in over
200 data-centers world-wide.

![Create permission](../../public/media/guides/archiving-requests-to-storage/Untitled_1.png)

Then generate your SAS token - copy the token (not the URL) to the clipboard and
enter it into a new environment variable in your API called `BLOB_CREATE_SAS`.
You'll need another environment variable called `BLOB_CONTAINER_PATH`.

![SAS token](../../public/media/guides/archiving-requests-to-storage/Untitled_2.png)

Read more about [how policies work](/articles/policies)

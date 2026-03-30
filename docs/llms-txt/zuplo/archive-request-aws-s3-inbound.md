# Source: https://www.zuplo.com/docs/policies/archive-request-aws-s3-inbound.md

# Archive Request to AWS S3 Policy

:::tip{title="Custom Policy Example"}

Zuplo is extensible, so we don't have a built-in policy for Archive Request to AWS S3, instead we've a template here that shows you how you can use your superpower (code) to achieve your goals. To learn more about custom policies [see the documentation](/policies/custom-code-inbound).

:::

In this example shows how you can archive the body of incoming requests to AWS
S3 Storage. This can be useful for auditing, logging, or archival scenarios.
Additionally, you could use this policy to save the body of a request and then
enqueue some asynchronous work that uses this body.

```ts title="modules/my-policy.ts"
import { PutObjectCommand, S3Client } from "@aws-sdk/client-s3";
import { ZuploContext, ZuploRequest } from "@zuplo/runtime";

type PolicyOptions = {
  region: string;
  bucketName: string;
  path: string;
  accessKeyId: string;
  accessKeySecret: string;
};
export default async function (
  request: ZuploRequest,
  context: ZuploContext,
  options: PolicyOptions,
  policyName: string,
) {
  // NOTE: policy options should be validated, but to keep the sample short,
  // we are skipping that here.

  // Initialize the S3 client
  const s3Client = new S3Client({
    region: options.region,
    credentials: {
      accessKeyId: options.accessKeyId,
      secretAccessKey: options.accessKeySecret,
    },
  });

  // Create the file
  const file = `${options.path}/${Date.now()}-${crypto.randomUUID()}.req.txt`;

  // because we will read the body, we need to
  // create a clone of this request first, otherwise
  // there may be two attempts to read the body
  // causing a runtime error
  const clone = request.clone();

  // In this example we assume the body could be text, but you could also
  // request the blob() to handle binary data types like images.
  //
  // This example loads the entire body into memory. This is fine for
  // small payloads, but if you have a large payload you should instead
  // save the body via streaming.
  const body = await clone.text();

  // Create the S3 command
  const command = new PutObjectCommand({
    Bucket: options.bucketName,
    Key: file,
    Body: body,
  });

  // Use the S3 client to save the object
  await s3Client.send(command);

  // Continue the request
  return request;
}
```

## Configuration

The example below shows how to configure a custom code policy in the 'policies.json' document that utilizes the above example policy code.

```json title="config/policies.json"
{
  "name": "my-archive-request-aws-s3-inbound-policy",
  "policyType": "archive-request-aws-s3-inbound",
  "handler": {
    "export": "ArchiveResponseOutbound",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "region": "us-east-1",
      "bucketName": "test-bucket-123.s3.amazonaws.com",
      "path": "responses/",
      "accessKeyId": "$env(AWS_ACCESS_KEY_ID)",
      "accessKeySecret": "$env(AWS_ACCESS_KEY_SECRET)"
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `archive-request-aws-s3-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `default`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(./modules/YOUR_MODULE)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `region` <code className="text-green-600">&lt;string&gt;</code> - The AWS region where the bucket is located
- `bucketName` <code className="text-green-600">&lt;string&gt;</code> - The name of the storage bucket
- `path` <code className="text-green-600">&lt;string&gt;</code> - The path where requests are stored
- `accessKeyId` <code className="text-green-600">&lt;string&gt;</code> - The Access Key ID of the account authorized to write to the bucket
- `accessKeySecret` <code className="text-green-600">&lt;string&gt;</code> - The Access Key Secret of the account authorized to write to the bucket

## Using the Policy

Read more about [how policies work](/articles/policies)

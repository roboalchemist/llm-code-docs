# Source: https://docs.envzero.com/guides/integrations/notifications/webhooks.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Webhooks Notifications

> Set up webhook notifications in env zero to send deployment event data to your server or services

Webhooks allow our system to instantly notify your server whenever a specific event occurs, providing a secure and flexible way to create custom integrations with your env zero account. For example, you can use webhooks to send notifications to your preferred collaboration platform, update JIRA tickets, or log events in real-time.

# Setup a webhook

##### Name

The name of the webhook notification target must be unique across the organization.

##### URL

The URL to which an HTTP request will be sent with data about the event. An HTTPS connection is required. You can easily experiment with webhooks without the need to set up a server by using services such as [webhook.site](https://webhook.site).

##### Type

Must be set to Webhook

#### Secret

An optional field. When set, a hash signature is added to the request to validate that it was sent by env zero. More details can be found in the 'Validating webhook deliveries' section below.

When using a secret, you should choose a random string with high entropy and store it in a secure location that you can later access to validate the request.

<Image src="/images/guides/integrations/notifications/6de3adf-screenshot_2024-05-15_at_19.png" />

# Request structure

## Headers

| Header                            | description                                                                                                         |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------ |
| User-Agent                        | Equals to `env-zero-webhook`                                                                                        |
| x-env-zero-notification-target-id | The ID of the notification target to which the request was sent.                                                    |
| x-env-zero-event                  | The event type, e.g., `com.env-zero.deploy.succeeded`                                                               |
| x-env-zero-event-id               | A globally unique ID that identifies the request                                                                    |
| x-env-zero-signature              | If a secret is set, contains the hash signature. More details in the 'Validating webhook deliveries' section below. |

## Body

| Param           | description                                                                                                                                                       |
| :-------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type            | The event type, e.g., `com.env-zero.deploy.succeeded`                                                                                                             |
| source          | Should be equal to `env-zero-webhooks`                                                                                                                            |
| id              | A globally unique ID that identifies the request                                                                                                                  |
| datacontenttype | Equals to `application/json`                                                                                                                                      |
| data            | Event data, JSON encoded. Schema is defined by the event type as specified [in our API reference under the WEBHOOKS section](ref:post_com-env0-budget-exceeded-1) |

## Request example

### Headers

| Header                        | value                                                            |
| :---------------------------- | :--------------------------------------------------------------- |
| User-Agent                    | env0-webhook                                                     |
| x-env0-notification-target-id | 727dbd33-38d3-4057-ab4d-19bc6d40a1d9                             |
| x-env0-event                  | com.env0.webhook.test                                            |
| x-env0-event-id               | e6328df5-81d7-4dd8-851f-66c01f87b5c7                             |
| x-env0-signature              | 0b844da97d713d4965b66b72d0e9dc9fa8990e601acb8d7cdd33b560d41891d7 |

### Body

```json  theme={null}
{
  "type": "com.env0.webhook.test",
  "source": "https://env0.com",
  "id": "b6cf1180-7bbb-4640-9a0b-98e012756b55",
  "time": "2024-05-15T09:22:12.315Z",
  "datacontenttype": "application/json",
  "data": {
    "endpoint": {
      "id": "727dbd33-38d3-4057-ab4d-19bc6d40a1d9",
      "value": "<webhook url>",
      "type": "Webhook",
      "organizationId": "bd12a04a-b051-4f51-9a8a-8a32ac198802"
    }
  }
}
```

# Testing a webhook

You can test your webhook by clicking 'Test endpoint':

<Image src="/images/guides/integrations/notifications/16e0452-screenshot_2024-05-15_at_16.png" />

Then click 'Send test event' to send a test event and examine the request and response (or error details).

## Example Webhook Payload

```json  theme={null}
{
  "type": "com.env0.deploy.succeeded",
  "source": "https://env0.com",
  "id": "2c1a27e4-e3ec-4ad3-bcf8-7caf882a1165",
  "time": "2024-08-02T18:26:27.905Z",
  "datacontenttype": "application/json",
  "data": {
    "environment": {
      "lockStatus": null,
      "nextScheduledDates": null,
      "id": "53c687b3-58f5-4356-8917-c5a30573f83b",
      "createdAt": "2024-07-30T14:32:44.761Z",
      "updatedAt": "2024-08-02T18:26:27.482Z",
      "name": "acme-demo simple-ec2-instance dev",
      "organizationId": "bde19c6d-d0dc-4b11-a951-8f43fe49db92",
      "projectId": "7320dd7a-4822-426c-84b5-62ddd8be0799",
      "userId": "google-oauth2|110563071352660869820",
      "workspaceName": "dev-ec2-0730",
      "requiresApproval": true,
      "status": "ACTIVE",
      "driftStatus": "OK",
      "latestDeploymentLogId": "c8bcfa77-48ea-4550-afa0-644119744dbe",
      "lifespanEndAt": null,
      "markedForAutoDestroy": 0,
      "isArchived": false,
      "continuousDeployment": true,
      "pullRequestPlanDeployments": true,
      "vcsPrCommentsEnabled": true,
      "vcsCommandsAlias": null,
      "autoDeployOnPathChangesOnly": true,
      "autoDeployByCustomGlob": null,
      "terragruntWorkingDirectory": null,
      "isSingleUseBlueprint": true,
      "workflowEnvironmentId": null,
      "isRemoteBackend": true,
      "k8sNamespace": null,
      "isRemoteApplyEnabled": false,
      "latestDeploymentLog": {
        "output": {
          "instances": {
            "sensitive": false,
            "type": [
              "tuple",
              [
                "string"
              ]
            ],
            "value": [
              "i-0152932ae4ca06ef0"
            ]
          },
          "private_ip": {
            "sensitive": false,
            "type": [
              "tuple",
              [
                "string"
              ]
            ],
            "value": [
              "10.0.3.31"
            ]
          },
          "public_ip": {
            "sensitive": false,
            "type": [
              "tuple",
              [
                "string"
              ]
            ],
            "value": [
              "35.89.168.8"
            ]
          }
        },
        "error": null,
        "costEstimation": {
          "totalMonthlyCost": "14.524",
          "projects": [
            {
              "diff": {
                "totalMonthlyCost": "0"
              }
            }
          ]
        },
        "customEnv0EnvironmentVariables": null,
        "plan": {
          "resourceChanges": [],
          "outputChanges": []
        },
        "planSummary": {
          "added": 0,
          "changed": 0,
          "destroyed": 0,
          "imported": 0
        },
        "workflowFile": null,
        "id": "c8bcfa77-48ea-4550-afa0-644119744dbe",
        "createdAt": "2024-08-02T18:25:04.835Z",
        "updatedAt": "2024-08-02T18:26:27.482Z",
        "type": "deploy",
        "startedBy": "google-oauth2|110563071352660869820",
        "queuedAt": "2024-08-02T18:25:04.834Z",
        "startedAt": "2024-08-02T18:25:07.000Z",
        "finishedAt": "2024-08-02T18:26:27.280Z",
        "reviewers": [],
        "status": "SUCCESS",
        "blueprintId": "71cc6df1-5da0-44e8-95e1-43f305855f71",
        "blueprintName": "single-use-template-for-acme-demo simple-ec2-instance dev",
        "blueprintRepository": "https://github.com/env0/acme-demo",
        "blueprintRevision": "main",
        "blueprintPath": "simple-ec2-instance",
        "gitUser": null,
        "targets": null,
        "gitAvatarUrl": null,
        "comment": null,
        "prNumber": null,
        "blueprintType": "terraform",
        "environmentId": "53c687b3-58f5-4356-8917-c5a30573f83b",
        "resourceCount": 4,
        "isSkippedApply": true,
        "workflowDeploymentId": null,
        "workflowDeploymentOptions": null,
        "isScheduledRun": false,
        "abortedBy": null,
        "triggerName": "user",
        "driftDetected": null,
        "stateVersionId": null,
        "deploymentDurationMinutes": 1.30338
      },
      "isLocked": false,
      "user": {
        "email": "andrew.way@env0.com",
        "name": "Andrew Way",
        "created_at": "2021-03-25T19:59:28.357Z",
        "picture": "https://lh3.googleusercontent.com/a/ACg8ocJ1qa3WEUOrrSIQPuVZNHFmdBe7clVtsjQ9dwAGTQI72Ha9WLNE=s96-c",
        "user_id": "google-oauth2|110563071352660869820",
        "family_name": "Way",
        "given_name": "Andrew",
        "last_login": "2024-08-01T22:29:49.203Z",
        "app_metadata": {}
      },
      "url": "https://app.env0.com/p/7320dd7a-4822-426c-84b5-62ddd8be0799/environments/53c687b3-58f5-4356-8917-c5a30573f83b"
    },
    "organization": {
      "mode": "paying",
      "enableOidc": true,
      "createdAt": "2021-05-06T17:05:17.429Z",
      "createdBy": "google-oauth2|110563071352660869820",
      "name": "ACME Financial Services",
      "photoUrl": "https://daks2k3a4ib2z.cloudfront.net/63df9b273f861215467107c8/642395d03a96cecd67802156_env0-icon-256px-p-130x130q80.png",
      "enforcePrCommenterPermissions": true,
      "projectCustomFlowsPolicy": "MERGE_WITH_TEMPLATES",
      "updatedAt": "2024-08-01T18:07:36.224Z",
      "doNotConsiderMergeCommitsForPrPlans": true,
      "defaultTtl": "8-h",
      "description": "env0 helps local and remote teams manage Infrastructure as Code (IaC) deployments in AWS, Azure, and GCP. env0 is the first cloud management platform built around enabling a company’s entire team with self-service while maintaining governance and cost control. We’ve had a number of our early partners using it for the last several months, to help their teams work more independently and relieve workload off their SRE/DevOps team.",
      "id": "bde19c6d-d0dc-4b11-a951-8f43fe49db92",
      "maxTtl": "1-w",
      "doNotReportSkippedStatusChecks": true,
      "role": "Admin",
      "isSelfHostedK8s": false,
      "url": "https://app.env0.com/organizations/bde19c6d-d0dc-4b11-a951-8f43fe49db92"
    },
    "project": {
      "isArchived": false,
      "organizationId": "bde19c6d-d0dc-4b11-a951-8f43fe49db92",
      "updatedAt": "2024-04-10T16:14:29.053Z",
      "hierarchy": "92c172d6-2122-4bca-8e16-9a0a5694e0bb|7320dd7a-4822-426c-84b5-62ddd8be0799",
      "parentProjectId": "92c172d6-2122-4bca-8e16-9a0a5694e0bb",
      "createdAt": "2021-06-04T21:08:14.928Z",
      "description": "Dev Team",
      "id": "7320dd7a-4822-426c-84b5-62ddd8be0799",
      "createdBy": "google-oauth2|110563071352660869820",
      "name": "NonProd - 244172364962",
      "createdByUser": {
        "email": "andrew.way@env0.com",
        "name": "Andrew Way",
        "created_at": "2021-03-25T19:59:28.357Z",
        "picture": "https://lh3.googleusercontent.com/a/ACg8ocJ1qa3WEUOrrSIQPuVZNHFmdBe7clVtsjQ9dwAGTQI72Ha9WLNE=s96-c",
        "user_id": "google-oauth2|110563071352660869820",
        "family_name": "Way",
        "given_name": "Andrew",
        "last_login": "2024-08-01T22:29:49.203Z",
        "app_metadata": {}
      },
      "url": "https://app.env0.com/p/7320dd7a-4822-426c-84b5-62ddd8be0799/environments"
    },
    "deploymentLog": {
      "output": {
        "instances": {
          "sensitive": false,
          "type": [
            "tuple",
            [
              "string"
            ]
          ],
          "value": [
            "i-0152932ae4ca06ef0"
          ]
        },
        "private_ip": {
          "sensitive": false,
          "type": [
            "tuple",
            [
              "string"
            ]
          ],
          "value": [
            "10.0.3.31"
          ]
        },
        "public_ip": {
          "sensitive": false,
          "type": [
            "tuple",
            [
              "string"
            ]
          ],
          "value": [
            "35.89.168.8"
          ]
        }
      },
      "error": null,
      "costEstimation": {
        "totalMonthlyCost": "14.524",
        "projects": [
          {
            "diff": {
              "totalMonthlyCost": "0"
            }
          }
        ]
      },
      "customEnv0EnvironmentVariables": null,
      "plan": {
        "resourceChanges": [],
        "outputChanges": []
      },
      "planSummary": {
        "added": 0,
        "changed": 0,
        "destroyed": 0,
        "imported": 0
      },
      "workflowFile": null,
      "id": "c8bcfa77-48ea-4550-afa0-644119744dbe",
      "createdAt": "2024-08-02T18:25:04.835Z",
      "updatedAt": "2024-08-02T18:26:27.482Z",
      "type": "deploy",
      "startedBy": "google-oauth2|110563071352660869820",
      "queuedAt": "2024-08-02T18:25:04.834Z",
      "startedAt": "2024-08-02T18:25:07.000Z",
      "finishedAt": "2024-08-02T18:26:27.280Z",
      "reviewers": [],
      "status": "SUCCESS",
      "blueprintId": "71cc6df1-5da0-44e8-95e1-43f305855f71",
      "blueprintName": "single-use-template-for-acme-demo simple-ec2-instance dev",
      "blueprintRepository": "https://github.com/env0/acme-demo",
      "blueprintRevision": "main",
      "blueprintPath": "simple-ec2-instance",
      "gitUser": null,
      "targets": null,
      "gitAvatarUrl": null,
      "comment": null,
      "prNumber": null,
      "blueprintType": "terraform",
      "environmentId": "53c687b3-58f5-4356-8917-c5a30573f83b",
      "resourceCount": 4,
      "isSkippedApply": true,
      "workflowDeploymentId": null,
      "workflowDeploymentOptions": null,
      "isScheduledRun": false,
      "abortedBy": null,
      "triggerName": "user",
      "driftDetected": null,
      "stateVersionId": null,
      "deploymentDurationMinutes": 1.30338,
      "reviewersUsers": [],
      "startedByUser": {
        "email": "andrew.way@env0.com",
        "name": "Andrew Way",
        "created_at": "2021-03-25T19:59:28.357Z",
        "picture": "https://lh3.googleusercontent.com/a/ACg8ocJ1qa3WEUOrrSIQPuVZNHFmdBe7clVtsjQ9dwAGTQI72Ha9WLNE=s96-c",
        "user_id": "google-oauth2|110563071352660869820",
        "family_name": "Way",
        "given_name": "Andrew",
        "last_login": "2024-08-01T22:29:49.203Z",
        "app_metadata": {}
      },
      "url": "https://app.env0.com/p/7320dd7a-4822-426c-84b5-62ddd8be0799/environments/53c687b3-58f5-4356-8917-c5a30573f83b/deployments/c8bcfa77-48ea-4550-afa0-644119744dbe"
    },
    "blueprint": {
      "projectId": "ROOT",
      "repository": "https://github.com/env0/acme-demo",
      "fileName": "",
      "path": "simple-ec2-instance",
      "revision": "main",
      "authorId": "google-oauth2|110563071352660869820",
      "createdAt": "2024-07-30T14:32:44.319Z",
      "githubInstallationId": 11551359,
      "isAzureDevOps": false,
      "isBitbucketServer": false,
      "name": "single-use-template-for-acme-demo simple-ec2-instance dev",
      "isSingleUse": true,
      "retry": {},
      "sshKeys": [],
      "isGitLab": false,
      "tokenName": "",
      "organizationId": "bde19c6d-d0dc-4b11-a951-8f43fe49db92",
      "updatedAt": "2024-07-30T14:32:44.319Z",
      "isHelmRepository": false,
      "terraformVersion": "1.5.7",
      "isGitLabEnterprise": false,
      "id": "71cc6df1-5da0-44e8-95e1-43f305855f71",
      "isGitHubEnterprise": false,
      "type": "terraform",
      "projectIds": [],
      "author": {
        "email": "andrew.way@env0.com",
        "name": "Andrew Way",
        "created_at": "2021-03-25T19:59:28.357Z",
        "picture": "https://lh3.googleusercontent.com/a/ACg8ocJ1qa3WEUOrrSIQPuVZNHFmdBe7clVtsjQ9dwAGTQI72Ha9WLNE=s96-c",
        "user_id": "google-oauth2|110563071352660869820",
        "family_name": "Way",
        "given_name": "Andrew",
        "last_login": "2024-08-01T22:29:49.203Z",
        "app_metadata": {}
      },
      "url": "https://app.env0.com/templates/71cc6df1-5da0-44e8-95e1-43f305855f71"
    },
    "gitRevision": "bc7cdada039b75c0da4b3d8194eb3670ffdfc516"
  }
}
```

# Validating webhook deliveries

If a secret is set for the webhook, env zero will use it to create a hash signature that can be used to make sure that the request was sent by env zero. The signature is set in the `x-env0-signature` header.

In your code that handles the requests, you should calculate the hash signature using the secret and the request body. Then, make sure that it equals the signature in the request `x-env0-signature` header.

##### Notes

* The signature is computed based on the webhook secret and the request body using  [HMAC](https://en.wikipedia.org/wiki/HMAC) hex digset.
* When calculating the signature on your side, decode the body as UTF-8.
* To mitigate certain timing attacks, it is highly recommended not to use plain `==` operator when comparing the signature in the request with the one you calculated. Instead, use methods like [secure\_compare](https://www.rubydoc.info/gems/rack/Rack%2FUtils:secure_compare) or [crypto.timingSafeEqual](https://nodejs.org/api/crypto.html#cryptotimingsafeequala-b), which perform a "constant time" string comparison

#### Verify your implementation

You can use the following secret and payload to make sure that your implementation is correct:

secret: `"Secret example"`\
payload: `"Hello, World!"`\
A correct implementation should generate the following signature:\
`0b844da97d713d4965b66b72d0e9dc9fa8990e601acb8d7cdd33b560d41891d7`

## Examples

Here's what signature validation might look like in various programming languages.

<CodeGroup>
  ```typescript TypeScript theme={null}
  import * as crypto from "crypto";

  const WEBHOOK_SECRET: string = process.env.WEBHOOK_SECRET;

  const verify_signature = (req: Request) => {
    const signature = crypto
      .createHmac("sha256", WEBHOOK_SECRET)
      .update(JSON.stringify(req.body))
      .digest("hex");
    let trusted = Buffer.from(`sha256=${signature}`, 'ascii');
    let untrusted =  Buffer.from(req.headers.get("x-hub-signature-256"), 'ascii');
    return crypto.timingSafeEqual(trusted, untrusted);
  };

  const handleWebhook = (req: Request, res: Response) => {
    if (!verify_signature(req)) {
      res.status(401).send("Unauthorized");
      return;
    }
    // The rest of your logic here
  };

  ```

  ```javascript JavaScript theme={null}
  let encoder = new TextEncoder();

  async function verifySignature(secret, header, payload) {
      let parts = header.split("=");
      let sigHex = parts[1];

      let algorithm = { name: "HMAC", hash: { name: 'SHA-256' } };

      let keyBytes = encoder.encode(secret);
      let extractable = false;
      let key = await crypto.subtle.importKey(
          "raw",
          keyBytes,
          algorithm,
          extractable,
          [ "sign", "verify" ],
      );

      let sigBytes = hexToBytes(sigHex);
      let dataBytes = encoder.encode(payload);
      let equal = await crypto.subtle.verify(
          algorithm.name,
          key,
          sigBytes,
          dataBytes,
      );

      return equal;
  }

  function hexToBytes(hex) {
      let len = hex.length / 2;
      let bytes = new Uint8Array(len);

      let index = 0;
      for (let i = 0; i < hex.length; i += 2) {
          let c = hex.slice(i, i + 2);
          let b = parseInt(c, 16);
          bytes[index] = b;
          index += 1;
      }

      return bytes;
  }
  ```

  ```python Python theme={null}
  import hashlib
  import hmac
  def verify_signature(payload_body, secret_token, signature_header):
      """Verify that the payload was sent from GitHub by validating SHA256.

      Raise and return 403 if not authorized.

      Args:
          payload_body: original request body to verify (request.body())
          secret_token: GitHub app webhook token (WEBHOOK_SECRET)
          signature_header: header received from GitHub (x-hub-signature-256)
      """
      if not signature_header:
          raise HTTPException(status_code=403, detail="x-hub-signature-256 header is missing!")
      hash_object = hmac.new(secret_token.encode('utf-8'), msg=payload_body, digestmod=hashlib.sha256)
      expected_signature = "sha256=" + hash_object.hexdigest()
      if not hmac.compare_digest(expected_signature, signature_header):
          raise HTTPException(status_code=403, detail="Request signatures didn't match!")
  ```

</CodeGroup>

# Protecting against replay attacks

To mitigate replay attacks, where a bad actor intercepts webhook deliveries and re-sends the requests, use the `x-env0-event-id` header to ensure that each request is unique.

# Allow env zero's IP addresses

env zero will use the IP addresses listed [here](/guides/overview/security-overview/ip-addresses) when sending a request to the webhook URL. You can add these to your server IP allow list to block spoofed requests.

# 10-seconds response timeout

Your server should respond within 10 seconds with a 2XX response. If it takes longer, the delivery fails.

# No retries for failed requests

If a request to the webhook URL fails, env zero will not retry to send the event.

Built with [Mintlify](https://mintlify.com).

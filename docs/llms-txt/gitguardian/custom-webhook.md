# Source: https://docs.gitguardian.com/platform/configure-alerting/notifiers-integrations/custom-webhook.md

# Custom webhook

> Configure custom webhook notifications to forward GitGuardian incident events to any HTTP endpoint.

Custom webhooks allow you to receive GitGuardian notifications on any server that accepts incoming json-encoded HTTP "POST" requests.

We use HMAC with sha256 as a hash function to sign the payload of our requests. The key used is a string concatenation
of the timestamp and the signature token.
This allows you to check that requests are coming from GitGuardian and that the payload was not altered during transport.
See below how to implement the verification procedure. You can set the signature token in your settings.

The âTimestampâ field in the header counters replay attacks. If your current timestamp differs from our sending âTimestampâ
by more than a few seconds, it is safer to drop the request.

A custom header can also be added to the requests from your settings to specify, for example, the environment or service.

## How to create a custom webhook endpoint

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/DJqetLVxgNs?controls=0&modestbranding=1" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowFullScreen></iframe>

1. Navigate to Settings > Workspace > Integrations > Destinations > [Custom webhook](https://dashboard.gitguardian.com/settings/integrations/custom_webhook)

### For a personal workspace

2. Create a new custom webhook with the name of your webhook and the URL where you want to receive GitGuardian notifications.
   GitGuardian generates a default signature token for you to verify the authenticity of the webhook. The signature token can be edited, make sure to store it in a safe place as you won't be able to access it again after creating the webhook.

   ![Custom webhook form](/img/platform/configure-alerting/notifiers-integrations/custom-webhook/custom_webhook_form.png)

3. Select the events you would like to subscribe to and receive.
4. Configure the endpoint on your side to verify the incoming request and handle GitGuardian alerts.

### For a business workspace

2. Create a new custom webhook at team level.

- If you intend to activate the custom webhook for ALL incidents within the workspace, you should create it within the 'All-incidents team'.
- If you intend to activate the custom webhook for incidents within a particular team, you should create it within that team.

This can be done directly from the integration page:

![Manage integrations](/img/platform/collaboration-and-sharing/team-notifiers-workspaceconf.png)

or from the team page:

![Custom webhook form team](/img/platform/configure-alerting/notifiers-integrations/custom-webhook/custom-webhook-team.png)

3. Select the events you would like to subscribe to and receive.
4. Configure the endpoint on your side to verify the incoming request and handle GitGuardian alerts.

### Events

You can subscribe to the following events from **GitGuardian Internal Monitoring** and/or **GitGuardian Public Monitoring** (if your workspace and team have access to Public Monitoring):

| Name                           | Description                                                        |
|--------------------------------|--------------------------------------------------------------------|
| **New incident detected**      | A new incident has been detected.                                  |
| **New occurrence detected**    | A new occurrence has been detected for this incident.              |
| **Incident resolved**          | This incident has been resolved.                                   |
| **Incident ignored**           | This incident has been ignored.                                    |
| **Incident reopened**          | This incident has been reopened.                                   |
| **Incident regression**        | A new regression was found for this incident.                      |
| **Incident assigned**          | This incident has been assigned to a user.                         |
| **Incident reassigned**        | This incident has been reassigned to a different user.             |
| **Incident unassigned**        | A user was unassigned from this incident.                          |
| **Incident Severity changed**  | The severity has been updated for this incident.                   |
| **Incident Validity changed**  | The validity has been updated for this incident.                   |
| **Incident access granted**    | A user has been granted access to this incident.                   |
| **Incident access revoked**    | Access to this incident has been revoked for a user.               |
| **Incident shared publicly**   | A user has generated a public sharing link for this incident.      |
| **Incident unshared publicly** | A user has deactivated the public sharing link for this incident.  |
| **Feedback submitted**         | A feedback has been submitted for this incident.                   |
| **New comment on an incident** | A new note has been created for this incident.                     |

## How to test the webhook

You can send a test message from the GitGuardian workspace in order to check that your webhook is operational. Here is a sample payload of the test message you will receive:

```json
{
  "author": {
    "info": "sample@sample.sample",
    "name": "Sample Sample"
  },
  "origin": "GitGuardian",
  "date": "2042-10-10 04:00:00 PM",
  "type": "Welcome Message Token",
  "policy": "Secrets detection",
  "gitguardian_link": "http://dashboard.gitguardian.com/workspace/34123/incidents/8213",
  "break_url": "github.com/sample_user/sample_repo/compare#ae32df",
  "severity": "unknown",
  "validity": "invalid",
  "matches": [
    {
      "type": "client_id",
      "match": "--censored--",
      "index_start": 74,
      "index_end": 86,
      "pre_line_start": 2,
      "pre_line_end": 2,
      "post_line_start": 3,
      "post_line_end": 3
    },
    {
      "type": "client_secret",
      "match": "--censored--",
      "index_start": 30,
      "index_end": 44,
      "pre_line_start": 1,
      "pre_line_end": 1,
      "post_line_start": 2,
      "post_line_end": 2
    }
  ]
}
```

> Note: your response message will contain the matched secret in plain text and will not show as `--censored--` as shown above.

## How to verify the payload signature

We use HMAC with SHA256 as a hash function to sign the payload of our requests. The key used is a string concatenation
of the timestamp and the signature token. This allows you to check that requests are coming from GitGuardian and that the payload was not altered during transport.

See below how to implement the verification procedure. You can set the signature token in your settings.

The `Timestamp` field in the header counters replay attacks. If your current timestamp differs from our sending `Timestamp`
by more than a few seconds, it is safer to drop the request.

The `Gitguardian-Signature` replaces the old header `X-GitGuardian-Signature`, which is still available but deprecated as we switch to the new.

#### Python3 example

Here is a python3 example of how to verify the signature of our notifications:

- **signature** is from our request's headers
- **timestamp** is from our request's headers
- **signature_token** is the token that you have specified in the settings
- **payload** is our request body, decoded from âutf-8â (i.e. string representing our json)

```python

def verify_signature(signature: str, timestamp: str, signature_token: str, payload: str) -> bool:
  if not signature.startswith("sha256="):
    return False

  signature = signature.split("sha256=")[-1]
  hmac_digest = hmac.new(key=bytes(timestamp + signature_token, "utf-8"),
                         msg=bytes(payload, "utf-8"),
                         digestmod=hashlib.sha256).hexdigest()
  return hmac.compare_digest(signature, hmac_digest)
```

Here is a very basic unit test that lets you check that your implementation is correct:

```python
assert verify_signature_gitguardian(
    signature="sha256=172fe3d694b734aa53dc892fd3b8d62163fc240064de570ba006900bb54a0fc2",
    timestamp="0",
    signature_token="foo",
    payload="bar"
  )
```

#### AWS Lambda example

When using AWS lambda, a **HTTP API Gateway** must be used as trigger.

![HTTP API Gateway](/img/platform/configure-alerting/notifiers-integrations/custom-webhook/lambda.png)

Below are two examples, respectively in Javascript and Python, on how to validate the
payload received from the dashboard.

##### Javascript

```js
const { createHmac } = require('crypto')

function verifySignature(signature, timestamp, signatureToken, payload) {
  var signatureHeader = signature.substring(0, 7)
  if (signatureHeader !== 'sha256=') {
    return false
  }

  var signatureActual = signature.split('=')[1]

  var hmac = createHmac(
    'sha256',
    Buffer.from(timestamp + signatureToken, 'utf8')
  )
  hmac.update(payload)

  var result = hmac.digest('hex')

  if (result === signatureActual) {
    return true
  } else {
    return false
  }
}

exports.handler = async (event) => {
  const payload_signature = event.headers['gitguardian-signature']
  const timestamp = event.headers['timestamp']
  const webhook_token = '<INSERT SIGNATURE TOKEN HERE>'
  const payload = event.body

  let statusCode
  if (verifySignature(payload_signature, timestamp, webhook_token, payload)) {
    console.log('OK')
    statusCode = 200
  } else {
    statusCode = 400
    throw new Error()
  }
  const response = {
    statusCode,
  }
  return response
}
```

##### Python

```python

def verify_signature(signature: str, timestamp: str, signature_token: str, payload: str) -> bool:
    if not signature.startswith("sha256="):
        return False
    signature = signature.split("sha256=")[-1]
    hmac_digest = hmac.new(key=bytes(timestamp + signature_token, "utf-8"),
                           msg=bytes(payload, "utf-8"),
                           digestmod=hashlib.sha256).hexdigest()
    return hmac.compare_digest(signature, hmac_digest)

def lambda_handler(event, context):
    payload_dump = event["body"]

    timestamp = event["headers"]["timestamp"]
    payload_signature = event["headers"]["gitguardian-signature"]
    webhook_token = "<INSERT SIGNATURE TOKEN HERE>"

    if verify_signature(payload_signature, timestamp, webhook_token, payload_dump):
        return {'statusCode': 200, 'body': json.dumps('Success') }

    return {'statusCode': 400, 'body': json.dumps('Failed to verify') }
```

## Payload structure

:::caution
Please be aware that webhook delivery is not guaranteed and is best effort. When a webhook event is triggered, GitGuardian sends a single HTTP POST request to your defined webhook endpoint. However, if your endpoint is unreachable or there are network issues between GitGuardian and your server, the webhook event may not be received. While webhooks are generally reliable, it's important to remember that delivery cannot be guaranteed.
:::

The payloads are described by the OpenAPI specification. Below are a few examples for the different events you can subscribe to.

<details>

<summary>Incident events payloads</summary>

#### New incident

```json
{
  "source": "GitGuardian",
  "timestamp": "2022-06-20T07:45:32.930965Z",
  "action": "incident_triggered",
  "message": "A new incident has been detected.",
  "target_user": "GitGuardian",
  "target_team": "My team",
  "custom_webhook_name": "My custom webhook name",
  "incident": {
    "id": 31542,
    "date": "2022-06-20T07:45:31.666462Z",
    "detector": {
      "name": "generic_password",
      "display_name": "Generic Password",
      "nature": "generic",
      "family": "Other",
      "detector_group_name": "generic_password",
      "detector_group_display_name": "Generic Password"
    },
    "secret_hash": "xxx",
    "hmsl_hash": "xxx",
    "secret_revoked": false,
    "validity": "no_checker",
    "occurrence_count": 0,
    "status": "triggered",
    "declarative_secret_status": "active", // only for public monitoring incidents.
    "regression": false, // only for internal monitoring incidents.
    "assignee_email": null,
    "severity": "unknown",
    "ignored_at": null,
    "ignore_reason": null,
    "resolved_at": null,
    "gitguardian_url": "https://dashboard.gitguardian.com/workspace/1/incidents/xxx",
    "share_url": null,
    "feedbacks": []
  }
}
```

#### Assign event

```json
{
  "source": "GitGuardian",
  "timestamp": "2022-06-17T12:18:41.917977Z",
  "action": "incident_assigned",
  "message": "This incident has been assigned to a user.",
  "target_user": "John Doe john.doe@gitguardian.com",
  "target_team": "My team",
  "custom_webhook_name": "My custom webhook name",
  "incident": {
    "id": 31450,
    "date": "2022-06-15T09:16:42.378417Z",
    "detector": {
      "name": "generic_password",
      "display_name": "Generic Password",
      "nature": "generic",
      "family": "Other",
      "detector_group_name": "generic_password",
      "detector_group_display_name": "Generic Password"
    },
    "secret_hash": "xxx",
    "hmsl_hash": "xxx",
    "secret_revoked": false,
    "validity": "no_checker",
    "occurrence_count": 1,
    "status": "assigned",
    "declarative_secret_status": "active", // only for public monitoring incidents.
    "regression": false, // only for internal monitoring incidents.
    "assignee_email": "bruce.wayne@gitguardian.com",
    "severity": "medium",
    "ignored_at": null,
    "ignore_reason": null,
    "resolved_at": null,
    "gitguardian_url": "https://dashboard.gitguardian.com/workspace/1/incidents/xxx",
    "share_url": null,
    "feedbacks": []
  }
}
```

#### Re-assign event

```json
{
  "source": "GitGuardian",
  "timestamp": "2022-06-17T12:18:41.917977Z",
  "action": "incident_reassigned",
  "message": "This incident has been reassigned to a different user.",
  "target_user": "John Doe john.doe@gitguardian.com",
  "target_team": "My team",
  "custom_webhook_name": "My custom webhook name",
  "incident": {
    "id": 31450,
    "date": "2022-06-15T09:16:42.378417Z",
    "detector": {
      "name": "generic_password",
      "display_name": "Generic Password",
      "nature": "generic",
      "family": "Other",
      "detector_group_name": "generic_password",
      "detector_group_display_name": "Generic Password"
    },
    "secret_hash": "xxx",
    "hmsl_hash": "xxx",
    "secret_revoked": false,
    "validity": "no_checker",
    "occurrence_count": 1,
    "status": "assigned",
    "declarative_secret_status": "active", // only for public monitoring incidents.
    "regression": false, // only for internal monitoring incidents.
    "assignee_email": "bruce.wayne@gitguardian.com",
    "severity": "medium",
    "ignored_at": null,
    "ignore_reason": null,
    "resolved_at": null,
    "gitguardian_url": "https://dashboard.gitguardian.com/workspace/1/incidents/xxx",
    "share_url": null,
    "feedbacks": []
  }
}
```

#### Severity change

```json
{
  "source": "GitGuardian",
  "timestamp": "2022-06-17T12:18:22.220508Z",
  "action": "incident_severity_changed",
  "message": "The severity has been updated for this incident.",
  "target_user": "John Doe john.doe@gitguardian.com",
  "target_team": "My team",
  "custom_webhook_name": "My custom webhook name",
  "incident": {
    "id": 31450,
    "date": "2022-06-15T09:16:42.378417Z",
    "detector": {
      "name": "generic_password",
      "display_name": "Generic Password",
      "nature": "generic",
      "family": "Other",
      "detector_group_name": "generic_password",
      "detector_group_display_name": "Generic Password"
    },
    "secret_hash": "xxx",
    "hmsl_hash": "xxx",
    "secret_revoked": false,
    "validity": "no_checker",
    "occurrence_count": 1,
    "status": "triggered",
    "declarative_secret_status": "active", // only for public monitoring incidents.
    "regression": false, // only for internal monitoring incidents.
    "assignee_email": null,
    "severity": "medium",
    "ignored_at": null,
    "ignore_reason": null,
    "resolved_at": null,
    "gitguardian_url": "https://dashboard.gitguardian.com/workspace/1/incidents/xxx",
    "share_url": null,
    "feedbacks": []
  }
}
```

#### Validity change

```json
{
  "source": "GitGuardian",
  "timestamp": "2022-06-17T12:18:22.220508Z",
  "action": "incident_validity_changed",
  "message": "The validity has been updated for this incident.",
  "target_user": "John Doe john.doe@gitguardian.com",
  "target_team": "My team",
  "custom_webhook_name": "My custom webhook name",
  "incident": {
    "id": 31450,
    "date": "2022-06-15T09:16:42.378417Z",
    "detector": {
      "name": "generic_password",
      "display_name": "Generic Password",
      "nature": "generic",
      "family": "Other",
      "detector_group_name": "generic_password",
      "detector_group_display_name": "Generic Password"
    },
    "secret_hash": "xxx",
    "hmsl_hash": "xxx",
    "secret_revoked": false,
    "validity": "invalid",
    "occurrence_count": 1,
    "status": "triggered",
    "declarative_secret_status": "active", // only for public monitoring incidents.
    "regression": false, // only for internal monitoring incidents.
    "assignee_email": null,
    "severity": "medium",
    "ignored_at": null,
    "ignore_reason": null,
    "resolved_at": null,
    "gitguardian_url": "https://dashboard.gitguardian.com/workspace/1/incidents/xxx",
    "share_url": null,
    "feedbacks": []
  }
}
```

#### Incident resolved

```json
{
  "source": "GitGuardian",
  "timestamp": "2022-06-22T09:00:16.143457Z",
  "action": "incident_resolved",
  "message": "This incident has been resolved.",
  "target_user": "John Doe john.doe@gitguardian.com",
  "target_team": "My team",
  "custom_webhook_name": "My custom webhook name",
  "incident": {
    "id": 31605,
    "date": "2022-06-16T08:23:40Z",
    "detector": {
      "name": "aws_iam",
      "display_name": "AWS Keys",
      "nature": "specific",
      "family": "credentials",
      "detector_group_name": "aws_iam",
      "detector_group_display_name": "AWS Keys"
    },
    "secret_hash": "xxx",
    "hmsl_hash": "xxx",
    "secret_revoked": true,
    "validity": "not_checked",
    "occurrence_count": 1,
    "status": "resolved",
    "declarative_secret_status": "active", // only for public monitoring incidents.
    "regression": false, // only for internal monitoring incidents.
    "assignee_email": null,
    "severity": "high",
    "ignored_at": null,
    "ignore_reason": null,
    "resolved_at": "2022-06-22T09:00:16.038050Z",
    "gitguardian_url": "https://dashboard.gitguardian.com/workspace/1/incidents/xxx",
    "share_url": null,
    "feedbacks": []
  }
}
```

#### Incident ignored

```json
{
  "source": "GitGuardian",
  "timestamp": "2022-06-22T09:02:57.377837Z",
  "action": "incident_ignored",
  "message": "This incident has been ignored.",
  "target_user": "John Doe john.doe@gitguardian.com",
  "target_team": "My team",
  "custom_webhook_name": "My custom webhook name",
  "incident": {
    "id": 31605,
    "date": "2022-06-16T08:23:40Z",
    "detector": {
      "name": "aws_iam",
      "display_name": "AWS Keys",
      "nature": "specific",
      "family": "credentials",
      "detector_group_name": "aws_iam",
      "detector_group_display_name": "AWS Keys"
    },
    "secret_hash": "xxx",
    "hmsl_hash": "xxx",
    "secret_revoked": false,
    "validity": "not_checked",
    "occurrence_count": 1,
    "status": "ignored",
    "declarative_secret_status": "active", // only for public monitoring incidents.
    "regression": false, // only for internal monitoring incidents.
    "assignee_email": null,
    "severity": "high",
    "ignored_at": "2022-06-22T09:02:57.292217Z",
    "ignore_reason": "low_risk",
    "resolved_at": null,
    "gitguardian_url": "https://dashboard.gitguardian.com/workspace/1/incidents/xxx",
    "share_url": null,
    "feedbacks": []
  }
}
```

#### Incident reopened

```json
{
  "source": "GitGuardian",
  "timestamp": "2022-06-22T09:03:10.775369Z",
  "action": "incident_reopened",
  "message": "This incident has been reopened.",
  "target_user": "John Doe john.doe@gitguardian.com",
  "target_team": "My team",
  "custom_webhook_name": "My custom webhook name",
  "incident": {
    "id": 31605,
    "date": "2022-06-16T08:23:40Z",
    "detector": {
      "name": "aws_iam",
      "display_name": "AWS Keys",
      "nature": "specific",
      "family": "credentials",
      "detector_group_name": "aws_iam",
      "detector_group_display_name": "AWS Keys"
    },
    "secret_hash": "xxx",
    "hmsl_hash": "xxx",
    "secret_revoked": false,
    "validity": "not_checked",
    "occurrence_count": 1,
    "status": "ignored",
    "declarative_secret_status": "active", // only for public monitoring incidents.
    "regression": false, // only for internal monitoring incidents.
    "assignee_email": null,
    "severity": "high",
    "ignored_at": "2022-06-22T09:02:57.292217Z",
    "ignore_reason": "low_risk",
    "resolved_at": null,
    "gitguardian_url": "https://dashboard.gitguardian.com/workspace/1/incidents/xxx",
    "share_url": null,
    "feedbacks": []
  }
}
```

#### Incident regression

```json
{
  "source": "GitGuardian",
  "timestamp": "2022-06-28T09:10:19.966461Z",
  "action": "incident_regression",
  "message": "A new regression was found for this incident.",
  "target_user": "GitGuardian",
  "target_team": "My team",
  "custom_webhook_name": "My custom webhook name",
  "incident": {
    "id": 1234,
    "date": "2022-06-28T09:10:18.613418Z",
    "detector": {
      "name": "aws_iam",
      "display_name": "AWS Keys",
      "nature": "specific",
      "family": "credentials",
      "detector_group_name": "aws_iam",
      "detector_group_display_name": "AWS Keys"
    },
    "secret_hash": "xxx",
    "hmsl_hash": "xxx",
    "secret_revoked": true,
    "validity": "invalid",
    "occurrence_count": 4,
    "status": "triggered",
    "declarative_secret_status": "active", // only for public monitoring incidents.
    "regression": false, // only for internal monitoring incidents.
    "assignee_email": null,
    "severity": "high",
    "ignored_at": null,
    "ignore_reason": null,
    "resolved_at": null,
    "gitguardian_url": "https://dashboard.gitguardian.com/workspace/1/incidents/xxx",
    "share_url": null,
    "feedbacks": []
  }
}
```

#### Incident access granted

```json
{
  "source": "GitGuardian",
  "timestamp": "2022-06-28T09:15:55.682589Z",
  "action": "incident_access_granted",
  "message": "A user has been granted access to this incident.",
  "target_user": "John Doe john.doe@gitguardian.com",
  "target_team": "My team",
  "custom_webhook_name": "My custom webhook name",
  "incident": {
    "id": 3831600,
    "date": "2022-06-28T00:03:46.110078Z",
    "detector": {
      "name": "stripe",
      "display_name": "Stripe Keys",
      "nature": "specific",
      "family": "token",
      "detector_group_name": "stripe_keys",
      "detector_group_display_name": "Stripe Keys"
    },
    "secret_hash": "xxx",
    "hmsl_hash": "xxx",
    "secret_revoked": false,
    "validity": "invalid",
    "occurrence_count": 2,
    "status": "triggered",
    "declarative_secret_status": "active", // only for public monitoring incidents.
    "regression": false, // only for internal monitoring incidents.
    "assignee_email": null,
    "severity": "unknown",
    "ignored_at": null,
    "ignore_reason": null,
    "resolved_at": null,
    "gitguardian_url": "https://dashboard.gitguardian.com/workspace/8/incidents/xxx",
    "share_url": "https://dashboard.gitguardian.com/share/incidents/xxx",
    "feedbacks": []
  },
  "member": {
    "id": 3252,
    "name": "John Smith",
    "email": "john.smith@example.org",
    "access_level": "owner"
  }
}
```

`member` provides details about the member who have been granted access during this event. If multiple members were granted access, there will be one event for each access granted.

#### Incident access revoked

```json
{
  "source": "GitGuardian",
  "timestamp": "2022-06-28T09:17:01.353280Z",
  "action": "incident_access_revoked",
  "message": "Access to this incident has been revoked for a user.",
  "target_user": "John Doe john.doe@gitguardian.com",
  "target_team": "My team",
  "custom_webhook_name": "My custom webhook name",
  "incident": {
    "id": 3831600,
    "date": "2022-06-28T00:03:46.110078Z",
    "detector": {
      "name": "stripe",
      "display_name": "Stripe Keys",
      "nature": "specific",
      "family": "token",
      "detector_group_name": "stripe_keys",
      "detector_group_display_name": "Stripe Keys"
    },
    "secret_hash": "xxx",
    "hmsl_hash": "xxx",
    "secret_revoked": false,
    "validity": "invalid",
    "occurrence_count": 2,
    "status": "triggered",
    "declarative_secret_status": "active", // only for public monitoring incidents.
    "regression": false, // only for internal monitoring incidents.
    "assignee_email": null,
    "severity": "unknown",
    "ignored_at": null,
    "ignore_reason": null,
    "resolved_at": null,
    "gitguardian_url": "https://dashboard.gitguardian.com/workspace/8/incidents/xxx",
    "share_url": "https://dashboard.gitguardian.com/share/incidents/xxx",
    "feedbacks": []
  },
  "member": {
    "id": 3252,
    "name": "John Smith",
    "email": "john.smith@example.org",
    "access_level": "owner"
  }
}
```

`member` provides details about the member who have been revoked access during this event. If multiple members were granted access, there will be one event for each access granted.

#### Incident shared publicly

```json
{
  "source": "GitGuardian",
  "timestamp": "2022-06-28T08:48:49.290758Z",
  "action": "incident_shared_publicly",
  "message": "A user has generated a public sharing link for this incident.",
  "target_user": "John Doe john.doe@gitguardian.com",
  "target_team": "My team",
  "custom_webhook_name": "My custom webhook name",
  "incident": {
    "id": 3827964,
    "date": "2022-06-23T14:34:11Z",
    "detector": {
      "name": "aws_iam",
      "display_name": "AWS Keys",
      "nature": "specific",
      "family": "credentials",
      "detector_group_name": "aws_iam",
      "detector_group_display_name": "AWS Keys"
    },
    "secret_hash": "xxx",
    "hmsl_hash": "xxx",
    "secret_revoked": false,
    "validity": "invalid",
    "occurrence_count": 1,
    "status": "triggered",
    "declarative_secret_status": "active", // only for public monitoring incidents.
    "regression": false, // only for internal monitoring incidents.
    "assignee_email": null,
    "severity": "unknown",
    "ignored_at": null,
    "ignore_reason": null,
    "resolved_at": null,
    "gitguardian_url": "https://dashboard.gitguardian.com/workspace/1/incidents/xx",
    "share_url": "https://dashboard.gitguardian.com/share/incidents/xxx",
    "feedbacks": []
  }
}
```

#### Incident publicly unshared

```json
{
  "source": "GitGuardian",
  "timestamp": "2022-06-28T08:49:56.806741Z",
  "action": "incident_unshared_publicly",
  "message": "A user has deactivated the public sharing link for this incident.",
  "target_user": "John Doe john.doe@gitguardian.com",
  "target_team": "My team",
  "custom_webhook_name": "My custom webhook name",
  "incident": {
    "id": 3827964,
    "date": "2022-06-23T14:34:11Z",
    "detector": {
      "name": "aws_iam",
      "display_name": "AWS Keys",
      "nature": "specific",
      "family": "credentials",
      "detector_group_name": "aws_iam",
      "detector_group_display_name": "AWS Keys"
    },
    "secret_hash": "xxx",
    "hmsl_hash": "xxx",
    "secret_revoked": false,
    "validity": "invalid",
    "occurrence_count": 2,
    "status": "triggered",
    "declarative_secret_status": "active", // only for public monitoring incidents.
    "regression": false, // only for internal monitoring incidents.
    "assignee_email": null,
    "severity": "unknown",
    "ignored_at": null,
    "ignore_reason": null,
    "resolved_at": null,
    "gitguardian_url": "https://dashboard.gitguardian.com/workspace/1/incidents/xxx",
    "share_url": null,
    "feedbacks": []
  }
}
```

#### Incident feedback received
```json
{
  "source": "GitGuardian",
  "timestamp": "2022-06-28T08:49:56.806741Z",
  "action": "incident_feedback_received",
  "message": "A feedback has been submitted for this incident.",
  "target_user": "John Doe john.doe@gitguardian.com",
  "target_team": "My team",
  "custom_webhook_name": "My custom webhook name",
  "incident": {
    "id": 3827964,
    "date": "2022-06-23T14:34:11Z",
    "detector": {
      "name": "aws_iam",
      "display_name": "AWS Keys",
      "nature": "specific",
      "family": "credentials",
      "detector_group_name": "aws_iam",
      "detector_group_display_name": "AWS Keys"
    },
    "secret_hash": "xxx",
    "hmsl_hash": "xxx",
    "secret_revoked": false,
    "validity": "invalid",
    "occurrence_count": 2,
    "status": "triggered",
    "declarative_secret_status": "active", // only for public monitoring incidents.
    "regression": false, // only for internal monitoring incidents.
    "assignee_email": null,
    "severity": "unknown",
    "ignored_at": null,
    "ignore_reason": null,
    "resolved_at": null,
    "gitguardian_url": "https://dashboard.gitguardian.com/workspace/1/incidents/xxx",
    "share_url": null,
    "feedbacks": [
      {
        "id": 1,
        "date": "2022-06-28T08:49:56.806741Z",
        "updated_at": "2022-06-28T08:49:56.806741Z",
        "revoked": false,
        "remarks": "This secret is no longer valid.",
        "member": {
          "id": 1,
          "role": "owner",
          "name": "John Doe",
          "email": "john.doe@gitguardian.com"
        },
        "real_secret": false,
        "sensitive": false
      }
    ]
  }
}
```

</details>

<details>
<summary>Occurrences events payload</summary>

#### New occurrence

```json
{
   "source": "GitGuardian",
   "timestamp": "2022-06-23T09:10:24.594597Z",
   "action": "new_occurrence",
   "message": "A new occurrence has been detected for this incident.",
   "target_user": "GitGuardian",
   "target_team": "My team",
   "custom_webhook_name": "My custom webhook name",
   "incident": {
      "id": 31605,
      "date": "2022-06-16T08:23:40Z",
      "detector": {
         "name": "aws_iam",
         "display_name": "AWS Keys",
         "nature": "specific",
         "family": "credentials",
         "detector_group_name": "aws_iam",
         "detector_group_display_name": "AWS Keys"
      },
      "secret_hash": "xxx",
      "hmsl_hash": "xxx",
      "secret_revoked": false,
      "validity": "not_checked",
      "occurrence_count": 5,
      "status": "assigned",
      "declarative_secret_status": "active", // only for public monitoring incidents.
      "regression": false, // only for internal monitoring incidents.
      "assignee_email": "bruce.wayne@gitguardian.com",
      "severity": "high",
      "ignored_at": null,
      "ignore_reason": null,
      "resolved_at": null,
      "gitguardian_url": "https://dashboard.gitguardian.com/workspace/1/incidents/xxx",
      "share_url": null,
      "feedbacks": []
   },
   "occurrence": {
      "id": 1234,
      "incident_id": 1243,
      "kind": "RLTM",
      "sha": "xxx", // only for internal monitoring incidents.
      "element_type": "GIT_COMMIT", // only for public monitoring incidents.
      "element": "xxx", // only for public monitoring incidents.
      "actors": [ // actors section only for public monitoring incidents.
         {
            "id": 1234,
            "type": "github_user",
            "name": "xxx",
            "email": "xxx@yy.com",
            "primary": true,
            "url": "https://github.com/xxx"
         }
      ],
      "author_name": "GitHub", // only for internal monitoring incidents.
      "author_info": "noreply@github.com", // only for internal monitoring incidents.
      "date": "2022-06-23T09:10:23.529812Z",
      "presence": "visible",
      "url": "https://github.com/user/repo/commit/123#diff-xxx",
      "filepath": "my/path/TestJS.js",
      "change_type": "addition", // only for VCS sources, null otherwise.
      "filename": "TestJS.js", // only for public monitoring incidents.
      "source": {
         "id": 710,
         "url": "https://github.com/user/repo",
         "type": "github",
         "full_name": "name of repository", // only for internal monitoring incidents.
         "name": "name of repository", // only for public monitoring incidents.
         "health": "at_risk", // only for internal monitoring incidents.
         "open_incidents_count": 5, // only for internal monitoring incidents.
         "closed_incidents_count": 0, // only for internal monitoring incidents.
         "visibility": "private", // only for internal monitoring incidents.
         "last_scan": { // only for internal monitoring incidents.
            "status": "finished",
            "date": "2022-11-18T17:07:59.079520Z"
         },
         "external_id": "github_id",
         "metadata": {} // only for public monitoring incidents.
      }
   }
}
```

</details>

<details>
<summary>Notes events payloads</summary>

#### New incident note

```json
{
  "source": "GitGuardian",
  "timestamp": "2022-06-22T09:11:02.733441Z",
  "action": "incident_note_created",
  "message": "A new note has been created for this incident.",
  "target_user": "John Doe john.doe@gitguardian.com",
  "target_team": "My team",
  "custom_webhook_name": "My custom webhook name",
  "incident": {
    "id": 31605,
    "date": "2022-06-16T08:23:40Z",
    "detector": {
      "name": "aws_iam",
      "display_name": "AWS Keys",
      "nature": "specific",
      "family": "credentials",
      "detector_group_name": "aws_iam",
      "detector_group_display_name": "AWS Keys"
    },
    "secret_hash": "xxx",
    "hmsl_hash": "xxx",
    "secret_revoked": false,
    "validity": "not_checked",
    "occurrence_count": 1,
    "status": "triggered",
    "declarative_secret_status": "active", // only for public monitoring incidents.
    "regression": false, // only for internal monitoring incidents.
    "assignee_email": null,
    "severity": "high",
    "ignored_at": null,
    "ignore_reason": null,
    "resolved_at": null,
    "gitguardian_url": "https://dashboard.gitguardian.com/workspace/1/incidents/xxx",
    "share_url": null,
    "feedbacks": []
  },
  "incident_note": {
    "id": 46389,
    "api_token": null,
    "created_at": "2022-06-22T09:11:02.683727Z",
    "updated_at": null,
    "comment": "This is not a test"
  }
}
```

</details>

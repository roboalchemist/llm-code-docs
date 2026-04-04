# Source: https://www.courier.com/docs/tutorials/sending/how-to-send-bulk-notifications.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How To Send Bulk Notifications

> Learn how to use Courier's Bulk API to send notifications to large user groups with batched ingestion and a single execution call.

The Bulk API lets you incrementally build a notification job for a large number of users and then execute it with a single API call. While the Send API can deliver messages to multiple recipients, the Bulk API gives you more control over ingestion and lets you track progress as the job runs.

Like sending a single message, the Bulk API works across channels (email, SMS, chat, in-app inbox, push) and providers (Twilio, SendGrid, etc).

## Prerequisites

* A [Courier account](https://app.courier.com/) with an API key
* A published notification template (or inline content)
* Recipient user IDs or profile data for the users you want to notify

## Sending a Bulk Job

<Steps>
  <Step title="Create a bulk job">
    Define the job with a template and any global data that applies to all recipients. The response returns a `jobId` you'll use for the remaining steps.

    <CodeGroup>
      ```bash cURL theme={null}
      curl -X POST https://api.courier.com/bulk \
        -H "Authorization: Bearer YOUR_AUTH_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{
          "message": {
            "message": {
              "template": "YOUR_TEMPLATE_ID"
            },
            "data": {
              "company_name": "Acme Corp"
            }
          }
        }'
      ```

      ```javascript Node.js theme={null}
      import Courier from "@trycourier/courier";

      const client = new Courier({ apiKey: "YOUR_AUTH_TOKEN" });

      const { jobId } = await client.bulk.createJob({
        message: {
          message: {
            template: "YOUR_TEMPLATE_ID",
          },
          data: {
            company_name: "Acme Corp",
          },
        },
      });

      console.log("Job created:", jobId);
      ```

      ```python Python theme={null}
      from courier import Courier

      client = Courier(api_key="YOUR_AUTH_TOKEN")

      response = client.bulk.create_job(
          message={
              "message": {
                  "template": "YOUR_TEMPLATE_ID",
              },
              "data": {
                  "company_name": "Acme Corp",
              },
          }
      )

      print("Job created:", response.job_id)
      ```
    </CodeGroup>

    **Response:**

    ```json  theme={null}
    {
      "jobId": "1-61e9dd53-b5bb6c863b7ffbe83ad4b28d"
    }
    ```

    <Tip>
      All bulk endpoints support idempotent requests using the `Idempotency-Key` header. Include one if you want safe retries.
    </Tip>

    You can also pass optional fields like `brand`, `locale`, and a global `data` object that applies to every recipient. Per-user data (added in the next step) takes precedence over global data.
  </Step>

  <Step title="Ingest users into the job">
    Add recipients to the job using the `jobId`. You can call this endpoint multiple times to ingest users in batches; the job won't expire until you run it.

    <CodeGroup>
      ```bash cURL theme={null}
      curl -X POST https://api.courier.com/bulk/JOB_ID \
        -H "Authorization: Bearer YOUR_AUTH_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{
          "users": [
            {
              "to": {
                "user_id": "spike_spiegel",
                "data": {
                  "recipientName": "Spike Spiegel"
                }
              }
            },
            {
              "to": {
                "user_id": "faye_valentine",
                "data": {
                  "recipientName": "Faye Valentine"
                }
              }
            }
          ]
        }'
      ```

      ```javascript Node.js theme={null}
      await client.bulk.addUsers("JOB_ID", {
        users: [
          {
            to: {
              user_id: "spike_spiegel",
              data: { recipientName: "Spike Spiegel" },
            },
          },
          {
            to: {
              user_id: "faye_valentine",
              data: { recipientName: "Faye Valentine" },
            },
          },
        ],
      });
      ```

      ```python Python theme={null}
      client.bulk.add_users(
          job_id="JOB_ID",
          users=[
              {
                  "to": {
                      "user_id": "spike_spiegel",
                      "data": {"recipientName": "Spike Spiegel"},
                  },
              },
              {
                  "to": {
                      "user_id": "faye_valentine",
                      "data": {"recipientName": "Faye Valentine"},
                  },
              },
          ],
      )
      ```
    </CodeGroup>

    Each user object supports these optional fields:

    | Field         | Description                                                 |
    | ------------- | ----------------------------------------------------------- |
    | `to.user_id`  | Courier user ID for the recipient                           |
    | `to.data`     | Per-user data that overrides the global `data` from the job |
    | `profile`     | Inline profile data (email, phone, etc.)                    |
    | `preferences` | Per-user preference overrides                               |

    <Note>
      You can call this endpoint as many times as needed before running the job. The bulk job will not expire until it is invoked.
    </Note>

    If there are errors (e.g. duplicate users), the response includes them alongside the successful count:

    ```json  theme={null}
    {
      "errors": [
        {
          "error": "Duplicate user",
          "user": {
            "profile": { "email": "foo@bar.com" },
            "data": { "recipientName": "Foo Bar" },
            "recipient": "foo-bar"
          }
        }
      ],
      "total": 1
    }
    ```
  </Step>

  <Step title="Run the job">
    Once all users are ingested, execute the job. This triggers Courier to fan out and send individual messages to each recipient.

    <CodeGroup>
      ```bash cURL theme={null}
      curl -X POST https://api.courier.com/bulk/JOB_ID/run \
        -H "Authorization: Bearer YOUR_AUTH_TOKEN"
      ```

      ```javascript Node.js theme={null}
      await client.bulk.runJob("JOB_ID");
      ```

      ```python Python theme={null}
      client.bulk.run_job(job_id="JOB_ID")
      ```
    </CodeGroup>

    Returns `202 Accepted`. The job begins processing asynchronously.

    <Warning>
      A job can only be triggered once. If you need to send to more users after running, create a new job.
    </Warning>
  </Step>

  <Step title="Monitor job status">
    Track the job's progress using the `jobId`. The status response includes delivery statistics.

    ```bash  theme={null}
    curl https://api.courier.com/bulk/JOB_ID \
      -H "Authorization: Bearer YOUR_AUTH_TOKEN"
    ```

    ```json  theme={null}
    {
      "job": {
        "definition": {
          "event": "V7E6M48EFQMB78H746QCCD1KSRAA"
        },
        "enqueued": 2,
        "failures": 0,
        "received": 2,
        "status": "COMPLETED"
      }
    }
    ```

    | Field      | Description                             |
    | ---------- | --------------------------------------- |
    | `received` | Total users ingested into the job       |
    | `enqueued` | Messages placed on the pipeline         |
    | `failures` | Errors during job processing            |
    | `status`   | `CREATED`, `PROCESSING`, or `COMPLETED` |

    You can also fetch individual user statuses with pagination:

    ```bash  theme={null}
    curl "https://api.courier.com/bulk/JOB_ID/users?cursor=CURSOR" \
      -H "Authorization: Bearer YOUR_AUTH_TOKEN"
    ```

    ```json  theme={null}
    {
      "items": [
        {
          "recipient": "spike_spiegel",
          "messageId": "1-61e9dd7d-13c08339357603322c433d55",
          "status": "ENQUEUED"
        },
        {
          "recipient": "faye_valentine",
          "status": "PENDING"
        }
      ],
      "paging": {
        "cursor": "next_cursor",
        "more": true
      }
    }
    ```

    Each item's `messageId` is the same ID you'd get from a regular `/send` request. You can look up individual messages in the [Message Logs](/platform/analytics/message-logs) or via the Messages API. If you have [Outbound Webhooks](/platform/workspaces/outbound-webhooks) configured, Courier will invoke them throughout the message lifecycle.
  </Step>
</Steps>

## What's Next

<CardGroup cols={2}>
  <Card title="Send to Lists and List Patterns" icon="list" href="/tutorials/sending/how-to-send-to-a-list-or-list-pattern-using-wildcarding">
    Use lists and wildcarding to target groups of recipients
  </Card>

  <Card title="Configure Multi-Channel Routing" icon="list-tree" href="/tutorials/sending/how-to-configure-multi-channel-routing">
    Set up channel priority and failover rules
  </Card>

  <Card title="Bulk API Reference" icon="code" href="/api-reference/bulk/create-a-bulk-job">
    Full API documentation for the Bulk endpoint
  </Card>

  <Card title="Message Logs" icon="magnifying-glass" href="/platform/analytics/message-logs">
    Track delivery status and debug notification issues
  </Card>
</CardGroup>

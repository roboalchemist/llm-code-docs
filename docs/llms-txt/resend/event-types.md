# Source: https://resend.com/docs/dashboard/webhooks/event-types.md

# Event Types

> List of supported event types and their payload.

### `email.sent`

Occurs whenever the **API request was successful**. Resend will attempt to deliver the message to the recipient's mail server.

<Accordion title="Sample Request Body">
  ```json  theme={null}
  {
    "type": "email.sent",
    "created_at": "2024-02-22T23:41:12.126Z",
    "data": {
      "broadcast_id": "8b146471-e88e-4322-86af-016cd36fd216",
      "created_at": "2024-02-22T23:41:11.894719+00:00",
      "email_id": "56761188-7520-42d8-8898-ff6fc54ce618",
      "from": "Acme <onboarding@resend.dev>",
      "to": ["delivered@resend.dev"],
      "subject": "Sending this example",
      "template_id": "43f68331-0622-4e15-8202-246a0388854b",
      "tags": {
        "category": "confirm_email"
      }
    }
  }
  ```
</Accordion>

### `email.delivered`

Occurs whenever Resend **successfully delivered the email** to the recipient's mail server.

<Accordion title="Sample Request Body">
  ```json  theme={null}
  {
    "type": "email.delivered",
    "created_at": "2024-02-22T23:41:12.126Z",
    "data": {
      "broadcast_id": "8b146471-e88e-4322-86af-016cd36fd216",
      "created_at": "2024-02-22T23:41:11.894719+00:00",
      "email_id": "56761188-7520-42d8-8898-ff6fc54ce618",
      "from": "Acme <onboarding@resend.dev>",
      "to": ["delivered@resend.dev"],
      "subject": "Sending this example",
      "template_id": "43f68331-0622-4e15-8202-246a0388854b",
      "tags": {
        "category": "confirm_email"
      }
    }
  }
  ```
</Accordion>

### `email.delivery_delayed`

Occurs whenever the **email couldn't be delivered due to a temporary issue**.

Delivery delays can occur, for example, when the recipient's inbox is full, or when the receiving email server experiences a transient issue.

<Accordion title="Sample Request Body">
  ```json  theme={null}
  {
    "type": "email.delivery_delayed",
    "created_at": "2024-02-22T23:41:12.126Z",
    "data": {
      "broadcast_id": "8b146471-e88e-4322-86af-016cd36fd216",
      "created_at": "2024-02-22T23:41:11.894719+00:00",
      "email_id": "56761188-7520-42d8-8898-ff6fc54ce618",
      "from": "Acme <onboarding@resend.dev>",
      "to": ["delivered@resend.dev"],
      "subject": "Sending this example",
      "template_id": "43f68331-0622-4e15-8202-246a0388854b",
      "tags": {
        "category": "confirm_email"
      }
    }
  }
  ```
</Accordion>

### `email.complained`

Occurs whenever the email was successfully **delivered, but the recipient marked it as spam**.

<Accordion title="Sample Request Body">
  ```json  theme={null}
  {
    "type": "email.complained",
    "created_at": "2024-02-22T23:41:12.126Z",
    "data": {
      "broadcast_id": "8b146471-e88e-4322-86af-016cd36fd216",
      "created_at": "2024-02-22T23:41:11.894719+00:00",
      "email_id": "56761188-7520-42d8-8898-ff6fc54ce618",
      "from": "Acme <onboarding@resend.dev>",
      "to": ["delivered@resend.dev"],
      "subject": "Sending this example",
      "template_id": "43f68331-0622-4e15-8202-246a0388854b",
      "tags": {
        "category": "confirm_email"
      }
    }
  }
  ```
</Accordion>

### `email.bounced`

Occurs whenever the recipient's mail server **permanently rejected the email**.

<Accordion title="Sample Request Body">
  ```json  theme={null}
  {
    "type": "email.bounced",
    "created_at": "2024-11-22T23:41:12.126Z",
    "data": {
      "broadcast_id": "8b146471-e88e-4322-86af-016cd36fd216",
      "created_at": "2024-11-22T23:41:11.894719+00:00",
      "email_id": "56761188-7520-42d8-8898-ff6fc54ce618",
      "from": "Acme <onboarding@resend.dev>",
      "to": ["delivered@resend.dev"],
      "subject": "Sending this example",
      "template_id": "43f68331-0622-4e15-8202-246a0388854b",
      "bounce": {
        "message": "The recipient's email address is on the suppression list because it has a recent history of producing hard bounces.",
        "subType": "Suppressed",
        "type": "Permanent"
      },
      "tags": {
        "category": "confirm_email"
      }
    }
  }
  ```
</Accordion>

### `email.opened`

Occurs whenever the **recipient opened the email**.

<Accordion title="Sample Request Body">
  ```json  theme={null}
  {
    "type": "email.opened",
    "created_at": "2024-02-22T23:41:12.126Z",
    "data": {
      "broadcast_id": "8b146471-e88e-4322-86af-016cd36fd216",
      "created_at": "2024-02-22T23:41:11.894719+00:00",
      "email_id": "56761188-7520-42d8-8898-ff6fc54ce618",
      "from": "Acme <onboarding@resend.dev>",
      "to": ["delivered@resend.dev"],
      "subject": "Sending this example",
      "template_id": "43f68331-0622-4e15-8202-246a0388854b",
      "tags": {
        "category": "confirm_email"
      }
    }
  }
  ```
</Accordion>

### `email.clicked`

Occurs whenever the **recipient clicks on an email link**.

<Accordion title="Sample Request Body">
  ```json  theme={null}
  {
    "type": "email.clicked",
    "created_at": "2024-11-22T23:41:12.126Z",
    "data": {
      "broadcast_id": "8b146471-e88e-4322-86af-016cd36fd216",
      "created_at": "2024-11-22T23:41:11.894719+00:00",
      "email_id": "56761188-7520-42d8-8898-ff6fc54ce618",
      "from": "Acme <onboarding@resend.dev>",
      "to": ["delivered@resend.dev"],
      "click": {
        "ipAddress": "122.115.53.11",
        "link": "https://resend.com",
        "timestamp": "2024-11-24T05:00:57.163Z",
        "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"
      },
      "subject": "Sending this example",
      "template_id": "43f68331-0622-4e15-8202-246a0388854b",
      "tags": {
        "category": "confirm_email"
      }
    }
  }
  ```
</Accordion>

### `email.received`

Occurs whenever Resend **successfully receives an email**.

<Accordion title="Sample Request Body">
  ```json  theme={null}
  {
    "type": "email.received",
    "created_at": "2024-02-22T23:41:12.126Z",
    "data": {
      "email_id": "56761188-7520-42d8-8898-ff6fc54ce618",
      "created_at": "2024-02-22T23:41:11.894719+00:00",
      "from": "Acme <onboarding@resend.dev>",
      "to": ["delivered@resend.dev"],
      "bcc": [],
      "cc": [],
      "message_id": "<example+123>",
      "subject": "Sending this example",
      "attachments": [
        {
          "id": "2a0c9ce0-3112-4728-976e-47ddcd16a318",
          "filename": "avatar.png",
          "content_type": "image/png",
          "content_disposition": "inline",
          "content_id": "img001"
        }
      ]
    }
  }
  ```
</Accordion>

### `email.failed`

Occurs whenever the **email failed to send due to an error**.

This event is triggered when there are issues such as invalid recipients, API key problems, domain verification issues, email quota limits, or other sending failures.

<Accordion title="Sample Request Body">
  ```json  theme={null}
  {
    "type": "email.failed",
    "created_at": "2024-11-22T23:41:12.126Z",
    "data": {
      "broadcast_id": "8b146471-e88e-4322-86af-016cd36fd216",
      "created_at": "2024-11-22T23:41:11.894719+00:00",
      "email_id": "56761188-7520-42d8-8898-ff6fc54ce618",
      "from": "Acme <onboarding@resend.dev>",
      "to": ["delivered@resend.dev"],
      "subject": "Sending this example",
      "template_id": "43f68331-0622-4e15-8202-246a0388854b",
      "failed": {
        "reason": "reached_daily_quota"
      },
      "tags": {
        "category": "confirm_email"
      }
    }
  }
  ```
</Accordion>

### `contact.created`

Occurs whenever a **contact was successfully created**.

*Note: When importing multiple contacts using CSV, these events won't be triggered. [Contact support](https://resend.com/contact) if you have any questions.*

<Accordion title="Sample Request Body">
  ```json  theme={null}
  {
    "type": "contact.created",
    "created_at": "2024-11-17T19:32:22.980Z",
    "data": {
      "id": "e169aa45-1ecf-4183-9955-b1499d5701d3",
      "audience_id": "78261eea-8f8b-4381-83c6-79fa7120f1cf",
      "segment_ids": ["78261eea-8f8b-4381-83c6-79fa7120f1cf"],
      "created_at": "2024-11-17T19:32:22.980Z",
      "updated_at": "2024-11-17T19:32:22.980Z",
      "email": "steve.wozniak@gmail.com",
      "first_name": "Steve",
      "last_name": "Wozniak",
      "unsubscribed": false
    }
  }
  ```
</Accordion>

### `contact.updated`

Occurs whenever a **contact was successfully updated**.

<Accordion title="Sample Request Body">
  ```json  theme={null}
  {
    "type": "contact.updated",
    "created_at": "2024-10-11T23:47:56.678Z",
    "data": {
      "id": "e169aa45-1ecf-4183-9955-b1499d5701d3",
      "audience_id": "78261eea-8f8b-4381-83c6-79fa7120f1cf",
      "segment_ids": ["78261eea-8f8b-4381-83c6-79fa7120f1cf"],
      "created_at": "2024-10-10T15:11:94.110Z",
      "updated_at": "2024-10-11T23:47:56.678Z",
      "email": "steve.wozniak@gmail.com",
      "first_name": "Steve",
      "last_name": "Wozniak",
      "unsubscribed": false
    }
  }
  ```
</Accordion>

### `contact.deleted`

Occurs whenever a **contact was successfully deleted**.

<Accordion title="Sample Request Body">
  ```json  theme={null}
  {
    "type": "contact.deleted",
    "created_at": "2024-11-17T19:32:22.980Z",
    "data": {
      "id": "e169aa45-1ecf-4183-9955-b1499d5701d3",
      "audience_id": "78261eea-8f8b-4381-83c6-79fa7120f1cf",
      "segment_ids": ["78261eea-8f8b-4381-83c6-79fa7120f1cf"],
      "created_at": "2024-11-10T15:11:94.110Z",
      "updated_at": "2024-11-17T19:32:22.980Z",
      "email": "steve.wozniak@gmail.com",
      "first_name": "Steve",
      "last_name": "Wozniak",
      "unsubscribed": false
    }
  }
  ```
</Accordion>

### `domain.created`

Occurs when a **domain was successfully created**.

<Accordion title="Sample Request Body">
  ```json  theme={null}
  {
    "type": "domain.created",
    "created_at": "2024-11-17T19:32:22.980Z",
    "data": {
      "id": "d91cd9bd-1176-453e-8fc1-35364d380206",
      "name": "example.com",
      "status": "not_started",
      "created_at": "2024-04-26T20:21:26.347412+00:00",
      "region": "us-east-1",
      "records": [
        {
          "record": "SPF",
          "name": "send",
          "type": "MX",
          "ttl": "Auto",
          "status": "not_started",
          "value": "feedback-smtp.us-east-1.amazonses.com",
          "priority": 10
        },
        {
          "record": "SPF",
          "name": "send",
          "value": "\"v=spf1 include:amazonses.com ~all\"",
          "type": "TXT",
          "ttl": "Auto",
          "status": "not_started"
        },
        {
          "record": "DKIM",
          "name": "resend._domainkey",
          "value": "p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDsc4Lh8xilsngyKEgN2S84+21gn+x6SEXtjWvPiAAmnmggr5FWG42WnqczpzQ/mNblqHz4CDwUum6LtY6SdoOlDmrhvp5khA3cd661W9FlK3yp7+jVACQElS7d9O6jv8VsBbVg4COess3gyLE5RyxqF1vYsrEXqyM8TBz1n5AGkQIDAQA2",
          "type": "TXT",
          "status": "not_started",
          "ttl": "Auto"
        }
      ]
    }
  }
  ```
</Accordion>

### `domain.updated`

Occurs when a **domain was successfully updated**.

<Note>
  The `data.status` field represents an aggregated status of the domain. For
  domains that can both [send](/dashboard/emails/introduction) and
  [receive](/dashboard/receiving/introduction) emails, the status may be
  `partially_failed`, which indicates that one of these features is verified
  while the other is not.
</Note>

<Accordion title="Sample Request Body">
  ```json  theme={null}
  {
    "type": "domain.updated",
    "created_at": "2024-11-17T19:32:22.980Z",
    "data": {
      "id": "d91cd9bd-1176-453e-8fc1-35364d380206",
      "name": "example.com",
      "status": "not_started",
      "created_at": "2024-04-26T20:21:26.347412+00:00",
      "region": "us-east-1",
      "records": [
        {
          "record": "SPF",
          "name": "send",
          "type": "MX",
          "ttl": "Auto",
          "status": "not_started",
          "value": "feedback-smtp.us-east-1.amazonses.com",
          "priority": 10
        },
        {
          "record": "SPF",
          "name": "send",
          "value": "\"v=spf1 include:amazonses.com ~all\"",
          "type": "TXT",
          "ttl": "Auto",
          "status": "not_started"
        },
        {
          "record": "DKIM",
          "name": "resend._domainkey",
          "value": "p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDsc4Lh8xilsngyKEgN2S84+21gn+x6SEXtjWvPiAAmnmggr5FWG42WnqczpzQ/mNblqHz4CDwUum6LtY6SdoOlDmrhvp5khA3cd661W9FlK3yp7+jVACQElS7d9O6jv8VsBbVg4COess3gyLE5RyxqF1vYsrEXqyM8TBz1n5AGkQIDAQA2",
          "type": "TXT",
          "status": "not_started",
          "ttl": "Auto"
        },
        {
          "name": "inbound.yourdomain.tld",
          "priority": 10,
          "record": "Receiving MX",
          "status": "pending",
          "ttl": "Auto",
          "type": "MX",
          "value": "inbound-smtp.us-east-1.amazonaws.com"
        }
      ]
    }
  }
  ```
</Accordion>

### `domain.deleted`

Occurs when a **domain was successfully deleted**.

<Accordion title="Sample Request Body">
  ```json  theme={null}
  {
    "type": "domain.deleted",
    "created_at": "2024-11-17T19:32:22.980Z",
    "data": {
      "id": "d91cd9bd-1176-453e-8fc1-35364d380206",
      "name": "example.com",
      "status": "not_started",
      "created_at": "2024-04-26T20:21:26.347412+00:00",
      "region": "us-east-1",
      "records": [
        {
          "record": "SPF",
          "name": "send",
          "type": "MX",
          "ttl": "Auto",
          "status": "not_started",
          "value": "feedback-smtp.us-east-1.amazonses.com",
          "priority": 10
        },
        {
          "record": "SPF",
          "name": "send",
          "value": "\"v=spf1 include:amazonses.com ~all\"",
          "type": "TXT",
          "ttl": "Auto",
          "status": "not_started"
        },
        {
          "record": "DKIM",
          "name": "resend._domainkey",
          "value": "p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDsc4Lh8xilsngyKEgN2S84+21gn+x6SEXtjWvPiAAmnmggr5FWG42WnqczpzQ/mNblqHz4CDwUum6LtY6SdoOlDmrhvp5khA3cd661W9FlK3yp7+jVACQElS7d9O6jv8VsBbVg4COess3gyLE5RyxqF1vYsrEXqyM8TBz1n5AGkQIDAQA2",
          "type": "TXT",
          "status": "not_started",
          "ttl": "Auto"
        }
      ]
    }
  }
  ```
</Accordion>

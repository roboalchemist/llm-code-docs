# Source: https://developers-classic.mailerlite.com/docs/webhooks.md

# Webhooks

## Introduction

Webhooks allow you to subscribe to real-time notifications about various events that occur in MailerLite. For example, when a new subscriber is added to your account, HTTP POST callback is sent to your provided URL with a payload containing the new subscriber. It allows you to get the most recent updates without constantly polling the API.

## Setup

Currently, you can only create subscriptions using our RESTful API for webhooks. It is documented [here](https://developers-classic.mailerlite.com/reference/get-webhooks-list).

## Payload

Our responses contain fat payloads including the information about the event-related object so there is no need to make an additional API request.

```json
{
  "events": [
      {
        "account_id": 334443,
        "data": {
          "subscriber": {
            "clicked": 0,
            "date_created": "2017-05-23 14:50:03",
            "date_subscribe": null,
            "date_unsubscribe": null,
            "date_updated": null,
            "email": "randomguy+wh1@mailerlite.com",
            "fields": [
              {
                "key":"email",
                "value":"randomguy+wh1@mailerlite.com",
                "type":"TEXT"
              },
              {
                "key":"name",
                "value":"Guy",
                "type":"TEXT"
              },
              {
                "key":"last_name",
                "value":"Random",
                "type":"TEXT"
              }
            ],
            "id": 2300951083,
            "name": "Guy",
            "opened": 0,
            "sent": 0,
            "type": "active"
          }
        },
        "timestamp": 1495551003,
        "type": "subscriber.create",
        "webhook_id": 2
      }
  ]
}
```

## Available events

| Event                              | Description                                                       |
| :--------------------------------- | :---------------------------------------------------------------- |
| subscriber.create                  | Fired when a new subscriber is added to an account.               |
| subscriber.active                  | Fired when an unconfirmed subscriber confirms their subscription. |
| subscriber.update                  | Fired when any of the subscriber's custom fields are updated.     |
| subscriber.unsubscribe             | Fired when a subscriber becomes unsubscribed.                     |
| subscriber.add\_to\_group          | Fired when a subscriber is added to a group.                      |
| subscriber.remove\_from\_group     | Fired when a subscriber is removed from a group.                  |
| subscriber.added\_through\_webform | Fired when a subscriber is added though a form.                   |
| subscriber.bounced                 | Fired when an email address bounces.                              |
| subscriber.complaint               | Fired when subscriber marks a campaign as a spam.                 |
| subscriber.automation\_triggered   | Fired when subscriber starts automation.                          |
| subscriber.automation\_complete    | Fired when subscriber finishes automation.                        |
| campaign.sent                      | Fired when campaign is sent.                                      |

## Batching events

We send events in batches every minute. For example, if there are a few events fired and they belong to the same webhook, we group all of them and send a single HTTP request instead of multiple requests to the same URL.

## Security

Webhook requests include `X-MailerLite-Signature` header, its value is base64 encoded HMAC (sha256) which is generated from payload JSON using your account's API key as a secret key. You can check its validity in order to be guaranteed that a request is sent from our side.

An example of a working function which produces a signature in PHP:

```php
<?php

function generateSignature($jsonPayload, $apiKey) {
  return base64_encode(
    hash_hmac('sha256', $jsonPayload, $apiKey, true)
  ); 
}
```

## Retry

If there is any other response than 2xx from your webhook's endpoint, we attempt to retry our callbacks for a while. However, your webhook is set to inactive after 3 days of responding with an error.

## Unsubscribing webhooks

You can manually stop subscribing events for a particular webhook by using API or just responding with a status code 410.

## Useful tools

[Requestbin](http://requestbin.com)  is a useful tool for testing webhooks quickly and seeing how it works without any coding on your side to see what's being sent.
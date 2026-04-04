# Source: https://www.cosmicjs.com/docs/api/webhooks.md

# Webhooks

Learn about webhooks; used to create automation workflows when you create, update, and delete content using the Cosmic dashboard and API.

## Creating webhooks

Go to Bucket Settings > Webhooks to create a new webhook. Give your webhook a URL, title, properties to return, custom headers, and select the events you want to listen for on a given resource. See the [dashboard reference for webhooks](/docs/dashboard/buckets#webhooks) for more information on creating webhooks in the dashboard.

When webhooks are activated, whenever an event happens in the dashboard or API, a webhook is sent by Cosmic to the indicated URL as a `POST` request. See section below for possible event types and payload example.

---

## The webhook model

The webhook response model contains all the information about the webhook response.

### Properties

The resource that received the action.

Options `objects | media`

The event that occured.

Options `created | edited | deleted`

The time the event was triggered (in UTC milliseconds).

The payload that you define in the dashboard using `props`. Optional.

---

## Consuming webhooks

When your app receives a webhook request from Cosmic, check the `resource` and `event` property to see what event occured.

### Using props

You can specify which `props` you would like to include in the `data` property (if
any). For example, this is the payload you would receive when a new object is created
and published with the `props` of `slug,title,type,status,metadata` included.
```json {{ 'title': 'Example payload' }}
{
  "resource": "objects",
  "event": "created",
  "triggered_at": 1576861549889,
  "data": {
    "object": {
      "slug": "cosmic-webhooks-rock",
      "title": "Cosmic webhooks rock",
      "type": "blog-posts",
      "status": "published",
      "metadata": {
        "content": "<p>Cosmic webhooks enable me to communicate with third-party APIs automatically when I update content in my Cosmic Bucket, sweet!</p>",
        "headline": "Cosmic webhooks are AMAZING!",
        "emoji": "🚀"
      }
    }
  }
}

```
---

## Custom headers

You can also include custom headers to send any custom information, or for an added layer of security. For example, when verifying the request using a secret key.
```js
const secret = req.headers['super-secret-key'];

if (secret === process.env.SUPER_SECRET_KEY) {
  // Request is verified
} else {
  // Request could not be verified
}

```
If the `super-secret-key` value in the custom header you created matches the one in your environment variable you can be sure that the request was truly coming from Cosmic.

## Testing webhooks

You can use a service like [Beeceptor](https://beeceptor.com/) to test your webhooks and view response data.
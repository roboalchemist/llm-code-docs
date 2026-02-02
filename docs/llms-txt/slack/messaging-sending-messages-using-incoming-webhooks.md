# Sending messages using incoming webhooks

Incoming webhooks are a way to post messages from apps into Slack. Creating an incoming webhook gives you a unique URL to which you send a [JSON](https://en.wikipedia.org/wiki/JSON) payload with the message text and some options. You can use all the usual [formatting](/messaging/formatting-message-text) and [layout blocks](/messaging#complex_layouts) with incoming webhooks to make the messages stand out.

If you're looking for the Help Center article on using webhooks with Workflow Builder, [head over here](https://slack.com/help/articles/360041352714). Otherwise, read on!

---

## Getting started with incoming webhooks

We're going to walk through a 4-step process (if you've already done some of these things it'll be even easier) that will have you posting messages using incoming webhooks in just a few minutes:

### 1. Create a Slack app (if you don't have one already)

[Create an app](https://api.slack.com/apps?new_app=1)

Pick a name, choose a workspace to associate your app with (bear in mind you'll probably be posting lots of test messages, so you may want to create a channel for sandbox use), then click **Create App**. If you've already created an app, you can use that one. Have a treat for being prepared! 🍪

### 2. Enable incoming webhooks

You'll be redirected to the settings page for your new app (if you're using an existing app, you can load its settings via your [app's management dashboard](https://api.slack.com/apps)).

From here, select **Incoming Webhooks**, and toggle **Activate Incoming Webhooks** to on. If you already have this activated, well, you deserve another treat! 🍪

### 3. Create an incoming webhook

Now that incoming webhooks are enabled, the settings page should refresh and some additional options will appear. One of those options is a very helpful button called **Add New Webhook to Workspace** — click it!

What this button does is trigger a shortcut version of the installation flow for Slack apps, one that is completely self-contained so that you don't have to actually build any code to generate an incoming webhook URL. We'll [show how you can generate webhooks programmatically later](#incoming_webhooks_programmatic), but for now, you'll see something like the following:

![Permissions screen with incoming webhooks channel selector](https://slack.dev/img/guides/incoming_webhooks_permissions_screen.png)

Go ahead and pick a channel that the app will post to, then select **Authorize**. If you need to add the incoming webhook to a private channel, you must first be in that channel.

You'll be sent back to your app settings, where you should see a new entry under the **Webhook URLs for Your Workspace** section. Your webhook URL will look something like this:

```http
https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX
```

That URL is your shiny new incoming webhook, one that's specific to a single user and a single channel.

#### For GovSlack devs

If you're developing a [GovSlack](/govslack) app for use by public sector customers, make your API calls to the `slack-gov.com` domain instead of the `slack.com` domain.

Let's see how you can actually use that webhook to post a message.

#### Keep it secret, keep it safe

Your webhook URL contains a secret. Don't share it online, including via public version control repositories. **Slack actively searches out and revokes leaked secrets.**

### 4. Use your incoming webhook URL to post a message

Later in this doc we'll explain [how to make your messages more expressive or interactive](#advanced_message_formatting), but for right now anything will do, so we're going to use that old standby — "Hello, world".

Make an HTTP POST request like this:

```http
POST https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX
Content-type: application/json
{
    "text": "Hello, world."
}
```

The URL that you're making the POST request to should be the same URL you generated in the previous step.

That's it! Go and check the channel your app was installed into, and you'll see that the "Hello, World" message has been posted by your app.

You can use this in a real Slack app without much change, just substitute your favorite HTTP Request library for cURL and structure all the requests in the exact same way. You'll also need to pay attention to some details [we've outlined below](#incoming_webhooks_programmatic) when you're distributing your app.

#### Incoming webhooks do not allow you to delete a message after it's been posted.

If you need a more complex chat flow including message deletion, call [`chat.postMessage`](/reference/methods/chat.postMessage).

Great work, you've set up incoming webhooks for your Slack app and made a successful test call, and you're ready to start making those messages more interesting and useful. We baked some extra treats to celebrate! 🍪🍪🍪🍪

---

## Making it fancy with advanced formatting

Incoming webhooks conform to the same rules and functionality as any of our other messaging APIs. You can make your posted messages just a single line of text, or use [interactive components](/messaging/creating-interactive-messages).

<video autoplay loop muted playsinline style="width:100%">[Video Example](/img/guides/buttons_simple_example.mp4)</video>

The process of using all these extras and features is similar to [the one explained above](#posting_with_webhooks). The only difference is the JSON payload that you send to your webhook URL will contain other fields in addition to `text`. Here's a more advanced HTTP request example that you can use with the same webhook `url` that you [used above](#posting_with_webhooks):

```http
POST https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX
Content-type: application/json
{
    "text": "Danny Torrence left a 1 star review for your property.",
    "blocks": [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Danny Torrence left the following review for your property:"
            }
        },
        {
            "type": "section",
            "block_id": "section567",
            "text": {
                "type": "mrkdwn",
                "text": "<https://example.com|Overlook Hotel> \n :star: \n Doors had too many axe holes, guest in room 237 was far too rowdy, whole place felt stuck in the 1920s."
            },
            "accessory": {
                "type": "image",
                "image_url": "https://is5-ssl.mzstatic.com/image/thumb/Purple3/v4/d3/72/5c/d3725c8f-c642-5d69-1904-aa36e4297885/source/256x256bb.jpg",
                "alt_text": "Haunted hotel image"
            }
        },
        {
            "type": "section",
            "block_id": "section789",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": "*Average Rating*\n1.0"
                }
            ]
        }
    ]
}
```

This example uses [Block Kit](/block-kit) visual components to make the message more expressive and
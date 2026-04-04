Source: https://docs.slack.dev/changelog/2018/12/01/a-bric-a-brac-of-broadcasts-built-with-blocks

# A bric a brac of broadcasts built with blocks

December 1, 2018

The data structure that represents a message now contains additional new fields on top of all [the existing fields](/reference/events/message) your app may be currently expecting. The new structure took effect on February 13, 2019.

These changes come with Block Kit—a new set of components for Slack apps that can be combined to create visually rich and compellingly interactive messages. You can read more about Block Kit [below](#block-preview).

Even if you aren't using Block Kit to compose messages, its launch still affects the data structure of messages _received_ via our APIs, so read on to learn how to prepare your apps.

## What's changing? {#what}

Blocks now appear in the data structure of messages retrieved via APIs like [`conversations.history`](/reference/methods/conversations.history) or sent via the [Events API](/apis/events-api/#event_types).

## What do blocks look like? {#block-preview}

Block Kit gives Slack apps more visual flexibility and more control over message layout and structure. Here's an example of the kind of message that developers can compose with blocks:

![Screenshot of an app published message composed of multiple blocks](/assets/images/block_kit_changelog_preview-57c688c62b02ddf45ceb7fc7547543bc.png)

Blocks also introduce more [interactive options](/legacy/legacy-messaging/legacy-making-messages-interactive) for app developers. They provide visually cleaner ways to incorporate [buttons](/legacy/legacy-messaging/legacy-message-buttons) or [menus](/legacy/legacy-messaging/legacy-adding-menus-to-messages), as well as new interactive elements like date pickers or overflow menus.

Check out the [Block Kit documentation](/block-kit) for how-to guides and reference material.

## How do I prepare? {#how}

A message that includes any blocks now carries a new field, called `blocks`. Depending on how your app is built, you might need to change it to accommodate this new field.

The `blocks` field is an array of block objects, and can be included at the 'top-level' of a message structure, or within the existing `attachments` field.

Here's the JSON that could be used to construct the message with the blocks shown in [the screenshot above](#block-preview), showing `blocks` at the top-level of a message:

```json
{  "channel": "C1H9RESGL",  "blocks": [    {      "type": "section",      "block_id": "section295439417",      "text": {        "type": "mrkdwn",        "text": "Hello, Wally!\n*André* wants to know where you'd like to have dinner tonight. Please select a restaurant:"      }    },    {      "type": "section",      "block_id": "section42177494",      "text": {        "type": "mrkdwn",        "text": "*Café des Artistes*\n:star::star::star::star: 1528 reviews\n Excellent location for a long conversation with friends and a few glasses of wine. They have something for everyone here."      },      "accessory": {        "type": "image",        "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/c7ed05m9lC2EmA3Aruue7A/o.jpg",        "alt_text": "alt text for image"      }    },    {      "type": "section",      "block_id": "section205112062",      "text": {        "type": "mrkdwn",        "text": "*Kin Khao*\n:star::star::star: 1638 reviews\n The sticky rice goes wonderfully with the caramelized pork belly, which is absolutely melt-in-your-mouth and so soft."      },      "accessory": {        "type": "image",        "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/korel-1YjNtFtJlMTaC26A/o.jpg",        "alt_text": "alt text for image"      }    },    {      "type": "section",      "block_id": "section573300221",      "text": {        "type": "mrkdwn",        "text": "*Ler Ros*\n:star::star::star: 2082 reviews\n I would really recommend the Yum Koh Moo Yang - Spicy lime dressing and roasted quick marinated pork shoulder, basil leaves, chili & rice powder."      },      "accessory": {        "type": "image",        "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/DawwNigKJ2ckPeDeDM7jAg/o.jpg",        "alt_text": "alt text for image"      }    },    {      "type": "actions",      "block_id": "actions521633010",      "elements": [        {          "type": "button",          "text": {            "type": "plain_text",            "text": "Café des Artistes",            "emoji": true          },          "value": "click_me_123",          "action_id": "button47806181"        },        {          "type": "button",          "text": {            "type": "plain_text",            "text": "Kin Khao",            "emoji": true          },          "value": "click_me_123",          "action_id": "button306887175"        },        {          "type": "button",          "text": {            "type": "plain_text",            "text": "Ler Ros",            "emoji": true          },          "value": "click_me_123",          "action_id": "button567254933"        }      ]    }  ]}
```text

And here's an example of `blocks` being included inside an `attachments` field:

```json
{    "text": "I am a test message http://slack.com",    "attachments": [      {        "blocks": [          {            "type": "image",            "title": {              "type": "plain_text",              "text": "Hang in there"            },            "block_id": "image575160834",            "image_url": "https://images.pexels.com/photos/257532/pexels-photo-257532.jpeg",            "alt_text": "hang_in_there"          }        ]      }    ]}
```text

These examples show some of the available blocks, but your app only needs to be prepared for the existence of the `blocks` array. Further details about each of the block objects, and the fields within them, can be found in the [Block Kit documentation](/block-kit).

## What if I do nothing? {#nothing}

If your app doesn't _receive_ messages, either directly via a Web API like [`conversations.history`](/reference/methods/conversations.history) or indirectly when it gets pings from the [Events API](/apis/events-api/#event_types), then nothing is exactly what you should do!

If it _does_ receive messages, then your code might be assuming a specific format or structure of JSON response, and the addition of the `blocks` field could cause some code comprehension consternation.

If your app only _publishes_ messages, don't worry - Block Kit is an additive change, and doesn't break any existing message composition options.

## When does this happen? {#when}

Block Kit has officially launched! [Read more about the new features available within the land of blocks](/block-kit).

Keep an eye on the [main changelog](/changelog) for more updates about Block Kit.

## Tags:

* [New feature](/changelog/tags/new-feature)
* [Breaking change](/changelog/tags/breaking-change)

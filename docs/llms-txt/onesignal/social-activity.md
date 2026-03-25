# Source: https://documentation.onesignal.com/docs/en/social-activity.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Social Activity

> Learn how to use OneSignal to send push notifications for social actions like likes, follows, and invites, as well as for user-to-user direct messages.

Use OneSignal to notify users about social activity (likes, follows, invites) and user messages. These alerts can drive re-engagement even when users aren't currently active in your app.

<Warning>
  OneSignal and push notifications are not designed explicitly for real-time communication. They are best used as a fallback when both users are not active on your app.

  For real-time communication, consider dedicated live chat solutions such as:

* [XMPP](https://xmpp.org/)
* [Stream](https://getstream.io/chat/)
* [Firebase Realtime Database](https://firebase.google.com/products/database)
</Warning>

***

## Social activity notifications

Trigger a push notification when a user is involved in social actions.

### Common social actions

| Action  | Example message                        |
| ------- | -------------------------------------- |
| Like    | “Anna liked your post.”                |
| Mention | “Leo mentioned you in a comment.”      |
| Tag     | “Sara tagged you in a photo.”          |
| Invite  | “Ben invited you to the event.”        |
| Comment | “Maya replied: ‘Looks awesome!’”       |
| Follow  | “James started following you.”         |
| Share   | “Alex shared ‘Hawaii Album’ with you.” |

### Requirements

* A backend or CRM that tracks user activity and relationships.
  * [Integration](./integrations)
  * [Database, DMP, & CRM integration](./database-dmp-crm-integration)
* External IDs set in OneSignal to identify users.
* Using our [Create Notification API](/reference/create-message).

### Setup

#### 1. Map users with External ID

Use [Aliases & External ID](./users) to uniquely identify users in OneSignal.

#### 2. Detect the social action

In your backend, track who performed the action and who it affects.

```json json theme={null}
{
  "action": "like",
  "actor_id": "user_b",
  "recipient_id": "user_a",
  "post_id": "xyz789"
}
```

#### 3. Send a push notification

Use the OneSignal API to notify the recipient:

```json  theme={null}
{
  "app_id": "YOUR_APP_ID",
  "contents": { "en": "user_b liked your photo." },
  "include_aliases": { "external_id": ["user_a"] }
}
```

### Add-ons

* Use [Message Personalization](./message-personalization) to insert custom data like usernames, post titles, images, and more!
* Display a history of social alerts using an [Activity Feed](./create-an-activity-feed).

***

## Direct (user-to-user) messages

Let users know they have a new message and optionally include message content or a deep link to the chat.

<Warning> Push notifications are best used as a fallback when both users are not actively chatting in the app. </Warning>
Send a push when User A sends a message to User B, and B is not currently online or in the chat screen.

### Setup

#### 1. Map users with External ID

Use [Aliases & External ID](./users) to uniquely identify users in OneSignal.

#### 2. Trigger a notification on message send

From your backend, send a push to the recipient using the [Create Notification API](/reference/push-notification) with the `include_aliases` field:

```json  theme={null}
{
  "include_aliases": {
    "external_id": ["USER_B_ID"]
  },
  "contents": { "en": "New message from Anna: 'Hey, you around?'" },
  "headings": { "en": "New Message" },
  "data": {
    "sender_id": "user_a",
    "conversation_id": "chat_1234",
    "click_action": "open_chat"
  }
}

```

### Best practices

* Avoid spamming: Don’t send a notification for every single message. Use batching or only alert after X minutes of inactivity.
* Respect user settings: Let users mute or disable message notifications if needed.
* Use routing logic in your app to open the conversation. See [Deep Linking](./deep-linking) for more information.

***

## Related articles

* [Create an Activity Feed](./create-an-activity-feed)
* [Deep Linking](./deep-linking)
* [Message Personalization](./message-personalization)
* [Transactional Messages](./transactional-messages)

***

Built with [Mintlify](https://mintlify.com).

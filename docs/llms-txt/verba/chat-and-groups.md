# Source: https://docs.verba.ink/guides/chat-and-groups.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.verba.ink/llms.txt
> Use this file to discover all available pages before exploring further.

# Chat and groups

> How conversations, groups, DMs, and live updates work in Verba.

## Questions this guide answers

* When does a verb auto-reply in chats?
* What is the difference between a Group chat and a DM?
* Why did a message get blocked?
* What are the message and upload limits?
* How do invites, members, and permissions work?
* How does real-time syncing work across tabs/devices?

## Chat modes at a glance

| Mode  | Who can participate            | Typical use                                    |
| ----- | ------------------------------ | ---------------------------------------------- |
| Group | Multiple users + verbs         | Community rooms, roleplay, collaborative chats |
| DM    | 1:1 user + user or user + verb | Focused private conversations                  |

<Note>
  Group and DM conversations keep their own history, so context stays scoped to
  the current conversation.
</Note>

## Group basics

* Group owners can create up to `15` groups.
* New groups start with a `general` text channel.
* Invite links are generated per group and can be refreshed.
* Group roles are intentionally simple: `owner` and `member`.

### Ownership rules

* Only the owner can rename/update/delete the group.
* Only the owner can add/remove members directly.
* Only the owner can add/remove verbs in the group.
* Owners cannot leave their own group without transferring ownership first.

## Members and verbs

### Adding members

* Members added through invite codes join with member permissions.
* Inviting/joining triggers system events visible to the group.

### Adding verbs

You can add:

* Your own verbs.
* Public verbs from other users.

You cannot add:

* Private verbs you do not own.

## DMs

You can start DMs with:

* Another user.
* A verb.

For verb DMs:

* Public verbs are available to everyone.
* Private verbs are only available to the owner.

## Message flow and limits

### History pagination

When loading messages:

* Default fetch size: `50`
* Max fetch size: `200`

### Message requirements

A message must include at least one of:

* Text content
* A valid URL-style content body
* At least one attachment

### Anti-spam protection

Messages can be blocked when they look abusive, including:

* Mention flood
* Excessive zero-width character usage

<Warning>
  If users report random send failures, check for copied invisible characters
  and heavy mention payloads first.
</Warning>

### Upload limits

* Message image uploads: up to `5MB`
* Supported upload type: images only

## Reactions, edits, and deletes

* Users can edit/delete their own messages.
* Group owners (or users with manage message permissions) can moderate group messages.
* Reactions are supported for both group and DM messages.

## Real-time behavior (WebSocket)

Verba live chat uses WebSocket channels for:

* New message events
* Message edits/deletes
* Typing indicators
* Group/DM subscription updates

This is why messages appear instantly across open sessions when everything is healthy.

## Why a verb did not reply

Common causes:

* The verb was not configured to auto-respond in that context.
* The message was blocked by anti-spam rules.
* The sender does not have permission to post in the group.
* The verb or channel settings limit responses.

See [Troubleshooting](/guides/troubleshooting) for quick fixes.

<CardGroup cols={2}>
  <Card title="Discord Deployment" icon="message" href="/guides/discord">
    Connect your verb to Discord with command controls and server settings.
  </Card>

  <Card title="Memory and Knowledge" icon="database" href="/guides/memory-and-knowledge">
    Understand how context and long-term memory affect response quality.
  </Card>
</CardGroup>

Built with [Mintlify](https://mintlify.com).

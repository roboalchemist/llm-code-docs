Source: https://docs.slack.dev/changelog/2018-05-file-threads-soon-tread

# File threads soon tread

May 1, 2018

We're fixing file comments and in the process we're phasing out some related API methods and events.

File comments look like messages in a channel but they _aren't_. They travel with files, wherever shared, disrupting conversation at inopportune moments.

We started to gradually roll out _file threads_ on July 23, 2018. Sharing a file with a channel will now create an actual message instead of something that looked convincingly _like_ a message. People and bots may reply to that message as they would any other message. You can even upload files _into_ threads.

## What changed? {#what-changed}

Here is an overview of the changes to expect.

* Files no longer have an associated, global collection of comments or reactions against it.
* Commenting or reacting to files is done on a per-conversation basis.
* As users share files to channels, messages are created and any replies to the file are created as threaded replies.
* Users cannot react to files directly.
* Reactions apply on a per-conversation basis to the message announcing the file (the _file thread parent_) — not to the file itself.
* `files:read` used to be sufficient to read file comments but as comments become messages in a thread, your app **must** be awarded a conversations "history" scope like `channels:history`.
* `files:write` was once adequate to comment on a file but since comments are now messages in a thread, your app **must** be awarded a `chat:write` scope to comment on files.
* The `file` attribute attached to messages is replaced with a new `files` field that includes an array of files in a different format instead.
* The `message` subtype event, `file_share`, will no longer be sent to RTM connections.
* We'll continue sending a [_modified_ form](#file_share) of the event to the Events API.

### Transitioning OAuth scopes {#transitioning-oauth-scopes}

With file comments becoming [threaded messages](/messaging#threading), the `files:read`, `files:write`, and `files:write:user` scopes will no longer be the _right_ scopes for accessing content _about_ files.

To read file message threads, your app or bot will need to "listen" for messages dispatched to the [RTM](/legacy/legacy-rtm-api) and [Events](/apis/events-api/) APIs and/or use methods like [`conversations.replies`](/reference/methods/conversations.replies) with the appropriate related conversation scope like `channels:history`, `groups:history`, `im:history`, and `mpim:history`.

To write to file message threads, your app will need one of `chat:write`, `chat:write:user`, and/or `chat:write:bot` to post messages targeting a thread's `thread_ts`. When using a bot user token, your bot must be a member of the channel its writing messages to. With user tokens, the represented user must be a member of the channel.

## If you don't already have these scopes, you must request users to re-authorize your application and approve them.

Apps in the Slack Marketplace will need to add the scopes to their app and request approval from our review team before requesting the additional scopes.

You may want to begin the process of asking for these new scopes before you _need_ them in July 2018 and beyond.

### Discontinued events {#discontinued-events}

These events are being phased out because file comments won't be created any more.

* `file_comment_added` - look for `message` events in reply to the file's original file message thread parent.
* `file_comment_edited` - `message_changed` events broadcast as users reply to file messages instead.
* `message` event subtype, [`file_mention`](/reference/events/message/file_mention)
* `message` event subtype, [`file_comment`](/reference/events/message/file_comment)
* `message` event subtype, [`file_share`](/reference/events/message/file_share) is discontinued. However, we will continue sending it via the [Events API](/apis/events-api/) until further notice. You'll find a `files` array instead of a single `file` attribute.

### Mutating Web API methods {#shares}

The shape of a [file object](/reference/objects/file-object) changes slightly.

We're phasing out the `channels`, `groups`, and `ims` fields in favor of a more unified `shares` node instead.

## Changes to [`files.info`](/reference/methods/files.info) & [`files.list`](/reference/methods/files.list)

Here's an _abbreviated_ file object in the new model, highlighting `shares`:

```json
{    "ok": true,    "files": [        {            "id": "F0PHJN941",            "created": 1524085964,            "name": "ping.png",            "mimetype": "image/png",            "user": "U061F7AUR",            "shares": {                "public": {                    "C061FA5PB": [                        {                            "reply_users": [],                            "reply_users_count": 0,                            "reply_count": 0,                            "ts": "1524086081.000029"                        }                    ],                    "C061EG9SL": [                        {                            "reply_users": [                                "U061F7AUR"                            ],                            "reply_users_count": 1,                            "reply_count": 1,                            "latest_reply": "1524085983.000010",                            "ts": "1524085969.000036"                        }                    ]                },                "private": {                    "D0PNCRP9N": [                        {                            "reply_users": [],                            "reply_users_count": 0,                            "reply_count": 0,                            "ts": "1524086053.000018"                        }                    ]                }            },            "channels": [                "C061FA5PB",                "C061EG9SL"            ],            "groups": [],            "ims": [                "D0PNCRP9N"            ],            "comments_count": 0        }    ]}
```text

Each share instance comes with:

* `reply_users` - an array of up to 5 user IDs corresponding to the first users having replied to the file thread parent
* `reply_users_count` - an integer value counting the number of replying users
* `reply_count` - the raw integer number of replies to the file thread parent
* `latest_reply` - if the file thread parent has 1 or more replies, points to the most recent message's `ts` value; it is otherwise omitted
* `thread_ts` - if the file was shared into a thread directly, this is the original parent message's `ts` value; it is otherwise omitted
* `ts` - the file thread parent message identifier. Use this as the `thread_ts` value when posting threaded comments, or as the target when adding reactions with [`reactions.add`](/reference/methods/reactions.add)

The above example notes two public channel shares (one with a reply), and a single private channel share.

Up to 50 of the most recent shares are returned in `files.list` and `files.info`.

## Changes coming to [`files.upload`](/reference/methods/files.upload)

Any provided `initial_comment` value will automatically be used as part of the file thread parent message instead of as a file comment.

You can provide a `thread_ts` to upload and share a file directly to an existing thread and `broadcast` to share that reply with a channel, just like using [`chat.postMessage`](/reference/methods/chat.postMessage) in typical [message threads](/messaging#threading).

Responses to `files.upload` will include the [`shares` attribute](#shares), detailing the channel(s) and file thread parent `ts` value. Log the `ts` value to track replies to the newly uploaded file.

## Reactions to files become reactions to file thread parents

You'll find changes to [`reactions.get`](/reference/methods/reactions.get) and [`reactions.list`](/reference/methods/reactions.list), all the consequence of reactions applying to file thread parents instead of globally to a file itself.

## Changes coming to other Web API methods

Any place you'd previously find messages with `file` fields, like when browsing [`conversations.history`](/reference/methods/conversations.history), you'll now find a `files` attribute containing an array instead.

### Discontinued Web API methods {#discontinued-web-api-methods}

During a transition period, these methods will remain quasi-functional with adapted behavior. We encourage you to use [`chat.postMessage`](/reference/methods/chat.postMessage) and [`chat.update`](/reference/methods/chat.update) to work with messages instead.

* `files.comments.add`
* `files.comments.edit`

For a limited time, we'll automatically pipe comments added through this method into _messages_ in reply to the _most recently_ shared file message.

### Events API changes {#file_share}

Some events in both the Events API and RTM APIs will be discontinued; they are going away because what they describe is going away.

For best results, track our supported top-level events like [`file_shared`](/reference/events/file_shared) and [`file_created`](/reference/events/file_created) instead of "message subtypes" like `file_share`.

If you're used to `file_share` and use the Events API, you'll be happy to know we'll continue dispatching this message subtype until further notice. It will no longer be served over RTM.

These retained events, however, are still different in a single way: instead of coming with a `file` attribute, you'll find a `files` array containing one or more leaner file objects inside.

Here's an example:

```json
{        "token": "your-verification-token",        "team_id": "T061EG9R6",        "api_app_id": "A0K0UQXCZ",        "event": {                "type": "message",                "text": "We got one!",                "files": [                        {                                "id": "F0RDC39U1",                                "created": 1529342081,                                "timestamp": 1529342081,                                "name": "ghostrap.png",                                "title": "ghostrap.png",                                "mimetype": "image/png",                                "filetype": "png",                                "pretty_type": "PNG",                                "user": "U061F7AUR",                                "editable": false,                                "size": 196920,                                "mode": "hosted",                                "is_external": false,                                "external_type": "",                                "is_public": false,                                "public_url_shared": false,                                "display_as_bot": false,                                "username": "",                                "url_private": "https://.../ghostrap.png",                                "url_private_download": "https://.../download/ghostrap.png",                                "thumb_64": "https://.../ghostrap_64.png",                                "thumb_80": "https://.../ghostrap_80.png",                                "thumb_360": "https://.../ghostrap_360.png",                                "thumb_360_w": 360,                                "thumb_360_h": 360,                                "thumb_480": "https://.../ghostrap_480.png",                                "thumb_480_w": 480,                                "thumb_480_h": 480,                                "thumb_160": "https://.../ghostrap_160.png",                                "image_exif_rotation": 1,                                "original_w": 512,                                "original_h": 512,                                "pjpeg": "https://.../ghostrap_pjpeg.jpg",                                "permalink": "https://.../ghostrap.png",                                "permalink_public": "https://.../815d735817",                                "has_rich_preview": false                        }                ],                "user": "U061F7AUR",                "upload": true,                "display_as_bot": false,                "bot_id": null,                "ts": "1529342088.000086",                "channel": "D0L4B9P0Q",                "subtype": "file_share",                "event_ts": "1529342088.000086",                "channel_type": "im"        },        "type": "event_callback",        "event_id": "Ev0RDC3U6M",        "event_time": 1529342088,        "authed_users": [                "U0L4B9NSU"        ]}
```text

## What isn't changing? {#what-isnt-changing}

We're making some best-effort, short-term accommodations to help ease the transition — we'll eventually retire them as well.

* `files.comments.add` and `files.comments.edit` will continue to function. Instead of working against _file comments_, they'll adapt to working against the most recently shared file thread message.
* `files.upload`'s `initial_comment` will automatically convert the file comment into a file thread instead, tied to the file thread parent.

## How do I prepare? {#how-do-i-prepare}

If you work with files and/or file comments, here's how to get ready:

Do you write file comments and want to write file thread replies instead? You'll need a `chat:write` (for [workspace apps](/changelog/2021-01-workspace-apps-retiring-the-platform-graveyard-in-aug-2021)), `chat:write:user`, or `chat:write:bot` scope to create messages in reply to file thread parents. `files:write` is no longer enough.

If you work with file comments, adapt your code to work with [threaded messages](/messaging#threading) instead. Consider joining our [pilot program](#pilot_program) for a head start.

## When is this happening? {#when-is-this-happening}

File threads began rolling out on July 23, 2018. Within a few months, we'd like to remove the legacy accordances we've made to preserve the illusion of file comments.

Something amiss? [Let us know](https://slack.com/help/requests/new).

## Pilot program {#pilot_program}

Thank you to the developers that previewed File Threads as we finished readying it for release.

## Tags:

* [Breaking change](/changelog/tags/breaking-change)
* [Announcement](/changelog/tags/announcement)
* [Deprecation](/changelog/tags/deprecation)

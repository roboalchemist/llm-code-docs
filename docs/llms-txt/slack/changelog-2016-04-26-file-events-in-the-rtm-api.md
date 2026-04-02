Source: https://docs.slack.dev/changelog/2016/04/26/file-events-in-the-rtm-api

# RTM API file events payload change

April 26, 2016

If you parse events referencing [files](/reference/objects/file-object) in the [real-time messaging API](/legacy/legacy-rtm-api), you may have noticed we send a sometimes comically large packet of information when streaming nearly anything related to a file.

To improve performance and provide a better user experience, we're reducing the payload of most file-related events in the RTM API to include only the file's ID. You'll need to use the [`files.info`](/reference/methods/files.info) API method to retrieve additional information about files.

These changes will roll out gradually beginning May 16th, 2016 — read below to understand how this change may effect you, especially if you work with bot users.

[Bot users](/legacy/legacy-bot-users) will gain comparable capabilities, allowing bot user tokens to work with `files.info` based on the channel memberships and related capabilities granted to them.

## What's changing: {#whats-changing}

The following Real Time Messaging events will be modified:

* [`file_created`](/reference/events/file_created)
* [`file_shared`](/reference/events/file_shared)
* [`file_unshared`](/reference/events/file_unshared)
* [`file_public`](/reference/events/file_public)
* [`file_change`](/reference/events/file_change)
* `file_comment_added`
* `file_comment_edited`
* `file_comment_deleted`

When pins or stars are applied to or removed from messages containing files, you'll also find this new behavior in these associated events:

* [`star_added`](/reference/events/star_added)
* [`star_removed`](/reference/events/star_removed)
* [`pin_added`](/reference/events/pin_added)
* [`pin_removed`](/reference/events/pin_removed)

### How these events will change {#how-these-events-will-change}

After release, you will receive abbreviated `file` events, with only the `id` attribute:

```json
{    "file_id": "F2147483862",    "type": "file_shared",    "file": {        "id": "F2147483862"    }}
```text

This `id` value may be used with the [`files.info`](/reference/methods/files.info) API method to obtain fresh information about the file it represents. We'll also include a top-level `file_id` field, which you may want to use going forward instead.

Until now, these events would have had more verbose file details included:

```json
{    "type": "file_shared",    "file": {        "id" : "F2147483862",        "created" : 1356032811,        "timestamp" : 1356032811,        "name" : "file.htm",        "title" : "My HTML file",        "mimetype" : "text\/plain",        "filetype" : "text",        "pretty_type": "Text",        "user" : "U2147483697",        "mode" : "hosted",        "editable" : true,        "is_external": false,        "external_type": "",        "username": "",        "size" : 12345,        "url_private": "https:\/\/slack.com\/files-pri\/T024BE7LD-F024BERPE\/1.png",        "url_private_download": "https:\/\/slack.com\/files-pri\/T024BE7LD-F024BERPE\/download\/1.png",        "thumb_64": "https:\/\/slack-files.com\/files-tmb\/T024BE7LD-F024BERPE-c66246\/1_64.png",        "thumb_80": "https:\/\/slack-files.com\/files-tmb\/T024BE7LD-F024BERPE-c66246\/1_80.png",        "thumb_360": "https:\/\/slack-files.com\/files-tmb\/T024BE7LD-F024BERPE-c66246\/1_360.png",        "thumb_360_gif": "https:\/\/slack-files.com\/files-tmb\/T024BE7LD-F024BERPE-c66246\/1_360.gif",        "thumb_360_w": 100,        "thumb_360_h": 100,        "thumb_480": "https:\/\/slack-files.com\/files-tmb\/T024BE7LD-F024BERPE-c66246\/1_480.png",        "thumb_480_w": 480,        "thumb_480_h": 480,        "thumb_160": "https:\/\/slack-files.com\/files-tmb\/T024BE7LD-F024BERPE-c66246\/1_160.png",        "permalink" : "https:\/\/tinyspeck.slack.com\/files\/cal\/F024BERPE\/1.png",        "permalink_public" : "https:\/\/tinyspeck.slack.com\/T024BE7LD-F024BERPE-3f9216b62c",        "edit_link" : "https:\/\/tinyspeck.slack.com\/files\/cal\/F024BERPE\/1.png/edit",        "preview" : "&lt;!DOCTYPE html&gt;\n&lt;html&gt;\n&lt;meta charset='utf-8'&gt;",        "preview_highlight" : "&lt;div class=\"sssh-code\"&gt;&lt;div class=\"sssh-line\"&gt;&lt;pre&gt;&lt;!DOCTYPE html...",        "lines" : 123,        "lines_more": 118,        "is_public": true,        "public_url_shared": false,        "display_as_bot" : false,        "channels": ["C024BE7LT", ...],        "groups": ["G12345", ...],        "ims": ["D12345", ...],        "initial_comment": {...},        "num_stars": 7,        "is_starred": true,        "pinned_to": ["C024BE7LT", ...],        "reactions": [        {            "name": "astonished",            "count": 3,            "users": [ "U1", "U2", "U3" ]        },        {            "name": "facepalm",            "count": 1034,            "users": [ "U1", "U2", "U3", "U4", "U5" ]        }        ],        "comments_count": 1    }}
```text

### Bot users {#bot-users}

Today, some bot users may rely on the current behavior to utilize or index files referenced in the channels they belong to. To support that use case, we will improve the `files.info` method to make it accessible to bot users and scoped only to the files that a bot has access to when using its bot user token.

We'll post a follow up within the next two weeks when we're ready to release these new capabilities.

## How to prepare: {#how-to-prepare}

Review your streaming integration to determine where and when you rely on the full file object being present in events. If you don't need the full file object, consume only the file ID. If you need the full file object, request it using `files.info`.

## When it's happening: {#when-its-happening}

**May 16th, 2016**.

We want to make these improvements as soon as possible, beginning a gradual roll out on May 16th, 2016. If you believe that your application, custom integration, or third party library will outright break or non-gracefully degrade as a result of this change, please let us know immediately so we may work together to make this transition as seamless as possible.

## Tags:

* [Announcement](/changelog/tags/announcement)
* [Breaking change](/changelog/tags/breaking-change)

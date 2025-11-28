# Source: https://developers.google.com/youtube/v3/live/docs/fanFundingEvents.md.txt

# FanFundingEvents

**Note:** This is a deprecation announcement.  

The Fan Funding feature has been deprecated, and the Fan Funding API will be turned off on February 28, 2017. This deprecation announcement coincides with the release of YouTube's new [Super Chat](https://youtube.googleblog.com/2017/01/can-we-chat-hello-super-chat.html) feature.
A **fanFundingEvent** resource represents a Fan Funding event on a YouTube channel. Fan Funding provides a way to monetarily support YouTube creators. A Fan Funding event occurs when a user makes a one-time, voluntary payment to a channel. See the [YouTube Help Center](https://support.google.com/youtube/answer/6052077) to learn more about Fan Funding.

## Methods

The API supports the following methods for `fanFundingEvents` resources:

[list](https://developers.google.com/youtube/v3/live/docs/fanFundingEvents/list)
:   Lists fan funding events for a channel. The API request must be authorized by the channel owner.
    [Try it now](https://developers.google.com/youtube/v3/live/docs/fanFundingEvents/list#try-it).

## Resource representation

The following JSON structure shows the format of a `fanFundingEvents` resource:  

```text
{
  "kind": "youtube#fanFundingEvent",
  "etag": etag,
  "id": string,
  "snippet": {
    "channelId": string,
    "supporterDetails": {
      "channelId": string,
      "channelUrl": string,
      "displayName": string,
      "profileImageUrl": string
    },
    "commentText": string,
    "createdAt": datetime,
    "amountMicros": unsigned long,
    "currency": string,
    "displayString": string
  }
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                                                                                                                                                                                                          Properties                                                                                                                                                                                                                                          ||
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `kind`                                     | `string` Identifies the API resource's type. The value will be `youtube#fanFundingEvent`.                                                                                                                                                                                                                                                                                                                                                        |
| `etag`                                     | `etag` The Etag of this resource.                                                                                                                                                                                                                                                                                                                                                                                                                |
| `id`                                       | `string` The ID that YouTube assigns to uniquely identify the fan funding event.                                                                                                                                                                                                                                                                                                                                                                 |
| `snippet`                                  | `object` The `snippet` object contains information about the fan funding event.                                                                                                                                                                                                                                                                                                                                                                  |
| snippet.`channelId`                        | `string` The ID of the channel that received the funding.                                                                                                                                                                                                                                                                                                                                                                                        |
| snippet.`supporterDetails`                 | `object` Details about the supporter's channel. This object is only present if the supporter made the funding event public.                                                                                                                                                                                                                                                                                                                      |
| snippet.supporterDetails.`channelId`       | `string` The supporter's YouTube channel ID.                                                                                                                                                                                                                                                                                                                                                                                                     |
| snippet.supporterDetails.`channelUrl`      | `string` The URL of the supporter's channel.                                                                                                                                                                                                                                                                                                                                                                                                     |
| snippet.supporterDetails.`displayName`     | `string` The display name of the supporter's channel.                                                                                                                                                                                                                                                                                                                                                                                            |
| snippet.supporterDetails.`profileImageUrl` | `string` The avatar URL for the supporter's channel.                                                                                                                                                                                                                                                                                                                                                                                             |
| snippet.`commentText`                      | `string` The text contents of the supporter's comment.                                                                                                                                                                                                                                                                                                                                                                                           |
| snippet.`createdAt`                        | `datetime` The date and time when the funding occurred. The value is specified in [ISO 8601](https://www.w3.org/TR/NOTE-datetime) (`YYYY-MM-DDThh:mm:ss.sZ`) format.                                                                                                                                                                                                                                                                             |
| snippet.`amountMicros`                     | `unsigned long` The amount of money contributed in the funding event. The value is in micros of the funding currency. For example, if the funder contributed one dollar ($1), the `snippet.amountMicros` property value is `1000000`.                                                                                                                                                                                                            |
| snippet.`currency`                         | `string` The currency associated with the funding amount. The value is an [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code.                                                                                                                                                                                                                                                                                                      |
| snippet.`displayString`                    | `string` A string, intended for display, that shows the fund amount and currency. If the `fanFundingEvents.list` request specified an application language with the [hl](https://developers.google.com/youtube/v3/live/docs/fanFundingEvents/list#hl) parameter, the display string is localized for display in that language. For example, in English, currency would be displayed as `$1.50`, but in French, it would be displayed as `1,50$`. |
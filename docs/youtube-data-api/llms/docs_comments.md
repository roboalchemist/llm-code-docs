# Source: https://developers.google.com/youtube/v3/docs/comments.md.txt

A **comment** resource contains information about a single YouTube comment. A `comment` resource can represent a comment about either a video or a channel. In addition, the comment could be a top-level comment or a reply to a top-level comment.

## Methods

The API supports the following methods for `comments` resources:

[list](https://developers.google.com/youtube/v3/docs/comments/list)
:   Returns a list of comments that match the API request parameters.
    [Try it now](https://developers.google.com/youtube/v3/docs/comments/list#usage).

[insert](https://developers.google.com/youtube/v3/docs/comments/insert)
:   Creates a reply to an existing comment. **Note:** To create a top-level comment, use the [commentThreads.insert](https://developers.google.com/youtube/v3/docs/commentThreads/insert) method.
    [Try it now](https://developers.google.com/youtube/v3/docs/comments/insert#usage).

[update](https://developers.google.com/youtube/v3/docs/comments/update)
:   Modifies a comment.
    [Try it now](https://developers.google.com/youtube/v3/docs/comments/update#usage).

[delete](https://developers.google.com/youtube/v3/docs/comments/delete)
:   Deletes a comment.
    [Try it now](https://developers.google.com/youtube/v3/docs/comments/delete#usage).

[setModerationStatus](https://developers.google.com/youtube/v3/docs/comments/setModerationStatus)
:   Sets the moderation status of one or more comments. The API request must be authorized by the owner of the channel or video associated with the comments.
    [Try it now](https://developers.google.com/youtube/v3/docs/comments/setModerationStatus#usage).

## Resource representation

The following JSON structure shows the format of a `comments` resource:  

```text
{
  "kind": "youtube#comment",
  "etag": etag,
  "id": string,
  "snippet": {
    "authorDisplayName": string,
    "authorProfileImageUrl": string,
    "authorChannelUrl": string,
    "authorChannelId": {
      "value": string
    },
    "channelId": string,
    "textDisplay": string,
    "textOriginal": string,
    "parentId": string,
    "canRate": boolean,
    "viewerRating": string,
    "likeCount": unsigned integer,
    "moderationStatus": string,
    "publishedAt": datetime,
    "updatedAt": datetime
  }
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                                                                                                                                                                                                     Properties                                                                                                                                                                                                                                     ||
|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `kind`                          | `string` Identifies the API resource's type. The value will be `youtube#comment`.                                                                                                                                                                                                                                                                                                                                                                 |
| `etag`                          | `etag` The Etag of this resource.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `id`                            | `string` The ID that YouTube uses to uniquely identify the comment.                                                                                                                                                                                                                                                                                                                                                                               |
| `snippet`                       | `object` The `snippet` object contains basic details about the comment.                                                                                                                                                                                                                                                                                                                                                                           |
| snippet.`authorDisplayName`     | `string` The display name of the user who posted the comment.                                                                                                                                                                                                                                                                                                                                                                                     |
| snippet.`authorProfileImageUrl` | `string` The URL for the avatar of the user who posted the comment.                                                                                                                                                                                                                                                                                                                                                                               |
| snippet.`authorChannelUrl`      | `string` The URL of the comment author's YouTube channel, if available.                                                                                                                                                                                                                                                                                                                                                                           |
| snippet.`authorChannelId`       | `object` This object encapsulates information about the comment author's YouTube channel, if available.                                                                                                                                                                                                                                                                                                                                           |
| snippet.authorChannelId.`value` | `string` The ID of the comment author's YouTube channel, if available.                                                                                                                                                                                                                                                                                                                                                                            |
| snippet.`channelId`             | `string` The ID of the YouTube channel associated with the comment.                                                                                                                                                                                                                                                                                                                                                                               |
| snippet.`textDisplay`           | `string` The comment's text. The text can be retrieved in either plain text or HTML. (The `comments.list` and `commentThreads.list` methods both support a `textFormat` parameter, which specifies the chosen text format.) Even the plain text may differ from the original comment text. For example, it may replace video links with video titles.                                                                                             |
| snippet.`textOriginal`          | `string` The original, raw text of the comment as it was initially posted or last updated. The original text is only returned to the authenticated user if they are the comment's author.                                                                                                                                                                                                                                                         |
| snippet.`parentId`              | `string` The unique ID of the parent comment. This property is only set if the comment was submitted as a reply to another comment.                                                                                                                                                                                                                                                                                                               |
| snippet.`canRate`               | `boolean` This setting indicates whether the current viewer can rate the comment.                                                                                                                                                                                                                                                                                                                                                                 |
| snippet.`viewerRating`          | `string` The rating the viewer has given to this comment. This property doesn't identify `dislike` ratings, though this behavior is subject to change. In the meantime, the property value is `like` if the viewer has rated the comment positively. The value is `none` in all other cases, including the user having given the comment a negative rating or not having rated the comment. Valid values for this property are: - `like` - `none` |
| snippet.`likeCount`             | `unsigned integer` The total number of likes (positive ratings) the comment has received.                                                                                                                                                                                                                                                                                                                                                         |
| snippet.`moderationStatus`      | `string` The comment's moderation status. This property is only returned if the API request was authorized by the owner of the channel or the video on which the requested comments were made. Also, this property isn't set if the API request used the [id](https://developers.google.com/youtube/v3/docs/comments/list#id) filter parameter. Valid values for this property are: - `heldForReview` - `likelySpam` - `published` - `rejected`   |
| snippet.`publishedAt`           | `datetime` The date and time when the comment was orignally published. The value is specified in [ISO 8601](https://www.w3.org/TR/NOTE-datetime) format.                                                                                                                                                                                                                                                                                          |
| snippet.`updatedAt`             | `datetime` The date and time when the comment was last updated. The value is specified in [ISO 8601](https://www.w3.org/TR/NOTE-datetime) format.                                                                                                                                                                                                                                                                                                 |
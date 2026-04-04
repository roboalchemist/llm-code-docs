# Source: https://developers.google.com/youtube/v3/guides/implementation/subscriptions.md.txt

# Implementation: Subscriptions

The following examples show how to use the YouTube Data API (v3) to perform functions related to subscriptions.

## Retrieve a channel's subscriptions

Call the [subscriptions.list](https://developers.google.com/youtube/v3/docs/subscriptions/list) method to retrieve subscriptions for a particular channel. There are two ways to identify the channel:

- To retrieve the currently authenticated user's subscriptions, set the [mine](https://developers.google.com/youtube/v3/docs/subscriptions/list#mine) parameter's value to `true`. Note that a request that uses the `mine` parameter must be authorized using OAuth 2.0.

  ```
  https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.subscriptions.list?
          part=snippet,contentDetails
          &mine=true
  ```
- To retrieve subscriptions for any other channel, set the [channelId](https://developers.google.com/youtube/v3/docs/subscriptions/list#channelId) parameter's value to that channel's unique YouTube channel ID. The example below retrieves a list of channels subscribed to by the TED channel on YouTube.

  ```
  https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.subscriptions.list?
          part=snippet,contentDetails
          &channelId=UCAuUUnT6oDeKwE6v1NGQxug
  ```

  **Note:** The API returns a `403 (Forbidden)` HTTP response code if the specified channel does not publicly expose its subscriptions and the request is not authorized by the channel's owner.

See the [subscriptions.list](https://developers.google.com/youtube/v3/docs/subscriptions/list#usage) method's documentation for code samples.

## Add a subscription

Call the [subscriptions.insert](https://developers.google.com/youtube/v3/docs/subscriptions/insert) method to add a channel subscription. This request must be authorized using OAuth 2.0. The request body is a [subscription](https://developers.google.com/youtube/v3/docs/subscriptions) resource that sets the following values:

<br />

- The [snippet.resourceId.kind](https://developers.google.com/youtube/v3/docs/subscriptions#snippet.resourceId.kind) contains the value `youtube#channel`.
- The [snippet.resourceId.channelId](https://developers.google.com/youtube/v3/docs/subscriptions#snippet.resourceId.channelId) property identifies the channel that is being subscribed to. The property value is a unique YouTube channel ID. The channel ID could be obtained in multiple ways, including calling the [channels.list](https://developers.google.com/youtube/v3/docs/channels/list) method or retrieving [search results for channels](https://developers.google.com/youtube/v3/docs/search/list).

<br />

The API request below subscribes you to the TED channel on YouTube:  

```
https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.subscriptions.insert?
        part=snippet
```

The request body is:  

```
{
  "snippet": {
    "resourceId": {
      "kind": "youtube#channel",
      "videoId": "UCAuUUnT6oDeKwE6v1NGQxug"
    }
  }
}
```

See the [subscriptions.insert](https://developers.google.com/youtube/v3/docs/subscriptions/insert#usage) method's documentation for code samples.

## Delete a subscription

This example deletes a subscription. This request must be authorized using OAuth 2.0. This example has two steps:

- **Step 1: Retrieve the subscriptions for the authenticated user's channel**

  Call the [subscriptions.list](https://developers.google.com/youtube/v3/docs/subscriptions/list) method to retrieve the list of subscriptions. The example above for retrieving a channel's subscriptions explains how to make this request.

  The application calling the API could process the API response to display a list of subscriptions, using each subscription's ID as a key. In the response, each item's `id` property identifies the subscription ID that uniquely identifies the corresponding subscription. You will use that value to remove an item from the list in the next step.
- **Step 2: Delete a subscription**

  Call the [subscriptions.delete](https://developers.google.com/youtube/v3/docs/subscriptions/delete) method to delete a subscription. Set the request's [id](https://developers.google.com/youtube/v3/docs/subscriptions/delete#id) parameter to the subscription ID for the subscription that you want to remove. This request must be authorized using OAuth 2.0.

  To complete the request in the APIs Explorer, you need to set the `id` property's value.  

  ```
  https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.subscriptions.delete?
          id=SUBSCRIPTION_ID
  ```

See the [subscriptions.delete](https://developers.google.com/youtube/v3/docs/subscriptions/delete#usage) method's documentation for code samples.

## Retrieve a list of subscribers to the authorized user's channel

To retrieve a list of channels that subscribe to the currently authenticated user's channel, call the `subscriptions.list` method and set the [mySubscribers](https://developers.google.com/youtube/v3/docs/subscriptions/list#mySubscribers) parameter's value to `true`. The request must be authorized using OAuth 2.0.  

```
https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.subscriptions.list?
        part=snippet,contentDetails
        &mySubscribers=true
```
# Source: https://developers.google.com/youtube/v3/guides/implementation/activities.md.txt

# Implementation: Activities

YouTube is deprecating the channel bulletin feature. As a result, the [activities.insert](https://developers.google.com/youtube/v3/docs/activities/insert) method will be deprecated, and the [activities.list](https://developers.google.com/youtube/v3/docs/activities/list) method will stop returning channel bulletins. These changes will be effective in the API on or after May 18, 2020. For more details, please see the [YouTube Help Center](https://support.google.com/youtube?p=channel-bulletins).

The following examples show how to use the YouTube Data API (v3) to perform functions related to user activity.

## Retrieve a list of channel activities

To retrieve a list of events related to a particular channel, call the [activities.list](https://developers.google.com/youtube/v3/docs/activities/list) method using one of the following two methods to identify the channel:

- Set the [mine](https://developers.google.com/youtube/v3/docs/activities/list#mine) parameter value to `true` to retrieve a list of the currently authenticated user's activities. Your request must be authorized using OAuth 2.0.

  ```
  https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.activities.list?
          part=snippet,contentDetails
          &mine=true
  ```
- Set the [channelId](https://developers.google.com/youtube/v3/docs/activities/list#channelId) parameter to the YouTube channel ID that uniquely identifies the channel for which you are retrieving an activity list. This example sets the `channelId` parameter to `UCK8sQmJBp8GCxrOtXWBpyEA`, which also identifies Google's official YouTube channel.

  ```
  https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.activities.list?
          part=snippet,contentDetails
          &channelId=UCK8sQmJBp8GCxrOtXWBpyEA
  ```

## Retrieve a list of subscription activities

Subscription activities refer to events associated with channels that the authenticated user subscribes to. To retrieve a list of subscription activities for the currently authenticated user, call the [activities.list](https://developers.google.com/youtube/v3/docs/activities/list) method and set the [home](https://developers.google.com/youtube/v3/docs/activities/list#home) parameter's value to `true`. The request must be authorized using OAuth 2.0.  

```
https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.activities.list?
        part=snippet,contentDetails
        &home=true
```
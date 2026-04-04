# Source: https://developers.google.com/youtube/v3/sample_requests.md.txt

# Sample API Requests

This page shows sample requests to the YouTube Data API. You use the YouTube Data API to retrieve and manipulate YouTube resources like videos, channels, and playlists. Each sample links to and populates the Google APIs Explorer so that you can execute the sample and see the response.

For information about *uploading* content using the YouTube Data API, see [Resumable Uploads](https://developers.google.com/youtube/v3/guides/using_resumable_upload_protocol).

## Overview

For clarity of presentation, the samples on this page show the distinctive elements of each request and abbreviate the base URL for the host that processes Data API requests (`https://www.googleapis.com/youtube/v3`). To make the request outside of the context of the samples, you need to include the full URL.

For example, here is a sample request as it appears on this page:  

```
GET {base-URL}/channels?part=contentDetails
                       &mine=true
```

The complete URL for this request is:  

```
GET https://www.googleapis.com/youtube/v3/channels?part=contentDetails
                                                  &mine=true
```

Several of the requests retrieve data that is accessible only to the owner of the YouTube channel, such as the list of subscribers. These requests require the channel owner to grant the Google APIs Explorer the right to perform YouTube Data API requests on their behalf. (See [Implementing OAuth 2.0 Authentication](https://developers.google.com/youtube/v3/guides/authentication) for details about authorizing access to private channel data.) After linking to the APIs Explorer, click the **Authorize requests using OAuth 2.0** button. This step authorizes the APIs Explorer to make requests on behalf of the owner. You also select the scope of the authorization, which specifies the types of requests the APIs Explorer can perform.

The response to each request is the [JSON](http://json.org) representation of a YouTube resource. The `part` parameter in the request specifies which portions of the resource are included in the response. The parameter identifies one or more top-level (non-nested) resource properties that should be included in the response. For example, some of the parts of a [video](https://developers.google.com/youtube/v3/docs/videos#resource) resource are:

- snippet
- contentDetails
- player
- statistics
- status

All of these parts are objects that contain nested properties, and you can think of these objects as groups of metadata fields that the API server might (or might not) retrieve. As such, the `part` parameter requires you to select the resource components that your application actually uses. See [Getting Started with the YouTube Data API](https://developers.google.com/youtube/v3/getting-started#partial) for more information.

## Retrieve channel information

This request uses the [channels.list](https://developers.google.com/youtube/v3/docs/channels/list) method to retrieve details about the channels belonging to the authenticated user.  

```
GET {base_URL}/channels?part=contentDetails
                       &mine=true
```

The response to this request includes the channel ID and `contentDetails` for the authenticated user's channel. The `contentDetails` include the several system-generated playlists associated with the channel. Many of the subsequent requests require either the channel ID or one of the playlist IDs, so it's important to record them.  

```gdscript
{
  "id": {CHANNEL_ID},
  "kind": "youtube#channel",
  "etag": etag,
  "contentDetails": {
    "relatedPlaylists": {
      "likes": {LIKES_PLAYLIST_ID},
      "favorites": {FAVORITES_PLAYLIST_ID},
      "uploads": {UPLOADS_PLAYLIST_ID},
      "watchHistory": {WATCHHISTORY_PLAYLIST_ID},
      "watchLater": {WATCHLATER_PLAYLIST_ID}
    },
    "googlePlusUserId": string
  },
}
```

### Uploaded videos and system-generated playlists

YouTube adds all uploaded videos to a playlist associated with the channel. To get a list of the uploaded videos, you query the "uploads" playlist returned in [the response shown above for channel information](https://developers.google.com/youtube/v3/sample_requests#channel_information), using the [playlistItems.list](https://developers.google.com/youtube/v3/docs/playlistItems/list) method to retrieve the videos in that playlist.

Before executing the following sample request in the Google APIs Explorer, replace <var translate="no">{UPLOADS_PLAYLIST_ID}</var> with the playlist ID from the earlier request.  

```
GET {base_URL}/playlistItems?part=contentDetails
                            &playlistId={UPLOADS_PLAYLIST_ID}
```

Note that the `"id"` value for each returned item is its playlistItem ID. The video ID for the playlist item is the `videoId` in the `contentDetails` part.

You can retrieve a user's favorites, likes, watch history, or watch later lists using the above request by substituting the corresponding playlist ID from the channel information response.

### User-created playlists

This request uses the [playlists.list](https://developers.google.com/youtube/v3/docs/playlists/list) method to retrieve the playlists associated with the authenticated channel. Note that this request does ***not*** retrieve the system-generated playlists included in the channel information (uploads, watchHistory, and so on). It retrieves only user-created playlists.  

```
GET {base_URL}/playlists?part=snippet
                        &mine=true
```

Once you have a playlist ID, you can retrieve the items from the playlist using the [request shown in the previous section](https://developers.google.com/youtube/v3/sample_requests#uploaded_videos).

You can request information about information about a channel's public playlists without authentication. When you submit an unauthenticated request, you need to include the `key` argument that specifies the[unique API key for the application](https://developers.google.com/youtube/registering_an_application) making the request. For example, this request retrieves the playlists associated with the GoogleDevelopers channel.  

```
GET {base_URL}/playlists?part=snippet
                        &channelId=UC_x5XG1OV2P6uZZ5FSM9Ttw
                        &key={YOUR_API_KEY}
```

## Retrieve Subscriptions

A [subscription](https://developers.google.com/youtube/v3/docs/subscriptions) resource defines a relationship between a YouTube user (the subscriber) and a channel. The [subscriptions.list](https://developers.google.com/youtube/v3/docs/subscriptions/list) method retrieves the subscribers to a particular channel or the subscriptions for a particular user, depending on which parameters you include in the request.

### Channel subscribers

This request retrieves a list of the subscribers to the authenticated channel.  

```
GET {base_URL}/subscriptions?part=snippet
                            &mySubscribers=true
```

### User subscriptions

The same method that lists subscribers ([subscriptions.list](https://developers.google.com/youtube/v3/docs/subscriptions/list)) can be used to list the channels that a user subscribes to. This request uses the `mine` parameter to retrieve a list of the YouTube channels that the authenticated user subscribes to.  

```
GET {base_URL}/subscriptions?part=snippet
                            &mine=true
```

## Retrieve user activity

An [activity](https://developers.google.com/youtube/v3/docs/activities) resource contains information about an action that a particular channel or user has taken on YouTube -- uploading a video, subscribing to a channel, and so on. The [activities.list](https://developers.google.com/youtube/v3/docs/activities/list) method retrieves the actions associated with a channel or user that match the request criteria. For example, you can retrieve actions associated with a particular channel, with the user's subscriptions, or with the user's custom YouTube home page.

### Activity during a time period

This request retrieves all of the actions that the authenticated user took during April 2013.  

```
GET {base_URL}/activities?part=snippet,contentDetails
                         &mine=true
                         &publishedAfter=2013-04-01T00%3A00%3A00Z
                         &publishedBefore=2013-05-01T00%3A00%3A00Z
```

### Home page activity

This request retrieves the custom activity feed that displays on the authenticated user's YouTube home page.  

```
GET {base_URL}/activities?part=snippet,contentDetails
                         &home=true
```

To retrieve viewing statistics, popularity metrics, and demographic information for YouTube videos and channels, you use the [YouTube Analytics API](https://developers.google.com/youtube/analytics/). The [Sample API Requests](https://developers.google.com/youtube/analytics/sample-requests) page shows how to retrieve common reports from YouTube Analytics.

## Search

The [search.list](https://developers.google.com/youtube/v3/docs/search/list) method enables you to search for YouTube videos, channels, or playlists that match specified criteria. You can search based on video properties, keywords, or topics (or a combination of these), and you can sort the results based on factors such as creation date, viewcount, or rating.

Like other YouTube Data API requests, the `search.list` method returns the JSON representation of a YouTube resource. Unlike other YouTube resources, however, a search result is not a persistent object with a unique ID.

Many requests search for publicly available content and therefore don't require authentication. Among the samples below, only the first requires authentication, since it specifically asks for "my" videos. When you submit an unauthenticated request, you need to include the `key` argument that specifies the[unique API key for your application](https://developers.google.com/youtube/registering_an_application).

### My most-viewed videos

This request retrieves all of the authenticated user's video and lists them in descending order by viewcount.  

```
GET {base_URL}/search?part=snippet
                     &forMine=true
                     &order=viewCount
                     &type=video
```

### Embeddable high-definition videos

This request searches for videos that have particular properties, namely high-definition videos that can be embedded on other sites. It lists the results in descending order of rating.  

```
GET {base_URL}/search?part=snippet
                     &order=rating
                     &type=video
                     &videoDefinition=high
                     &videoEmbeddable=true
                     &key={YOUR_API_KEY}
```

### Videos about a particular subject

This request performs a keyword search for videos about the YouTube Data API that include captions.  

```
GET {base_URL}/search?part=snippet
                     &q=YouTube+Data+API
                     &type=video
                     &videoCaption=closedCaption
                     &key={YOUR_API_KEY}
```

### Topic-based searching

A more sophisticated way to search for videos on a particular topic is to use [Freebase topics](https://developers.google.com/youtube/v3/guides/searching_by_topic) instead of keywords. YouTube channel and video resources all contain a [topicDetails](https://developers.google.com/youtube/v3/docs/videos#topicDetails) object that contains a list of Freebase topic IDs associated with the resource. A topic-based search is more intelligent than a keyword search, because a Freebase topic represents all aspects of a real-world concept or thing.

To search using a Freebase topic, you first need to retrieve the topic ID using the [Freebase API](https://developers.google.com/freebase/). This request returns videos associated with the Freebase topic for Python, whose topic ID is `/m/05z1_`.  

```
GET {base_URL}/search?part=snippet
                     &topicId=/m/05z1_
                     &type=video
                     &key={YOUR_API_KEY}
```

### Searching for playlists or channels

Searching is not limited to videos. You can also search for playlists or channels. This request retrieves playlists that match the keyword 'soccer'.  

```
GET {base_URL}/search?part=snippet
                     &q=soccer
                     &type=playlist
                     &key={YOUR_API_KEY}
```

If you'd rather find soccer channels, just change the `type` parameter.  

```
GET {base_URL}/search?part=snippet
                     &q=soccer
                     &type=channel
                     &key={YOUR_API_KEY}
```

If you'd like *all* soccer-related content (channels, playlists, and videos), you can do a universal search. If you omit the `type` parameter, the request retrieves content of all types  

```
GET {base_URL}/search?part=snippet
                     &q=soccer
                     &key={YOUR_API_KEY}
```

## Create and update resources

The requests we've looked at so far all use the HTTP GET method to retrieve YouTube data. The YouTube Data API also offers methods that use HTTP POST to create or update YouTube resources such as videos, playlists, or channels. The following requests provide examples.

POST methods include a `Request body`, which is the JSON representation of the resource being created or updated. You can create JSON representations in the Google APIs Explorer using an interactive tool.

### Create a subscription

This request subscribes the authenticated user to the GoogleDevelopers channel. In other words, it creates a subscription resource.  

```
POST {base_URL}/subscriptions?part=snippet
 Request body:
  {
    'snippet': {
      'resourceId': {
        'kind': 'youtube#channel',
        'channelId': 'UC_x5XG1OV2P6uZZ5FSM9Ttw' 
       }
     }
  }
```

### Create a playlist

This request creates a new public playlist.  

```
POST {base_URL}/playlists?part=snippet
 Request body:
  {
    'snippet': {
      'title': 'New playlist', 
      'description': 'Sample playlist for Data API',
     }
  }
```

### Adding a video to a playlist

Now that we've created a playlist, let's add a video to it. This request adds a video to the beginning of the playlist (`'position': 0`).  

```
POST {base_URL}/playlistItems?part=snippet
  Request body:
  {
    'snippet': {
      'playlistId': '{PLAYLIST_ID}', 
      'resourceId': {
          'kind': 'youtube#video',
          'videoId': '{VIDEO_ID}'
        }
     'position': 0
      }
   }
```
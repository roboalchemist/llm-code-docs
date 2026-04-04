# Source: https://developers.google.com/youtube/v3/guides/implementation/playlists.md.txt

# Implementation: Playlists

The following examples show how to use the YouTube Data API (v3) to perform functions related to playlists and playlist items.

## Retrieve the current user's playlists

Call the [playlists.list](https://developers.google.com/youtube/v3/docs/playlists/list) method to retrieve the currently authenticated user's playlists. In your request, set the [mine](https://developers.google.com/youtube/v3/docs/playlists/list#mine) parameter's value to `true`. Note that a request that uses the `mine` parameter must be authorized using OAuth 2.0.  

```
https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.playlists.list?
        part=snippet,contentDetails
        &mine=true
```

## Retrieve a user's playlists

This example retrieves the playlists created by a particular channel. The example has two steps:

- **Step 1: Retrieving the channel ID**

  Call the [channels.list](https://developers.google.com/youtube/v3/docs/channels/list) method to retrieve the channel ID associated with a particular YouTube username. (In this example, the username is `GoogleDevelopers`.) In the API response, the `id` property identifies the channel ID.  

  ```
  https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.channels.list?
          part=id
          &forUsername=GoogleDevelopers
  ```
- **Step 2: Retrieving the channel's playlists**

  Call the [playlists.list](https://developers.google.com/youtube/v3/docs/playlists/list) method to retrieve the channel's playlists. Set the [channelId](https://developers.google.com/youtube/v3/docs/playlists/list#channelId) parameter's value to the value obtained in step 1.  

  ```
  https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.playlists.list?
          part=snippet,contentDetails
          &channelId=UC_x5XG1OV2P6uZZ5FSM9Ttw
  ```

## Retrieve information about a specific playlist

To retrieve information about one or more specific playlists, call the [playlists.list](https://developers.google.com/youtube/v3/docs/playlists/list) method and set the [id](https://developers.google.com/youtube/v3/docs/playlists/list#id) parameter to a comma-separated list of YouTube playlist IDs that identify the desired resources. A common use case for this functionality is a request to retrieve additional information about a group of playlists returned in a set of search results. For example, you might want to retrieve the number of items in each playlist.

The request below calls the `playlists.list` method to retrieve the number of items in two playlists that match the query term "GoogleDevelopers." This information is in the `playlist` resource's `contentDetails.itemCount` property, so the request sets the `part` parameter value to `contentDetails`.  

```
https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.playlists.list?
        part=contentDetails
        &id=PLOU2XLYxmsIIM9h1Ybw2DuRw6o2fkNMeR,PLyYlLs02rgBYRWBzYpoHz7m2SE8mEZ68w
```

## Add a playlist

This example calls the [playlists.insert](https://developers.google.com/youtube/v3/docs/playlists/insert) method to create a private playlist in the authenticated user's channel. Any API request to this method must be authorized using OAuth 2.0.  

```
https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.playlists.insert?
        part=snippet,status
```

The link to the APIs Explorer also sets a parameter that specifies the body of the API request. The request body contains a [playlist](https://developers.google.com/youtube/v3/docs/playlists) resource, which defines information like the playlist's title, description, and privacy status. In this example, the request body is:  

```
{
  "snippet": {
    "title": "New playlist",
    "description": "New playlist description"
  },
  "status": {
    "privacyStatus": "private"
  }
}
```

The following example marks the new playlist as a podcast show:  

```
{
  "snippet": {
    "title": "New playlist",
    "description": "New playlist description"
  },
  "status": {
    "podcastStatus": "enabled"
  }
}
```

Related code samples: [Java](https://developers.google.com/youtube/v3/code_samples/java#create_a_playlist), [JavaScript](https://developers.google.com/youtube/v3/code_samples/javascript#create_a_playlist), [.NET](https://developers.google.com/youtube/v3/code_samples/dotnet#create_a_playlist), [PHP](https://developers.google.com/youtube/v3/code_samples/php#create_a_playlist), [Python](https://developers.google.com/youtube/v3/code_samples/python#create_a_playlist)

## Update a playlist

This example updates a playlist's privacy status from `private` to `public`. The example has two steps:

- **Step 1: Retrieve the playlist ID**

  Call the [playlists.list](https://developers.google.com/youtube/v3/docs/playlists/list) method to retrieve the playlists in the currently authenticated user's channel. The sample request above for [retrieving the current user's playlists](https://developers.google.com/youtube/v3/guides/implementation/playlists#playlists-retrieve-for-current-user) demonstrates this request. The application calling the API could process the API response to display a list of playlists, using each playlist's ID as a key.
- **Step 2: Updating a playlist**

  Call the [playlists.update](https://developers.google.com/youtube/v3/docs/playlists/update) method to modify a specific playlist. This method requires a valid OAuth 2.0 authorization token.

  The request body must include the `playlist` resource's `snippet` part because the `snippet.title` property is required when calling this method. In addition, if the playlist resource being updated specifies values for the `snippet.description` or `snippet.tags` properties, those values must be respecified in the update request or they will be deleted.  

  ```
  https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.playlists.update?
          part=snippet,status
  ```

  As in the example above for adding a playlist, the link to the APIs Explorer sets a parameter that specifies the body of the API request. The request body contains a [playlist](https://developers.google.com/youtube/v3/docs/playlists) resource, which defines information like the playlist's title, description, and privacy status. The following request body is used in this example:  

  ```
  {
    "id": "PLAYLIST_ID",
    "snippet": {
      "title": "New playlist",
      "description": "New playlist description"
    },
    "status": {
      "privacyStatus": "public"
    }
  }
  ```

  The following example marks the playlist as a podcast show:  

  ```
  {
    "id": "PLAYLIST_ID",
    "snippet": {
      "title": "New playlist",
      "description": "New playlist description"
    },
    "status": {
      "podcastStatus": "enabled"
    }
  }
  ```

  **Note:** If you are testing this query in the APIs Explorer, you will need to substitute a valid playlist ID into the resource body. To get a playlist ID, we recommend that you first run the request shown above for [adding a playlist](https://developers.google.com/youtube/v3/guides/implementation/playlists#playlists-insert). Extract the playlist ID from the API response and use that value for the playlist you want to update. The playlist title and description used in this example are the same as those used in that example.

## Add a playlist item

This example adds an item to a playlist. This request must be authorized using OAuth 2.0. This example has two steps:

- **Step 1: Retrieve the appropriate playlist ID**

  Call the [playlists.list](https://developers.google.com/youtube/v3/docs/playlists/list) method to retrieve the playlists in the currently authenticated user's channel. The sample request above for [retrieving the current user's playlists](https://developers.google.com/youtube/v3/guides/implementation/playlists#playlists-retrieve-for-current-user) demonstrates this request. The application calling the API could process the API response to display a list of playlists, using each playlist's ID as a key.
- **Step 2: Add a video to the playlist**

  Call the [playlistItems.insert](https://developers.google.com/youtube/v3/docs/playlistItems/insert) method to add a video to the playlist. This request must be authorized using OAuth 2.0. The request body is a [playlistItem](https://developers.google.com/youtube/v3/docs/playlistItems) resource that specifies at least the following values:

  <br />

  - The [snippet.playlistId](https://developers.google.com/youtube/v3/docs/playlistItems#snippet.playlistId) identifies the playlist to which you are adding the video. This is the playlist ID you obtained in step 1.
  - The [snippet.resourceId.kind](https://developers.google.com/youtube/v3/docs/playlistItems#snippet.resourceId.kind) contains the value `youtube#video`.
  - The [snippet.resourceId.videoId](https://developers.google.com/youtube/v3/docs/playlistItems#snippet.resourceId.videoId) identifies the video that you are adding to the playlist. The property value is a unique YouTube video ID.

  <br />

  The API request below adds a video to a playlist. The request body is:  

  ```
  {
    "snippet": {
      "playlistId": "PLAYLIST_ID",
      "resourceId": {
        "kind": "youtube#video",
        "videoId": "VIDEO_ID"
      }
    }
  }
  ```

  To complete the request in the APIs Explorer, you need to set values for the `snippet.playlistId` and `snippet.resourceId.videoId` properties.  

  ```
  https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.playlistItems.insert?
          part=snippet
  ```

  **Note:** The documentation for the [playlistItems.insert](https://developers.google.com/youtube/v3/docs/playlistItems/insert#request_body) method identifies the other property values you can set when adding a playlist item.

## Add a playlist image

You can use the v3 API's [playlistImages.insert](https://developers.google.com/youtube/v3/docs/playlistImages/insert) method to upload a custom thumbnail image and set it for a playlist. In your request, the [playlistId](https://developers.google.com/youtube/v3/docs/playlistImages/insert#playlistId) parameter's value identifies the playlist for which the thumbnail will be used.

This query cannot be tested using the APIs Explorer because the APIs Explorer does not support the ability to upload media files, which is a requirement for this method.

## Update a playlist item

This example updates a playlist item so that it is the first item in a playlist. This request must be authorized using OAuth 2.0. This example has three steps:

- **Step 1: Retrieve the appropriate playlist ID**

  Call the [playlists.list](https://developers.google.com/youtube/v3/docs/playlists/list) method to retrieve the playlists in the currently authenticated user's channel. The sample request above for [retrieving the current user's playlists](https://developers.google.com/youtube/v3/guides/implementation/playlists#playlists-retrieve-for-current-user) demonstrates this request. The application calling the API could process the API response to display a list of playlists, using each playlist's ID as a key.
- **Step 2: Retrieve the items in the selected playlist**

  Call the `playlistItems.list` method to retrieve the list of videos in the selected playlist. Set the [playlistId](https://developers.google.com/youtube/v3/docs/playlistItems/list#playlistId) parameter's value to the playlist ID that you obtained in step 1.

  Each resource in the API response contains an `id` property, which identifies the playlist item ID that uniquely identifies that item. You will use that value to remove an item from the list in the next step.
- **Step 3: Update the selected playlist item**

  Call the [playlistItems.update](https://developers.google.com/youtube/v3/docs/playlistItems/update) method to change the video's position in the playlist. Set the [part](https://developers.google.com/youtube/v3/docs/playlistItems/update#part) parameter value to `snippet`. The request body must be a [playlistItem](https://developers.google.com/youtube/v3/docs/playlistItems) resource that at least sets the following values:

  <br />

  - Set the `id` property to the playlist item ID obtained in step 2.
  - Set the `snippet.playlistId` property to the playlist ID obtained in step 1.
  - Set the `snippet.resourceId.kind` property to `youtube#video`.
  - Set the `snippet.resourceId.videoId` property to the video ID that uniquely identifies the video included in the playlist.
  - Set the `snippet.position` property to `0` or to whatever position you want the item to appear (using a 0-based index).

  <br />

  The API request below updates a playlist item to be the first item in a playlist. The request body is:  

  ```
  {
    "id": "PLAYLIST_ITEM_ID",
    "snippet": {
      "playlistId": "PLAYLIST_ID",
      "resourceId": {
        "kind": "youtube#video",
        "videoId": "VIDEO_ID"
      },
      "position": 0
    }
  }
  ```

  To complete the request in the APIs Explorer, you need to set values for the `id`, `snippet.playlistId` and `snippet.resourceId.videoId` properties.  

  ```
  https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.playlistItems.update?
          part=snippet
  ```

## Update a playlist image

You can use the v3 API's [playlistImages.update](https://developers.google.com/youtube/v3/docs/playlistImages/update) method to update the thumbnail image of a playlist. In your request, the [playlistId](https://developers.google.com/youtube/v3/docs/playlistImages/update#playlistId) parameter's value identifies the playlist for which the thumbnail will be used.

This query cannot be tested using the APIs Explorer because the APIs Explorer does not support the ability to upload media files, which is a requirement for this method.

## Remove a playlist item

This example deletes a video from a playlist. This request must be authorized using OAuth 2.0. This example has three steps. The first two steps are the same as those in the example above for [updating a playlist item](https://developers.google.com/youtube/v3/guides/implementation/playlists#playlistItems-update).

After completing those steps, call the [playlistItems.delete](https://developers.google.com/youtube/v3/docs/playlistItems/delete) method to remove a video from the playlist. Set the request's [id](https://developers.google.com/youtube/v3/docs/playlistItems/delete#id) parameter to the playlist item ID for the item you want to remove. This request must be authorized using OAuth 2.0.

Note that the playlist item ID used to identify a video in a playlist is different than the YouTube video ID that uniquely identifies the video. The playlist item ID identifies the video as an item in a particular playlist.

To complete the request in the APIs Explorer, you need to set the `id` property's value.  

```
https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.playlistItems.delete?
        id=PLAYLIST_ITEM_ID
```

## Remove a playlist image

This example deletes a playlist image. The example has two steps:

- **Step 1: Retrieve the playlist**

  Call the [playlists.list](https://developers.google.com/youtube/v3/docs/playlists/list) method to retrieve the playlists in the currently authenticated user's channel. The sample request above for [retrieving the current user's playlists](https://developers.google.com/youtube/v3/guides/implementation/playlists#playlists-retrieve-for-current-user) demonstrates this request. The application calling the API could process the API response to display a list of playlists, using each playlist's ID as a key.
- **Step 2: Retrieve the playlist image ID**

  Call the [playlistImages.list](https://developers.google.com/youtube/v3/docs/playlistImages/list) method to retrieve a playlist's thumbnail image. Use the playlist ID for the playlist you want to change.
- **Step 3: Deleting a playlist image**

  Call the [playlistImages.delete](https://developers.google.com/youtube/v3/docs/playlistImages/delete) method to delete a specific playlist image. In the request, the `id` parameter specifies the ID of the playlist image being deleted. This method requires a valid OAuth 2.0 authorization token. If you are testing this query in the APIs Explorer, you will need to replace the `id` parameter value with a valid playlist ID.  

  ```
  https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.playlistImages.delete?
          id=ID
  ```

  **Note:** If you are testing this query in the APIs Explorer, you will need to replace the `id` parameter value with a valid playlist image ID.

## Remove a playlist

This example deletes a playlist. The example has two steps:

- **Step 1: Retrieve the playlist ID**

  Call the [playlists.list](https://developers.google.com/youtube/v3/docs/playlists/list) method to retrieve the playlists in the currently authenticated user's channel. The sample request above for [retrieving the current user's playlists](https://developers.google.com/youtube/v3/guides/implementation/playlists#playlists-retrieve-for-current-user) demonstrates this request. The application calling the API could process the API response to display a list of playlists, using each playlist's ID as a key.
- **Step 2: Deleting a playlist**

  Call the [playlists.delete](https://developers.google.com/youtube/v3/docs/playlists/delete) method to delete a specific playlist. In the request, the `id` parameter specifies the playlist ID of the playlist being deleted. This method requires a valid OAuth 2.0 authorization token. If you are testing this query in the APIs Explorer, you will need to replace the `id` parameter value with a valid playlist ID.  

  ```
  https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.playlists.delete?
          id=PLAYLIST_ID
  ```

  **Note:** If you are testing this query in the APIs Explorer, you will need to replace the `id` parameter value with a valid playlist ID. To get a playlist ID, we recommend that you first run the request shown above for [adding a playlist](https://developers.google.com/youtube/v3/guides/implementation/playlists#playlists-insert). Extract the playlist ID from the API response and use that value for the playlist you want to delete.
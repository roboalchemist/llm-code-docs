# Source: https://developers.google.com/youtube/v3/code_samples/apps-script.md.txt

# Apps Script Code Samples

The following Apps Script code samples are available for the YouTube Data API. You can download these code samples from the `apps-script` folder of the [YouTube APIs code sample repository on GitHub](https://github.com/youtube/api-samples).

## Retrieve my uploads

This function retrieves the current script user's uploaded videos. To execute, it requires the OAuth read/write scope for YouTube as well as user authorization. In Apps Script's runtime environment, the first time a user runs a script, Apps Script will prompt the user for permission to access the services called by the script. After permissions are granted, they are cached for some period of time. The user running the script will be prompted for permission again once the permissions required change, or when they are invalidated by the `ScriptApp.invalidateAuth()` function.  

This script takes the following steps to retrieve the active user's uploaded videos:

1. Fetches the user's channels.
2. Fetches the user's 'uploads' playlist.
3. Iterates through this playlist and logs the video IDs and titles.
4. Fetches a next page token, if any. If there is one, fetches the next page. Repeat step 3.

```gdscript
/**
 * This function retrieves the current script user's uploaded videos. To execute,
 * it requires the OAuth read/write scope for YouTube as well as user authorization.
 * In Apps Script's runtime environment, the first time a user runs a script, Apps
 * Script will prompt the user for permission to access the services called by the
 * script. After permissions are granted, they are cached for some periodF of time.
 * The user running the script will be prompted for permission again once the
 * permissions required change, or when they are invalidated by the
 * ScriptApp.invalidateAuth() function.
 *
 * This script takes the following steps to retrieve the active user's uploaded videos:
 *    1. Fetches the user's channels
 *    2. Fetches the user's 'uploads' playlist
 *    3. Iterates through this playlist and logs the video IDs and titles
 *    4. Fetches a next page token (if any). If there is one, fetches the next page. GOTO Step 3
 */
function retrieveMyUploads() {
  var results = YouTube.Channels.list('contentDetails', {mine: true});
  for(var i in results.items) {
    var item = results.items[i];
    // Get the playlist ID, which is nested in contentDetails, as described in the
    // Channel resource: https://developers.google.com/youtube/v3/docs/channels
    var playlistId = item.contentDetails.relatedPlaylists.uploads;

    var nextPageToken = '';

    // This loop retrieves a set of playlist items and checks the nextPageToken in the
    // response to determine whether the list contains additional items. It repeats that process
    // until it has retrieved all of the items in the list.
    while (nextPageToken != null) {
      var playlistResponse = YouTube.PlaylistItems.list('snippet', {
        playlistId: playlistId,
        maxResults: 25,
        pageToken: nextPageToken
      });

      for (var j = 0; j < playlistResponse.items.length; j++) {
        var playlistItem = playlistResponse.items[j];
        Logger.log('[%s] Title: %s',
                   playlistItem.snippet.resourceId.videoId,
                   playlistItem.snippet.title);

      }
      nextPageToken = playlistResponse.nextPageToken;
    }
  }
}
```

## Search by keyword

This function searches for videos related to the keyword `'dogs'`. The video IDs and titles of the search results are logged to Apps Script's log.  

Note that this sample limits the results to 25. To return more results, pass additional parameters as documented in [Search:list](https://developers.google.com/youtube/v3/docs/search/list).  

```transact-sql
/**
 * This function searches for videos related to the keyword 'dogs'. The video IDs and titles
 * of the search results are logged to Apps Script's log.
 *
 * Note that this sample limits the results to 25. To return more results, pass
 * additional parameters as documented here:
 *   https://developers.google.com/youtube/v3/docs/search/list
 */
function searchByKeyword() {
  var results = YouTube.Search.list('id,snippet', {q: 'dogs', maxResults: 25});
  for(var i in results.items) {
    var item = results.items[i];
    Logger.log('[%s] Title: %s', item.id.videoId, item.snippet.title);
  }
}
```

## Search by topic

This function searches for videos that are associated with a particular Freebase topic, logging their video IDs and titles to the Apps Script log. This example uses the topic ID for Google Apps Script.  

Note that this sample limits the results to 25. To return more results, pass additional parameters as documented in [Search:list](https://developers.google.com/youtube/v3/docs/search/list).  

```transact-sql
/**
 * This function searches for videos that are associated with a particular Freebase
 * topic, logging their video IDs and titles to the Apps Script log. This example uses
 * the topic ID for Google Apps Script.
 *
 * Note that this sample limits the results to 25. To return more results, pass
 * additional parameters as documented here:
 *   https://developers.google.com/youtube/v3/docs/search/list
 */
function searchByTopic() {
  var mid = '/m/0gjf126';
  var results = YouTube.Search.list('id,snippet', {topicId: mid, maxResults: 25});
  for(var i in results.items) {
    var item = results.items[i];
    Logger.log('[%s] Title: %s', item.id.videoId, item.snippet.title);
  }
}
```

## Subscribe to channel

This sample subscribes the active user to the Google Developers YouTube channel, specified by the channelId.  

```gdscript
/**
 * This sample subscribes the active user to the Google Developers
 * YouTube channel, specified by the channelId.
 */
function addSubscription() {
  // Replace this channel ID with the channel ID you want to subscribe to
  var channelId = 'UC_x5XG1OV2P6uZZ5FSM9Ttw';
  var resource = {
    snippet: {
      resourceId: {
        kind: 'youtube#channel',
        channelId: channelId
      }
    }
  };

  try {
    var response = YouTube.Subscriptions.insert(resource, 'snippet');
    Logger.log(response);
  } catch (e) {
    if(e.message.match('subscriptionDuplicate')) {
      Logger.log('Cannot subscribe; already subscribed to channel: ' + channelId);
    } else {
      Logger.log('Error adding subscription: ' + e.message);
    }
  }
}
```

## Update video

This sample finds the active user's uploads, then updates the most recent upload's description by appending a string.  

```gdscript
/**
 * This sample finds the active user's uploads, then updates the most recent
 * upload's description by appending a string.
 */
function updateVideo() {
  // 1. Fetch all the channels owned by active user
  var myChannels = YouTube.Channels.list('contentDetails', {mine: true});
  // 2. Iterate through the channels and get the uploads playlist ID
  for (var i = 0; i < myChannels.items.length; i++) {
    var item = myChannels.items[i];
    var uploadsPlaylistId = item.contentDetails.relatedPlaylists.uploads;

    var playlistResponse = YouTube.PlaylistItems.list('snippet', {
      playlistId: uploadsPlaylistId,
      maxResults: 1
    });

    // Get the videoID of the first video in the list
    var video = playlistResponse.items[0];
    var originalDescription = video.snippet.description;
    var updatedDescription = originalDescription + ' Description updated via Google Apps Script';

    video.snippet.description = updatedDescription;

    var resource = {
      snippet: {
        title: video.snippet.title,
        description: updatedDescription,
        categoryId: '22'
      },
      id: video.snippet.resourceId.videoId
    };
    YouTube.Videos.update(resource, 'id,snippet');
  }
}
```
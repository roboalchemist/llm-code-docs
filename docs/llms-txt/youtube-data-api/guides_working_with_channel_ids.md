# Source: https://developers.google.com/youtube/v3/guides/working_with_channel_ids.md.txt

# Work with Channel IDs

*Jeff Posnick, YouTube Developer Relations -- June 2013*
For more than a year, it's been possible to link Google+ profiles with YouTube channels, and we've [blogged](http://apiblog.youtube.com/2012/03/youtube-google-api-and-you.html) about how some of the Data API v2 responses have changed as a result of that profile link. More recently, it has become possible to create new YouTube channels that don't have a traditional YouTube username associated with them and, instead, are [solely identified by their Google+ profile](http://youtubecreator.blogspot.com/2013/04/using-google-page-identity-on-youtube.html). Much of the information from that blog post still applies, but this extra wrinkle does invalidate some fundamental assumptions about YouTube channels -- like that each one will always be associated with a unique YouTube username -- and we wanted to follow up with some additional best practices to write code that works with all flavors of channels.

## Channel IDs in the Data API v3

All v3 operations that work with channels use [channel IDs](https://developers.google.com/youtube/v3/docs/channels#id) exclusively as a means of identifying those channels. The ID for a specific YouTube user's channel is identical in both v2 and v3 of the API, simplifying migrations between versions. This complete reliance on channel IDs might be perplexing for developers who were previously used to passing YouTube usernames to API methods, but v3 was designed to treat channels with and without legacy usernames identically, and that means using channel IDs everywhere.

If you are using v3 and want to retrieve the channel ID that corresponds to the currently authorized user, you can call the [channels.list(part="id", mine=true)](https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.channels.list?part=id&mine=true) method. This is equivalent to asking for the channel profile of the `default` user in v2.

If you ever do find yourself with an arbitrary legacy YouTube username that you need to translate into a channel ID using v3 of the API, you can make a [channels.list(part="id", forUsername="<var class="apiparam" translate="no">username</var>")](https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.channels.list?part=id&forUsername=YouTubeDev) call to the API.

If you only know a display name and are looking to find the corresponding channel, the [search.list(part="snippet", type="channel", q="<var class="apiparam" translate="no">display name</var>")](https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.search.list?part=snippet&q=YouTube+for+Developers&type=channel) method will come in handy. You should be prepared to deal with the possibility of the call returning more than one item in the response, since display names are not unique.

## Channel IDs in the Data API v2

**Note:** The YouTube Data API (v2) has been deprecated since February 26, 2014, and the API has been [turned down](http://youtube-eng.blogspot.com/2015/04/bye-bye-youtube-data-api-v2.html). Applications still using the v2 API should migrate to the v3 API immediately.

The biggest takeaway for developers using the older [Data API v2](https://developers.google.com/youtube/2.0/developers_guide_protocol_audience) is that you must be aware that **not every YouTube channel has a unique username** . Fortunately, every YouTube channel is guaranteed to have a unique channel ID associated with it, represented by the value in the [`<yt:channelId>` tag](https://developers.google.com/youtube/2.0/reference#youtube_data_api_tag_yt:channelId), and that's the value that we recommend developers use instead of usernames. For instance, if you have a database that maps YouTube usernames to information about that channel, your older entries should continue to work. (Existing channels won't lose their usernames.) However, as time goes on, it will become more and more likely that you'll have to work with channels that can't be uniquely identified by a username.

A couple of factors simplify the transition from usernames to channel IDs. First, the Data API v2 accepts channel IDs in request URLs wherever it accepts YouTube usernames, meaning that you can seamlessly swap a channel ID into your existing code. For example, since `UC_x5XG1OV2P6uZZ5FSM9Ttw` is the channel ID for the channel with the legacy username `GoogleDevelopers`, the following two URLs are equivalent API requests:  

    https://gdata.youtube.com/feeds/api/users/GoogleDevelopers?v=2.1
    https://gdata.youtube.com/feeds/api/users/UC_x5XG1OV2P6uZZ5FSM9Ttw?v=2.1

Another thing to keep in mind is that whenever you're making [authenticated](https://developers.google.com/youtube/2.0/developers_guide_protocol_authentication) v2 requests, you never need to include the authorized channel's username when constructing request URLs. You can always use the value `default` in place of a username (or channel ID). So if you want to retrieve the video uploads feed for the currently authorized user, for instance, you can do so at `https://gdata.youtube.com/feeds/api/users/default/uploads?v=2.1`.
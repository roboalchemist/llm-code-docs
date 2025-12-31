# Source: https://developers.google.com/youtube/v3/guides/made_for_kids_status.md.txt

# Finding the MadeForKids status of a video

Interactions with YouTube content that is specifically directed towards children, which
YouTube labels "MadeForKids" or "MFK", require special care and attention.

As an example, if you embed a YouTube video that is designated MadeForKids on your site or
app, you are required by [Section III.E.4.j of the
Developer Policies](https://developers.google.com/youtube/terms/developer-policies#III-E-4-j) to turn off tracking and make sure that all data collection, with
respect to that player, is compliant with applicable laws, including U.S. Children's Online
Privacy Protection Act (COPPA).

If you are not sure whether a video is designated MadeForKids, you can check the status of a
video at any given time via the YouTube Data API Service following the instructions outlined
below:

1. Create or access your Google developer account via <https://console.cloud.google.com/>.
2. Add the YouTube API to your selected API Project (if you haven't already). Note that the default YouTube API Services quota is 10,000 daily quota points; this is sufficient to check the MadeForKids video status of up to 5000 videos.
3. Using the YouTube Data API Service, call the [videos.list](https://developers.google.com/youtube/v3/docs/videos/list) endpoint.
   1. Include the relevant Video ID(s) in the request parameters.
   2. Include, at minimum, the `id` and `status` parts in the request's [part](https://developers.google.com/youtube/v3/docs/videos/list#part) parameter.
4. Check the [video](https://developers.google.com/youtube/v3/docs/videos#resource) resource returned for the MFK status, which is returned in the resource's [status.madeForKids](https://developers.google.com/youtube/v3/docs/videos#status.madeForKids) property.

You can learn more about MadeForKids guidelines in the
[YouTube Help Center](https://support.google.com/youtube/answer/9528076).
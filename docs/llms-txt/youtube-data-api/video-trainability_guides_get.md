# Source: https://developers.google.com/youtube/v3/video-trainability/guides/get.md.txt

# Get video trainability status

To get a video's trainability status, use the
[`videoTrainability.get`](https://developers.google.com/youtube/v3/video-trainability/reference/rest/get)
method.

You can quickly run the method using `curl` on the command line:  

    curl 'https://youtube.googleapis.com/youtube/v3/videoTrainability?id=VIDEO_ID'

For example:  

    curl 'https://youtube.googleapis.com/youtube/v3/videoTrainability?id=jNQXAC9IVRw'

| **Note:** Using the YouTube Video Third-Party Trainability API doesn't require authentication or quota requests.

### Check permitted parties

The `videoTrainability.get`
[response](https://developers.google.com/youtube/v3/video-trainability/reference/rest/get#response-body)
includes a `permitted` list:

- `all` indicates that anyone can use the video for training.
- `none` indicates that the video is not permitted for training.
- If the creator has specified a list of allowed companies, the response includes the list.
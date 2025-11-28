# Source: https://developers.google.com/youtube/v3/code_samples/python_appengine.md.txt

# Python on App Engine Code Samples

The following Python code samples demonstrate how to use App Engine to make YouTube Data API (v3) calls. You can download these code samples from the [Google App Engine Python code sample repositories on GitHub](https://github.com/youtube/api-samples/tree/master/python_appengine).

## Prerequisites

You must set up a project in the [Google API Console](https://console.cloud.google.com/) and get an API key to be able to run the code samples below. Currently, each project defines an `API_KEY` variable that is set to the value `REPLACE_ME`. You need to replace that value with your own API key to be able to run the samples.

**Important:** To be able to run all of these examples, you must enable the YouTube Data API (v3) and the Freebase API for the project associated with your API key. If your application accesses private user or channel data, you will also need an OAuth 2.0 client ID.
See instructions for creating an API key and getting your OAuth 2.0 client ID.

### Create your project and get authorization credentials

1. Open the [Credentials page](https://console.cloud.google.com/apis/credentials) in the API Console.
2. This API supports two types of credentials. Create whichever credentials are appropriate for your project:
   - **OAuth 2.0:** Whenever your application requests private user
     data, it must send an OAuth 2.0 token along with the request. Your
     application first sends a client ID and, possibly, a client secret to
     obtain a token. You can generate OAuth 2.0 credentials for web
     applications, service accounts, or installed applications.

     For more information, see the [OAuth 2.0 documentation](https://developers.google.com/identity/protocols/OAuth2).
   - **API keys:**

     A request that does not provide an OAuth 2.0 token must send an API
     key.

     The key identifies your project and provides API access, quota, and
     reports.

     The API supports several types of restrictions on API keys. If the API key that you
     need doesn't already exist, then create an API key in the Console by
     clicking **[Create credentials](https://console.cloud.google.com/apis/credentials) \> API key** . You can restrict the key before using it
     in production by clicking **Restrict key** and selecting one of the
     **Restrictions**.

To keep your API keys secure, follow the [best practices for
securely using API keys](https://cloud.google.com/docs/authentication/api-keys).

## Code samples

### Search by keyword

The code sample below calls the API's `search.list` method to retrieve search results associated with a particular keyword.  

```python
import os
import urllib
import webapp2
import jinja2

from apiclient.discovery import build
from optparse import OptionParser

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

# Set DEVELOPER_KEY to the "API key" value from the Google Developers Console:
# https://console.developers.google.com/project/_/apiui/credential
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "REPLACE_ME"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

class MainHandler(webapp2.RequestHandler):
   
   def get(self):
        if DEVELOPER_KEY == "REPLACE_ME":
          self.response.write("""You must set up a project and get an API key
                                 to run this project.  Please visit 
				 <landing page> to do so."""
        else:
          youtube = build(
            YOUTUBE_API_SERVICE_NAME, 
            YOUTUBE_API_VERSION, 
            developerKey=DEVELOPER_KEY)
          search_response = youtube.search().list(
            q="Hello",
            part="id,snippet",
            maxResults=5
          ).execute()
        
          videos = []
          channels = []
          playlists = []
        
          for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                videos.append("%s (%s)" % (search_result["snippet"]["title"], 
                  search_result["id"]["videoId"]))
            elif search_result["id"]["kind"] == "youtube#channel":
                channels.append("%s (%s)" % (search_result["snippet"]["title"], 
                  search_result["id"]["channelId"]))
            elif search_result["id"]["kind"] == "youtube#playlist":
                playlists.append("%s (%s)" % (search_result["snippet"]["title"], 
                  search_result["id"]["playlistId"]))
        
          template_values = {
           'videos': videos,
           'channels': channels,
           'playlists': playlists
          }
       
	  self.response.headers['Content-type'] = 'text/plain' 
          template = JINJA_ENVIRONMENT.get_template('index.html')
          self.response.write(template.render(template_values))
        
app = webapp2.WSGIApplication([
  ('/.*', MainHandler),
], debug=True)
```

### Search by topic

The code sample below calls the API's `search.list` method to retrieve search results associated with a particular Freebase topic.  

```python
import os
import urllib
import webapp2
import jinja2

from apiclient.discovery import build
from optparse import OptionParser

import json

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

REGISTRATION_INSTRUCTIONS = """
    You must set up a project and get an API key to run this code. Please see
    the instructions for creating a project and a key at <a
    href="https://developers.google.com/youtube/registering_an_application"
    >https://developers.google.com/youtube/registering_an_application</a>.
    <br><br>
    Make sure that you have enabled the YouTube Data API (v3) and the Freebase
    API for your project."""

# Set API_KEY to the "API key" value from the Google Developers Console:
# https://console.developers.google.com/project/_/apiui/credential
# Please ensure that you have enabled the YouTube Data API and Freebase API
# for your project.
API_KEY = "REPLACE_ME"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
FREEBASE_SEARCH_URL = "https://www.googleapis.com/freebase/v1/search?%s"
QUERY_TERM = "dog"

class MainHandler(webapp2.RequestHandler):

  def get(self):
    if API_KEY == 'REPLACE_ME':
      self.response.write(REGISTRATION_INSTRUCTIONS)
    else:
      # Present a list of Freebase topic IDs for the query term
      self.list_topics(QUERY_TERM)

  def list_topics(self, QUERY_TERM):
    # Retrieve a list of Freebase topics associated with the query term
    freebase_params = dict(query=QUERY_TERM, key=API_KEY)
    freebase_url = FREEBASE_SEARCH_URL % urllib.urlencode(freebase_params)
    freebase_response = json.loads(urllib.urlopen(freebase_url).read())

    if len(freebase_response["result"]) == 0:
      exit("No matching terms were found in Freebase.")

    # Create a page that shows a select box listing the topics.
    # When the user selects a topic and submits the form, the
    # 'post' method below will handle the form submission and
    # retrieve videos for the selected topic.
    select_topic_page = ('''
        <html>
          <body>
            <p>The following topics were found:</p>
            <form method="post">
              <select name="topic">
    ''')
    for result in freebase_response["result"]:
      select_topic_page += ('<option value="' + result["mid"] + '">' +
                            result.get("name", "Unknown") + '</option>')

    select_topic_page += '''
              </select>
              <p><input type="submit" /></p>
            </form>
          </body>
        </html>
    '''

    # Display the HTML page listing the topic choices.
    self.response.out.write(select_topic_page)

  def post(self):
    topic_id = self.request.get('topic')

    # Service for calling the YouTube API
    youtube = build(YOUTUBE_API_SERVICE_NAME,
                    YOUTUBE_API_VERSION,
                    developerKey=API_KEY)

    # Execute the search request using default query term and retrieved topic.
    search_response = youtube.search().list(
      part = 'id,snippet',
      type = 'video',
      topicId = topic_id
    ).execute()

    videos = []

    for search_result in search_response.get("items", []):
      videos.append(search_result)

    template_values = {
      'videos': videos
    }

    self.response.headers['Content-type'] = 'text/html'
    template = JINJA_ENVIRONMENT.get_template('index.html')
    self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
  ('/.*', MainHandler),
], debug=True)
```

### Retrieve a channel's uploads

The code sample below calls the API's `playlistItems.list` method to retrieve a list of videos uploaded to a specified channel. The channel can be identified by its channel ID or channel name. The code also calls the `channels.list` method to retrieve the playlist ID that identifies the channel's uploaded videos.  

```python
import os
import urllib
import webapp2
import jinja2

from apiclient.discovery import build
from optparse import OptionParser

import json

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

REGISTRATION_INSTRUCTIONS = """
    You must set up a project and get an API key to run this code. Please see
    the instructions for creating a project and a key at <a
    href="https://developers.google.com/youtube/registering_an_application"
    >https://developers.google.com/youtube/registering_an_application</a>.
    <br><br>
    Make sure that you have enabled the YouTube Data API (v3) and the Freebase
    API for your project."""

# Set API_KEY to the "API key" value from the Google Developers Console:
# https://console.developers.google.com/project/_/apiui/credential
# Please ensure that you have enabled the YouTube Data API and Freebase API
# for your project.
API_KEY = "REPLACE_ME"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
FREEBASE_SEARCH_URL = "https://www.googleapis.com/freebase/v1/search?%s"
QUERY_TERM = "dog"

class MainHandler(webapp2.RequestHandler):

  def get(self):
    if API_KEY == 'REPLACE_ME':
      self.response.write(REGISTRATION_INSTRUCTIONS)
    else:
      # Present a list of Freebase topic IDs for the query term
      self.request_channel()

  def request_channel(self):
    # Display a text box where the user can enter a channel name or
    # channel ID.
    select_channel_page = '''
        <html>
          <body>
            <p>Which channel's videos do you want to see?</p>
            <form method="post">
              <p>
                <select name="channel_type">
                  <option value="id">Channel ID</option>
                  <option value="name">Channel name</option>
                </select>Â Â 
                <input name="channel" size="30">
              </p>
              <p><input type="submit" /></p>
            </form>
          </body>
        </html>
    '''

    # Display the HTML page that shows the form.
    self.response.out.write(select_channel_page)

  def post(self):
    # Service for calling the YouTube API
    youtube = build(YOUTUBE_API_SERVICE_NAME,
                    YOUTUBE_API_VERSION,
                    developerKey=API_KEY)

    # Use form inputs to create request params for channel details
    channel_type = self.request.get('channel_type')
    channels_response = None
    if channel_type == 'id':
      channels_response = youtube.channels().list(
          id=self.request.get('channel'),
          part='snippet,contentDetails'
      ).execute()
    else:
      channels_response = youtube.channels().list(
          forUsername=self.request.get('channel'),
          part='snippet,contentDetails'
      ).execute()

    channel_name = ''
    videos = []

    for channel in channels_response['items']:
      uploads_list_id = channel['contentDetails']['relatedPlaylists']['uploads']
      channel_name = channel['snippet']['title']
      
      next_page_token = ''
      while next_page_token is not None:
        playlistitems_response = youtube.playlistItems().list(
            playlistId=uploads_list_id,
            part='snippet',
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        for playlist_item in playlistitems_response['items']:
          videos.append(playlist_item)
          
        next_page_token = playlistitems_response.get('tokenPagination', {}).get(
            'nextPageToken')
        
        if len(videos) > 100:
          break

    template_values = {
      'channel_name': channel_name,
      'videos': videos
    }

    self.response.headers['Content-type'] = 'text/html'
    template = JINJA_ENVIRONMENT.get_template('index.html')
    self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
  ('/.*', MainHandler),
], debug=True)
```
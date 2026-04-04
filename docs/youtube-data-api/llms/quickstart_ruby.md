# Source: https://developers.google.com/youtube/v3/quickstart/ruby.md.txt

# Ruby Quickstart

Complete the steps described in the rest of this page, and in about five minutes
you'll have a simple Ruby command-line application that makes requests to the
YouTube Data API.
The sample code used in this guide retrieves the `channel` resource for the GoogleDevelopers YouTube channel and prints some basic information from that resource.

## Prerequisites

To run this quickstart, you'll need:

- Ruby 2.0 or greater.
- Access to the internet and a web browser.
- A Google account.

## Step 1: Turn on the YouTube Data API

1. Use
   [this wizard](https://console.developers.google.com/start/api?id=youtube)
   to create or select a project in the Google Developers Console and
   automatically turn on the API. Click **Continue** , then
   **Go to credentials**.

2. On the **Create credentials** page, click the
   **Cancel** button.

3. At the top of the page, select the **OAuth consent screen** tab.
   Select an **Email address** , enter a **Product name** if not
   already set, and click the **Save** button.

4. Select the **Credentials** tab, click the **Create credentials**
   button and select **OAuth client ID**.

5. Select the application type **Other** , enter the name
   "YouTube Data API Quickstart", and click the **Create** button.

6. Click **OK** to dismiss the resulting dialog.

7. Click the file_download
   (Download JSON) button to the right of the client ID.

8. Move the downloaded file to your working directory and rename it
   `client_secret.json`.

## Step 2: Install the Google Client Library

Run the following command to install the library:  

    gem install google-api-client

See the library's [installation
page](https://developers.google.com/api-client-library/ruby/start/installation) for the alternative
installation options.

## Step 3: Set up the sample

Create a file named `quickstart.rb` in your working directory and copy in the
following code:


```ruby
# Sample Ruby code for user authorization

require 'rubygems'
gem 'google-api-client', '>0.7'
require 'google/apis'
require 'google/apis/youtube_v3'
require 'googleauth'
require 'googleauth/stores/file_token_store'

require 'fileutils'
require 'json'

# REPLACE WITH VALID REDIRECT_URI FOR YOUR CLIENT
REDIRECT_URI = 'http://localhost'
APPLICATION_NAME = 'YouTube Data API Ruby Tests'

# REPLACE WITH NAME/LOCATION OF YOUR client_secrets.json FILE
CLIENT_SECRETS_PATH = 'client_secret.json'

# REPLACE FINAL ARGUMENT WITH FILE WHERE CREDENTIALS WILL BE STORED
CREDENTIALS_PATH = File.join(Dir.home, '.credentials',
                             "youtube-quickstart-ruby-credentials.yaml")

# SCOPE FOR WHICH THIS SCRIPT REQUESTS AUTHORIZATION
SCOPE = Google::Apis::YoutubeV3::AUTH_YOUTUBE_READONLY

def authorize
  FileUtils.mkdir_p(File.dirname(CREDENTIALS_PATH))

  client_id = Google::Auth::ClientId.from_file(CLIENT_SECRETS_PATH)
  token_store = Google::Auth::Stores::FileTokenStore.new(file: CREDENTIALS_PATH)
  authorizer = Google::Auth::UserAuthorizer.new(
    client_id, SCOPE, token_store)
  user_id = 'default'
  credentials = authorizer.get_credentials(user_id)
  if credentials.nil?
    url = authorizer.get_authorization_url(base_url: REDIRECT_URI)
    puts "Open the following URL in the browser and enter the " +
         "resulting code after authorization"
    puts url
    code = gets
    credentials = authorizer.get_and_store_credentials_from_code(
      user_id: user_id, code: code, base_url: REDIRECT_URI)
  end
  credentials
end

# Initialize the API
service = Google::Apis::YoutubeV3::YouTubeService.new
service.client_options.application_name = APPLICATION_NAME
service.authorization = authorize

# Sample ruby code for channels.list

def channels_list_by_username(service, part, **params)
  response = service.list_channels(part, params).to_json
  item = JSON.parse(response).fetch("items")[0]

  puts ("This channel's ID is #{item.fetch("id")}. " +
        "Its title is '#{item.fetch("snippet").fetch("title")}', and it has " +
        "#{item.fetch("statistics").fetch("viewCount")} views.")
end

channels_list_by_username(service, 'snippet,contentDetails,statistics', for_username: 'GoogleDevelopers')
https://github.com/youtube/api-samples/blob/07263305b59a7c3275bc7e925f9ce6cabf774022/ruby/quickstart.rb
```

<br />

## Step 4: Run the sample

Run the sample using the following command:  

    ruby quickstart.rb

The first time you run the sample, it will prompt you to authorize access:

1. The sample attempts to open a new window or tab in your default browser.
   If this fails, copy the URL from the console and manually open it in
   your browser.

   If you are not already logged into your Google account, you are
   prompted to log in. If you are logged into multiple Google accounts,
   you are asked to select one account to use for the authorization.
2. Click the **Accept** button.
3. Copy the code you're given, paste it into the command-line prompt, and press
   **Enter**. The code may appear in the URL of the page you are redirected to
   after granting authorization:

   ```
   http://localhost/?code=4/nr_1TspmmQPFyifh7nz...OFo#
   ```

It worked! **Great!** Check out the further reading section below to learn more.
I got an error **Bummer.** Thanks for letting us know and we'll work to fix this quickstart.

## Notes

- Authorization information is stored on the file system, so subsequent executions will not prompt for authorization.
- The authorization flow in this example is designed for a command-line application. For information on how to perform authorization in a web application, see [Using OAuth 2.0 for Web Server Applications](https://developers.google.com/youtube/v3/guides/auth/server-side-web-apps).

## Further reading

- [Google Developers Console help documentation](https://developers.google.com/console/help/new)
- [Google APIs Client for Ruby documentation](https://developers.google.com/api-client-library/ruby)
- [YouTube Data API reference documentation](https://developers.google.com/youtube/v3/docs)
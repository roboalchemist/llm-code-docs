# Source: https://developers.google.com/youtube/v3/quickstart/nodejs.md.txt

# Node.js Quickstart

Complete the steps described in the rest of this page, and in about five minutes
you'll have a simple Node.js command-line application that makes requests to the
YouTube Data API.
The sample code used in this guide retrieves the `channel` resource for the GoogleDevelopers YouTube channel and prints some basic information from that resource.

## Prerequisites

To run this quickstart, you'll need:

- Node.js installed.
- The [npm](https://www.npmjs.com/) package management tool (comes with Node.js).
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

## Step 2: Install the client library

Run the following commands to install the libraries using npm:  

    npm install googleapis --save
    npm install google-auth-library --save

## Step 3: Set up the sample

Create a file named `quickstart.js` in your working directory and copy in
the following code:


```javascript
var fs = require('fs');
var readline = require('readline');
var {google} = require('googleapis');
var OAuth2 = google.auth.OAuth2;

// If modifying these scopes, delete your previously saved credentials
// at ~/.credentials/youtube-nodejs-quickstart.json
var SCOPES = ['https://www.googleapis.com/auth/youtube.readonly'];
var TOKEN_DIR = (process.env.HOME || process.env.HOMEPATH ||
    process.env.USERPROFILE) + '/.credentials/';
var TOKEN_PATH = TOKEN_DIR + 'youtube-nodejs-quickstart.json';

// Load client secrets from a local file.
fs.readFile('client_secret.json', function processClientSecrets(err, content) {
  if (err) {
    console.log('Error loading client secret file: ' + err);
    return;
  }
  // Authorize a client with the loaded credentials, then call the YouTube API.
  authorize(JSON.parse(content), getChannel);
});

/**
 * Create an OAuth2 client with the given credentials, and then execute the
 * given callback function.
 *
 * @param {Object} credentials The authorization client credentials.
 * @param {function} callback The callback to call with the authorized client.
 */
function authorize(credentials, callback) {
  var clientSecret = credentials.installed.client_secret;
  var clientId = credentials.installed.client_id;
  var redirectUrl = credentials.installed.redirect_uris[0];
  var oauth2Client = new OAuth2(clientId, clientSecret, redirectUrl);

  // Check if we have previously stored a token.
  fs.readFile(TOKEN_PATH, function(err, token) {
    if (err) {
      getNewToken(oauth2Client, callback);
    } else {
      oauth2Client.credentials = JSON.parse(token);
      callback(oauth2Client);
    }
  });
}

/**
 * Get and store new token after prompting for user authorization, and then
 * execute the given callback with the authorized OAuth2 client.
 *
 * @param {google.auth.OAuth2} oauth2Client The OAuth2 client to get token for.
 * @param {getEventsCallback} callback The callback to call with the authorized
 *     client.
 */
function getNewToken(oauth2Client, callback) {
  var authUrl = oauth2Client.generateAuthUrl({
    access_type: 'offline',
    scope: SCOPES
  });
  console.log('Authorize this app by visiting this url: ', authUrl);
  var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });
  rl.question('Enter the code from that page here: ', function(code) {
    rl.close();
    oauth2Client.getToken(code, function(err, token) {
      if (err) {
        console.log('Error while trying to retrieve access token', err);
        return;
      }
      oauth2Client.credentials = token;
      storeToken(token);
      callback(oauth2Client);
    });
  });
}

/**
 * Store token to disk be used in later program executions.
 *
 * @param {Object} token The token to store to disk.
 */
function storeToken(token) {
  try {
    fs.mkdirSync(TOKEN_DIR);
  } catch (err) {
    if (err.code != 'EEXIST') {
      throw err;
    }
  }
  fs.writeFile(TOKEN_PATH, JSON.stringify(token), (err) => {
    if (err) throw err;
    console.log('Token stored to ' + TOKEN_PATH);
  });
}

/**
 * Lists the names and IDs of up to 10 files.
 *
 * @param {google.auth.OAuth2} auth An authorized OAuth2 client.
 */
function getChannel(auth) {
  var service = google.youtube('v3');
  service.channels.list({
    auth: auth,
    part: 'snippet,contentDetails,statistics',
    forUsername: 'GoogleDevelopers'
  }, function(err, response) {
    if (err) {
      console.log('The API returned an error: ' + err);
      return;
    }
    var channels = response.data.items;
    if (channels.length == 0) {
      console.log('No channel found.');
    } else {
      console.log('This channel\'s ID is %s. Its title is \'%s\', and ' +
                  'it has %s views.',
                  channels[0].id,
                  channels[0].snippet.title,
                  channels[0].statistics.viewCount);
    }
  });
}
https://github.com/youtube/api-samples/blob/07263305b59a7c3275bc7e925f9ce6cabf774022/javascript/nodejs-quickstart.js
```

<br />

## Step 4: Run the sample

Run the sample using the following command:  

    node quickstart.js

The first time you run the sample, it will prompt you to authorize access:

1. Browse to the provided URL in your web browser.

   If you are not already logged into your Google account, you will be
   prompted to log in. If you are logged into multiple Google accounts, you
   will be asked to select one account to use for the authorization.
2. Click the **Accept** button.
3. Copy the code you're given, paste it into the command-line prompt, and press **Enter**.

It worked! **Great!** Check out the further reading section below to learn more.
I got an error **Bummer.** Thanks for letting us know and we'll work to fix this quickstart.

## Notes

- Authorization information is stored on the file system, so subsequent executions will not prompt for authorization.
- The authorization flow in this example is designed for a command line application. For information on how to perform authorization in a web application that uses the YouTube Data API, see [Using OAuth 2.0 for Web Server Applications](https://developers.google.com/youtube/v3/guides/auth/server-side-web-apps).   

  For information on how to perform authorization in other contexts, see the [Authorizing and Authenticating](https://github.com/google/google-api-nodejs-client/#authorizing-and-authenticating) section of the library's README.

## Further reading

- [Google Developers Console help documentation](https://developers.google.com/console/help/new)
- [Google APIs Client for Node.js documentation](https://github.com/google/google-api-nodejs-client/#google-apis-nodejs-client)
- [YouTube Data API reference documentation](https://developers.google.com/youtube/v3/docs)
# Source: https://developers.google.com/youtube/v3/quickstart/go.md.txt

# Go Quickstart

Complete the steps described in the rest of this page, and in about five minutes
you'll have a simple Go command-line application that makes requests to the
YouTube Data API.
The sample code used in this guide retrieves the `channel` resource for the GoogleDevelopers YouTube channel and prints some basic information from that resource.

## Prerequisites

To run this quickstart, you'll need:

- [Go](https://golang.org/), latest version recommended.
- [Git](https://git-scm.com/), latest version recommended.
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

## Step 2: Prepare the workspace

1. Set the `GOPATH` environment variable to your working directory.
2. Get the YouTube Data API Go client library and OAuth2 package using the following commands:

    go get -u google.golang.org/api/youtube/v3
    go get -u golang.org/x/oauth2/...

## Step 3: Set up the sample

Create a file named `quickstart.go` in your working directory and copy
in the following code:


```go
// Sample Go code for user authorization

package main

import (
  "encoding/json"
  "fmt"
  "log"
  "io/ioutil"
  "net/http"
  "net/url"
  "os"
  "os/user"
  "path/filepath"

  "golang.org/x/net/context"
  "golang.org/x/oauth2"
  "golang.org/x/oauth2/google"
  "google.golang.org/api/youtube/v3"
)

const missingClientSecretsMessage = `
Please configure OAuth 2.0
`

// getClient uses a Context and Config to retrieve a Token
// then generate a Client. It returns the generated Client.
func getClient(ctx context.Context, config *oauth2.Config) *http.Client {
  cacheFile, err := tokenCacheFile()
  if err != nil {
    log.Fatalf("Unable to get path to cached credential file. %v", err)
  }
  tok, err := tokenFromFile(cacheFile)
  if err != nil {
    tok = getTokenFromWeb(config)
    saveToken(cacheFile, tok)
  }
  return config.Client(ctx, tok)
}

// getTokenFromWeb uses Config to request a Token.
// It returns the retrieved Token.
func getTokenFromWeb(config *oauth2.Config) *oauth2.Token {
  authURL := config.AuthCodeURL("state-token", oauth2.AccessTypeOffline)
  fmt.Printf("Go to the following link in your browser then type the "+
    "authorization code: \n%v\n", authURL)

  var code string
  if _, err := fmt.Scan(&code); err != nil {
    log.Fatalf("Unable to read authorization code %v", err)
  }

  tok, err := config.Exchange(oauth2.NoContext, code)
  if err != nil {
    log.Fatalf("Unable to retrieve token from web %v", err)
  }
  return tok
}

// tokenCacheFile generates credential file path/filename.
// It returns the generated credential path/filename.
func tokenCacheFile() (string, error) {
  usr, err := user.Current()
  if err != nil {
    return "", err
  }
  tokenCacheDir := filepath.Join(usr.HomeDir, ".credentials")
  os.MkdirAll(tokenCacheDir, 0700)
  return filepath.Join(tokenCacheDir,
    url.QueryEscape("youtube-go-quickstart.json")), err
}

// tokenFromFile retrieves a Token from a given file path.
// It returns the retrieved Token and any read error encountered.
func tokenFromFile(file string) (*oauth2.Token, error) {
  f, err := os.Open(file)
  if err != nil {
    return nil, err
  }
  t := &oauth2.Token{}
  err = json.NewDecoder(f).Decode(t)
  defer f.Close()
  return t, err
}

// saveToken uses a file path to create a file and store the
// token in it.
func saveToken(file string, token *oauth2.Token) {
  fmt.Printf("Saving credential file to: %s\n", file)
  f, err := os.OpenFile(file, os.O_RDWR|os.O_CREATE|os.O_TRUNC, 0600)
  if err != nil {
    log.Fatalf("Unable to cache oauth token: %v", err)
  }
  defer f.Close()
  json.NewEncoder(f).Encode(token)
}

func handleError(err error, message string) {
  if message == "" {
    message = "Error making API call"
  }
  if err != nil {
    log.Fatalf(message + ": %v", err.Error())
  }
}

func channelsListByUsername(service *youtube.Service, part string, forUsername string) {
  call := service.Channels.List(part)
  call = call.ForUsername(forUsername)
  response, err := call.Do()
  handleError(err, "")
  fmt.Println(fmt.Sprintf("This channel's ID is %s. Its title is '%s', " +
              "and it has %d views.",
              response.Items[0].Id,
              response.Items[0].Snippet.Title,
              response.Items[0].Statistics.ViewCount))
}


func main() {
  ctx := context.Background()

  b, err := ioutil.ReadFile("client_secret.json")
  if err != nil {
    log.Fatalf("Unable to read client secret file: %v", err)
  }

  // If modifying these scopes, delete your previously saved credentials
  // at ~/.credentials/youtube-go-quickstart.json
  config, err := google.ConfigFromJSON(b, youtube.YoutubeReadonlyScope)
  if err != nil {
    log.Fatalf("Unable to parse client secret file to config: %v", err)
  }
  client := getClient(ctx, config)
  service, err := youtube.New(client)

  handleError(err, "Error creating YouTube client")

  channelsListByUsername(service, "snippet,contentDetails,statistics", "GoogleDevelopers")
}
https://github.com/youtube/api-samples/blob/07263305b59a7c3275bc7e925f9ce6cabf774022/go/quickstart.go
```

<br />

## Step 4: Run the sample

Build and run the sample using the following command from your working
directory:  

    go run quickstart.go

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
- The authorization flow in this example is designed for a command-line application. For information on how to perform authorization in a web application, see [Using OAuth 2.0 for Web Server Applications](https://developers.google.com/youtube/v3/guides/auth/server-side-web-apps).

## Further reading

- [Google Developers Console help documentation](https://developers.google.com/console/help/new)
- [Google APIs Client for Go](https://github.com/google/google-api-go-client)
- [YouTube Data API reference documentation](https://developers.google.com/youtube/v3/docs)
# Source: https://developers.google.com/youtube/v3/code_samples/go.md.txt

# Go Code Samples

The following code samples, which use the [Google APIs Client Library for Go](https://github.com/google/google-api-go-client), are available for the YouTube Data API. You can download these code samples from the `go` folder of the [YouTube APIs code sample repository on GitHub](https://github.com/youtube/api-samples).

## Authorize a request

This code sample performs OAuth 2.0 authorization by checking for the presence of a local file that
contains authorization credentials. If the file is not present, the script opens a browser and waits for a response,
then saves the returned credentials locally.  

```go
package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net"
	"net/http"
	"net/url"
	"os"
	"os/exec"
	"os/user"
	"path/filepath"
	"runtime"

	"golang.org/x/net/context"
	"golang.org/x/oauth2"
	"golang.org/x/oauth2/google"
)

// This variable indicates whether the script should launch a web server to
// initiate the authorization flow or just display the URL in the terminal
// window. Note the following instructions based on this setting:
// * launchWebServer = true
//   1. Use OAuth2 credentials for a web application
//   2. Define authorized redirect URIs for the credential in the Google APIs
//      Console and set the RedirectURL property on the config object to one
//      of those redirect URIs. For example:
//      config.RedirectURL = "http://localhost:8090"
//   3. In the startWebServer function below, update the URL in this line
//      to match the redirect URI you selected:
//         listener, err := net.Listen("tcp", "localhost:8090")
//      The redirect URI identifies the URI to which the user is sent after
//      completing the authorization flow. The listener then captures the
//      authorization code in the URL and passes it back to this script.
// * launchWebServer = false
//   1. Use OAuth2 credentials for an installed application. (When choosing
//      the application type for the OAuth2 client ID, select "Other".)
//   2. Set the redirect URI to "urn:ietf:wg:oauth:2.0:oob", like this:
//      config.RedirectURL = "urn:ietf:wg:oauth:2.0:oob"
//   3. When running the script, complete the auth flow. Then copy the
//      authorization code from the browser and enter it on the command line.
const launchWebServer = false

const missingClientSecretsMessage = `
Please configure OAuth 2.0
To make this sample run, you need to populate the client_secrets.json file
found at:
   %v
with information from the {{ Google Cloud Console }}
{{ https://cloud.google.com/console }}
For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
`

// getClient uses a Context and Config to retrieve a Token
// then generate a Client. It returns the generated Client.
func getClient(scope string) *http.Client {
	ctx := context.Background()
	
	b, err := ioutil.ReadFile("client_secret.json")
	if err != nil {
		log.Fatalf("Unable to read client secret file: %v", err)
	}
	
	// If modifying the scope, delete your previously saved credentials
	// at ~/.credentials/youtube-go.json
	config, err := google.ConfigFromJSON(b, scope)
	if err != nil {
		log.Fatalf("Unable to parse client secret file to config: %v", err)
	}
	
	// Use a redirect URI like this for a web app. The redirect URI must be a
	// valid one for your OAuth2 credentials.
	config.RedirectURL = "http://localhost:8090"
	// Use the following redirect URI if launchWebServer=false in oauth2.go
	// config.RedirectURL = "urn:ietf:wg:oauth:2.0:oob"
	
	cacheFile, err := tokenCacheFile()
	if err != nil {
		log.Fatalf("Unable to get path to cached credential file. %v", err)
	}
	tok, err := tokenFromFile(cacheFile)
	if err != nil {
		authURL := config.AuthCodeURL("state-token", oauth2.AccessTypeOffline)
		if launchWebServer {
			fmt.Println("Trying to get token from web")
			tok, err = getTokenFromWeb(config, authURL)
		} else {
			fmt.Println("Trying to get token from prompt")
			tok, err = getTokenFromPrompt(config, authURL)
		}
		if err == nil {
			saveToken(cacheFile, tok)
		}
	}
	return config.Client(ctx, tok)
}

// startWebServer starts a web server that listens on http://localhost:8080.
// The webserver waits for an oauth code in the three-legged auth flow.
func startWebServer() (codeCh chan string, err error) {
	listener, err := net.Listen("tcp", "localhost:8090")
	if err != nil {
		return nil, err
	}
	codeCh = make(chan string)

	go http.Serve(listener, http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		code := r.FormValue("code")
		codeCh <- code // send code to OAuth flow
		listener.Close()
		w.Header().Set("Content-Type", "text/plain")
		fmt.Fprintf(w, "Received code: %v\r\nYou can now safely close this browser window.", code)
	}))

	return codeCh, nil
}

// openURL opens a browser window to the specified location.
// This code originally appeared at:
//   http://stackoverflow.com/questions/10377243/how-can-i-launch-a-process-that-is-not-a-file-in-go
func openURL(url string) error {
	var err error
	switch runtime.GOOS {
	case "linux":
		err = exec.Command("xdg-open", url).Start()
	case "windows":
		err = exec.Command("rundll32", "url.dll,FileProtocolHandler", "http://localhost:4001/").Start()
	case "darwin":
		err = exec.Command("open", url).Start()
	default:
		err = fmt.Errorf("Cannot open URL %s on this platform", url)
	}
	return err
}

// Exchange the authorization code for an access token
func exchangeToken(config *oauth2.Config, code string) (*oauth2.Token, error) {
	tok, err := config.Exchange(oauth2.NoContext, code)
	if err != nil {
		log.Fatalf("Unable to retrieve token %v", err)
	}
	return tok, nil
}

// getTokenFromPrompt uses Config to request a Token and prompts the user
// to enter the token on the command line. It returns the retrieved Token.
func getTokenFromPrompt(config *oauth2.Config, authURL string) (*oauth2.Token, error) {
	var code string
	fmt.Printf("Go to the following link in your browser. After completing " +
		"the authorization flow, enter the authorization code on the command " +
		"line: \n%v\n", authURL)

	if _, err := fmt.Scan(&code); err != nil {
		log.Fatalf("Unable to read authorization code %v", err)
	}
	fmt.Println(authURL)
	return exchangeToken(config, code)
}

// getTokenFromWeb uses Config to request a Token.
// It returns the retrieved Token.
func getTokenFromWeb(config *oauth2.Config, authURL string) (*oauth2.Token, error) {
	codeCh, err := startWebServer()
	if err != nil {
		fmt.Printf("Unable to start a web server.")
		return nil, err
	}

	err = openURL(authURL)
	if err != nil {
		log.Fatalf("Unable to open authorization URL in web server: %v", err)
	} else {
		fmt.Println("Your browser has been opened to an authorization URL.",
			" This program will resume once authorization has been provided.\n")
		fmt.Println(authURL)
	}

	// Wait for the web server to get the code.
	code := <-codeCh
	return exchangeToken(config, code)
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
		url.QueryEscape("youtube-go.json")), err
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
	fmt.Println("trying to save token")
	fmt.Printf("Saving credential file to: %s\n", file)
	f, err := os.OpenFile(file, os.O_RDWR|os.O_CREATE|os.O_TRUNC, 0600)
	if err != nil {
		log.Fatalf("Unable to cache oauth token: %v", err)
	}
	defer f.Close()
	json.NewEncoder(f).Encode(token)
}
https://github.com/youtube/api-samples/blob/07263305b59a7c3275bc7e925f9ce6cabf774022/go/oauth2.go
```

## List playlists

This code sample calls the API's `playlists.list` method. Use command-line flags to
define the parameters you want to use in the request as shown in the following examples:  

```
# Retrieve playlists for a specified channel
go run playlists.go oauth.go errors.go --channelId=UC_x5XG1OV2P6uZZ5FSM9Ttw

# Retrieve authenticated user's playlists
go run playlists.go oauth.go errors.go --mine=true
```  

```go
package main

import (
        "flag"
        "fmt"
        "log"

        "google.golang.org/api/youtube/v3"
)

var (
        method = flag.String("method", "list", "The API method to execute. (List is the only method that this sample currently supports.")

        channelId       = flag.String("channelId", "", "Retrieve playlists for this channel. Value is a YouTube channel ID.")
        hl    = flag.String("hl", "", "Retrieve localized resource metadata for the specified application language.")
        maxResults    = flag.Int64("maxResults", 5, "The maximum number of playlist resources to include in the API response.")
        mine    = flag.Bool("mine", false, "List playlists for authenticated user's channel. Default: false.")
        onBehalfOfContentOwner    = flag.String("onBehalfOfContentOwner", "", "Indicates that the request's auth credentials identify a user authorized to act on behalf of the specified content owner.")
        pageToken    = flag.String("pageToken", "", "Token that identifies a specific page in the result set that should be returned.")
        part    = flag.String("part", "snippet", "Comma-separated list of playlist resource parts that API response will include.")
        playlistId       = flag.String("playlistId", "", "Retrieve information about this playlist.")
)

func playlistsList(service *youtube.Service, part string, channelId string, hl string, maxResults int64, mine bool, onBehalfOfContentOwner string, pageToken string, playlistId string) *youtube.PlaylistListResponse {
        call := service.Playlists.List(part)
        if channelId != "" {
                call = call.ChannelId(channelId)
        }
        if hl != "" {
                call = call.Hl(hl)
        }
        call = call.MaxResults(maxResults)
        if mine != false {
                call = call.Mine(true)
        }
        if onBehalfOfContentOwner != "" {
                call = call.OnBehalfOfContentOwner(onBehalfOfContentOwner)
        }
        if pageToken != "" {
                call = call.PageToken(pageToken)
        }
        if playlistId != "" {
                call = call.Id(playlistId)
        }
        response, err := call.Do()
        handleError(err, "")
        return response
}

func main() {
        flag.Parse()

        if *channelId == "" && *mine == false && *playlistId == "" {
                log.Fatalf("You must either set a value for the channelId or playlistId flag or set the mine flag to 'true'.")
        }
        client := getClient(youtube.YoutubeReadonlyScope)

        service, err := youtube.New(client)
        if err != nil {
                log.Fatalf("Error creating YouTube client: %v", err)
        }

        response := playlistsList(service, "snippet,contentDetails", *channelId, *hl, *maxResults, *mine, *onBehalfOfContentOwner, *pageToken, *playlistId)

        for _, playlist := range response.Items {
                playlistId := playlist.Id
                playlistTitle := playlist.Snippet.Title

                // Print the playlist ID and title for the playlist resource.
                fmt.Println(playlistId, ": ", playlistTitle)
        }
}
https://github.com/youtube/api-samples/blob/07263305b59a7c3275bc7e925f9ce6cabf774022/go/playlists.go
```

## Retrieve my uploads

This code sample calls the API's `playlistItems.list` method to retrieve a list of
videos uploaded to the channel associated with the request. The code also calls the `channels.list`
method with the `mine` parameter set to `true` to retrieve the playlist ID that identifies
the channel's uploaded videos.  

```go
package main

import (
	"fmt"
	"log"

	"google.golang.org/api/youtube/v3"
)

// Retrieve playlistItems in the specified playlist
func playlistItemsList(service *youtube.Service, part string, playlistId string, pageToken string) *youtube.PlaylistItemListResponse {
	call := service.PlaylistItems.List(part)
	call = call.PlaylistId(playlistId)
	if pageToken != "" {
		call = call.PageToken(pageToken)
	}
	response, err := call.Do()
	handleError(err, "")
	return response
}

// Retrieve resource for the authenticated user's channel
func channelsListMine(service *youtube.Service, part string) *youtube.ChannelListResponse {
	call := service.Channels.List(part)
	call = call.Mine(true)
	response, err := call.Do()
	handleError(err, "")
	return response
}

func main() {
	client := getClient(youtube.YoutubeReadonlyScope)
	service, err := youtube.New(client)
	
	if err != nil {
		log.Fatalf("Error creating YouTube client: %v", err)
	}

	response := channelsListMine(service, "contentDetails")

	for _, channel := range response.Items {
		playlistId := channel.ContentDetails.RelatedPlaylists.Uploads
		
		// Print the playlist ID for the list of uploaded videos.
		fmt.Printf("Videos in list %s\r\n", playlistId)

		nextPageToken := ""
		for {
			// Retrieve next set of items in the playlist.
			playlistResponse := playlistItemsList(service, "snippet", playlistId, nextPageToken)
			
			for _, playlistItem := range playlistResponse.Items {
				title := playlistItem.Snippet.Title
				videoId := playlistItem.Snippet.ResourceId.VideoId
				fmt.Printf("%v, (%v)\r\n", title, videoId)
			}

			// Set the token to retrieve the next page of results
			// or exit the loop if all results have been retrieved.
			nextPageToken = playlistResponse.NextPageToken
			if nextPageToken == "" {
				break
			}
			fmt.Println()
		}
	}
}
https://github.com/youtube/api-samples/blob/07263305b59a7c3275bc7e925f9ce6cabf774022/go/my_uploads.go
```

## Search by keyword

This code sample calls the API's `search.list` method to retrieve search results associated
with a particular keyword.  

```go
package main

import (
	"flag"
	"fmt"
	"log"
	"net/http"

	"google.golang.org/api/googleapi/transport"
	"google.golang.org/api/youtube/v3"
)

var (
	query      = flag.String("query", "Google", "Search term")
	maxResults = flag.Int64("max-results", 25, "Max YouTube results")
)

const developerKey = "YOUR DEVELOPER KEY"

func main() {
	flag.Parse()

	client := &http.Client{
		Transport: &transport.APIKey{Key: developerKey},
	}

	service, err := youtube.New(client)
	if err != nil {
		log.Fatalf("Error creating new YouTube client: %v", err)
	}

	// Make the API call to YouTube.
	call := service.Search.List("id,snippet").
		Q(*query).
		MaxResults(*maxResults)
	response, err := call.Do()
	handleError(err, "")

	// Group video, channel, and playlist results in separate lists.
	videos := make(map[string]string)
	channels := make(map[string]string)
	playlists := make(map[string]string)

	// Iterate through each item and add it to the correct list.
	for _, item := range response.Items {
		switch item.Id.Kind {
		case "youtube#video":
			videos[item.Id.VideoId] = item.Snippet.Title
		case "youtube#channel":
			channels[item.Id.ChannelId] = item.Snippet.Title
		case "youtube#playlist":
			playlists[item.Id.PlaylistId] = item.Snippet.Title
		}
	}

	printIDs("Videos", videos)
	printIDs("Channels", channels)
	printIDs("Playlists", playlists)
}

// Print the ID and title of each result in a list as well as a name that
// identifies the list. For example, print the word section name "Videos"
// above a list of video search results, followed by the video ID and title
// of each matching video.
func printIDs(sectionName string, matches map[string]string) {
	fmt.Printf("%v:\n", sectionName)
	for id, title := range matches {
		fmt.Printf("[%v] %v\n", id, title)
	}
	fmt.Printf("\n\n")
}
https://github.com/youtube/api-samples/blob/07263305b59a7c3275bc7e925f9ce6cabf774022/go/search_by_keyword.go
```

## Upload a video

This code sample calls the API's `videos.insert` method to upload a video to the channel
associated with the request.  

```go
package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"strings"

	"google.golang.org/api/youtube/v3"
)

var (
	filename    = flag.String("filename", "", "Name of video file to upload")
	title       = flag.String("title", "Test Title", "Video title")
	description = flag.String("description", "Test Description", "Video description")
	category    = flag.String("category", "22", "Video category")
	keywords    = flag.String("keywords", "", "Comma separated list of video keywords")
	privacy     = flag.String("privacy", "unlisted", "Video privacy status")
)

func main() {
	flag.Parse()

	if *filename == "" {
		log.Fatalf("You must provide a filename of a video file to upload")
	}

	client := getClient(youtube.YoutubeUploadScope)

	service, err := youtube.New(client)
	if err != nil {
		log.Fatalf("Error creating YouTube client: %v", err)
	}

	upload := &youtube.Video{
		Snippet: &youtube.VideoSnippet{
			Title:       *title,
			Description: *description,
			CategoryId:  *category,
		},
		Status: &youtube.VideoStatus{PrivacyStatus: *privacy},
	}

	// The API returns a 400 Bad Request response if tags is an empty string.
	if strings.Trim(*keywords, "") != "" {
		upload.Snippet.Tags = strings.Split(*keywords, ",")
	}

	call := service.Videos.Insert("snippet,status", upload)

	file, err := os.Open(*filename)
	defer file.Close()
	if err != nil {
		log.Fatalf("Error opening %v: %v", *filename, err)
	}

	response, err := call.Media(file).Do()
	handleError(err, "")
	fmt.Printf("Upload successful! Video ID: %v\n", response.Id)
}
https://github.com/youtube/api-samples/blob/07263305b59a7c3275bc7e925f9ce6cabf774022/go/upload_video.go
```
# Source: https://developers.google.com/youtube/v3/quickstart/js.md.txt

# JavaScript Quickstart

This quickstart guide explains how to set up a simple page that makes requests
to the YouTube Data API. This quickstart actually explains how to make two API
requests:

1. You will use an API key, which identifies your application, to retrieve information about the GoogleDevelopers YouTube channel.
2. You will use an OAuth 2.0 client ID to submit an *authorized* request that retrieves information about your own YouTube channel.

| **Note:** More generally, you can follow the instructions for the first example for any use case that uses an API key or the instructions for the second example for any use case that requires authorization using OAuth 2.0. See the [use cases and code samples tool](https://developers.google.com/youtube/v3/code_samples/code_snippets) for more examples.

## Prerequisites

To run this quickstart, you'll need:

- Python 2.4 or greater (to provide a web server)
- Access to the internet and a web browser.
- A Google account.

## Step 1: Set up your project and credentials

Create or select a project in the [API Console](https://console.cloud.google.com/). Complete the following tasks in the API Console for your project:

1. In the [library panel](https://console.developers.google.com/apis/library),
   search for the YouTube Data API v3. Click into the listing for that API and
   make sure the API is enabled for your project.

2. In the [credentials
   panel](https://console.developers.google.com/apis/credentials),
   create two credentials:

   1. **Create an API key**
      You will use the API key to make API requests that do
      not require user authorization. For example, you do not need user
      authorization to retrieve information about a public YouTube channel.

   2. **Create an OAuth 2.0 client ID**

      Set the application type to **Web application**. You need to use OAuth
      2.0 credentials for requests that require user authorization. For
      example, you need user authorization to retrieve information about the
      currently authenticated user's YouTube channel.

      In the **Authorized JavaScript origins** field, enter the URL
      `http://localhost:8000`. You can leave the **Authorized redirect URIs**
      field blank.

## Step 2: Set up and run the sample

Use the APIs Explorer widget in the side panel to obtain sample code for
retrieving information about the GoogleDevelopers YouTube channel. This request
uses an API key to identify your application, and it does not require user
authorization or any special permissions from the user running the sample.

1. Open the documentation for the API's [channels.list](https://developers.google.com/youtube/v3/docs/channels/list) method.
2. On that page, the "Common use cases" section contains a table that explains
   several common ways that the method is used. The first listing in the table
   is for listing results by channel ID.

   Click the code symbol for the first listing to open and populate the
   fullscreen APIs Explorer.

   ![Image that identifies the location of the code symbol link in the
   table that lists use cases for the channels.list documentation. The alt text
   for that image identifies the image as a code symbol and specifies the
   use case associated with that link.](https://developers.google.com/static/youtube/v3/quickstart/images/open_fullscreen_apis_explorer.png)
3. The left side of the fullscreen APIs Explorer shows the following:

   1. Below the **Request parameters** header, there is a list of parameters
      that the method supports. The `part` and `id` parameter values should
      be set. The `id` parameter value, `UC_x5XG1OV2P6uZZ5FSM9Ttw`, is the
      ID for the GoogleDevelopers YouTube channel.

   2. Below the parameters, there is a section named **Credentials** . The
      pulldown menu in that section should display the value **API key**. The
      APIs Explorer uses demo credentials by default to make it easier to get
      started. But you'll use your own API key to run the sample locally.

      ![Image that shows the 'Credentials' in the fullscreen APIs Explorer
      and the pulldown menu with the 'API key' option selected.](https://developers.google.com/static/youtube/v3/quickstart/images/apis_explorer_credentials.png)
4. The right side of the fullscreen APIs Explorer shows tabs with code samples
   in different languages. Select the **JavaScript** tab.

5. Copy the code sample and save it in a file named
   `example.html`.

6. In the sample that you downloaded, find the `YOUR_API_KEY` string and
   replace that with the API key that you created in step 1 of this quickstart.

7. Start the web server using the following command from your working
   directory:

   ### Python 2.x

       python -m SimpleHTTPServer 8000

   ### Python 3.x

       python -m http.server 8000

8. Open the example.html file in your browser. Also open the browser's
   developer tools, such as the "Developer Tools" in the Chrome browser.

   1. Click the **load** button on the page to load the Google APIs Client
      Library for JavaScript. After you click the button, the developer
      console should display a note indicating that the GAPI client loaded.

   2. Click the **execute** button to send the API request. The developer's
      console should then display the API response.

## Step 3: Run an authorized request

In this step, you'll modify your code sample so that instead of retrieving
information about the GoogleDevelopers YouTube channel, it retrieves information
about *your* YouTube channel. This request does require user authorization.

1. Go back to the documentation for the API's
   [channels.list](https://developers.google.com/youtube/v3/docs/channels/list) method.

2. In the "Common use cases" section, click the code symbol for the third
   listing in the table. That use case is to call the `list` method for "my
   channel."

3. Again, in the left side of the fullscreen APIs Explorer, you will see a
   list of parameters followed by the **Credentials** section. However, there
   are two changes from the example where you retrieved information about the
   GoogleDevelopers channel:

   1. In the parameters section, instead of the `id` parameter value being
      set, the `mine` parameter value should be set to `true`. This instructs
      the API server to retrieve information about the currently authenticated
      user's channel.

   2. In the **Credentials** section, the pulldown menu should select the
      option for **Google OAuth 2.0**.

      In addition, if you click the **Show scopes** link, the
      **https://www.googleapis.com/auth/youtube.readonly** scope should be
      checked.

      ![Image that shows scopes in the fullscreen APIs Explorer and the
      option to use 'Google OAuth 2.0' credentials selected.](https://developers.google.com/static/youtube/v3/quickstart/images/apis_explorer_scopes.png)
4. As with the previous example, select the **JavaScript** tab,
   copy the code sample, and save it to `example.html`.

   In the code, find the `YOUR_CLIENT_ID` string and replace it with the
   client ID that you created in step 1 of this quickstart.
5. Start the web server using the following command from your working
   directory:

   ### Python 2.x

       python -m SimpleHTTPServer 8000

   ### Python 3.x

       python -m http.server 8000

6. Go to `http://localhost:8000/example.html` file in your browser.
   Open the browser's developer tools, such as the "Developer Tools" in the
   Chrome browser.

7. Click the **authorize and load** button on the page to load the Google
   APIs Client Library for JavaScript and initiate the authorization flow.
   You should be prompted to grant the application permission to read data
   from your YouTube account.

   If you grant the permission, the developer's console should display
   messages indicating that sign-in was successful and that the API client
   loaded.
8. Click the **execute** button to send the API request. The developer's
   console should then display the API response.

## Further reading

- [Google Developers Console help documentation](https://developers.google.com/console/help/new)
- [Google APIs Client Library for JavaScript documentation](https://developers.google.com/api-client-library/javascript)
- [YouTube Data API reference documentation](https://developers.google.com/youtube/v3/docs)
# Source: https://developers.google.com/youtube/v3/quickstart/java.md.txt

# Java Quickstart

This quickstart guide explains how to set up a simple, Java
command-line application that makes requests to the YouTube Data API. This
quickstart actually explains how to make two API requests:

1. You will use an API key, which identifies your application, to retrieve information about the GoogleDevelopers YouTube channel.
2. You will use an OAuth 2.0 client ID to submit an *authorized* request that retrieves information about your own YouTube channel.

| **Note:** More generally, you can follow the instructions for the first example for any use case that uses an API key or the instructions for the second example for any use case that requires authorization using OAuth 2.0. See the [use cases and code samples tool](https://developers.google.com/youtube/v3/code_samples/code_snippets) for more examples.

## Prerequisites

To run this quickstart, you'll need:

- Java 1.7 or greater.
- [Gradle 2.3 or greater](http://gradle.org/downloads).
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

      Set the application type to **Other**. You need to use OAuth 2.0
      credentials for requests that require user authorization. For example,
      you need user authorization to retrieve information about the currently
      authenticated user's YouTube channel.

      Download the JSON file that contains your OAuth 2.0 credentials. The
      file has a name like `client_secret_CLIENTID.json`, where `CLIENTID` is
      the client ID for your project.

## Step 2: Prepare the project

Complete the following steps to prepare your Gradle project:

1. In your working directory, run the following commands to create a new
   project structure:

       $ gradle init --type basic
       $ mkdir -p src/main/java src/main/resources

2. Move the JSON file that you downloaded after creating your OAuth 2.0 client
   ID to the `src/main/resources` directory below your working directory, and
   rename the file to `client_secret.json`.

3. Open the `build.gradle` file in your working directory and replace its
   contents with the following:

   ```java
   apply plugin: 'java'
   apply plugin: 'application'

   mainClassName = 'ApiExample'
   sourceCompatibility = 1.7
   targetCompatibility = 1.7
   version = '1.0'

   repositories {
       mavenCentral()
   }

   dependencies {
       compile 'com.google.api-client:google-api-client:1.23.0'
       compile 'com.google.oauth-client:google-oauth-client-jetty:1.23.0'
       compile 'com.google.apis:google-api-services-youtube:v3-rev<var translate="no">REVISION</var>-CL_VERSION'
   }
   ```
4. In the `build.gradle` file, you need to replace the
   <var translate="no">REVISION</var> and <var translate="no">CL_VERSION</var> variables with two values from
   the [client library
   documentation](https://developers.google.com/resources/api-libraries/documentation/youtube/v3/java/latest/)
   for the YouTube Data API. The screenshot below, which shows the
   documentation for the YouTube Analytics API, shows where the two variables
   appear on the page.

   ![Screenshot of JavaDoc reference showing how to find values for 'REVISION' and 'CL_VERSION' variables](https://developers.google.com/static/explorer-help/guides/images/apis-explorer-java-client-library-version.png)

## Step 3: Set up and run the sample

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
   in different languages. Select the **Java** tab.

5. Copy the code sample and save it in a file named
   `src/main/java/ApiExample.java`.

   Every sample uses the same class name (`ApiExample`) so that you don't
   need to modify the `build.gradle` file to run different samples.

6. In the sample that you downloaded, find the `YOUR_API_KEY` string and
   replace that with the API key that you created in step 1 of this quickstart.

7. Run the sample from the command line. In your working directory, run:


   `gradle -q run`


8. The sample should execute the request and print the response to `STDOUT`.

## Step 4: Run an authorized request

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
4. As with the previous example, select the **Java** tab,
   copy the code sample, and save it to `src/main/java/ApiExample.java`.

   <br />

5. Run the sample from the command line. In your working directory, run:


   `gradle -q run`


6.
   The sample should attempt to open a new window or tab in your default
   browser. If this fails, copy the URL from the terminal and manually open it
   in your browser.

   <br />

   If you are not already logged into your Google account, you will be
   prompted to log in. If you are logged into multiple Google accounts, you
   will be asked to select one account to use for the authorization.
7. Click the button to grant your application access to the scopes specified in
   your code sample.

8.
   The sample will proceed automatically, and you may close the browser tab
   used for the auth flow.

   <br />

   The API response should again be printed to `STDOUT`.

## Further reading

- [Google Developers Console help documentation](https://developers.google.com/console/help/new)
- [Google APIs Client Library for Java documentation](https://developers.google.com/api-client-library/java)
- [YouTube Data API Javadoc documentation](https://developers.google.com/resources/api-libraries/documentation/youtube/v3/java/latest)
- [YouTube Data API reference documentation](https://developers.google.com/youtube/v3/docs)
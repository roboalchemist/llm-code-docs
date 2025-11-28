# Source: https://developers.google.com/youtube/v3/guides/moving_to_oauth.md.txt

# Move from ClientLogin to OAuth 2.0

*Ikai Lan, YouTube Developer Relations -- June 2013*
YouTube APIs use [OAuth 2.0](https://developers.google.com/youtube/v3/guides/authentication) to authorize user requests. We are frequently asked whether we will add support for ClientLogin authentication or something similar in YouTube APIs going forward. However, we [officially deprecated ClientLogin as of April 20, 2012](https://developers.google.com/youtube/2.0/developers_guide_protocol_clientlogin), and there are no plans to add such a mechanism.

There are numerous reasons why we believe supporting various flows of OAuth 2.0 authorization is better for YouTube users than ClientLogin. These flows support use cases for desktop applications, web-only applications, native mobile applications, and even applications that run on devices like televisions that don't have sophisticated input mechanisms, something which is difficult to do using ClientLogin. Also, we've found that ClientLogin causes more headaches post-launch for many developers, some of which we describe in our blog post, [ClientLogin #FAIL](http://apiblog.youtube.com/2011/03/clientlogin-fail.html).

## Using OAuth 2.0 for server-side, standalone scripts

Many developers use ClientLogin to authorize command-line scripts that run on servers without a browser. With OAuth 2.0, there's almost always going to be a browser involved -- the exception being when you're working on an Android application that uses Google Play Services to fetch tokens via [GoogleAuthUtil.](http://developer.android.com/reference/com/google/android/gms/auth/GoogleAuthUtil.html)

In a [web-only flow](https://developers.google.com/accounts/docs/OAuth2WebServer), a website that wants to make authenticated API calls on behalf of a user must redirect the user to a google.com authentication page that explains what the application is trying to access. The web application then receives a token, which it uses to make API calls. The user can then revoke the application's access at any time using the [connected apps and sites](https://accounts.google.com/IssuedAuthSubTokens) page.

Our [Python code samples](https://developers.google.com/youtube/v3/code_samples/python) demonstrate how command-line scripts can launch a browser and make API calls from a terminal window, create a local server to listen for the code after the authorization redirect, and automatically save a token for future API calls. A video of this in action is below:

The token used is an ASCII string. If it is an `offline` token, it is *portable* . Using the retrieved token, you will be able to run the script on your desktop, then copy and use the code on a remote server without a GUI, provided that code instantiates an OAuth 2.0 client with the same client ID and secret. In addition to Python, the [Google API client libraries](https://developers.google.com/discovery/libraries) for other programming languages also provide helper methods for managing tokens, which can be shared between clients and even used in lower-level HTTP libraries directly [in a client header or as a URL parameter](https://developers.google.com/accounts/docs/OAuth2UserAgent#callinganapi).

Some examples of server-side scripts that use offline tokens:

- A daemon that monitors a directory for new videos to automatically upload to YouTube
- A cron job that that updates playlists daily with new content
- A script that monitors video data via the [YouTube Analytics API](https://developers.google.com/youtube/analytics/) and notifies channel managers when certain events take place, such as aggregate watch time exceeding a limit. Note that in this case, OAuth 2.0 is the only supported authorization method because the Analytics API does not support ClientLogin.

The section on [long-lived access tokens](https://developers.google.com/youtube/v3/guides/moving_to_oauth#offline_access) provides more detail about how to generate the offline tokens that can be used for server side processes.

## Client ID and client secret best practices

Any code that shares the same client ID and secret pair can use the same access tokens. It's best to restrict access to client ID and client secrets to code that runs on machines and devices within your organization.

Do not include your client ID and client secret as part of your native mobile applications code. All developers doing OAuth 2.0 authentication from a mobile device should make use of the "Installed application" client ID, which asks for additional information to verify that the request is coming only from an application released by your team.

![](https://developers.google.com/static/youtube/images/create_client_id_dialog.png)

On Android devices, instead of using a client ID and client secret, your application is identified using a combination of the package name and a signing certificate hash. On iOS devices, the bundle ID and the app store ID are used. The official documentation on retrieving this information can be found on the [Google API Console help page](https://developers.google.com/console/help/#installed_applications).

## Service Accounts do not work with the YouTube API

Service accounts do not work for YouTube Data API calls because service accounts require an associated YouTube channel, and you cannot associate new or existing channels with service accounts. If you use a service account to call the YouTube Data API, the API server [returns an error](https://developers.google.com/youtube/v3/docs/errors#youtube.api.RequestContextError-unauthorized-youtubeSignupRequired) with the error type set to `unauthorized` and the reason set to `youtubeSignupRequired`.

## Offline/long-lived access to the YouTube API

OAuth 2.0 has short-lived tokens and long-lived tokens. For one-off operations, short-lived [access tokens](https://tools.ietf.org/html/rfc6749#section-1.4) are the best option. These tokens expire shortly after they are granted. For long running jobs, you may want to look into acquiring a [refresh token](https://developers.google.com/youtube/v3/guides/authentication#OAuth2_Refreshing_a_Token), which is used to fetch short-lived access tokens.

To ensure that your application receives a long-lived refresh token and not a short-lived access token, use the "Installed Application" flow when creating a client ID, and select `Other` for the "Installed application type" value:

![](https://developers.google.com/static/youtube/images/installed_app_client_id.png)

It's recommended that you use the "Installed application" flow for this use case. If you need long-lived access to the YouTube API in a web application, you can retrieve one by setting the `access_type` parameter to `offline` and the `approval_prompt` parameter to `force` in the [initial authorization request or your client configuration](https://developers.google.com/accounts/docs/OAuth2WebServer#offline). Some client libraries will manage fetching and refreshing access tokens. If you are interested in writing your own custom authorization code, we published a [blog post on the Google Code blog](http://googlecode.blogspot.com/2011/10/upcoming-changes-to-oauth-20-endpoint.html) that you can use as the basis for your code.

## Using OAuth 2.0 with phones, tablets and other devices

When writing Android applications, developers can take advantage of [Google Play services](http://developer.android.com/google/play-services/index.html) to handle the authorization details. Google Play services offers a [standard authorization flow for all Google APIs](http://developer.android.com/google/play-services/auth.html), including APIs for the YouTube platform. This approach will provide a far superior user experience for users of your Android application than a custom authentication using ClientLogin.

![](https://developers.google.com/static/youtube/images/android_play_services_auth.png)

On iOS devices, Google provides two options:


- the [Google+ Platform for iOS](https://developers.google.com/+/mobile/ios/), which integrates sign-in for Google products and also enables social features
- the [gtm-oauth2 toolkit](https://github.com/google/gtm-oauth2), which provides an authorization UIWebView and manages tokens

<br />

For devices that are meant to act as "second screen" devices or devices such as televisions without easy-to-use input mechanisms, [OAuth 2.0 for Devices](https://developers.google.com/accounts/docs/OAuth2ForDevices) is the preferred approach. OAuth 2.0 for Devices works by presenting a unique code for a user when an authorization request is required. At this point, users are asked to browse to <http://google.com/device> on another device, such as a laptop or a phone, and enter in the unique code. The application presents a screen that looks something like this:

![](https://developers.google.com/static/youtube/images/oauth_for_devices_auth.png)

While the user is entering the code on another device, the application periodically polls to see if the code has been entered. Once it has, it retrieves a token for making API calls. To see this in action, check out [the demo](http://stb-web-app.appspot.com/static/index.html), which can be run on any web-enabled device. The API itself is platform-agnostic, making it useful for devices that don't have web rendering capabilities. We've posted [sample code in Python](https://code.google.com/p/gdata-samples/source/browse/trunk/ytplayer/stb-web-app/?r=238) for the demo to be used as a reference.

## Summary

OAuth 2.0 authorization provides flexibility for developers that require YouTube authorization. Developers familiar with ClientLogin may find that setting up their applications to use OAuth 2.0 requires slightly more work to get started, but once ported, OAuth 2.0 applications offer more flexibility, security and usability across multiple platforms for end users.

If you have any more questions about OAuth 2.0 or any of the examples in this article, please feel feel to ask with the [youtube-api tag on StackOverflow](http://stackoverflow.com/questions/tagged/youtube-api).
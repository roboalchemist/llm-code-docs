# Source: https://developers.google.com/youtube/v3/live/registering_an_application.md.txt

# Obtaining authorization credentials

Your application must have authorization credentials to be able to use the YouTube Live Streaming API.

This document describes the different types of authorization credentials that the [Google API Console](https://console.cloud.google.com/) supports. It also explains how to find or create authorization credentials for your project.

## Create your project and select API services

1. Open the [Credentials page](https://console.cloud.google.com/apis/credentials) in the API Console.
2. The page allows you to create two different types of credentials. However, all of the methods for the YouTube Live Streaming API require OAuth 2.0 authorization. Follow the instructions below to generate OAuth 2.0 credentials.
   - **OAuth 2.0:** Whenever your application requests private user
     data, it must send an OAuth 2.0 token along with the request. Your
     application first sends a client ID and, possibly, a client secret to
     obtain a token. You can generate OAuth 2.0 credentials for web
     applications, service accounts, or installed applications.

     For more information, see the [OAuth 2.0 documentation](https://developers.google.com/identity/protocols/OAuth2).
   - **API keys:**

     You have the option of including an API key with a request.

     The key identifies your project and provides API access, quota, and
     reports.


     Note that all of the methods for the YouTube Live Streaming API require
     OAuth 2.0 authorization.


     For that reason, you need to follow the instructions above for
     generating OAuth 2.0 credentials. If you want, you can also send an
     API key, but that's not necessary.

     The API supports several types of restrictions on API keys. If the API key that you
     need doesn't already exist, then create an API key in the Console by
     clicking **[Create credentials](https://console.cloud.google.com/apis/credentials) \> API key** . You can restrict the key before using it
     in production by clicking **Restrict key** and selecting one of the
     **Restrictions**.

To keep your API keys secure, follow the [best practices for
securely using API keys](https://cloud.google.com/docs/authentication/api-keys).
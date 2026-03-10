# Source: https://firebase.google.com/docs/dynamic-links/rest.md.txt

> [!NOTE]
> **Note:** Firebase Dynamic Links is *deprecated* and should not be used in new projects. The service will be shutting down soon. Follow the [migration guide](https://firebase.google.com/support/dynamic-links-faq#how_should_i_migrate_from_the_service) and see the [Dynamic Links Deprecation FAQ](https://firebase.google.com/support/dynamic-links-faq) for more information.

> [!NOTE]
> **Note** : The full [Short Links API reference](https://firebase.google.com/docs/reference/dynamic-links/link-shortener) can be found in the Reference section.

You can create short Dynamic Links with the Firebase Dynamic Links REST API. This API
accepts either a long Dynamic Link or an object containing Dynamic Link parameters, and
returns a URL like the following example:

```
https://example.page.link/WXYZ
```

Short Dynamic Links created with the API and client (Android/Apple) SDK do not show up
in the Firebase console. Such Dynamic Links are intended for user-to-user sharing.
For marketing use cases, continue to create your links directly through the
[Dynamic Links page](https://console.firebase.google.com/project/_/durablelinks/)
of the Firebase console.

### Before you begin

1. Get your API key. You will need an API key to authenticate your requests to the API. To find your API key:
   1. Open the [Settings page](https://console.firebase.google.com/project/_/settings/general/) of the Firebase console. If you are prompted to choose a project, select your Firebase project from the menu.
   2. Take note of the value of the **Web API Key** field.
2. In the Firebase console, open the **Dynamic Links** section.
3. If you have not already accepted the terms of service and set a domain
   for your Dynamic Links, do so when prompted.

   If you already have a Dynamic Links domain, take note of it. You need to
   provide a Dynamic Links domain when you programmatically create Dynamic Links.

   ![](https://firebase.google.com/static/docs/dynamic-links/images/dynamic-links-domain.png)

## Creating a short Dynamic Link

### Create a short link from a long link

You can use the Firebase Dynamic Links API to shorten a long Dynamic Link. To do so,
make an HTTP POST request to the `shortLinks` endpoint, specifying the
long Dynamic Link in the `longDynamicLink` parameter. For example:

```
POST https://firebasedynamiclinks.googleapis.com/v1/shortLinks?key=api_key
Content-Type: application/json

{
   "longDynamicLink": "https://example.page.link/?link=https://www.example.com/&apn=com.example.android&ibi=com.example.ios"
}
```

See [Manually construct a URL](https://firebase.google.com/docs/dynamic-links/create-manually) to learn how
to create long Dynamic Links.

### Create a short link from parameters

You can also create a short Dynamic Link by specifying the Dynamic Link parameters
directly. To do so, make an HTTP POST request to the `shortLinks`
endpoint, specifying the Dynamic Link parameters in the `dynamicLinkInfo` parameter.
For example:

```
POST https://firebasedynamiclinks.googleapis.com/v1/shortLinks?key=api_key
Content-Type: application/json

{
  "dynamicLinkInfo": {
    "domainUriPrefix": "https://example.page.link",
    "link": "https://www.example.com/",
    "androidInfo": {
      "androidPackageName": "com.example.android"
    },
    "iosInfo": {
      "iosBundleId": "com.example.ios"
    }
  }
}
```

For a complete specification of the `dynamicLinkInfo` object, see the
[API reference](https://firebase.google.com/docs/reference/dynamic-links/link-shortener).

### Set the length of a short Dynamic Link

You can also set the `suffix` parameter to specify how the path component of the
short Dynamic Link is generated.

By default, or if you set the parameter to `"UNGUESSABLE"`, the path component
will be a 17-character string, such as in the following example:

```
https://example.page.link/UVWXYZuvwxyz12345
```

Such strings are created by base62-encoding randomly generated 96-bit numbers.
Use this setting to prevent your Dynamic Links URLs from being guessed and crawled,
which can potentially expose sensitive information to unintended recipients.

If you set the parameter to `"SHORT"`, the path component will be a string that
is only as long as needed to be unique, with a minimum length of 4 characters.

```
https://example.page.link/WXYZ
```

Use this method if sensitive information would not be exposed if a short Dynamic Link
URL were guessed.

The following example shows how you can set the `suffix` parameter:

```
POST https://firebasedynamiclinks.googleapis.com/v1/shortLinks?key=api_key
Content-Type: application/json

{
   "longDynamicLink": "https://example.page.link/?link=http://www.example.com/&apn=com.example.android&ibi=com.example.ios",
   "suffix": {
     "option": "UNGUESSABLE"
   }
}

```

### Ensure deep link is valid

At minimum, the deep-link value provided must begin with http:// or https:// schemes.
It must also match any URL patterns whitelist entered in the console.
Else, the creation API will fail with HTTP error code 400.

## Next steps

Now that you've created Dynamic Links, you need to set up your app to receive
Dynamic Links and send users to the right place in your app after a user opens them.

To receive Dynamic Links in your app, see the documentation for
[iOS](https://firebase.google.com/docs/dynamic-links/ios/receive), [Android](https://firebase.google.com/docs/dynamic-links/android/receive),
[C++](https://firebase.google.com/docs/dynamic-links/cpp/receive), and [Unity](https://firebase.google.com/docs/dynamic-links/unity/receive).

Requests are limited to 5 requests/IP address/second, and 200,000 requests/day.
If exceeded, then the response will return HTTP error code 429. To request for
more quota, fill out this [form](https://firebase.google.com/support/troubleshooter/fdl/quotas).
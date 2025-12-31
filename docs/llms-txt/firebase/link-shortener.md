# Source: https://firebase.google.com/docs/reference/dynamic-links/link-shortener.md.txt

You can use this REST API to generate shortDynamic Links. See the[developer guide](https://firebase.google.com/docs/dynamic-links/short-links)to get started.

## HTTP request

```
POST https://firebasedynamiclinks.googleapis.com/v1/shortLinks?key=api_key
Content-Type: application/json

request_body
```

## Request body

The request body looks like one of the following, depending on whether you want to specify theDynamic Linkparameters as a longDynamic Linkor as a JSON object.

To specify theDynamic Linkparameters as a longDynamic Link:  

    {
      "longDynamicLink": string,
      "suffix": {
        "option": "SHORT" or "UNGUESSABLE"
      }
    }

To specify theDynamic Linkparameters as a JSON object:  

    {
      "dynamicLinkInfo": {
        "domainUriPrefix": string,
        "link": string,
        "androidInfo": {
          "androidPackageName": string,
          "androidFallbackLink": string,
          "androidMinPackageVersionCode": string
        },
        "iosInfo": {
          "iosBundleId": string,
          "iosFallbackLink": string,
          "iosCustomScheme": string,
          "iosIpadFallbackLink": string,
          "iosIpadBundleId": string,
          "iosAppStoreId": string
        },
        "navigationInfo": {
          "enableForcedRedirect": boolean,
        },
        "analyticsInfo": {
          "googlePlayAnalytics": {
            "utmSource": string,
            "utmMedium": string,
            "utmCampaign": string,
            "utmTerm": string,
            "utmContent": string
          },
          "itunesConnectAnalytics": {
            "at": string,
            "ct": string,
            "mt": string,
            "pt": string
          }
        },
        "socialMetaTagInfo": {
          "socialTitle": string,
          "socialDescription": string,
          "socialImageLink": string
        }
      },
      "suffix": {
        "option": "SHORT" or "UNGUESSABLE"
      }
    }

### Parameters

All parameters are optional unless otherwise specified.

|                                                                                                                                                                                                                                                                                                                                                                                           General parameters                                                                                                                                                                                                                                                                                                                                                                                            ||
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| domainUriPrefix | Required if you didn't set a value for the`longDynamicLink`parameter. Your Firebase project'sDynamic Linksdomain. You can find this value in theDynamic Linkssection of the[Firebaseconsole](https://console.firebase.google.com/).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| link            | Required if you didn't set a value for the`longDynamicLink`parameter. The link your app will open. Specify a URL that your app can handle, typically the app's content or payload, which initiates app-specific logic (such as crediting the user with a coupon or displaying a welcome screen). This link must be a well-formatted URL, be properly URL-encoded, use either HTTP or HTTPS, and cannot be another Dynamic Link. | When users open aDynamic Linkon a desktop web browser, they will load this URL (unless the`ofl`parameter is specified). If you don't have a web equivalent to the linked content, the URL doesn't need to point to a valid web resource. In this situation, you should set up a redirect from this URL to, for example, your home page.              |
| suffix          | Specifies how to create the path component of a shortDynamic Link. By default,Firebase Dynamic Linksgenerates 17-character string suffixes. Set the parameter to`{ "option": "SHORT" }`to generate path strings that are only as long as needed to be unique, with a minimum length of 4 characters. Use this method if sensitive information would not be exposed if a shortDynamic LinkURL were guessed. Omit this parameter or set the parameter to`{ "option": "UNGUESSABLE" }`to shorten the path to an unguessable string. Such strings are created by base62-encoding randomly generated 96-bit numbers, and consist of 17 alphanumeric characters. Use unguessable strings to prevent yourDynamic Linksfrom being crawled, which can potentially expose sensitive information. |

|                                                                                                                                    Android parameters                                                                                                                                     ||
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| androidPackageName           | The package name of the Android app to use to open the link. The app must be connected to your project from the Overview page of theFirebaseconsole. Required for theDynamic Linkto open an Android app.                                                    |
| androidFallbackLink          | The link to open when the app isn't installed. Specify this to do something other than install your app from the Play Store when the app isn't installed, such as open the mobile web version of the content, or display a promotional page for your app.   |
| androidMinPackageVersionCode | The[`versionCode`](http://developer.android.com/tools/publishing/versioning.html#appversioning)of the minimum version of your app that can open the link. If the installed app is an older version, the user is taken to the Play Store to upgrade the app. |

|                                                                                                                                 iOS parameters                                                                                                                                  ||
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| iosBundleId         | The bundle ID of the iOS app to use to open the link. The app must be connected to your project from the Overview page of theFirebaseconsole. Required for theDynamic Linkto open an iOS app.                                                              |
| iosFallbackLink     | The link to open when the app isn't installed. Specify this to do something other than install your app from the App Store when the app isn't installed, such as open the mobile web version of the content, or display a promotional page for your app.   |
| iosCustomScheme     | Your app's custom URL scheme, if defined to be something other than your app's bundle ID                                                                                                                                                                   |
| iosIpadFallbackLink | The link to open on iPads when the app isn't installed. Specify this to do something other than install your app from the App Store when the app isn't installed, such as open the web version of the content, or display a promotional page for your app. |
| iosIpadBundleId     | The bundle ID of the iOS app to use on iPads to open the link. The app must be connected to your project from the Overview page of theFirebaseconsole.                                                                                                     |
| iosAppStoreId       | Your app's App Store ID, used to send users to the App Store when the app isn't installed                                                                                                                                                                  |

|                                                                                                                                                                                                                                                   Navigation parameters                                                                                                                                                                                                                                                   ||
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| enableForcedRedirect | If set to '1', skip the app preview page when theDynamic Linkis opened, and instead redirect to the app or store. The app preview page (enabled by default) can more reliably send users to the most appropriate destination when they openDynamic Linksin apps; however, if you expect aDynamic Linkto be opened only in apps that can openDynamic Linksreliably without this page, you can disable it with this parameter. This parameter will affect the behavior of theDynamic Linkonly on iOS. |

|                                Social Meta Tag parameters                                 ||
|-------------------|------------------------------------------------------------------------|
| socialTitle       | The title to use when theDynamic Linkis shared in a social post.       |
| socialDescription | The description to use when theDynamic Linkis shared in a social post. |
| socialImageLink   | The URL to an image related to this link.                              |

|                                   Analytics parameters                                   ||
|----------------------------------------------------|--------------------------------------|
| utmSource utmMedium utmCampaign utmTerm utmContent | Google Play analytics parameters.    |
| at ct mt pt                                        | iTunes Connect analytics parameters. |

## Response body

The response to a request is a JSON object like the following:  

    {
      "shortLink": string,
      "previewLink": string
    }

|                          Response fields                          ||
|-------------|------------------------------------------------------|
| shortLink   | The generated shortDynamic Link.                     |
| previewLink | A link to a flowchart of theDynamic Link's behavior. |
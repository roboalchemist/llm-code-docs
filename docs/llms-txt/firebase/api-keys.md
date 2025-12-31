# Source: https://firebase.google.com/docs/projects/api-keys.md.txt

An API key is a unique string that's used to route requests to your Firebase project when interacting with Firebase and Google services. This page describes basic information about API keys as well as best practices for using and managing API keys with Firebase apps.
| **Here are the most important things to learn about API keys for Firebase:**
|
| - [Firebase-related APIs](https://firebase.google.com/docs/projects/api-keys#faq-required-apis-for-restricted-firebase-api-key)use API keys only to*identify* the Firebase project or app,*not for authorization* to call the API (like some other APIs allow).*Authorization* for Firebase-related APIs is handled separately from the API key, either throughGoogle CloudIAM permissions,Firebase Security Rules, orFirebase App Check. This is why**it's OK to include Firebase API keys in your code when you use them only with[Firebase-related APIs](https://firebase.google.com/docs/projects/api-keys#faq-required-apis-for-restricted-firebase-api-key)**.
| - We recommend that you[review and apply appropriate restrictions and limits](https://firebase.google.com/docs/projects/api-keys#apply-restrictions)to all your API keys (even your Firebase API keys). Specifically, restrict the key to only the APIs that you actually use in your app and limit the quota, as applicable. Note that**[all Firebase-provisioned API keys have "API restrictions" applied by default](https://firebase.google.com/docs/projects/api-keys#faq-api-keys-restricted-by-default)**.
| - **Use your Firebase-provisioned API keys*only* for[Firebase-related APIs](https://firebase.google.com/docs/projects/api-keys#faq-required-apis-for-restricted-firebase-api-key).** For all other APIs (for example, the Places API for Maps or the Google AI Gemini API), use a[separate API key](https://firebase.google.com/docs/projects/api-keys#use-separate-keys-for-specific-apis).
| - We strongly recommend that you**secure yourRealtime Database,Cloud Firestore, andCloud Storage*data* by usingFirebase Security Rules**. Don't rely only on API key restrictions.

## General information about API keys and Firebase

### API keys for Firebase are different from typical API keys

**Unlike how API keys are typically used, API keys for Firebase services are*not* used to control*access*to backend resources** ; that can only be done withFirebase Security Rules(to control which*end users* can access resources) andFirebase App Check(to control which*apps*can access resources).

Usually, you need to fastidiously guard API keys (for example, by using a vault service or setting the keys as environment variables); however, API keys for Firebase services are OK to include in code or checked-in config files.

Although API keys for Firebase services are safe to include in code, you should[review and apply appropriate restrictions and limits to them](https://firebase.google.com/docs/projects/api-keys#apply-restrictions).
| **Secure yourRealtime Database,Cloud Firestore, andCloud Storage***data*** by using[Firebase Security Rules](https://firebase.google.com/docs/rules)**. Don't rely only on restricting and/or obscuring your API keys.

### Creating API keys

A Firebase project can have many API keys, but each API key can only be associated with a single Firebase project.

![API keys automatically created by Firebase for your Firebase Apps](https://firebase.google.com/static/docs/projects/images/api-keys-from-firebase-cloud-console.png)

Firebase automatically creates API keys for your project when you do any of the following:

- Create a Firebase project \>`Browser key`auto-created
- Create a Firebase Apple App \>`iOS key`auto-created
- Create a Firebase Android App \>`Android key`auto-created

| **Important:** The API keys auto-created by Firebase, by default, are automatically restricted to a list of APIs that require the client to provide an API key along with the call. See the FAQ[Are API keys for Firebase services restricted by default?](https://firebase.google.com/docs/projects/api-keys#faq-api-keys-restricted-by-default).

You can also create your own API keys in the[Google Cloudconsole](https://console.cloud.google.com/apis/credentials), for example[for development or debugging](https://firebase.google.com/docs/projects/api-keys#test-vs-prod-keys). Learn more about when this might be recommended later on this page.

### Finding your API keys

You can view and manage*all* your project's API keys in the[*APIs \& Services \> Credentials*](https://console.cloud.google.com/apis/credentials)panel in theGoogle Cloudconsole.

You can also find which[API key is automatically matched to a Firebase App](https://firebase.google.com/docs/projects/api-keys#faq-auto-matching-app-to-key)in the following places. By default, all of your project's Firebase Apps*for the same platform*(Apple vs Android vs Web) will use the same API key.

- **Firebase Apple Apps** --- Find the auto-matched API key in the Firebase config file,GoogleService-Info.plist, in the`API_KEY`field.

- **Firebase Android Apps** --- Find the auto-matched API key in the Firebase config file,google-services.json, in the`current_key`field.

- **Firebase Web Apps** --- Find the auto-matched API key in the Firebase config object, in the`apiKey`field.

### Using an API key

API keys for Firebase are used to identify your Firebase project when interacting with Firebase or Google services. Specifically, they're used to associate API requests with your project for quota and billing. They're also useful for accessing public data.

**For the vast majority of developers and use cases, you don't interact with these API keys directly.** Instead, when your app makes a call to a Firebase API that requires an API key provided by the mobile or web client, your app will*automatically* look for an API key in your app's[Firebase configuration](https://firebase.google.com/docs/projects/learn-more#config-files-objects). This config was added to your app's codebase when you connected your app to Firebase.

Note that you can provide your app's API key within your app using a different mechanism, like Firebase options or using environment variables.

Also, for a few of the REST APIs for Firebase services, you might need to explicitly pass the value of the API key into the call as a query parameter. This example shows how you might make a request using theFirebase AuthenticationAPI:  

```
https://identitytoolkit.googleapis.com/v1/accounts:signInWithCustomToken?key=API_KEY
```

## Review and apply appropriate restrictions to API keys*(recommended)*

Although it's not necessary to treat an API key for Firebase services as a secret, you should review and apply restrictions and limits as described in this section.
| For API keys in use by production apps, be cautious about changing its restrictions or limits. You should test the new settings in a testing app and with a[test API key](https://firebase.google.com/docs/projects/api-keys#test-vs-prod-keys)before changing restrictions or limits for your production API key.
| **Note:** If the API key that you use for Firebase services has "API restrictions" and you're getting a`API_KEY_SERVICE_BLOCKED`or Forbidden 403 error, make sure that the API key has all the[required APIs included in the key's "API restrictions" allowlist](https://firebase.google.com/docs/projects/api-keys#faq-required-apis-for-restricted-firebase-api-key).

### Review the APIs automatically added to the allowlist for your Firebase API keys

**When Firebase creates an API key in your project, we automatically add["API restrictions"](https://cloud.google.com/docs/authentication/api-keys#adding_api_restrictions)to that key.**The APIs added to this allowlist are Firebase-related APIs that require the client to provide an API key along with the call. Note that most APIs required for use of Firebase services don't actually need to be on the allowlist for your API keys.

Since Firebase adds the necessary APIs for*all* Firebase services, the allowlist for an API key may include APIs for products that you do not use. You can remove APIs from the allowlist, but you must**be very careful to not remove the APIs required for Firebase and the Firebase services that you use** (see the[list of the Firebase-related APIs](https://firebase.google.com/docs/projects/api-keys#faq-required-apis-for-restricted-firebase-api-key)that need to be on the allowlist for each service / product). Otherwise, you will get errors when making calls to Firebase services.
| **Note:** During May 2024, Firebase automatically applied API restrictions to all existing and*unrestricted* Firebase-provisioned API keys. Learn more in the FAQ[Are API keys for Firebase services restricted by default?](https://firebase.google.com/docs/projects/api-keys#faq-api-keys-restricted-by-default).

### Tighten quota if you use password-basedAuthentication

| No matter which authentication option you use,**secure yourRealtime Database,Cloud Firestore, andCloud Storage***data*** by using[Firebase Security Rules](https://firebase.google.com/docs/rules)**.

If you use password-basedFirebase Authenticationand someone gets hold of your API key, they will**not** be able to access any of your Firebase project's database orCloud Storagedata*as long as this data is protected by[Firebase Security Rules](https://firebase.google.com/docs/rules)*. They could, however, use your API key to access Firebase's authentication endpoints and make authentication requests against your project.

To mitigate against the possibility that someone might misuse an API key to attempt a brute force attack, you can tighten the default quota of the`identitytoolkit.googleapis.com`endpoints to reflect the normal traffic expectations of your app. Be aware that if you tighten this quota and your app suddenly gains users, you might get sign-in errors until you increase the quota. You can change your project's API quotas in the[Google Cloudconsole](https://console.cloud.google.com/apis/api/identitytoolkit.googleapis.com/quotas?project=_).

### Use separate, restricted API keys for any non-Firebase service

Although API keys used for Firebase services do not generally need to be treated as secret, you should take some extra precautions with API keys that you use with otherGoogle CloudAPIs.

If you use aGoogle CloudAPI (on any platform) that's not for a Firebase service / product, we strongly recommend creating separate, restricted API keys for use with those APIs. This is particularly important if the API is for a billableGoogle Cloudservice.

For example, if you useFirebase MLand the Cloud Vision APIs on iOS, you should[create separate API keys](https://firebase.google.com/docs/ml/ios/secure-api-key)that you use only for accessing the Cloud Vision APIs.

By using separate, restricted API keys for non-Firebase APIs, you can rotate or replace the keys when necessary and[add additional restrictions to the API keys](https://cloud.google.com/docs/authentication/api-keys#api_key_restrictions)without disrupting your use of Firebase services.

<br />

#### **View instructions for creating API-specific keys**

<br />

**These instructions describe how to create a separate, restricted API key for a*fake* API called`Super Service API`.**

#### Step 1: Configure your existing API keys to disallow access to`Super Service API`

1. Open the[Credentials](https://console.cloud.google.com/apis/credentials?project=_)page of theGoogle Cloudconsole. When prompted, select your project.

2. For each existing API key in the list, open the editing view.

3. In the*API restrictions* section, select**Restrict key** , then add to the list all of the APIs to which you want the API key to have access. Make sure to***not*** include the API for which you're creating a separate API key (in this example,`Super Service API`).

   When you configure an API key's*API restrictions* , you are explicitly declaring the APIs to which the key has access.**By default, when the*API restrictions* section has*Don't restrict key*selected, an API key can be used to access any API that is enabled for the project.**

Now, your existing API keys will not grant access to`Super Service API`, but each key will continue to work for any APIs that you added to its*API restrictions*list.
| **Important:** If you enable any additional APIs in the future, you must add them to the*API restrictions*list for the applicable API key.

#### Step 2: Create and use a new API key for access to`Super Service API`

1. Return to the[Credentials](https://console.cloud.google.com/apis/credentials?project=_)page. Be sure your Firebase project is still selected.

2. Click**Create credentials \> API key** . Take note of the new API key, then click**Restrict key**.

3. In the*API restrictions* section, select**Restrict key** , then add to the list***only*** the`Super Service API`.

   This new API key grants access only to the`Super Service API`.
4. Configure your app and services to use the new API key.

<br />

<br />

## Use environment-specific API keys*(recommended)*

If you set up different Firebase projects for different environments, such as staging and production, it's important that each app instance interacts with its corresponding Firebase project. For example, your staging app instance should never talk to your production Firebase project. This also means that your staging app needs to use API keys associated with your staging Firebase project.

To reduce problems promoting code changes from development to staging to production, instead of including API keys in the code itself, either set them as environment variables or include them in a configuration file.

Note that if you're using theFirebase Local Emulator Suitefor development along withFirebase ML, you must create and use a debug-only API key. Instructions for creating that kind of key are found in the[Firebase MLdocs](https://firebase.google.com/docs/ml/android/secure-api-key#3_create_and_use_a_debug-only_api_key).

## FAQs and troubleshooting

### FAQs

<br />

#### Are API keys for Firebase services restricted by default?

<br />

Yes, by default, all API keys that Firebase auto-provisions for use with Firebase-related APIs have["API Restrictions"](https://cloud.google.com/docs/authentication/api-keys#adding_api_restrictions)applied automatically. See the[list of the Firebase-related APIs](https://firebase.google.com/docs/projects/api-keys#faq-required-apis-for-restricted-firebase-api-key)that are on this allowlist.

The APIs added to this allowlist are those APIs called by Firebase services from client-code and require API keys for identification of your Firebase project or app. Note that*most*APIs required for use of Firebase services don't actually need to be on the allowlist for your API keys.

Since Firebase adds the necessary APIs for*all* Firebase services, the allowlist for an API key may include APIs for products that you do not use. You can remove APIs from the allowlist, but you must**be very careful to not remove the APIs required for Firebase and the Firebase services that you use** (see the[list of the Firebase-related APIs](https://firebase.google.com/docs/projects/api-keys#faq-required-apis-for-restricted-firebase-api-key)that need to be on the allowlist for each service / product). Otherwise, you will get errors when making calls to Firebase services.
| **Important:** None of the Firebase-related APIs use an API key as*authorization*for calling the API. The API key passed with the API call is only used for identification of the Firebase project or app.

You can view all your API keys and their "API restrictions" in the[*APIs \& Services* \>*Credentials*](https://console.cloud.google.com/apis/credentials)panel in theGoogle Cloudconsole.

**Note the following about how Firebase applies these "API restrictions":**

- Starting in May 2024, all***new*** API keys auto-provisioned by Firebase are automatically restricted to the[list of the Firebase-related APIs](https://firebase.google.com/docs/projects/api-keys#faq-required-apis-for-restricted-firebase-api-key).

- During May 2024, all existing and*unrestricted* API keys that Firebase had previously auto-provisioned are restricted to the[list of the Firebase-related APIs](https://firebase.google.com/docs/projects/api-keys#faq-required-apis-for-restricted-firebase-api-key)*plus*any of the project's currently enabled APIs.

- Any existing and*already restricted*API keys that Firebase had previously auto-provisioned were not changed.

- Any existing API keys that were*not*auto-provisioned by Firebase were not changed.

| **Important:** If you use aGoogle CloudAPI (on any platform) that's not for a Firebase service / product, we strongly recommend[creating separate, restricted API keys](https://firebase.google.com/docs/projects/api-keys#use-separate-keys-for-specific-apis)for use with those APIs.

<br />

<br />

<br />

#### How can I determine which API key is associated with my Firebase App?

<br />

You can use any of the following options to determine which API key is associated with your Firebase App:  

### Firebaseconsole

1. Go tosettings[*Project settings*](https://console.firebase.google.com/project/_/settings/general/), and then scroll down to the*Your apps*card.

2. Select the app of interest.

3. Obtain the Firebase config file/object for the app of interest, and then find its API key:

   - **Apple** : Download the`GoogleService-Info.plist`, and then find the`API_KEY`field

   - **Android** : Download the`google-services.json`, find the config for the app of interest (look for its package name), and then find the`current_key`field

   - **Web** : Select the*Config* option, and then find the`apiKey`field

### FirebaseCLI

1. Obtain the Firebase config file/object for the app of interest by running the following command:

   ```
   firebase apps:sdkconfig PLATFORM FIREBASE_APP_ID
   ```
   - <var translate="no">PLATFORM</var>(one of):`IOS`\|`ANDROID`\|`WEB`
   - <var translate="no">FIREBASE_APP_ID</var>: the Firebase-assigned unique identifier for your Firebase App ([find your App ID](https://firebase.google.com/support/faq#find-app-id))
2. In the app's printed Firebase configuration, find its API key:

   - **Apple** : Find the`API_KEY`field

   - **Android** : Find the config for the app of interest (look for its package name), and then find the`current_key`field

   - **Web** : Find the`apiKey`field

### REST API

1. Obtain the`apiKeyId`(the UID) of the API key by calling the applicable endpoint for the app of interest, and then passing the`apiKeyId`value to the next step.

   - **Apple** : Call[`projects.iosApps.get`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps/get)
   - **Android** : Call[`projects.androidApps.get`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps/get)
   - **Web** : Call[`projects.webApps.get`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps/get)
2. Obtain the API key string by calling[`projects.locations.keys.getKeyString`](https://cloud.google.com/api-keys/docs/reference/rest/v2/projects.locations.keys/getKeyString).

   This`keyString`is the same value that can be found in the App's configuration artifact ([Apple](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps/getConfig)\|[Android](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps/getConfig)\|[Web](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps/getConfig)).

<br />

<br />

<br />

#### Can I have two API keys listed for the same Firebase App in my Firebase config file/object?

<br />

- **Firebase Apple Apps**--- Each app has its own config file and can have only one API key listed.

- **Firebase Android Apps** --- All Android apps in the Firebase project are listed in the same config file, and*each*app can only have one API key listed. Each app in this config file can have a different key listed, though.

- **Firebase Web Apps**--- Each app has its own config object and can have only one API key listed.

You*can*use multiple API keys with one app, though. You must provide a mechanism for your app to access these other API keys, like via an environment variable. The mechanism to access the other API keys just can't depend on those API keys being listed in your Firebase config file/object.

<br />

<br />

<br />

#### How does Firebase know which API key to match to an app (like in the Firebase config file/object)?

<br />

When you first[obtain your app's Firebase config file/object](https://support.google.com/firebase/answer/7015592), Firebase checks if there are any existing API keys in your project that have["Application Restrictions"](https://cloud.google.com/docs/authentication/api-keys#adding_application_restrictions)that match the app (for example, a matching bundle ID for the Apple app).

If Firebase doesn't find any restricted keys that match, then it will list in the config file/object the`iOS key`for Apple apps, the`Android key`for Android apps, and the`Browser key`for web apps (assuming that these keys exist and have no "Application Restrictions" that keep them from matching to that app).

<br />

<br />

<br />

#### Can I manually delete the API key and field from my Firebase config file/object?

<br />

Yes, you can manually delete your API key from your config file/object. However,**you must provide some other mechanism for your app to access an API key**(like via an environment variable). Otherwise, any calls to Firebase services will fail.

<br />

<br />

<br />

#### Can I manually edit my Firebase config file/object with different API keys?

<br />

Yes, you can manually edit a config file/object to associate a different API key with an app.
| Manually editing the API key in your Firebase config file/object is possible, but**not usually recommended** . It increases the chances of issues with accessing Firebase services. However, if you choose to edit your config file/object, do the following:
|
| - Make sure that the API key is scoped to the Project ID listed in the config file/object.
| - Make sure that there aren't any["API Key Restrictions"](https://cloud.google.com/docs/authentication/api-keys#api_key_restrictions)that would inhibit the API key from being used with that app.
| - Make sure that the API key has the appropriate "API restrictions" applied to it. See the[list of the Firebase-related APIs](https://firebase.google.com/docs/projects/api-keys#faq-required-apis-for-restricted-firebase-api-key)that need to be on the allowlist for each Firebase service / product.

Note that if you[re-obtain your app's config file/object](https://support.google.com/firebase/answer/7015592)from the console, it will always list the API keys that[Firebase automatically matches to that app](https://firebase.google.com/docs/projects/api-keys#faq-auto-matching-app-to-key). So, you'll need to repeat your manual edits, as needed.

<br />

<br />

<br />

#### Can I move an API key from one Firebase project to another?

<br />

No, an API key only identifies a specific project and cannot be moved to another project.

<br />

<br />

<br />

#### What happens if I delete an API key listed in theGoogle Cloudconsole?

<br />

If you delete an API key that's in use by an app, then API calls from that app will fail. You may get reports, emails, or errors that you're attempting to use an API key that is invalid.

Deleting an API key is permanent and cannot be undone.

<br />

<br />

<br />

#### Which APIs are required in the "API restrictions" allowlist for a Firebase API key?

<br />

For a Firebase API key, the only APIs that need to be on the key's "API restrictions" allowlist are the APIs that require the client to provide an API key along with the call. Note that very few Firebase-related APIs have this requirement. Most Firebase-related APIs enabled in your project don't need to be on the key's "API restrictions" allowlist.
| **Important:** None of the Firebase-related APIs use an API key as*authorization* for calling the API. The API key passed with the API call is only used for*identification*of the Firebase project or app.

Use the following table to determine which Firebase-related APIs need to be included in the "API restrictions" allowlist for a Firebase API key. Remember, Firebase API keys should only be used for Firebase services. Learn more about creating[separate, restricted API keys for specific types of APIs](https://firebase.google.com/docs/projects/api-keys#use-separate-keys-for-specific-apis).

You can view and manage your project's API keys in the[*APIs \& Services* \>*Credentials*](https://console.cloud.google.com/apis/credentials)panel in theGoogle Cloudconsole.
| **Note:** If you're getting a`API_KEY_SERVICE_BLOCKED`or Forbidden 403 error when trying to call a Firebase-related API and the API key that you're using has all the required APIs listed in this table, reach out to[Firebase Support](https://firebase.google.com/support/troubleshooter/contact).

|         **API name (service name)**         |        **API display name**         |                           **Associated Firebase service / product**                           |
|---------------------------------------------|-------------------------------------|-----------------------------------------------------------------------------------------------|
| firebase.googleapis.com                     | Firebase Management API             | all products                                                                                  |
| logging.googleapis.com                      | Cloud Logging API                   | all products                                                                                  |
| firebaseinstallations.googleapis.com        | Firebase Installations API          | Cloud Messaging,Crashlytics,In-App Messaging,Performance Monitoring,Remote Config,Firebase ML |
| firebaseappcheck.googleapis.com             | Firebase App Check API              | App Check                                                                                     |
| firebaseappdistribution.googleapis.com      | Firebase App Distribution API       | App Distribution                                                                              |
| firebaseapptesters.googleapis.com           | Firebase App Testers API            | App Distribution                                                                              |
| identitytoolkit.googleapis.com              | Identity Toolkit API                | Authentication                                                                                |
| securetoken.googleapis.com                  | Token Service API                   | Authentication                                                                                |
| firebaserules.googleapis.com**\***          | Firebase Rules API                  | Cloud Firestore,Cloud Storage,Realtime Database                                               |
| datastore.googleapis.com                    | Cloud Datastore API                 | Cloud Firestore                                                                               |
| firestore.googleapis.com                    | Google Cloud Firestore API          | Cloud Firestore                                                                               |
| fcmregistrations.googleapis.com             | FCM Registration API                | Cloud Messaging                                                                               |
| firebasestorage.googleapis.com              | Cloud Storage for Firebase API      | Cloud Storage                                                                                 |
| firebasedynamiclinks.googleapis.com         | Firebase Dynamic Links API          | Dynamic Links                                                                                 |
| firebasehosting.googleapis.com**\***        | Firebase Hosting API                | Hosting                                                                                       |
| firebaseinappmessaging.googleapis.com       | Firebase In-App Messaging API       | In-App Messaging                                                                              |
| firebaseml.googleapis.com                   | Firebase ML API                     | Firebase ML                                                                                   |
| mlkit.googleapis.com**\*\***                | ML Kit API                          | Firebase ML                                                                                   |
| mobilecrashreporting.googleapis.com         | Mobile Crash Reporting API          | Performance Monitoring                                                                        |
| play.googleapis.com                         | Google Play Android Developer API   | Performance Monitoring                                                                        |
| firebaseremoteconfig.googleapis.com         | Firebase Remote Config API          | Performance Monitoring,Remote Config                                                          |
| firebaseremoteconfigrealtime.googleapis.com | Firebase Remote Config Realtime API | Performance Monitoring,Remote Config                                                          |
| cloudconfig.googleapis.com**\*\***          | N/A                                 | Remote Config                                                                                 |
| firebasedatabase.googleapis.com**\***       | Firebase Realtime Database API      | Realtime Database                                                                             |
| firebasevertexai.googleapis.com             | Firebase AI Logic API               | Firebase AI Logicclient SDKs                                                                  |

^*\* Required only if you're using the Firebase API key with third-party tools or direct REST access to the Firebase service / product.*^

^*\*\* Required for earlier versions of the product's SDK. If you're using the latest version of the SDK, the API doesn't need to be on the key's allowlist.*^

<br />

<br />

### Troubleshooting

<br />

#### How do I fix a`API_KEY_SERVICE_BLOCKED`or Forbidden 403 error that says requests to this API are blocked?

<br />

Follow the guidance in this FAQ if you're getting a`API_KEY_SERVICE_BLOCKED`error or an error that looks like the following:  

    Forbidden: 403 POST https://example-service.googleapis.com/method: Requests to this API example-service.googleapis.com method google.example-service.rest.method are blocked.

The API key used by your app to call the API probably has["API Restrictions"](https://cloud.google.com/docs/authentication/api-keys#adding_api_restrictions)applied to it, and the key's allowlist doesn't include that API.

- If you're getting this error when trying to use a Firebase-related service / product, then make sure that the API key that you're using has all the[required APIs included in the key's "API restrictions" allowlist](https://firebase.google.com/docs/projects/api-keys#faq-required-apis-for-restricted-firebase-api-key).

- If you're getting this error when trying to use a*non-Firebase service* , then we strongly recommend creating a new API key specifically for that service and API. Firebase API keys should only be used for Firebase services / products. Learn more about creating[separate, restricted API keys for specific types of APIs](https://firebase.google.com/docs/projects/api-keys#use-separate-keys-for-specific-apis).

<br />

<br />

<br />

#### How do I fix this error? "Failed to fetch this Firebase app's measurement ID from the server."

<br />

The API key used by your web app probably has["API Restrictions"](https://cloud.google.com/docs/authentication/api-keys#adding_api_restrictions)applied to it. If this is the case, make sure that the Firebase Management API is in the list of allowed APIs.

<br />

<br />

<br />

#### I got an email or error that my API key is invalid. What happened and how do I fix this?

<br />

Here are a few of the most common causes for invalid API keys:

- The API key has["API Key Restrictions"](https://cloud.google.com/docs/authentication/api-keys#api_key_restrictions)applied to it that make it unmatchable to the app attempting to use the key ("Application Restrictions") or unusable for the API being called ("API Restrictions").

- The API key was deleted from the project in theGoogle Cloudconsole.

- The API key was not created for the Project ID listed in the app's Firebase config file/object.

One way to fix this issue is to[obtain the updated version of your app's Firebase config file/object](https://support.google.com/firebase/answer/7015592), then*replace* your old config file/object with the new updated file/object. Before sending a config file for download or displaying a config object in the console, Firebase checks that the API key(s) listed[match to the app(s)](https://firebase.google.com/docs/projects/api-keys#faq-auto-matching-app-to-key).

<br />

<br />
# Source: https://firebase.google.com/docs/android/play-data-disclosure.md.txt

<br />

In May 2021, Google Play[announced the new Data safety section](https://android-developers.googleblog.com/2021/05/new-safety-section-in-google-play-will.html), which is a developer-provided disclosure for an app's data collection, sharing, and security practices.

This page can help you complete the requirements for this data disclosure in regards to your usage of Firebase Android SDKs. On this page, you can find information on whether and how our SDKs handle end-user data, including examples of applicable configurations or invocations you can control as the app developer.

We aim to be as transparent as possible in supporting you; however, as the app developer, you are solely responsible for deciding how to respond to Google Play's Data safety section form regarding your app's end-user data collection, sharing, and security practices.

### How to use the information on this page

This page lists the end-user data collected by only the***latest version***of each Firebase Android SDK.

Each SDK has its own section later on this page where we provide information about data***collected automatically*** versus data***collected depending on your usage***. Automatic collection means that the SDK collects specific data without you invoking any specific method or class in your app. However, in many cases, the data collected by the SDK depends on your app's specific usage of the product, meaning your app's configuration and how you invoke the SDK.

To complete your data disclosure, you can use Android's[guide about data types](https://developer.android.com/guide/topics/data/collect-share)to help you determine which***data type***best describes the collected data. In your data disclosure, make sure to also account for how your specific app shares and uses the collected data.
| **Important** : To help you ensure that your app's disclosures are accurate, we recommend the following:
|
| - Always use the latest SDK versions in your app. This page lists the data collected by only the*latest*version of each SDK.
| - Review this page whenever you update your app's SDK versions. Check that your data disclosures are accurate and up-to-date.

### Overview of data encryption, data sharing, and data deletion for Firebase Android SDKs

|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Data encryption** | For the collected end-user data listed on this page, Firebase encrypts the data in transit using HTTPS.                                                                                                                                                                                                                                                                |
| **Data sharing**    | For the collected end-user data listed on this page, Firebase does not transfer this data to third-parties except: - To[third-party subprocessors](https://firebase.google.com/terms/subprocessors)that assist us in providing Firebase services. - In accordance with your instructions (for example, if you choose to link Firebase to other non-Firebase services). |
| **Data deletion**   | Firebase enables developers to delete end-user data in a manner consistent with the functionality of the Firebase services.                                                                                                                                                                                                                                            |

<br />

*** ** * ** ***

## **Firebase user agent**

The***Firebase user agent***is not a Firebase Android SDK, but rather a bundle of information that's collected by several Firebase Android SDKs and includes the following:

- Device metadata: OS version, name, model, brand, and form factor

- App that was used to install your app (for example, the Play Store) (see[documentation](https://developer.android.com/reference/android/content/pm/PackageManager#getInstallerPackageName(java.lang.String)))

- Which Firebase SDKs are used in your app, including their versions

The Firebase user agent is used internally by Google to determine platform and version adoption in order to provide, maintain, and improve Firebase services. It is never linked to a user or device identifier.

If a Firebase Android SDK collects the Firebase user agent, it will be listed in the SDK's section below.

<br />

*** ** * ** ***

## **A/B Testing**

`com.google.firebase:firebase-abt`

### **Data collected automatically**

TheFirebase A/B TestingSDK does not*automatically*collect any end-user data.

#### Other considerations

TheFirebase A/B TestingSDK sets and usesGoogle Analyticsuser properties in order to specify membership in experiment groups forFirebase Remote ConfigandFirebase In-App Messaging.

Since theA/B TestingSDK is only used directly by[Firebase Remote Config](https://firebase.google.com/docs/android/play-data-disclosure#remote-config)and[Firebase In-App Messaging](https://firebase.google.com/docs/android/play-data-disclosure#in-app-messaging), refer to those specific sections on this page to learn more about any data collection and the purpose of collection.

### **Data collected depending on your usage**

TheFirebase A/B TestingSDK doesn't have optional features that the developer can configure or invoke to collect other end-user data.

<br />

*** ** * ** ***

## **Firebase AI Logic**

`com.google.firebase:firebase-ai`

*Firebase AI Logicwas formerly called "Vertex AI in Firebase" with the package`com.google.firebase:firebase-vertexai`.*

### **Data collected automatically**

TheFirebase AI LogicSDK collects the following data*automatically*.

|                Data                |                                         By default, theFirebase AI LogicSDK...                                         |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Model name                         | Collects the model name at invocation.                                                                                 |
| Version of the SDK used by the app | Collects the version of theFirebase AI LogicSDK used by the app. This value is included in the header of each request. |
| Language version                   | Collects the version of the Kotlin runtime used by the app. This value is included in the header of each request.      |
| Firebase App ID                    | If data collection is enabled, collects the Firebase App ID. This value is included in the header of each request.     |
| App Version                        | If data collection is enabled, collects the app version. This value is included in the header of each request.         |

### **Data collected depending on your usage**

Depending on how you configure or invoke theFirebase AI LogicSDK and the product's features, your app may collect end-user data that needs to be included in your data disclosure. Make sure that you account for any developer-defined end-user data that's collected by your specific usage.

#### Other considerations

If you useFirebase AI LogicwithFirebase Authentication, and if an end-user is signed-in, then every request fromFirebase AI Logicautomatically includes the applicable User ID fromFirebase Authentication.

If you enable[AI monitoring in theFirebaseconsole](https://firebase.google.com/docs/ai-logic/monitoring#ai-monitoring-in-console)for theVertex AIGemini API, then the prompts and generated output from each sampled request are collected along with performance and usage metrics.

Make sure to review[Data governance and Responsible AI](https://firebase.google.com/docs/ai-logic/data-governance)in theFirebase AI Logicdocumentation to ensure that you're accounting for your use of the underlying APIs (theVertex AIGemini APIor theGemini Developer API).

### **Additional information**

#### Purpose for data collection

Firebase AI Logicgenerally uses the collected data listed in the sub-sections above to invoke the backend service in response to requests from your app. Also, review the sub-sections above for information about how*specific*data may be used. In your data disclosure, make sure to also account for how you specifically use the collected data, in addition to how you use any developer-defined end-user data collected by the SDK.

<br />

*** ** * ** ***

## **App Check**

`com.google.firebase:firebase-appcheck`  
`com.google.firebase:firebase-appcheck-ktx`  
`com.google.firebase:firebase-appcheck-debug`  
`com.google.firebase:firebase-appcheck-playintegrity`

### **Data collected automatically**

TheFirebase App CheckSDKs collect the following data*automatically*.

|        Data         |                                                          By default, theFirebase App CheckSDKs...                                                          |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Firebase user agent | For information, refer to the[Firebase user agent section](https://firebase.google.com/docs/android/play-data-disclosure#firebase-user-agent)on this page. |

### **Data collected depending on your usage**

Depending on how you configure or invoke theFirebase App CheckSDKs and the product's features, your app may collect end-user data that needs to be included in your data disclosure. The following table lists examples of end-user data that can be collected depending on your usage, but make sure to account for any data collected by your specific usage.

|                                                Data                                                |                                                                     Depending on your app's configuration and invocation, theFirebase App CheckSDKs...                                                                      |
|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Integrity token from[Play Integrity](https://developer.android.com/google/play/integrity/overview) | Collect this integrity token if your app uses Play Integrity as an attestation provider. See additional[data safety information for Play Integrity](https://developer.android.com/google/play/integrity/terms#data-safety). |

### **Additional information**

#### Purpose for data collection

The Firebase user agent is used internally by Google to determine platform and version adoption in order to provide, maintain, and improve Firebase services. It is never linked to a user or device identifier.

Firebase App Checkgenerally uses the other collected data listed in the sub-sections above to validate app attestations to help protect your backend resources from abuse. Also, review the sub-sections above for information about how*specific*data may be used. In your data disclosure, make sure to also account for how you specifically use the collected data.

<br />

*** ** * ** ***

## **App Distribution**

#### FullApp DistributionAndroid SDK implementation

`com.google.firebase:firebase-appdistribution`

The fullApp DistributionAndroid SDK implementation is intended for Beta testing usage only. Do not include the fullApp DistributionSDK implementation in your application when submitting toGoogle Play.

#### API-onlyApp DistributionAndroid SDK

`com.google.firebase:firebase-appdistribution-api`  
`com.google.firebase:firebase-appdistribution-api-ktx`

### **Data collected automatically**

The API-onlyApp DistributionAndroid SDK does not*automatically*collect any end-user data.

### **Data collected depending on your usage**

The API-onlyApp DistributionAndroid SDK doesn't have optional features that the developer can configure or invoke to collect other end-user data.

<br />

*** ** * ** ***

## **Authentication**

`com.google.firebase:firebase-auth`  
`com.google.firebase:firebase-auth-ktx`

### **Data collected automatically**

TheFirebase AuthenticationSDK collects the following data*automatically*.

|                                                             Data                                                             |                                                        By default, theFirebase AuthenticationSDK...                                                        |
|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Firebase user agent                                                                                                          | For information, refer to the[Firebase user agent section](https://firebase.google.com/docs/android/play-data-disclosure#firebase-user-agent)on this page. |
| IP address                                                                                                                   | Collects IP addresses to provide added security and prevent abuse during sign-up and authentication.                                                       |
| User agent strings: - whether the app uses FirebaseUI - version ofAuthenticationSDK used by the app - platform of the device | Collects user agent strings to provide, maintain, and improve Firebase services. Note that this user agent is*not* referring to the*Firebase user agent*.  |
| Firebase Android App ID                                                                                                      | Collects the Firebase Android App ID of the app (this is not the app's package name). This value is included in the header of each request.                |

### **Data collected depending on your usage**

Depending on how you configure or invoke theFirebase AuthenticationSDK and the product's features, your app may collect end-user data that needs to be included in your data disclosure. The following table lists examples of end-user data that can be collected depending on your usage, but make sure to account for any data collected by your specific usage.

|                                                Data                                                |                                                                                                                                                         Depending on your app's configuration and invocation, theFirebase AuthenticationSDK...                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Display name                                                                                       | Collects a user's display name if the developer provides it.                                                                                                                                                                                                                                                                                                                                            |
| Email address                                                                                      | Collects a user's email address (as provided by the developer) if the app uses any of the following: - email password authentication - email link authentication - a federated identity as an authentication method and the federated provider's response contains the email address                                                                                                                    |
| Phone number                                                                                       | Collects a user's phone number (as provided by the developer) if the app uses any of the following: - phone authentication - phone number as an authentication method - SMS-as-second-factor authentication flows                                                                                                                                                                                       |
| Integrity token from[Play Integrity](https://developer.android.com/google/play/integrity/overview) | Collects this integrity token if your app uses Phone Authentication. See additional[data safety information for Play Integrity](https://developer.android.com/google/play/integrity/terms#data-safety).                                                                                                                                                                                                 |
| Token from[reCAPTCHA Enterprise](https://cloud.google.com/recaptcha-enterprise/docs)               | Collects this token if your app uses[reCAPTCHA Enterprise to protectAuthenticationflows](https://cloud.google.com/identity-platform/docs/recaptcha-enterprise). See additional[data safety information for reCAPTCHA Enterprise](https://cloud.google.com/recaptcha-enterprise/docs/disclosure-requirements-android).                                                                                   |
| Contact information                                                                                | Collects a user's contact information related to third-party authentication providers if the app uses a third-party authentication provider with Firebase Authentication. For example, a user's identifier may be linked to their Facebook profile if the app uses Facebook authentication, depending on the scopes granted. Refer to the authentication provider's documentation for more information. |
| Game Center ID                                                                                     | Collects a user's Game Center ID if the app is linked to the[Game Center](https://developer.apple.com/game-center/).                                                                                                                                                                                                                                                                                    |
| User ID                                                                                            | Generates and stores a uniqueFirebase Authenticationidentifier.                                                                                                                                                                                                                                                                                                                                         |

### **Additional information**

#### Purpose for data collection

Firebase Authenticationgenerally uses the collected data listed in the sub-sections above to enable authentication and account management. User agent strings are used to provide, maintain, and improve Firebase services. Also, review the sub-sections above for information about how*specific*data may be used. In your data disclosure, make sure to also account for how you specifically use the collected data.

<br />

*** ** * ** ***

## **Cloud Firestore**

`com.google.firebase:firebase-firestore`  
`com.google.firebase:firebase-firestore-ktx`

### **Data collected automatically**

TheCloud FirestoreSDK collects the following data*automatically*.

|        Data         |                                                            By default, theCloud FirestoreSDK...                                                            |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Firebase user agent | For information, refer to the[Firebase user agent section](https://firebase.google.com/docs/android/play-data-disclosure#firebase-user-agent)on this page. |

### **Data collected depending on your usage**

Depending on how you configure or invoke theCloud FirestoreSDK and the product's features, your app may collect end-user data that needs to be included in your data disclosure. Make sure that you account for any developer-defined end-user data that's collected by your specific usage.

#### Other considerations

If you useCloud FirestorewithFirebase Authentication, and if an end-user is signed-in, then every request fromCloud Firestoreautomatically includes the applicable User ID fromFirebase Authentication.

### **Additional information**

#### Purpose for data collection

The Firebase user agent is used internally by Google to determine platform and version adoption in order to provide, maintain, and improve Firebase services. It is never linked to a user or device identifier.

Review the sub-sections above for information about how*specific*data may be used. In your data disclosure, make sure to also account for how you specifically use the collected data, in addition to how you use any developer-defined end-user data collected by the SDK.

<br />

*** ** * ** ***

## **Cloud Functions for Firebase**

`com.google.firebase:firebase-functions`  
`com.google.firebase:firebase-functions-ktx`

### **Data collected automatically**

TheCloud Functions for FirebaseClient SDKcollects the following data*automatically*.

|                Data                 |                                                                                                    By default, theCloud Functions for FirebaseClient SDK...                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Function name                       | Collects the function name at function invocation.                                                                                                                                                                                                             |
| IP address                          | Collects the IP address of the function caller at function invocation in order to execute event-handling functions and HTTP functions based on end-user actions.                                                                                               |
| Firebase Cloud Messaging(FCM) token | Collects theFCMtoken to allow developers to use it in their functions to send notifications to the calling device at the time of call or to store it for later. Note that this token is collected independently of whether the app includes or uses theFCMSDK. |

### **Data collected depending on your usage**

TheCloud Functions for FirebaseClient SDKdoesn't have optional features that the developer can configure or invoke to collect other end-user data.

#### Other considerations

If an end-user is signed-in viaFirebase Authentication, every function request automatically includes the applicable User ID fromFirebase Authentication.

### **Additional information**

#### Purpose for data collection

Cloud Functions for Firebasegenerally uses the collected data listed in the sub-sections above to run backend code in response to events triggered by Firebase features and HTTPS requests from your app. Also, review the sub-sections above for information about how*specific*data may be used. In your data disclosure, make sure to also account for how you specifically use the collected data.

<br />

*** ** * ** ***

## **Cloud Messaging**

`com.google.firebase:firebase-messaging`  
`com.google.firebase:firebase-messaging-ktx`

### **Data collected automatically**

TheFirebase Cloud MessagingSDK collects the following data*automatically*.

|        Data         |                                                       By default, theFirebase Cloud MessagingSDK...                                                        |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Application version | Collects the app's version for topic subscription and unsubscription.                                                                                      |
| Firebase user agent | For information, refer to the[Firebase user agent section](https://firebase.google.com/docs/android/play-data-disclosure#firebase-user-agent)on this page. |

#### Other considerations

Cloud Messaginghas a dependency on theFirebaseinstallations SDK. Since that SDK is transitively included in your app, make sure to account for the end-user data collected automatically by that SDK (see the[installations section](https://firebase.google.com/docs/android/play-data-disclosure#installations)on this page). To learn about the data thatCloud Messaginguses from that SDK's data collection, visit the[ManageFirebaseinstallations documentation](https://firebase.google.com/docs/projects/manage-installations).

### **Data collected depending on your usage**

Depending on how you configure or invoke theFirebase Cloud MessagingSDK and the product's features, your app may collect end-user data that needs to be included in your data disclosure. The following table lists examples of end-user data that can be collected depending on your usage, but make sure to account for any data collected by your specific usage.

|           Data           |                                                                                                                                                                     Depending on your app's configuration and invocation, theFirebase Cloud MessagingSDK...                                                                                                                                                                      |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Message delivery metrics | Collects and sends[message delivery metrics](https://firebase.google.com/docs/cloud-messaging/understand-delivery?platform=android#export-platform)to BigQuery if the BigQuery integration is enabled and[`setDeliveryMetricsExportToBigQuery`](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#public-void-setdeliverymetricsexporttobigquery-boolean-enable)is set to true. |

#### Other considerations

Some optional features ofCloud Messagingdepend on the Firebase SDK for Google Analytics. If you include that SDK in your app, make sure to account for the end-user data collected automatically by that SDK (see the[Google Analytics documentation](https://firebase.google.com/docs/android/play-data-disclosure#analytics)). The following table lists additional logged data:

|              Data               |                                     If your app includes the Firebase SDK for Google Analytics, thenCloud Messaging...                                      |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Notification interaction events | Sends message interaction events locally on-device for logging via the Firebase SDK for Google Analytics in order to provide analytics data for developers. |

### **Additional information**

#### Purpose for data collection

The Firebase user agent is used internally by Google to determine platform and version adoption in order to provide, maintain, and improve Firebase services. It is never linked to a user or device identifier.

Cloud Messaginggenerally uses the other collected data listed in the sub-sections above to send messages to the client app. Also, review the sub-sections above for information about how*specific*data may be used. In your data disclosure, make sure to also account for how you specifically use the collected data.

<br />

*** ** * ** ***

## **Cloud Storage for Firebase**

`com.google.firebase:firebase-storage`  
`com.google.firebase:firebase-storage-ktx`

### **Data collected automatically**

TheCloud Storage for FirebaseSDK collects the following data*automatically*.

|                      Data                      |                                                By default, theFirebase Cloud MessagingSDK...                                                |
|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Version of theCloud StorageSDK used by the app | Collects the version of theCloud Storage for FirebaseSDK used by the app. This value is included in the header of each request.             |
| Firebase Android App ID                        | Collects the Firebase Android App ID of the app (this is not the app's package name). This value is included in the header of each request. |

### **Data collected depending on your usage**

Depending on how you configure or invoke theCloud Storage for FirebaseSDK and the product's features, your app may collect end-user data that needs to be included in your data disclosure. Make sure that you account for any developer-defined end-user data that's collected by your specific usage.

#### Other considerations

If you useCloud Storage for FirebasewithFirebase Authentication, and if an end-user is signed-in, then every request fromCloud Storage for Firebaseautomatically includes the applicable User ID fromFirebase Authentication.

### **Additional information**

#### Purpose for data collection

Cloud Storage for Firebasegenerally uses the collected data listed in the sub-sections above to provide, maintain, and improve Firebase services. Also, review the sub-sections above for information about how*specific*data may be used. In your data disclosure, make sure to also account for how you specifically use the collected data, in addition to how you use any developer-defined end-user data collected by the SDK.

<br />

*** ** * ** ***

## **Crashlytics**

`com.google.firebase:firebase-crashlytics`  
`com.google.firebase:firebase-crashlytics-ktx`  
`com.google.firebase:firebase-crashlytics-ndk`

### **Data collected automatically**

TheFirebase CrashlyticsSDK collects the following data*automatically*.

|                                           Data                                           |                                By default, theFirebase CrashlyticsSDK...                                 |
|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Stack traces                                                                             | Collects stack traces when an application crashes.                                                       |
| Relevant application state                                                               | Collects relevant application state when an application crashes.                                         |
| Relevant[device metadata](https://firebase.google.com/support/privacy#crash-stored-info) | Collects point-in-time metadata about the device when an application crashes.                            |
| Crashlyticsinstallation UUID                                                             | Generates and stores theCrashlyticsinstallation UUID to measure the number of users impacted by a crash. |

#### Other considerations

Crashlyticshas a dependency on theFirebaseinstallations SDK. Since that SDK is transitively included in your app, make sure to account for the end-user data collected automatically by that SDK (see the[installations section](https://firebase.google.com/docs/android/play-data-disclosure#installations)on this page). Note thatCrashlyticsdoesn't use any of the data collected by theFirebaseinstallations SDK, except to rotate theCrashlyticsinstallation UUID based on changes to the app instance'sFirebaseinstallation ID.

Crashlyticsalso has a dependency on theFirebase sessionsSDK to provide quality metrics in theFirebaseconsole. Since that SDK is transitively included in your app, make sure to account for the end-user data collected automatically by that SDK (see the[Firebase sessionsSDK](https://firebase.google.com/docs/android/play-data-disclosure#sessions)section on this page).

### **Data collected depending on your usage**

Depending on how you configure or invoke theFirebase CrashlyticsSDK and the product's features, your app may collect end-user data that needs to be included in your data disclosure. The following table lists examples of end-user data that can be collected depending on your usage, but make sure to account for any data collected by your specific usage.

|          Data          |        Depending on your app's configuration and invocation, theFirebase CrashlyticsSDK...         |
|------------------------|----------------------------------------------------------------------------------------------------|
| Developer-defined data | Collects any custom keys, logs, and free-text user IDs that a developer attaches to crash reports. |
| Developer-defined data | Collects any developer-defined non-fatal events with custom stack traces.                          |

#### Other considerations

Some optional features ofCrashlyticsdepend on the Firebase SDK for Google Analytics. If you include that SDK in your app, make sure to account for the end-user data collected automatically by that SDK (see the[Google Analytics documentation](https://firebase.google.com/docs/android/play-data-disclosure#analytics)). The following table lists the data thatCrashlyticsuses from that data collection:

|       Data        |                                           If your app includes the Firebase SDK for Google Analytics, thenCrashlytics...                                            |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| "breadcrumb" logs | Uses the "breadcrumb" logs collected by the Firebase SDK for Google Analytics. These logs identify user actions immediately before a crash along with crash counts. |

If you also include theFirebase Remote ConfigSDK in your app, make sure to account for the developer-definedRemote Configdata collected automatically by theCrashlyticsSDK. The following table lists the data that theCrashlyticsSDK collects:

|                      Data                      |                                          If your app includes theFirebase Remote ConfigSDK, then theCrashlyticsSDK...                                           |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Developer-definedRemote Configrollout metadata | Collects rollout metadata, which includesRemote Configtemplate versions, rollout variant IDs, parameter keys, and parameter values affected by active rollouts. |

### **Additional information**

#### Purpose for data collection

Firebase Crashlyticsgenerally uses the collected data listed in the sub-sections above to enable crash reporting and crash management services. Also, review the sub-sections above for information about how*specific*data may be used. In your data disclosure, make sure to also account for how you specifically use the collected data, in addition to how you use any developer-defined end-user data collected by the SDK.

<br />

*** ** * ** ***

## **Data Connect**

`com.google.firebase:firebase-dataconnect`

### **Data collected automatically**

TheFirebase Data ConnectSDK collects the following data*automatically*.

|                                                         Data                                                          |                                                                                                By default, theData ConnectSDK...                                                                                                 |
|-----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Whether[local code generation](https://firebase.google.com/docs/data-connect/android-sdk)forData Connectis being used | Collects whether requests to theData Connectservice are coming from code generated by theData Connectcode generator, or, instead, from direct usage of theData ConnectSDK. This value is included in the header of each request. |
| Firebase Android App ID                                                                                               | Collects the Firebase Android App ID of the app (this is not the app's package name). This value is included in the header of each request.                                                                                      |
| Firebase user agent                                                                                                   | For information, refer to the[Firebase user agent section](https://firebase.google.com/docs/android/play-data-disclosure#firebase-user-agent)on this page.                                                                       |

### **Data collected depending on your usage**

Depending on how you configure or invoke theData ConnectSDK and the product's features, your app may collect end-user data that needs to be included in your data disclosure. Make sure that you account for any developer-defined end-user data that's collected by your specific usage.

#### Other considerations

If you useData ConnectwithFirebase Authentication, and if an end-user is signed in, then every request fromData Connectautomatically includes the applicable User ID fromFirebase Authentication.

### **Additional information**

#### Purpose for data collection

The Firebase user agent is used internally by Google to determine platform and version adoption in order to provide, maintain, and improve Firebase services. It is never linked to a user or device identifier.

Review the sub-sections above for information about how*specific*data may be used. In your data disclosure, make sure to also account for how you specifically use the collected data, in addition to how you use any developer-defined end-user data collected by the SDK.

<br />

*** ** * ** ***

## **Dynamic Links**

`com.google.firebase:firebase-dynamic-links`  
`com.google.firebase:firebase-dynamic-links-ktx`

### **Data collected automatically**

TheFirebase Dynamic LinksSDK collects the following data*automatically*.

|       Data       |                                                              By default, theFirebase Dynamic LinksSDK...                                                               |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Dynamic link URL | Collects the dynamic link URL when the URL is interacted with, including the developer-defined metadata that the developer sets in the link when the link was created. |

If the app is installed with theFirebase Dynamic LinksSDK integrated, then Firebase logs the app state and link interaction events.

#### Other considerations

If a user interacts with a Firebase dynamic link, the following data is logged automatically, regardless if the app is installed on the user's device:

|        **Data**         |                                                                    **By default, Firebase...**                                                                     |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Dynamic link URL        | Logs the dynamic link URL when the URL is interacted with, including the developer-defined metadata that the developer sets in the link when the link was created. |
| Package name of the app | Logs the app's package name for deferred-deep linking (deep-link post app install).                                                                                |
| App state               | Logs information relating to the state of the app on the user's device, including install state and if the app has been opened before.                             |
| Link interaction events | Logs link interaction events.                                                                                                                                      |

### **Data collected depending on your usage**

TheFirebase Dynamic LinksSDK doesn't have optional features that the developer can configure or invoke to collect other end-user data.

#### Other considerations

Some optional features ofDynamic Linksdepend on the Firebase SDK for Google Analytics. If you include that SDK in your app, make sure to account for the end-user data collected automatically by that SDK (see the[Google Analytics documentation](https://firebase.google.com/docs/android/play-data-disclosure#analytics)). The following table lists additional logged data:

|          Data           |                                     If your app includes the Firebase SDK for Google Analytics, thenDynamic Links...                                     |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link interaction events | Sends link interaction events locally on-device for logging via the Firebase SDK for Google Analytics in order to provide analytics data for developers. |

### **Additional information**

#### Purpose for data collection

Firebase Dynamic Linksgenerally uses the collected data listed in the sub-sections above to take end users directly to the linked content in your app. Also, review the sub-sections above for information about how*specific*data may be used. In your data disclosure, make sure to also account for how you specifically use the collected data, in addition to how you use any developer-defined end-user data collected by the SDK.

<br />

*** ** * ** ***

## **Google Analytics**

`com.google.firebase:firebase-analytics`  
`com.google.firebase:firebase-analytics-ktx`

Find Google Analytics data collection information in the[Google Analytics documentation](https://support.google.com/analytics/answer/11582702).

<br />

*** ** * ** ***

## **In-App Messaging**

`com.google.firebase:firebase-inappmessaging`  
`com.google.firebase:firebase-inappmessaging-display`  
`com.google.firebase:firebase-inappmessaging-ktx`  
`com.google.firebase:firebase-inappmessaging-display-ktx`

### **Data collected automatically**

TheFirebase In-App MessagingSDK collects the following data*automatically*.

|                                   Data                                    |                   By default, theFirebase In-App MessagingSDK...                    |
|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Message interaction events, including impressions, clicks, and dismissals | Sends message interaction events in order to provide analytics data for developers. |

#### Other considerations

In-App Messaginghas a required dependency on the Firebase SDK for Google Analytics. Since you must include that SDK in your app, make sure to account for the end-user data collected automatically by that SDK (see the[Google Analytics documentation](https://firebase.google.com/docs/android/play-data-disclosure#analytics)). The following table lists examples of how theIn-App MessagingSDK interacts with data fromGoogle Analytics:

|                                   Data                                    |                                If your app includes the Firebase SDK for Google Analytics, thenFirebase In-App Messaging...                                 |
|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Message interaction events, including impressions, clicks, and dismissals | Sends message interaction events locally on-device for logging via the Firebase SDK for Google Analytics in order to provide analytics data for developers. |
| User properties                                                           | Sets and uses user properties collected by the Firebase SDK forGoogle Analyticsin order to target messages that are based on user property conditions.      |

In-App Messagingalso has a dependency on theFirebaseinstallations SDK. Since that SDK is transitively included in your app, make sure to account for the end-user data collected automatically by that SDK (see the[installations section](https://firebase.google.com/docs/android/play-data-disclosure#installations)on this page). To learn about the data thatIn-App Messaginguses from that SDK's data collection, visit the[ManageFirebaseinstallations documentation](https://firebase.google.com/docs/projects/manage-installations).

### **Data collected depending on your usage**

TheFirebase In-App MessagingSDKs don't have optional features that the developer can configure or invoke to collect other end-user data.

### **Additional information**

#### Purpose for data collection

Firebase In-App Messaginggenerally uses the collected data listed in the sub-sections above to send messages to end users within the app itself. Also, review the sub-sections above for information about how*specific*data may be used. In your data disclosure, make sure to also account for how you specifically use the collected data.

<br />

*** ** * ** ***

## **Installations**

`com.google.firebase:firebase-installations`  
`com.google.firebase:firebase-installations-ktx`

### **Data collected automatically**

TheFirebaseinstallations SDK collects the following data*automatically*.

|             Data              |                                                        By default, theFirebaseinstallations SDK...                                                         |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Firebaseinstallation ID (FID) | Generates and collects a per-installation identifier (FID) that does not uniquely identify a user or physical device.                                      |
| Firebase user agent           | For information, refer to the[Firebase user agent section](https://firebase.google.com/docs/android/play-data-disclosure#firebase-user-agent)on this page. |

### **Data collected depending on your usage**

TheFirebaseinstallations SDK doesn't have optional features that the developer can configure or invoke to collect other end-user data.

### **Additional information**

#### Purpose for data collection

The Firebase user agent is used internally by Google to determine platform and version adoption in order to provide, maintain, and improve Firebase services. It is never linked to a user or device identifier.

Firebaseinstallations generally uses the other collected data listed in the sub-sections above to provide a unique identifier to identify app installations. Also, review the sub-sections above for information about how*specific*data may be used. In your data disclosure, make sure to also account for how you specifically use the collected data.

<br />

*** ** * ** ***

## **Firebase MLmodel downloader**

`com.google.firebase:firebase-ml-modeldownloader`  
`com.google.firebase:firebase-ml-modeldownloader-ktx`

### **Data collected automatically**

TheFirebase MLmodel downloader SDK collects the following data*automatically*.

|                                        Data                                        |                                                         By default, theFirebase MLmodel downloader SDK...                                                         |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ML model download metadata, including download events, deletion events, and errors | Collects model download event metadata to monitor for stability and latency issues.                                                                               |
| installation auth token                                                            | Collects[installation auth tokens]()for device authentication when interacting with app instances (for example, to distribute developer models to app instances). |

#### Other considerations

Firebase MLmodel downloader has a dependency on theFirebaseinstallations SDK. Since that SDK is transitively included in your app, make sure to account for the end-user data collected automatically by that SDK (see the[installations section](https://firebase.google.com/docs/android/play-data-disclosure#installations)on this page). To learn about the data thatFirebase MLmodel downloader uses from that SDK's data collection, visit the[ManageFirebaseinstallations documentation](https://firebase.google.com/docs/projects/manage-installations).

### **Data collected depending on your usage**

TheFirebase MLmodel downloader SDK doesn't have optional features that the developer can configure or invoke to collect other end-user data.

### **Additional information**

#### Purpose for data collection

Firebase MLgenerally uses the collected data listed in the sub-sections above to download ML models.Firebase MLaggregates and uses the model download metadata to monitor product quality, understand usage, and inform product direction. Also, review the sub-sections above for information about how*specific*data may be used. In your data disclosure, make sure to also account for how you specifically use the collected data.

<br />

*** ** * ** ***

## **Performance Monitoring**

`com.google.firebase:firebase-perf`  
`com.google.firebase:firebase-perf-ktx`

### **Data collected automatically**

TheFirebase Performance MonitoringSDK collects the following data*automatically*.

|                                                     Data                                                     |                          By default, theFirebase Performance MonitoringSDK...                           |
|--------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| App performance metrics, including app start time and network request latency                                | Collects app performance metrics during the lifecycle and end-user usage of the app.                    |
| CPU/memory usage                                                                                             | Collects CPU/memory usage of the application to provide a timeline view of the app's performance.       |
| Relevant[device metadata](https://firebase.google.com/support/privacy#performance-monitoring-collected-info) | Collects relevant device metadata to filter the performance data against different segments of devices. |
| IP address                                                                                                   | Collects the IP address to map performance events to the countries they originate from.                 |

#### Other considerations

Performance Monitoringhas a dependency on theFirebaseinstallations SDK. Since that SDK is transitively included in your app, make sure to account for the end-user data collected automatically by that SDK (see the[installations section](https://firebase.google.com/docs/android/play-data-disclosure#installations)on this page). To learn about the data thatPerformance Monitoringuses from that SDK's data collection, visit the[ManageFirebaseinstallations documentation](https://firebase.google.com/docs/projects/manage-installations).

Performance Monitoringalso has a dependency on theFirebase Remote ConfigSDK to help control the volume of events collected from an application. Since that SDK is transitively included in your app, make sure to account for the end-user data collected automatically by that SDK (see the[Remote Configsection](https://firebase.google.com/docs/android/play-data-disclosure#remote_config)on this page).

Performance Monitoringalso has a dependency on theFirebase sessionsSDK to report timeline views of performance data in theFirebaseconsole. Since that SDK is transitively included in your app, make sure to account for the end-user data collected automatically by that SDK (see the[Firebase sessionsSDK](https://firebase.google.com/docs/android/play-data-disclosure#sessions)section on this page).

### **Data collected depending on your usage**

Depending on how you configure or invoke theFirebase Performance MonitoringSDK and the product's features, your app may collect end-user data that needs to be included in your data disclosure. The following table lists examples of end-user data that can be collected depending on your usage, but make sure to account for any data collected by your specific usage.

|                         Data                          |  Depending on your app's configuration and invocation, theFirebase Performance MonitoringSDK...   |
|-------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| Developer-defined custom traces                       | Collects app performance metrics for any custom traces that a developer instruments in their app. |
| Custom performance metrics *(developer-defined data)* | Collects any custom performance metrics that a developer attaches to custom traces.               |
| Custom attributes *(developer-defined data)*          | Collects any custom attributes that a developer attaches to custom traces.                        |

### **Additional information**

#### Purpose for data collection

Firebase Performance Monitoringgenerally uses the collected data listed in the sub-sections above to enable app performance reporting and monitoring. Also, review the sub-sections above for information about how*specific*data may be used. In your data disclosure, make sure to also account for how you specifically use the collected data, in addition to how you use any developer-defined end-user data collected by the SDK.

<br />

*** ** * ** ***

## **Firebase Phone Number Verification**

`com.google.firebase:firebase-pnv`

### **Data collected automatically**

TheFirebase PNVSDK collects the following data*automatically*.

|          Data           |                                           By default, theFirebase Phone Number VerificationSDK...                                           |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Firebase Android App ID | Collects the Firebase Android App ID of the app (this is not the app's package name). This value is included in the header of each request. |

### **Data collected depending on your usage**

Depending on how you configure or invoke theFirebase Phone Number VerificationSDK and the product's features, your app may collect end-user data that needs to be included in your data disclosure. The following table lists examples of end-user data that can be collected depending on your usage, but make sure to account for any data collected by your specific usage.

|     Data     | Depending on your app's configuration and invocation, theFirebase Phone Number VerificationSDK... |
|--------------|---------------------------------------------------------------------------------------------------|
| Phone number | Retrieves the phone number of the device (with the user's consent).                               |

### **Additional information**

#### Purpose for data collection

Firebase Phone Number Verificationis a service intended to enable apps to obtain the phone number of a device directly from the mobile carrier. The SDK requires user consent every time the app requests the device's phone number. This capability is often, but not necessarily, used for app sign-in purposes.

In your data disclosure, make sure to also account for how you specifically use the collected data, in addition to how you use any developer-defined end-user data collected by the SDK.

<br />

*** ** * ** ***

## **Realtime Database**

`com.google.firebase:firebase-database`  
`com.google.firebase:firebase-database-ktx`

### **Data collected automatically**

TheFirebase Realtime DatabaseSDK collects the following data*automatically*.

|    Data     |                                                                                                          By default, theFirebase Realtime DatabaseSDK...                                                                                                           |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IP address  | Collects IP addresses to enable the[profiler tool](https://firebase.google.com/docs/database/usage/profile), which helps developers understand usage trends and platform breakdowns                                                                                |
| User agents | Collects user agent strings to enable the[profiler tool](https://firebase.google.com/docs/database/usage/profile), which helps developers understand usage trends and platform breakdowns Note that this user agent is*not* referring to the*Firebase user agent*. |

### **Data collected depending on your usage**

Depending on how you configure or invoke theFirebase Realtime DatabaseSDK and the product's features, your app may collect end-user data that needs to be included in your data disclosure. Make sure that you account for any developer-defined end-user data that's collected by your specific usage.

#### Other considerations

If you useRealtime DatabasewithFirebase Authentication, and if an end-user is signed-in, then every request fromRealtime Databaseautomatically includes the applicable User ID fromFirebase Authentication.

### **Additional information**

#### Purpose for data collection

Please review the sub-sections above for information about how*specific*data may be used. In your data disclosure, make sure to also account for how you specifically use the collected data, in addition to how you use any developer-defined end-user data collected by the SDK.

<br />

*** ** * ** ***

## **Remote Config**

`com.google.firebase:firebase-config`  
`com.google.firebase:firebase-config-ktx`

### **Data collected automatically**

TheFirebase Remote ConfigSDK collects the following data*automatically*.

|                      Data                      |                                                   By default, theFirebase Remote ConfigSDK...                                                   |
|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Country code                                   | Collects country code in order to target parameters that are based on this data.                                                                |
| Language code                                  | Collects language code in order to target parameters that are based on this data.                                                               |
| Time zone                                      | Collects time zone in order to target parameters that are based on this data.                                                                   |
| Platform version                               | Collects platform version in order to target parameters that are based on this data.                                                            |
| OS version                                     | Collects OS version in order to target parameters that are based on this data.                                                                  |
| Firebase Android App ID                        | Collects the Firebase Android App ID of the app (this is not the app's package name) in order to target parameters that are based on this data. |
| Package name of the app                        | Collects the package name in order to target parameters that are based on this data.                                                            |
| Version of theRemote ConfigSDK used by the app | Collects the version of the SDK to provide, maintain, and improve Firebase services.                                                            |

#### Other considerations

Remote Confighas a dependency on theFirebaseinstallations SDK. Since that SDK is transitively included in your app, make sure to account for the end-user data collected automatically by that SDK (see the[installations section](https://firebase.google.com/docs/android/play-data-disclosure#installations)on this page). To learn about the data thatRemote Configuses from that SDK's data collection, visit the[ManageFirebaseinstallations documentation](https://firebase.google.com/docs/projects/manage-installations).

### **Data collected depending on your usage**

TheFirebase Remote ConfigSDK doesn't have optional features that the developer can configure or invoke to collect other end-user data.

#### Other considerations

Some optional features ofRemote Configdepend on the Firebase SDK for Google Analytics. If you include that SDK in your app, make sure to account for the end-user data collected automatically by that SDK (see the[Google Analytics documentation](https://firebase.google.com/docs/android/play-data-disclosure#analytics)). The following table lists examples of how theRemote ConfigSDK interacts with data fromGoogle Analytics:

|      Data       |                                     If your app includes the Firebase SDK for Google Analytics, thenRemote Config...                                     |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| User properties | Collects user properties obtained by the Firebase SDK forGoogle Analyticsin order to target parameters that are based on user property conditions.       |
| First open time | Collects the`first_open`event timestamp obtained by the Firebase SDK forGoogle Analyticsin order to target parameters that are based on first open time. |

IfRemote Configpersonalization is implemented, the data obtained by theFirebase Remote ConfigSDK and the events obtained by the Firebase SDK forGoogle Analyticscan be used to construct predictive models and measure the performance of those models.

### **Additional information**

#### Purpose for data collection

Firebase Remote Configgenerally uses the collected data listed in the sub-sections above to change the behavior and appearance of your app without publishing an app update. Aggregated data for OS version and SDK version is used by Firebase to understand usage trends and inform product direction. Also, review the sub-sections above for information about how*specific*data may be used. In your data disclosure, make sure to also account for how you specifically use the collected data.

<br />

*** ** * ** ***

## Transitively included Firebase libraries

The Firebase libraries listed in this section are transitively included in some of the other Firebase libraries. None of the following libraries have an accessible surface for developers, but they might collect end-user data (see each library below for details).

### Firebase sessions

`com.google.firebase:firebase-sessions`

#### Data collected automatically

TheFirebase sessionsSDK collects the following data*automatically*.

|        Data         |                                            By default, theFirebase sessionsSDK...                                            |
|---------------------|------------------------------------------------------------------------------------------------------------------------------|
| App metadata        | Collects metadata about the application, such as the package name, OS information, SDK version, and network connection type. |
| Device metadata     | Collects metadata about the application, such as device manufacturer and model.                                              |
| Application metrics | Collects usage data such as the time an app was foregrounded to start a new session.                                         |

#### Data collected depending on your usage

TheFirebase sessionsSDK doesn't have optional features that the developer can configure or invoke to collect other end-user data.

#### Additional Information

##### Purpose for data collection

TheFirebase sessionsSDK uses the collected data listed in the sub-sections above to provide crash and performance metrics for the application. Also, review the sub-sections above for information about how*specific*data may be used. In your data disclosure, make sure to also account for how you specifically use the collected data, in addition to how you use any developer-defined end-user data collected by the SDK.

<br />

*** ** * ** ***

## Other helpful resources

- [Prepare for Apple's App Store data disclosure requirements](https://firebase.google.com/docs/ios/app-store-data-collection)
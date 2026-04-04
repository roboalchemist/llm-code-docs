# Source: https://firebase.google.com/docs/ios/app-store-data-collection.md.txt

<br />

Apple requires developers publishing apps on the App Store to disclose[certain information](https://developer.apple.com/app-store/app-privacy-details/)regarding their apps' data use.
| **Note:** Firebase's[privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files)disclose data that is always collected and collected by default.**It is your responsibility to ensure your privacy nutrition labels are accurate based on your app's actual usage of Firebase.** For example, if you decide to store APNs tokens inCloud Firestore, then you might consider disclosing that your app collects identifiers even though the published privacy manifest forCloud Firestoredoes not state thatCloud Firestorecollects identifiers.

This document contains Firebase Apple platform library behaviors that could require disclosure according to Apple's guidelines. When installing Firebase, take note of the build targets installed into your app by your dependency manager of choice. For each target that your dependency manager lists, review the corresponding section of this document to determine what data collection you must disclose. The number of Firebase build targets you have installed may be greater than the number you expected since some Firebase build targets have transient dependencies on others.

If you are using any optional product features that involve additional data or participating in any tests of new product features that involve additional data, be sure to check if those features or tests require additional data disclosures.

To ensure your app's disclosures are accurate, we recommend that you always use the latest version of each Firebase SDK.

## Firebase user agent

The***Firebase user agent***is a bundle of information collected from most Firebase SDKs and includes the following: device, OS, app bundle ID, and developer platform. The user agent is never linked to a user or device identifier and is used by the Firebase team to determine platform and version adoption in order to better inform Firebase feature decisions.

## `FirebaseCore`

- Does not collect data.

## `GoogleUtilities`

- Does not collect data, but includes networking utilities which may be used by other SDKs to collect data.

## `GoogleDataTransport`

Includes networking utilities which may be used by other SDKs to collect data.

### Always collected

- Collects metadata about SDK performance, such as the size of the client log event cache and the number of client log events dropped for various reasons, to monitor and maintain product quality.

## `FirebaseABTesting`

A/B Testing does not collect data.

TheFirebase A/B TestingSDK sets and usesGoogle Analyticsuser properties in order to specify membership in experiment groups forFirebase Remote ConfigandFirebase In-App Messaging.

## `FirebaseAILogic`

*Firebase AI Logicwas formerly called "Vertex AI in Firebase" with the library`FirebaseVertexAI`. Also,Firebase AI Logicformerly had the library`FirebaseAI`.*

### Always collected

- Collects the Firebase SDK version and the Swift language version.
- Collects the model name at invocation.

### Collected by default

- If[data collection](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp#isdatacollectiondefaultenabled)is enabled, collects the Firebase Apple app ID and the application version.

### Usage dependent

- If[AI monitoring in theFirebaseconsole](https://firebase.google.com/docs/ai-logic/monitoring#ai-monitoring-in-console)is enabled for theVertex AIGemini API, then the prompts and generated output from each sampled request are collected along with performance and usage metrics.

## Google Analytics

Google Analyticsdata collection information can be found in this[support article](https://support.google.com/analytics/answer/10285841).

## `FirebaseAppCheck`

### Collected by default

- If[data collection](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp#isdatacollectiondefaultenabled)is enabled, collects the[Firebase user agent](https://firebase.google.com/docs/ios/app-store-data-collection#firebase-user-agent).

### Usage dependent

- If the DeviceCheck provider is installed, collects the`DCDevice`token from[DeviceCheck](https://developer.apple.com/documentation/devicecheck).
- If the App Attest provider is installed, collects both the attestation object and the assertion object from[App Attest](https://developer.apple.com/documentation/devicecheck/validating_apps_that_connect_to_your_server).

## `FirebaseAppDistribution`

The App Distribution SDK is intended for beta testing usage only. Do not include the App Distribution SDK in your application when submitting to the App Store.

## `FirebaseAuthentication`

### Always collected

- Generates and stores identifiers for user authentication purposes.

### Collected by default

- If[data collection](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp#isdatacollectiondefaultenabled)is enabled, collects the[Firebase user agent](https://firebase.google.com/docs/ios/app-store-data-collection#firebase-user-agent).

### Usage dependent

- Collects a display name, if the developer provides a display name for the user.
- Collects users' email addresses as provided by the developer when using email password or email link authentication, or as contained in the response from a federated provider if the developer uses a federated identity.
- Collects users' phone numbers as provided by the developer when using phone auth or if the user's phone number is added as an authentication method. Also collected during SMS-as-second-factor authentication flows.
- Collects contact information related to third-party authentication providers if the developer uses a third-party authentication provider withFirebase Authentication. For example, a user's identifier may be linked to their Facebook profile if the developer uses Facebook authentication, depending on the scopes granted. Refer to the authentication provider's documentation for more information.
- Stores the user's Game Center ID if the app is linked to the Game Center.
- Collects this token if your app uses[reCAPTCHA Enterprise](https://cloud.google.com/identity-platform/docs/recaptcha-enterprise)to protectAuthenticationflows. See additional[Apple privacy details for reCAPTCHA Enterprise](https://cloud.google.com/recaptcha-enterprise/docs/apple-privacy-details).

## `FirebaseCrashlytics`

### Always collected

- Collects stack traces and relevant application state when an application crashes.
- Collects[device and OS information](https://firebase.google.com/support/privacy#crash-stored-info)to assist with debugging crashes.

### Usage dependent

- Collects any custom keys, logs, and free-text user IDs that developers attach to crash reports. Also collects any developer-defined non-fatal events with custom stack traces.
- Collects "breadcrumb" logs ifCrashlyticsis used together withGoogle Analytics. These logs identify user actions immediately before a crash along with crash counts.
- Collects developer-defined portions of the[Remote Configtemplate](https://firebase.google.com/docs/remote-config/templates)and template metadata if theFirebase Remote ConfigSDK is also included in the app. This data includesRemote Configtemplate version, rollout variant ID, parameter keys, and parameter values affected by active rollouts.

## `FirebaseDatabase`

### Collected by default

- If[data collection](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp#isdatacollectiondefaultenabled)is enabled, collects the[Firebase user agent](https://firebase.google.com/docs/ios/app-store-data-collection#firebase-user-agent).

## `FirebaseDataConnect`

### Collected by default

If[data collection](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp#isdatacollectiondefaultenabled)is enabled:

- Collects the[Firebase user agent](https://firebase.google.com/docs/ios/app-store-data-collection#firebase-user-agent).
- Collects whether[local code generation](https://firebase.google.com/docs/data-connect/ios-sdk)forData Connectis being used by checking whether requests to theData Connectservice are coming from code generated by the code generator, or, instead, from direct usage of theData ConnectSDK.
- Collects the Firebase App ID of the app (this is not the app's bundle ID). This value is included in the header of each request.

## `FirebaseDynamicLinks`

### Always collected

- Temporarily collects device data, including the device's screen dimensions, language, OS version, bundle ID, IP address, and Firebase SDK version for deferred-deep links (deep-link post app install).

### Collected by default

- Temporarily collects the dynamic link URL in the device pasteboard, if available, on first app launch. Developers can disable the use of Pasteboard by setting the`FirebaseDeepLinkPasteboardRetrievalEnabled`property to`NO`in the app's`Info.plist`file.

### Usage dependent

IfDynamic Linksis used together withGoogle Analytics:

- Automatically logs link interaction events viaGoogle Analytics. To disable automatic event logging, remove`FirebaseAnalytics`from the app.

## `FirebaseFirestore`

### Collected by default

- If[data collection](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp#isdatacollectiondefaultenabled)is enabled, collects the[Firebase user agent](https://firebase.google.com/docs/ios/app-store-data-collection#firebase-user-agent).

## `FirebaseFunctions`

### Always collected

- Collects function invocation metadata, including the function name and IP address of the function caller.

## `FirebaseInAppMessaging`

### Always collected

- Records interactions with in-app messages. These interactions (impressions, clicks, dismissals) are recorded viaGoogle Analytics. Interactions are also recorded by Firebase to help developers evaluate the effectiveness of messaging campaigns.

## `FirebaseInstallations`

### Collected by default

- If[data collection](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp#isdatacollectiondefaultenabled)is enabled, collects the[Firebase user agent](https://firebase.google.com/docs/ios/app-store-data-collection#firebase-user-agent).

## `FirebaseMessaging`

### Always collected

- Records the APNs token and associates it with a collected app installation ID that acts as the Firebase Cloud Messaging (FCM) registration token.
- Collects device model, language, time zone, OS version, application identifier and application version for topic subscription and unsubscription.

### Collected by default

- If[data collection](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp#isdatacollectiondefaultenabled)is enabled, collects the[Firebase user agent](https://firebase.google.com/docs/ios/app-store-data-collection#firebase-user-agent).

### Usage dependent

IfCloud Messagingis used together withGoogle Analytics:

- Automatically logs notification interactions viaGoogle Analytics. To disable this behavior, remove`FirebaseAnalytics`from your app.

## `FirebaseMLModelDownloader`

### Always collected

- Collects ML model download metadata, such as download events, deletion events, and errors.

## `FirebasePerformance`

### Always collected

- Collects IP addresses to provide geography-based segmentation of performance data.
- Collects app performance metrics such as app launch time and network request latency, as well as developer-specified custom traces to measure app performance.
- Collects CPU/memory usage of the application to provide a timeline view of the app's performance.
- Collects[device information, OS information, and application information](https://firebase.google.com/support/privacy#performance-monitoring-collected-info)to filter the performance data against different segments of devices.

## `FirebaseRemoteConfig`

### Always collected

- Collects the device's country code, language code, time zone, OS version, Firebase Apple app ID, and bundle ID in order to target parameters that are based on this data. OS version and SDK version are also collected and aggregated to understand usage trends and inform product direction.

### Collected by default

- If[data collection](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp#isdatacollectiondefaultenabled)is enabled, collects the[Firebase user agent](https://firebase.google.com/docs/ios/app-store-data-collection#firebase-user-agent).

### Usage dependent

IfRemote Configis used together withGoogle Analytics:

- Collects user properties obtained by the Firebase SDK forGoogle Analyticsin order to target parameters that are based on user property conditions.
- Collects the`first_open`event timestamp obtained by the Firebase SDK forGoogle Analyticsin order to target parameters that are based on first open time.

IfRemote Configpersonalization is used:

- The data obtained by theFirebase Remote ConfigSDK and the events obtained by the Firebase SDK forGoogle Analyticscan be used to construct predictive models and measure the performance of those models.

## `FirebaseSessions`

### Always collected

- Collects metadata about app performance, such as the bundle ID, OS information, SDK version, and network connection type to monitor app quality.
- Collects usage data such as the time an app was backgrounded to group performance metrics into user sessions for filtering usage by session.

## `FirebaseStorage`

### Collected by default

- If[data collection](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp#isdatacollectiondefaultenabled)is enabled, collects the[Firebase user agent](https://firebase.google.com/docs/ios/app-store-data-collection#firebase-user-agent).
# Source: https://firebase.google.com/docs/android/android-play-services.md.txt

<br />

Some Firebase Android SDKs depend on[Google Playservices](https://developers.google.com/android/guides/overview), which means they will only run on devices and emulators withGoogle Playservicesinstalled. These Firebase SDKs communicate with theGoogle Playservicesbackground service on the device to provide a secure, up-to-date, and lightweight API to your app. Certain Android devices, such as Amazon Kindle Fire devices or those sold in some regions, do not haveGoogle Playservicesinstalled.
| **Note:** The[`google-services`Gradle plugin](https://developers.google.com/android/guides/google-services-plugin)is used by all Firebase SDKs, but this plugin is not related toGoogle Playservices.

## Which Firebase Android SDKs requireGoogle Playservices?

Firebase SDKs can be divided into three categories:

- **Playservicesrequired** --- These SDKs requireGoogle Playservices, otherwise they have no functionality.
- **Playservicesrecommended** --- These SDKs requireGoogle Playservicesto have*full* functionality, but they still offer*most* functionality even withoutGoogle Playservices.
- **Playservicesnot required** --- These SDKS do not requireGoogle Playservicesto have full functionality.

The tables below are accurate only for the[latest release](https://firebase.google.com/support/release-notes/android#latest_sdk_versions)of each SDK. Some older versions may have stricter requirements.

### Google Playservicesnotrequired

|                Product                 |                                             Library                                             | Google Playservices? |
|----------------------------------------|-------------------------------------------------------------------------------------------------|----------------------|
| Firebase AI Logic^1^                   | com.google.firebase:firebase-ai:17.7.0                                                          | Not Required         |
| App Checkcustom and debug providers    | com.google.firebase:firebase-appcheck:19.0.1 com.google.firebase:firebase-appcheck-debug:19.0.1 | Not Required         |
| App DistributionAPI                    | com.google.firebase:firebase-appdistribution-api:16.0.0-beta17                                  | Not Required         |
| App Distribution                       | com.google.firebase:firebase-appdistribution:16.0.0-beta17                                      | Not Required         |
| Authentication                         | com.google.firebase:firebase-auth:24.0.1                                                        | Not Required         |
| Cloud Firestore                        | com.google.firebase:firebase-firestore:26.0.2                                                   | Not Required         |
| Cloud Functions for FirebaseClient SDK | com.google.firebase:firebase-functions:22.1.0                                                   | Not Required         |
| Cloud Storage for Firebase             | com.google.firebase:firebase-storage:22.0.1                                                     | Not Required         |
| Crashlytics                            | com.google.firebase:firebase-crashlytics:20.0.3                                                 | Not Required         |
| Data Connect                           | com.google.firebase:firebase-dataconnect:17.1.2                                                 | Not Required         |
| In-App Messaging                       | com.google.firebase:firebase-inappmessaging:22.0.2                                              | Not Required         |
| In-App MessagingDisplay                | com.google.firebase:firebase-inappmessaging-display:22.0.2                                      | Not Required         |
| Firebaseinstallations                  | com.google.firebase:firebase-installations:19.0.1                                               | Not Required         |
| Performance Monitoring                 | com.google.firebase:firebase-perf:22.0.4                                                        | Not Required         |
| Realtime Database                      | com.google.firebase:firebase-database:22.0.1                                                    | Not Required         |
| Remote Config                          | com.google.firebase:firebase-config:23.0.1                                                      | Not Required         |
| **DEPRECATED OR UNSUPPORTED LIBRARIES**                                                                                                                       |||
| **Firebase KTX modules - no longer supported** | **In[July 2025](https://firebase.google.com/support/release-notes/android#2025-07-21), we stopped releasing new versions of KTX modules for Firebase libraries, and we removed the KTX libraries from theFirebase Android BoM(v34.0.0).** | If you use KTX APIs from the previously released KTX modules, we strongly recommend that you***migrate your app to use KTX APIs from the main modules instead*** . For details, see the[FAQ about this initiative](https://firebase.google.com/docs/android/kotlin-migration). |----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------| | App Check                              | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-appcheck-ktx:18.0.0                                                                      | Not Required | | App DistributionAPI                    | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-appdistribution-api-ktx:16.0.0-beta15                                                    | Not Required | | Authentication                         | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-auth-ktx:23.2.1                                                                          | Not Required | | Cloud Firestore                        | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-firestore-ktx:25.1.4                                                                     | Not Required | | Cloud Functions for FirebaseClient SDK | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-functions-ktx:21.2.1                                                                     | Not Required | | Cloud Storage for Firebase             | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-storage-ktx:21.0.2                                                                       | Not Required | | Crashlytics                            | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-crashlytics-ktx:19.4.4                                                                   | Not Required | | In-App Messaging                       | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-inappmessaging-ktx:21.0.2 com.google.firebase:firebase-inappmessaging-display-ktx:21.0.2 | Not Required | | Firebaseinstallations                  | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-installations-ktx:18.0.0                                                                 | Not Required | | Performance Monitoring                 | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-perf-ktx:21.0.5                                                                          | Not Required | | Realtime Database                      | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-database-ktx:21.0.0                                                                      | Not Required | | Remote Config                          | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-config-ktx:22.1.2                                                                        | Not Required | |||

^**1** *Firebase AI Logicwas formerly called "Vertex AI in Firebase" with the package`com.google.firebase:firebase-vertexai`.*^

### Google Playservicesrequired or recommended

|              Product               |                          Library                           | Google Playservices? |
|------------------------------------|------------------------------------------------------------|----------------------|
| AdMob                              | com.google.android.gms:play-services-ads:24.9.0            | Recommended^2^       |
| Analytics                          | com.google.firebase:firebase-analytics:23.0.0              | Recommended^2^       |
| App CheckPlay Integrity provider   | com.google.firebase:firebase-appcheck-playintegrity:19.0.1 | Required             |
| App Indexing                       | com.google.firebase:firebase-appindexing:20.0.0            | Required             |
| Cloud Messaging                    | com.google.firebase:firebase-messaging:25.0.1              | Required             |
| Firebase Phone Number Verification | com.google.firebase:firebase-pnv:16.0.0-beta01             | Required             |
| Firebase MLVision                  | com.google.firebase:firebase-ml-vision:24.1.0              | Required             |
| Firebase MLCustom Model            | com.google.firebase:firebase-ml-model-interpreter:22.0.4   | Required             |
| **DEPRECATED OR UNSUPPORTED LIBRARIES**                                                                              |||
| Dynamic Links                      | com.google.firebase:firebase-dynamic-links:22.1.0          | Required             |
| **Firebase KTX modules - no longer supported** | **In[July 2025](https://firebase.google.com/support/release-notes/android#2025-07-21), we stopped releasing new versions of KTX modules for Firebase libraries, and we removed the KTX libraries from theFirebase Android BoM(v34.0.0).** | If you use KTX APIs from the previously released KTX modules, we strongly recommend that you***migrate your app to use KTX APIs from the main modules instead*** . For details, see the[FAQ about this initiative](https://firebase.google.com/docs/android/kotlin-migration). |-----------------|-------------------------------------------------------------------------------------------------------------------|----------------| | Analytics       | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-analytics-ktx:22.5.0     | Recommended^2^ | | Cloud Messaging | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-messaging-ktx:24.1.2     | Required       | | Dynamic Links   | *Do not use; KTX module libraries are no longer supported.* com.google.firebase:firebase-dynamic-links-ktx:22.1.0 | Required       | |||

^**2** *The Firebase SDK for Google Analytics can send events on any device, but some automatic insights such as demographics are only available on devices withGoogle Playservices.*^
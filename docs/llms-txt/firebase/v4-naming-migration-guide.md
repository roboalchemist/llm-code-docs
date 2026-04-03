# Source: https://firebase.google.com/docs/ios/v4-naming-migration-guide.md.txt

In version 4.0.0 of the Firebase iOS SDK for Swift, we included changes to follow the naming conventions in the[Swift API Design Guidelines](https://swift.org/documentation/api-design-guidelines/). To fix any errors or warnings you might receive when you update your app's version of the Firebase iOS SDK, follow the steps in this migration guide.
| **Note:** These changes are for Swift only. No naming changes have been made to the Objective-C SDK.

## Changes in the new version

The following changes have been made to the Swift SDK across all Firebase products:

- Removing the`FIR`prefix across names for all constants, protocols, classes, enums, and type definitions.
- Renaming`FIRApp`to`FirebaseApp`.
- Renaming`FIROptions`to`FirebaseOptions`.

For a full list of the changes, see the[detailed list of changes section](https://firebase.google.com/docs/ios/v4-naming-migration-guide#detailed_list_of_changes).

## Resolve errors

The best way to resolve errors resulting from these changes is to use the Fix-it dialog in Xcode.

1. When you open your updated project in your Xcode workspace, errors resulting from the naming changes appear in the[issue navigator](https://help.apple.com/xcode/mac/8.3/index.html?localePath=en.lproj#/dev88d75d488).
2. Click the error and resolve it with the suggestion in the[Fix-it dialog](https://help.apple.com/xcode/mac/8.3/index.html?localePath=en.lproj#/dev5b37f5c1d).

## Resolve naming conflicts

To resolve naming conflicts, use the namespace provided by the module. For example, in the case of`FIRUser`, which is now`User`, you may want to differentiate between your`User`class/struct and the Firebase`User`class.  

```python
@import Firebase
...
var firebaseUser: Firebase.User?
```

<br />

## Detailed list of changes

#### Analytics

|                  Previous                  |                   New                   |
|--------------------------------------------|-----------------------------------------|
| Functions                                                                           ||
| `FIRAnalytics`                                                                      ||
| `logEvent(withName:parameters:)`           | `logEvent(_:parameters:)`               |
| **Previous usage:** ```text FIRAnalytics.logEvent(withName: "com.myapp.appStart", parameters: nil) ``` **New usage:** ```text Analytics.logEvent("com.myapp.appStart", parameters: nil) ``` ||
| `setUserPropertyString(_:forName:)`        | `setUserProperty(_:forName:)`           |
| **Previous usage:** ```text FIRAnalytics.setUserPropertyString("mechanic", forName: "job") ``` **New usage:** ```text Analytics.setUserProperty("mechanic", forName: "job") ``` ||
| Classes                                                                             ||
| `FIRAnalytics`                             | `Analytics`                             |
| Constants                                                                           ||
| `FIRAnalyticsEventAddPaymentInfo`          | `AnalyticsEventAddPaymentInfo`          |
| `FIRAnalyticsEventAddToCart`               | `AnalyticsEventAddToCart`               |
| `FIRAnalyticsEventAddToWishlist`           | `AnalyticsEventAddToWishlist`           |
| `FIRAnalyticsEventAppOpen`                 | `AnalyticsEventAppOpen`                 |
| `FIRAnalyticsEventBeginCheckout`           | `AnalyticsEventBeginCheckout`           |
| `FIRAnalyticsEventCampaignDetails`         | `AnalyticsEventCampaignDetails`         |
| `FIRAnalyticsEventCheckoutProgress`        | `AnalyticsEventCheckoutProgress`        |
| `FIRAnalyticsEventEarnVirtualCurrency`     | `AnalyticsEventEarnVirtualCurrency`     |
| `FIRAnalyticsEventEcommercePurchase`       | `AnalyticsEventEcommercePurchase`       |
| `FIRAnalyticsEventGenerateLead`            | `AnalyticsEventGenerateLead`            |
| `FIRAnalyticsEventJoinGroup`               | `AnalyticsEventJoinGroup`               |
| `FIRAnalyticsEventLevelUp`                 | `AnalyticsEventLevelUp`                 |
| `FIRAnalyticsEventLogin`                   | `AnalyticsEventLogin`                   |
| `FIRAnalyticsEventPostScore`               | `AnalyticsEventPostScore`               |
| `FIRAnalyticsEventPresentOffer`            | `AnalyticsEventPresentOffer`            |
| `FIRAnalyticsEventPurchaseRefund`          | `AnalyticsEventPurchaseRefund`          |
| `FIRAnalyticsEventRemoveFromCart`          | `AnalyticsEventRemoveFromCart`          |
| `FIRAnalyticsEventSearch`                  | `AnalyticsEventSearch`                  |
| `FIRAnalyticsEventSelectContent`           | `AnalyticsEventSelectContent`           |
| `FIRAnalyticsEventSetCheckoutOption`       | `AnalyticsEventSetCheckoutOption`       |
| `FIRAnalyticsEventShare`                   | `AnalyticsEventShare`                   |
| `FIRAnalyticsEventSignUp`                  | `AnalyticsEventSignUp`                  |
| `FIRAnalyticsEventSpendVirtualCurrency`    | `AnalyticsEventSpendVirtualCurrency`    |
| `FIRAnalyticsEventTutorialBegin`           | `AnalyticsEventTutorialBegin`           |
| `FIRAnalyticsEventTutorialComplete`        | `AnalyticsEventTutorialComplete`        |
| `FIRAnalyticsEventUnlockAchievement`       | `AnalyticsEventUnlockAchievement`       |
| `FIRAnalyticsEventViewItem`                | `AnalyticsEventViewItem`                |
| `FIRAnalyticsEventViewItemList`            | `AnalyticsEventViewItemList`            |
| `FIRAnalyticsEventViewSearchResults`       | `AnalyticsEventViewSearchResults`       |
| `FIRAnalyticsParameterAchievementID`       | `AnalyticsParameterAchievementID`       |
| `FIRAnalyticsParameterAdNetworkClickID`    | `AnalyticsParameterAdNetworkClickID`    |
| `FIRAnalyticsParameterAffiliation`         | `AnalyticsParameterAffiliation`         |
| `FIRAnalyticsParameterCampaign`            | `AnalyticsParameterCampaign`            |
| `FIRAnalyticsParameterCharacter`           | `AnalyticsParameterCharacter`           |
| `FIRAnalyticsParameterCheckoutStep`        | `AnalyticsParameterCheckoutStep`        |
| `FIRAnalyticsParameterCheckoutOption`      | `AnalyticsParameterCheckoutOption`      |
| `FIRAnalyticsParameterContent`             | `AnalyticsParameterContent`             |
| `FIRAnalyticsParameterContentType`         | `AnalyticsParameterContentType`         |
| `FIRAnalyticsParameterCoupon`              | `AnalyticsParameterCoupon`              |
| `FIRAnalyticsParameterCreativeName`        | `AnalyticsParameterCreativeName`        |
| `FIRAnalyticsParameterCreativeSlot`        | `AnalyticsParameterCreativeSlot`        |
| `FIRAnalyticsParameterCurrency`            | `AnalyticsParameterCurrency`            |
| `FIRAnalyticsParameterDestination`         | `AnalyticsParameterDestination`         |
| `FIRAnalyticsParameterEndDate`             | `AnalyticsParameterEndDate`             |
| `FIRAnalyticsParameterFlightNumber`        | `AnalyticsParameterFlightNumber`        |
| `FIRAnalyticsParameterGroupID`             | `AnalyticsParameterGroupID`             |
| `FIRAnalyticsParameterIndex`               | `AnalyticsParameterIndex`               |
| `FIRAnalyticsParameterItemBrand`           | `AnalyticsParameterItemBrand`           |
| `FIRAnalyticsParameterItemCategory`        | `AnalyticsParameterItemCategory`        |
| `FIRAnalyticsParameterItemID`              | `AnalyticsParameterItemID`              |
| `FIRAnalyticsParameterItemLocationID`      | `AnalyticsParameterItemLocationID`      |
| `FIRAnalyticsParameterItemName`            | `AnalyticsParameterItemName`            |
| `FIRAnalyticsParameterItemList`            | `AnalyticsParameterItemList`            |
| `FIRAnalyticsParameterItemVariant`         | `AnalyticsParameterItemVariant`         |
| `FIRAnalyticsParameterLevel`               | `AnalyticsParameterLevel`               |
| `FIRAnalyticsParameterLocation`            | `AnalyticsParameterLocation`            |
| `FIRAnalyticsParameterMedium`              | `AnalyticsParameterMedium`              |
| `FIRAnalyticsParameterNumberOfNights`      | `AnalyticsParameterNumberOfNights`      |
| `FIRAnalyticsParameterNumberOfPassengers`  | `AnalyticsParameterNumberOfPassengers`  |
| `FIRAnalyticsParameterNumberOfRooms`       | `AnalyticsParameterNumberOfRooms`       |
| `FIRAnalyticsParameterOrigin`              | `AnalyticsParameterOrigin`              |
| `FIRAnalyticsParameterPrice`               | `AnalyticsParameterPrice`               |
| `FIRAnalyticsParameterQuantity`            | `AnalyticsParameterQuantity`            |
| `FIRAnalyticsParameterScore`               | `AnalyticsParameterScore`               |
| `FIRAnalyticsParameterSearchTerm`          | `AnalyticsParameterSearchTerm`          |
| `FIRAnalyticsParameterShipping`            | `AnalyticsParameterShipping`            |
| `FIRAnalyticsParameterSignUpMethod`        | `AnalyticsParameterSignUpMethod`        |
| `FIRAnalyticsParameterSource`              | `AnalyticsParameterSource`              |
| `FIRAnalyticsParameterStartDate`           | `AnalyticsParameterStartDate`           |
| `FIRAnalyticsParameterTax`                 | `AnalyticsParameterTax`                 |
| `FIRAnalyticsParameterTerm`                | `AnalyticsParameterTerm`                |
| `FIRAnalyticsParameterTransactionID`       | `AnalyticsParameterTransactionID`       |
| `FIRAnalyticsParameterTravelClass`         | `AnalyticsParameterTravelClass`         |
| `FIRAnalyticsParameterValue`               | `AnalyticsParameterValue`               |
| `FIRAnalyticsParameterVirtualCurrencyName` | `AnalyticsParameterVirtualCurrencyName` |
| `FIRAnalyticsUserPropertySignUpMethod`     | `AnalyticsUserPropertySignUpMethod`     |

#### Auth

|               Previous                |                New                 |
|---------------------------------------|------------------------------------|
| Functions                                                                 ||
| `FIRAuth.h`                                                               ||
| `init?(app:)`                         | `auth(app:)`                       |
| **Previous usage:** ```text let auth = FIRAuth(app: myApp) ``` **New usage:** ```text let auth = Auth.auth(app: myApp) ``` ||
| `FIRUser.h`                                                               ||
| `updateEmail(_:completion:)`          | `updateEmail(to:completion:)`      |
| **Previous usage:** ```transact-sql user.updateEmail("firebase_rox42@gmail.com") { error in // Check for error } ``` **New usage:** ```transact-sql user.updateEmail(to: "firebase_rox42@gmail.com") { error in // Check for error } ``` ||
| `updatePassword(_:completion:)`       | `updatePassword(to:completion:)`   |
| **Previous usage:** ```text user.updatePassword("hunter2") { error in // Check for error } ``` **New usage:** ```text user.updatePassword(to: "hunter2") { error in // Check for error } ``` ||
| `profileChangeRequest()`              | `createProfileChangeRequest()`     |
| **Previous usage:** ```text let request = user.profileChangeRequest() ``` **New usage:** ```text let request = user.createProfileChangeRequest() ``` ||
| `getTokenWithCompletion(_:)`          | `getToken(completion:)`            |
| **Previous usage:** ```text user.getTokenWithCompletion() { token, error in // Handle token or error here } ``` **New usage:** ```text user.getToken() { token, error in // Handle token or error here } ``` ||
| Classes                                                                   ||
| `FIRAdditionalUserInfo`               | `AdditionalUserInfo`               |
| `FIRActionCodeInfo`                   | `ActionCodeInfo`                   |
| `FIRAuth`                             | `Auth`                             |
| `FIRAuthCredential`                   | `AuthCredential`                   |
| `FIRAuthDataResult`                   | `AuthDataResult`                   |
| `FIRAuthErrors`                       | `AuthErrors`                       |
| `FIRSecureTokenService`               | `SecureTokenService`               |
| `FIRUser`                             | `User`                             |
| `FIRUserProfileChangeRequest`         | `UserProfileChangeRequest`         |
| `FIRUserInfo`                         | `UserInfo`                         |
| `FIREmailAuthProvider`                | `EmailAuthProvider`                |
| `FIRFacebookAuthProvider`             | `FacebookAuthProvider`             |
| `FIRGitHubAuthProvider`               | `GitHubAuthProvider`               |
| `FIRGoogleAuthProvider`               | `GoogleAuthProvider`               |
| `FIROAuthProvider`                    | `OAuthProvider`                    |
| `FIRTwitterAuthProvider`              | `TwitterAuthProvider`              |
| Constants                                                                 ||
| `FIRAuthErrorDomain`                  | `AuthErrorDomain`                  |
| `FIRAuthErrorNameKey`                 | `AuthErrorNameKey`                 |
| `FIREmailAuthProviderID`              | `EmailAuthProviderID`              |
| `FIRFacebookAuthProviderID`           | `FacebookAuthProviderID`           |
| `FIRGitHubAuthProviderID`             | `GitHubAuthProviderID`             |
| `FIRGoogleAuthProviderID`             | `GoogleAuthProviderID`             |
| `FIRTwitterAuthProviderID`            | `TwitterAuthProviderID`            |
| `FIRAuthStateDidChange`               | `AuthStateDidChange`               |
| Type Declarations                                                         ||
| `FIRAuthStateDidChangeListenerHandle` | `AuthStateDidChangeListenerHandle` |
| `FIRAuthStateDidChangeListenerBlock`  | `AuthStateDidChangeListenerBlock`  |
| `FIRAuthDataResultCallback`           | `AuthDataResultCallback`           |
| `FIRAuthResultCallback`               | `AuthResultCallback`               |
| `FIRProviderQueryCallback`            | `ProviderQueryCallback`            |
| `FIRSendPasswordResetCallback`        | `SendPasswordResetCallback`        |
| `FIRConfirmPasswordResetCallback`     | `ConfirmPasswordResetCallback`     |
| `FIRVerifyPasswordResetCodeCallback`  | `VerifyPasswordResetCodeCallback`  |
| `FIRApplyActionCodeCallback`          | `ApplyActionCodeCallback`          |
| `FIRVerificationResultCallback`       | `VerificationResultCallback`       |
| Enums                                                                     ||
| `FIRActionDataKey`                    | `ActionDataKey`                    |
| `FIRActionCodeOperation`              | `ActionCodeOperation`              |
| `FIRAuthErrorCode`                    | `AuthErrorCode`                    |

#### Core

|                   Previous                   |                  New                   |
|----------------------------------------------|----------------------------------------|
| Functions                                                                            ||
| `FIRAnalyticsConfiguration.sharedInstance()` | `AnalyticsConfiguration.shared()`      |
| `FIRApp.configure(withName:options:)`        | `FirebaseApp.configure(name:options:)` |
| **Previous usage:** ```text FIRApp.configure(withName: "myCustomApp", options: customOptions) ``` **New usage:** ```text FirebaseApp.configure(name: "myCustomApp", options: customOptions) ``` ||
| `FIRApp.defaultApp()`                        | `FirebaseApp.app()`                    |
| `FIRApp.init?(named:)`                       | `FirebaseApp.app(name:)`               |
| **Previous usage:** ```text let app = FIRApp(named: "myCustomApp") ``` **New usage:** ```text let app = FirebaseApp.app(name: "myCustomApp") ``` ||
| `FIRApp.allApps()`                           | `FirebaseApp.allApps`                  |
| **Previous usage:** ```text for app in FIRApp.allApps() { print("App name: \(app.name)") } ``` **New usage:** ```text for app in FirebaseApp.allApps { print("App name: \(app.name)") } ``` ||
| `FIRConfiguration.sharedInstance()`          | `FirebaseConfiguration.shared()`       |
| `FIROptions.default()`                       | `FirebaseOptions.defaultOptions()`     |
| Properties                                                                           ||
| FIROptions                                                                           ||
| `GCMSenderID`                                | `gcmSenderID`                          |
| Classes                                                                              ||
| `FIRAnalyticsConfiguration`                  | `AnalyticsConfiguration`               |
| `FIRApp`                                     | `FirebaseApp`                          |
| `FIRConfiguration`                           | `FirebaseConfiguration`                |
| `FIROptions`                                 | `FirebaseOptions`                      |
| Type Declarations                                                                    ||
| `FIRAppVoidBoolCallback`                     | `FirebaseAppVoidBoolCallback`          |
| Enums                                                                                ||
| `FIRLoggerLevel`                             | `FirebaseLoggerLevel`                  |

#### Crash

|       Previous        |            New             |
|-----------------------|----------------------------|
| Functions                                         ||
| `FIRCrashMessage(_:)` | `FirebaseCrashMessage(_:)` |

#### Database

|        Previous        |          New           |
|------------------------|------------------------|
| Properties                                     ||
| FIRDatabase.h                                  ||
| `persistenceEnabled`   | `isPersistenceEnabled` |
| Classes                                        ||
| `FIRDataSnapshot`      | `DataSnapshot`         |
| `FIRDatabase`          | `Database`             |
| `FIRDatabaseQuery`     | `DatabaseQuery`        |
| `FIRDatabaseReference` | `DatabaseReference`    |
| `FIRMutableData`       | `MutableData`          |
| `FIRServerValue`       | `ServerValue`          |
| `FIRTransactionResult` | `TransactionResult`    |
| Type Declarations                              ||
| `FIRDatabaseHandle`    | `DatabaseHandle`       |
| Enums                                          ||
| `FIRDataEventType`     | `DataEventType`        |

#### Dynamic Links

|                     Previous                     |                      New                      |
|--------------------------------------------------|-----------------------------------------------|
| Functions                                                                                       ||
| `// FIRDynamicLinks.h`                                                                          ||
| `dynamicLink(fromUniversalLinkURL:)`             | `dynamicLink(fromUniversalLink:)`             |
| Classes                                                                                         ||
| `FIRDynamicLink`                                 | `DynamicLink`                                 |
| `FIRDLRetrievalDelegate`                         | `DLRetrievalDelegate`                         |
| `FIRDynamicLinks`                                | `DynamicLinks`                                |
| `FIRDynamicLinkGoogleAnalyticsParameters`        | `DynamicLinkGoogleAnalyticsParameters`        |
| `FIRDynamicLinkIOSParameters`                    | `DynamicLinkIOSParameters`                    |
| `FIRDynamicLinkItunesConnectAnalyticsParameters` | `DynamicLinkItunesConnectAnalyticsParameters` |
| `FIRDynamicLinkAndroidParameters`                | `DynamicLinkAndroidParameters`                |
| `FIRDynamicLinkSocialMetaTagParameters`          | `DynamicLinkSocialMetaTagParameters`          |
| `FIRDynamicLinkNavigationInfoParameters`         | `DynamicLinkNavigationInfoParameters`         |
| `FIRDynamicLinkComponentsOptions`                | `DynamicLinkComponentsOptions`                |
| `FIRDynamicLinkComponents`                       | `DynamicLinkComponents`                       |
| Type Declarations                                                                               ||
| `FIRDynamicLinkResolverHandler`                  | `DynamicLinkResolverHandler`                  |
| `FIRDynamicLinkUniversalLinkHandler`             | `DynamicLinkUniversalLinkHandler`             |
| `FIRDynamicLinkShortenerCompletion`              | `DynamicLinkShortenerCompletion`              |
| Enums                                                                                           ||
| `FIRDynamicLinkMatchConfidence`                  | `DynamicLinkMatchConfidence`                  |
| `FIRDLRequiredMatchConfidence`                   | `DLRequiredMatchConfidence`                   |
| `FIRDLRetrieveResult`                            | `DLRetrieveResult`                            |
| `FIRShortDynamicLinkPathLength`                  | `ShortDynamicLinkPathLength`                  |

#### Instance ID

|               Previous                |                New                 |
|---------------------------------------|------------------------------------|
| Functions                                                                 ||
| `FIRInstanceID.h`                                                         ||
| `getWithHandler()`                    | `getIDWithHandler()`               |
| **Previous usage:** ```text FIRInstanceID.instanceID().get { identity, error in // Check identity and error } ``` **New usage:** ```text instanceID.instanceID().getID { identity, error in // Check identity and error } ``` ||
| `deleteWithHandler()`                 | `deleteIDWithHandler()`            |
| **Previous usage:** ```text FIRInstanceID.instanceID().delete { error in // Check error } ``` **New usage:** ```text instanceID.instanceID().deleteID { error in // Check error } ``` ||
| Classes                                                                   ||
| `FIRInstanceID`                       | `InstanceID`                       |
| Constants                                                                 ||
| `FIRInstanceIDScopeFirebaseMessaging` | `InstanceIDScopeFirebaseMessaging` |
| `FIRInstanceIDTokenRefresh`           | `InstanceIDTokenRefresh`           |
| Type Declarations                                                         ||
| `FIRInstanceIDTokenHandler`           | `InstanceIDTokenHandler`           |
| `FIRInstanceIDDeleteTokenHandler`     | `InstanceIDDeleteTokenHandler`     |
| `FIRInstanceIDHandler`                | `InstanceIDHandler`                |
| `FIRInstanceIDDeleteHandler`          | `InstanceIDDeleteHandler`          |
| Enums                                                                     ||
| `FIRInstanceIDError`                  | `InstanceIDError`                  |
| `FIRInstanceIDAPNSTokenType`          | `InstanceIDAPNSTokenType`          |

#### Invites

|           Previous            |            New             |
|-------------------------------|----------------------------|
| Classes                                                   ||
| `FIRInvites`                  | `Invites`                  |
| `FIRInvitesTargetApplication` | `InvitesTargetApplication` |
| `FIRReceivedInvite`           | `ReceivedInvite`           |
| Constants                                                 ||
| `FIRInvitesErrorDomain`       | `InvitesErrorDomain`       |
| Enums                                                     ||
| `FIRInvitesErrorCode`         | `InvitesErrorCode`         |
| `FIRReceivedInviteMatchType`  | `ReceivedInviteMatchType`  |
| Protocols                                                 ||
| `FIRInviteBuilder`            | `InviteBuilder`            |
| `FIRInviteDelegate`           | `InviteDelegate`           |

#### Messaging

|                 Previous                 |                  New                  |
|------------------------------------------|---------------------------------------|
| Functions                                                                       ||
| FIRMessaging                                                                    ||
| `connect(completion:)`                   | `connect(handler:)`                   |
| Classes                                                                         ||
| `FIRMessagingMessageInfo`                | `MessagingMessageInfo`                |
| `FIRMessagingRemoteMessage`              | `MessagingRemoteMessage`              |
| `FIRMessaging`                           | `Messaging`                           |
| Constants                                                                       ||
| `FIRMessagingSendSuccess`                | `MessagingSendSuccess`                |
| `FIRMessagingSendError`                  | `MessagingSendError`                  |
| `FIRMessagingMessagesDeleted`            | `MessagingMessagesDeleted`            |
| `FIRMessagingConnectionStateChanged`     | `MessagingConnectionStateChanged`     |
| `FIRMessagingRegistrationTokenRefreshed` | `MessagingRegistrationTokenRefreshed` |
| Type Declarations                                                               ||
| `FIRMessagingFCMTokenFetchCompletion`    | `MessagingFCMTokenFetchCompletion`    |
| `FIRMessagingDeleteFCMTokenCompletion`   | `MessagingDeleteFCMTokenCompletion`   |
| Enums                                                                           ||
| `FIRMessagingError`                      | `MessagingError`                      |
| `FIRMessagingMessageStatus`              | `MessagingMessageStatus`              |
| `FIRMessagingAPNSTokenType`              | `MessagingAPNSTokenType`              |
| Protocols                                                                       ||
| `FIRMessagingDelegate`                   | `MessagingDelegate`                   |

#### Remote Config

|                   Previous                    |                    New                     |
|-----------------------------------------------|--------------------------------------------|
| Functions                                                                                 ||
| FIRRemoteConfig                                                                           ||
| `setDefaultsFromPlistFileName(_:)`            | `setDefaults(fromPlist:)`                  |
| `setDefaultsFromPlistFileName(_:namespace)`   | `setDefaults(fromPlist:namespace)`         |
| Classes                                                                                   ||
| `FIRRemoteConfigValue`                        | `RemoteConfigValue`                        |
| `FIRRemoteConfigSettings`                     | `RemoteConfigSettings`                     |
| `FIRRemoteConfig`                             | `RemoteConfig`                             |
| Constants                                                                                 ||
| `FIRNamespaceGoogleMobilePlatform`            | `NamespaceGoogleMobilePlatform`            |
| `FIRRemoteConfigThrottledEndTimeInSecondsKey` | `RemoteConfigThrottledEndTimeInSecondsKey` |
| `FIRRemoteConfigErrorDomain`                  | `RemoteConfigErrorDomain`                  |
| Type Declarations                                                                         ||
| `FIRRemoteConfigFetchCompletion`              | `RemoteConfigFetchCompletion`              |
| Enums                                                                                     ||
| `FIRRemoteConfigFetchStatus`                  | `RemoteConfigFetchStatus`                  |
| `FIRRemoteConfigError`                        | `RemoteConfigError`                        |
| `FIRRemoteConfigSource`                       | `RemoteConfigSource`                       |

#### Storage

|             Previous              |                 New                  |
|-----------------------------------|--------------------------------------|
| Functions                                                               ||
| FIRStorageReference                                                     ||
| `put(_:)`                         | `putData(_:)`                        |
| `put(_:metadata:)`                | `putData(_:metadata:)`               |
| `put(_:metadata:completion:)`     | `putData(_:metadata:completion:)`    |
| `putFile(_:)`                     | `putFile(from:)`                     |
| `putFile(_:metadata:)`            | `putFile(from:metadata:)`            |
| `putFile(_:metadata:completion:)` | `putFile(from:metadata:completion:)` |
| `data(withMaxSize:completion:)`   | `getData(maxSize:completion:)`       |
| `metadata(completion:)`           | `getMetadata(completion:)`           |
| `update(_:completion:)`           | `updateMetadata(_:completion:)`      |
| Classes                                                                 ||
| `FIRStorage`                      | `Storage`                            |
| `FIRStorageDownloadTask`          | `StorageDownloadTask`                |
| `FIRStorageMetadata`              | `StorageMetadata`                    |
| `FIRStorageObservableTask`        | `StorageObservableTask`              |
| `FIRStorageReference`             | `StorageReference`                   |
| `FIRStorageTask`                  | `StorageTask`                        |
| `FIRStorageTaskSnapshot`          | `StorageTaskSnapshot`                |
| `FIRStorageUploadTask`            | `StorageUploadTask`                  |
| Constants                                                               ||
| `FIRStorageErrorDomain`           | `StorageErrorDomain`                 |
| Enums                                                                   ||
| `FIRStorageTaskStatus`            | `StorageTaskStatus`                  |
| `FIRStorageErrorCode`             | `StorageErrorCode`                   |
| Protocols                                                               ||
| `FIRStorageTaskManagement`        | `StorageTaskManagement`              |
| Type Declarations                                                       ||
| `FIRStorageHandle`                | `StorageHandle`                      |
| `FIRStorageVoidDataError`         | `StorageVoidDataError`               |
| `FIRStorageVoidError`             | `StorageVoidError`                   |
| `FIRStorageVoidMetadata`          | `StorageVoidMetadata`                |
| `FIRStorageVoidMetadataError`     | `StorageVoidMetadataError`           |
| `FIRStorageVoidSnapshot`          | `StorageVoidSnapshot`                |
| `FIRStorageVoidURLError`          | `StorageVoidURLError`                |
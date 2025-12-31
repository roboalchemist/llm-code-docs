# Source: https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Classes/FIRAnalytics.md.txt

# FIRAnalytics


    @interface FIRAnalytics : NSObject

The top level Firebase Analytics singleton that provides methods for logging events and setting user properties. See[the developer guides](http://goo.gl/gz8SLz)for general information on using Firebase Analytics in your apps.  
Note
The Analytics SDK uses SQLite to persist events and other app-specific data. Calling certain thread-unsafe global SQLite methods like`sqlite3_shutdown()`can result in unexpected crashes at runtime.
- `
  ``
  ``
  `

  ### [+logEventWithName:parameters:](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Classes/FIRAnalytics#/c:objc(cs)FIRAnalytics(cm)logEventWithName:parameters:)

  `
  `  
  Logs an app event. The event can have up to 25 parameters. Events with the same name must have the same parameters. Up to 500 event names are supported. Using predefined events and/or parameters is recommended for optimal reporting.

  The following event names are reserved - events with these names will be dropped, and instead an error event will be logged:
  - ad_activeview
  - ad_click
  - ad_exposure
  - ad_query
  - ad_reward
  - adunit_exposure
  - app_clear_data
  - app_exception
  - app_remove
  - app_store_refund
  - app_store_subscription_cancel
  - app_store_subscription_convert
  - app_store_subscription_renew
  - app_update
  - app_upgrade
  - dynamic_link_app_open
  - dynamic_link_app_update
  - dynamic_link_first_open
  - error
  - firebase_campaign
  - first_open
  - first_visit
  - notification_dismiss
  - notification_foreground
  - notification_open
  - notification_receive
  - os_update
  - session_start
  - session_start_with_rollout
  - user_engagement  

  #### Declaration

  Objective-C  

      + (void)logEventWithName:(nonnull NSString *)name
                    parameters:(nullable NSDictionary<NSString *, id> *)parameters;

  #### Parameters

  |--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*name*` `       | The name of the event. Should contain 1 to 40 alphanumeric characters or underscores. The name must start with an alphabetic character. Some event names are reserved. See FIREventNames.h for the list of reserved event names. The "firebase_", "google_", and "ga_" prefixes are reserved and should not be used. Note that event names are case-sensitive and that logging two events whose names differ only in case will result in two distinct events. To manually log screen view events, use the`screen_view`event name.                                                           |
  | ` `*parameters*` ` | The dictionary of event parameters. Passing`nil`indicates that the event has no parameters. Parameter names can be up to 40 characters long and must start with an alphabetic character and contain only alphanumeric characters and underscores. Only String, Int, and Double parameter types are supported. String parameter values can be up to 100 characters long for standard Google Analytics properties, and up to 500 characters long for Google Analytics 360 properties. The "firebase_", "google_", and "ga_" prefixes are reserved and should not be used for parameter names. |

- `
  ``
  ``
  `

  ### [+setUserPropertyString:forName:](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Classes/FIRAnalytics#/c:objc(cs)FIRAnalytics(cm)setUserPropertyString:forName:)

  `
  `  
  Sets a user property to a given value. Up to 25 user property names are supported. Once set, user property values persist throughout the app lifecycle and across sessions.

  The following user property names are reserved and cannot be used:
  - first_open_time
  - last_deep_link_referrer
  - user_id  

  #### Declaration

  Objective-C  

      + (void)setUserPropertyString:(nullable NSString *)value
                            forName:(nonnull NSString *)name;

  #### Parameters

  |---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*value*` ` | The value of the user property. Values can be up to 36 characters long. Setting the value to`nil`removes the user property.                                                                                                                                  |
  | ` `*name*` `  | The name of the user property to set. Should contain 1 to 24 alphanumeric characters or underscores and must start with an alphabetic character. The "firebase_", "google_", and "ga_" prefixes are reserved and should not be used for user property names. |

- `
  ``
  ``
  `

  ### [+setUserID:](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Classes/FIRAnalytics#/c:objc(cs)FIRAnalytics(cm)setUserID:)

  `
  `  
  Sets the user ID property. This feature must be used in accordance with[Google's Privacy Policy](https://www.google.com/policies/privacy)  

  #### Declaration

  Objective-C  

      + (void)setUserID:(nullable NSString *)userID;

  #### Parameters

  |----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*userID*` ` | The user ID to ascribe to the user of this app on this device, which must be non-empty and no more than 256 characters long. Setting userID to`nil`removes the user ID. |

- `
  ``
  ``
  `

  ### [+setAnalyticsCollectionEnabled:](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Classes/FIRAnalytics#/c:objc(cs)FIRAnalytics(cm)setAnalyticsCollectionEnabled:)

  `
  `  
  Sets whether analytics collection is enabled for this app on this device. This setting is persisted across app sessions. By default it is enabled.  

  #### Declaration

  Objective-C  

      + (void)setAnalyticsCollectionEnabled:(BOOL)analyticsCollectionEnabled;

  #### Parameters

  |------------------------------------|-------------------------------------------------------|
  | ` `*analyticsCollectionEnabled*` ` | A flag that enables or disables Analytics collection. |

- `
  ``
  ``
  `

  ### [+setSessionTimeoutInterval:](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Classes/FIRAnalytics#/c:objc(cs)FIRAnalytics(cm)setSessionTimeoutInterval:)

  `
  `  
  Sets the interval of inactivity in seconds that terminates the current session. The default value is 1800 seconds (30 minutes).  

  #### Declaration

  Objective-C  

      + (void)setSessionTimeoutInterval:(NSTimeInterval)sessionTimeoutInterval;

  #### Parameters

  |--------------------------------|---------------------------------------------------------------------------------|
  | ` `*sessionTimeoutInterval*` ` | The custom time of inactivity in seconds before the current session terminates. |

- `
  ``
  ``
  `

  ### [+sessionIDWithCompletion:](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Classes/FIRAnalytics#/c:objc(cs)FIRAnalytics(cm)sessionIDWithCompletion:)

  `
  `  
  Asynchronously retrieves the identifier of the current app session.

  The session ID retrieval could fail due to Analytics collection disabled, app session expired, etc.  

  #### Declaration

  Objective-C  

      + (void)sessionIDWithCompletion:
          (nonnull void (^)(int64_t, NSError *_Nullable))completion;

  #### Parameters

  |--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | The completion handler to call when the session ID retrieval is complete. This handler is executed on a system-defined global concurrent queue. This completion handler takes the following parameters:**sessionID** The identifier of the current app session. The value is undefined if the request failed.**error** An error object that indicates why the request failed, or`nil`if the request was successful. |

- `
  ``
  ``
  `

  ### [+appInstanceID](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Classes/FIRAnalytics#/c:objc(cs)FIRAnalytics(cm)appInstanceID)

  `
  `  
  Returns the unique ID for this instance of the application or`nil`if`ConsentType.analyticsStorage`has been set to`ConsentStatus.denied`.  
  See
  `FIRAnalytics+Consent.h`  

  #### Declaration

  Objective-C  

      + (nullable NSString *)appInstanceID;

- `
  ``
  ``
  `

  ### [+resetAnalyticsData](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Classes/FIRAnalytics#/c:objc(cs)FIRAnalytics(cm)resetAnalyticsData)

  `
  `  
  Clears all analytics data for this instance from the device and resets the app instance ID.  

  #### Declaration

  Objective-C  

      + (void)resetAnalyticsData;

- `
  ``
  ``
  `

  ### [+setDefaultEventParameters:](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Classes/FIRAnalytics#/c:objc(cs)FIRAnalytics(cm)setDefaultEventParameters:)

  `
  `  
  Adds parameters that will be set on every event logged from the SDK, including automatic ones. The values passed in the parameters dictionary will be added to the dictionary of default event parameters. These parameters persist across app runs. They are of lower precedence than event parameters, so if an event parameter and a parameter set using this API have the same name, the value of the event parameter will be used. The same limitations on event parameters apply to default event parameters.  

  #### Declaration

  Objective-C  

      + (void)setDefaultEventParameters:
          (nullable NSDictionary<NSString *, id> *)parameters;

  #### Parameters

  |--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*parameters*` ` | Parameters to be added to the dictionary of parameters added to every event. They will be added to the dictionary of default event parameters, replacing any existing parameter with the same name. Valid parameters are String, Int, and Double. Setting a key's value to`NSNull()`will clear that parameter. Passing in a`nil`dictionary will clear all parameters. |

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Classes/FIRAnalytics#/c:objc(cs)FIRAnalytics(im)init)

  `
  `  
  Unavailable  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

[## AppDelegate](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Classes/FIRAnalytics#/AppDelegate)

- `
  ``
  ``
  `

  ### [+handleEventsForBackgroundURLSession:completionHandler:](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Classes/FIRAnalytics#/c:objc(cs)FIRAnalytics(cm)handleEventsForBackgroundURLSession:completionHandler:)

  `
  `  
  Handles events related to a URL session that are waiting to be processed.
  1. If SwiftUI lifecycle is adopted, call this method from`UIApplicationDelegate.application(_:handleEventsForBackgroundURLSession:completionHandler:)`in your app delegate.

  2. If SwiftUI lifecycle is not adopted, Firebase Analytics does not require delegation implementation from the AppDelegate. If you choose instead to delegate manually, you can set FirebaseAppDelegateProxyEnabled to boolean`NO`in your app's Info.plist and call this method from`UIApplicationDelegate.application(_:handleEventsForBackgroundURLSession:completionHandler:)`in your app delegate.

  #### Declaration

  Objective-C  

      + (void)handleEventsForBackgroundURLSession:(nonnull NSString *)identifier
                                completionHandler:
                                    (nullable void (^)(void))completionHandler;

  #### Parameters

  |---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*identifier*` `        | The identifier of the URL session requiring attention.                                                                                                                                                |
  | ` `*completionHandler*` ` | The completion handler to call when you finish processing the events. Calling this completion handler lets the system know that your app's user interface is updated and a new snapshot can be taken. |

- `
  ``
  ``
  `

  ### [+handleOpenURL:](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Classes/FIRAnalytics#/c:objc(cs)FIRAnalytics(cm)handleOpenURL:)

  `
  `  
  Handles the event when the app is launched by a URL (custom URL scheme or universal link).
  1. If SwiftUI lifecycle is adopted, use`onOpenURL(perform:)`to register a handler and call this method in the handler.

  2. If UIScene lifecycle is adopted, call this method from`UISceneDelegate.scene(_:willConnectTo:options:)`and`UISceneDelegate.scene(_:openURLContexts:)`when the URL contexts are available.

  3. If neither SwiftUI nor UIScene lifecycle is adopted, Firebase Analytics does not require delegation implementation from the AppDelegate. If you choose instead to delegate manually, you can set FirebaseAppDelegateProxyEnabled to boolean`NO`in your app's Info.plist and call this method from`UIApplicationDelegate.application(_:open:options:)`in your app delegate.

  #### Declaration

  Objective-C  

      + (void)handleOpenURL:(nonnull NSURL *)url;

  #### Parameters

  |-------------|------------------------------------------------------------------------------|
  | ` `*url*` ` | The URL resource to open. This resource can be a network resource or a file. |

- `
  ``
  ``
  `

  ### [+handleUserActivity:](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Classes/FIRAnalytics#/c:objc(cs)FIRAnalytics(cm)handleUserActivity:)

  `
  `  
  Handles the event when the app receives data associated with user activity that includes a Universal Link.
  1. If SwiftUI lifecycle is adopted, use`onOpenURL(perform:)`to register a handler and call`Analytics.handleOpen(_:)`instead in the handler.

  2. If UIScene lifecycle is adopted, call this method from`UISceneDelegate.scene(_:willConnectTo:options:)`and`UISceneDelegate.scene(_:continue:)`when NSUserActivity is available. See the[Apple doc](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app)for more details.

  3. If neither SwiftUI nor UIScene lifecycle is adopted, Firebase Analytics does not require delegation implementation from the AppDelegate. If you choose instead to delegate manually, you can set FirebaseAppDelegateProxyEnabled to boolean`NO`in your app's Info.plist and call this method from`UIApplication.application(_:continue:restorationHandler:)`in your app delegate.

  #### Declaration

  Objective-C  

      + (void)handleUserActivity:(nonnull id)userActivity;

  #### Parameters

  |----------------------|-------------------------------------------------------------------------------------------|
  | ` `*userActivity*` ` | The activity object containing the data associated with the task the user was performing. |

[## Consent](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Classes/FIRAnalytics#/Consent)

- `
  ``
  ``
  `

  ### [+setConsent:](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Classes/FIRAnalytics#/c:objc(cs)FIRAnalytics(cm)setConsent:)

  `
  `  
  Sets the applicable end user consent state (e.g. for device identifiers) for this app on this device. Use the consent settings to specify individual consent type values. Settings are persisted across app sessions. By default consent types are set to`ConsentStatus.granted`.  

  #### Declaration

  Objective-C  

      + (void)setConsent:
          (nonnull NSDictionary<https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Type-Definitions.html#/c:FIRAnalytics+Consent.h@T@FIRConsentType, https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Type-Definitions.html#/c:FIRAnalytics+Consent.h@T@FIRConsentStatus> *)consentSettings;

  #### Parameters

  |-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*consentSettings*` ` | A Dictionary of consent types. Supported consent type keys are`ConsentType.adStorage`,`ConsentType.analyticsStorage`,`ConsentType.adUserData`, and`ConsentType.adPersonalization`. Valid values are`ConsentStatus.granted`and`ConsentStatus.denied`. |

[## OnDevice](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Classes/FIRAnalytics#/OnDevice)

- `
  ``
  ``
  `

  ### [+initiateOnDeviceConversionMeasurementWithEmailAddress:](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Classes/FIRAnalytics#/c:objc(cs)FIRAnalytics(cm)initiateOnDeviceConversionMeasurementWithEmailAddress:)

  `
  `  
  Initiates on-device conversion measurement given a user email address. Requires dependency GoogleAdsOnDeviceConversion from<https://github.com/googleads/google-ads-on-device-conversion-ios-sdk/>to be linked in, otherwise it is a no-op.  

  #### Declaration

  Objective-C  

      + (void)initiateOnDeviceConversionMeasurementWithEmailAddress:
          (nonnull NSString *)emailAddress;

  #### Parameters

  |----------------------|------------------------------------------------------------------------------------------------------|
  | ` `*emailAddress*` ` | User email address. Include a domain name for all email addresses (e.g. gmail.com or hotmail.co.jp). |

- `
  ``
  ``
  `

  ### [+initiateOnDeviceConversionMeasurementWithPhoneNumber:](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Classes/FIRAnalytics#/c:objc(cs)FIRAnalytics(cm)initiateOnDeviceConversionMeasurementWithPhoneNumber:)

  `
  `  
  Initiates on-device conversion measurement given a phone number in E.164 format. Requires dependency GoogleAdsOnDeviceConversion from<https://github.com/googleads/google-ads-on-device-conversion-ios-sdk/>to be linked in, otherwise it is a no-op.  

  #### Declaration

  Objective-C  

      + (void)initiateOnDeviceConversionMeasurementWithPhoneNumber:
          (nonnull NSString *)phoneNumber;

  #### Parameters

  |---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*phoneNumber*` ` | User phone number. Must be in E.164 format, which means it must be limited to a maximum of 15 digits and must include a plus sign (+) prefix and country code with no dashes, parentheses, or spaces. |

- `
  ``
  ``
  `

  ### [+initiateOnDeviceConversionMeasurementWithHashedEmailAddress:](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Classes/FIRAnalytics#/c:objc(cs)FIRAnalytics(cm)initiateOnDeviceConversionMeasurementWithHashedEmailAddress:)

  `
  `  
  Initiates on-device conversion measurement given a sha256-hashed user email address. Requires dependency GoogleAdsOnDeviceConversion from<https://github.com/googleads/google-ads-on-device-conversion-ios-sdk/>to be linked in, otherwise it is a no-op.  

  #### Declaration

  Objective-C  

      + (void)initiateOnDeviceConversionMeasurementWithHashedEmailAddress:
          (nonnull NSData *)hashedEmailAddress;

  #### Parameters

  |----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*hashedEmailAddress*` ` | User email address as a UTF8-encoded string normalized and hashed according to the instructions at<https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-3>. |

- `
  ``
  ``
  `

  ### [+initiateOnDeviceConversionMeasurementWithHashedPhoneNumber:](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Classes/FIRAnalytics#/c:objc(cs)FIRAnalytics(cm)initiateOnDeviceConversionMeasurementWithHashedPhoneNumber:)

  `
  `  
  Initiates on-device conversion measurement given a sha256-hashed phone number in E.164 format. Requires dependency GoogleAdsOnDeviceConversion from<https://github.com/googleads/google-ads-on-device-conversion-ios-sdk/>to be linked in, otherwise it is a no-op.  

  #### Declaration

  Objective-C  

      + (void)initiateOnDeviceConversionMeasurementWithHashedPhoneNumber:
          (nonnull NSData *)hashedPhoneNumber;

  #### Parameters

  |---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*hashedPhoneNumber*` ` | UTF8-encoded user phone number in E.164 format and then hashed according to the instructions at<https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-3>. |
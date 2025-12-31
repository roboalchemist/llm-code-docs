# Source: https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Classes/Analytics.md.txt

# Analytics

    class Analytics : NSObject

The top level Firebase Analytics singleton that provides methods for logging events and setting user properties. See[the developer guides](http://goo.gl/gz8SLz)for general information on using Firebase Analytics in your apps.  
Note
The Analytics SDK uses SQLite to persist events and other app-specific data. Calling certain thread-unsafe global SQLite methods like`sqlite3_shutdown()`can result in unexpected crashes at runtime.
- `
  ``
  ``
  `

  ### [logEvent(_:parameters:)](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Classes/Analytics#/c:objc(cs)FIRAnalytics(cm)logEventWithName:parameters:)

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

  Swift  

      class func logEvent(_ name: String, parameters: [String : Any]?)

  #### Parameters

  |--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*name*` `       | The name of the event. Should contain 1 to 40 alphanumeric characters or underscores. The name must start with an alphabetic character. Some event names are reserved. See FIREventNames.h for the list of reserved event names. The "firebase_", "google_", and "ga_" prefixes are reserved and should not be used. Note that event names are case-sensitive and that logging two events whose names differ only in case will result in two distinct events. To manually log screen view events, use the`screen_view`event name.                                                           |
  | ` `*parameters*` ` | The dictionary of event parameters. Passing`nil`indicates that the event has no parameters. Parameter names can be up to 40 characters long and must start with an alphabetic character and contain only alphanumeric characters and underscores. Only String, Int, and Double parameter types are supported. String parameter values can be up to 100 characters long for standard Google Analytics properties, and up to 500 characters long for Google Analytics 360 properties. The "firebase_", "google_", and "ga_" prefixes are reserved and should not be used for parameter names. |

- `
  ``
  ``
  `

  ### [setUserProperty(_:forName:)](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Classes/Analytics#/c:objc(cs)FIRAnalytics(cm)setUserPropertyString:forName:)

  `
  `  
  Sets a user property to a given value. Up to 25 user property names are supported. Once set, user property values persist throughout the app lifecycle and across sessions.

  The following user property names are reserved and cannot be used:
  - first_open_time
  - last_deep_link_referrer
  - user_id  

  #### Declaration

  Swift  

      class func setUserProperty(_ value: String?, forName name: String)

  #### Parameters

  |---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*value*` ` | The value of the user property. Values can be up to 36 characters long. Setting the value to`nil`removes the user property.                                                                                                                                  |
  | ` `*name*` `  | The name of the user property to set. Should contain 1 to 24 alphanumeric characters or underscores and must start with an alphabetic character. The "firebase_", "google_", and "ga_" prefixes are reserved and should not be used for user property names. |

- `
  ``
  ``
  `

  ### [setUserID(_:)](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Classes/Analytics#/c:objc(cs)FIRAnalytics(cm)setUserID:)

  `
  `  
  Sets the user ID property. This feature must be used in accordance with[Google's Privacy Policy](https://www.google.com/policies/privacy)  

  #### Declaration

  Swift  

      class func setUserID(_ userID: String?)

  #### Parameters

  |----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*userID*` ` | The user ID to ascribe to the user of this app on this device, which must be non-empty and no more than 256 characters long. Setting userID to`nil`removes the user ID. |

- `
  ``
  ``
  `

  ### [setAnalyticsCollectionEnabled(_:)](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Classes/Analytics#/c:objc(cs)FIRAnalytics(cm)setAnalyticsCollectionEnabled:)

  `
  `  
  Sets whether analytics collection is enabled for this app on this device. This setting is persisted across app sessions. By default it is enabled.  

  #### Declaration

  Swift  

      class func setAnalyticsCollectionEnabled(_ analyticsCollectionEnabled: Bool)

  #### Parameters

  |------------------------------------|-------------------------------------------------------|
  | ` `*analyticsCollectionEnabled*` ` | A flag that enables or disables Analytics collection. |

- `
  ``
  ``
  `

  ### [setSessionTimeoutInterval(_:)](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Classes/Analytics#/c:objc(cs)FIRAnalytics(cm)setSessionTimeoutInterval:)

  `
  `  
  Sets the interval of inactivity in seconds that terminates the current session. The default value is 1800 seconds (30 minutes).  

  #### Declaration

  Swift  

      class func setSessionTimeoutInterval(_ sessionTimeoutInterval: TimeInterval)

  #### Parameters

  |--------------------------------|---------------------------------------------------------------------------------|
  | ` `*sessionTimeoutInterval*` ` | The custom time of inactivity in seconds before the current session terminates. |

- `
  ``
  ``
  `

  ### [sessionID()](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Classes/Analytics#/c:objc(cs)FIRAnalytics(cm)sessionIDWithCompletion:)

  `
  `  
  Asynchronously retrieves the identifier of the current app session.

  The session ID retrieval could fail due to Analytics collection disabled, app session expired, etc.  

  #### Declaration

  Swift  

      class func sessionID() async throws -> Int64

  #### Parameters

  |--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | The completion handler to call when the session ID retrieval is complete. This handler is executed on a system-defined global concurrent queue. This completion handler takes the following parameters:**sessionID** The identifier of the current app session. The value is undefined if the request failed.**error** An error object that indicates why the request failed, or`nil`if the request was successful. |

- `
  ``
  ``
  `

  ### [appInstanceID()](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Classes/Analytics#/c:objc(cs)FIRAnalytics(cm)appInstanceID)

  `
  `  
  Returns the unique ID for this instance of the application or`nil`if`ConsentType.analyticsStorage`has been set to`ConsentStatus.denied`.  
  See
  `FIRAnalytics+Consent.h`  

  #### Declaration

  Swift  

      class func appInstanceID() -> String?

- `
  ``
  ``
  `

  ### [resetAnalyticsData()](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Classes/Analytics#/c:objc(cs)FIRAnalytics(cm)resetAnalyticsData)

  `
  `  
  Clears all analytics data for this instance from the device and resets the app instance ID.  

  #### Declaration

  Swift  

      class func resetAnalyticsData()

- `
  ``
  ``
  `

  ### [setDefaultEventParameters(_:)](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Classes/Analytics#/c:objc(cs)FIRAnalytics(cm)setDefaultEventParameters:)

  `
  `  
  Adds parameters that will be set on every event logged from the SDK, including automatic ones. The values passed in the parameters dictionary will be added to the dictionary of default event parameters. These parameters persist across app runs. They are of lower precedence than event parameters, so if an event parameter and a parameter set using this API have the same name, the value of the event parameter will be used. The same limitations on event parameters apply to default event parameters.  

  #### Declaration

  Swift  

      class func setDefaultEventParameters(_ parameters: [String : Any]?)

  #### Parameters

  |--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*parameters*` ` | Parameters to be added to the dictionary of parameters added to every event. They will be added to the dictionary of default event parameters, replacing any existing parameter with the same name. Valid parameters are String, Int, and Double. Setting a key's value to`NSNull()`will clear that parameter. Passing in a`nil`dictionary will clear all parameters. |

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Classes/Analytics#/c:objc(cs)FIRAnalytics(im)init)

  `
  `  
  Unavailable  
  Unavailable.
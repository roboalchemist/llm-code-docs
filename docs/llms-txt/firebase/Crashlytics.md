# Source: https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/Crashlytics.md.txt

# FirebaseCrashlytics Framework Reference

# Crashlytics

    class Crashlytics : NSObject

The Firebase Crashlytics API provides methods to annotate and manage fatal and
non-fatal reports captured and reported to Firebase Crashlytics.

By default, Firebase Crashlytics is initialized with `FirebaseApp.configure()`.

Note: The Crashlytics class cannot be subclassed. If this makes testing difficult,
we suggest using a wrapper class or a protocol extension.
- `
  ``
  ``
  `

  ### [crashlytics()](https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/Crashlytics#/c:objc(cs)FIRCrashlytics(cm)crashlytics)

  `
  `  
  Accesses the singleton Crashlytics instance.  

  #### Declaration

  Swift  

      class func crashlytics() -> Self

  #### Return Value

  The singleton Crashlytics instance.
- `
  ``
  ``
  `

  ### [log(_:)](https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/Crashlytics#/c:objc(cs)FIRCrashlytics(im)log:)

  `
  `  
  Adds logging that is sent with your crash data. The logging does not appear in app
  logs and is only visible in the Crashlytics dashboard.  

  #### Declaration

  Swift  

      func log(_ msg: String)

  #### Parameters

  |-------------|----------------|
  | ` `*msg*` ` | Message to log |

- `
  ``
  ``
  `

  ### [-logWithFormat:](https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/Crashlytics#/c:objc(cs)FIRCrashlytics(im)logWithFormat:)

  `
  `  
  Adds logging that is sent with your crash data. The logging does not appear in app
  logs and is only visible in the Crashlytics dashboard.  

  #### Parameters

  |----------------|----------------------------------------------------------------------------------------------------------|
  | ` `*format*` ` | The format of the string, followed by a comma-separated list of arguments to substitute into the format. |

- `
  ``
  ``
  `

  ### [log(format:arguments:)](https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/Crashlytics#/c:objc(cs)FIRCrashlytics(im)logWithFormat:arguments:)

  `
  `  
  Adds logging that is sent with your crash data. The logging does not appear in app
  logs and is only visible in the Crashlytics dashboard.  

  #### Declaration

  Swift  

      func log(format: String, arguments args: CVaListPointer)

  #### Parameters

  |----------------|-------------------------------------|
  | ` `*format*` ` | Format of string                    |
  | ` `*args*` `   | Arguments to substitute into format |

- `
  ``
  ``
  `

  ### [setCustomValue(_:forKey:)](https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/Crashlytics#/c:objc(cs)FIRCrashlytics(im)setCustomValue:forKey:)

  `
  `  
  Sets a custom key and value to be associated with subsequent fatal and non-fatal reports.
  When setting an object value, the object is converted to a string. This is
  typically done by using the object's `description`.  

  #### Declaration

  Swift  

      func setCustomValue(_ value: Any?, forKey key: String)

  #### Parameters

  |---------------|-----------------------------------------|
  | ` `*value*` ` | The value to be associated with the key |
  | ` `*key*` `   | A unique key                            |

- `
  ``
  ``
  `

  ### [setCustomKeysAndValues(_:)](https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/Crashlytics#/c:objc(cs)FIRCrashlytics(im)setCustomKeysAndValues:)

  `
  `  
  Sets custom keys and values to be associated with subsequent fatal and non-fatal reports.
  The objects in the dictionary are converted to strings. This is
  typically done by using the object's `description`.  

  #### Declaration

  Swift  

      func setCustomKeysAndValues(_ keysAndValues: [AnyHashable : Any])

  #### Parameters

  |-----------------------|---------------------------------------------------------|
  | ` `*keysAndValues*` ` | The values to be associated with the corresponding keys |

- `
  ``
  ``
  `

  ### [setUserID(_:)](https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/Crashlytics#/c:objc(cs)FIRCrashlytics(im)setUserID:)

  `
  `  
  Records a user ID (identifier) that's associated with subsequent fatal and non-fatal reports.

  If you want to associate a crash with a specific user, we recommend specifying an arbitrary
  string (e.g., a database, ID, hash, or other value that you can index and query, but is
  meaningless to a third-party observer). This allows you to facilitate responses for support
  requests and reach out to users for more information.  

  #### Declaration

  Swift  

      func setUserID(_ userID: String?)

  #### Parameters

  |----------------|----------------------------------------------------------------------------------------|
  | ` `*userID*` ` | An arbitrary user identifier string that associates a user to a record in your system. |

- `
  ``
  ``
  `

  ### [record(error:)](https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/Crashlytics#/c:objc(cs)FIRCrashlytics(im)recordError:)

  `
  `  
  Records a non-fatal event described by an Error object. The events are
  grouped and displayed similarly to crashes. Keep in mind that this method can be expensive.
  The total number of Errors that can be recorded during your app's life-cycle is limited by a
  fixed-size circular buffer. If the buffer is overrun, the oldest data is dropped. Errors are
  relayed to Crashlytics on a subsequent launch of your application.  

  #### Declaration

  Swift  

      func record(error: any Error)

  #### Parameters

  |---------------|--------------------------------|
  | ` `*error*` ` | Non-fatal error to be recorded |

- `
  ``
  ``
  `

  ### [record(error:userInfo:)](https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/Crashlytics#/c:objc(cs)FIRCrashlytics(im)recordError:userInfo:)

  `
  `  
  Records a non-fatal event described by an NSError object. The events are
  grouped and displayed similarly to crashes. Keep in mind that this method can be expensive.
  The total number of NSErrors that can be recorded during your app's life-cycle is limited by a
  fixed-size circular buffer. If the buffer is overrun, the oldest data is dropped. Errors are
  relayed to Crashlytics on a subsequent launch of your application.  

  #### Declaration

  Swift  

      func record(error: any Error, userInfo: [String : Any]? = nil)

  #### Parameters

  |------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*error*` `    | Non-fatal error to be recorded                                                                                                                                         |
  | ` `*userInfo*` ` | Additional keys and values to send with the logged error. These keys and values are added to the error, in addition to the Crashlytics global list of keys and values. |

- `
  ``
  ``
  `

  ### [record(exceptionModel:)](https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/Crashlytics#/c:objc(cs)FIRCrashlytics(im)recordExceptionModel:)

  `
  `  
  Records an Exception Model described by an ExceptionModel object. The events are
  grouped and displayed similarly to crashes. Keep in mind that this method can be expensive.
  The total number of ExceptionModels that can be recorded during your app's life-cycle is
  limited by a fixed-size circular buffer. If the buffer is overrun, the oldest data is dropped.
  ExceptionModels are relayed to Crashlytics on a subsequent launch of your application.  

  #### Declaration

  Swift  

      func record(exceptionModel: https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/ExceptionModel.html)

  #### Parameters

  |------------------------|-----------------------------------------------|
  | ` `*exceptionModel*` ` | Instance of the ExceptionModel to be recorded |

- `
  ``
  ``
  `

  ### [didCrashDuringPreviousExecution()](https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/Crashlytics#/c:objc(cs)FIRCrashlytics(im)didCrashDuringPreviousExecution)

  `
  `  
  Returns whether the app crashed during the previous execution.  

  #### Declaration

  Swift  

      func didCrashDuringPreviousExecution() -> Bool

- `
  ``
  ``
  `

  ### [setCrashlyticsCollectionEnabled(_:)](https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/Crashlytics#/c:objc(cs)FIRCrashlytics(im)setCrashlyticsCollectionEnabled:)

  `
  `  
  Enables/disables automatic data collection.

  Calling this method overrides both the FirebaseCrashlyticsCollectionEnabled flag in your
  App's Info.plist and FirebaseApp's isDataCollectionDefaultEnabled flag.

  When you set a value for this method, it persists across runs of the app.

  The value does not apply until the next run of the app. If you want to disable data
  collection without rebooting, add the FirebaseCrashlyticsCollectionEnabled flag to your app's
  Info.plist.
  \*  

  #### Declaration

  Swift  

      func setCrashlyticsCollectionEnabled(_ enabled: Bool)

  #### Parameters

  |-----------------|---------------------------------------------------------|
  | ` `*enabled*` ` | Determines whether automatic data collection is enabled |

- `
  ``
  ``
  `

  ### [isCrashlyticsCollectionEnabled()](https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/Crashlytics#/c:objc(cs)FIRCrashlytics(im)isCrashlyticsCollectionEnabled)

  `
  `  
  Indicates whether or not automatic data collection is enabled

  This method uses three ways to decide whether automatic data collection is enabled,
  in order of priority:
  - If setCrashlyticsCollectionEnabled is called with a value, use it
  - If the FirebaseCrashlyticsCollectionEnabled key is in your app's Info.plist, use it
  - Otherwise, use the default isDataCollectionDefaultEnabled in FirebaseApp  

  #### Declaration

  Swift  

      func isCrashlyticsCollectionEnabled() -> Bool

- `
  ``
  ``
  `

  ### [checkForUnsentReports()](https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/Crashlytics#/c:objc(cs)FIRCrashlytics(im)checkForUnsentReportsWithCompletion:)

  `
  `  
  Determines whether there are any unsent crash reports cached on the device, then calls the given
  callback.

  The callback only executes if automatic data collection is disabled. You can use
  the callback to get one-time consent from a user upon a crash, and then call
  sendUnsentReports or deleteUnsentReports, depending on whether or not the user gives consent.

  Disable automatic collection by:
  - Adding the `FirebaseCrashlyticsCollectionEnabled` key with the value set to NO to your app's Info.plist
  - Calling `FirebaseCrashlytics.crashlytics().setCrashlyticsCollectionEnabled(false)` in your app
  - Setting `FirebaseApp`'s `isDataCollectionDefaultEnabled` to false

  #### Declaration

  Swift  

      func checkForUnsentReports() async -> Bool

  #### Parameters

  |--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | The callback that's executed once Crashlytics finishes checking for unsent reports. The callback is set to true if there are unsent reports on disk. |

- `
  ``
  ``
  `

  ### [checkAndUpdateUnsentReports()](https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/Crashlytics#/c:objc(cs)FIRCrashlytics(im)checkAndUpdateUnsentReportsWithCompletion:)

  `
  `  
  Determines whether there are any unsent crash reports cached on the device, then calls the given
  callback with a CrashlyticsReport object that you can use to update the unsent report.
  CrashlyticsReports have a lot of the familiar Crashlytics methods like setting custom keys and
  logs.

  The callback only executes if automatic data collection is disabled. You can use
  the callback to get one-time consent from a user upon a crash, and then call
  sendUnsentReports or deleteUnsentReports, depending on whether or not the user gives consent.

  Disable automatic collection by:
  - Adding the `FirebaseCrashlyticsCollectionEnabled` key with the value set to NO to your app's Info.plist
  - Calling `FirebaseCrashlytics.crashlytics().setCrashlyticsCollectionEnabled(false)` in your app
  - Setting `FirebaseApp`'s `isDataCollectionDefaultEnabled` to false

  Not calling `sendUnsentReports()`/`deleteUnsentReports()` will result in the report staying on
  disk, which means the same CrashlyticsReport can show up in multiple runs of the app. If you
  want avoid duplicates, ensure there was a crash on the last run of the app by checking the value
  of `didCrashDuringPreviousExecution`.  

  #### Declaration

  Swift  

      func checkAndUpdateUnsentReports() async -> https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/CrashlyticsReport.html?

  #### Parameters

  |--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | The callback that's executed once Crashlytics finishes checking for unsent reports. The callback is called with the newest unsent Crashlytics Report, or nil if there are none cached on disk. |

- `
  ``
  ``
  `

  ### [sendUnsentReports()](https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/Crashlytics#/c:objc(cs)FIRCrashlytics(im)sendUnsentReports)

  `
  `  
  Enqueues any unsent reports on the device to upload to Crashlytics.

  This method only applies if automatic data collection is disabled.

  When automatic data collection is enabled, Crashlytics automatically uploads and deletes reports
  at startup, so this method is ignored.  

  #### Declaration

  Swift  

      func sendUnsentReports()

- `
  ``
  ``
  `

  ### [deleteUnsentReports()](https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/Crashlytics#/c:objc(cs)FIRCrashlytics(im)deleteUnsentReports)

  `
  `  
  Deletes any unsent reports on the device.

  This method only applies if automatic data collection is disabled.  

  #### Declaration

  Swift  

      func deleteUnsentReports()
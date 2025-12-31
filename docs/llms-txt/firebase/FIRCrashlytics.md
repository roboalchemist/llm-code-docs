# Source: https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlytics.md.txt

# FirebaseCrashlytics Framework Reference

# FIRCrashlytics


    @interface FIRCrashlytics : NSObject

The Firebase Crashlytics API provides methods to annotate and manage fatal and
non-fatal reports captured and reported to Firebase Crashlytics.

By default, Firebase Crashlytics is initialized with `FirebaseApp.configure()`.

Note: The Crashlytics class cannot be subclassed. If this makes testing difficult,
we suggest using a wrapper class or a protocol extension.
- `
  ``
  ``
  `

  ### [+crashlytics](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlytics#/c:objc(cs)FIRCrashlytics(cm)crashlytics)

  `
  `  
  Accesses the singleton Crashlytics instance.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)crashlytics;

  #### Return Value

  The singleton Crashlytics instance.
- `
  ``
  ``
  `

  ### [-log:](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlytics#/c:objc(cs)FIRCrashlytics(im)log:)

  `
  `  
  Adds logging that is sent with your crash data. The logging does not appear in app
  logs and is only visible in the Crashlytics dashboard.  

  #### Declaration

  Objective-C  

      - (void)log:(nonnull NSString *)msg;

  #### Parameters

  |-------------|----------------|
  | ` `*msg*` ` | Message to log |

- `
  ``
  ``
  `

  ### [-logWithFormat:](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlytics#/c:objc(cs)FIRCrashlytics(im)logWithFormat:)

  `
  `  
  Adds logging that is sent with your crash data. The logging does not appear in app
  logs and is only visible in the Crashlytics dashboard.  

  #### Declaration

  Objective-C  

      - (void)logWithFormat:(nonnull NSString *)format, ...;

  #### Parameters

  |----------------|----------------------------------------------------------------------------------------------------------|
  | ` `*format*` ` | The format of the string, followed by a comma-separated list of arguments to substitute into the format. |

- `
  ``
  ``
  `

  ### [-logWithFormat:arguments:](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlytics#/c:objc(cs)FIRCrashlytics(im)logWithFormat:arguments:)

  `
  `  
  Adds logging that is sent with your crash data. The logging does not appear in app
  logs and is only visible in the Crashlytics dashboard.  

  #### Declaration

  Objective-C  

      - (void)logWithFormat:(nonnull NSString *)format arguments:(va_list)args;

  #### Parameters

  |----------------|-------------------------------------|
  | ` `*format*` ` | Format of string                    |
  | ` `*args*` `   | Arguments to substitute into format |

- `
  ``
  ``
  `

  ### [-setCustomValue:forKey:](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlytics#/c:objc(cs)FIRCrashlytics(im)setCustomValue:forKey:)

  `
  `  
  Sets a custom key and value to be associated with subsequent fatal and non-fatal reports.
  When setting an object value, the object is converted to a string. This is
  typically done by using the object's `description`.  

  #### Declaration

  Objective-C  

      - (void)setCustomValue:(nullable id)value forKey:(nonnull NSString *)key;

  #### Parameters

  |---------------|-----------------------------------------|
  | ` `*value*` ` | The value to be associated with the key |
  | ` `*key*` `   | A unique key                            |

- `
  ``
  ``
  `

  ### [-setCustomKeysAndValues:](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlytics#/c:objc(cs)FIRCrashlytics(im)setCustomKeysAndValues:)

  `
  `  
  Sets custom keys and values to be associated with subsequent fatal and non-fatal reports.
  The objects in the dictionary are converted to strings. This is
  typically done by using the object's `description`.  

  #### Declaration

  Objective-C  

      - (void)setCustomKeysAndValues:(nonnull NSDictionary *)keysAndValues;

  #### Parameters

  |-----------------------|---------------------------------------------------------|
  | ` `*keysAndValues*` ` | The values to be associated with the corresponding keys |

- `
  ``
  ``
  `

  ### [-setUserID:](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlytics#/c:objc(cs)FIRCrashlytics(im)setUserID:)

  `
  `  
  Records a user ID (identifier) that's associated with subsequent fatal and non-fatal reports.

  If you want to associate a crash with a specific user, we recommend specifying an arbitrary
  string (e.g., a database, ID, hash, or other value that you can index and query, but is
  meaningless to a third-party observer). This allows you to facilitate responses for support
  requests and reach out to users for more information.  

  #### Declaration

  Objective-C  

      - (void)setUserID:(nullable NSString *)userID;

  #### Parameters

  |----------------|----------------------------------------------------------------------------------------|
  | ` `*userID*` ` | An arbitrary user identifier string that associates a user to a record in your system. |

- `
  ``
  ``
  `

  ### [-recordError:](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlytics#/c:objc(cs)FIRCrashlytics(im)recordError:)

  `
  `  
  Records a non-fatal event described by an Error object. The events are
  grouped and displayed similarly to crashes. Keep in mind that this method can be expensive.
  The total number of Errors that can be recorded during your app's life-cycle is limited by a
  fixed-size circular buffer. If the buffer is overrun, the oldest data is dropped. Errors are
  relayed to Crashlytics on a subsequent launch of your application.  

  #### Declaration

  Objective-C  

      - (void)recordError:(nonnull NSError *)error;

  #### Parameters

  |---------------|--------------------------------|
  | ` `*error*` ` | Non-fatal error to be recorded |

- `
  ``
  ``
  `

  ### [-recordError:userInfo:](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlytics#/c:objc(cs)FIRCrashlytics(im)recordError:userInfo:)

  `
  `  
  Records a non-fatal event described by an NSError object. The events are
  grouped and displayed similarly to crashes. Keep in mind that this method can be expensive.
  The total number of NSErrors that can be recorded during your app's life-cycle is limited by a
  fixed-size circular buffer. If the buffer is overrun, the oldest data is dropped. Errors are
  relayed to Crashlytics on a subsequent launch of your application.  

  #### Declaration

  Objective-C  

      - (void)recordError:(nonnull NSError *)error
                 userInfo:(nullable NSDictionary<NSString *, id> *)userInfo;

  #### Parameters

  |------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*error*` `    | Non-fatal error to be recorded                                                                                                                                         |
  | ` `*userInfo*` ` | Additional keys and values to send with the logged error. These keys and values are added to the error, in addition to the Crashlytics global list of keys and values. |

- `
  ``
  ``
  `

  ### [-recordExceptionModel:](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlytics#/c:objc(cs)FIRCrashlytics(im)recordExceptionModel:)

  `
  `  
  Records an Exception Model described by an ExceptionModel object. The events are
  grouped and displayed similarly to crashes. Keep in mind that this method can be expensive.
  The total number of ExceptionModels that can be recorded during your app's life-cycle is
  limited by a fixed-size circular buffer. If the buffer is overrun, the oldest data is dropped.
  ExceptionModels are relayed to Crashlytics on a subsequent launch of your application.  

  #### Declaration

  Objective-C  

      - (void)recordExceptionModel:(nonnull https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRExceptionModel.html *)exceptionModel;

  #### Parameters

  |------------------------|-----------------------------------------------|
  | ` `*exceptionModel*` ` | Instance of the ExceptionModel to be recorded |

- `
  ``
  ``
  `

  ### [-didCrashDuringPreviousExecution](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlytics#/c:objc(cs)FIRCrashlytics(im)didCrashDuringPreviousExecution)

  `
  `  
  Returns whether the app crashed during the previous execution.  

  #### Declaration

  Objective-C  

      - (BOOL)didCrashDuringPreviousExecution;

- `
  ``
  ``
  `

  ### [-setCrashlyticsCollectionEnabled:](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlytics#/c:objc(cs)FIRCrashlytics(im)setCrashlyticsCollectionEnabled:)

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

  Objective-C  

      - (void)setCrashlyticsCollectionEnabled:(BOOL)enabled;

  #### Parameters

  |-----------------|---------------------------------------------------------|
  | ` `*enabled*` ` | Determines whether automatic data collection is enabled |

- `
  ``
  ``
  `

  ### [-isCrashlyticsCollectionEnabled](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlytics#/c:objc(cs)FIRCrashlytics(im)isCrashlyticsCollectionEnabled)

  `
  `  
  Indicates whether or not automatic data collection is enabled

  This method uses three ways to decide whether automatic data collection is enabled,
  in order of priority:
  - If setCrashlyticsCollectionEnabled is called with a value, use it
  - If the FirebaseCrashlyticsCollectionEnabled key is in your app's Info.plist, use it
  - Otherwise, use the default isDataCollectionDefaultEnabled in FirebaseApp  

  #### Declaration

  Objective-C  

      - (BOOL)isCrashlyticsCollectionEnabled;

- `
  ``
  ``
  `

  ### [-checkForUnsentReportsWithCompletion:](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlytics#/c:objc(cs)FIRCrashlytics(im)checkForUnsentReportsWithCompletion:)

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

  Objective-C  

      - (void)checkForUnsentReportsWithCompletion:(nonnull void (^)(BOOL))completion;

  #### Parameters

  |--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | The callback that's executed once Crashlytics finishes checking for unsent reports. The callback is set to true if there are unsent reports on disk. |

- `
  ``
  ``
  `

  ### [-checkAndUpdateUnsentReportsWithCompletion:](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlytics#/c:objc(cs)FIRCrashlytics(im)checkAndUpdateUnsentReportsWithCompletion:)

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

  Objective-C  

      - (void)checkAndUpdateUnsentReportsWithCompletion:
          (nonnull void (^)(https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlyticsReport.html *_Nullable))completion;

  #### Parameters

  |--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | The callback that's executed once Crashlytics finishes checking for unsent reports. The callback is called with the newest unsent Crashlytics Report, or nil if there are none cached on disk. |

- `
  ``
  ``
  `

  ### [-sendUnsentReports](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlytics#/c:objc(cs)FIRCrashlytics(im)sendUnsentReports)

  `
  `  
  Enqueues any unsent reports on the device to upload to Crashlytics.

  This method only applies if automatic data collection is disabled.

  When automatic data collection is enabled, Crashlytics automatically uploads and deletes reports
  at startup, so this method is ignored.  

  #### Declaration

  Objective-C  

      - (void)sendUnsentReports;

- `
  ``
  ``
  `

  ### [-deleteUnsentReports](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlytics#/c:objc(cs)FIRCrashlytics(im)deleteUnsentReports)

  `
  `  
  Deletes any unsent reports on the device.

  This method only applies if automatic data collection is disabled.  

  #### Declaration

  Objective-C  

      - (void)deleteUnsentReports;
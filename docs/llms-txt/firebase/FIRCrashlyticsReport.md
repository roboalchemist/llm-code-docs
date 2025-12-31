# Source: https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlyticsReport.md.txt

# FirebaseCrashlytics Framework Reference

# FIRCrashlyticsReport


    @interface FIRCrashlyticsReport : NSObject

The Firebase Crashlytics Report provides a way to read and write information
to a past Crashlytics reports. A common use case is gathering end-user feedback
on the next run of the app.

The CrashlyticsReport should be modified before calling send/deleteUnsentReports.
- `
  ``
  ``
  `

  ### [reportID](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlyticsReport#/c:objc(cs)FIRCrashlyticsReport(py)reportID)

  `
  `  
  Returns the unique ID for the Crashlytics report.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSString *_Nonnull reportID;

- `
  ``
  ``
  `

  ### [dateCreated](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlyticsReport#/c:objc(cs)FIRCrashlyticsReport(py)dateCreated)

  `
  `  
  Returns the date that the report was created.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSDate *_Nonnull dateCreated;

- `
  ``
  ``
  `

  ### [hasCrash](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlyticsReport#/c:objc(cs)FIRCrashlyticsReport(py)hasCrash)

  `
  `  
  Returns true when one of the events in the Crashlytics report is a crash.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) BOOL hasCrash;

- `
  ``
  ``
  `

  ### [-log:](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlyticsReport#/c:objc(cs)FIRCrashlyticsReport(im)log:)

  `
  `  
  Adds logging that is sent with your crash data. The logging does not appear in the
  system.log and is only visible in the Crashlytics dashboard.  

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

  ### [-logWithFormat:](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlyticsReport#/c:objc(cs)FIRCrashlyticsReport(im)logWithFormat:)

  `
  `  
  Adds logging that is sent with your crash data. The logging does not appear in the
  system.log and is only visible in the Crashlytics dashboard.  

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

  ### [-logWithFormat:arguments:](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlyticsReport#/c:objc(cs)FIRCrashlyticsReport(im)logWithFormat:arguments:)

  `
  `  
  Adds logging that is sent with your crash data. The logging does not appear in the
  system.log and is only visible in the Crashlytics dashboard.  

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

  ### [-setCustomValue:forKey:](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlyticsReport#/c:objc(cs)FIRCrashlyticsReport(im)setCustomValue:forKey:)

  `
  `  
  Sets a custom key and value to be associated with subsequent fatal and non-fatal reports.
  When setting an object value, the object is converted to a string. This is
  typically done by using the object's description.  

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

  ### [-setCustomKeysAndValues:](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlyticsReport#/c:objc(cs)FIRCrashlyticsReport(im)setCustomKeysAndValues:)

  `
  `  
  Sets custom keys and values to be associated with subsequent fatal and non-fatal reports.
  The objects in the dictionary are converted to strings. This is
  typically done by using the object's description.  

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

  ### [-setUserID:](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlyticsReport#/c:objc(cs)FIRCrashlyticsReport(im)setUserID:)

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
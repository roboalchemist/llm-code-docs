# Source: https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes.md.txt

# FirebaseCrashlytics Framework Reference

# Classes

The following classes are available globally.
- `


  ### [FIRCrashlytics](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlytics)


  ` The Firebase Crashlytics API provides methods to annotate and manage fatal and
  non-fatal reports captured and reported to Firebase Crashlytics.

  By default, Firebase Crashlytics is initialized with `FirebaseApp.configure()`.

  Note: The Crashlytics class cannot be subclassed. If this makes testing difficult,
  we suggest using a wrapper class or a protocol extension.

  #### Declaration

  Objective-C


      @interface FIRCrashlytics : NSObject

- `


  ### [FIRCrashlyticsReport](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRCrashlyticsReport)


  ` The Firebase Crashlytics Report provides a way to read and write information
  to a past Crashlytics reports. A common use case is gathering end-user feedback
  on the next run of the app.

  The CrashlyticsReport should be modified before calling send/deleteUnsentReports.

  #### Declaration

  Objective-C


      @interface FIRCrashlyticsReport : NSObject

- `


  ### [FIRExceptionModel](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRExceptionModel)


  ` The Firebase Crashlytics ExceptionModel provides a way to report custom exceptions
  to Crashlytics that came from a runtime environment outside of the native
  platform Crashlytics is running in.

  #### Declaration

  Objective-C


      @interface FIRExceptionModel : NSObject

- `


  ### [FIRStackFrame](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRStackFrame)


  ` The Firebase Crashlytics `StackFrame` provides a way to construct the lines of
  a stack trace for reporting along with a recorded `ExceptionModel`.

  #### Declaration

  Objective-C


      @interface FIRStackFrame : NSObject
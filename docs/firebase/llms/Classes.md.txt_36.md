# Source: https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes.md.txt

# FirebaseCrashlytics Framework Reference

# Classes

The following classes are available globally.
- `


  ### [Crashlytics](https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/Crashlytics)


  ` The Firebase Crashlytics API provides methods to annotate and manage fatal and
  non-fatal reports captured and reported to Firebase Crashlytics.

  By default, Firebase Crashlytics is initialized with `FirebaseApp.configure()`.

  Note: The Crashlytics class cannot be subclassed. If this makes testing difficult,
  we suggest using a wrapper class or a protocol extension.

  #### Declaration

  Swift

      class Crashlytics : NSObject

- `


  ### [CrashlyticsReport](https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/CrashlyticsReport)


  ` The Firebase Crashlytics Report provides a way to read and write information
  to a past Crashlytics reports. A common use case is gathering end-user feedback
  on the next run of the app.

  The CrashlyticsReport should be modified before calling send/deleteUnsentReports.

  #### Declaration

  Swift

      class CrashlyticsReport : NSObject

- `


  ### [ExceptionModel](https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/ExceptionModel)


  ` The Firebase Crashlytics ExceptionModel provides a way to report custom exceptions
  to Crashlytics that came from a runtime environment outside of the native
  platform Crashlytics is running in.

  #### Declaration

  Swift

      class ExceptionModel : NSObject

- `


  ### [StackFrame](https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/StackFrame)


  ` The Firebase Crashlytics `StackFrame` provides a way to construct the lines of
  a stack trace for reporting along with a recorded `https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/ExceptionModel`.

  #### Declaration

  Swift

      class StackFrame : NSObject
# Source: https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Classes.md.txt

# FirebaseAnalytics Framework Reference

# Classes

The following classes are available globally.
- `


  ### [Analytics](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Classes/Analytics)


  ` The top level Firebase Analytics singleton that provides methods for logging events and setting
  user properties. See [the developer guides](http://goo.gl/gz8SLz) for general
  information on using Firebase Analytics in your apps.
  Note
  The Analytics SDK uses SQLite to persist events and other app-specific data. Calling certain thread-unsafe global SQLite methods like `sqlite3_shutdown()` can result in unexpected crashes at runtime.

  #### Declaration

  Swift

      class Analytics : NSObject
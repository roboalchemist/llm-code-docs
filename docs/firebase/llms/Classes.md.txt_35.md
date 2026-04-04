# Source: https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes.md.txt

# FirebaseCore Framework Reference

# Classes

The following classes are available globally.
- `


  ### [FirebaseApp](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp)


  ` The entry point of Firebase SDKs.

  Initialize and configure `FirebaseApp` using `https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp#/c:objc(cs)FIRApp(cm)configure`
  or other customized ways as shown below.

  The logging system has two modes: default mode and debug mode. In default mode, only logs with
  log level Notice, Warning and Error will be sent to device. In debug mode, all logs will be sent
  to device. The log levels that Firebase uses are consistent with the ASL log levels.

  Enable debug mode by passing the `-FIRDebugEnabled` argument to the application. You can add this
  argument in the application's Xcode scheme. When debug mode is enabled via `-FIRDebugEnabled`,
  further executions of the application will also be in debug mode. In order to return to default
  mode, you must explicitly disable the debug mode with the application argument
  `-FIRDebugDisabled`.

  It is also possible to change the default logging level in code by calling
  `FirebaseConfiguration.shared.setLoggerLevel(_:)` with the desired level.

  #### Declaration

  Swift

      class FirebaseApp : NSObject

- `


  ### [FirebaseConfiguration](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseConfiguration)


  ` This interface provides global level properties that the developer can tweak.

  #### Declaration

  Swift

      class FirebaseConfiguration : NSObject

- `


  ### [FirebaseOptions](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseOptions)


  ` This class provides constant fields of Google APIs.

  #### Declaration

  Swift

      class FirebaseOptions : NSObject, NSCopying

- `


  ### [Timestamp](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/Timestamp)


  ` A Timestamp represents a point in time independent of any time zone or calendar, represented as
  seconds and fractions of seconds at nanosecond resolution in UTC Epoch time. It is encoded using
  the Proleptic Gregorian Calendar which extends the Gregorian calendar backwards to year one. It
  is encoded assuming all minutes are 60 seconds long, i.e. leap seconds are "smeared" so that no
  leap second table is needed for interpretation. Range is from 0001-01-01T00:00:00Z to
  9999-12-31T23:59:59.999999999Z. By restricting to that range, we ensure that we can convert to
  and from RFC 3339 date strings.
  See
  <https://github.com/google/protobuf/blob/main/src/google/protobuf/timestamp.proto> for the reference timestamp definition.

  #### Declaration

  Swift

      class Timestamp : NSObject, NSCopying, @unchecked Sendable
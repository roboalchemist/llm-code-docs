# Source: https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes.md.txt

# FirebasePerformance Framework Reference

# Classes

The following classes are available globally.
- `


  ### [FIRHTTPMetric](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRHTTPMetric)


  ` Instances of `HTTPMetric` can be used to record HTTP network request information.

  #### Declaration

  Objective-C


      @interface FIRHTTPMetric : NSObject <https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Protocols/FIRPerformanceAttributable>

- `


  ### [FIRPerformance](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRPerformance)


  ` This class allows you to configure the Firebase Performance Reporting SDK. It also provides the
  interfaces to create timers and enable or disable automatic metrics capture.

  This SDK uses a Firebase Installations ID to identify the app instance and periodically sends
  data to the Firebase backend (see `Installations.installationID(completion:)`).
  To stop this periodic sync, call `Installations.delete(completion:)` and
  either disable this SDK or set Performance.dataCollectionEnabled to false.

  #### Declaration

  Objective-C


      @interface FIRPerformance : NSObject

- `


  ### [FIRTrace](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRTrace)


  ` FIRTrace objects contain information about a "Trace", which is a sequence of steps. Traces can be
  used to measure the time taken for a sequence of steps.
  Traces also include "Counters". Counters are used to track information which is cumulative in
  nature (e.g., Bytes downloaded). Counters are scoped to an FIRTrace object.

  #### Declaration

  Objective-C


      @interface FIRTrace : NSObject <https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Protocols/FIRPerformanceAttributable>
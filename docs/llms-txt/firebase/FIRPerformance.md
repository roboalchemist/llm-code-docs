# Source: https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRPerformance.md.txt

# FirebasePerformance Framework Reference

# FIRPerformance


    @interface FIRPerformance : NSObject

This class allows you to configure the Firebase Performance Reporting SDK. It also provides the
interfaces to create timers and enable or disable automatic metrics capture.

This SDK uses a Firebase Installations ID to identify the app instance and periodically sends
data to the Firebase backend (see `Installations.installationID(completion:)`).
To stop this periodic sync, call `Installations.delete(completion:)` and
either disable this SDK or set Performance.dataCollectionEnabled to false.
- `
  ``
  ``
  `

  ### [dataCollectionEnabled](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRPerformance#/c:objc(cs)FIRPerformance(py)dataCollectionEnabled)

  `
  `  
  Controls the capture of performance data. When this value is set to NO, none of the performance
  data will sent to the server. Default is true.

  This setting is persisted, and is applied on future invocations of your application. Once
  explicitly set, it overrides any settings in your Info.plist.  

  #### Declaration

  Objective-C  

      @property (nonatomic, assign, unsafe_unretained, readwrite,
                getter=isDataCollectionEnabled) BOOL dataCollectionEnabled;

- `
  ``
  ``
  `

  ### [instrumentationEnabled](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRPerformance#/c:objc(cs)FIRPerformance(py)instrumentationEnabled)

  `
  `  
  Controls the instrumentation of the app to capture performance data. Setting this value to false
  has immediate effect only if it is done so before calling FirebaseApp.configure(). Otherwise it
  takes effect on the next app start.

  If set to false, the app will not be instrumented to collect performance
  data (in scenarios like `app_start`, networking monitoring). Default is true.

  This setting is persisted, and is applied on future invocations of your application. Once
  explicitly set, it overrides any settings in your `Info.plist`.  

  #### Declaration

  Objective-C  

      @property (nonatomic, assign, unsafe_unretained, readwrite,
                getter=isInstrumentationEnabled) BOOL instrumentationEnabled;

- `
  ``
  ``
  `

  ### [+sharedInstance](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRPerformance#/c:objc(cs)FIRPerformance(cm)sharedInstance)

  `
  `  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)sharedInstance;

  #### Return Value

  The shared instance.
- `
  ``
  ``
  `

  ### [+startTraceWithName:](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRPerformance#/c:objc(cs)FIRPerformance(cm)startTraceWithName:)

  `
  `  
  Creates an instance of Trace after creating the shared instance of Performance. The trace
  will automatically be started on a successful creation of the instance. The `name` of the trace
  cannot be an empty string.  

  #### Declaration

  Objective-C  

      + (nullable https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRTrace.html *)startTraceWithName:(nonnull NSString *)name;

  #### Parameters

  |--------------|------------------------|
  | ` `*name*` ` | The name of the trace. |

  #### Return Value

  The Trace object.
- `
  ``
  ``
  `

  ### [-traceWithName:](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRPerformance#/c:objc(cs)FIRPerformance(im)traceWithName:)

  `
  `  
  Creates an instance of Trace. This API does not start the trace. To start the trace, use the
  `start()` method on the returned Trace object. The `name` cannot be an empty string.  

  #### Declaration

  Objective-C  

      - (nullable https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRTrace.html *)traceWithName:(nonnull NSString *)name;

  #### Parameters

  |--------------|------------------------|
  | ` `*name*` ` | The name of the Trace. |

  #### Return Value

  The FIRTrace object.
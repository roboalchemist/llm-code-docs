# Source: https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp.md.txt

# FirebaseCore Framework Reference

# FirebaseApp

    class FirebaseApp : NSObject

The entry point of Firebase SDKs.

Initialize and configure `FirebaseApp` using `https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp.html#/c:objc(cs)FIRApp(cm)configure`
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
- `


  ### [configure()](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp#/c:objc(cs)FIRApp(cm)configure)


  ` Configures a default Firebase app. Raises an exception if any configuration step fails. The
  default app is named "__FIRAPP_DEFAULT". This method should be called after the app is launched
  and before using Firebase services. This method should be called from the main thread and
  contains synchronous file I/O (reading GoogleService-Info.plist from disk).

  #### Declaration

  Swift

      class func configure()

- `


  ### [configure(options:)](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp#/c:objc(cs)FIRApp(cm)configureWithOptions:)


  ` Configures the default Firebase app with the provided options. The default app is named
  "__FIRAPP_DEFAULT". Raises an exception if any configuration step fails. This method should be
  called from the main thread.

  #### Declaration

  Swift

      class func configure(options: FIROptions)

  #### Parameters

  |---|---|
  | ` options ` | The Firebase application options used to configure the service. |

- `


  ### [configure(name:options:)](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp#/c:objc(cs)FIRApp(cm)configureWithName:options:)


  ` Configures a Firebase app with the given name and options. Raises an exception if any
  configuration step fails. This method should be called from the main thread.

  #### Declaration

  Swift

      class func configure(name: String, options: FIROptions)

  #### Parameters

  |---|---|
  | ` name ` | The application's name given by the developer. The name should should only contain Letters, Numbers and Underscore. |
  | ` options ` | The Firebase application options used to configure the services. |

- `


  ### [app()](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp#/c:objc(cs)FIRApp(cm)defaultApp)


  ` Returns the default app, or `nil` if the default app does not exist.

  #### Declaration

  Swift

      class func app() -> FirebaseApp?

- `


  ### [app(name:)](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp#/c:objc(cs)FIRApp(cm)appNamed:)


  ` Returns a previously created `FirebaseApp` instance with the given name, or `nil` if no such app
  exists. This method is thread safe.

  #### Declaration

  Swift

      class func app(name: String) -> FirebaseApp?

- `


  ### [allApps](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp#/c:objc(cs)FIRApp(cpy)allApps)


  ` Returns the set of all extant `FirebaseApp` instances, or `nil` if there are no `FirebaseApp`
  instances. This method is thread safe.

  #### Declaration

  Swift

      class var allApps: [String : FirebaseApp]? { get }

- `


  ### [delete()](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp#/c:objc(cs)FIRApp(im)deleteApp:)


  ` Cleans up the current `FirebaseApp`, freeing associated data and returning its name to the pool
  for future use. This method is thread safe.

  #### Declaration

  Swift

      func delete() async -> Bool

- `


  ### [-init](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp#/c:objc(cs)FIRApp(im)init)


  ` Unavailable
  `FirebaseApp` instances should not be initialized directly. Call `https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp.html#/c:objc(cs)FIRApp(cm)configure`,
  `https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp.html#/c:objc(cs)FIRApp(cm)configureWithOptions:`, or `https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp.html#/c:objc(cs)FIRApp(cm)configureWithName:options:` directly.
- `


  ### [name](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp#/c:objc(cs)FIRApp(py)name)


  ` Gets the name of this app.

  #### Declaration

  Swift

      var name: String { get }

- `


  ### [options](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp#/c:objc(cs)FIRApp(py)options)


  ` Gets a copy of the options for this app. These are non-modifiable.

  #### Declaration

  Swift

      @NSCopying var options: FIROptions { get }

- `


  ### [isDataCollectionDefaultEnabled](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp#/c:objc(cs)FIRApp(py)dataCollectionDefaultEnabled)


  ` Gets or sets whether automatic data collection is enabled for all products. Defaults to `true`
  unless `FirebaseDataCollectionDefaultEnabled` is set to `NO` in your app's Info.plist. This value
  is persisted across runs of the app so that it can be set once when users have consented to
  collection.

  #### Declaration

  Swift

      var isDataCollectionDefaultEnabled: Bool { get set }
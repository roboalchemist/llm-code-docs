# Source: https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseConfiguration.md.txt

# FirebaseCore Framework Reference

# FirebaseConfiguration

    class FirebaseConfiguration : NSObject

This interface provides global level properties that the developer can tweak.
- `
  ``
  ``
  `

  ### [shared](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseConfiguration#/c:objc(cs)FIRConfiguration(cpy)sharedInstance)

  `
  `  
  Returns the shared configuration object.  

  #### Declaration

  Swift  

      class var shared: FirebaseConfiguration { get }

- `
  ``
  ``
  `

  ### [setLoggerLevel(_:)](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseConfiguration#/c:objc(cs)FIRConfiguration(im)setLoggerLevel:)

  `
  `  
  Sets the logging level for internal Firebase logging. Firebase will only log messages
  that are logged at or below `loggerLevel`. The messages are logged both to the Xcode
  console and to the device's log. Note that if an app is running from AppStore, it will
  never log above `.notice` even if `loggerLevel` is set to a higher (more verbose)
  setting.  

  #### Declaration

  Swift  

      func setLoggerLevel(_ loggerLevel: FirebaseLoggerLevel)

  #### Parameters

  |---------------------|------------------------------------------------------------------------------|
  | ` `*loggerLevel*` ` | The maximum logging level. The default level is set to FIRLoggerLevelNotice. |

- `
  ``
  ``
  `

  ### [loggerLevel()](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseConfiguration#/c:objc(cs)FIRConfiguration(im)loggerLevel)

  `
  `  
  Returns the logging level for internal Firebase logging.  

  #### Declaration

  Swift  

      func loggerLevel() -> FirebaseLoggerLevel
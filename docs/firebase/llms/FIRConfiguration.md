# Source: https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Classes/FIRConfiguration.md.txt

# FIRConfiguration


    @interface FIRConfiguration : NSObject

This interface provides global level properties that the developer can tweak.
- `
  ``
  ``
  `

  ### [sharedInstance](https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Classes/FIRConfiguration#/c:objc(cs)FIRConfiguration(cpy)sharedInstance)

  `
  `  
  Returns the shared configuration object.  

  #### Declaration

  Objective-C  

      @property (class, nonatomic, readonly) NS_SWIFT_NAME FIRConfiguration *sharedInstance;

- `
  ``
  ``
  `

  ### [-setLoggerLevel:](https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Classes/FIRConfiguration#/c:objc(cs)FIRConfiguration(im)setLoggerLevel:)

  `
  `  
  Sets the logging level for internal Firebase logging. Firebase will only log messages that are logged at or below`loggerLevel`. The messages are logged both to the Xcode console and to the device's log. Note that if an app is running from AppStore, it will never log above`.notice`even if`loggerLevel`is set to a higher (more verbose) setting.  

  #### Declaration

  Objective-C  

      - (void)setLoggerLevel:(https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Enums/FIRLoggerLevel.html)loggerLevel;

  #### Parameters

  |---------------------|------------------------------------------------------------------------------|
  | ` `*loggerLevel*` ` | The maximum logging level. The default level is set to FIRLoggerLevelNotice. |

- `
  ``
  ``
  `

  ### [-loggerLevel](https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Classes/FIRConfiguration#/c:objc(cs)FIRConfiguration(im)loggerLevel)

  `
  `  
  Returns the logging level for internal Firebase logging.  

  #### Declaration

  Objective-C  

      - (https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Enums/FIRLoggerLevel.html)loggerLevel;
# Source: https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRExceptionModel.md.txt

# FirebaseCrashlytics Framework Reference

# FIRExceptionModel


    @interface FIRExceptionModel : NSObject

The Firebase Crashlytics ExceptionModel provides a way to report custom exceptions
to Crashlytics that came from a runtime environment outside of the native
platform Crashlytics is running in.
- `
  ``
  ``
  `

  ### [-initWithName:reason:](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRExceptionModel#/c:objc(cs)FIRExceptionModel(im)initWithName:reason:)

  `
  `  
  Initializes an ExceptionModel with the given required fields.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)initWithName:(nonnull NSString *)name
                                    reason:(nonnull NSString *)reason;

  #### Parameters

  |----------------|------------------------------------------------|
  | ` `*name*` `   | - typically the type of the Exception class    |
  | ` `*reason*` ` | - the human-readable reason the issue occurred |

- `
  ``
  ``
  `

  ### [+exceptionModelWithName:reason:](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRExceptionModel#/c:objc(cs)FIRExceptionModel(cm)exceptionModelWithName:reason:)

  `
  `  
  Creates an ExceptionModel with the given required fields.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)exceptionModelWithName:(nonnull NSString *)name
                                              reason:(nonnull NSString *)reason;

  #### Parameters

  |----------------|------------------------------------------------|
  | ` `*name*` `   | - typically the type of the Exception class    |
  | ` `*reason*` ` | - the human-readable reason the issue occurred |

- `
  ``
  ``
  `

  ### [stackTrace](https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRExceptionModel#/c:objc(cs)FIRExceptionModel(py)stackTrace)

  `
  `  
  A list of stack frames that make up the stack trace. The order of the stack trace is top-first,
  so typically the "main" function is the last element in this list.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy) NSArray<https://firebase.google.com/docs/reference/ios/firebasecrashlytics/api/reference/Classes/FIRStackFrame.html *> *_Nonnull stackTrace;
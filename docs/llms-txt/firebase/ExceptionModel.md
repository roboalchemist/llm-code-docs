# Source: https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/ExceptionModel.md.txt

# FirebaseCrashlytics Framework Reference

# ExceptionModel

    class ExceptionModel : NSObject

The Firebase Crashlytics ExceptionModel provides a way to report custom exceptions
to Crashlytics that came from a runtime environment outside of the native
platform Crashlytics is running in.
- `
  ``
  ``
  `

  ### [init(name:reason:)](https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/ExceptionModel#/c:objc(cs)FIRExceptionModel(im)initWithName:reason:)

  `
  `  
  Initializes an ExceptionModel with the given required fields.  

  #### Declaration

  Swift  

      init(name: String, reason: String)

  #### Parameters

  |----------------|------------------------------------------------|
  | ` `*name*` `   | - typically the type of the Exception class    |
  | ` `*reason*` ` | - the human-readable reason the issue occurred |

- `
  ``
  ``
  `

  ### [+exceptionModelWithName:reason:](https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/ExceptionModel#/c:objc(cs)FIRExceptionModel(cm)exceptionModelWithName:reason:)

  `
  `  
  Creates an ExceptionModel with the given required fields.  

  #### Parameters

  |----------------|------------------------------------------------|
  | ` `*name*` `   | - typically the type of the Exception class    |
  | ` `*reason*` ` | - the human-readable reason the issue occurred |

- `
  ``
  ``
  `

  ### [stackTrace](https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/ExceptionModel#/c:objc(cs)FIRExceptionModel(py)stackTrace)

  `
  `  
  A list of stack frames that make up the stack trace. The order of the stack trace is top-first,
  so typically the "main" function is the last element in this list.  

  #### Declaration

  Swift  

      var stackTrace: [https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/StackFrame.html] { get set }
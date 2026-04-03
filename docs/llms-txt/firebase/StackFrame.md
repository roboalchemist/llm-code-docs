# Source: https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/StackFrame.md.txt

# FirebaseCrashlytics Framework Reference

# StackFrame

    class StackFrame : NSObject

The Firebase Crashlytics `StackFrame` provides a way to construct the lines of
a stack trace for reporting along with a recorded [ExceptionModel](https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/ExceptionModel.html).
- `
  ``
  ``
  `

  ### [init(symbol:file:line:)](https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/StackFrame#/c:objc(cs)FIRStackFrame(im)initWithSymbol:file:line:)

  `
  `  
  Initializes a symbolicated `StackFrame` with the given required fields. Symbolicated
  `StackFrame`s will appear in the Crashlytics dashboard as reported in these fields.  

  #### Declaration

  Swift  

      init(symbol: String, file: String, line: Int)

  #### Parameters

  |----------------|-----------------------------------------|
  | ` `*symbol*` ` | - The function or method name           |
  | ` `*file*` `   | - the file where the exception occurred |
  | ` `*line*` `   | - the line number                       |

- `
  ``
  ``
  `

  ### [init(address:)](https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/StackFrame#/c:objc(cs)FIRStackFrame(cm)stackFrameWithAddress:)

  `
  `  
  Creates a symbolicated `StackFrame` from an address. The address will be
  symbolicated in the Crashlytics backend for the customer and reported in the
  Crashlytics dashboard with the appropriate file name and line number. If an
  invalid address is provided it will appear in the dashboard as missing.  

  #### Declaration

  Swift  

      convenience init(address: UInt)

  #### Parameters

  |-----------------|--------------------------------------------|
  | ` `*address*` ` | - the address where the exception occurred |

- `
  ``
  ``
  `

  ### [+stackFrameWithSymbol:file:line:](https://firebase.google.com/docs/reference/swift/firebasecrashlytics/api/reference/Classes/StackFrame#/c:objc(cs)FIRStackFrame(cm)stackFrameWithSymbol:file:line:)

  `
  `  
  Creates a symbolicated `StackFrame` with the given required fields. Symbolicated
  `StackFrame`s will appear in the Crashlytics dashboard as reported in these fields.  

  #### Parameters

  |----------------|-----------------------------------------|
  | ` `*symbol*` ` | - The function or method name           |
  | ` `*file*` `   | - the file where the exception occurred |
  | ` `*line*` `   | - the line number                       |
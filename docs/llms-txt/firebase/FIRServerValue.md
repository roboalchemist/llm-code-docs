# Source: https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRServerValue.md.txt

# FirebaseDatabase Framework Reference

# FIRServerValue


    @interface FIRServerValue : NSObject

Placeholder values you may write into Firebase Database as a value or
priority that will automatically be populated by the Firebase Database
server.
- `
  ``
  ``
  `

  ### [+timestamp](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRServerValue#/c:objc(cs)FIRServerValue(cm)timestamp)

  `
  `  
  Placeholder value for the number of milliseconds since the Unix epoch  

  #### Declaration

  Objective-C  

      + (nonnull NSDictionary *)timestamp;

- `
  ``
  ``
  `

  ### [+increment:](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRServerValue#/c:objc(cs)FIRServerValue(cm)increment:)

  `
  `  
  Returns a placeholder value that can be used to atomically increment the
  current database value by the provided delta.

  The delta must be a long or double value. If the current value is not an
  integer or double, or if the data does not yet exist, the transformation will
  set the data to the delta value. If either of the delta value or the existing
  data are doubles, both values will be interpreted as doubles. Double
  arithmetic and representation of double values follow IEEE 754 semantics. If
  there is positive/negative integer overflow, the sum is calculated as a
  double.  

  #### Declaration

  Objective-C  

      + (nonnull NSDictionary *)increment:(nonnull NSNumber *)delta;

  #### Parameters

  |---------------|----------------------------------------------------|
  | ` `*delta*` ` | the amount to modify the current value atomically. |

  #### Return Value

  a placeholder value for modifying data atomically server-side.
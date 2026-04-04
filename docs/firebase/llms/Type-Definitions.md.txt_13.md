# Source: https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Type-Definitions.md.txt

# FirebaseDatabase Framework Reference

# Type Definitions

The following type definitions are available globally.
- `


  ### [FIRDatabaseHandle](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Type-Definitions#/c:FIRDatabaseQuery.h@T@FIRDatabaseHandle)


  ` A `DatabaseHandle` is used to identify listeners of Firebase Database
  events. These handles are returned by `observe(_:with:)` and can later be
  passed to `removeObserver(withHandle:)` to stop receiving updates.

  #### Declaration

  Objective-C

      typedef NSUInteger FIRDatabaseHandle
# Source: https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Protocols/FIRPerformanceAttributable.md.txt

# FirebasePerformance Framework Reference

# FIRPerformanceAttributable

    @protocol FIRPerformanceAttributable <NSObject>

Defines the interface that allows adding/removing attributes to any object.
- `
  ``
  ``
  `

  ### [attributes](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Protocols/FIRPerformanceAttributable#/c:objc(pl)FIRPerformanceAttributable(py)attributes)

  `
  `  
  List of attributes.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nonnull) NSDictionary<NSString *, NSString *> *attributes;

- `
  ``
  ``
  `

  ### [-setValue:forAttribute:](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Protocols/FIRPerformanceAttributable#/c:objc(pl)FIRPerformanceAttributable(im)setValue:forAttribute:)

  `
  `  
  Sets a value as a string for the specified attribute. Updates the value of the attribute if a
  value had already existed.  

  #### Declaration

  Objective-C  

      - (void)setValue:(nonnull NSString *)value
          forAttribute:(nonnull NSString *)attribute;

  #### Parameters

  |-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*value*` `     | The value that needs to be set/updated for an attribute. If the length of the value exceeds the maximum allowed, the value will be truncated to the maximum allowed. |
  | ` `*attribute*` ` | The name of the attribute. If the length of the value exceeds the maximum allowed, the value will be truncated to the maximum allowed.                               |

- `
  ``
  ``
  `

  ### [-valueForAttribute:](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Protocols/FIRPerformanceAttributable#/c:objc(pl)FIRPerformanceAttributable(im)valueForAttribute:)

  `
  `  
  Reads the value for the specified attribute. If the attribute does not exist, returns nil.  

  #### Declaration

  Objective-C  

      - (nullable NSString *)valueForAttribute:(nonnull NSString *)attribute;

  #### Parameters

  |-------------------|----------------------------|
  | ` `*attribute*` ` | The name of the attribute. |

  #### Return Value

  The value for the attribute. Returns nil if the attribute does not exist.
- `
  ``
  ``
  `

  ### [-removeAttribute:](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Protocols/FIRPerformanceAttributable#/c:objc(pl)FIRPerformanceAttributable(im)removeAttribute:)

  `
  `  
  Removes an attribute from the list. Does nothing if the attribute does not exist.  

  #### Declaration

  Objective-C  

      - (void)removeAttribute:(nonnull NSString *)attribute;

  #### Parameters

  |-------------------|----------------------------|
  | ` `*attribute*` ` | The name of the attribute. |
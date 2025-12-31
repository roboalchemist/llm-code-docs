# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Filter.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Filter.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Filter.md.txt

# FirebaseFirestore Framework Reference

# Filter

    class Filter : NSObject, @unchecked Sendable

A Filter represents a restriction on one or more field values and can be used to refine
the results of a Query.
[## Create Filter](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Filter#/Create-Filter)

- `
  ``
  ``
  `

  ### [whereField(_:isEqualTo:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Filter#/c:objc(cs)FIRFilter(cm)filterWhereField:isEqualTo:)

  `
  `  
  Creates a new filter for checking that the given field is equal to the given value.  

  #### Declaration

  Swift  

      class func whereField(_ field: String, isEqualTo value: Any) -> Filter

  #### Parameters

  |---------------|--------------------------------|
  | ` `*field*` ` | The field used for the filter. |
  | ` `*value*` ` | The value used for the filter. |

  #### Return Value

  The newly created filter.
- `
  ``
  ``
  `

  ### [whereField(_:isEqualTo:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Filter#/c:objc(cs)FIRFilter(cm)filterWhereFieldPath:isEqualTo:)

  `
  `  
  Creates a new filter for checking that the given field is equal to the given value.  

  #### Declaration

  Swift  

      class func whereField(_ path: FIRFieldPath, isEqualTo value: Any) -> Filter

  #### Parameters

  |---------------|-------------------------------------|
  | ` `*path*` `  | The field path used for the filter. |
  | ` `*value*` ` | The value used for the filter.      |

  #### Return Value

  The newly created filter.
- `
  ``
  ``
  `

  ### [whereField(_:isNotEqualTo:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Filter#/c:objc(cs)FIRFilter(cm)filterWhereField:isNotEqualTo:)

  `
  `  
  Creates a new filter for checking that the given field is not equal to the given value.  

  #### Declaration

  Swift  

      class func whereField(_ field: String, isNotEqualTo value: Any) -> Filter

  #### Parameters

  |---------------|--------------------------------|
  | ` `*field*` ` | The field used for the filter. |
  | ` `*value*` ` | The value used for the filter. |

  #### Return Value

  The newly created filter.
- `
  ``
  ``
  `

  ### [whereField(_:isNotEqualTo:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Filter#/c:objc(cs)FIRFilter(cm)filterWhereFieldPath:isNotEqualTo:)

  `
  `  
  Creates a new filter for checking that the given field is not equal to the given value.  

  #### Declaration

  Swift  

      class func whereField(_ path: FIRFieldPath, isNotEqualTo value: Any) -> Filter

  #### Parameters

  |---------------|-------------------------------------|
  | ` `*path*` `  | The field path used for the filter. |
  | ` `*value*` ` | The value used for the filter.      |

  #### Return Value

  The newly created filter.
- `
  ``
  ``
  `

  ### [whereField(_:isGreaterThan:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Filter#/c:objc(cs)FIRFilter(cm)filterWhereField:isGreaterThan:)

  `
  `  
  Creates a new filter for checking that the given field is greater than the given value.  

  #### Declaration

  Swift  

      class func whereField(_ field: String, isGreaterThan value: Any) -> Filter

  #### Parameters

  |---------------|--------------------------------|
  | ` `*field*` ` | The field used for the filter. |
  | ` `*value*` ` | The value used for the filter. |

  #### Return Value

  The newly created filter.
- `
  ``
  ``
  `

  ### [whereField(_:isGreaterThan:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Filter#/c:objc(cs)FIRFilter(cm)filterWhereFieldPath:isGreaterThan:)

  `
  `  
  Creates a new filter for checking that the given field is greater than the given value.  

  #### Declaration

  Swift  

      class func whereField(_ path: FIRFieldPath, isGreaterThan value: Any) -> Filter

  #### Parameters

  |---------------|-------------------------------------|
  | ` `*path*` `  | The field path used for the filter. |
  | ` `*value*` ` | The value used for the filter.      |

  #### Return Value

  The newly created filter.
- `
  ``
  ``
  `

  ### [whereField(_:isGreaterOrEqualTo:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Filter#/c:objc(cs)FIRFilter(cm)filterWhereField:isGreaterThanOrEqualTo:)

  `
  `  
  Creates a new filter for checking that the given field is greater than or equal to the given
  value.  

  #### Declaration

  Swift  

      class func whereField(_ field: String, isGreaterOrEqualTo value: Any) -> Filter

  #### Parameters

  |---------------|--------------------------------|
  | ` `*field*` ` | The field used for the filter. |
  | ` `*value*` ` | The value used for the filter. |

  #### Return Value

  The newly created filter.
- `
  ``
  ``
  `

  ### [whereField(_:isGreaterOrEqualTo:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Filter#/c:objc(cs)FIRFilter(cm)filterWhereFieldPath:isGreaterThanOrEqualTo:)

  `
  `  
  Creates a new filter for checking that the given field is greater than or equal to the given
  value.  

  #### Declaration

  Swift  

      class func whereField(_ path: FIRFieldPath, isGreaterOrEqualTo value: Any) -> Filter

  #### Parameters

  |---------------|-------------------------------------|
  | ` `*path*` `  | The field path used for the filter. |
  | ` `*value*` ` | The value used for the filter.      |

  #### Return Value

  The newly created filter.
- `
  ``
  ``
  `

  ### [whereField(_:isLessThan:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Filter#/c:objc(cs)FIRFilter(cm)filterWhereField:isLessThan:)

  `
  `  
  Creates a new filter for checking that the given field is less than the given value.  

  #### Declaration

  Swift  

      class func whereField(_ field: String, isLessThan value: Any) -> Filter

  #### Parameters

  |---------------|--------------------------------|
  | ` `*field*` ` | The field used for the filter. |
  | ` `*value*` ` | The value used for the filter. |

  #### Return Value

  The newly created filter.
- `
  ``
  ``
  `

  ### [whereField(_:isLessThan:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Filter#/c:objc(cs)FIRFilter(cm)filterWhereFieldPath:isLessThan:)

  `
  `  
  Creates a new filter for checking that the given field is less than the given value.  

  #### Declaration

  Swift  

      class func whereField(_ path: FIRFieldPath, isLessThan value: Any) -> Filter

  #### Parameters

  |---------------|-------------------------------------|
  | ` `*path*` `  | The field path used for the filter. |
  | ` `*value*` ` | The value used for the filter.      |

  #### Return Value

  The newly created filter.
- `
  ``
  ``
  `

  ### [whereField(_:isLessThanOrEqualTo:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Filter#/c:objc(cs)FIRFilter(cm)filterWhereField:isLessThanOrEqualTo:)

  `
  `  
  Creates a new filter for checking that the given field is less than or equal to the given
  value.  

  #### Declaration

  Swift  

      class func whereField(_ field: String, isLessThanOrEqualTo value: Any) -> Filter

  #### Parameters

  |---------------|--------------------------------|
  | ` `*field*` ` | The field used for the filter. |
  | ` `*value*` ` | The value used for the filter. |

  #### Return Value

  The newly created filter.
- `
  ``
  ``
  `

  ### [whereField(_:isLessThanOrEqualTo:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Filter#/c:objc(cs)FIRFilter(cm)filterWhereFieldPath:isLessThanOrEqualTo:)

  `
  `  
  Creates a new filter for checking that the given field is less than or equal to the given
  value.  

  #### Declaration

  Swift  

      class func whereField(_ path: FIRFieldPath, isLessThanOrEqualTo value: Any) -> Filter

  #### Parameters

  |---------------|-------------------------------------|
  | ` `*path*` `  | The field path used for the filter. |
  | ` `*value*` ` | The value used for the filter.      |

  #### Return Value

  The newly created filter.
- `
  ``
  ``
  `

  ### [whereField(_:arrayContains:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Filter#/c:objc(cs)FIRFilter(cm)filterWhereField:arrayContains:)

  `
  `  
  Creates a new filter for checking that the given array field contains the given value.  

  #### Declaration

  Swift  

      class func whereField(_ field: String, arrayContains value: Any) -> Filter

  #### Parameters

  |---------------|--------------------------------|
  | ` `*field*` ` | The field used for the filter. |
  | ` `*value*` ` | The value used for the filter. |

  #### Return Value

  The newly created filter.
- `
  ``
  ``
  `

  ### [whereField(_:arrayContains:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Filter#/c:objc(cs)FIRFilter(cm)filterWhereFieldPath:arrayContains:)

  `
  `  
  Creates a new filter for checking that the given array field contains the given value.  

  #### Declaration

  Swift  

      class func whereField(_ path: FIRFieldPath, arrayContains value: Any) -> Filter

  #### Parameters

  |---------------|-------------------------------------|
  | ` `*path*` `  | The field path used for the filter. |
  | ` `*value*` ` | The value used for the filter.      |

  #### Return Value

  The newly created filter.
- `
  ``
  ``
  `

  ### [whereField(_:arrayContainsAny:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Filter#/c:objc(cs)FIRFilter(cm)filterWhereField:arrayContainsAny:)

  `
  `  
  Creates a new filter for checking that the given array field contains any of the given values.  

  #### Declaration

  Swift  

      class func whereField(_ field: String, arrayContainsAny values: [Any]) -> Filter

  #### Parameters

  |----------------|-----------------------------------------|
  | ` `*field*` `  | The field used for the filter.          |
  | ` `*values*` ` | The list of values used for the filter. |

  #### Return Value

  The newly created filter.
- `
  ``
  ``
  `

  ### [whereField(_:arrayContainsAny:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Filter#/c:objc(cs)FIRFilter(cm)filterWhereFieldPath:arrayContainsAny:)

  `
  `  
  Creates a new filter for checking that the given array field contains any of the given values.  

  #### Declaration

  Swift  

      class func whereField(_ path: FIRFieldPath, arrayContainsAny values: [Any]) -> Filter

  #### Parameters

  |----------------|-----------------------------------------|
  | ` `*path*` `   | The field path used for the filter.     |
  | ` `*values*` ` | The list of values used for the filter. |

  #### Return Value

  The newly created filter.
- `
  ``
  ``
  `

  ### [whereField(_:in:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Filter#/c:objc(cs)FIRFilter(cm)filterWhereField:in:)

  `
  `  
  Creates a new filter for checking that the given field equals any of the given values.  

  #### Declaration

  Swift  

      class func whereField(_ field: String, in values: [Any]) -> Filter

  #### Parameters

  |----------------|-----------------------------------------|
  | ` `*field*` `  | The field used for the filter.          |
  | ` `*values*` ` | The list of values used for the filter. |

  #### Return Value

  The newly created filter.
- `
  ``
  ``
  `

  ### [whereField(_:in:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Filter#/c:objc(cs)FIRFilter(cm)filterWhereFieldPath:in:)

  `
  `  
  Creates a new filter for checking that the given field equals any of the given values.  

  #### Declaration

  Swift  

      class func whereField(_ path: FIRFieldPath, in values: [Any]) -> Filter

  #### Parameters

  |----------------|-----------------------------------------|
  | ` `*path*` `   | The field path used for the filter.     |
  | ` `*values*` ` | The list of values used for the filter. |

  #### Return Value

  The newly created filter.
- `
  ``
  ``
  `

  ### [whereField(_:notIn:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Filter#/c:objc(cs)FIRFilter(cm)filterWhereField:notIn:)

  `
  `  
  Creates a new filter for checking that the given field does not equal any of the given values.  

  #### Declaration

  Swift  

      class func whereField(_ field: String, notIn values: [Any]) -> Filter

  #### Parameters

  |----------------|-----------------------------------------|
  | ` `*field*` `  | The field path used for the filter.     |
  | ` `*values*` ` | The list of values used for the filter. |

  #### Return Value

  The newly created filter.
- `
  ``
  ``
  `

  ### [whereField(_:notIn:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Filter#/c:objc(cs)FIRFilter(cm)filterWhereFieldPath:notIn:)

  `
  `  
  Creates a new filter for checking that the given field does not equal any of the given values.  

  #### Declaration

  Swift  

      class func whereField(_ path: FIRFieldPath, notIn values: [Any]) -> Filter

  #### Parameters

  |----------------|-----------------------------------------|
  | ` `*path*` `   | The field path used for the filter.     |
  | ` `*values*` ` | The list of values used for the filter. |

  #### Return Value

  The newly created filter.
- `
  ``
  ``
  `

  ### [orFilter(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Filter#/c:objc(cs)FIRFilter(cm)orFilterWithFilters:)

  `
  `  
  Creates a new filter that is a disjunction of the given filters. A disjunction filter includes
  a document if it satisfies any of the given filters.  

  #### Declaration

  Swift  

      class func orFilter(_ filters: [Filter]) -> Filter

  #### Parameters

  |-----------------|---------------------------------------------------|
  | ` `*filters*` ` | The list of filters to perform a disjunction for. |

  #### Return Value

  The newly created filter.
- `
  ``
  ``
  `

  ### [andFilter(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Filter#/c:objc(cs)FIRFilter(cm)andFilterWithFilters:)

  `
  `  
  Creates a new filter that is a conjunction of the given filters. A conjunction filter includes
  a document if it satisfies all of the given filters.  

  #### Declaration

  Swift  

      class func andFilter(_ filters: [Filter]) -> Filter

  #### Parameters

  |-----------------|---------------------------------------------------|
  | ` `*filters*` ` | The list of filters to perform a disjunction for. |

  #### Return Value

  The newly created filter.
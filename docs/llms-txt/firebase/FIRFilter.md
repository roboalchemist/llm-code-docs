# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFilter.md.txt

# FirebaseFirestore Framework Reference

# FIRFilter


    @interface FIRFilter : NSObject

A Filter represents a restriction on one or more field values and can be used to refine
the results of a Query.
[## Create Filter](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFilter#/Create-Filter)

- `
  ``
  ``
  `

  ### [+filterWhereField:isEqualTo:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFilter#/c:objc(cs)FIRFilter(cm)filterWhereField:isEqualTo:)

  `
  `  
  Creates a new filter for checking that the given field is equal to the given value.  

  #### Declaration

  Objective-C  

      + (nonnull FIRFilter *)filterWhereField:(nonnull NSString *)field
                                    isEqualTo:(nonnull id)value;

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

  ### [+filterWhereFieldPath:isEqualTo:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFilter#/c:objc(cs)FIRFilter(cm)filterWhereFieldPath:isEqualTo:)

  `
  `  
  Creates a new filter for checking that the given field is equal to the given value.  

  #### Declaration

  Objective-C  

      + (nonnull FIRFilter *)filterWhereFieldPath:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldPath.html *)path
                                        isEqualTo:(nonnull id)value;

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

  ### [+filterWhereField:isNotEqualTo:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFilter#/c:objc(cs)FIRFilter(cm)filterWhereField:isNotEqualTo:)

  `
  `  
  Creates a new filter for checking that the given field is not equal to the given value.  

  #### Declaration

  Objective-C  

      + (nonnull FIRFilter *)filterWhereField:(nonnull NSString *)field
                                 isNotEqualTo:(nonnull id)value;

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

  ### [+filterWhereFieldPath:isNotEqualTo:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFilter#/c:objc(cs)FIRFilter(cm)filterWhereFieldPath:isNotEqualTo:)

  `
  `  
  Creates a new filter for checking that the given field is not equal to the given value.  

  #### Declaration

  Objective-C  

      + (nonnull FIRFilter *)filterWhereFieldPath:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldPath.html *)path
                                     isNotEqualTo:(nonnull id)value;

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

  ### [+filterWhereField:isGreaterThan:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFilter#/c:objc(cs)FIRFilter(cm)filterWhereField:isGreaterThan:)

  `
  `  
  Creates a new filter for checking that the given field is greater than the given value.  

  #### Declaration

  Objective-C  

      + (nonnull FIRFilter *)filterWhereField:(nonnull NSString *)field
                                isGreaterThan:(nonnull id)value;

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

  ### [+filterWhereFieldPath:isGreaterThan:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFilter#/c:objc(cs)FIRFilter(cm)filterWhereFieldPath:isGreaterThan:)

  `
  `  
  Creates a new filter for checking that the given field is greater than the given value.  

  #### Declaration

  Objective-C  

      + (nonnull FIRFilter *)filterWhereFieldPath:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldPath.html *)path
                                    isGreaterThan:(nonnull id)value;

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

  ### [+filterWhereField:isGreaterThanOrEqualTo:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFilter#/c:objc(cs)FIRFilter(cm)filterWhereField:isGreaterThanOrEqualTo:)

  `
  `  
  Creates a new filter for checking that the given field is greater than or equal to the given
  value.  

  #### Declaration

  Objective-C  

      + (nonnull FIRFilter *)filterWhereField:(nonnull NSString *)field
                       isGreaterThanOrEqualTo:(nonnull id)value;

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

  ### [+filterWhereFieldPath:isGreaterThanOrEqualTo:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFilter#/c:objc(cs)FIRFilter(cm)filterWhereFieldPath:isGreaterThanOrEqualTo:)

  `
  `  
  Creates a new filter for checking that the given field is greater than or equal to the given
  value.  

  #### Declaration

  Objective-C  

      + (nonnull FIRFilter *)filterWhereFieldPath:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldPath.html *)path
                           isGreaterThanOrEqualTo:(nonnull id)value;

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

  ### [+filterWhereField:isLessThan:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFilter#/c:objc(cs)FIRFilter(cm)filterWhereField:isLessThan:)

  `
  `  
  Creates a new filter for checking that the given field is less than the given value.  

  #### Declaration

  Objective-C  

      + (nonnull FIRFilter *)filterWhereField:(nonnull NSString *)field
                                   isLessThan:(nonnull id)value;

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

  ### [+filterWhereFieldPath:isLessThan:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFilter#/c:objc(cs)FIRFilter(cm)filterWhereFieldPath:isLessThan:)

  `
  `  
  Creates a new filter for checking that the given field is less than the given value.  

  #### Declaration

  Objective-C  

      + (nonnull FIRFilter *)filterWhereFieldPath:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldPath.html *)path
                                       isLessThan:(nonnull id)value;

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

  ### [+filterWhereField:isLessThanOrEqualTo:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFilter#/c:objc(cs)FIRFilter(cm)filterWhereField:isLessThanOrEqualTo:)

  `
  `  
  Creates a new filter for checking that the given field is less than or equal to the given
  value.  

  #### Declaration

  Objective-C  

      + (nonnull FIRFilter *)filterWhereField:(nonnull NSString *)field
                          isLessThanOrEqualTo:(nonnull id)value;

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

  ### [+filterWhereFieldPath:isLessThanOrEqualTo:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFilter#/c:objc(cs)FIRFilter(cm)filterWhereFieldPath:isLessThanOrEqualTo:)

  `
  `  
  Creates a new filter for checking that the given field is less than or equal to the given
  value.  

  #### Declaration

  Objective-C  

      + (nonnull FIRFilter *)filterWhereFieldPath:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldPath.html *)path
                              isLessThanOrEqualTo:(nonnull id)value;

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

  ### [+filterWhereField:arrayContains:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFilter#/c:objc(cs)FIRFilter(cm)filterWhereField:arrayContains:)

  `
  `  
  Creates a new filter for checking that the given array field contains the given value.  

  #### Declaration

  Objective-C  

      + (nonnull FIRFilter *)filterWhereField:(nonnull NSString *)field
                                arrayContains:(nonnull id)value;

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

  ### [+filterWhereFieldPath:arrayContains:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFilter#/c:objc(cs)FIRFilter(cm)filterWhereFieldPath:arrayContains:)

  `
  `  
  Creates a new filter for checking that the given array field contains the given value.  

  #### Declaration

  Objective-C  

      + (nonnull FIRFilter *)filterWhereFieldPath:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldPath.html *)path
                                    arrayContains:(nonnull id)value;

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

  ### [+filterWhereField:arrayContainsAny:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFilter#/c:objc(cs)FIRFilter(cm)filterWhereField:arrayContainsAny:)

  `
  `  
  Creates a new filter for checking that the given array field contains any of the given values.  

  #### Declaration

  Objective-C  

      + (nonnull FIRFilter *)filterWhereField:(nonnull NSString *)field
                             arrayContainsAny:(nonnull NSArray<id> *)values;

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

  ### [+filterWhereFieldPath:arrayContainsAny:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFilter#/c:objc(cs)FIRFilter(cm)filterWhereFieldPath:arrayContainsAny:)

  `
  `  
  Creates a new filter for checking that the given array field contains any of the given values.  

  #### Declaration

  Objective-C  

      + (nonnull FIRFilter *)filterWhereFieldPath:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldPath.html *)path
                                 arrayContainsAny:(nonnull NSArray<id> *)values;

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

  ### [+filterWhereField:in:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFilter#/c:objc(cs)FIRFilter(cm)filterWhereField:in:)

  `
  `  
  Creates a new filter for checking that the given field equals any of the given values.  

  #### Declaration

  Objective-C  

      + (nonnull FIRFilter *)filterWhereField:(nonnull NSString *)field
                                           in:(nonnull NSArray<id> *)values;

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

  ### [+filterWhereFieldPath:in:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFilter#/c:objc(cs)FIRFilter(cm)filterWhereFieldPath:in:)

  `
  `  
  Creates a new filter for checking that the given field equals any of the given values.  

  #### Declaration

  Objective-C  

      + (nonnull FIRFilter *)filterWhereFieldPath:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldPath.html *)path
                                               in:(nonnull NSArray<id> *)values;

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

  ### [+filterWhereField:notIn:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFilter#/c:objc(cs)FIRFilter(cm)filterWhereField:notIn:)

  `
  `  
  Creates a new filter for checking that the given field does not equal any of the given values.  

  #### Declaration

  Objective-C  

      + (nonnull FIRFilter *)filterWhereField:(nonnull NSString *)field
                                        notIn:(nonnull NSArray<id> *)values;

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

  ### [+filterWhereFieldPath:notIn:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFilter#/c:objc(cs)FIRFilter(cm)filterWhereFieldPath:notIn:)

  `
  `  
  Creates a new filter for checking that the given field does not equal any of the given values.  

  #### Declaration

  Objective-C  

      + (nonnull FIRFilter *)filterWhereFieldPath:(nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldPath.html *)path
                                            notIn:(nonnull NSArray<id> *)values;

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

  ### [+orFilterWithFilters:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFilter#/c:objc(cs)FIRFilter(cm)orFilterWithFilters:)

  `
  `  
  Creates a new filter that is a disjunction of the given filters. A disjunction filter includes
  a document if it satisfies any of the given filters.  

  #### Declaration

  Objective-C  

      + (nonnull FIRFilter *)orFilterWithFilters:
          (nonnull NSArray<FIRFilter *> *)filters;

  #### Parameters

  |-----------------|---------------------------------------------------|
  | ` `*filters*` ` | The list of filters to perform a disjunction for. |

  #### Return Value

  The newly created filter.
- `
  ``
  ``
  `

  ### [+andFilterWithFilters:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFilter#/c:objc(cs)FIRFilter(cm)andFilterWithFilters:)

  `
  `  
  Creates a new filter that is a conjunction of the given filters. A conjunction filter includes
  a document if it satisfies all of the given filters.  

  #### Declaration

  Objective-C  

      + (nonnull FIRFilter *)andFilterWithFilters:
          (nonnull NSArray<FIRFilter *> *)filters;

  #### Parameters

  |-----------------|---------------------------------------------------|
  | ` `*filters*` ` | The list of filters to perform a disjunction for. |

  #### Return Value

  The newly created filter.
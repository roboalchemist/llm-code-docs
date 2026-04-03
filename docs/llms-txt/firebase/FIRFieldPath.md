# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldPath.md.txt

# FirebaseFirestore Framework Reference

# FIRFieldPath


    @interface FIRFieldPath : NSObject <NSCopying>

A `FieldPath` refers to a field in a document. The path may consist of a single field name
(referring to a top level field in the document), or a list of field names (referring to a nested
field in the document).
- `
  ``
  ``
  `

  ### [-initWithFields:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldPath#/c:objc(cs)FIRFieldPath(im)initWithFields:)

  `
  `  
  Creates a `FieldPath` from the provided field names. If more than one field name is provided, the
  path will point to a nested field in a document.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)initWithFields:
          (nonnull NSArray<NSString *> *)fieldNames;

  #### Parameters

  |--------------------|------------------------|
  | ` `*fieldNames*` ` | A list of field names. |

  #### Return Value

  A `FieldPath` that points to a field location in a document.
- `
  ``
  ``
  `

  ### [+documentID](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldPath#/c:objc(cs)FIRFieldPath(cm)documentID)

  `
  `  
  A special sentinel `FieldPath` to refer to the ID of a document. It can be used in queries to
  sort or filter by the document ID.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)documentID;
# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionImageLabel.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionImageLabel


    @interface FIRVisionImageLabel : NSObject

Represents a label for an image.
- `
  ``
  ``
  `

  ### [text](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionImageLabel#/c:objc(cs)FIRVisionImageLabel(py)text)

  `
  `  
  The human readable label text in American English. For example: "Balloon".

  This string is not fit for display purposes, as it is not localized. Use the
  [entityID](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionImageLabel.html#/c:objc(cs)FIRVisionImageLabel(py)entityID) and query the Knowledge Graph to get a localized description of the label text.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly) NSString *_Nonnull text;

- `
  ``
  ``
  `

  ### [confidence](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionImageLabel#/c:objc(cs)FIRVisionImageLabel(py)confidence)

  `
  `  
  Confidence for the label in range \[0, 1\]. The value is a `floatValue`.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSNumber *confidence;

- `
  ``
  ``
  `

  ### [entityID](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionImageLabel#/c:objc(cs)FIRVisionImageLabel(py)entityID)

  `
  `  
  Opaque entity ID used to query the Knowledge Graph to get a localized description of the label
  text. Some IDs may be available in [Google Knowledge Graph Search API](https://developers.google.com/knowledge-graph/).  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nullable) NSString *entityID;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionImageLabel#/c:objc(cs)FIRVisionImageLabel(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;
# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionImageLabel.md.txt

# FirebaseMLVision Framework Reference

# VisionImageLabel

    class VisionImageLabel : NSObject

Represents a label for an image.
- `
  ``
  ``
  `

  ### [text](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionImageLabel#/c:objc(cs)FIRVisionImageLabel(py)text)

  `
  `  
  The human readable label text in American English. For example: "Balloon".

  This string is not fit for display purposes, as it is not localized. Use the
  [entityID](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionImageLabel.html#/c:objc(cs)FIRVisionImageLabel(py)entityID) and query the Knowledge Graph to get a localized description of the label text.  

  #### Declaration

  Swift  

      var text: String { get }

- `
  ``
  ``
  `

  ### [confidence](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionImageLabel#/c:objc(cs)FIRVisionImageLabel(py)confidence)

  `
  `  
  Confidence for the label in range \[0, 1\]. The value is a `floatValue`.  

  #### Declaration

  Swift  

      var confidence: NSNumber? { get }

- `
  ``
  ``
  `

  ### [entityID](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionImageLabel#/c:objc(cs)FIRVisionImageLabel(py)entityID)

  `
  `  
  Opaque entity ID used to query the Knowledge Graph to get a localized description of the label
  text. Some IDs may be available in [Google Knowledge Graph Search API](https://developers.google.com/knowledge-graph/).  

  #### Declaration

  Swift  

      var entityID: String? { get }

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionImageLabel#/c:objc(cs)FIRVisionImageLabel(im)init)

  `
  `  
  Unavailable.
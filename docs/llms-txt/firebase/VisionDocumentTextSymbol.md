# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextSymbol.md.txt

# FirebaseMLVision Framework Reference

# VisionDocumentTextSymbol

    class VisionDocumentTextSymbol : NSObject

A document text symbol recognized in an image.
- `
  ``
  ``
  `

  ### [text](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextSymbol#/c:objc(cs)FIRVisionDocumentTextSymbol(py)text)

  `
  `  
  String representation of the document text symbol that was recognized.  

  #### Declaration

  Swift  

      var text: String { get }

- `
  ``
  ``
  `

  ### [frame](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextSymbol#/c:objc(cs)FIRVisionDocumentTextSymbol(py)frame)

  `
  `  
  The rectangle that contains the document text symbol relative to the image in the default
  coordinate space.  

  #### Declaration

  Swift  

      var frame: CGRect { get }

- `
  ``
  ``
  `

  ### [confidence](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextSymbol#/c:objc(cs)FIRVisionDocumentTextSymbol(py)confidence)

  `
  `  
  The confidence of the recognized document text symbol.  

  #### Declaration

  Swift  

      var confidence: NSNumber { get }

- `
  ``
  ``
  `

  ### [recognizedLanguages](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextSymbol#/c:objc(cs)FIRVisionDocumentTextSymbol(py)recognizedLanguages)

  `
  `  
  An array of recognized languages in the document text symbol. If no languages are recognized, the
  array is empty.  

  #### Declaration

  Swift  

      var recognizedLanguages: [FIRVisionTextRecognizedLanguage] { get }

- `
  ``
  ``
  `

  ### [recognizedBreak](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextSymbol#/c:objc(cs)FIRVisionDocumentTextSymbol(py)recognizedBreak)

  `
  `  
  The recognized start or end of the document text symbol.  

  #### Declaration

  Swift  

      var recognizedBreak: FIRVisionTextRecognizedBreak? { get }

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextSymbol#/c:objc(cs)FIRVisionDocumentTextSymbol(im)init)

  `
  `  
  Unavailable.
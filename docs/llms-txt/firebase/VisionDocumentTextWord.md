# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextWord.md.txt

# FirebaseMLVision Framework Reference

# VisionDocumentTextWord

    class VisionDocumentTextWord : NSObject

A document text word recognized in an image that consists of an array of symbols.
- `
  ``
  ``
  `

  ### [text](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextWord#/c:objc(cs)FIRVisionDocumentTextWord(py)text)

  `
  `  
  String representation of the document text word that was recognized.  

  #### Declaration

  Swift  

      var text: String { get }

- `
  ``
  ``
  `

  ### [symbols](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextWord#/c:objc(cs)FIRVisionDocumentTextWord(py)symbols)

  `
  `  
  An array of symbols in the document text word.  

  #### Declaration

  Swift  

      var symbols: [FIRVisionDocumentTextSymbol] { get }

- `
  ``
  ``
  `

  ### [frame](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextWord#/c:objc(cs)FIRVisionDocumentTextWord(py)frame)

  `
  `  
  The rectangle that contains the document text word relative to the image in the default
  coordinate space.  

  #### Declaration

  Swift  

      var frame: CGRect { get }

- `
  ``
  ``
  `

  ### [confidence](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextWord#/c:objc(cs)FIRVisionDocumentTextWord(py)confidence)

  `
  `  
  The confidence of the recognized document text word.  

  #### Declaration

  Swift  

      var confidence: NSNumber { get }

- `
  ``
  ``
  `

  ### [recognizedLanguages](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextWord#/c:objc(cs)FIRVisionDocumentTextWord(py)recognizedLanguages)

  `
  `  
  An array of recognized languages in the document text word. If no languages are recognized, the
  array is empty.  

  #### Declaration

  Swift  

      var recognizedLanguages: [FIRVisionTextRecognizedLanguage] { get }

- `
  ``
  ``
  `

  ### [recognizedBreak](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextWord#/c:objc(cs)FIRVisionDocumentTextWord(py)recognizedBreak)

  `
  `  
  The recognized start or end of the document text word.  

  #### Declaration

  Swift  

      var recognizedBreak: FIRVisionTextRecognizedBreak? { get }

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextWord#/c:objc(cs)FIRVisionDocumentTextWord(im)init)

  `
  `  
  Unavailable.
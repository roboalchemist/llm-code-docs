# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextParagraph.md.txt

# FirebaseMLVision Framework Reference

# VisionDocumentTextParagraph

    class VisionDocumentTextParagraph : NSObject

A document text paragraph recognized in an image that consists of an array of words.
- `
  ``
  ``
  `

  ### [text](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextParagraph#/c:objc(cs)FIRVisionDocumentTextParagraph(py)text)

  `
  `  
  String representation of the document text paragraph that was recognized.  

  #### Declaration

  Swift  

      var text: String { get }

- `
  ``
  ``
  `

  ### [words](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextParagraph#/c:objc(cs)FIRVisionDocumentTextParagraph(py)words)

  `
  `  
  An array of words in the document text paragraph.  

  #### Declaration

  Swift  

      var words: [FIRVisionDocumentTextWord] { get }

- `
  ``
  ``
  `

  ### [frame](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextParagraph#/c:objc(cs)FIRVisionDocumentTextParagraph(py)frame)

  `
  `  
  The rectangle that contains the document text paragraph relative to the image in the default
  coordinate space.  

  #### Declaration

  Swift  

      var frame: CGRect { get }

- `
  ``
  ``
  `

  ### [confidence](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextParagraph#/c:objc(cs)FIRVisionDocumentTextParagraph(py)confidence)

  `
  `  
  The confidence of the recognized document text paragraph.  

  #### Declaration

  Swift  

      var confidence: NSNumber { get }

- `
  ``
  ``
  `

  ### [recognizedLanguages](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextParagraph#/c:objc(cs)FIRVisionDocumentTextParagraph(py)recognizedLanguages)

  `
  `  
  An array of recognized languages in the document text paragraph. If no languages are recognized,
  the array is empty.  

  #### Declaration

  Swift  

      var recognizedLanguages: [FIRVisionTextRecognizedLanguage] { get }

- `
  ``
  ``
  `

  ### [recognizedBreak](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextParagraph#/c:objc(cs)FIRVisionDocumentTextParagraph(py)recognizedBreak)

  `
  `  
  The recognized start or end of the document text paragraph.  

  #### Declaration

  Swift  

      var recognizedBreak: FIRVisionTextRecognizedBreak? { get }

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextParagraph#/c:objc(cs)FIRVisionDocumentTextParagraph(im)init)

  `
  `  
  Unavailable.
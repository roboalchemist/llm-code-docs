# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextBlock.md.txt

# FirebaseMLVision Framework Reference

# VisionDocumentTextBlock

    class VisionDocumentTextBlock : NSObject

A document text block recognized in an image that consists of an array of paragraphs.
- `
  ``
  ``
  `

  ### [type](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextBlock#/c:objc(cs)FIRVisionDocumentTextBlock(py)type)

  `
  `  
  The detected block type.  

  #### Declaration

  Swift  

      var type: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionDocumentTextBlockType.html { get }

- `
  ``
  ``
  `

  ### [text](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextBlock#/c:objc(cs)FIRVisionDocumentTextBlock(py)text)

  `
  `  
  String representation of the document text block that was recognized.  

  #### Declaration

  Swift  

      var text: String { get }

- `
  ``
  ``
  `

  ### [paragraphs](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextBlock#/c:objc(cs)FIRVisionDocumentTextBlock(py)paragraphs)

  `
  `  
  An array of paragraphs in the block if the type is [VisionDocumentTextBlockType.text](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionDocumentTextBlockType.html#/c:@E@FIRVisionDocumentTextBlockType@FIRVisionDocumentTextBlockTypeText). Otherwise,
  the array is empty.  

  #### Declaration

  Swift  

      var paragraphs: [FIRVisionDocumentTextParagraph] { get }

- `
  ``
  ``
  `

  ### [frame](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextBlock#/c:objc(cs)FIRVisionDocumentTextBlock(py)frame)

  `
  `  
  The rectangle that contains the document text block relative to the image in the default
  coordinate space.  

  #### Declaration

  Swift  

      var frame: CGRect { get }

- `
  ``
  ``
  `

  ### [confidence](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextBlock#/c:objc(cs)FIRVisionDocumentTextBlock(py)confidence)

  `
  `  
  The confidence of the recognized document text block.  

  #### Declaration

  Swift  

      var confidence: NSNumber { get }

- `
  ``
  ``
  `

  ### [recognizedLanguages](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextBlock#/c:objc(cs)FIRVisionDocumentTextBlock(py)recognizedLanguages)

  `
  `  
  An array of recognized languages in the document text block. If no languages are recognized, the
  array is empty.  

  #### Declaration

  Swift  

      var recognizedLanguages: [FIRVisionTextRecognizedLanguage] { get }

- `
  ``
  ``
  `

  ### [recognizedBreak](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextBlock#/c:objc(cs)FIRVisionDocumentTextBlock(py)recognizedBreak)

  `
  `  
  The recognized start or end of the document text block.  

  #### Declaration

  Swift  

      var recognizedBreak: FIRVisionTextRecognizedBreak? { get }

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextBlock#/c:objc(cs)FIRVisionDocumentTextBlock(im)init)

  `
  `  
  Unavailable.
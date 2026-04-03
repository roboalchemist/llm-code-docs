# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextBlock.md.txt

# FirebaseMLVision Framework Reference

# VisionTextBlock

    class VisionTextBlock : NSObject

A text block recognized in an image that consists of an array of text lines.
- `
  ``
  ``
  `

  ### [text](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextBlock#/c:objc(cs)FIRVisionTextBlock(py)text)

  `
  `  
  String representation of the text block that was recognized.  

  #### Declaration

  Swift  

      var text: String { get }

- `
  ``
  ``
  `

  ### [lines](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextBlock#/c:objc(cs)FIRVisionTextBlock(py)lines)

  `
  `  
  An array of text lines that make up the block.  

  #### Declaration

  Swift  

      var lines: [FIRVisionTextLine] { get }

- `
  ``
  ``
  `

  ### [frame](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextBlock#/c:objc(cs)FIRVisionTextBlock(py)frame)

  `
  `  
  The rectangle that contains the text block relative to the image in the default coordinate space.  

  #### Declaration

  Swift  

      var frame: CGRect { get }

- `
  ``
  ``
  `

  ### [recognizedLanguages](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextBlock#/c:objc(cs)FIRVisionTextBlock(py)recognizedLanguages)

  `
  `  
  An array of recognized languages in the text block. On-device text recognizers only detect
  Latin-based languages, while cloud text recognizers can detect multiple languages. If no
  languages are recognized, the array is empty.  

  #### Declaration

  Swift  

      var recognizedLanguages: [FIRVisionTextRecognizedLanguage] { get }

- `
  ``
  ``
  `

  ### [cornerPoints](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextBlock#/c:objc(cs)FIRVisionTextBlock(py)cornerPoints)

  `
  `  
  The four corner points of the text block in clockwise order starting with the top left point
  relative to the image in the default coordinate space. The `NSValue` objects are `CGPoint`s. For
  cloud text recognizers, the array is `nil`.  

  #### Declaration

  Swift  

      var cornerPoints: [NSValue]? { get }

- `
  ``
  ``
  `

  ### [confidence](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextBlock#/c:objc(cs)FIRVisionTextBlock(py)confidence)

  `
  `  
  The confidence of the recognized text block. The value is `nil` for all text recognizers except
  for cloud text recognizers with model type [VisionCloudTextModelType.dense](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionCloudTextModelType.html#/c:@E@FIRVisionCloudTextModelType@FIRVisionCloudTextModelTypeDense).  

  #### Declaration

  Swift  

      var confidence: NSNumber? { get }

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextBlock#/c:objc(cs)FIRVisionTextBlock(im)init)

  `
  `  
  Unavailable.
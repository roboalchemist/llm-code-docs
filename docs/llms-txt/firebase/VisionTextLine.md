# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextLine.md.txt

# FirebaseMLVision Framework Reference

# VisionTextLine

    class VisionTextLine : NSObject

A text line recognized in an image that consists of an array of elements.
- `
  ``
  ``
  `

  ### [text](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextLine#/c:objc(cs)FIRVisionTextLine(py)text)

  `
  `  
  String representation of the text line that was recognized.  

  #### Declaration

  Swift  

      var text: String { get }

- `
  ``
  ``
  `

  ### [elements](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextLine#/c:objc(cs)FIRVisionTextLine(py)elements)

  `
  `  
  An array of text elements that make up the line.  

  #### Declaration

  Swift  

      var elements: [FIRVisionTextElement] { get }

- `
  ``
  ``
  `

  ### [frame](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextLine#/c:objc(cs)FIRVisionTextLine(py)frame)

  `
  `  
  The rectangle that contains the text line relative to the image in the default coordinate space.  

  #### Declaration

  Swift  

      var frame: CGRect { get }

- `
  ``
  ``
  `

  ### [recognizedLanguages](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextLine#/c:objc(cs)FIRVisionTextLine(py)recognizedLanguages)

  `
  `  
  An array of recognized languages in the text line. On-device text recognizers only detect
  Latin-based languages, while cloud text recognizers can detect multiple languages. If no
  languages are recognized, the array is empty.  

  #### Declaration

  Swift  

      var recognizedLanguages: [FIRVisionTextRecognizedLanguage] { get }

- `
  ``
  ``
  `

  ### [cornerPoints](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextLine#/c:objc(cs)FIRVisionTextLine(py)cornerPoints)

  `
  `  
  The four corner points of the text line in clockwise order starting with the top left point
  relative to the image in the default coordinate space. The `NSValue` objects are `CGPoint`s. For
  cloud text recognizers, the array is `nil`.  

  #### Declaration

  Swift  

      var cornerPoints: [NSValue]? { get }

- `
  ``
  ``
  `

  ### [confidence](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextLine#/c:objc(cs)FIRVisionTextLine(py)confidence)

  `
  `  
  The confidence of the recognized text line. The value is `nil` for all text recognizers except
  for cloud text recognizers with model type [VisionCloudTextModelType.dense](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionCloudTextModelType.html#/c:@E@FIRVisionCloudTextModelType@FIRVisionCloudTextModelTypeDense).  

  #### Declaration

  Swift  

      var confidence: NSNumber? { get }

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextLine#/c:objc(cs)FIRVisionTextLine(im)init)

  `
  `  
  Unavailable.
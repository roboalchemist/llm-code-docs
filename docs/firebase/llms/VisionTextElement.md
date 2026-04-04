# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextElement.md.txt

# FirebaseMLVision Framework Reference

# VisionTextElement

    class VisionTextElement : NSObject

A text element recognized in an image. A text element is roughly equivalent to a space-separated
word in most Latin-script languages.
- `
  ``
  ``
  `

  ### [text](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextElement#/c:objc(cs)FIRVisionTextElement(py)text)

  `
  `  
  String representation of the text element that was recognized.  

  #### Declaration

  Swift  

      var text: String { get }

- `
  ``
  ``
  `

  ### [frame](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextElement#/c:objc(cs)FIRVisionTextElement(py)frame)

  `
  `  
  The rectangle that contains the text element relative to the image in the default coordinate
  space.  

  #### Declaration

  Swift  

      var frame: CGRect { get }

- `
  ``
  ``
  `

  ### [recognizedLanguages](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextElement#/c:objc(cs)FIRVisionTextElement(py)recognizedLanguages)

  `
  `  
  An array of recognized languages in the text element. (Cloud API only.)  

  #### Declaration

  Swift  

      var recognizedLanguages: [FIRVisionTextRecognizedLanguage] { get }

- `
  ``
  ``
  `

  ### [cornerPoints](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextElement#/c:objc(cs)FIRVisionTextElement(py)cornerPoints)

  `
  `  
  The four corner points of the text element in clockwise order starting with the top left point
  relative to the image in the default coordinate space. The `NSValue` objects are `CGPoint`s. For
  cloud text recognizers, the array is `nil`.  

  #### Declaration

  Swift  

      var cornerPoints: [NSValue]? { get }

- `
  ``
  ``
  `

  ### [confidence](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextElement#/c:objc(cs)FIRVisionTextElement(py)confidence)

  `
  `  
  The confidence of the recognized text element. The value is `nil` for all text recognizers except
  for cloud text recognizers with model type [VisionCloudTextModelType.dense](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionCloudTextModelType.html#/c:@E@FIRVisionCloudTextModelType@FIRVisionCloudTextModelTypeDense).  

  #### Declaration

  Swift  

      var confidence: NSNumber? { get }

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextElement#/c:objc(cs)FIRVisionTextElement(im)init)

  `
  `  
  Unavailable.
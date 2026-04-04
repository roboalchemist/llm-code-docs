# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeDetectorOptions.md.txt

# FirebaseMLVision Framework Reference

# VisionBarcodeDetectorOptions

    class VisionBarcodeDetectorOptions : NSObject

Options for specifying a Barcode detector.
- `
  ``
  ``
  `

  ### [formats](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeDetectorOptions#/c:objc(cs)FIRVisionBarcodeDetectorOptions(py)formats)

  `
  `  
  The barcode formats detected in an image. Note that the detection time will increase for each
  additional format that is specified.  

  #### Declaration

  Swift  

      var formats: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionBarcodeFormat.html { get }

- `
  ``
  ``
  `

  ### [init()](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeDetectorOptions#/c:objc(cs)FIRVisionBarcodeDetectorOptions(im)init)

  `
  `  
  Initializes an instance that detects all supported barcode formats.  

  #### Declaration

  Swift  

      convenience init()

  #### Return Value

  A new instance of Firebase barcode detector options.
- `
  ``
  ``
  `

  ### [init(formats:)](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeDetectorOptions#/c:objc(cs)FIRVisionBarcodeDetectorOptions(im)initWithFormats:)

  `
  `  
  Initializes an instance with the given barcode formats to look for.  

  #### Declaration

  Swift  

      init(formats: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionBarcodeFormat.html)

  #### Parameters

  |-----------------|-----------------------------------------------------------------|
  | ` `*formats*` ` | The barcode formats to initialize the barcode detector options. |

  #### Return Value

  A new instance of Firebase barcode detector options.
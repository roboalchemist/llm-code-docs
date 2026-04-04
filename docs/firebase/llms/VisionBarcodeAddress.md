# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeAddress.md.txt

# FirebaseMLVision Framework Reference

# VisionBarcodeAddress

    class VisionBarcodeAddress : NSObject

An address.
- `
  ``
  ``
  `

  ### [addressLines](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeAddress#/c:objc(cs)FIRVisionBarcodeAddress(py)addressLines)

  `
  `  
  Formatted address, containing multiple lines when appropriate.

  The parsing of address formats is quite limited. Typically all address information will appear
  on the first address line. To handle addresses better, it is recommended to parse the raw data.
  The raw data is available in `FIRVisionBarcode`'s `rawValue` property.  

  #### Declaration

  Swift  

      var addressLines: [String]? { get }

- `
  ``
  ``
  `

  ### [type](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeAddress#/c:objc(cs)FIRVisionBarcodeAddress(py)type)

  `
  `  
  Address type.  

  #### Declaration

  Swift  

      var type: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionBarcodeAddressType.html { get }

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeAddress#/c:objc(cs)FIRVisionBarcodeAddress(im)init)

  `
  `  
  Unavailable.
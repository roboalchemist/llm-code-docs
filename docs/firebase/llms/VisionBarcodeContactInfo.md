# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeContactInfo.md.txt

# FirebaseMLVision Framework Reference

# VisionBarcodeContactInfo

    class VisionBarcodeContactInfo : NSObject

A person's or organization's business card. This may come from different underlying formats
including VCARD and MECARD.

This object represents a simplified view of possible business cards. If you require lossless
access to the information in the barcode, you should parse the raw data yourself. To access the
raw data, use the `FIRVisionBarcode`s `rawValue` property.
- `
  ``
  ``
  `

  ### [addresses](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeContactInfo#/c:objc(cs)FIRVisionBarcodeContactInfo(py)addresses)

  `
  `  
  Person's or organization's addresses.  

  #### Declaration

  Swift  

      var addresses: [https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeAddress.html]? { get }

- `
  ``
  ``
  `

  ### [emails](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeContactInfo#/c:objc(cs)FIRVisionBarcodeContactInfo(py)emails)

  `
  `  
  Contact emails.  

  #### Declaration

  Swift  

      var emails: [https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeEmail.html]? { get }

- `
  ``
  ``
  `

  ### [name](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeContactInfo#/c:objc(cs)FIRVisionBarcodeContactInfo(py)name)

  `
  `  
  A person's name.  

  #### Declaration

  Swift  

      var name: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodePersonName.html? { get }

- `
  ``
  ``
  `

  ### [phones](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeContactInfo#/c:objc(cs)FIRVisionBarcodeContactInfo(py)phones)

  `
  `  
  Contact phone numbers.  

  #### Declaration

  Swift  

      var phones: [https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodePhone.html]? { get }

- `
  ``
  ``
  `

  ### [urls](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeContactInfo#/c:objc(cs)FIRVisionBarcodeContactInfo(py)urls)

  `
  `  
  Contact URLs.  

  #### Declaration

  Swift  

      var urls: [String]? { get }

- `
  ``
  ``
  `

  ### [jobTitle](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeContactInfo#/c:objc(cs)FIRVisionBarcodeContactInfo(py)jobTitle)

  `
  `  
  A job title.  

  #### Declaration

  Swift  

      var jobTitle: String? { get }

- `
  ``
  ``
  `

  ### [organization](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeContactInfo#/c:objc(cs)FIRVisionBarcodeContactInfo(py)organization)

  `
  `  
  A business organization.  

  #### Declaration

  Swift  

      var organization: String? { get }

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeContactInfo#/c:objc(cs)FIRVisionBarcodeContactInfo(im)init)

  `
  `  
  Unavailable.
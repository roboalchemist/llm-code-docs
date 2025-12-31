# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeDriverLicense.md.txt

# FirebaseMLVision Framework Reference

# VisionBarcodeDriverLicense

    class VisionBarcodeDriverLicense : NSObject

A driver license or ID card data representation.

An ANSI driver license contains more fields than are represented by this class. The
`FIRVisionBarcode`s `rawValue` property can be used to access the other fields.
- `
  ``
  ``
  `

  ### [firstName](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeDriverLicense#/c:objc(cs)FIRVisionBarcodeDriverLicense(py)firstName)

  `
  `  
  Holder's first name.  

  #### Declaration

  Swift  

      var firstName: String? { get }

- `
  ``
  ``
  `

  ### [middleName](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeDriverLicense#/c:objc(cs)FIRVisionBarcodeDriverLicense(py)middleName)

  `
  `  
  Holder's middle name.  

  #### Declaration

  Swift  

      var middleName: String? { get }

- `
  ``
  ``
  `

  ### [lastName](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeDriverLicense#/c:objc(cs)FIRVisionBarcodeDriverLicense(py)lastName)

  `
  `  
  Holder's last name.  

  #### Declaration

  Swift  

      var lastName: String? { get }

- `
  ``
  ``
  `

  ### [gender](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeDriverLicense#/c:objc(cs)FIRVisionBarcodeDriverLicense(py)gender)

  `
  `  
  Holder's gender. 1 is male and 2 is female.  

  #### Declaration

  Swift  

      var gender: String? { get }

- `
  ``
  ``
  `

  ### [addressCity](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeDriverLicense#/c:objc(cs)FIRVisionBarcodeDriverLicense(py)addressCity)

  `
  `  
  Holder's city address.  

  #### Declaration

  Swift  

      var addressCity: String? { get }

- `
  ``
  ``
  `

  ### [addressState](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeDriverLicense#/c:objc(cs)FIRVisionBarcodeDriverLicense(py)addressState)

  `
  `  
  Holder's state address.  

  #### Declaration

  Swift  

      var addressState: String? { get }

- `
  ``
  ``
  `

  ### [addressStreet](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeDriverLicense#/c:objc(cs)FIRVisionBarcodeDriverLicense(py)addressStreet)

  `
  `  
  Holder's street address.  

  #### Declaration

  Swift  

      var addressStreet: String? { get }

- `
  ``
  ``
  `

  ### [addressZip](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeDriverLicense#/c:objc(cs)FIRVisionBarcodeDriverLicense(py)addressZip)

  `
  `  
  Holder's address' zipcode.  

  #### Declaration

  Swift  

      var addressZip: String? { get }

- `
  ``
  ``
  `

  ### [birthDate](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeDriverLicense#/c:objc(cs)FIRVisionBarcodeDriverLicense(py)birthDate)

  `
  `  
  Holder's birthday. The date format depends on the issuing country.  

  #### Declaration

  Swift  

      var birthDate: String? { get }

- `
  ``
  ``
  `

  ### [documentType](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeDriverLicense#/c:objc(cs)FIRVisionBarcodeDriverLicense(py)documentType)

  `
  `  
  "DL" for driver licenses, "ID" for ID cards.  

  #### Declaration

  Swift  

      var documentType: String? { get }

- `
  ``
  ``
  `

  ### [licenseNumber](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeDriverLicense#/c:objc(cs)FIRVisionBarcodeDriverLicense(py)licenseNumber)

  `
  `  
  Driver license ID number.  

  #### Declaration

  Swift  

      var licenseNumber: String? { get }

- `
  ``
  ``
  `

  ### [expiryDate](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeDriverLicense#/c:objc(cs)FIRVisionBarcodeDriverLicense(py)expiryDate)

  `
  `  
  Driver license expiration date. The date format depends on the issuing country.  

  #### Declaration

  Swift  

      var expiryDate: String? { get }

- `
  ``
  ``
  `

  ### [issuingDate](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeDriverLicense#/c:objc(cs)FIRVisionBarcodeDriverLicense(py)issuingDate)

  `
  `  
  The date format depends on the issuing country.  

  #### Declaration

  Swift  

      var issuingDate: String? { get }

- `
  ``
  ``
  `

  ### [issuingCountry](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeDriverLicense#/c:objc(cs)FIRVisionBarcodeDriverLicense(py)issuingCountry)

  `
  `  
  A country in which DL/ID was issued.  

  #### Declaration

  Swift  

      var issuingCountry: String? { get }

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeDriverLicense#/c:objc(cs)FIRVisionBarcodeDriverLicense(im)init)

  `
  `  
  Unavailable.
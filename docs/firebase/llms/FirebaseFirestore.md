# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Extensions/FirebaseFirestore.md.txt

# FirebaseFirestore Framework Reference

# FirebaseFirestore

- `
  ``
  ``
  `

  ### [DocumentReference](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Extensions/FirebaseFirestore#/c:objc(cs)FIRDocumentReference)

  `
  `  

  #### Declaration

  Swift  

      extension FirebaseFirestore.DocumentReference: FirebaseFirestore.CodableDocumentReference

      extension FirebaseFirestore.DocumentReference: @retroactive Codable

- `
  ``
  ``
  `

  ### [FieldValue](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Extensions/FirebaseFirestore/FieldValue.html)

  `
  `  
  Extends FieldValue to conform to Encodable.  

  #### Declaration

  Swift  

      extension FirebaseFirestore.FieldValue: Swift.Encodable

- `
  ``
  ``
  `

  ### [GeoPoint](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Extensions/FirebaseFirestore#/c:objc(cs)FIRGeoPoint)

  `
  `  
  Extends GeoPoint to conform to Codable.  

  #### Declaration

  Swift  

      extension FirebaseFirestore.GeoPoint: FirebaseFirestore.CodableGeoPoint

      extension FirebaseFirestore.GeoPoint: @retroactive Codable

- `
  ``
  ``
  `

  ### [VectorValue](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Extensions/FirebaseFirestore#/c:objc(cs)FIRVectorValue)

  `
  `  
  Extends VectorValue to conform to Codable.  

  #### Declaration

  Swift  

      extension FirebaseFirestore.VectorValue: FirebaseFirestore.CodableVectorValue

      extension FirebaseFirestore.VectorValue: @retroactive Codable
# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudLandmark.md.txt

# FirebaseMLVision Framework Reference

# VisionCloudLandmark

    class VisionCloudLandmark : NSObject

Set of landmark properties identified by a vision cloud detector.
- `
  ``
  ``
  `

  ### [entityId](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudLandmark#/c:objc(cs)FIRVisionCloudLandmark(py)entityId)

  `
  `  
  Opaque entity ID. Some IDs may be available in [Google Knowledge Graph Search API](https://developers.google.com/knowledge-graph/).  

  #### Declaration

  Swift  

      var entityId: String? { get }

- `
  ``
  ``
  `

  ### [landmark](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudLandmark#/c:objc(cs)FIRVisionCloudLandmark(py)landmark)

  `
  `  
  Textual description of the landmark.  

  #### Declaration

  Swift  

      var landmark: String? { get }

- `
  ``
  ``
  `

  ### [confidence](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudLandmark#/c:objc(cs)FIRVisionCloudLandmark(py)confidence)

  `
  `  
  Overall confidence of the result. The value is float, in range \[0, 1\].  

  #### Declaration

  Swift  

      var confidence: NSNumber? { get }

- `
  ``
  ``
  `

  ### [frame](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudLandmark#/c:objc(cs)FIRVisionCloudLandmark(py)frame)

  `
  `  
  A rectangle image region to which this landmark belongs to (in the view coordinate system).  

  #### Declaration

  Swift  

      var frame: CGRect { get }

- `
  ``
  ``
  `

  ### [locations](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudLandmark#/c:objc(cs)FIRVisionCloudLandmark(py)locations)

  `
  `  
  The location information for the detected landmark. Multiple LocationInfo elements can be present
  because one location may indicate the location of the scene in the image, and another location
  may indicate the location of the place where the image was taken.  

  #### Declaration

  Swift  

      var locations: [FIRVisionLatitudeLongitude]? { get }

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudLandmark#/c:objc(cs)FIRVisionCloudLandmark(im)init)

  `
  `  
  Unavailable.
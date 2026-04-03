# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudLandmark.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionCloudLandmark


    @interface FIRVisionCloudLandmark : NSObject

Set of landmark properties identified by a vision cloud detector.
- `
  ``
  ``
  `

  ### [entityId](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudLandmark#/c:objc(cs)FIRVisionCloudLandmark(py)entityId)

  `
  `  
  Opaque entity ID. Some IDs may be available in [Google Knowledge Graph Search API](https://developers.google.com/knowledge-graph/).  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nullable) NSString *entityId;

- `
  ``
  ``
  `

  ### [landmark](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudLandmark#/c:objc(cs)FIRVisionCloudLandmark(py)landmark)

  `
  `  
  Textual description of the landmark.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nullable) NSString *landmark;

- `
  ``
  ``
  `

  ### [confidence](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudLandmark#/c:objc(cs)FIRVisionCloudLandmark(py)confidence)

  `
  `  
  Overall confidence of the result. The value is float, in range \[0, 1\].  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSNumber *confidence;

- `
  ``
  ``
  `

  ### [frame](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudLandmark#/c:objc(cs)FIRVisionCloudLandmark(py)frame)

  `
  `  
  A rectangle image region to which this landmark belongs to (in the view coordinate system).  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) CGRect frame;

- `
  ``
  ``
  `

  ### [locations](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudLandmark#/c:objc(cs)FIRVisionCloudLandmark(py)locations)

  `
  `  
  The location information for the detected landmark. Multiple LocationInfo elements can be present
  because one location may indicate the location of the scene in the image, and another location
  may indicate the location of the place where the image was taken.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSArray<https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionLatitudeLongitude.html *> *locations;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudLandmark#/c:objc(cs)FIRVisionCloudLandmark(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;
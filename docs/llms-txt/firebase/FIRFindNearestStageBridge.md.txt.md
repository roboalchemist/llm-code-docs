# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFindNearestStageBridge.md.txt

# FirebaseFirestore Framework Reference

# FIRFindNearestStageBridge

    @interface FIRFindNearestStageBridge : https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRStageBridge.html
    - (id)initWithField:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldBridge.html *)field
            vectorValue:(FIRVectorValue *)vectorValue
        distanceMeasure:(NSString *)distanceMeasure
                  limit:(NSNumber *_Nullable)limit
          distanceField:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes.html#/c:objc(cs)FIRExprBridge *_Nullable)distanceField;
    @end

Undocumented
- `


  ### [-initWithField:vectorValue:distanceMeasure:limit:distanceField:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFindNearestStageBridge#/c:objc(cs)FIRFindNearestStageBridge(im)initWithField:vectorValue:distanceMeasure:limit:distanceField:)


  ` Undocumented

  #### Declaration

  Objective-C

      - (id)initWithField:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFieldBridge.html *)field
              vectorValue:(FIRVectorValue *)vectorValue
          distanceMeasure:(NSString *)distanceMeasure
                    limit:(NSNumber *_Nullable)limit
            distanceField:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes.html#/c:objc(cs)FIRExprBridge *_Nullable)distanceField;
# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRPipelineBridge.md.txt

# FirebaseFirestore Framework Reference

# FIRPipelineBridge

    @interface FIRPipelineBridge : NSObject

    /** :nodoc: */
    - (id)initWithStages:(NSArray<https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRStageBridge.html *> *)stages db:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore.html *)db;

    - (void)executeWithCompletion:(void (^)(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/__FIRPipelineSnapshotBridge.html *_Nullable result,
                                            NSError *_Nullable error))completion;

    + (NSArray<https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRStageBridge.html *> *)createStageBridgesFromQuery:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery.html *)query;
    @end

Undocumented
- `


  ### [-executeWithCompletion:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRPipelineBridge#/c:objc(cs)FIRPipelineBridge(im)executeWithCompletion:)


  ` Undocumented

  #### Declaration

  Objective-C

      - (void)executeWithCompletion:(void (^)(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/__FIRPipelineSnapshotBridge.html *_Nullable result,
                                              NSError *_Nullable error))completion;

- `


  ### [+createStageBridgesFromQuery:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRPipelineBridge#/c:objc(cs)FIRPipelineBridge(cm)createStageBridgesFromQuery:)


  ` Undocumented

  #### Declaration

  Objective-C

      + (NSArray<https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRStageBridge.html *> *)createStageBridgesFromQuery:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery.html *)query;
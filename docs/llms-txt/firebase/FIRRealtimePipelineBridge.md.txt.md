# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRRealtimePipelineBridge.md.txt

# FirebaseFirestore Framework Reference

# FIRRealtimePipelineBridge

    @interface FIRRealtimePipelineBridge : NSObject

    /** :nodoc: */
    - (id)initWithStages:(NSArray<https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRStageBridge.html *> *)stages db:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore.html *)db;

    - (id<https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Protocols/FIRListenerRegistration.html>)
        addSnapshotListenerWithOptions:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/__FIRPipelineListenOptionsBridge.html *)options
                              listener:
                                  (void (^)(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/__FIRRealtimePipelineSnapshotBridge.html *_Nullable snapshot,
                                            NSError *_Nullable error))listener
        NS_SWIFT_NAME(addSnapshotListener(options:listener:));

    @end

Undocumented
- `


  ### [-addSnapshotListenerWithOptions:listener:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRRealtimePipelineBridge#/c:objc(cs)FIRRealtimePipelineBridge(im)addSnapshotListenerWithOptions:listener:)


  ` Undocumented

  #### Declaration

  Objective-C

      - (id<https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Protocols/FIRListenerRegistration.html>)
          addSnapshotListenerWithOptions:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/__FIRPipelineListenOptionsBridge.html *)options
                                listener:
                                    (void (^)(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/__FIRRealtimePipelineSnapshotBridge.html *_Nullable snapshot,
                                              NSError *_Nullable error))listener
          NS_SWIFT_NAME(addSnapshotListener(options:listener:));
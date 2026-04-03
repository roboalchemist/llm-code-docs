# Source: https://firebase.google.com/docs/reference/ios/firebaseinstanceid/api/reference/Classes/FIRInstanceIDResult.md.txt

# FirebaseInstanceID Framework Reference

# FIRInstanceIDResult


    @interface FIRInstanceIDResult : NSObject <NSCopying>

A class contains the results of InstanceID and token query.
- `
  ``
  ``
  `

  ### [instanceID](https://firebase.google.com/docs/reference/ios/firebaseinstanceid/api/reference/Classes/FIRInstanceIDResult#/c:objc(cs)FIRInstanceIDResult(py)instanceID)

  `
  `  
  An instanceID uniquely identifies the app instance.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly) NSString *_Nonnull instanceID;

- `
  ``
  ``
  `

  ### [token](https://firebase.google.com/docs/reference/ios/firebaseinstanceid/api/reference/Classes/FIRInstanceIDResult#/c:objc(cs)FIRInstanceIDResult(py)token)

  `
  `  
  Undocumented  

  #### Declaration

  Objective-C  

      @property(nonatomic, readonly, copy) NSString *token
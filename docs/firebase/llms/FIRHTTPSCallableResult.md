# Source: https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Classes/FIRHTTPSCallableResult.md.txt

# FirebaseFunctions Framework Reference

# FIRHTTPSCallableResult


    @interface FIRHTTPSCallableResult : NSObject

A `HTTPSCallableResult` contains the result of calling a `HTTPSCallable`.
- `
  ``
  ``
  `

  ### [data](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Classes/FIRHTTPSCallableResult#/c:@M@FirebaseFunctions@objc(cs)FIRHTTPSCallableResult(py)data)

  `
  `  
  The data that was returned from the Callable HTTPS trigger.
  The data is in the form of native objects. For example, if your trigger returned an
  array, this object would be an `Array`. If your trigger returned a JavaScript object with
  keys and values, this object would be an instance of `[String: Any]`.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) id _Nonnull data;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Classes/FIRHTTPSCallableResult#/c:@M@FirebaseFunctions@objc(cs)FIRHTTPSCallableResult(im)init)

  `
  `  
  Undocumented  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init SWIFT_UNAVAILABLE;

- `
  ``
  ``
  `

  ### [+new](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Classes/FIRHTTPSCallableResult#/c:@M@FirebaseFunctions@objc(cs)FIRHTTPSCallableResult(cm)new)

  `
  `  
  Undocumented  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)new SWIFT_UNAVAILABLE_MSG("-init is unavailable");
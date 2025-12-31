# Source: https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/HTTPSCallableResult.md.txt

# FirebaseFunctions Framework Reference

# HTTPSCallableResult

    @objc(FIRHTTPSCallableResult)
    open class HTTPSCallableResult : NSObject

A `HTTPSCallableResult` contains the result of calling a [HTTPSCallable](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/HTTPSCallable.html).
- `
  ``
  ``
  `

  ### [data](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/HTTPSCallableResult#/c:@M@FirebaseFunctions@objc(cs)FIRHTTPSCallableResult(py)data)

  `
  `  
  The data that was returned from the Callable HTTPS trigger.

  The data is in the form of native objects. For example, if your trigger returned an
  array, this object would be an `Array<Any>`. If your trigger returned a JavaScript object with
  keys and values, this object would be an instance of `[String: Any]`.  

  #### Declaration

  Swift  

      @objc
      public let data: Any
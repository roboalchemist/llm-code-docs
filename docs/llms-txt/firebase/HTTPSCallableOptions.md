# Source: https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/HTTPSCallableOptions.md.txt

# FirebaseFunctions Framework Reference

# HTTPSCallableOptions

    @objc(FIRHTTPSCallableOptions)
    public final class HTTPSCallableOptions : NSObject, Sendable

Configuration options for a [HTTPSCallable](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/HTTPSCallable.html) instance.
- `
  ``
  ``
  `

  ### [requireLimitedUseAppCheckTokens](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/HTTPSCallableOptions#/c:@M@FirebaseFunctions@objc(cs)FIRHTTPSCallableOptions(py)requireLimitedUseAppCheckTokens)

  `
  `  
  Whether or not to protect the callable function with a limited-use App Check token.  

  #### Declaration

  Swift  

      @objc
      public let requireLimitedUseAppCheckTokens: Bool

- `
  ``
  ``
  `

  ### [init(requireLimitedUseAppCheckTokens:)](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Classes/HTTPSCallableOptions#/c:@M@FirebaseFunctions@objc(cs)FIRHTTPSCallableOptions(im)initWithRequireLimitedUseAppCheckTokens:)

  `
  `  
  Designated initializer.  

  #### Declaration

  Swift  

      @objc
      public init(requireLimitedUseAppCheckTokens: Bool)

  #### Parameters

  |-----------------------------------------|--------------------------------------------------------------------------------------------------------------|
  | ` `*requireLimitedUseAppCheckTokens*` ` | A boolean used to decide whether or not to protect the callable function with a limited use App Check token. |
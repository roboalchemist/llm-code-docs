# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenImagesBlockedError.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenImagesBlockedError.md.txt

# FirebaseAI Framework Reference

# ImagenImagesBlockedError

    public struct ImagenImagesBlockedError : Error

    extension ImagenImagesBlockedError: CustomNSError

An error that occurs when image generation fails due to all generated images being blocked.

The images may have been blocked due to the specified [ImagenSafetyFilterLevel](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenSafetyFilterLevel.html), the
[ImagenPersonFilterLevel](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenPersonFilterLevel.html), or filtering included in the model. These filter levels may be
adjusted in your [ImagenSafetySettings](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenSafetySettings.html). See the [Responsible AI and usage guidelines for
Imagen](https://cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen)
for more details.
[## CustomNSError Conformance](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenImagesBlockedError#/CustomNSError-Conformance)

- `
  ``
  ``
  `

  ### [errorDomain](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenImagesBlockedError#/s:10Foundation13CustomNSErrorP11errorDomainSSvpZ)

  `
  `  

  #### Declaration

  Swift  

      public static var errorDomain: String { get }

- `
  ``
  ``
  `

  ### [errorCode](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenImagesBlockedError#/s:10Foundation13CustomNSErrorP9errorCodeSivp)

  `
  `  

  #### Declaration

  Swift  

      public var errorCode: Int { get }

- `
  ``
  ``
  `

  ### [errorUserInfo](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenImagesBlockedError#/s:10Foundation13CustomNSErrorP13errorUserInfoSDySSypGvp)

  `
  `  

  #### Declaration

  Swift  

      public var errorUserInfo: [String : Any] { get }
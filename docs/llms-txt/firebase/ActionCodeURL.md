# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeURL.md.txt

# FirebaseAuth Framework Reference

# ActionCodeURL

    @objc(FIRActionCodeURL)
    open class ActionCodeURL : NSObject, @unchecked Sendable

This class will allow developers to easily extract information about out of band links.
- `
  ``
  ``
  `

  ### [apiKey](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeURL#/c:@M@FirebaseAuth@objc(cs)FIRActionCodeURL(py)APIKey)

  `
  `  
  Returns the API key from the link. nil, if not provided.  

  #### Declaration

  Swift  

      @objc(APIKey)
      public let apiKey: String?

- `
  ``
  ``
  `

  ### [operation](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeURL#/c:@M@FirebaseAuth@objc(cs)FIRActionCodeURL(py)operation)

  `
  `  
  Returns the mode of oob action.

  The property will be of [ActionCodeOperation](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/ActionCodeOperation.html) type.
  It will return `.unknown` if no oob action is provided.  

  #### Declaration

  Swift  

      @objc
      public let operation: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/ActionCodeOperation.html

- `
  ``
  ``
  `

  ### [code](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeURL#/c:@M@FirebaseAuth@objc(cs)FIRActionCodeURL(py)code)

  `
  `  
  Returns the email action code from the link. nil, if not provided.  

  #### Declaration

  Swift  

      @objc
      public let code: String?

- `
  ``
  ``
  `

  ### [continueURL](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeURL#/c:@M@FirebaseAuth@objc(cs)FIRActionCodeURL(py)continueURL)

  `
  `  
  Returns the continue URL from the link. nil, if not provided.  

  #### Declaration

  Swift  

      @objc
      public let continueURL: URL?

- `
  ``
  ``
  `

  ### [languageCode](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeURL#/c:@M@FirebaseAuth@objc(cs)FIRActionCodeURL(py)languageCode)

  `
  `  
  Returns the language code from the link. nil, if not provided.  

  #### Declaration

  Swift  

      @objc
      public let languageCode: String?

- `
  ``
  ``
  `

  ### [init(link:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeURL#/c:@M@FirebaseAuth@objc(cs)FIRActionCodeURL(im)actionCodeURLWithLink:)

  `
  `  
  Construct an `ActionCodeURL` from an out of band link (e.g. email link).  

  #### Declaration

  Swift  

      @objc(actionCodeURLWithLink:)
      public init?(link: String)

  #### Parameters

  |--------------|------------------------------------------------------------|
  | ` `*link*` ` | The oob link string used to construct the action code URL. |

  #### Return Value

  The ActionCodeURL object constructed based on the oob link provided.
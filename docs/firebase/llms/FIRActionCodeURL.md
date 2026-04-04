# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRActionCodeURL.md.txt

# FirebaseAuth Framework Reference

# FIRActionCodeURL


    @interface FIRActionCodeURL : NSObject

This class will allow developers to easily extract information about out of band links.
- `
  ``
  ``
  `

  ### [APIKey](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRActionCodeURL#/c:objc(cs)FIRActionCodeURL(py)APIKey)

  `
  `  
  Returns the API key from the link. nil, if not provided.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nullable) NSString *APIKey;

- `
  ``
  ``
  `

  ### [operation](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRActionCodeURL#/c:objc(cs)FIRActionCodeURL(py)operation)

  `
  `  
  Returns the mode of oob action. The property will be of [FIRActionCodeOperation](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRActionCodeOperation.html) type.
  It will return `FIRActionCodeOperationUnknown` if no oob action is provided.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Enums/FIRActionCodeOperation.html operation;

- `
  ``
  ``
  `

  ### [code](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRActionCodeURL#/c:objc(cs)FIRActionCodeURL(py)code)

  `
  `  
  Returns the email action code from the link. nil, if not provided.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nullable) NSString *code;

- `
  ``
  ``
  `

  ### [continueURL](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRActionCodeURL#/c:objc(cs)FIRActionCodeURL(py)continueURL)

  `
  `  
  Returns the continue URL from the link. nil, if not provided.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nullable) NSURL *continueURL;

- `
  ``
  ``
  `

  ### [languageCode](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRActionCodeURL#/c:objc(cs)FIRActionCodeURL(py)languageCode)

  `
  `  
  Returns the language code from the link. nil, if not provided.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nullable) NSString *languageCode;

- `
  ``
  ``
  `

  ### [+actionCodeURLWithLink:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRActionCodeURL#/c:objc(cs)FIRActionCodeURL(cm)actionCodeURLWithLink:)

  `
  `  
  Construct an `ActionCodeURL` from an out of band link (e.g. email link).  

  #### Declaration

  Objective-C  

      + (nullable instancetype)actionCodeURLWithLink:(nonnull NSString *)link;

  #### Parameters

  |--------------|------------------------------------------------------------|
  | ` `*link*` ` | The oob link string used to construct the action code URL. |

  #### Return Value

  The `ActionCodeURL` object constructed based on the oob link provided.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRActionCodeURL#/c:objc(cs)FIRActionCodeURL(im)init)

  `
  `  
  Please use `init(link:)` in Swift or `actionCodeURLWithLink:` in Objective-C
  instead.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;
# Source: https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Type-Definitions.md.txt

# FirebaseDynamicLinks Framework Reference

# Type Definitions

The following type definitions are available globally.
- `


  ### [FIRDynamicLinkShortenerCompletion](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Type-Definitions#/c:FDLURLComponents.h@T@FIRDynamicLinkShortenerCompletion)


  ` The definition of the completion block used by URL shortener.

  #### Parameters

  |---|---|
  | ` shortURL ` | Shortened URL. |
  | ` warnings ` | Warnings that describe usability or function limitations of the generated short link. Usually presence of warnings means parameters format error, parameters value error or missing parameter. |
  | ` error ` | Error if URL can't be shortened. |

- `


  ### [FIRDynamicLinkResolverHandler](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Type-Definitions#/c:FIRDynamicLinksCommon.h@T@FIRDynamicLinkResolverHandler)


  ` The definition of the block used by \|resolveShortLink:completion:\|
- `


  ### [FIRDynamicLinkUniversalLinkHandler](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Type-Definitions#/c:FIRDynamicLinksCommon.h@T@FIRDynamicLinkUniversalLinkHandler)


  ` The definition of the block used by \|handleUniversalLink:completion:\|
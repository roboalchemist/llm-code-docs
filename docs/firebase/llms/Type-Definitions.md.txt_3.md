# Source: https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Type-Definitions.md.txt

# FirebaseDynamicLinks Framework Reference

# Type Definitions

The following type definitions are available globally.
- `


  ### [FIRDynamicLinkShortenerCompletion](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Type-Definitions#/c:FDLURLComponents.h@T@FIRDynamicLinkShortenerCompletion)


  ` The definition of the completion block used by URL shortener.

  #### Declaration

  Objective-C

      typedef void (^FIRDynamicLinkShortenerCompletion)(
          NSURL *_Nullable, NSArray<NSString *> *_Nullable, NSError *_Nullable)

  #### Parameters

  |---|---|
  | ` shortURL ` | Shortened URL. |
  | ` warnings ` | Warnings that describe usability or function limitations of the generated short link. Usually presence of warnings means parameters format error, parameters value error or missing parameter. |
  | ` error ` | Error if URL can't be shortened. |

- `


  ### [FIRDynamicLinkResolverHandler](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Type-Definitions#/c:FIRDynamicLinksCommon.h@T@FIRDynamicLinkResolverHandler)


  ` The definition of the block used by \|resolveShortLink:completion:\|

  #### Declaration

  Objective-C

      typedef void (^FIRDynamicLinkResolverHandler)(NSURL *_Nullable,
                                                    NSError *_Nullable)

- `


  ### [FIRDynamicLinkUniversalLinkHandler](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Type-Definitions#/c:FIRDynamicLinksCommon.h@T@FIRDynamicLinkUniversalLinkHandler)


  ` The definition of the block used by \|handleUniversalLink:completion:\|

  #### Declaration

  Objective-C

      typedef void (^FIRDynamicLinkUniversalLinkHandler)(https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLink *_Nullable,
                                                         NSError *_Nullable)
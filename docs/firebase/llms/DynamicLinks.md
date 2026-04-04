# Source: https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinks.md.txt

# FirebaseDynamicLinks Framework Reference

# DynamicLinks

Deprecated

Firebase Dynamic Links is deprecated and the service will shut down on August 25, 2025.  

    class DynamicLinks : NSObject

A class that checks for pending Dynamic Links and parses URLs.
This class is available on iOS only.
- `
  ``
  ``
  `

  ### [dynamicLinks()](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinks#/c:objc(cs)FIRDynamicLinks(cm)dynamicLinks)

  `
  `  
  Deprecated

  Firebase Dynamic Links is deprecated and the service will shut down on August 25, 2025.  
  Shared instance of FIRDynamicLinks.  

  #### Declaration

  Swift  

      class func dynamicLinks() -> Self

  #### Return Value

  Shared instance of FIRDynamicLinks.
- `
  ``
  ``
  `

  ### [shouldHandleDynamicLink(fromCustomSchemeURL:)](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinks#/c:objc(cs)FIRDynamicLinks(im)shouldHandleDynamicLinkFromCustomSchemeURL:)

  `
  `  
  Deprecated

  Firebase Dynamic Links is deprecated and the service will shut down on August 25, 2025.  
  Determine whether FIRDynamicLinks should handle the given URL. This does not
  guarantee that \|dynamicLinkFromCustomSchemeURL:\| will return a non-nil value, but it means
  the client should not attempt to handle the URL.  

  #### Declaration

  Swift  

      func shouldHandleDynamicLink(fromCustomSchemeURL url: URL) -> Bool

  #### Parameters

  |-------------|--------------------|
  | ` `*url*` ` | Custom scheme URL. |

  #### Return Value

  Whether the URL can be handled by FIRDynamicLinks.
- `
  ``
  ``
  `

  ### [dynamicLink(fromCustomSchemeURL:)](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinks#/c:objc(cs)FIRDynamicLinks(im)dynamicLinkFromCustomSchemeURL:)

  `
  `  
  Deprecated

  Firebase Dynamic Links is deprecated and the service will shut down on August 25, 2025.  
  Get a Dynamic Link from a custom scheme URL. This method parses URLs with a custom
  scheme, for instance, "comgoogleapp://google/link?deep_link_id=abc123". It is suggested to
  call it inside your \|UIApplicationDelegate\|'s
  \|application:openURL:sourceApplication:annotation\| and \|application:openURL:options:\|
  methods.  

  #### Declaration

  Swift  

      func dynamicLink(fromCustomSchemeURL url: URL) -> https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLink.html?

  #### Parameters

  |-------------|--------------------|
  | ` `*url*` ` | Custom scheme URL. |

  #### Return Value

  Dynamic Link object if the URL is valid and has link parameter, otherwise nil.
- `
  ``
  ``
  `

  ### [dynamicLink(fromUniversalLink:)](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinks#/c:objc(cs)FIRDynamicLinks(im)dynamicLinkFromUniversalLinkURL:completion:)

  `
  `  
  Deprecated

  Firebase Dynamic Links is deprecated and the service will shut down on August 25, 2025.  
  Get a Dynamic Link from a universal link URL. This method parses universal link
  URLs, for instance,
  "[https://example.page.link?link=https://www.google.com\&ibi=com.google.app\&ius=comgoogleapp](https://example.page.link?link=https://www.google.com&ibi=com.google.app&ius=comgoogleapp)".
  It is suggested to call it inside your \|UIApplicationDelegate\|'s
  \|application:continueUserActivity:restorationHandler:\| method.  

  #### Declaration

  Swift  

      func dynamicLink(fromUniversalLink url: URL) async throws -> https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLink.html

  #### Parameters

  |--------------------|-------------------------------------------------------------------------------------------------|
  | ` `*url*` `        | Custom scheme URL.                                                                              |
  | ` `*completion*` ` | A block that handles the outcome of attempting to get a Dynamic Link from a universal link URL. |

- `
  ``
  ``
  `

  ### [dynamicLink(fromUniversalLink:)](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinks#/c:objc(cs)FIRDynamicLinks(im)dynamicLinkFromUniversalLinkURL:)

  `
  `  
  Deprecated

  Firebase Dynamic Links is deprecated and the service will shut down on August 25, 2025.  
  Get a Dynamic Link from a universal link URL. This method parses universal link
  URLs, for instance,
  "[https://example.page.link?link=https://www.google.com\&ibi=com.google.app\&ius=comgoogleapp](https://example.page.link?link=https://www.google.com&ibi=com.google.app&ius=comgoogleapp)".
  It is suggested to call it inside your \|UIApplicationDelegate\|'s
  \|application:continueUserActivity:restorationHandler:\| method.  

  #### Declaration

  Swift  

      func dynamicLink(fromUniversalLink url: URL) -> https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLink.html?

  #### Parameters

  |-------------|--------------------|
  | ` `*url*` ` | Custom scheme URL. |

  #### Return Value

  Dynamic Link object if the URL is valid and has link parameter, otherwise nil.
- `
  ``
  ``
  `

  ### [handleUniversalLink(_:completion:)](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinks#/c:objc(cs)FIRDynamicLinks(im)handleUniversalLink:completion:)

  `
  `  
  Deprecated

  Firebase Dynamic Links is deprecated and the service will shut down on August 25, 2025.  
  Convenience method to handle a Universal Link whether it is long or short.  

  #### Declaration

  Swift  

      func handleUniversalLink(_ url: URL, completion: @escaping (https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLink.html?, (any Error)?) -> Void) -> Bool

  #### Parameters

  |--------------------|----------------------------------------------------------------------------|
  | ` `*url*` `        | A Universal Link URL.                                                      |
  | ` `*completion*` ` | A block that handles the outcome of attempting to create a FIRDynamicLink. |

  #### Return Value

  YES if FIRDynamicLinks is handling the link, otherwise, NO.
- `
  ``
  ``
  `

  ### [resolveShortLink(_:)](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinks#/c:objc(cs)FIRDynamicLinks(im)resolveShortLink:completion:)

  `
  `  
  Deprecated

  Firebase Dynamic Links is deprecated and the service will shut down on August 25, 2025.  
  Retrieves the details of the Dynamic Link that the shortened URL represents.  

  #### Declaration

  Swift  

      func resolveShortLink(_ url: URL) async throws -> URL

  #### Parameters

  |--------------------|----------------------------------|
  | ` `*url*` `        | A Short Dynamic Link.            |
  | ` `*completion*` ` | Block to be run upon completion. |

- `
  ``
  ``
  `

  ### [matchesShortLinkFormat(_:)](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinks#/c:objc(cs)FIRDynamicLinks(im)matchesShortLinkFormat:)

  `
  `  
  Deprecated

  Firebase Dynamic Links is deprecated and the service will shut down on August 25, 2025.  
  Determines if a given URL matches the given short Dynamic Link format.  

  #### Declaration

  Swift  

      func matchesShortLinkFormat(_ url: URL) -> Bool

  #### Parameters

  |-------------|--------|
  | ` `*url*` ` | A URL. |

  #### Return Value

  YES if the URL is a short Dynamic Link, otherwise, NO.
- `
  ``
  ``
  `

  ### [performDiagnostics()](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinks#/c:objc(cs)FIRDynamicLinks(cm)performDiagnosticsWithCompletion:)

  `
  `  
  Deprecated

  Firebase Dynamic Links is deprecated and the service will shut down on August 25, 2025.  
  Performs basic FDL self diagnostic. Method effect on startup latency is quite small
  and no user-visible UI is presented. This method should be used for debugging purposes.
  App developers are encouraged to include output, generated by this method, to the support
  requests sent to Firebase support.  

  #### Declaration

  Swift  

      class func performDiagnostics() async -> (String, Bool)

  #### Parameters

  |---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*completionHandler*` ` | Handler that will be called when diagnostic completes. If value of the completionHandler is nil than diagnostic output will be printed to the standard output. diagnosticOutput String that includes diagnostic information. hasErrors Param will have YES value if diagnostic method detected error, NO otherwise. |
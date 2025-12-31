# Source: https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinks.md.txt

# FirebaseDynamicLinks Framework Reference

# FIRDynamicLinks

Deprecated

Firebase Dynamic Links is deprecated and the service will shut down on August 25, 2025.  


    @interface FIRDynamicLinks : NSObject

A class that checks for pending Dynamic Links and parses URLs.
This class is available on iOS only.
- `
  ``
  ``
  `

  ### [+dynamicLinks](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinks#/c:objc(cs)FIRDynamicLinks(cm)dynamicLinks)

  `
  `  
  Deprecated

  Firebase Dynamic Links is deprecated and the service will shut down on August 25, 2025.  
  Shared instance of FIRDynamicLinks.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)dynamicLinks;

  #### Return Value

  Shared instance of FIRDynamicLinks.
- `
  ``
  ``
  `

  ### [-shouldHandleDynamicLinkFromCustomSchemeURL:](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinks#/c:objc(cs)FIRDynamicLinks(im)shouldHandleDynamicLinkFromCustomSchemeURL:)

  `
  `  
  Deprecated

  Firebase Dynamic Links is deprecated and the service will shut down on August 25, 2025.  
  Determine whether FIRDynamicLinks should handle the given URL. This does not
  guarantee that \|dynamicLinkFromCustomSchemeURL:\| will return a non-nil value, but it means
  the client should not attempt to handle the URL.  

  #### Declaration

  Objective-C  

      - (BOOL)shouldHandleDynamicLinkFromCustomSchemeURL:(nonnull NSURL *)url;

  #### Parameters

  |-------------|--------------------|
  | ` `*url*` ` | Custom scheme URL. |

  #### Return Value

  Whether the URL can be handled by FIRDynamicLinks.
- `
  ``
  ``
  `

  ### [-dynamicLinkFromCustomSchemeURL:](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinks#/c:objc(cs)FIRDynamicLinks(im)dynamicLinkFromCustomSchemeURL:)

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

  Objective-C  

      - (nullable https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLink.html *)dynamicLinkFromCustomSchemeURL:
          (nonnull NSURL *)url;

  #### Parameters

  |-------------|--------------------|
  | ` `*url*` ` | Custom scheme URL. |

  #### Return Value

  Dynamic Link object if the URL is valid and has link parameter, otherwise nil.
- `
  ``
  ``
  `

  ### [-dynamicLinkFromUniversalLinkURL:completion:](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinks#/c:objc(cs)FIRDynamicLinks(im)dynamicLinkFromUniversalLinkURL:completion:)

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

  Objective-C  

      - (void)dynamicLinkFromUniversalLinkURL:(nonnull NSURL *)url
                                   completion:(nonnull void (^)(
                                                  https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLink.html *_Nullable,
                                                  NSError *_Nullable))completion;

  #### Parameters

  |--------------------|-------------------------------------------------------------------------------------------------|
  | ` `*url*` `        | Custom scheme URL.                                                                              |
  | ` `*completion*` ` | A block that handles the outcome of attempting to get a Dynamic Link from a universal link URL. |

- `
  ``
  ``
  `

  ### [-dynamicLinkFromUniversalLinkURL:](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinks#/c:objc(cs)FIRDynamicLinks(im)dynamicLinkFromUniversalLinkURL:)

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

  Objective-C  

      - (nullable https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLink.html *)dynamicLinkFromUniversalLinkURL:
          (nonnull NSURL *)url;

  #### Parameters

  |-------------|--------------------|
  | ` `*url*` ` | Custom scheme URL. |

  #### Return Value

  Dynamic Link object if the URL is valid and has link parameter, otherwise nil.
- `
  ``
  ``
  `

  ### [-handleUniversalLink:completion:](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinks#/c:objc(cs)FIRDynamicLinks(im)handleUniversalLink:completion:)

  `
  `  
  Deprecated

  Firebase Dynamic Links is deprecated and the service will shut down on August 25, 2025.  
  Convenience method to handle a Universal Link whether it is long or short.  

  #### Declaration

  Objective-C  

      - (BOOL)handleUniversalLink:(nonnull NSURL *)url
                       completion:(nonnull void (^)(https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLink.html *_Nullable,
                                                    NSError *_Nullable))completion;

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

  ### [-resolveShortLink:completion:](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinks#/c:objc(cs)FIRDynamicLinks(im)resolveShortLink:completion:)

  `
  `  
  Deprecated

  Firebase Dynamic Links is deprecated and the service will shut down on August 25, 2025.  
  Retrieves the details of the Dynamic Link that the shortened URL represents.  

  #### Declaration

  Objective-C  

      - (void)resolveShortLink:(nonnull NSURL *)url
                    completion:(nonnull void (^)(NSURL *_Nullable,
                                                 NSError *_Nullable))completion;

  #### Parameters

  |--------------------|----------------------------------|
  | ` `*url*` `        | A Short Dynamic Link.            |
  | ` `*completion*` ` | Block to be run upon completion. |

- `
  ``
  ``
  `

  ### [-matchesShortLinkFormat:](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinks#/c:objc(cs)FIRDynamicLinks(im)matchesShortLinkFormat:)

  `
  `  
  Deprecated

  Firebase Dynamic Links is deprecated and the service will shut down on August 25, 2025.  
  Determines if a given URL matches the given short Dynamic Link format.  

  #### Declaration

  Objective-C  

      - (BOOL)matchesShortLinkFormat:(nonnull NSURL *)url;

  #### Parameters

  |-------------|--------|
  | ` `*url*` ` | A URL. |

  #### Return Value

  YES if the URL is a short Dynamic Link, otherwise, NO.
- `
  ``
  ``
  `

  ### [+performDiagnosticsWithCompletion:](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinks#/c:objc(cs)FIRDynamicLinks(cm)performDiagnosticsWithCompletion:)

  `
  `  
  Deprecated

  Firebase Dynamic Links is deprecated and the service will shut down on August 25, 2025.  
  Performs basic FDL self diagnostic. Method effect on startup latency is quite small
  and no user-visible UI is presented. This method should be used for debugging purposes.
  App developers are encouraged to include output, generated by this method, to the support
  requests sent to Firebase support.  

  #### Declaration

  Objective-C  

      + (void)performDiagnosticsWithCompletion:
          (void (^_Nullable)(NSString *_Nonnull, BOOL))completionHandler;

  #### Parameters

  |---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*completionHandler*` ` | Handler that will be called when diagnostic completes. If value of the completionHandler is nil than diagnostic output will be printed to the standard output. diagnosticOutput String that includes diagnostic information. hasErrors Param will have YES value if diagnostic method detected error, NO otherwise. |
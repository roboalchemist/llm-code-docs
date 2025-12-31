# Source: https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkComponents.md.txt

# FirebaseDynamicLinks Framework Reference

# DynamicLinkComponents

    class DynamicLinkComponents : NSObject

The class used for Dynamic Link URL generation; supports creation of short and long
Dynamic Link URLs. Short URLs will have a domain and a randomized path; long URLs will have a
domain and a query that contains all of the Dynamic Link parameters.
- `
  ``
  ``
  `

  ### [analyticsParameters](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkComponents#/c:objc(cs)FIRDynamicLinkComponents(py)analyticsParameters)

  `
  `  
  Applies Analytics parameters to a generated Dynamic Link URL.  

  #### Declaration

  Swift  

      var analyticsParameters: https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkGoogleAnalyticsParameters.html? { get set }

- `
  ``
  ``
  `

  ### [socialMetaTagParameters](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkComponents#/c:objc(cs)FIRDynamicLinkComponents(py)socialMetaTagParameters)

  `
  `  
  Applies Social Meta Tag parameters to a generated Dynamic Link URL.  

  #### Declaration

  Swift  

      var socialMetaTagParameters: https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkSocialMetaTagParameters.html? { get set }

- `
  ``
  ``
  `

  ### [iOSParameters](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkComponents#/c:objc(cs)FIRDynamicLinkComponents(py)iOSParameters)

  `
  `  
  Applies iOS parameters to a generated Dynamic Link URL.  

  #### Declaration

  Swift  

      var iOSParameters: https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkIOSParameters.html? { get set }

- `
  ``
  ``
  `

  ### [iTunesConnectParameters](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkComponents#/c:objc(cs)FIRDynamicLinkComponents(py)iTunesConnectParameters)

  `
  `  
  Applies iTunes Connect parameters to a generated Dynamic Link URL.  

  #### Declaration

  Swift  

      var iTunesConnectParameters: https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkItunesConnectAnalyticsParameters.html? { get set }

- `
  ``
  ``
  `

  ### [androidParameters](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkComponents#/c:objc(cs)FIRDynamicLinkComponents(py)androidParameters)

  `
  `  
  Applies Android parameters to a generated Dynamic Link URL.  

  #### Declaration

  Swift  

      var androidParameters: https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkAndroidParameters.html? { get set }

- `
  ``
  ``
  `

  ### [navigationInfoParameters](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkComponents#/c:objc(cs)FIRDynamicLinkComponents(py)navigationInfoParameters)

  `
  `  
  Applies Navigation Info parameters to a generated Dynamic Link URL.  

  #### Declaration

  Swift  

      var navigationInfoParameters: https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkNavigationInfoParameters.html? { get set }

- `
  ``
  ``
  `

  ### [otherPlatformParameters](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkComponents#/c:objc(cs)FIRDynamicLinkComponents(py)otherPlatformParameters)

  `
  `  
  Applies Other platform parameters to a generated Dynamic Link URL.  

  #### Declaration

  Swift  

      var otherPlatformParameters: https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkOtherPlatformParameters.html? { get set }

- `
  ``
  ``
  `

  ### [options](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkComponents#/c:objc(cs)FIRDynamicLinkComponents(py)options)

  `
  `  
  Defines behavior for generating Dynamic Link URLs.  

  #### Declaration

  Swift  

      var options: https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkComponentsOptions.html? { get set }

- `
  ``
  ``
  `

  ### [link](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkComponents#/c:objc(cs)FIRDynamicLinkComponents(py)link)

  `
  `  
  The link the target app will open. You can specify any URL the app can handle, such as
  a link to the app's content, or a URL that initiates some app-specific logic such as
  crediting the user with a coupon, or displaying a specific welcome screen. This link must be
  a well-formatted URL, be properly URL-encoded, and use the HTTP or HTTPS scheme.  

  #### Declaration

  Swift  

      var link: URL { get set }

- `
  ``
  ``
  `

  ### [domain](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkComponents#/c:objc(cs)FIRDynamicLinkComponents(py)domain)

  `
  `  
  The Firebase project's Dynamic Links domain. You can find this value in the Dynamic
  Links section of the Firebase console.
  <https://console.firebase.google.com/>  

  #### Declaration

  Swift  

      var domain: String? { get set }

- `
  ``
  ``
  `

  ### [url](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkComponents#/c:objc(cs)FIRDynamicLinkComponents(py)url)

  `
  `  
  A generated long Dynamic Link URL.  

  #### Declaration

  Swift  

      var url: URL? { get }

- `
  ``
  ``
  `

  ### [+componentsWithLink:domainURIPrefix:](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkComponents#/c:objc(cs)FIRDynamicLinkComponents(cm)componentsWithLink:domainURIPrefix:)

  `
  `  
  Generates a Dynamic Link URL components object with the minimum necessary parameters
  set to generate a fully-functional Dynamic Link.  

  #### Parameters

  |-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*link*` `            | Deep link to be stored in created Dynamic link. This link also called "payload" of the Dynamic link.                                                                                                    |
  | ` `*domainURIPrefix*` ` | Domain URI Prefix of your App. This value must be your assigned domain from the Firebase console. (e.g. <https://xyz.page.link>) The domain URI prefix must start with a valid HTTPS scheme (https://). |

  #### Return Value

  Returns an instance of FIRDynamicLinkComponents if the parameters succeed validation,
  else returns nil.
- `
  ``
  ``
  `

  ### [init(link:domainURIPrefix:)](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkComponents#/c:objc(cs)FIRDynamicLinkComponents(im)initWithLink:domainURIPrefix:)

  `
  `  
  Generates a Dynamic Link URL components object with the minimum necessary parameters
  set to generate a fully-functional Dynamic Link.  

  #### Declaration

  Swift  

      init?(link: URL, domainURIPrefix: String)

  #### Parameters

  |-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*link*` `            | Deep link to be stored in created Dynamic link. This link also called "payload" of the Dynamic link.                                                                                                    |
  | ` `*domainURIPrefix*` ` | Domain URI Prefix of your App. This value must be your assigned domain from the Firebase console. (e.g. <https://xyz.page.link>) The domain URI prefix must start with a valid HTTPS scheme (https://). |

  #### Return Value

  Returns an instance of FIRDynamicLinkComponents if the parameters succeed validation,
  else returns nil.
- `
  ``
  ``
  `

  ### [shortenURL(_:options:)](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkComponents#/c:objc(cs)FIRDynamicLinkComponents(cm)shortenURL:options:completion:)

  `
  `  
  Shortens a Dynamic Link URL. This method may be used for shortening a custom URL that
  was not generated using FIRDynamicLinkComponents.  

  #### Declaration

  Swift  

      class func shortenURL(_ url: URL, options: https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkComponentsOptions.html?) async throws -> (URL, [String])

  #### Parameters

  |--------------------|--------------------------------------------------------------------------------------------------------------------------------|
  | ` `*url*` `        | A properly-formatted long Dynamic Link URL.                                                                                    |
  | ` `*completion*` ` | A block to be executed upon completion of the shortening attempt. It is guaranteed to be executed once and on the main thread. |

- `
  ``
  ``
  `

  ### [shorten()](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkComponents#/c:objc(cs)FIRDynamicLinkComponents(im)shortenWithCompletion:)

  `
  `  
  Generates a short Dynamic Link URL using all set parameters.  

  #### Declaration

  Swift  

      func shorten() async throws -> (URL, [String])

  #### Parameters

  |--------------------|--------------------------------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | A block to be executed upon completion of the shortening attempt. It is guaranteed to be executed once and on the main thread. |
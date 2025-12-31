# Source: https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkComponents.md.txt

# FirebaseDynamicLinks Framework Reference

# FIRDynamicLinkComponents


    @interface FIRDynamicLinkComponents : NSObject

The class used for Dynamic Link URL generation; supports creation of short and long
Dynamic Link URLs. Short URLs will have a domain and a randomized path; long URLs will have a
domain and a query that contains all of the Dynamic Link parameters.
- `
  ``
  ``
  `

  ### [analyticsParameters](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkComponents#/c:objc(cs)FIRDynamicLinkComponents(py)analyticsParameters)

  `
  `  
  Applies Analytics parameters to a generated Dynamic Link URL.  

  #### Declaration

  Objective-C  

      @property (nonatomic, nullable) https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkGoogleAnalyticsParameters.html *analyticsParameters;

- `
  ``
  ``
  `

  ### [socialMetaTagParameters](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkComponents#/c:objc(cs)FIRDynamicLinkComponents(py)socialMetaTagParameters)

  `
  `  
  Applies Social Meta Tag parameters to a generated Dynamic Link URL.  

  #### Declaration

  Objective-C  

      @property (nonatomic, nullable) https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkSocialMetaTagParameters.html *socialMetaTagParameters;

- `
  ``
  ``
  `

  ### [iOSParameters](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkComponents#/c:objc(cs)FIRDynamicLinkComponents(py)iOSParameters)

  `
  `  
  Applies iOS parameters to a generated Dynamic Link URL.  

  #### Declaration

  Objective-C  

      @property (nonatomic, nullable) https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkIOSParameters.html *iOSParameters;

- `
  ``
  ``
  `

  ### [iTunesConnectParameters](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkComponents#/c:objc(cs)FIRDynamicLinkComponents(py)iTunesConnectParameters)

  `
  `  
  Applies iTunes Connect parameters to a generated Dynamic Link URL.  

  #### Declaration

  Objective-C  

      @property (nonatomic, nullable) https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkItunesConnectAnalyticsParameters.html *iTunesConnectParameters;

- `
  ``
  ``
  `

  ### [androidParameters](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkComponents#/c:objc(cs)FIRDynamicLinkComponents(py)androidParameters)

  `
  `  
  Applies Android parameters to a generated Dynamic Link URL.  

  #### Declaration

  Objective-C  

      @property (nonatomic, nullable) https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkAndroidParameters.html *androidParameters;

- `
  ``
  ``
  `

  ### [navigationInfoParameters](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkComponents#/c:objc(cs)FIRDynamicLinkComponents(py)navigationInfoParameters)

  `
  `  
  Applies Navigation Info parameters to a generated Dynamic Link URL.  

  #### Declaration

  Objective-C  

      @property (nonatomic, nullable) https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkNavigationInfoParameters.html *navigationInfoParameters;

- `
  ``
  ``
  `

  ### [otherPlatformParameters](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkComponents#/c:objc(cs)FIRDynamicLinkComponents(py)otherPlatformParameters)

  `
  `  
  Applies Other platform parameters to a generated Dynamic Link URL.  

  #### Declaration

  Objective-C  

      @property (nonatomic, nullable) https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkOtherPlatformParameters.html *otherPlatformParameters;

- `
  ``
  ``
  `

  ### [options](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkComponents#/c:objc(cs)FIRDynamicLinkComponents(py)options)

  `
  `  
  Defines behavior for generating Dynamic Link URLs.  

  #### Declaration

  Objective-C  

      @property (nonatomic, nullable) https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkComponentsOptions.html *options;

- `
  ``
  ``
  `

  ### [link](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkComponents#/c:objc(cs)FIRDynamicLinkComponents(py)link)

  `
  `  
  The link the target app will open. You can specify any URL the app can handle, such as
  a link to the app's content, or a URL that initiates some app-specific logic such as
  crediting the user with a coupon, or displaying a specific welcome screen. This link must be
  a well-formatted URL, be properly URL-encoded, and use the HTTP or HTTPS scheme.  

  #### Declaration

  Objective-C  

      @property (nonatomic) NSURL *_Nonnull link;

- `
  ``
  ``
  `

  ### [domain](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkComponents#/c:objc(cs)FIRDynamicLinkComponents(py)domain)

  `
  `  
  The Firebase project's Dynamic Links domain. You can find this value in the Dynamic
  Links section of the Firebase console.
  <https://console.firebase.google.com/>  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSString *domain;

- `
  ``
  ``
  `

  ### [url](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkComponents#/c:objc(cs)FIRDynamicLinkComponents(py)url)

  `
  `  
  A generated long Dynamic Link URL.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSURL *url;

- `
  ``
  ``
  `

  ### [+componentsWithLink:domainURIPrefix:](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkComponents#/c:objc(cs)FIRDynamicLinkComponents(cm)componentsWithLink:domainURIPrefix:)

  `
  `  
  Generates a Dynamic Link URL components object with the minimum necessary parameters
  set to generate a fully-functional Dynamic Link.  

  #### Declaration

  Objective-C  

      + (nullable instancetype)componentsWithLink:(nonnull NSURL *)link
                                  domainURIPrefix:(nonnull NSString *)domainURIPrefix;

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

  ### [-initWithLink:domainURIPrefix:](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkComponents#/c:objc(cs)FIRDynamicLinkComponents(im)initWithLink:domainURIPrefix:)

  `
  `  
  Generates a Dynamic Link URL components object with the minimum necessary parameters
  set to generate a fully-functional Dynamic Link.  

  #### Declaration

  Objective-C  

      - (nullable instancetype)initWithLink:(nonnull NSURL *)link
                            domainURIPrefix:(nonnull NSString *)domainURIPrefix;

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

  ### [+shortenURL:options:completion:](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkComponents#/c:objc(cs)FIRDynamicLinkComponents(cm)shortenURL:options:completion:)

  `
  `  
  Shortens a Dynamic Link URL. This method may be used for shortening a custom URL that
  was not generated using FIRDynamicLinkComponents.  

  #### Declaration

  Objective-C  

      + (void)shortenURL:(nonnull NSURL *)url
                 options:(https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkComponentsOptions.html *_Nullable)options
              completion:(nonnull void (^)(NSURL *_Nullable,
                                           NSArray<NSString *> *_Nullable,
                                           NSError *_Nullable))completion;

  #### Parameters

  |--------------------|--------------------------------------------------------------------------------------------------------------------------------|
  | ` `*url*` `        | A properly-formatted long Dynamic Link URL.                                                                                    |
  | ` `*completion*` ` | A block to be executed upon completion of the shortening attempt. It is guaranteed to be executed once and on the main thread. |

- `
  ``
  ``
  `

  ### [-shortenWithCompletion:](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkComponents#/c:objc(cs)FIRDynamicLinkComponents(im)shortenWithCompletion:)

  `
  `  
  Generates a short Dynamic Link URL using all set parameters.  

  #### Declaration

  Objective-C  

      - (void)shortenWithCompletion:(nonnull void (^)(NSURL *_Nullable,
                                                      NSArray<NSString *> *_Nullable,
                                                      NSError *_Nullable))completion;

  #### Parameters

  |--------------------|--------------------------------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | A block to be executed upon completion of the shortening attempt. It is guaranteed to be executed once and on the main thread. |
# Source: https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes.md.txt

# FirebaseDynamicLinks Framework Reference

# Classes

The following classes are available globally.
- `


  ### [FIRDynamicLinkGoogleAnalyticsParameters](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkGoogleAnalyticsParameters)


  ` The Dynamic Link analytics parameters.

  #### Declaration

  Objective-C


      @interface FIRDynamicLinkGoogleAnalyticsParameters : NSObject

- `


  ### [FIRDynamicLinkIOSParameters](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkIOSParameters)


  ` The Dynamic Link iOS parameters.

  #### Declaration

  Objective-C


      @interface FIRDynamicLinkIOSParameters : NSObject

- `


  ### [FIRDynamicLinkItunesConnectAnalyticsParameters](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkItunesConnectAnalyticsParameters)


  ` The Dynamic Link iTunes Connect parameters.

  #### Declaration

  Objective-C


      @interface FIRDynamicLinkItunesConnectAnalyticsParameters : NSObject

- `


  ### [FIRDynamicLinkAndroidParameters](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkAndroidParameters)


  ` The Dynamic Link Android parameters.

  #### Declaration

  Objective-C


      @interface FIRDynamicLinkAndroidParameters : NSObject

- `


  ### [FIRDynamicLinkSocialMetaTagParameters](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkSocialMetaTagParameters)


  ` The Dynamic Link Social Meta Tag parameters.

  #### Declaration

  Objective-C


      @interface FIRDynamicLinkSocialMetaTagParameters : NSObject

- `


  ### [FIRDynamicLinkNavigationInfoParameters](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkNavigationInfoParameters)


  ` Options class for defining navigation behavior of the Dynamic Link.

  #### Declaration

  Objective-C


      @interface FIRDynamicLinkNavigationInfoParameters : NSObject

- `


  ### [FIRDynamicLinkOtherPlatformParameters](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkOtherPlatformParameters)


  ` Options class for defining other platform(s) parameters of the Dynamic Link.
  Other here means not covered by specific parameters (not iOS and not Android).

  #### Declaration

  Objective-C


      @interface FIRDynamicLinkOtherPlatformParameters : NSObject

- `


  ### [FIRDynamicLinkComponentsOptions](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkComponentsOptions)


  ` Options class for defining how Dynamic Link URLs are generated.

  #### Declaration

  Objective-C


      @interface FIRDynamicLinkComponentsOptions : NSObject

- `


  ### [FIRDynamicLinkComponents](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkComponents)


  ` The class used for Dynamic Link URL generation; supports creation of short and long
  Dynamic Link URLs. Short URLs will have a domain and a randomized path; long URLs will have a
  domain and a query that contains all of the Dynamic Link parameters.

  #### Declaration

  Objective-C


      @interface FIRDynamicLinkComponents : NSObject

- `


  ### [FIRDynamicLink](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLink)


  ` A received Dynamic Link.

  #### Declaration

  Objective-C


      @interface FIRDynamicLink : NSObject

- `


  ### [FIRDynamicLinks](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinks)


  ` Deprecated

  Firebase Dynamic Links is deprecated and the service will shut down on August 25, 2025.
  A class that checks for pending Dynamic Links and parses URLs.
  This class is available on iOS only.

  #### Declaration

  Objective-C


      @interface FIRDynamicLinks : NSObject
# Source: https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes.md.txt

# FirebaseDynamicLinks Framework Reference

# Classes

The following classes are available globally.
- `


  ### [DynamicLinkGoogleAnalyticsParameters](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkGoogleAnalyticsParameters)


  ` The Dynamic Link analytics parameters.

  #### Declaration

  Swift

      class DynamicLinkGoogleAnalyticsParameters : NSObject

- `


  ### [DynamicLinkIOSParameters](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkIOSParameters)


  ` The Dynamic Link iOS parameters.

  #### Declaration

  Swift

      class DynamicLinkIOSParameters : NSObject

- `


  ### [DynamicLinkItunesConnectAnalyticsParameters](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkItunesConnectAnalyticsParameters)


  ` The Dynamic Link iTunes Connect parameters.

  #### Declaration

  Swift

      class DynamicLinkItunesConnectAnalyticsParameters : NSObject

- `


  ### [DynamicLinkAndroidParameters](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkAndroidParameters)


  ` The Dynamic Link Android parameters.

  #### Declaration

  Swift

      class DynamicLinkAndroidParameters : NSObject

- `


  ### [DynamicLinkSocialMetaTagParameters](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkSocialMetaTagParameters)


  ` The Dynamic Link Social Meta Tag parameters.

  #### Declaration

  Swift

      class DynamicLinkSocialMetaTagParameters : NSObject

- `


  ### [DynamicLinkNavigationInfoParameters](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkNavigationInfoParameters)


  ` Options class for defining navigation behavior of the Dynamic Link.

  #### Declaration

  Swift

      class DynamicLinkNavigationInfoParameters : NSObject

- `


  ### [DynamicLinkOtherPlatformParameters](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkOtherPlatformParameters)


  ` Options class for defining other platform(s) parameters of the Dynamic Link.
  Other here means not covered by specific parameters (not iOS and not Android).

  #### Declaration

  Swift

      class DynamicLinkOtherPlatformParameters : NSObject

- `


  ### [DynamicLinkComponentsOptions](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkComponentsOptions)


  ` Options class for defining how Dynamic Link URLs are generated.

  #### Declaration

  Swift

      class DynamicLinkComponentsOptions : NSObject

- `


  ### [DynamicLinkComponents](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkComponents)


  ` The class used for Dynamic Link URL generation; supports creation of short and long
  Dynamic Link URLs. Short URLs will have a domain and a randomized path; long URLs will have a
  domain and a query that contains all of the Dynamic Link parameters.

  #### Declaration

  Swift

      class DynamicLinkComponents : NSObject

- `


  ### [DynamicLink](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLink)


  ` A received Dynamic Link.

  #### Declaration

  Swift

      class DynamicLink : NSObject

- `


  ### [DynamicLinks](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinks)


  ` Deprecated

  Firebase Dynamic Links is deprecated and the service will shut down on August 25, 2025.
  A class that checks for pending Dynamic Links and parses URLs.
  This class is available on iOS only.

  #### Declaration

  Swift

      class DynamicLinks : NSObject
# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADServerSideVerificationOptions.md.txt

# GoogleMobileAds Framework Reference

# GADServerSideVerificationOptions

    @interface GADServerSideVerificationOptions : NSObject <NSCopying>

Options for server-to-server verification callbacks for a rewarded ad.
- `


  ### [userIdentifier](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADServerSideVerificationOptions#/c:objc(cs)GADServerSideVerificationOptions(py)userIdentifier)


  ` A unique identifier used to identify the user when making server-to-server reward callbacks.
  This value will be passed as a parameter of the callback URL to the publisher's server.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable) NSString *userIdentifier;

- `


  ### [customRewardString](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADServerSideVerificationOptions#/c:objc(cs)GADServerSideVerificationOptions(py)customRewardString)


  ` Optional custom reward string to include in the server-to-server callback.

  #### Declaration

  Objective-C

      @property (readwrite, copy, nonatomic, nullable) NSString *customRewardString;
# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADServerSideVerificationOptions.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADServerSideVerificationOptions.md.txt

# GoogleMobileAds Framework Reference

# GADServerSideVerificationOptions

    class GADServerSideVerificationOptions : NSObject, NSCopying

Options for server-to-server verification callbacks for a rewarded ad.
- `
  ``
  ``
  `

  ### [userIdentifier](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADServerSideVerificationOptions#/c:objc(cs)GADServerSideVerificationOptions(py)userIdentifier)

  `
  `  
  A unique identifier used to identify the user when making server-to-server reward callbacks.
  This value will be passed as a parameter of the callback URL to the publisher's server.  

  #### Declaration

  Swift  

      var userIdentifier: String? { get set }

- `
  ``
  ``
  `

  ### [customRewardString](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADServerSideVerificationOptions#/c:objc(cs)GADServerSideVerificationOptions(py)customRewardString)

  `
  `  
  Optional custom reward string to include in the server-to-server callback.  

  #### Declaration

  Swift  

      var customRewardString: String? { get set }
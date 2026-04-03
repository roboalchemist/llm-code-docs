# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADRewardedAdMetadataDelegate.md.txt

# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADRewardedAdMetadataDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADRewardedAdMetadataDelegate

    @protocol GADRewardedAdMetadataDelegate <NSObject>

Delegate for receiving metadata change messages from a GADRewardedAd.
- `
  ``
  ``
  `

  ### [-rewardedAdMetadataDidChange:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADRewardedAdMetadataDelegate#/c:objc(pl)GADRewardedAdMetadataDelegate(im)rewardedAdMetadataDidChange:)

  `
  `  
  Tells the delegate that the rewarded ad's metadata changed. Called when an ad loads, and when a
  loaded ad's metadata changes.  

  #### Declaration

  Objective-C  

      - (void)rewardedAdMetadataDidChange:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRewardedAd.html *)rewardedAd;
# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADRewardedAdMetadataDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADRewardedAdMetadataDelegate

    protocol GADRewardedAdMetadataDelegate : NSObjectProtocol

Delegate for receiving metadata change messages from a GADRewardedAd.
- `


  ### [rewardedAdMetadataDidChange(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADRewardedAdMetadataDelegate#/c:objc(pl)GADRewardedAdMetadataDelegate(im)rewardedAdMetadataDidChange:)


  ` Tells the delegate that the rewarded ad's metadata changed. Called when an ad loads, and when a
  loaded ad's metadata changes.

  #### Declaration

  Swift

      optional func rewardedAdMetadataDidChange(_ rewardedAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardedAd.html)
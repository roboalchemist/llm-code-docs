# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADRewardBasedVideoAdDelegate.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADRewardBasedVideoAdDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADRewardBasedVideoAdDelegate

    protocol GADRewardBasedVideoAdDelegate : NSObjectProtocol

Delegate for receiving state change messages from a GADRewardBasedVideoAd such as ad requests
succeeding/failing.
- `
  ``
  ``
  `

  ### [rewardBasedVideoAd(_:didRewardUserWith:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADRewardBasedVideoAdDelegate#/c:objc(pl)GADRewardBasedVideoAdDelegate(im)rewardBasedVideoAd:didRewardUserWithReward:)

  `
  `  
  Tells the delegate that the reward based video ad has rewarded the user.  

  #### Declaration

  Swift  

      func rewardBasedVideoAd(_ rewardBasedVideoAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardBasedVideoAd.html, didRewardUserWith reward: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAdReward.html)

- `
  ``
  ``
  `

  ### [rewardBasedVideoAd(_:didFailToLoadWithError:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADRewardBasedVideoAdDelegate#/c:objc(pl)GADRewardBasedVideoAdDelegate(im)rewardBasedVideoAd:didFailToLoadWithError:)

  `
  `  
  Tells the delegate that the reward based video ad failed to load.  

  #### Declaration

  Swift  

      optional func rewardBasedVideoAd(_ rewardBasedVideoAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardBasedVideoAd.html, didFailToLoadWithError error: Error)

- `
  ``
  ``
  `

  ### [rewardBasedVideoAdDidReceive(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADRewardBasedVideoAdDelegate#/c:objc(pl)GADRewardBasedVideoAdDelegate(im)rewardBasedVideoAdDidReceiveAd:)

  `
  `  
  Tells the delegate that a reward based video ad was received.  

  #### Declaration

  Swift  

      optional func rewardBasedVideoAdDidReceive(_ rewardBasedVideoAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardBasedVideoAd.html)

- `
  ``
  ``
  `

  ### [rewardBasedVideoAdDidOpen(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADRewardBasedVideoAdDelegate#/c:objc(pl)GADRewardBasedVideoAdDelegate(im)rewardBasedVideoAdDidOpen:)

  `
  `  
  Tells the delegate that the reward based video ad opened.  

  #### Declaration

  Swift  

      optional func rewardBasedVideoAdDidOpen(_ rewardBasedVideoAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardBasedVideoAd.html)

- `
  ``
  ``
  `

  ### [rewardBasedVideoAdDidStartPlaying(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADRewardBasedVideoAdDelegate#/c:objc(pl)GADRewardBasedVideoAdDelegate(im)rewardBasedVideoAdDidStartPlaying:)

  `
  `  
  Tells the delegate that the reward based video ad started playing.  

  #### Declaration

  Swift  

      optional func rewardBasedVideoAdDidStartPlaying(_ rewardBasedVideoAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardBasedVideoAd.html)

- `
  ``
  ``
  `

  ### [rewardBasedVideoAdDidCompletePlaying(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADRewardBasedVideoAdDelegate#/c:objc(pl)GADRewardBasedVideoAdDelegate(im)rewardBasedVideoAdDidCompletePlaying:)

  `
  `  
  Tells the delegate that the reward based video ad completed playing.  

  #### Declaration

  Swift  

      optional func rewardBasedVideoAdDidCompletePlaying(_ rewardBasedVideoAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardBasedVideoAd.html)

- `
  ``
  ``
  `

  ### [rewardBasedVideoAdDidClose(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADRewardBasedVideoAdDelegate#/c:objc(pl)GADRewardBasedVideoAdDelegate(im)rewardBasedVideoAdDidClose:)

  `
  `  
  Tells the delegate that the reward based video ad closed.  

  #### Declaration

  Swift  

      optional func rewardBasedVideoAdDidClose(_ rewardBasedVideoAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardBasedVideoAd.html)

- `
  ``
  ``
  `

  ### [rewardBasedVideoAdWillLeaveApplication(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADRewardBasedVideoAdDelegate#/c:objc(pl)GADRewardBasedVideoAdDelegate(im)rewardBasedVideoAdWillLeaveApplication:)

  `
  `  
  Tells the delegate that the reward based video ad will leave the application.  

  #### Declaration

  Swift  

      optional func rewardBasedVideoAdWillLeaveApplication(_ rewardBasedVideoAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardBasedVideoAd.html)

- `
  ``
  ``
  `

  ### [rewardBasedVideoAdMetadataDidChange(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADRewardBasedVideoAdDelegate#/c:objc(pl)GADRewardBasedVideoAdDelegate(im)rewardBasedVideoAdMetadataDidChange:)

  `
  `  
  Tells the delegate that the reward based video ad's metadata changed. Called when an ad loads,
  and when a loaded ad's metadata changes.  

  #### Declaration

  Swift  

      optional func rewardBasedVideoAdMetadataDidChange(_ rewardBasedVideoAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardBasedVideoAd.html)
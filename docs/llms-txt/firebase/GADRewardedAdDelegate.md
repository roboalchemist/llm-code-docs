# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADRewardedAdDelegate.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADRewardedAdDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADRewardedAdDelegate

    protocol GADRewardedAdDelegate : NSObjectProtocol

Delegate for receiving state change messages from a GADRewardedAd.
- `
  ``
  ``
  `

  ### [rewardedAd(_:userDidEarn:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADRewardedAdDelegate#/c:objc(pl)GADRewardedAdDelegate(im)rewardedAd:userDidEarnReward:)

  `
  `  
  Tells the delegate that the user earned a reward.  

  #### Declaration

  Swift  

      func rewardedAd(_ rewardedAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardedAd.html, userDidEarn reward: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAdReward.html)

- `
  ``
  ``
  `

  ### [rewardedAd(_:didFailToPresentWithError:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADRewardedAdDelegate#/c:objc(pl)GADRewardedAdDelegate(im)rewardedAd:didFailToPresentWithError:)

  `
  `  
  Tells the delegate that the rewarded ad failed to present.  

  #### Declaration

  Swift  

      optional func rewardedAd(_ rewardedAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardedAd.html, didFailToPresentWithError error: Error)

- `
  ``
  ``
  `

  ### [rewardedAdDidPresent(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADRewardedAdDelegate#/c:objc(pl)GADRewardedAdDelegate(im)rewardedAdDidPresent:)

  `
  `  
  Tells the delegate that the rewarded ad was presented.  

  #### Declaration

  Swift  

      optional func rewardedAdDidPresent(_ rewardedAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardedAd.html)

- `
  ``
  ``
  `

  ### [rewardedAdDidDismiss(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADRewardedAdDelegate#/c:objc(pl)GADRewardedAdDelegate(im)rewardedAdDidDismiss:)

  `
  `  
  Tells the delegate that the rewarded ad was dismissed.  

  #### Declaration

  Swift  

      optional func rewardedAdDidDismiss(_ rewardedAd: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRewardedAd.html)
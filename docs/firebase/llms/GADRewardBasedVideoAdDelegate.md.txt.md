# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADRewardBasedVideoAdDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADRewardBasedVideoAdDelegate

    @protocol GADRewardBasedVideoAdDelegate <NSObject>

Delegate for receiving state change messages from a GADRewardBasedVideoAd such as ad requests
succeeding/failing.
- `


  ### [-rewardBasedVideoAd:didRewardUserWithReward:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADRewardBasedVideoAdDelegate#/c:objc(pl)GADRewardBasedVideoAdDelegate(im)rewardBasedVideoAd:didRewardUserWithReward:)


  ` Tells the delegate that the reward based video ad has rewarded the user.

  #### Declaration

  Objective-C

      - (void)rewardBasedVideoAd:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRewardBasedVideoAd.html *)rewardBasedVideoAd
          didRewardUserWithReward:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdReward.html *)reward;

- `


  ### [-rewardBasedVideoAd:didFailToLoadWithError:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADRewardBasedVideoAdDelegate#/c:objc(pl)GADRewardBasedVideoAdDelegate(im)rewardBasedVideoAd:didFailToLoadWithError:)


  ` Tells the delegate that the reward based video ad failed to load.

  #### Declaration

  Objective-C

      - (void)rewardBasedVideoAd:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRewardBasedVideoAd.html *)rewardBasedVideoAd
          didFailToLoadWithError:(nonnull NSError *)error;

- `


  ### [-rewardBasedVideoAdDidReceiveAd:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADRewardBasedVideoAdDelegate#/c:objc(pl)GADRewardBasedVideoAdDelegate(im)rewardBasedVideoAdDidReceiveAd:)


  ` Tells the delegate that a reward based video ad was received.

  #### Declaration

  Objective-C

      - (void)rewardBasedVideoAdDidReceiveAd:
          (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRewardBasedVideoAd.html *)rewardBasedVideoAd;

- `


  ### [-rewardBasedVideoAdDidOpen:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADRewardBasedVideoAdDelegate#/c:objc(pl)GADRewardBasedVideoAdDelegate(im)rewardBasedVideoAdDidOpen:)


  ` Tells the delegate that the reward based video ad opened.

  #### Declaration

  Objective-C

      - (void)rewardBasedVideoAdDidOpen:
          (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRewardBasedVideoAd.html *)rewardBasedVideoAd;

- `


  ### [-rewardBasedVideoAdDidStartPlaying:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADRewardBasedVideoAdDelegate#/c:objc(pl)GADRewardBasedVideoAdDelegate(im)rewardBasedVideoAdDidStartPlaying:)


  ` Tells the delegate that the reward based video ad started playing.

  #### Declaration

  Objective-C

      - (void)rewardBasedVideoAdDidStartPlaying:
          (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRewardBasedVideoAd.html *)rewardBasedVideoAd;

- `


  ### [-rewardBasedVideoAdDidCompletePlaying:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADRewardBasedVideoAdDelegate#/c:objc(pl)GADRewardBasedVideoAdDelegate(im)rewardBasedVideoAdDidCompletePlaying:)


  ` Tells the delegate that the reward based video ad completed playing.

  #### Declaration

  Objective-C

      - (void)rewardBasedVideoAdDidCompletePlaying:
          (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRewardBasedVideoAd.html *)rewardBasedVideoAd;

- `


  ### [-rewardBasedVideoAdDidClose:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADRewardBasedVideoAdDelegate#/c:objc(pl)GADRewardBasedVideoAdDelegate(im)rewardBasedVideoAdDidClose:)


  ` Tells the delegate that the reward based video ad closed.

  #### Declaration

  Objective-C

      - (void)rewardBasedVideoAdDidClose:
          (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRewardBasedVideoAd.html *)rewardBasedVideoAd;

- `


  ### [-rewardBasedVideoAdWillLeaveApplication:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADRewardBasedVideoAdDelegate#/c:objc(pl)GADRewardBasedVideoAdDelegate(im)rewardBasedVideoAdWillLeaveApplication:)


  ` Tells the delegate that the reward based video ad will leave the application.

  #### Declaration

  Objective-C

      - (void)rewardBasedVideoAdWillLeaveApplication:
          (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRewardBasedVideoAd.html *)rewardBasedVideoAd;

- `


  ### [-rewardBasedVideoAdMetadataDidChange:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADRewardBasedVideoAdDelegate#/c:objc(pl)GADRewardBasedVideoAdDelegate(im)rewardBasedVideoAdMetadataDidChange:)


  ` Tells the delegate that the reward based video ad's metadata changed. Called when an ad loads,
  and when a loaded ad's metadata changes.

  #### Declaration

  Objective-C

      - (void)rewardBasedVideoAdMetadataDidChange:
          (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRewardBasedVideoAd.html *)rewardBasedVideoAd;
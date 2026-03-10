# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADRewardedAdDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADRewardedAdDelegate

    @protocol GADRewardedAdDelegate <NSObject>

Delegate for receiving state change messages from a GADRewardedAd.
- `


  ### [-rewardedAd:userDidEarnReward:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADRewardedAdDelegate#/c:objc(pl)GADRewardedAdDelegate(im)rewardedAd:userDidEarnReward:)


  ` Tells the delegate that the user earned a reward.

  #### Declaration

  Objective-C

      - (void)rewardedAd:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRewardedAd.html *)rewardedAd
          userDidEarnReward:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdReward.html *)reward;

- `


  ### [-rewardedAd:didFailToPresentWithError:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADRewardedAdDelegate#/c:objc(pl)GADRewardedAdDelegate(im)rewardedAd:didFailToPresentWithError:)


  ` Tells the delegate that the rewarded ad failed to present.

  #### Declaration

  Objective-C

      - (void)rewardedAd:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRewardedAd.html *)rewardedAd
          didFailToPresentWithError:(nonnull NSError *)error;

- `


  ### [-rewardedAdDidPresent:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADRewardedAdDelegate#/c:objc(pl)GADRewardedAdDelegate(im)rewardedAdDidPresent:)


  ` Tells the delegate that the rewarded ad was presented.

  #### Declaration

  Objective-C

      - (void)rewardedAdDidPresent:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRewardedAd.html *)rewardedAd;

- `


  ### [-rewardedAdDidDismiss:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADRewardedAdDelegate#/c:objc(pl)GADRewardedAdDelegate(im)rewardedAdDidDismiss:)


  ` Tells the delegate that the rewarded ad was dismissed.

  #### Declaration

  Objective-C

      - (void)rewardedAdDidDismiss:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADRewardedAd.html *)rewardedAd;
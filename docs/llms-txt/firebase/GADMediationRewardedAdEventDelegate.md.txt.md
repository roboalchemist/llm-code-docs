# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationRewardedAdEventDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADMediationRewardedAdEventDelegate

    protocol GADMediationRewardedAdEventDelegate : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdEventDelegate.html

Reports rewarded related information to the Google Mobile Ads SDK from the adapter.
- `


  ### [didRewardUser(with:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationRewardedAdEventDelegate#/c:objc(pl)GADMediationRewardedAdEventDelegate(im)didRewardUserWithReward:)


  ` Notifies the Google Mobile Ads SDK that the GADMediationAd has rewarded the user with a reward.

  #### Declaration

  Swift

      func didRewardUser(with reward: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAdReward.html)

- `


  ### [didStartVideo()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationRewardedAdEventDelegate#/c:objc(pl)GADMediationRewardedAdEventDelegate(im)didStartVideo)


  ` Notifies Google Mobile Ads SDK that the GADMediationAd started video playback.

  #### Declaration

  Swift

      func didStartVideo()

- `


  ### [didEndVideo()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationRewardedAdEventDelegate#/c:objc(pl)GADMediationRewardedAdEventDelegate(im)didEndVideo)


  ` Notifies Google Mobile Ads SDK that the GADMediationAd's video playback finished.

  #### Declaration

  Swift

      func didEndVideo()
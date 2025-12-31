# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationRewardedAdEventDelegate.md.txt

# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationRewardedAdEventDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADMediationRewardedAdEventDelegate

    @protocol GADMediationRewardedAdEventDelegate <https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdEventDelegate.html>

Reports rewarded related information to the Google Mobile Ads SDK from the adapter.
- `
  ``
  ``
  `

  ### [-didRewardUserWithReward:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationRewardedAdEventDelegate#/c:objc(pl)GADMediationRewardedAdEventDelegate(im)didRewardUserWithReward:)

  `
  `  
  Notifies the Google Mobile Ads SDK that the GADMediationAd has rewarded the user with a reward.  

  #### Declaration

  Objective-C  

      - (void)didRewardUserWithReward:(nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdReward.html *)reward;

- `
  ``
  ``
  `

  ### [-didStartVideo](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationRewardedAdEventDelegate#/c:objc(pl)GADMediationRewardedAdEventDelegate(im)didStartVideo)

  `
  `  
  Notifies Google Mobile Ads SDK that the GADMediationAd started video playback.  

  #### Declaration

  Objective-C  

      - (void)didStartVideo;

- `
  ``
  ``
  `

  ### [-didEndVideo](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationRewardedAdEventDelegate#/c:objc(pl)GADMediationRewardedAdEventDelegate(im)didEndVideo)

  `
  `  
  Notifies Google Mobile Ads SDK that the GADMediationAd's video playback finished.  

  #### Declaration

  Objective-C  

      - (void)didEndVideo;
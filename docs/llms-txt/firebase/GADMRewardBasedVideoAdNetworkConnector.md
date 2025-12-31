# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkConnector.md.txt

# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkConnector.md.txt

# GoogleMobileAds Framework Reference

# GADMRewardBasedVideoAdNetworkConnector

    @protocol GADMRewardBasedVideoAdNetworkConnector <https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMediationAdRequest.html>

Reward based video ad network adapters interact with the mediation SDK using an object that
conforms to the GADMRewardBasedVideoAdNetworkConnector protocol. The connector object can be
used to obtain information for ad requests and to call back to the mediation SDK on ad responses
and user interactions.
- `
  ``
  ``
  `

  ### [-adapterDidSetUpRewardBasedVideoAd:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkConnector#/c:objc(pl)GADMRewardBasedVideoAdNetworkConnector(im)adapterDidSetUpRewardBasedVideoAd:)

  `
  `  
  Tells the delegate that the adapter successfully set up a reward based video ad.  

  #### Declaration

  Objective-C  

      - (void)adapterDidSetUpRewardBasedVideoAd:
          (id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkAdapter.html>)rewardBasedVideoAdAdapter;

- `
  ``
  ``
  `

  ### [-adapter:didFailToSetUpRewardBasedVideoAdWithError:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkConnector#/c:objc(pl)GADMRewardBasedVideoAdNetworkConnector(im)adapter:didFailToSetUpRewardBasedVideoAdWithError:)

  `
  `  
  Tells the delegate that the adapter failed to set up a reward based video ad.  

  #### Declaration

  Objective-C  

      - (void)adapter:
                  (id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkAdapter.html>)rewardBasedVideoAdAdapter
          didFailToSetUpRewardBasedVideoAdWithError:(NSError *)error;

- `
  ``
  ``
  `

  ### [-adapterDidGetAdClick:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkConnector#/c:objc(pl)GADMRewardBasedVideoAdNetworkConnector(im)adapterDidGetAdClick:)

  `
  `  
  Tells the delegate that a reward based video ad was clicked.  

  #### Declaration

  Objective-C  

      - (void)adapterDidGetAdClick:(id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkAdapter.html>)adapter;

- `
  ``
  ``
  `

  ### [-adapterDidReceiveRewardBasedVideoAd:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkConnector#/c:objc(pl)GADMRewardBasedVideoAdNetworkConnector(im)adapterDidReceiveRewardBasedVideoAd:)

  `
  `  
  Tells the delegate that a reward based video ad has loaded.  

  #### Declaration

  Objective-C  

      - (void)adapterDidReceiveRewardBasedVideoAd:
          (id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkAdapter.html>)rewardBasedVideoAdAdapter;

- `
  ``
  ``
  `

  ### [-adapterDidOpenRewardBasedVideoAd:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkConnector#/c:objc(pl)GADMRewardBasedVideoAdNetworkConnector(im)adapterDidOpenRewardBasedVideoAd:)

  `
  `  
  Tells the delegate that a reward based video ad has opened.  

  #### Declaration

  Objective-C  

      - (void)adapterDidOpenRewardBasedVideoAd:
          (id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkAdapter.html>)rewardBasedVideoAdAdapter;

- `
  ``
  ``
  `

  ### [-adapterDidStartPlayingRewardBasedVideoAd:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkConnector#/c:objc(pl)GADMRewardBasedVideoAdNetworkConnector(im)adapterDidStartPlayingRewardBasedVideoAd:)

  `
  `  
  Tells the delegate that a reward based video ad has started playing.  

  #### Declaration

  Objective-C  

      - (void)adapterDidStartPlayingRewardBasedVideoAd:
          (id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkAdapter.html>)rewardBasedVideoAdAdapter;

- `
  ``
  ``
  `

  ### [-adapterDidCompletePlayingRewardBasedVideoAd:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkConnector#/c:objc(pl)GADMRewardBasedVideoAdNetworkConnector(im)adapterDidCompletePlayingRewardBasedVideoAd:)

  `
  `  
  Tells the delegate that a reward based video ad has completed playing.  

  #### Declaration

  Objective-C  

      - (void)adapterDidCompletePlayingRewardBasedVideoAd:
          (id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkAdapter.html>)rewardBasedVideoAdAdapter;

- `
  ``
  ``
  `

  ### [-adapterDidCloseRewardBasedVideoAd:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkConnector#/c:objc(pl)GADMRewardBasedVideoAdNetworkConnector(im)adapterDidCloseRewardBasedVideoAd:)

  `
  `  
  Tells the delegate that a reward based video ad has closed.  

  #### Declaration

  Objective-C  

      - (void)adapterDidCloseRewardBasedVideoAd:
          (id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkAdapter.html>)rewardBasedVideoAdAdapter;

- `
  ``
  ``
  `

  ### [-adapter:didRewardUserWithReward:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkConnector#/c:objc(pl)GADMRewardBasedVideoAdNetworkConnector(im)adapter:didRewardUserWithReward:)

  `
  `  
  Tells the delegate that the adapter has rewarded the user.  

  #### Declaration

  Objective-C  

      - (void)adapter:(id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkAdapter.html>)rewardBasedVideoAd
          didRewardUserWithReward:(https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdReward.html *)reward;

- `
  ``
  ``
  `

  ### [-adapterWillLeaveApplication:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkConnector#/c:objc(pl)GADMRewardBasedVideoAdNetworkConnector(im)adapterWillLeaveApplication:)

  `
  `  
  Tells the delegate that a reward based video ad's action will leave the application.  

  #### Declaration

  Objective-C  

      - (void)adapterWillLeaveApplication:
          (id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkAdapter.html>)rewardBasedVideoAdAdapter;

- `
  ``
  ``
  `

  ### [-adapter:didFailToLoadRewardBasedVideoAdwithError:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkConnector#/c:objc(pl)GADMRewardBasedVideoAdNetworkConnector(im)adapter:didFailToLoadRewardBasedVideoAdwithError:)

  `
  `  
  Tells the delegate that a reward based video ad failed to load.  

  #### Declaration

  Objective-C  

      - (void)adapter:
                  (id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkAdapter.html>)rewardBasedVideoAdAdapter
          didFailToLoadRewardBasedVideoAdwithError:(NSError *)error;
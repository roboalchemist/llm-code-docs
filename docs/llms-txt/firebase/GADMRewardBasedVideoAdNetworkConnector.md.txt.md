# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkConnector.md.txt

# GoogleMobileAds Framework Reference

# GADMRewardBasedVideoAdNetworkConnector

    protocol GADMRewardBasedVideoAdNetworkConnector : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdRequest.html

Reward based video ad network adapters interact with the mediation SDK using an object that
conforms to the GADMRewardBasedVideoAdNetworkConnector protocol. The connector object can be
used to obtain information for ad requests and to call back to the mediation SDK on ad responses
and user interactions.
- `


  ### [-adapterDidSetUpRewardBasedVideoAd:](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkConnector#/c:objc(pl)GADMRewardBasedVideoAdNetworkConnector(im)adapterDidSetUpRewardBasedVideoAd:)


  ` Tells the delegate that the adapter successfully set up a reward based video ad.
- `


  ### [-adapter:didFailToSetUpRewardBasedVideoAdWithError:](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkConnector#/c:objc(pl)GADMRewardBasedVideoAdNetworkConnector(im)adapter:didFailToSetUpRewardBasedVideoAdWithError:)


  ` Tells the delegate that the adapter failed to set up a reward based video ad.
- `


  ### [-adapterDidGetAdClick:](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkConnector#/c:objc(pl)GADMRewardBasedVideoAdNetworkConnector(im)adapterDidGetAdClick:)


  ` Tells the delegate that a reward based video ad was clicked.
- `


  ### [-adapterDidReceiveRewardBasedVideoAd:](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkConnector#/c:objc(pl)GADMRewardBasedVideoAdNetworkConnector(im)adapterDidReceiveRewardBasedVideoAd:)


  ` Tells the delegate that a reward based video ad has loaded.
- `


  ### [-adapterDidOpenRewardBasedVideoAd:](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkConnector#/c:objc(pl)GADMRewardBasedVideoAdNetworkConnector(im)adapterDidOpenRewardBasedVideoAd:)


  ` Tells the delegate that a reward based video ad has opened.
- `


  ### [-adapterDidStartPlayingRewardBasedVideoAd:](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkConnector#/c:objc(pl)GADMRewardBasedVideoAdNetworkConnector(im)adapterDidStartPlayingRewardBasedVideoAd:)


  ` Tells the delegate that a reward based video ad has started playing.
- `


  ### [-adapterDidCompletePlayingRewardBasedVideoAd:](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkConnector#/c:objc(pl)GADMRewardBasedVideoAdNetworkConnector(im)adapterDidCompletePlayingRewardBasedVideoAd:)


  ` Tells the delegate that a reward based video ad has completed playing.
- `


  ### [-adapterDidCloseRewardBasedVideoAd:](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkConnector#/c:objc(pl)GADMRewardBasedVideoAdNetworkConnector(im)adapterDidCloseRewardBasedVideoAd:)


  ` Tells the delegate that a reward based video ad has closed.
- `


  ### [-adapter:didRewardUserWithReward:](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkConnector#/c:objc(pl)GADMRewardBasedVideoAdNetworkConnector(im)adapter:didRewardUserWithReward:)


  ` Tells the delegate that the adapter has rewarded the user.
- `


  ### [-adapterWillLeaveApplication:](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkConnector#/c:objc(pl)GADMRewardBasedVideoAdNetworkConnector(im)adapterWillLeaveApplication:)


  ` Tells the delegate that a reward based video ad's action will leave the application.
- `


  ### [-adapter:didFailToLoadRewardBasedVideoAdwithError:](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMRewardBasedVideoAdNetworkConnector#/c:objc(pl)GADMRewardBasedVideoAdNetworkConnector(im)adapter:didFailToLoadRewardBasedVideoAdwithError:)


  ` Tells the delegate that a reward based video ad failed to load.
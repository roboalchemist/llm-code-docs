# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdReward.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAdReward.md.txt

# GoogleMobileAds Framework Reference

# GADAdReward

    class GADAdReward : NSObject

Reward information for GADRewardBasedVideoAd ads.
- `
  ``
  ``
  `

  ### [type](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAdReward#/c:objc(cs)GADAdReward(py)type)

  `
  `  
  Type of the reward.  

  #### Declaration

  Swift  

      var type: String { get }

- `
  ``
  ``
  `

  ### [amount](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAdReward#/c:objc(cs)GADAdReward(py)amount)

  `
  `  
  Amount rewarded to the user.  

  #### Declaration

  Swift  

      @NSCopying var amount: NSDecimalNumber { get }

- `
  ``
  ``
  `

  ### [init(rewardType:rewardAmount:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAdReward#/c:objc(cs)GADAdReward(im)initWithRewardType:rewardAmount:)

  `
  `  
  Returns an initialized GADAdReward with the provided reward type and reward amount. rewardType
  and rewardAmount must not be nil.  

  #### Declaration

  Swift  

      init(rewardType: String, rewardAmount: NSDecimalNumber)
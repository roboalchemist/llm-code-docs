# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdReward.md.txt

# GoogleMobileAds Framework Reference

# GADAdReward

    @interface GADAdReward : NSObject

Reward information for GADRewardBasedVideoAd ads.
- `


  ### [type](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdReward#/c:objc(cs)GADAdReward(py)type)


  ` Type of the reward.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic) NSString *_Nonnull type;

- `


  ### [amount](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdReward#/c:objc(cs)GADAdReward(py)amount)


  ` Amount rewarded to the user.

  #### Declaration

  Objective-C

      @property (readonly, copy, nonatomic) NSDecimalNumber *_Nonnull amount;

- `


  ### [-initWithRewardType:rewardAmount:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdReward#/c:objc(cs)GADAdReward(im)initWithRewardType:rewardAmount:)


  ` Returns an initialized GADAdReward with the provided reward type and reward amount. rewardType
  and rewardAmount must not be nil.

  #### Declaration

  Objective-C

      - (nonnull instancetype)initWithRewardType:(nonnull NSString *)rewardType
                                    rewardAmount:
                                        (nonnull NSDecimalNumber *)rewardAmount;
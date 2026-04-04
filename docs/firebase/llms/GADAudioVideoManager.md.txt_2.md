# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAudioVideoManager.md.txt

# GoogleMobileAds Framework Reference

# GADAudioVideoManager

    @interface GADAudioVideoManager : NSObject

Provides audio and video notifications and configurations management.

Don't create an instance of this class and use the one available from GADMobileAds
sharedInstace's audioVideoManager.
- `


  ### [delegate](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAudioVideoManager#/c:objc(cs)GADAudioVideoManager(py)delegate)


  ` Delegate for receiving video and audio updates.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADAudioVideoManagerDelegate.html>
          delegate;

- `


  ### [audioSessionIsApplicationManaged](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAudioVideoManager#/c:objc(cs)GADAudioVideoManager(py)audioSessionIsApplicationManaged)


  ` Indicates whether the application wishes to manage audio session. If set as YES, the Google
  Mobile Ads SDK will stop managing AVAudioSession during the video playback lifecycle. If set as
  NO, the Google Mobile Ads SDK will control AVAudioSession. That may include: setting
  AVAudioSession's category to AVAudioSessionCategoryAmbient when all videos are muted, setting
  AVAudioSession's category to AVAudioSessionCategorySoloAmbient when any playing video becomes
  unmuted, and allowing background apps to continue playing sound when all videos rendered by
  Google Mobile Ads SDK are muted or have stopped playing.

  #### Declaration

  Objective-C

      @property (assign, readwrite, nonatomic) BOOL audioSessionIsApplicationManaged;
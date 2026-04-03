# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAudioVideoManager.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAudioVideoManager.md.txt

# GoogleMobileAds Framework Reference

# GADAudioVideoManager

    class GADAudioVideoManager : NSObject

Provides audio and video notifications and configurations management.

Don't create an instance of this class and use the one available from GADMobileAds
sharedInstace's audioVideoManager.
- `
  ``
  ``
  `

  ### [delegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAudioVideoManager#/c:objc(cs)GADAudioVideoManager(py)delegate)

  `
  `  
  Delegate for receiving video and audio updates.  

  #### Declaration

  Swift  

      weak var delegate: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAudioVideoManagerDelegate.html? { get set }

- `
  ``
  ``
  `

  ### [audioSessionIsApplicationManaged](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAudioVideoManager#/c:objc(cs)GADAudioVideoManager(py)audioSessionIsApplicationManaged)

  `
  `  
  Indicates whether the application wishes to manage audio session. If set as YES, the Google
  Mobile Ads SDK will stop managing AVAudioSession during the video playback lifecycle. If set as
  NO, the Google Mobile Ads SDK will control AVAudioSession. That may include: setting
  AVAudioSession's category to AVAudioSessionCategoryAmbient when all videos are muted, setting
  AVAudioSession's category to AVAudioSessionCategorySoloAmbient when any playing video becomes
  unmuted, and allowing background apps to continue playing sound when all videos rendered by
  Google Mobile Ads SDK are muted or have stopped playing.  

  #### Declaration

  Swift  

      var audioSessionIsApplicationManaged: Bool { get set }
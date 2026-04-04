# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAudioVideoManagerDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADAudioVideoManagerDelegate

    protocol GADAudioVideoManagerDelegate : NSObjectProtocol

A set of methods to inform the delegate of audio video manager events.
- `


  ### [audioVideoManagerWillPlayVideo(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAudioVideoManagerDelegate#/c:objc(pl)GADAudioVideoManagerDelegate(im)audioVideoManagerWillPlayVideo:)


  ` Tells the delegate that the Google Mobile Ads SDK will start playing a video. This method isn't
  called if another video rendered by Google Mobile Ads SDK is already playing.

  #### Declaration

  Swift

      optional func audioVideoManagerWillPlayVideo(_ audioVideoManager: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAudioVideoManager.html)

- `


  ### [audioVideoManagerDidPauseAllVideo(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAudioVideoManagerDelegate#/c:objc(pl)GADAudioVideoManagerDelegate(im)audioVideoManagerDidPauseAllVideo:)


  ` Tells the delegate that the Google Mobile Ads SDK has paused/stopped all video playback.

  #### Declaration

  Swift

      optional func audioVideoManagerDidPauseAllVideo(_ audioVideoManager: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAudioVideoManager.html)

- `


  ### [audioVideoManagerWillPlayAudio(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAudioVideoManagerDelegate#/c:objc(pl)GADAudioVideoManagerDelegate(im)audioVideoManagerWillPlayAudio:)


  ` Tells the delegate that at least one video rendered by the Google Mobile Ads SDK will play
  sound. Your app should stop playing sound when this method is called.

  #### Declaration

  Swift

      optional func audioVideoManagerWillPlayAudio(_ audioVideoManager: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAudioVideoManager.html)

- `


  ### [audioVideoManagerDidStopPlayingAudio(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADAudioVideoManagerDelegate#/c:objc(pl)GADAudioVideoManagerDelegate(im)audioVideoManagerDidStopPlayingAudio:)


  ` Tells the delegate that all the video rendered by the Google Mobile Ads SDK has stopped playing
  sound. Your app can now resume any music playback or produce any kind of sound. Note that this
  message doesn't mean that all the video has stopped playing, just audio, so you shouldn't
  deactivate AVAudioSession's instance. Doing so can lead to unexpected video playback behavior.
  You may deactivate AVAudioSession only when all rendered video ads are paused or have finished
  playing, and 'audioVideoDidPauseAllVideo:' is called.

  #### Declaration

  Swift

      optional func audioVideoManagerDidStopPlayingAudio(_ audioVideoManager: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAudioVideoManager.html)
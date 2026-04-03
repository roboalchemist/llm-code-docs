# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADVideoControllerDelegate.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADVideoControllerDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADVideoControllerDelegate

    protocol GADVideoControllerDelegate : NSObjectProtocol

The GADVideoControllerDelegate protocol defines methods that are called by the video controller
object in response to the video events that occurred throughout the lifetime of the video
rendered by an ad.
- `
  ``
  ``
  `

  ### [videoControllerDidPlayVideo(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADVideoControllerDelegate#/c:objc(pl)GADVideoControllerDelegate(im)videoControllerDidPlayVideo:)

  `
  `  
  Tells the delegate that the video controller has began or resumed playing a video.  

  #### Declaration

  Swift  

      optional func videoControllerDidPlayVideo(_ videoController: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADVideoController.html)

- `
  ``
  ``
  `

  ### [videoControllerDidPauseVideo(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADVideoControllerDelegate#/c:objc(pl)GADVideoControllerDelegate(im)videoControllerDidPauseVideo:)

  `
  `  
  Tells the delegate that the video controller has paused video.  

  #### Declaration

  Swift  

      optional func videoControllerDidPauseVideo(_ videoController: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADVideoController.html)

- `
  ``
  ``
  `

  ### [videoControllerDidEndVideoPlayback(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADVideoControllerDelegate#/c:objc(pl)GADVideoControllerDelegate(im)videoControllerDidEndVideoPlayback:)

  `
  `  
  Tells the delegate that the video controller's video playback has ended.  

  #### Declaration

  Swift  

      optional func videoControllerDidEndVideoPlayback(_ videoController: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADVideoController.html)

- `
  ``
  ``
  `

  ### [videoControllerDidMuteVideo(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADVideoControllerDelegate#/c:objc(pl)GADVideoControllerDelegate(im)videoControllerDidMuteVideo:)

  `
  `  
  Tells the delegate that the video controller has muted video.  

  #### Declaration

  Swift  

      optional func videoControllerDidMuteVideo(_ videoController: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADVideoController.html)

- `
  ``
  ``
  `

  ### [videoControllerDidUnmuteVideo(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADVideoControllerDelegate#/c:objc(pl)GADVideoControllerDelegate(im)videoControllerDidUnmuteVideo:)

  `
  `  
  Tells the delegate that the video controller has unmuted video.  

  #### Declaration

  Swift  

      optional func videoControllerDidUnmuteVideo(_ videoController: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADVideoController.html)
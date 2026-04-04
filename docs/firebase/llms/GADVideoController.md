# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADVideoController.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADVideoController.md.txt

# GoogleMobileAds Framework Reference

# GADVideoController

    class GADVideoController : NSObject

The video controller class provides a way to get the video metadata and also manages video
content of the ad rendered by the Google Mobile Ads SDK. You don't need to create an instance of
this class. When the ad rendered by the Google Mobile Ads SDK loads video content, you may be
able to get an instance of this class from the rendered ad object.
- `
  ``
  ``
  `

  ### [delegate](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADVideoController#/c:objc(cs)GADVideoController(py)delegate)

  `
  `  
  Delegate for receiving video notifications.
- `
  ``
  ``
  `

  ### [setMute(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADVideoController#/c:objc(cs)GADVideoController(im)setMute:)

  `
  `  
  Mute or unmute video. Set to YES to mute the video. Set to NO to allow the video to play sound.  

  #### Declaration

  Swift  

      func setMute(_ mute: Bool)

- `
  ``
  ``
  `

  ### [play()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADVideoController#/c:objc(cs)GADVideoController(im)play)

  `
  `  
  Play the video. Doesn't do anything if the video is already playing.  

  #### Declaration

  Swift  

      func play()

- `
  ``
  ``
  `

  ### [pause()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADVideoController#/c:objc(cs)GADVideoController(im)pause)

  `
  `  
  Pause the video. Doesn't do anything if the video is already paused.  

  #### Declaration

  Swift  

      func pause()

- `
  ``
  ``
  `

  ### [stop()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADVideoController#/c:objc(cs)GADVideoController(im)stop)

  `
  `  
  Stops the video and displays the video's first frame. Call -play to resume playback at the start
  of the video. Contact your account manager to enable this feature.  

  #### Declaration

  Swift  

      func stop()

- `
  ``
  ``
  `

  ### [hasVideoContent()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADVideoController#/c:objc(cs)GADVideoController(im)hasVideoContent)

  `
  `  
  Returns a Boolean indicating if the receiver has video content.  

  #### Declaration

  Swift  

      func hasVideoContent() -> Bool

- `
  ``
  ``
  `

  ### [aspectRatio()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADVideoController#/c:objc(cs)GADVideoController(im)aspectRatio)

  `
  `  
  Returns the video's aspect ratio (width/height) or 0 if no video is present.  

  #### Declaration

  Swift  

      func aspectRatio() -> Double

- `
  ``
  ``
  `

  ### [customControlsEnabled()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADVideoController#/c:objc(cs)GADVideoController(im)customControlsEnabled)

  `
  `  
  Indicates whether video custom controls (i.e. play/pause/mute/unmute) are enabled.  

  #### Declaration

  Swift  

      func customControlsEnabled() -> Bool

- `
  ``
  ``
  `

  ### [clickToExpandEnabled()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADVideoController#/c:objc(cs)GADVideoController(im)clickToExpandEnabled)

  `
  `  
  Indicates whether video click to expand behavior is enabled.  

  #### Declaration

  Swift  

      func clickToExpandEnabled() -> Bool
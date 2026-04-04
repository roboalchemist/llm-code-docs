# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADVideoController.md.txt

# GoogleMobileAds Framework Reference

# GADVideoController

    @interface GADVideoController : NSObject

The video controller class provides a way to get the video metadata and also manages video
content of the ad rendered by the Google Mobile Ads SDK. You don't need to create an instance of
this class. When the ad rendered by the Google Mobile Ads SDK loads video content, you may be
able to get an instance of this class from the rendered ad object.
- `


  ### [delegate](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADVideoController#/c:objc(cs)GADVideoController(py)delegate)


  ` Delegate for receiving video notifications.

  #### Declaration

  Objective-C

      @property (readwrite, nonatomic, nullable) id<https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADVideoControllerDelegate.html>
          delegate;

- `


  ### [-setMute:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADVideoController#/c:objc(cs)GADVideoController(im)setMute:)


  ` Mute or unmute video. Set to YES to mute the video. Set to NO to allow the video to play sound.

  #### Declaration

  Objective-C

      - (void)setMute:(BOOL)mute;

- `


  ### [-play](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADVideoController#/c:objc(cs)GADVideoController(im)play)


  ` Play the video. Doesn't do anything if the video is already playing.

  #### Declaration

  Objective-C

      - (void)play;

- `


  ### [-pause](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADVideoController#/c:objc(cs)GADVideoController(im)pause)


  ` Pause the video. Doesn't do anything if the video is already paused.

  #### Declaration

  Objective-C

      - (void)pause;

- `


  ### [-stop](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADVideoController#/c:objc(cs)GADVideoController(im)stop)


  ` Stops the video and displays the video's first frame. Call -play to resume playback at the start
  of the video. Contact your account manager to enable this feature.

  #### Declaration

  Objective-C

      - (void)stop;

- `


  ### [-hasVideoContent](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADVideoController#/c:objc(cs)GADVideoController(im)hasVideoContent)


  ` Returns a Boolean indicating if the receiver has video content.

  #### Declaration

  Objective-C

      - (BOOL)hasVideoContent;

- `


  ### [-aspectRatio](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADVideoController#/c:objc(cs)GADVideoController(im)aspectRatio)


  ` Returns the video's aspect ratio (width/height) or 0 if no video is present.

  #### Declaration

  Objective-C

      - (double)aspectRatio;

- `


  ### [-customControlsEnabled](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADVideoController#/c:objc(cs)GADVideoController(im)customControlsEnabled)


  ` Indicates whether video custom controls (i.e. play/pause/mute/unmute) are enabled.

  #### Declaration

  Objective-C

      - (BOOL)customControlsEnabled;

- `


  ### [-clickToExpandEnabled](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADVideoController#/c:objc(cs)GADVideoController(im)clickToExpandEnabled)


  ` Indicates whether video click to expand behavior is enabled.

  #### Declaration

  Objective-C

      - (BOOL)clickToExpandEnabled;
# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADVideoControllerDelegate.md.txt

# GoogleMobileAds Framework Reference

# GADVideoControllerDelegate

    @protocol GADVideoControllerDelegate <NSObject>

The GADVideoControllerDelegate protocol defines methods that are called by the video controller
object in response to the video events that occurred throughout the lifetime of the video
rendered by an ad.
- `


  ### [-videoControllerDidPlayVideo:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADVideoControllerDelegate#/c:objc(pl)GADVideoControllerDelegate(im)videoControllerDidPlayVideo:)


  ` Tells the delegate that the video controller has began or resumed playing a video.

  #### Declaration

  Objective-C

      - (void)videoControllerDidPlayVideo:
          (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADVideoController.html *)videoController;

- `


  ### [-videoControllerDidPauseVideo:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADVideoControllerDelegate#/c:objc(pl)GADVideoControllerDelegate(im)videoControllerDidPauseVideo:)


  ` Tells the delegate that the video controller has paused video.

  #### Declaration

  Objective-C

      - (void)videoControllerDidPauseVideo:
          (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADVideoController.html *)videoController;

- `


  ### [-videoControllerDidEndVideoPlayback:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADVideoControllerDelegate#/c:objc(pl)GADVideoControllerDelegate(im)videoControllerDidEndVideoPlayback:)


  ` Tells the delegate that the video controller's video playback has ended.

  #### Declaration

  Objective-C

      - (void)videoControllerDidEndVideoPlayback:
          (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADVideoController.html *)videoController;

- `


  ### [-videoControllerDidMuteVideo:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADVideoControllerDelegate#/c:objc(pl)GADVideoControllerDelegate(im)videoControllerDidMuteVideo:)


  ` Tells the delegate that the video controller has muted video.

  #### Declaration

  Objective-C

      - (void)videoControllerDidMuteVideo:
          (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADVideoController.html *)videoController;

- `


  ### [-videoControllerDidUnmuteVideo:](https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADVideoControllerDelegate#/c:objc(pl)GADVideoControllerDelegate(im)videoControllerDidUnmuteVideo:)


  ` Tells the delegate that the video controller has unmuted video.

  #### Declaration

  Objective-C

      - (void)videoControllerDidUnmuteVideo:
          (nonnull https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADVideoController.html *)videoController;
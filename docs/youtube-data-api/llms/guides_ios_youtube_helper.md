# Source: https://developers.google.com/youtube/v3/guides/ios_youtube_helper.md.txt

# Embed YouTube Videos in iOS Applications with the YouTube Helper Library

The `youtube-ios-player-helper` is an open source library that helps you embed a
YouTube iframe player into an iOS application. The library creates a
`WebView` and a bridge between your application's Objective-C code and the
YouTube player's JavaScript code, thereby allowing the iOS application to control the
YouTube player. This article describes the steps to install the library and get started
using it from your iOS application.

## Installation

This article assumes you have created a new Single View Application iOS project targeting
the latest version of iOS, and that you add the following files when creating the
project:

- `Main.storyboard`
- `ViewController.h`
- `ViewController.m`

You can install the library via
[CocoaPods](https://cocoapods.org/) or by copying the library
and source files from the
[project's GitHub page](https://github.com/youtube/youtube-ios-player-helper).

- The library is available to install via CocoaPods. Alternatively, the library and source files are available via the project's GitHub page and can be copied into an existing project.

### Install the library via CocoaPods

If your project uses CocoaPods, add the line below to your Podfile to install the library.
In that line, replace `x.y.z` with the latest pod version, which will be
identified on the project's GitHub page.  

```text
pod "youtube-ios-player-helper", "~> x.y.z"
```

At the command line prompt, type `pod install` to update your workspace with the
dependencies.

Tip: Remember that when using CocoaPods, you must open the `.xcworkspace` file
in Xcode, not the `.xcodeproj` file.

Check out the [CocoaPods
tutorial](https://guides.cocoapods.org/using/getting-started.html) to learn more.

### Manually install the library

To install the helper library manually, either download the source via
[GitHub's download link](https://github.com/youtube/youtube-ios-player-helper) or
clone the repository. Once you have a local copy of the code, follow these steps:

1. Open the sample project in Xcode or Finder.

2. Select `YTPlayerView.h`, `YTPlayerView.m`, and the
   **Assets** folder. If you open the workspace in Xcode, these are available
   under **Pods -\> Development Pods -\> YouTube-Player-iOS-Helper** and
   **Pods -\> Development Pods -\> YouTube-Player-iOS-Helper -\> Resources** . In the Finder,
   these are available in the project's root directory in the **Classes** and
   **Assets** directories.

3. Drag these files and folders into your project. Make sure the **Copy items into
   destination group's folder** option is checked. When dragging the Assets folder, make
   sure that the **Create Folder References for any added folders** option is
   checked.

The library should now be installed.

## Add a `YTPlayerView` via Interface Builder or the Storyboard

To add a `YTPlayerView` via Interface Builder or the Storyboard:

1. Drag a `UIView` instance onto your View.

2. Select the Identity Inspector and change the class of the view to
   `YTPlayerView`.

3. Open `ViewController.h` and add the following header:

   ```objective-c
   #import "YTPlayerView.h"
   ```

   Also add the following property:  

   ```objective-c
   @property(nonatomic, strong) IBOutlet YTPlayerView *playerView;
   ```
4. In Interface Builder, create a connection from the View element that you defined in the
   previous step to your View Controller's `playerView` property.

5. Now open `ViewController.m` and add the following code to the end of your
   `viewDidLoad` method:

   ```objective-c
   [self.playerView loadWithVideoId:@"M7lc1UVf-VE"];
   ```

Build and run your application. When the video thumbnail loads, tap the video thumbnail to
launch the fullscreen video player.

## Control video playback

The `ViewController::loadWithVideoId:` method has a variant,
`loadWithVideoId:playerVars:`, that allows developers to pass additional player
variables to the view. These player variables correspond to the
[player parameters in the
IFrame Player API](https://developers.google.com/youtube/player_parameters). The `playsinline` parameter enables the video to play
directly in the view rather than playing fullscreen. When a video is playing inline, the
containing iOS application can programmatically control playback.

Replace the `loadWithVideoId:` call with this code:  

```objective-c
NSDictionary *playerVars = @{
  @"playsinline" : @1,
};
[self.playerView loadWithVideoId:@"M7lc1UVf-VE" playerVars:playerVars];
```

Open up the storyboard or Interface Builder. Drag two buttons onto your View, labeling them
**Play** and **Stop** . Open `ViewController.h` and add these methods, which
will be mapped to the buttons:  

```objective-c
- (IBAction)playVideo:(id)sender;
- (IBAction)stopVideo:(id)sender;
```

Now open `ViewController.m` and define these two functions:  

```objective-c
- (IBAction)playVideo:(id)sender {
  [self.playerView playVideo];
}

- (IBAction)stopVideo:(id)sender {
  [self.playerView stopVideo];
}
```

Most of the IFrame Player API functions have Objective-C equivalents, though some of the
naming may differ slightly to more closely match Objective-C coding guidelines. Notable
exceptions are methods controlling the volume of the video, since these are controlled by
the phone hardware or with built in `UIView` instances designed for this purpose,
such as [`MPVolumeView`](https://developer.apple.com/library/ios/documentation/mediaplayer/reference/MPVolumeView_Class/Reference/Reference.html).

Open your storyboard or Interface Builder and control-drag to connect the **Play** and
**Stop** buttons to the `playVideo:` and `stopVideo:` methods.

Now build and run the application. Once the video thumbnail loads, you should be able to
play and stop the video using native controls in addition to the player controls.

## Handle player callbacks

It can be useful to programmatically handle playback events, such as playback state changes
and playback errors. In the JavaScript API, this is done with
[event listeners](https://developers.google.com/youtube/iframe_api_reference#Adding_event_listener).
In Objective-C,this is done with a
[delegate](https://developer.apple.com/library/ios/documentation/general/conceptual/CocoaEncyclopedia/DelegatesandDataSources/DelegatesandDataSources.html).


The following code shows how to update the interface declaration in
`ViewController.h` so the class conforms to the delegate protocol. Change
`ViewController.h`'s interface declaration as follows:  

```objective-c
@interface ViewController : UIViewController<YTPlayerViewDelegate>
```

`YTPlayerViewDelegate` is a protocol for handling playback events in the player.
To update `ViewController.m` to handle some of the events, you first need to set
the `ViewController` instance as the delegate of the `YTPlayerView`
instance. To make this change, add the following line to the `viewDidLoad` method
in `ViewController.h`.  

```objective-c
self.playerView.delegate = self;
```

Now add the following method to `ViewController.m`:  

```objective-c
- (void)playerView:(YTPlayerView *)playerView didChangeToState:(YTPlayerState)state {
  switch (state) {
    case kYTPlayerStatePlaying:
      NSLog(@"Started playback");
      break;
    case kYTPlayerStatePaused:
      NSLog(@"Paused playback");
      break;
    default:
      break;
  }
}
```

Build and run the application. Watch the log output in Xcode as the player state changes.
You should see updates when the video is played or stopped.

The library provides the constants that begin with the `kYT*` prefix for
convenience and readability. For a full list of these constants, look at
`YTPlayerView.m`.

## Best practices and limitations

The library builds on top of the IFrame Player API by creating a `WebView` and
rendering the HTML and JavaScript required for a basic player. The library's goal is to be
as easy-to-use as possible, bundling methods that developers frequently have to write into a
package. There are a few limitations that should be noted:

- The library does not support concurrent video playback in multiple `YTPlayerView` instances. If your application has multiple `YTPlayerView` instances, a recommended best practice is to pause or stop playback in any existing instances before starting playback in a different instance. In the example application that ships with the project, the ViewControllers make use of `NSNotificationCenter` to dispatch notifications that playback is about to begin. Other ViewControllers are notified and will pause playback in their `YTPlayerView` instances.
- Reuse your existing, loaded `YTPlayerView` instances when possible. When a video needs to be changed in a View, don't create a new `UIView` instance or a new `YTPlayerView` instance, and don't call either `loadVideoId:` or `loadPlaylistId:`. Instead, use the `cueVideoById:startSeconds:` family of functions, which do not reload the `WebView`. There is a noticeable delay when loading the entire IFrame player.
- This player cannot play private videos, but it can play [unlisted videos](https://support.google.com/youtube/answer/157177). Since this library wraps the existing iframe player, the player's behavior should be nearly identical to that of a player embedded on a webpage in a mobile browser.

## Contributions

Since this is an open-source project, please submit fixes and improvements to the
[master branch of the GitHub
project](https://github.com/youtube/youtube-ios-player-helper).
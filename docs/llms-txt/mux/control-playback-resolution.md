# Source: https://www.mux.com/docs/guides/control-playback-resolution.md

# Control playback resolution
Control the video resolution your users receive in order to give the best user experience as well as take advantage of Mux's resolution based pricing.
# Default playback URL

The default playback URL will contain all available resolutions of your video. The resolutions available will depend on the video source file.

By default if the source file contains 1080p or higher, then the highest resolution provided by Mux will be 1080p. If the source file is lower than 1080p, the highest resolution available will be the resolution of the source.

You can also stream 4K content using Mux Video, which will be delivered at higher resolutions including 2.5K and 4K. For more details see the [guide to streaming 4K videos](/docs/guides/stream-videos-in-4k).

```
https://stream.mux.com/{PLAYBACK_ID}.m3u8
```

Use the default playback URL for most use cases. The video player will determine the best resolution based on the available bandwidth of the viewer.

# Using playback modifiers to manipulate playback resolution

Mux exposes a set of [playback modifiers](/docs/guides/modify-playback-behavior), which give you extra control over the availiable resolutions of your content.

## Specify maximum resolution

The playback URL below with the `max_resolution` query parameter modifies the resolutions available for the player to choose from.

```
https://stream.mux.com/{PLAYBACK_ID}.m3u8?max_resolution=720p
```

The `max_resolution` parameter can be set to `270p`, `360p`, `480p`, `540p`, `720p`, `1080p`, `1440p`, or `2160p`. You may want to do this in order to reduce your delivery costs, or build a feature to your product where only certain viewers get lower resolution video.

*Please note that not all resolutions are available for all assets. If you specify a max resolution that is not available for the asset, Mux will limit the resolution to the highest resolution available below the one you specified. For example, if you specify `max_resolution=1080p` but the highest resolution available for the asset is 720p, then the manifest will be capped at 720p.*

## Specify minimum resolution

The playback URL below with the `min_resolution` query parameter modifies the resolutions available for the player to choose from.

```
https://stream.mux.com/{PLAYBACK_ID}.m3u8?min_resolution=720p
```

The `min_resolution` parameter can be set to `270p`, `360p`, `480p`, `540p`, `720p`, `1080p`, `1440p`, or `2160p`. You may want to use this to omit the lowest quality renditions from the HLS manifest when the visual quality of your content is critical to the delivery, for example in live streams where detailed screen share content is present.

*Please note that not all resolutions are available for all assets. If you specify a min resolution that is not available for the asset, Mux will limit the resolution to the next highest resolution available below the one you specified. For example, if you specify `max_resolution=270p` but the lowest resolution available for the asset is 360p, then the manifest will start at at 360p.*

## Specify rendition order

By default the top resolution in the playlist is one of the middle resolutions. Many players will start with the first one listed so this default behavior strikes a balance by giving the player something that's not too low in terms of quality but also not too high in terms of bandwidth.

You may want to change this behavior by specifying `rendition_order=desc` which will sort the list of renditions from highest (highest quality, most bandwidth) to lowest (lowest quality, least bandwidth). Players that start with the first rendition in the list will now attempt to start playback with the highest resolution. The tradeoff is that users on slow connections will experience increaesed startup time.

```
https://stream.mux.com/{PLAYBACK_ID}.m3u8?rendition_order=desc
```

# Usage with signed URLs

If you are using `signed` Playback IDs according to the [Secure video playback guide](/docs/guides/secure-video-playback) then your playback modifiers must be encoded in the `token` that you generate on your server. [See the modify playback behaviour guide](/docs/guides/modify-playback-behavior) about embedding extra params in your JWT.

# Using playback modifiers in Mux Player

Mux Player supports  `min_resolution`, `max_resolution` and `rendition_order` as attributes on the web component and props on the React component.

For example to set the `max_resolution=` parameter with Mux Player, you can set `max-resolution="720p"` attribute (`maxResolution="720p"` in React). When setting this attribute Mux Player will internally add it on as a query parameter on the streaming URL.

As with all playback modifiers, if you're using signed URLs, your parameters should be encoded in the `playback-token` attribute (`tokens.playback` in React).

# When using AVPlayer on iOS

Set the playback modifier by appending a `URLQueryItem` to the playback `URL`. [Initialize `AVPlayer` using the `URL` itself](https://developer.apple.com/documentation/avfoundation/avplayer/1385706-init) as shown in an example below using `max_resolution` or [initialize with an `AVPlayerItem` constructed with the URL](https://developer.apple.com/documentation/avfoundation/avplayer/1387104-init).

```objc


/// Creates a playback URL.
///
/// - Parameters:
///     - playbackID: playback ID for the asset.
///     - enableMaximumResolution: if true include a query parameter 
///     that sets a maximum resolution for the video.
///
/// - Returns: Playback URL with maximum resolution query param appended.
///
- (NSURL *)playbackURLWithPlaybackID:(NSString *)playbackID
           enableMaximumResolution:(BOOL)enableMaximumResolution {
  if (enableMaximumResolution) {
      NSURLComponents *components = [
          NSURLComponents componentsWithURL: [NSURL URLWithString: @"https://stream.mux.com/"]
          resolvingAgainstBaseURL: NO
      ];
      components.path = [NSString stringWithFormat: @"%@.m3u8", playbackID];

      NSURLQueryItem *queryItem = [
          NSURLQueryItem queryItemWithName: @"max_resolution"
          value: @"720p"
      ];
      components.queryItems = @[queryItem];

      return [components URL];
  } else {
      NSString *formattedURLString = [
          NSString stringWithFormat: @"https://stream.mux.com/%@.m3u8", playbackID
      ];
      return [NSURL URLWithString: formattedURLString];
  }
}

NSString *playbackID = @"qxb01i6T202018GFS02vp9RIe01icTcDCjVzQpmaB00CUisJ4";

NSURL *url = [self playbackURLWithPlaybackID: playbackID
                     enableMaximumResolution: NO];

AVPlayerItem *playerItem = [[AVPlayerItem alloc] initWithURL: url];
AVPlayer *player = [[AVPlayer alloc] initWithPlayerItem: playerItem];
 
```

```swift

import AVKit
import Foundation

let playbackID = "qxb01i6T202018GFS02vp9RIe01icTcDCjVzQpmaB00CUisJ4"

// Flag controlling if a max resolution is requested
let shouldLimitResolutionTo720p = true

let player = AVPlayer(
    using: playbackID,
    limitResolutionTo720p: shouldLimitResolutionTo720p
)

extension AVPlayer {
    /// Initializes a player configured to stream
    /// the provided asset's playback ID.
    /// - Parameters:
    ///   - playbackID: a playback ID of your asset
    ///   - limitResolutionTo720p: if true configures
    ///   the player to select a resolution no higher
    ///   than 720p. False by default. 
    convenience init(
        using playbackID: String,
        limitResolutionTo720p: Bool = false
    ) {
        let playbackURL = URL.makePlaybackURL(
            playbackID: playbackID,
            limitResolutionTo720p: limitResolutionTo720p
        )
        
        self.init(
            url: playbackURL
        )
    }
}

/// Convenience extensions for working with URLs
extension URL {
    /// Convenience initializer for a static URL
    /// - Parameters:
    ///   - staticString: a static representation
    ///   of a valid URL, supplying an invalid URL
    ///   results in precondition failure
    init(staticString: StaticString) {
        guard let url = URL(
            string: "\(staticString)"
        ) else {
            preconditionFailure("Invalid URL static string")
        }

        self = url
    }

    /// Convenience constructor for a playback URL with
    /// an optional 720p limit
    /// - Parameters:
    ///     - baseURL: either the Mux stream URL or can be
    ///     customized if using Custom Domains for Mux Video.
    ///     - playbackID: playback ID for the asset
    ///     - limitResolutionTo720p: set an upper threshold for the
    ///     resolution chosen by the player to 720p. By default no limit 
    ///     is set and the player can choose any available resolution.
    /// - Returns: a playback URL for a Mux Video asset with a resolution
    /// limit if it is requested
    static func makePlaybackURL(
        baseURL: StaticString = "https://stream.mux.com",
        playbackID: String,
        limitResolutionTo720p: Bool = false
     ) -> URL {
        var components = URLComponents(
            url: URL(
                staticString: baseURL
            ),
            resolvingAgainstBaseURL: false
        )

        components?.path = "/\(playbackID).m3u8"

        if limitResolutionTo720p {
            components?.queryItems = [
                URLQueryItem(
                    name: "max_resolution",
                    value: "720p"
                )
            ]
        }
    
        guard let playbackURL = components?.url else {
            preconditionFailure("Invalid playback URL component")
        }

        return playbackURL
     }
}

```


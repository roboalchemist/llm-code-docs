# Source: https://www.mux.com/docs/guides/monitor-shaka-player.md

# Monitor Shaka player
This guide walks through integration with Shaka player to collect video performance metrics with Mux Data.
## Features

The following data can be collected by the Mux Data SDK when you use the \{featureDef.name} SDK, as described
&#x20;       below.

```md
- Engagement metrics
- Quality of Experience Metrics
- Web metrics such as Player Startup Time, Page Load Time, etc
- Available for deployment from a package manager
- Can infer CDN identification from response headers
- Custom Dimensions
- Average Bitrate metrics and `renditionchange` events
- Request metrics
- Customizable Error Tracking
- Custom Beacon Domain
- Extraction of HLS Session Data

```

Notes:

```md
Request Latency is not available.
```

## 1. Install \`@mux/mux-data-shakaplayer\`

Include the Mux JavaScript SDK on every page of your web app that includes video.

```npm
npm install --save @mux/mux-data-shakaplayer
```

```yarn
yarn add @mux/mux-data-shakaplayer
```

```cdn
<script src="https://src.litix.io/shakaplayer/5/shakaplayer-mux.js"></script>
```



## 2. Initialize Mux Data

Get your `ENV_KEY` from the [Mux environments dashboard](https://dashboard.mux.com/environments).

<Callout type="info" title="Env Key is different than your API token">
  `ENV_KEY` is a client-side key used for Mux Data monitoring. These are not to be confused with API tokens which are created in the admin settings dashboard and meant to access the Mux API from a trusted server.
</Callout>

<Image src="/docs/images/env-key.png" width={2004} height={250} />

Call `new shaka.Player` like you normally would and get the return value (a reference to the `player`). Call `initShakaPlayerMux` with the player reference and the SDK options.

```html

<div id="my-player"></div>
<script>
  const playerInitTime = initShakaPlayerMux.utils.now();
  const video = document.querySelector('#my-player');
  const player = new shaka.Player(video);

  // calling initShakaPlayerMux will return a shakaPlayerMux object
  // you will need this for handling any errors when calling
  // player.load()
  const shakaPlayerMux = initShakaPlayerMux(player, {
    debug: false,
    data: {
      env_key: 'ENV_KEY',
      // Metadata
      player_name: 'Custom Player', // ex: 'My Main Player',
      player_init_time: playerInitTime // ex: 1451606400000
      // ... and other metadata
    }
  });

  player.load('https://stream.mux.com/yb2L3z3Z4IKQH02HYkf9xPToVYkOC85WA.m3u8').then(function () {
    // Successfully loaded the manifest. Mux data will begin tracking
  }).catch(function (error) {
    // There was an error loading this manifest. Call shakaPlayerMux.loadErrorHandler(error) so that Mux data can track this error.
    shakaPlayerMux.loadErrorHandler(error);
    // Do the rest of your error handling logic
  })

  // When you are ready to destroy shakaplayer, you must also destroy
  // the mux monitor
  player.destroy()
  player.mux.destroy()
</script>

```

```javascript

import shaka from "shaka-player";
import initShakaPlayerMux from "@mux/mux-data-shakaplayer";

const playerInitTime = initShakaPlayerMux.utils.now();
const video = document.querySelector('#my-player');
const player = new shaka.Player(video);


// calling initShakaPlayerMux will return a shakaPlayerMux object
// you will need this for handling any errors when calling
// player.load()
const shakaPlayerMux = initShakaPlayerMux(player, {
  debug: false,
  data: {
    env_key: 'ENV_KEY',
    // Metadata
    player_name: 'Custom Player', // ex: 'My Main Player',
    player_init_time: playerInitTime // ex: 1451606400000
    // ... and other metadata
  }
}, shaka);

player.load('https://stream.mux.com/yb2L3z3Z4IKQH02HYkf9xPToVYkOC85WA.m3u8').then(function () {
  // Successfully loaded the manifest. Mux data will begin tracking
}).catch(function (error) {
  // There was an error loading this manifest. Call shakaPlayerMux.loadErrorHandler(error) so that Mux data can track this error.
  shakaPlayerMux.loadErrorHandler(error);
  // Do the rest of your error handling logic
})
// When you are ready to destroy shakaplayer, you must also destroy
// the mux monitor:
// player.destroy()
// player.mux.destroy()

```



## Passing in `shaka` global

You'll see the 3rd argument to `initShakaPlayerMux` is `shaka`. This is the global `shaka` object. If you are using a bundler and importing `shaka` with `require` or `import` then you'll need to pass in the `shaka` object.

If no `shaka` object is passed in, then `initShakaPlayerMux` will look for `shaka` on then global `window` object.

## 3. Make your data actionable

The only required field in the `options` that you pass into `@mux/mux-data-shakaplayer` is `env_key`. But without some metadata the metrics in your dashboard will lack the necessary information to take meaningful actions. Metadata allows you to search and filter on important fields in order to diagnose issues and optimize the playback experience for your end users.

Pass in metadata under the `data` on initialization.

```js
initShakaPlayerMux(player, {
  debug: false,
  data: {
    env_key: 'ENV_KEY',
    // Site Metadata
    viewer_user_id: '', // ex: '12345'
    experiment_name: '', // ex: 'player_test_A'
    sub_property_id: '', // ex: 'cus-1'
    // Player Metadata
    player_name: '', // ex: 'My Main Player'
    player_version: '', // ex: '1.0.0'
    player_init_time: '', // ex: 1451606400000
    // Video Metadata
    video_id: '', // ex: 'abcd123'
    video_title: '', // ex: 'My Great Video'
    video_series: '', // ex: 'Weekly Great Videos'
    video_duration: '', // in milliseconds, ex: 120000
    video_stream_type: '', // 'live' or 'on-demand'
    video_cdn: '' // ex: 'Fastly', 'Akamai'
  }
});
```

For more information, view [Make your data actionable](/docs/guides/make-your-data-actionable-with-metadata).

## 4. Set or update metadata after initialization

There are some cases where you may not have the full set of metadata until after the video playback has started. In this case, you should omit the values when you first call `initShakaPlayerMux`. Then, once you have the metadata, you can update the metadata with the `updateData` method.

```js
// player is the instance returned by `new shaka.Player`
player.mux.updateData({ video_title: 'My Updated Great Video' });
```

## 5. Changing the video

There are two cases where the underlying tracking of the video view need to be reset:

1. **New source:** When you load a new source URL into an existing player.
2. **New program:** When the program within a singular stream changes (such as a program change within a continuous live stream).

Note: You do not need to change the video info when changing to a different source of the same video content (e.g. different resolution or video format).

### New source

If your application plays multiple videos back-to-back in the same video player, you need to signal when a new video starts to the Mux SDK. Examples of when this is needed are:

* The player advances to the next video in a playlist
* The user selects a different video to play

In order to signal the Mux SDK that a new view is starting, you will need to emit a `videochange` event, along with metadata about the new video. See metadata in [Make your data actionable](/docs/guides/make-your-data-actionable-with-metadata) for the full list of video details you can provide. You can include any metadata when changing the video but you should only need to update the values that start with `video_`.

It's best to change the video info immediately after telling the player which new source to play.

```js
// player is the instance returned by `new shaka.Player`
player.mux.emit('videochange', {
  video_id: 'abc345',
  video_title: 'My Other Great Video',
  video_series: 'Weekly Great Videos',
  // ...
});
```

### New program

In some cases, you may have the program change within a stream, and you may want to track each program as a view on its own. An example of this is a live stream that streams multiple programs back to back, with no interruptions.

In this case, you emit a `programchange` event, including the updated metadata for the new program within the continuous stream. This will remove all previous video data and reset all metrics for the video view, creating a new video view. See [Metadata](/docs/guides/make-your-data-actionable-with-metadata) for the list of video details you can provide. You can include any metadata when changing the video but you should only need to update the values that start with `video`.

Note: The `programchange` event is intended to be used *only* while the player is currently not paused. If you emit this event while the player is paused, the resulting view will not track video startup time correctly, and may also have incorrect watch time. Do not emit this event while the player is paused.

```js
// player is the instance returned by `new shaka.Player`
player.mux.emit('programchange', {
  video_id: 'abc345',
  video_title: 'My Other Great Video',
  video_series: 'Weekly Great Videos',
  // ...
});
```

## 6. Advanced options

### Disable cookies

By default, Mux plugins for HTML5-based players use a cookie to track playback across subsequent page views in order to understand viewing sessions. This cookie includes information about the tracking of the viewer, such as an anonymized viewer ID that Mux generates for each user. None of this information is personally-identifiable, but you can disable the use of this cookie if desired. For instance, if your site or application is targeted towards children under 13, you should disable the use of cookies. For information about the specific data tracked in the cookie, please refer to: [What information is stored in Mux Data HTML cookies](/docs/guides/ensure-data-privacy-compliance#what-information-is-stored-in-mux-data-html-cookies).

This is done by setting `disableCookies: true` in the options.

```js
// player is the instance returned by `new shaka.Player`
initShakaPlayerMux(player, {
  debug: false,
  disableCookies: true,
  data: {
    env_key: "ENV_KEY",
    // ...
});
```

### Over-ride 'do not track' behavior

By default, Mux plugins for HTML5-based players do not respect [Do Not Track](https://www.eff.org/issues/do-not-track) when set within browsers. This can be enabled in the options passed to Mux, via a setting named `respectDoNotTrack`. The default for this is `false`. If you would like to change this behavior, pass `respectDoNotTrack: true`.

```js
// player is the instance returned by `new shaka.Player`
initShakaPlayerMux(player, {
  debug: false,
  respectDoNotTrack: true,
  data: {
    env_key: "ENV_KEY",
    // ...
});
```

### Customize error tracking behavior

<Callout type="error" title="Errors are fatal">
  Errors tracked by mux are considered fatal meaning that they are the result of playback failures. If errors are non-fatal they should not be captured.
</Callout>

By default, `@mux/mux-data-shakaplayer` will track errors emitted from the video element as fatal errors. If a fatal error happens outside of the context of the player, you can emit a custom error to the mux monitor.

```js
// player is the instance returned by `new shaka.Player`
player.mux.emit('error', {
  player_error_code: 100,
  player_error_message: 'Description of error',
  player_error_context: 'Additional context for the error'
});
```

When triggering an error event, it is important to provide values for `player_error_code` and `player_error_message`. The `player_error_message` should provide a generalized description of the error as it happened. The `player_error_code` must be an integer, and should provide a category of the error. If the errors match up with the [HTML Media Element Error](https://developer.mozilla.org/en-US/docs/Web/API/MediaError), you can use the same codes as the corresponding HTML errors. However, for custom errors, you should choose a number greater than or equal to `100`.

In general you should not send a distinct code for each possible error message, but rather group similar errors under the same code. For instance, if your library has two different conditions for network errors, both should have the same `player_error_code` but different messages.

The error message and code are combined together and aggregated with all errors that occur in your environment in order to find the most common errors that occur. To make error aggregation as useful as possible, these values should be general enough to provide useful information but not specific to each individual error (such as stack trace).

You can use `player_error_context` to provide instance-specific information derived from the error such as stack trace or segment-ids where an error occurred. This value is not aggregated with other errors and can be used to provide detailed information. *Note: Please do not include any personally identifiable information from the viewer in this data.*

### Error translator

If your player emits error events that are not fatal to playback or the errors are unclear and/or do not have helpful information in the default error message and codes you might find it helpful to use an error translator or disable automatic error tracking all together.

```js
function errorTranslator (error) {
  return {
    player_error_code: translateCode(error.player_error_code),
    player_error_message: translateMessage(error.player_error_message),
    player_error_context: translateContext(error.player_error_context)
  };
}

// player is the instance returned by `new shaka.Player`
initShakaPlayerMux(player, {
  debug: false,
  errorTranslator,
  data: {
    env_key: "ENV_KEY",
    // ...
  }
});
```

If you return `false` from your `errorTranslator` function then the error will not be tracked. Do this for non-fatal errors that you want to ignore. If your `errorTranslator` function itself raises an error, then it will be silenced and the player's original error will be used.

### Disable automatic error tracking

In the case that you want full control over what errors are counted as fatal or not, you may want to consider turning off Mux's automatic error tracking completely. This can be done by passing `automaticErrorTracking: false` in the configuration object.

```js
// player is the instance returned by `new shaka.Player`
initShakaPlayerMux(player, {
  debug: false,
  automaticErrorTracking: false,
  data: {
    env_key: "ENV_KEY",
    // ...
  }
});
```

### Track Ad playback with a custom integration

Our integration for Shaka player does not have a built-in integration for tracking ad playback. If you would like to track ads played within Shaka player, you will need to build a custom integration, which is detailed here: [Build a Custom Integration](/docs/guides/build-a-custom-data-integration).

### Customize beacon collection domain

If you have [integrated a custom domain for Data collection](/docs/guides/integrate-a-data-custom-domain), specify your custom domain by setting `beaconCollectionDomain`.

```js
// player is the instance returned by `new shaka.Player`
initShakaPlayerMux(player, {
  debug: false,
  beaconCollectionDomain: 'CUSTOM_DOMAIN', // ex: 'foo.bar.com'
  data: {
    env_key: "ENV_KEY",
    // ...
  }
});
```

<LinkedHeader step={steps[7]} />

### Current release

#### v5.14.18

* fix issue where playing time might accumulate for paused players
  * Updated dependency: `mux-embed` to v5.17.1

### Previous releases

#### v5.14.17

* add compatibility for dash.js 5
  * Updated dependency: `mux-embed` to v5.17.0

#### v5.14.16

* Update parsing of initial value for player\_playback\_mode
  * Updated dependency: `mux-embed` to v5.16.1

#### v5.14.15

* Add Playback Range Tracker for new engagement metrics
  * Updated dependency: `mux-embed` to v5.16.0

#### v5.14.14

* Automatically detect playback mode changes for HTML 5 Video
  * Updated dependency: `mux-embed` to v5.15.0

#### v5.14.13

* Emit a renditionchange event at the start of views to eanble updated rendition tracking.
  * Updated dependency: `mux-embed` to v5.14.0

#### v5.14.12

* Add ad type metadata to Ad Events
* Add support for the upcoming Playback Mode changes:
  * Updated dependency: `mux-embed` to v5.13.0

#### v5.14.11

* SDKs will no longer immediately send error events that are flagged as warnings. Fatal errors will still immediately be sent.
  * Updated dependency: `mux-embed` to v5.12.0

#### v5.14.10

* Allow dev to specify page starting load and page finished loading times to calculate Page Load Time
  * Updated dependency: `mux-embed` to v5.11.0

#### v5.14.9

* Adds support for cdnchange events
  * Updated dependency: `mux-embed` to v5.10.0

#### v5.14.8

* Submit Aggregate Startup Time when autoplay is set
  * Updated dependency: `mux-embed` to v5.9.1

#### v5.14.7

* Update `mux-embed` to v5.9.0

#### v5.14.6

* Update `mux-embed` to v5.8.3

#### v5.14.5

* Update `mux-embed` to v5.8.2

#### v5.14.4

* Update `mux-embed` to v5.8.1

#### v5.14.3

* Update `mux-embed` to v5.8.0

#### v5.14.2

* Update `mux-embed` to v5.7.0

#### v5.14.1

* Update `mux-embed` to v5.6.0

#### v5.14.0

* Update mechanism for generating unique IDs, used for `view_id` and others

* Update `mux-embed` to v5.5.0

#### v5.13.3

* \[chore] internal build process fix (no functional changes)
* Update `mux-embed` to v5.4.3

#### v5.13.2

* Update `mux-embed` to v5.4.2

#### v5.13.1

* Update `mux-embed` to v5.4.1

#### v5.13.0

* Add updateData function that allows Mux Data metadata to be updated mid-view.

* Update `mux-embed` to v5.4.0

#### v5.12.8

* Update `mux-embed` to v5.3.3

#### v5.12.7

* Update `mux-embed` to v5.3.2

#### v5.12.6

* Update `mux-embed` to v5.3.1

#### v5.12.5

* Update `mux-embed` to v5.3.0

#### v5.12.4

* fix an issue where `[Object object]` would be returned in error\_context at times

#### v5.12.3

* Update `mux-embed` to v5.2.1

#### v5.12.2

* Update `mux-embed` to v5.2.0

#### v5.12.1

* Resolve Shaka crash if `response.data` is not present

#### v5.12.0

* Target ES5 for bundles and validate bundles are ES5

* Update `mux-embed` to v5.1.0

#### v5.11.0

* tsignore added due to new TypeScript types (types not fully applied yet)

* Update `mux-embed` to v5.0.0

#### v5.10.5

* Update `mux-embed` to v4.30.0

#### v5.10.4

* Update `mux-embed` to v4.29.0

#### v5.10.3

* Only submit requestcompleted events for the manifest, media, and encryption requests

#### v5.10.2

* Update `mux-embed` to v4.28.1

#### v5.10.1

* Update `mux-embed` to v4.28.0

#### v5.10.0

* fix an issue where seek latency could be unexpectedly large

* fix an issue where seek latency does not include time at end of a view

* Update `mux-embed` to v4.27.0

#### v5.9.3

* Update `mux-embed` to v4.26.0

#### v5.9.2

* Update `mux-embed` to v4.25.1

#### v5.9.1

* Update `mux-embed` to v4.25.0

#### v5.9.0

* Fix an issue where beacons over a certain size could get hung and not be sent

* Update `mux-embed` to v4.24.0

#### v5.8.6

* Update `mux-embed` to v4.23.0

#### v5.8.5

* Update `mux-embed` to v4.22.0

#### v5.8.4

* Update `mux-embed` to v4.21.0

#### v5.8.3

* Update `mux-embed` to v4.20.0

#### v5.8.2

* Update `mux-embed` to v4.19.0

#### v5.8.1

* Load error codes on-demand

#### v5.8.0

* Collect Shaka contextual error information

* Update `mux-embed` to v4.18.0

#### v5.7.0

* Support `player_error_context` in `errorTranslator`

* Update `mux-embed` to v4.17.0

#### v5.6.0

* Add new `renditionchange` fields to Shaka SDK

* Adds support for new and updated fields: `renditionchange`, error, DRM type, dropped frames, and new custom fields

* Add frame drops to Shaka SDK

* Update `mux-embed` to v4.16.0

#### v5.5.0

* Expose `utils` on SDK initialization function to expose `utils.now()` for `player_init_time`

* Record `request_url` and `request_id` with network events

* Update `mux-embed` to v4.15.0

#### v5.4.5

* Update `mux-embed` to v4.14.0

#### v5.4.4

* Update `mux-embed` to v4.13.4

#### v5.4.3

* Update `mux-embed` to v4.13.3

#### v5.4.2

* Update `mux-embed` to v4.13.2

#### v5.4.1

* Fixes an issue with accessing the global object
* Update `mux-embed` to v4.13.1

#### v5.4.0

* Upgraded internal webpack version

* Update `mux-embed` to v4.13.0

#### v5.3.14

* Publish package to NPM

#### v5.3.13

* Update `mux-embed` to v4.12.1

#### v5.3.12

* Update `mux-embed` to v4.12.0

#### v5.3.11

* Update `mux-embed` to v4.11.0

#### v5.3.10

* Update `mux-embed` to v4.10.0

#### v5.3.9

* Update `mux-embed` to v4.9.4

#### v5.3.8

* Use common function for generating short IDs
* Update `mux-embed` to v4.9.3

#### v5.3.7

* Update `mux-embed` to v4.9.2

#### v5.3.6

* Update `mux-embed` to v4.9.1

#### v5.3.5

* Update `mux-embed` to v4.9.0

#### v5.3.4

* Update `mux-embed` to v4.8.0

#### v5.3.3

* Update `mux-embed` to v4.7.0

#### v5.3.2

* Update `mux-embed` to v4.6.2

#### v5.3.1

* Update `mux-embed` to v4.6.1

#### v5.3.0

* Bump mux-embed to 4.6.0

#### v5.2.0

* Update `mux-embed` to v4.2.0
* Fix an issue where views that resulted from `programchange` may not have been tracked correctly
* Fix an issue where if `destroy` was called multiple times, it would raise an exception

#### v5.1.0

* Update `mux-embed` to v4.1.1
* Fix an issue where `player_remote_played` would not be reported correctly

#### v5.0.0

* Update `mux-embed` to v4.0.0
* Support server-side device detection

#### v4.0.1

* remove mime type detection, Mux will now detect this server-side based on the source
* HLS mime type changed from `application/vnd.apple.mpegurl` to `application/x-mpegurl`. This is part of a larger effort to standardize mime type detection across different players

#### v4.0.0

* Only send 'critical' errors to Mux. Previously, any error (including non-fatal errors) could be sent to Mux. See: https://shaka-player-demo.appspot.com/docs/api/shaka.util.Error.html#.Severity

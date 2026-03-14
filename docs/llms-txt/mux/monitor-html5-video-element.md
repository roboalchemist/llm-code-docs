# Source: https://www.mux.com/docs/guides/monitor-html5-video-element.md

# Monitor HTML5 video element
This guide walks through integration with any HTML5 video player to collect video performance metrics with Mux data. Use this if Mux does not have an SDK specific for your player.
## Features

The following data can be collected by the Mux Data SDK when you use the \{featureDef.name} SDK, as described
&#x20;       below.

```md
- Engagement metrics
- Quality of Experience Metrics
- Web metrics such as Player Startup Time, Page Load Time, etc
- Available for deployment from a package manager
- Custom Dimensions
- Custom Beacon Domain

```

Notes:

```md
Live Latency is available for Native Safari HLS.
```

## 1. Install mux-embed

Include the Mux JavaScript SDK on every page of your web app that includes video. You can use the Mux-hosted version of the script or install via npm. `mux-embed` follows [semantic versioning](https://semver.org/) and the API will not change between major releases.

If possible, use the SDK for your particular player (e.g. Video.js, JW Player, etc.). While the HTML5 SDK works with any modern HTML5 video player, the player-specific Mux SDK is preferable because it offers a deeper integration and in most cases collects more pieces of data. If you don't see your player listed then use `mux-embed` and let us know so we can prioritize creating an SDK for the player that you are using.

```cdn

<script src="https://src.litix.io/core/4/mux.js"></script>

```

```npm

npm install --save mux-embed

```

```yarn

yarn add mux-embed

```



## 2. Initialize Mux Data

Get your `ENV_KEY` from the [Mux environments dashboard](https://dashboard.mux.com/environments).

<Callout type="info" title="Env Key is different than your API token">
  `ENV_KEY` is a client-side key used for Mux Data monitoring. These are not to be confused with API tokens which are created in the admin settings dashboard and meant to access the Mux API from a trusted server.
</Callout>

<Image src="/docs/images/env-key.png" width={2004} height={250} />

```html

<script>
  if (typeof mux !== 'undefined') {
    window.muxPlayerInitTime = mux.utils.now();
  }
</script>

<video
  id="my-player"
  src="https://muxed.s3.amazonaws.com/leds.mp4"
  controls
  width="960"
  height="400"
/>

<script>
  // Initialize Mux Data monitoring by passing in the "id" attribute of your video player
  if (typeof mux !== 'undefined') {
    mux.monitor('#my-player', {
      debug: false,
      data: {
        env_key: 'ENV_KEY', // required
        // Metadata fields
        player_name: 'Main Player', // any arbitrary string you want to use to identify this player
        player_init_time: window.muxPlayerInitTime // ex: 1451606400000
        // ...
      }
    });
  }
</script>

```

```javascript

import mux from 'mux-embed';

const playerInitTime = mux.utils.now();

// Initialize Mux Data monitoring by passing in the "id" attribute of your video player
mux.monitor('#my-player', {
  debug: false,
  data: {
    env_key: 'ENV_KEY', // required
    // Metadata fields
    player_name: 'Main Player', // any arbitrary string you want to use to identify this player
    player_init_time: playerInitTime,
    // ...
  }
});

```

```react

import mux from 'mux-embed';
import React, { useEffect, useRef } from 'react';

export default function VideoPlayer () {
  const videoRef = useRef(null);

  useEffect(() => {
    if (videoRef.current) {
      const initTime = mux.utils.now();

      mux.monitor(videoRef.current, {
        debug: false,
        data: {
          env_key: 'ENV_KEY', // required
          // Metadata fields
          player_name: 'Main Player', // any arbitrary string you want to use to identify this player
          player_init_time: initTime,
          // ...
        }
      });
    }
  }, [videoRef]);

  return (
    <video
      controls
      ref={videoRef}
      src="https://muxed.s3.amazonaws.com/leds.mp4"
      style={{ width: '100%', maxWidth: '500px' }}
    />
  );
}

```



Call `mux.monitor` and pass in a valid CSS selector or the video element itself. Followed by the SDK options and metadata. If you use a CSS selector that matches multiple elements, the first matching element in the document will be used.

Log in to the Mux dashboard and find the environment that corresponds to your `env_key` and look for video views. It takes about a minute or two from tracking a view for it to show up on the Metrics tab.

**If you aren't seeing data**, check to see if you have an ad blocker, tracking blocker or some kind of network firewall that prevents your player from sending requests to Mux Data servers.

## 3. Make your data actionable

The only required field in the `options` that you pass into `mux-embed` is `env_key`. But without some metadata the metrics in your dashboard will lack the necessary information to take meaningful actions. Metadata allows you to search and filter on important fields in order to diagnose issues and optimize the playback experience for your end users.

Pass in metadata under the `data` key when calling `mux.monitor`.

```js
mux.monitor('#my-player', {
  debug: false,
  data: {
    env_key: 'ENV_KEY', // required

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

There are some cases where you may not have the full set of metadata until after the video playback has started. In this case, you should omit the values when you first call `monitor`. Then, once you have the metadata, you can update the metadata with the `updateData` method.

```js
mux.updateData({ video_title: 'My Updated Great Video' });
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
const myPlayer = document.querySelector('#my-player');
myPlayer.src = 'https://muxed.s3.amazonaws.com/leds.mp4';

mux.emit('#my-player', 'videochange', {
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
mux.emit('#my-player', 'programchange', {
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
mux.monitor('#my-player', {
  debug: false,
  disableCookies: true,
  data: {
    env_key: 'ENV_KEY',
    // ... rest of metadata
  }
}
```

### Over-ride 'do not track' behavior

By default, Mux plugins for HTML5-based players do not respect [Do Not Track](https://www.eff.org/issues/do-not-track) when set within browsers. This can be enabled in the options passed to Mux, via a setting named `respectDoNotTrack`. The default for this is `false`. If you would like to change this behavior, pass `respectDoNotTrack: true`.

```js
mux.monitor('#my-player', {
  debug: false,
  respectDoNotTrack: true, // Disable tracking of browsers where Do Not Track is enabled
  data: {
    env_key: 'EXAMPLE_ENV_KEY',
    // ... rest of metadata
  }
}
```

### Customize error tracking behavior

By default, `mux-embed` will track errors emitted from the video element as fatal errors. If a fatal error happens outside of the context of the player, you can emit a custom error to the mux monitor.

```js
mux.emit('#my-player', 'error', {
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

mux.monitor('#my-player', {
  debug: false,
  errorTranslator: errorTranslator,
  data: {
    env_key: 'ENV_KEY', // required

    // ... additional metadata
  }
});
```

If you return `false` from your `errorTranslator` function then the error will not be tracked. Do this for non-fatal errors that you want to ignore. If your `errorTranslator` function itself raises an error, then it will be silenced and the player's original error will be used.

### Disable automatic error tracking

In the case that you want full control over what errors are counted as fatal or not, you may want to consider turning off Mux's automatic error tracking completely. This can be done by passing `automaticErrorTracking: false` in the configuration object.

```js
mux.monitor('#my-player', {
  debug: false,
  automaticErrorTracking: false,
  data: {
    env_key: 'ENV_KEY', // required

    // ... additional metadata
  }
```

### Use TypeScript with mux-embed  <BetaTag />

TypeScript support for mux-embed is currently in beta, so you'll need to take a couple extra steps in order to use it.

Use TypeScript's [triple slash `<reference path="..."/>` directive](https://www.typescriptlang.org/docs/handbook/triple-slash-directives.html#-reference-path-). At the top of your `.ts` or `.tsx` file where you want to use the types, add a line that looks like this:

```ts
/// <reference path="../../node_modules/mux-embed/dist/types/mux-embed.d.ts"/>
```

Note that the triple slash directive requires passing in the relevant path from your .ts or tsx file to the source d.ts file in node\_modules/.

Also, you may have a linting rule that prevents you from using the triple slash directive, you can disable that with and eslint-disable line:

```ts
// eslint-disable-next-line @typescript-eslint/triple-slash-reference
```

Here's an example directory structure and component file:

```sh filename="Directory Structure"
├── node_modules/
│   └── mux-embed/
│       └── dist/
│           └── types/
│               └── mux-embed.d.ts
└── src/
    └── video-component/
        └── video-component.ts
```

```ts filename="video-component.ts"
// NOTE: You may also need to disable linter rules, such as this example for @typescript-eslint
// eslint-disable-next-line @typescript-eslint/triple-slash-reference
/// <reference path="../../node_modules/mux-embed/dist/types/mux-embed.d.ts"/>
import mux from 'mux-embed';

// ...

let videoEl?: HTMLVideoElement;

// This should now be type valid, too!
videoEl?.mux.destroy();
```

This opt-in approach is temporary while we're in beta with TypeScript support. If you run into any issues with the types, please let us know so we can improve them.

### Customize beacon collection domain

If you have [integrated a custom domain for Data collection](/docs/guides/integrate-a-data-custom-domain), specify your custom domain by setting `beaconCollectionDomain`.

```js
mux.monitor('#my-player', {
  debug: false,
  beaconCollectionDomain: 'CUSTOM_DOMAIN', // ex: 'foo.bar.com'
  data: {
    env_key: 'ENV_KEY', // required
    // ... additional metadata
  }
});
```

<LinkedHeader step={steps[7]} />

### Current release

#### v5.17.1

* fix issue where playing time might accumulate for paused players

### Previous releases

#### v5.17.0

* add compatibility for dash.js 5

#### v5.16.1

* Update parsing of initial value for player\_playback\_mode

#### v5.16.0

* Add Playback Range Tracker for new engagement metrics

#### v5.15.0

* Automatically detect playback mode changes for HTML 5 Video

#### v5.14.0

* Emit a renditionchange event at the start of views to eanble updated rendition tracking.

#### v5.13.0

* Add ad type metadata to Ad Events
* Add support for the upcoming Playback Mode changes:
  * New playbackmodechange event
  * Two new metrics, ad\_playing\_time\_ms\_cumulative and view\_playing\_time\_ms\_cumulative, to track playing time by wall clock time

#### v5.12.0

* SDKs will no longer immediately send error events that are flagged as warnings. Fatal errors will still immediately be sent.

#### v5.11.0

* Allow dev to specify page starting load and page finished loading times to calculate Page Load Time

#### v5.10.0

* Adds support for cdnchange events

#### v5.9.1

* Submit Aggregate Startup Time when autoplay is set

#### v5.9.0

* Improve scaling calculation accuracy by using more events for tracking

#### v5.8.3

* add custom 11 through 20 to types

#### v5.8.2

* remove duplicate video\_source\_mime\_type from types

#### v5.8.1

* fix typo in types for viewer\_plan

#### v5.8.0

* Add support for video\_creator\_id

#### v5.7.0

* Add keys for new customer-defined dimensions

#### v5.6.0

* Fix issue where firefox did not send beacons, and some final beacons might not be sent

#### v5.5.0

* Update mechanism for generating unique IDs, used for `view_id` and others
* Use crypto.randomUUID(), when available, for generating UUID values

#### v5.4.3

* \[chore] internal build process fix (no functional changes)

#### v5.4.2

* feat(google-ima): Beta implementation of google-ima extension to mux-embed
* feat(mux-embed): Add methods for post-initialization overrides of functionality (for internal use only).
* fix(mux-embed): typecheck for dashjs.getSource is incorrect.

#### v5.4.1

* Expose `updateData` globally and fix types
* Fix an issue where views were not ended cleanly on long resume detection

#### v5.4.0

* Add updateData function that allows Mux Data metadata to be updated mid-view.

#### v5.3.3

* expose HEARTBEAT and DESTROY under mux.events

#### v5.3.2

* Fix type issues for error severity and business exception

#### v5.3.1

* fix(mux-embed): Remove 3rd party dependencies and replace with appropriately equivalent functionality.

#### v5.3.0

* Ignore request events when emitting heartbeat events
* Fix an issue where video quality metrics may not be calculated correctly on some devices

#### v5.2.1

* Send hb events regardless of errors

#### v5.2.0

* Bug fix to not de-dupe error event metadata
* Extend `errorTranslator` to work with `player_error_severity` and `player_error_business_exception`

#### v5.1.0

* Target ES5 for bundles and validate bundles are ES5

* fix an issue where seeking time before first play attempt counted towards video startup time

#### v5.0.0

* Add opt-in TypeScript Types to Mux Embed and use + refactor for other dependent data SDKs. Update published dists to include CJS and ESM.
* Mux Embed now provides (opt in) TypeScript types in its published package, as well as publishes CJS and ESM versions of the package.
* This allows us to provide a lower risk and iterative roll out of official TypeScript types for `mux-embed`. The export types updates were required to ensure actual matches between the dist package and corresponding TypeScript types.
* This *should* have no direct impact on users, though different build tools will now potentially select one of the new export types (e.g. the ESM "flavor" of `mux-embed`). TypeScript types *should not* be applied unless they are explicitly referenced in app (discussed in docs updates).

#### v4.30.0

* fix an issue causing certain network metrics to not be available for dashjs v4.x

* fix an issue where certain IDs used may cause a DOM exception to be raised

#### v4.29.0

* fix(mux-embed): avoid using element id for muxId. attach muxId to element.

#### v4.28.1

* fix an issue where beaconDomain deprecation line was incorrectly logged

#### v4.28.0

* Deprecate `beaconDomain` in favor of `beaconCollectionDomain`. The `beaconDomain` setting will continue to function, but integrations should change to `beaconCollectionDomain` instead.

#### v4.27.0

* Fix an issue where playback time was incorrectly counted during seeking and other startup activities
* Add events for the collection of ad clicks
* fix an issue where seek latency could be unexpectedly large
* fix an issue where seek latency does not include time at end of a view
* Add events for the collection of ad skips

#### v4.26.0

* muxData cookie expiration should be one year

#### v4.25.1

* Do not deduplicate ad IDs in ad events

#### v4.25.0

* Include ad watch time in playback time

#### v4.24.0

* Fix an issue where beacons over a certain size could get hung and not be sent

#### v4.23.0

* Collect Request Id from the response headers, when available, for HLS.js (`requestcompleted` and `requestfailed`) and Dash.js (`requestcompleted`). The following headers are collected: `x-request-Id`, `cf-ray` (Cloudflare), `x-amz-cf-id` (CloudFront), `x-akamai-request-id` (Akamai)

* Fix an issue where tracking rebuffering can get into an infinite loop

* Update Headers type

#### v4.22.0

* Send errors, `requestfailed`, and `requestcancelled` events on Dash.js. Because of this change, you may see the number of playback failures increase as we now automatically track additional fatal errors.

#### v4.21.0

* Include Ad metadata in ad events

#### v4.20.0

* Support for new dimension, `view_has_ad`

#### v4.19.0

* End views after 5 minutes of rebuffering

#### v4.18.0

* Add audio, subtitle, and encryption key request failures for HLS.js
* Capture ad metadata for Video.js IMA
* Capture detailed information from HLS.js for fatal errors in the Error Context

#### v4.17.0

* Extend `errorTranslator` to work with `player_error_context`

#### v4.16.0

* Add new `renditionchange` fields to Shaka SDK
* Adds support for new and updated fields: `renditionchange`, error, DRM type, dropped frames, and new custom fields
* Add frame drops to Shaka SDK
* Add new `renditionchange` info to Web SDKs
* Adds the new Media Collection Enhancement fields

#### v4.15.0

* update `mux.utils.now` to use `navigationStart` for timing reference

* fix issue where views after `videochange` might incorrectly accumulate rebuffering duration

* Resolved issue sending beacons when view is ended

* Record `request_url` and `request_id` with network events

#### v4.14.0

* Tracking FPS changes if specified in Manifest

#### v4.13.4

* Resolved issue sending beacons when paused

#### v4.13.3

* Fixed issue with monitoring network events for hls.js monitor

#### v4.13.2

* Fix an issue with sending unnecessary heartbeat events on the window `visibilitychange` event

#### v4.13.1

* Fixes an issue with accessing the global object

#### v4.13.0

* Collect the `x-request-id` header from segment responses to make it easier to correlate client requests to other logs

* Upgraded internal webpack version

* Flush events on window `visibilitychange` event

#### v4.12.1

* Use Fetch API for sending beacons

#### v4.12.0

* Generate a new unique view if the player monitor has not received any events for over an hour.

#### v4.11.0

* Detect fullscreen and player language

#### v4.10.0

* Replace query string dependency to reduce package size
* Remove `ImageBeacon` fallback, removing support for IE9

#### v4.9.4

* Generate all `view_id`'s internally

#### v4.9.3

* Use common function for generating short IDs

#### v4.9.2

* Fixed an issue around the `disablePlayheadRebufferTracking` option

#### v4.9.1

* Fix issue where `getStartDate` does not always return a date object

#### v4.9.0

* Support PDT and player\_live\_edge\_program\_time for Native Safari

* Set a max payload size in mux-embed

#### v4.8.0

* Add option `disablePlayheadRebufferTracking` to allow players to disable automatic rebuffering metrics.
  Players can emit their own `rebufferstart` or `rebufferend` events and track rebuffering metrics.

* Fix an issue with removing `player_error_code` and `player_error_message` when the error code is `1`.
  Also stops emitting `MEDIA_ERR_ABORTED` as errors.

* Now leaving Player Software Version for HTML5 Video Element unset rather than "No Versions" as it is no longer needed.

#### v4.7.0

* Add an option to specify beaconCollectionDomain for Data custom domains

#### v4.6.2

* Fix an issue with emitting heartbeat events while the player is not playing

#### v4.6.1

* Fix an issue with removing event listeners from window after the player monitor destroy event

#### v4.6.0

* Update hls.js monitor to record session data with fields prefixed as `io.litix.data.`
* Update the manifest parser to parse HLS session data tags

#### v4.5.0

* Add short codes to support internal video experiments
* Collect request header prefixed with `x-litix-*`
* Capture fatal hls.js errors
* Make `envKey` an optional parameter

#### v4.4.4

* Add a player events enum on the `mux` object (e.g. `mux.events.PLAY`)
* Use the browser `visibilitychange` listener instead of `unload` to handle destructuring the player monitor.

#### v4.4.3

* Fix: Specify `video_source_is_live` for HLS.js monitor

#### v4.4.2

* Group events into 10 second batches before sending a beacon

#### v4.4.1

* Exclude latency metrics from beacons if `video_source_is_live` is not `true`

#### v4.4.0

* Add a lightweight HLS manifest parser to capture latency metrics for player's that don't expose an API for accessing the manifest.
* Allow players to emit `player_program_time` instead of calculating internally

#### v4.3.0

* Add support for calculating latency metrics when streaming using HLS

#### v4.2.5

* Remove default `video_id` when not specified by the developer.

#### v4.2.4

* Add minified keys for latency metrics

#### v4.2.3

* Add minified keys for new program time metrics

#### v4.2.2

* Fix bug causing missing bitrate metrics using HLS.js {'>'}v1.0.0

#### v4.2.1

* (video element monitor) Fix an issue where some non-fatal errors thrown by the video were tracked as playback failures

#### v4.2.0

* Fix an issue where views triggered by `programchange` may not report metrics correctly
* Fix an issue where calling `el.mux.destroy()` multiple times in a row raised an exception

#### v4.1.1

* Fix an issue where `player_remote_played` wasn't functioning correctly

#### v4.1.0

* Add support for custom dimensions

#### v4.0.1

* Support HLS.js v1.0.0

#### v4.0.0

* Enable sending optional ad quartile events through.
* Move device detection server-side, improving data accuracy and reducing client SDK size.
* Fix an issue where jank may be experienced in some web applications when the SDK is loaded.

#### v3.4.0

* Setting to disable rebuffer tracking `disableRebufferTracking` that defaults to `false`.

#### v3.3.0

* Adds `viewer_connection_type` detection.

#### v3.2.0

* Adds support for `renditionchange`.

#### v3.1.0

* Add checks for window being undefined and expose a way for SDKs to pass in platform information. This work is necessary for compatibility with react-native-video.

#### v3.0.0

* Setting to disable Mux Data collection when Do Not Track is present now defaults to off
* Do not submit the source URL when a video is served using the data: protocol

#### v2.10.0

* Use Performance Timing API, when available, for view event timestamps

#### v2.9.1

* Fix an issue with server side rendering

#### v2.9.0

* Support for Dash.js v3

#### v2.8.0

* Submit Player Instance Id as a unique identifier

#### v2.7.3

* Fixed a bug when using `mux.monitor` with Hls.js or Dash.js the source hostname was not being properly collected.

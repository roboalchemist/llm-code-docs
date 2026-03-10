# Source: https://screenshotone.com/docs/animated-screenshots/

# Animated Screenshots

import Alert from "@/components/Alert.astro";
import Video from "@/components/Video.astro";

<Alert>
    In case you need a custom scenario or have propositions, feel free to reach
    out at `support@screenshotone.com`.
</Alert>

You can rely on ScreenshotOne API to generate animated screenshots and handle image and video streaming infrastructure.

ScreenshotOne supports animated (including scrollable) screenshots of different types, caching based on the world’s fastest and most potent CDN (Cloudflare), blocking ads, cookie banners, and chats.

In just one API request, you can quickly generate animated screenshots. And if you need more, various scenarios with many options are covered.

Grasp how simple it is:

```
https://api.screenshotone.com/animate?url=https://tailwindcss.com&scenario=scroll&access_key=<your access key>
```

The result might differ a bit in case default options are changed, but as for now, it is similar to what I have shown in the video:

<Video url="/videos/animated_screenshot.mp4" />

Don't forget that you can use [signed links to share videos and GIF images publicly](https://screenshotone.com/docs/signed-requests/), [caching](https://screenshotone.com/docs/options/#caching), [block ads](/docs/options/#block_ads), [block cookie banners](/docs/options/#block_cookie_banners), and [many other options](#all-supported-options).

## Scenarios

Select a basic scenario of how you want to animate screenshots or render ed HTML. Specify additional options and tune the scenario for your use case. And you are good to go.

### Default (stand still)

Use the `scenario=default` parameter, or don't specify `scenario` at all when sending a request to `/animate`.

The default scenario is to record animation after loading the site without additional animations.

The use case is when you generate animated screenshots of sites that have animations and you want to showcase it.

Look at [the Handwrytten site](https://www.handwrytten.com/) as an example. It has a default animation when loaded. So, we won't scroll it or add any other activities.

We will record the site as is after load:

```
https://api.screenshotone.com/animate?url=https://www.handwrytten.com/&access_key=<your access key>
```

The result:

<Video url="/videos/animated_handwrytten.mp4" />

### Scrollable (scrolling) screenshot

Use the `scenario=scroll` parameter, or don't specify `scenario` at all when sending a request to `/animate`.

There is an example for scrolling [Senja](https://senja.io):

```
https://api.screenshotone.com/animate?url=https://senja.io&scenario=scroll&access_key=<your access key>
```

The result is:

<Video url="/videos/animated_senja.mp4" />

These are supported options for scrolling screenshot animation:

-   `scroll_delay`—delay in milliseconds between scrolls. The default value is `500`.
-   `scroll_duration`—duration in milliseconds of one scroll. The default value is `1500`. The scroll duration is not the duration of the video or animated GIF. Please, use the `duration` parameter to specify the length of the video or animated GIF.
-   `scroll_by`—by how many pixes scroll. The default value is `1000`.
-   `scroll_start_immediately`—scroll immediately or wait for the `scroll_delay` milliseconds before scrolling. The default value is `true`.
-   `scroll_start_delay`—wait time (in milliseconds) till starting scrolling. The default value is `0``.
-   `scroll_back`—scroll back or not. The default value is `true`.
-   `scroll_back_algorithm`—`once` is by default and means that it will scroll back immediately once with the easing you have defined. But if you set `repeat`, it will repeat the same algorithm the API used to scroll to the bottom of the page.
-   `scroll_back_after_duration`—scroll back after the specified duration in milliseconds.
-   `scroll_complete`—stop recording animation when full scrolling is completed. The option `true` by default.
-   `scroll_stop_after_duration`—stop scrolling after the specified duration in milliseconds. Use `scroll_complete=false` and `scroll_back=false`, to stop and just stand still after the specified duration.
-   `scroll_easing`—use it to define the scrolling easing effect. The default value is `ease_in_out_quint`. There is a list of all available options:
    -   `linear`–no easing, no acceleration;
    -   `ease_in_quad`–accelerating from zero velocity;
    -   `ease_out_quad`–decelerating to zero velocity;
    -   `ease_in_out_quad`–acceleration until halfway, then deceleration;
    -   `ease_in_cubic`–accelerating from zero velocity;
    -   `ease_out_cubic`–decelerating to zero velocity;
    -   `ease_in_out_cubic`–acceleration until halfway, then deceleration;
    -   `ease_in_quart`–accelerating from zero velocity;
    -   `ease_out_quart`–decelerating to zero velocity;
    -   `ease_in_out_quart`–acceleration until halfway, then deceleration;
    -   `ease_in_quint`–accelerating from zero velocity;
    -   `ease_out_quint`–decelerating to zero velocity;
    -   `ease_in_out_quint`–acceleration until halfway, then deceleration.
-   `scroll_try_navigate`—navigate while scrolling and record the new opened page.
-   `scroll_navigate_after`—navigate after duration in milliseconds, by default it is half of the duration.
-   `scroll_navigate_to_url`—to what URL navigate;
-   `scroll_navigate_link_hints`—if the URL is not specified, the hints of what links to use, by default `'pricing', 'about', 'customers'`.  E.g. "pricing" means to open any internal link which has the "pricing" keyword in its text;
-   `scroll_till_selector`—scroll till the selector is visible;
-   `scroll_till_selector_adjust_top`—adjust the top position of the selector in the viewport;
-   `scroll_to_end_after`—scroll to the end after the specified duration in milliseconds with the specified easing in one scroll.

There is an example of applying custom options for scrolling [Senja](https://senja.io):

```
https://api.screenshotone.com/animate?url=https://senja.io&scenario=scroll&scroll_delay=400&scroll_by=400&access_key=<your access key>
```

The result is:

<Video url="/videos/animated_senja_custom.mp4" />

### Navigation

You can record a page navigation when recording scrolling screenshot video. It allows render less boring and more engaging videos.

<Video url="/videos/scrolling_screenshot_navigation.mp4" />

It is rendered with a simple request like: 

```
https://api.screenshotone.com/animate?url=https://screenshotone.com/&scenario=scroll&duration=10&scroll_try_navigate=true&scroll_navigate_link_hints=pricing&access_key=<YOUR KEY>
```

You need to specify either the "scroll_navigate_to_url" or the "scroll_navigate_link_hints" options.
If neither is specified, any first random visible internal link will be used for navigation if available.

The `scroll_navigate_link_hints` option can be used as an array:

```
scroll_navigate_link_hints[]=pricing&scroll_navigate_link_hints[]=about
```

The API will attempt to find any internal links that match the hints.

## All supported options

### Animation specific

#### format

Available response formats:

-   `mp4`
-   `mov`
-   `avi`
-   `webm`
-   `gif`

Default value is `mp4`.

#### duration

<Alert>
    If you need a longer animation, please, reach out at
    `support@screenshotone.com` and describe your use case.
</Alert>

The default value is `5` seconds (`duration=5`).

The minimum value is `1` and the maximum is `30`.

Suppose `scroll_complete` is set to `true`, which is by default, and [the scrolling scenario](/docs/animated-screenshots/#scrollable-scrolling-screenshot)) is completed earlier than the specified `duration`. In that case, the recording will be stopped, and the resulting animation will be short.

Since GIFs are not videos, but images, the duration might not be mapped exactly to the number of frames and represent the duration as is for the video. It is better to consider it as a duration of recording of the video, and then frames glued together into a GIF. 

#### width

You must specify both the `width` and [height](#height) parameters. You can't specify only one. By default, the width and the height parameters are the same as [viewport width](/docs/options/#viewport_width) and [viewport height](/docs/options/#viewport_height) parameters.

[The device scale factor](/docs/options/#device_scale_factor) is taken into consideration. If you set the viewport width and height to `1000x500`, with `device_scale_factor=1`, the resulting resolution of the video will be `1000x500`, but with `device_scale_factor=2`, it will be `2000x1000`.

If [aspect ratio](#aspect_ratio) is specified, `width` and `height` are not used. And API will try to fit the video of the viewport size into the specified aspect ratio.

#### height

You must specify both the [width](#width) and `height` parameters. You can't specify only one. By default, the width and the height parameters are the same as [viewport width](/docs/options/#viewport_width) and [viewport height](/docs/options/#viewport_height) parameters.

[The device scale factor](/docs/options/#device_scale_factor) is taken into consideration. If you set the viewport width and height to `1000x500`, with `device_scale_factor=1`, the resulting resolution of the video will be `1000x500`, but with `device_scale_factor=2`, it will be `2000x1000`.

If [aspect ratio](#aspect_ratio) is specified, `width` and `height` are not used. And API will try to fit the video of the viewport size into the specified aspect ratio.

#### aspect ratio

If [aspect ratio](#aspect_ratio) is specified, `width` and `height` are not used. And API will try to fit the video of the viewport size into the specified aspect ratio.

#### scenario

Available scenarios formats:

-   not specified or `default` is for [the default animation scenario](#default-stand-still).
-   `scroll` is for [the scrolling screenshots](#scrollable-scrolling-screenshot).

The default value is `default`.

#### clip

You can clip part of the video. But currently, it is only available when the format is `gif`.

Use `clip_width`, `clip_height, `clip_x`and`clip_y` to specify the clip size and coordinates.

### Regular

Animated screenshots also support most options supported by regular image screenshots. There is a list of supported options:

-   `omit_background` but only for the `mov` format;
-   [credentials](/docs/options/#credentials);
-   [essentials](/docs/options/#essentials), except `selector` and with different values for [format](#format);
-   [viewport](/docs/options/#viewport);
-   [emulations](/docs/options/#emulations);
-   [customization](/docs/options/#customization);
-   [blocking](/docs/options/#blocking);
-   [geolocation](/docs/options/#geolocation);
-   [request](/docs/options/#request);
-   [wait](/docs/options/#wait);
-   [caching](/docs/options/#caching);
-   [storing](/docs/options/#storing).
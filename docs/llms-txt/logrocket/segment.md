# Source: https://docs.logrocket.com/docs/segment.md

# Segment

Integrating LogRocket with [Segment](https://segment.com)

## Segment Destination Configuration

To configure LogRocket as a destination, navigate to the destination catalogue in Segment. You will need your appID. You can find your appID on [https://app.logrocket.com](https://app.logrocket.com/) under Settings > Project Setup.

Add LogRocket as a destination, then choose the source(s) which you would like to have start sending data to LogRocket. For the configuration, add your appID to the field:

![](https://files.readme.io/6bf150f-Screen_Shot_2023-02-08_at_3.19.26_PM.png "Screen Shot 2023-02-08 at 3.19.26 PM.png")

Additional recording configuration options are currently limited to full [network sanitization](https://docs.logrocket.com/reference/network#isenabled---boolean) (yes / no) and full [input sanitization](https://docs.logrocket.com/reference/dom#sanitize-all-user-input-fields) (yes / no).

#### Optional Additional Config

If you'd like to use the LogRocket Segment destination but need more advanced data redaction configuration, the `window.logRocketSettings` property will be set as the second parameter to the `LogRocket.init` call on your page during load. You can use this property to configure more advanced privacy options as detailed [here](https://docs.logrocket.com/reference/configure-privacy).

> 📘 Please Note
>
> While LogRocket can be configured as a Segment destination, we recommend [loading the SDK manually](https://docs.logrocket.com/reference/quickstart) when possible in order to minimize obstruction of the SDK. The configuration options below detail how all Segment events can be sent to LogRocket without configuring it as a destination.

## Adding Session URL

Add a LogRocket session recording URL to Segment

```javascript
LogRocket.getSessionURL(function (sessionURL) {
  analytics.track('LogRocket', {
    sessionURL: sessionURL,
  });
});
```

## Custom Analytics Events

To send all of your Segment events to LogRocket for search (via [LogRocket.track()](https://docs.logrocket.com/reference/track)), you can do EITHER of the following:

1. Redefine window\.analytics to also send data to LogRocket

```javascript
if (window.analytics) {
   const oldTrack = window.analytics.track.bind(window.analytics);
   window.analytics.track = (...args) => {
     LogRocket.track(...args);
     oldTrack(...args);
   };
}
```

You can do the same for `.identify` events as well.

2. Instead of (1), you can could also build a utility method that calls both `window.analytics` and `LogRocket.track`

```javascript
function analyticsTrack(...args) {
   window.analytics.track(...args);
   LogRocket.track(...args);
}
```

If you have deployed LogRocket by setting it as a Segment Destination, you can also send your Segment events to LogRocket automatically by [configuring a Mapping in Segment](https://segment.com/docs/connections/destinations/catalog/actions-logrocket/). This approach requires LogRocket to be deployed via Segment; the code-based approaches above can be used by customers who use Segment *alongside* LogRocket but do not want to deploy LogRocket *through* Segment.
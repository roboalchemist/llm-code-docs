# Source: https://docs.logrocket.com/docs/launchdarkly.md

# LaunchDarkly

Integrating LogRocket with [LaunchDarkly](https://www.launchdarkly.com)

If you are using LaunchDarkly to control feature flags, you can send the current set of flag states into LogRocket to segment sessions and compare user experiences across flag variations.

Below is a lightweight example that:

1. sends **all current flag values** to LogRocket when the LD client is ready, and
2. optionally re-sends whenever flags change.

```js
// LaunchDarkly JS SDK initialization (example)
import * as LDClient from 'launchdarkly-js-client-sdk';
import LogRocket from 'logrocket';

// Initialize LaunchDarkly
const ldClient = LDClient.initialize('YOUR_CLIENT_SIDE_ID', {
  key: currentUserId, // your user or multi-context key
  // ...any additional LD context attributes
});

// When the LD client is ready, capture all flag values
ldClient.on('ready', () => {
  const flags = ldClient.allFlags(); // { [flagKey]: value }
  // Send a single custom event containing the full flag map
  LogRocket.track('LaunchDarkly Flags', flags);
});
```

If you have many flags, consider whitelisting keys or transforming the map before sending to keep the event payload compact.

## Find these sessions in LogRocket

After you start sending `LogRocket.track('LaunchDarkly Flags', {...}):`

In LogRocket, filter sessions by Custom Event and search for LaunchDarkly Flags (or LaunchDarkly Flags Updated) to create buckets of sessions based on your flag state payload.
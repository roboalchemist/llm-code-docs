# Source: https://docs.anchorbrowser.io/advanced/session-timeout.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Session Timeout

### Managing Browser Session Lifetime

Anchor provides multiple ways to control and terminate browser sessions. In addition to manually stopping sessions via the [stop session API](/api-reference/browser-sessions/end-browser-session), you can configure two types of automatic timeout mechanisms to manage session lifetime effectively.

For the full list of available options, view the [interactive api documentation](/api-reference/browser-sessions).

### Timeout Configuration Options

The API offers two distinct timeout parameters through the `session.timeout` object to automatically manage browser session termination.

#### Idle Timeout

The `idle_timeout` parameter automatically terminates sessions after a period of inactivity. This timer starts after the last connection to the browser has disconnected, and any new connection will restart the timer. This includes live view sessions, CDP (Chrome DevTools Protocol) connections, and OS-level control connections.

The idle timeout is particularly useful for sessions with unknown length, allowing users to interact with browsers for as long as they need without keeping stale browsers alive unnecessarily. When set to `3` minutes for example, the session will terminate after 3 minutes with no active connections. The default value is `5` minutes, and you can disable automatic termination for idle sessions by setting it to `-1`.

#### Maximum Duration

The `max_duration` parameter sets a hard limit on total session lifetime. Unlike the idle timeout, this will automatically terminate the session after the specified duration regardless of activity level. This acts as a safety mechanism to ensure sessions don't run indefinitely.

The default maximum duration is `180` minutes (3 hours), but you can adjust this based on your needs. Setting `max_duration` to `10` will terminate the session after exactly 10 minutes, whether the browser is actively being used or not. There is no upper limit on how long you can set the maximum duration.

### Implementation Example

<CodeGroup>
  ```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';

  (async () => {
    const anchor_client = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
    
    const session = await anchor_client.sessions.create({
      session: {
        timeout: {
          max_duration: 10,  // 10 minutes hard limit
          idle_timeout: 3    // 3 minutes of inactivity
        }
      }
    });
    
    console.log("Session created with timeout configuration:", session.data.id);
  })().catch(console.error);
  ```

  ```python python theme={null}
  import os
  from anchorbrowser import Anchorbrowser

  anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

  session = anchor_client.sessions.create(
      session={
          "timeout": {
              "max_duration": 10,  # 10 minutes hard limit
              "idle_timeout": 3    # 3 minutes of inactivity
          }
      }
  )

  print("Session created with timeout configuration:", session.data.id)
  ```
</CodeGroup>

In this example, replace `"your_api_key_here"` with your actual API key. The configuration sets a 10-minute hard session limit with `max_duration`, while `idle_timeout` ensures the session terminates after 3 minutes of no active connections. These two timeout mechanisms work independently, so the session will end when whichever condition is met first.

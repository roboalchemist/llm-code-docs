# Source: https://docs.anchorbrowser.io/advanced/popup-blocker.md

# Popup Blocker

> Block cookie banners and consent dialogs in your browser sessions

Popup blocking is enabled by default in Anchor Browser. It blocks cookie banners and consent dialogs to create cleaner automation experiences.

<Info>
  Popup blocking is enabled by default. Disable it only if you need to test popup-related functionality.
</Info>

## Quick Start

<CodeGroup>
  ```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';

  (async () => {
    const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
    
    const session = await anchorClient.sessions.create({
      // Optional: Enabled by default (both), so this configuration is not required
      browser: {
        adblock: {
          active: true  // Required for popup blocking
        },
        popup_blocker: {
          active: true  // Blocks cookie banners and consent dialogs
        }
      }
    });
    
    console.log("Session:", session.data.id);
  })().catch(console.error);
  ```

  ```python python theme={null}
  import os
  from anchorbrowser import Anchorbrowser

  anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

  session = anchor_client.sessions.create(
      # Optional: Enabled by default (both), so this configuration is not required
      browser={
          "adblock": {
              "active": True  # Required for popup blocking
          },
          "popup_blocker": {
              "active": True  # Blocks cookie banners and consent dialogs
          }
      }
  )

  print("Session:", session.data.id)
  ```
</CodeGroup>

<Warning>
  Popup blocking requires ad blocking to be active. Disabling ad blocking will result an error.
</Warning>

## Disabling Popup Blocker

To disable popup blocking for a session, set `active: false` in the popup\_blocker configuration:

<CodeGroup>
  ```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';

  (async () => {
    const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
    
    const session = await anchorClient.sessions.create({
      browser: {
        // Optional: ad blocking is enabled by default, so this configuration is not required
        adblock: {
          active: true  // Ad blocking must remain active
        },
        // Required to disable popup_blocker
        popup_blocker: {
          active: false  // Disables popup blocking for this session
        }
      }
    });
    
    console.log("Session:", session.data.id);
  })().catch(console.error);
  ```

  ```python python theme={null}
  import os
  from anchorbrowser import Anchorbrowser

  anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

  session = anchor_client.sessions.create(
      browser={
          # Optional: ad blocking is enabled by default, so this configuration is not required
          "adblock": {
              "active": True  # Ad blocking must remain active
          },
          # Required to disable popup_blocker
          "popup_blocker": {
              "active": False  # Disables popup blocking for this session
          }
      }
  )

  print("Session:", session.data.id)
  ```
</CodeGroup>

## Related Features

* [Ad Blocker](/advanced/adblocker) - Block ads, trackers, and malicious content (required for popup blocking)
* [Captcha Solving](/advanced/captcha-solving) - Solve CAPTCHAs that may appear when ad blocking is detected

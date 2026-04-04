# Source: https://docs.anchorbrowser.io/advanced/adblocker.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Ad Blocker

> Block ads, trackers, and unwanted content in your browser sessions

Ad blocking is enabled by default in Anchor Browser. It blocks ads, trackers, and malicious content to improve page load times and create cleaner automation.

<Note>
  Ad blocking is enabled by default. Disable it only if you need to test ad-related functionality.
</Note>

## Quick Start

<CodeGroup>
  ```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';

  (async () => {
    const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
    
    const session = await anchorClient.sessions.create({
      // Optional: ad blocking is enabled by default, so this configuration is not required
      browser: {
        adblock: {
          active: true  // Set to false to disable ad blocking
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
      # Optional: ad blocking is enabled by default, so this configuration is not required
      browser={
          "adblock": {
              "active": True  # Set to False to disable ad blocking
          }
      }
  )

  print("Session:", session.data.id)
  ```
</CodeGroup>

## Disabling Ad Blocker

To disable ad blocking for a session, set `active: false` in the adblock configuration:

<CodeGroup>
  ```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';

  (async () => {
    const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
    
    const session = await anchorClient.sessions.create({
      browser: {
        adblock: {
          active: false  // Disables ad blocking for this session
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
          "adblock": {
              "active": False  # Disables ad blocking for this session
          }
      }
  )

  print("Session:", session.data.id)
  ```
</CodeGroup>

## Related Features

* [Popup Blocker](/advanced/popup-blocker) - Block cookie banners and consent dialogs
* [Captcha Solving](/advanced/captcha-solving) - Solve CAPTCHAs that may appear when ad blocking is detected

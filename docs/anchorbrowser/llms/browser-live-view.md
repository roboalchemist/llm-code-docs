# Source: https://docs.anchorbrowser.io/advanced/browser-live-view.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Embedded Browser Live UI

> Embed interactive browser sessions directly into your application

## Overview

Anchor Browser offers a live view feature that allows you to embed an interactive frame of a website as a web element. The `live_view_url` is received when creating a session.

## Headful Mode (Default)

Headful mode provides a single URL to view the full chrome view, including the address bar. This ensures the presented tab is always the active tab and provides the best user experience.

<img className="hidden dark:block mx-auto" src="https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/vnc-live-view.png?fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=774f0fea0d9359730307c6a21e50ae9c" alt="Browser Live View in Headful Mode" width="560" data-og-width="1210" data-og-height="1200" data-path="images/vnc-live-view.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/vnc-live-view.png?w=280&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=d875e016f7db64278e379367ca390fe0 280w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/vnc-live-view.png?w=560&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=9a23de6e2ced15f1d732e848dd4d35db 560w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/vnc-live-view.png?w=840&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=7504a6d074157d0fa130bab9426c062e 840w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/vnc-live-view.png?w=1100&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=afdb86cec4a4a69e1fbc6ca67bce875b 1100w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/vnc-live-view.png?w=1650&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=efe659aa8b61706a3671cecaf2e1d6e8 1650w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/vnc-live-view.png?w=2500&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=59bd34e12c9baf0775ab4354033a275d 2500w" />

To create a browser in headful mode, simply [create a session](/sdk-reference/browser-sessions/start-browser-session):

<CodeGroup>
  ```javascript node.js theme={null}
  import  AnchorBrowser from 'anchorbrowser';

  // Initialize the client
  const client = new AnchorBrowser({ apiKey: process.env.ANCHOR_API_KEY });

  // For explicit headfull session configuration (optional, default to false)
  const config = {
    browser: {
      headless: {
        active: false
      }
    }
  };

  const session = await client.sessions.create(config);
  const liveViewUrl = session.data.live_view_url;
  console.log(`Live view URL: ${liveViewUrl}`);
  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os

  # Initialize the client
  client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

  # For explicit headfull session configuration (optional, default to False)
  config = {
      "headless": {
        "active": False
      }
  }

  session = client.sessions.create(browser=config)
  print(f"Live view URL: {session.data.live_view_url}")
  ```
</CodeGroup>

Then, use the `live_view_url` from the response to embed the live view directly into an iframe:

```html  theme={null}
<iframe 
  src="{{live_view_url}}" 
  sandbox="allow-same-origin allow-scripts" 
  allow="clipboard-read; clipboard-write" 
  style="border: 0px; display: block; width: 100%; height: 100%; position: absolute; top: 0px; left: 0px;">
</iframe>
```

## Advanced Embedding Configuration

### Embed in Fullscreen View (Hide Navigation Bar)

To use the fullscreen view, replace the live view URL with the following:

```html  theme={null}
<iframe src="{{live_view_url}}" ...></iframe>
```

### Disable Browser Interactivity

To prevent the end user from interacting with the browser, add the `style="pointer-events: none;"` attribute to the iframe:

```html  theme={null}
<iframe 
  src="{{live_view_url}}" 
  sandbox="allow-same-origin allow-scripts" 
  allow="clipboard-read; clipboard-write" 
  style="border: 0px; display: block; width: 100%; height: 100%; position: absolute; top: 0px; left: 0px; pointer-events: none;">
</iframe>
```

<Note>
  This feature is available for both headful and headless modes.
</Note>

## Headless Mode

To obtain the browser live session URL in headless mode, start by [creating a session](/api-reference/browser-sessions/start-browser-session):

<CodeGroup>
  ```javascript node.js theme={null}
  import  AnchorBrowser from 'anchorbrowser';

  // Initialize the client
  const client = new AnchorBrowser({ apiKey: process.env.ANCHOR_API_KEY });

  const config = {
    browser: {
      headless: {
        active: true
      }
    }
  };

  const session = await client.sessions.create(config);
  const liveViewUrl = session.data.live_view_url;
  console.log(`Live view URL: ${liveViewUrl}`);
  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os

  # Initialize the client
  client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

  config = {
      "headless": {
        "active": True
      }
  }

  session = client.sessions.create(browser=config)
  print(f"Live view URL: {session.data.live_view_url}")
  ```
</CodeGroup>

<img className="hidden dark:block mx-auto" src="https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/cdp-live-view.png?fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=dc51ac109c87e8f58ff04aefd508ebf5" alt="Browser Live View in Headless Mode" width="560" data-og-width="1453" data-og-height="908" data-path="images/cdp-live-view.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/cdp-live-view.png?w=280&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=e64815d70775202b79f6bdb6c235f4a8 280w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/cdp-live-view.png?w=560&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=8eaac5ad8646f317a2353c45cefc7a99 560w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/cdp-live-view.png?w=840&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=aaa90eca3e4841e2c93e259e552d961a 840w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/cdp-live-view.png?w=1100&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=95d9c93aaef81b668948cbad33ebe118 1100w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/cdp-live-view.png?w=1650&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=fdfbcd53824a5960bb2ad3faa38b64b0 1650w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/cdp-live-view.png?w=2500&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=019129bf8c0aa2a4bbf861f2370e7132 2500w" />

<Warning>The live\_view\_url currently points to the browser default first page.</Warning>

Then, use the **create-session** response to embed the live view URL directly into an iframe:

```html  theme={null}
<iframe src="{{live_view_url}}" sandbox="allow-same-origin allow-scripts" allow="clipboard-read; clipboard-write" style="border: 0px; display: block; width: 100%; height: 100%; position: absolute; top: 0px; left: 0px;"></iframe>
```

# Source: https://docs.anchorbrowser.io/advanced/captcha-solving.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Captcha Solving

### Visual CAPTCHA solving

Anchor browser solves CAPTCHA challenges using a vision-based approach, along with extension-based fallbacks. The vision-based approach imitates human behavior to solve any CAPTCHA (including Cloudflare) without multiple challenges.

<Note> Proxy is required for CAPTCHA solving configuration.</Note>

For the full list of available options, view the [interactive api documentation](/api-reference)

### Enable CAPTCHA solving

<CodeGroup>
  ```javascript node.js theme={null}
  import Anchorbrowser from 'anchorbrowser';

  (async () => {
    const anchorClient = new Anchorbrowser({apiKey: process.env.ANCHOR_API_KEY});
    
    const session = await anchorClient.sessions.create({
      browser: {
        captcha_solver: {
          active: true
        }
      },
      session: {
        proxy: {
          active: true  // Required
        }
      }
    });
    
    console.log("Session created with CAPTCHA solver:", session.data.id);
  })().catch(console.error);
  ```

  ```python python theme={null}
  import os
  from anchorbrowser import Anchorbrowser

  anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

  session = anchor_client.sessions.create(
      browser= {
        "captcha_solver": {
          "active": True
        }
      },
      session= {
        "proxy": {
          "active": true  # Required
        }
      }
  )

  print("Session created with CAPTCHA solver:", session.data.id)
  ```
</CodeGroup>

#### Configure Text-based CAPTCHA solving

<CodeGroup>
  ```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';

  (async () => {
    const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
    
    const session = await anchorClient.sessions.create({
      browser: {
        captcha_solver: {
          active: true,
          image_selector: 'ol_capcha img',
          input_selector: 'ol-captcha input'
        }
      },
      session: {
        proxy: {
          active: true  // Required
        }
      }
    });
    
    console.log("Session created with text-based CAPTCHA solver:", session.data.id);
  })().catch(console.error);
  ```

  ```python python theme={null}
  import os
  from anchorbrowser import Anchorbrowser

  anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

  session = anchor_client.sessions.create(
      browser={
          "captcha_solver": {
              "active": True,
              "image_selector": 'ol_capcha img',
              "input_selector": 'ol-captcha input'
          }
      },
      session= {
        "proxy": {
          "active": true  # Required
        }
      }
  )

  print("Session created with text-based CAPTCHA solver:", session.data.id)
  ```
</CodeGroup>

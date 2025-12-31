# Source: https://docs.anchorbrowser.io/advanced/captcha-solving.md

# Captcha Solving

### Visual CAPTCHA solving

Anchor browser solves CAPTCHA challenges using a vision-based approach, along with extension-based fallbacks. The vision-based approach imitates human behavior to solve any CAPTCHA (including Cloudflare) without multiple challenges.

<Note> CAPTCHA solving works best with proxy enabled. Bot detectors would likely fail CAPTCHA solving attempts that are performed without Proxy.</Note>

For the full list of available options, view the [interactive api documentation](/api-reference)

### CAPTCHA solving Configuration

<CodeGroup>
  ```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';

  (async () => {
    const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
    
    const session = await anchorClient.sessions.create({
      browser: {
        captcha_solver: {
          active: true, // Visual CAPTCHA solving
          // Optional: Text-based CAPTCHA (both selectors below)
          image_selector: 'ol_capcha img',
          input_selector: 'ol-captcha input'
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
      browser={
          "captcha_solver": {
              "active": True,   # Visual CAPTCHA solving
              # Optional: Text-based CAPTCHA (defaults to false)
  	     "image_selector": 'ol_capcha img',
              "input_selector": 'ol-captcha'
          }
      }
  )

  print("Session created with CAPTCHA solver:", session.data.id)
  ```
</CodeGroup>

# Source: https://docs.anchorbrowser.io/essentials/stealth.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Extra Stealth Mode

> Advanced anti-detection and browser fingerprinting protection for automated browsing

<Note>
  Extra Stealth is available on our **Growth tier**.

  [Upgrade Now](https://app.anchorbrowser.io/billing)
</Note>

Anchor Browser provides built-in stealth capabilities that help avoid detection by anti-bot systems and website fingerprinting. These features enable automated browsing that mimics human behavior and bypasses common detection mechanisms.

## What is Extra Stealth Mode?

Extra Stealth Mode leverages a specialized Chrome browser environment that provides:

* 🔒 **Advanced Anti-Detection** - Bypass sophisticated bot detection systems and CAPTCHAs
* 🛡️ **Automation Consistency** - Maintain consistent access without getting blocked
* 👤 **Human-Like Behavior** - Mimic real user patterns to avoid suspicion

<Note>
  Alternative Cloudflare-verified access to webpages is available through our [Cloudflare Web Bot Auth Integration](/advanced/cloudflare-web-bot-auth).
</Note>

## Quick start - Enable stealth features

<Steps>
  <Step title="Create a session with extra stealth enabled">
    Create a browser session with extra stealth features enabled using the SDK:

    <Warning>
      Extra stealth mode requires proxy configuration to be active. **If proxy is disabled, extra stealth will be automatically disabled** by the system.

      Read more about [Proxy Configuration](/advanced/proxy)
    </Warning>

    <CodeGroup>
      ```JavaScript node.js theme={null}
      import Anchorbrowser from "anchorbrowser";

      const anchorClient = new Anchorbrowser()
      const session = await anchorClient.sessions.create({
          browser: {
              extra_stealth: {
                  active: true
              }
          },
          session: {
              proxy: {
                  active: true
              }
          }
      });

      console.log(session);
      ```

      ```python python theme={null}
      from anchorbrowser import Anchorbrowser
      import os

      anchorClient = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
      session = anchorClient.sessions.create(
          browser={
              "extra_stealth": {
                  "active": True
              }
          },
          session={
              "proxy": {
                  "active": True
              }
          }
      )
      print(session)
      ```
    </CodeGroup>
  </Step>

  <Step title="Use the session for automated browsing">
    Once your stealth session is created, you can use it for automated browsing that bypasses common detection mechanisms:

    <CodeGroup>
      ```JavaScript node.js theme={null}
      import Anchorbrowser from "anchorbrowser";

      const anchorClient = new Anchorbrowser()
       
      // Create stealth session
      const session = await anchorClient.sessions.create({
          browser: {
              extra_stealth: {
                  active: true
              }
          },
          session: {
              proxy: {
                  active: true
              }
          }
       })

      // Use the session for automated tasks
      const result = await anchorClient.agent.task(
          "Navigate to a website and check if I'm detected as a bot",
          {
              sessionId: session.data.id
          }
      );

      console.log(result);
      ```

      ```python python theme={null}
      from anchorbrowser import Anchorbrowser
      import os

      anchorClient = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

      # Create stealth session
      session = anchorClient.sessions.create(
          browser={
              "extra_stealth": {
                  "active": True
              }
          },
          session={
              "proxy": {
                  "active": True
              }
          }
      )

      # Use the session for automated tasks
      result = anchorClient.agent.task(
          session_options=session,
          prompt="Navigate to a website and check if I'm detected as a bot"
      )

      print(result)
      ```
    </CodeGroup>
  </Step>
</Steps>

## Usage with Profiles

Use stealth mode with saved browser profiles for persistent authenticated sessions:

<CodeGroup>
  ```JavaScript node.js theme={null}
  import Anchorbrowser from "anchorbrowser";

  const anchorClient = new Anchorbrowser()
  const session = await anchorClient.sessions.create({
      browser: {
          extra_stealth: {
              active: true
          },
          profile: {
              name: 'stealth-profile',
              persist: true   // Only on Profile Creation
          }
      },
      session: {
          proxy: {
              active: true
          }
      }
  })
  console.log(session)

  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os

  anchorClient = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
  session = anchorClient.sessions.create(
      browser={
          "extra_stealth": {
              "active": True
          },
          "profile": {
              "name": "stealth-profile",
              "persist": true   # Only on Profile Creation
          }
      },
      session={
          "proxy": {
              "active": True
          }
      }
  )
  print(session)
  ```
</CodeGroup>

## Enabling Console Logs

<Warning>
  When extra stealth mode is enabled, `page.on('console')` events are **disabled by default** to prevent detection. If you need to capture console output, you must explicitly enable it.
</Warning>

To receive console log events while using extra stealth, enable `console_logs` in your session configuration:

<CodeGroup>
  ```javascript node.js theme={null}
  import Anchorbrowser from "anchorbrowser";

  const anchorClient = new Anchorbrowser();

  const session = await anchorClient.sessions.create({
    browser: {
      extra_stealth: { active: true },
      console_logs: { active: true }
    },
    session: {
      proxy: { active: true }
    }
  });

  // Connect to the browser
  const browser = await anchorClient.browser.connect(session.data.id);
  const context = browser.contexts()[0];
  const page = context.pages()[0];

  // Now page.on('console') will work
  page.on('console', (msg) => {
    console.log(`[${msg.type()}] ${msg.text()}`);
  });

  await page.goto("https://example.com");
  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os

  anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

  session = anchor_client.sessions.create(
      browser={
          "extra_stealth": {"active": True},
          "console_logs": {"active": True}
      },
      session={
          "proxy": {"active": True}
      }
  )

  # Connect to the browser
  with anchor_client.browser.connect(session.data.id) as browser:
      context = browser.contexts[0]
      page = context.pages[0]

      # Now page.on('console') will work
      def handle_console(msg):
          print(f"[{msg.type}] {msg.text}")

      page.on("console", handle_console)

      page.goto("https://example.com")
  ```
</CodeGroup>

## Catching Captcha Events

When using stealth mode with captcha solving enabled, you can listen to captcha lifecycle events via CDP (Chrome DevTools Protocol). This allows you to track when captchas are detected, solved, or failed.

<CodeGroup>
  ```javascript node.js theme={null}
  import Anchorbrowser from "anchorbrowser";

  const anchorClient = new Anchorbrowser();

  // Create a session with extra stealth and captcha solving enabled
  const session = await anchorClient.sessions.create({
    browser: {
      extra_stealth: { active: true },
      captcha_solver: { active: true }
    },
    session: {
      proxy: { active: true }
    }
  });

  // Connect to the browser
  const browser = await anchorClient.browser.connect(session.data.id);
  const context = browser.contexts()[0];
  const page = context.pages()[0];

  // Create CDP session and listen to captcha events
  const client = await context.newCDPSession(page);

  client.on('Captcha.lifecycle', (event) => {
    if (event.name === 'detected') {
      console.log(`${event.captchaType} captcha detected on ${event.url}`);
    }
    
    if (event.name === 'solved') {
      console.log(`Captcha solved in ${event.timeToSolve}ms`);
    }

    if (event.name === 'failed') {
      console.log(`Captcha failed: ${event.error}`);
    }
  });

  // Navigate to a page with captcha
  await page.goto("https://example.com");
  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os

  anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

  # Create a session with extra stealth and captcha solving enabled
  session = anchor_client.sessions.create(
      browser={
          "extra_stealth": {"active": True},
          "captcha_solver": {"active": True}
      },
      session={
          "proxy": {"active": True}
      }
  )

  # Connect to the browser
  with anchor_client.browser.connect(session.data.id) as browser:
      context = browser.contexts[0]
      page = context.pages[0]

      # Create CDP session and listen to captcha events
      client = context.new_cdp_session(page)

      def handle_captcha_event(event):
          if event["name"] == "detected":
              print(f"{event['captchaType']} captcha detected on {event['url']}")
          
          if event["name"] == "solved":
              print(f"Captcha solved in {event['timeToSolve']}ms")
          
          if event["name"] == "failed":
              print(f"Captcha failed: {event['error']}")

      client.on("Captcha.lifecycle", handle_captcha_event)

      # Navigate to a page with captcha
      page.goto("https://example.com")
  ```
</CodeGroup>

### Event Types

| Event Name | Description                                   | Properties                      |
| ---------- | --------------------------------------------- | ------------------------------- |
| `detected` | Fired when a captcha is detected on the page  | `captchaType`, `url`            |
| `solved`   | Fired when the captcha is successfully solved | `timeToSolve` (in milliseconds) |
| `failed`   | Fired when captcha solving fails              | `error`                         |

# Source: https://docs.anchorbrowser.io/essentials/stealth.md

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


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.anchorbrowser.io/llms.txt
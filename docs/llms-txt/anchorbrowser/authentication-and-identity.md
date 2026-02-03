# Source: https://docs.anchorbrowser.io/essentials/authentication-and-identity.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Browser Profiles (Authenticated sessions)

Anchor allows you to save an existing browser state as "profiles" for use in future browser sessions. This feature enables users to:

* Store authenticated sessions and identities, allowing to stay logged in to websites
* Improve overall speed and performance

The following guide explains how to create and use Identity Profiles in Anchor Browser.

## Quick start - Create and use a profile

<Expandable title="Via SDK" defaultOpen>
  <Steps>
    <Step title="Start a session with a new profile">
      Create a session via SDK, Make sure to configure the new profile to persist.

      <CodeGroup>
        ```JavaScript node.js theme={null}
        import Anchorbrowser from "anchorbrowser";

        (async () => {
         const anchorClient = new Anchorbrowser()
         const session = await anchorClient.sessions.create({
            browser: {
                profile: {
                    name: 'new-profile',
                    persist: true
                    }
                }
            })
         console.log(session)
        })();
        ```

        ```python python theme={null}
        from anchorbrowser import Anchorbrowser
        import os

        anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
        session = anchor_client.sessions.create(browser={
            "profile": {
                "name": "new-profile",
                "persist": True
            }
        })
        print(session)
        ```
      </CodeGroup>
    </Step>

    <Step title="Authenticate Once">
      Authenticate to the target service and create a browser context with the required cookies and session data.

      <CodeGroup>
        ```JavaScript node.js theme={null}
        import Anchorbrowser from "anchorbrowser";

        (async () => {
         const anchorClient = new Anchorbrowser()
         const session = await anchorClient.sessions.create({
            browser: {
                profile: {
                    name: 'new-profile',
                    persist: true
                    }
                }
            })

         const sessionId = session.data.id;

         // Navigate to the login page
         await anchorClient.sessions.goto(sessionId, {
            url: 'https://example.com/login'
         })

         // Fill in your login credentials
         await anchorClient.sessions.mouse.click(sessionId, { x: 100, y: 200 })
         await anchorClient.sessions.keyboard.type(sessionId, { text: 'your-username' })

         await anchorClient.sessions.mouse.click(sessionId, { x: 100, y: 250 })
         await anchorClient.sessions.keyboard.type(sessionId, { text: 'your-password' })

         // Submit the login form
         await anchorClient.sessions.mouse.click(sessionId, { x: 100, y: 300 })

         console.log('Authentication completed. Profile will be saved when session ends.')
        })();
        ```

        ```python python theme={null}
        from anchorbrowser import Anchorbrowser
        import os

        anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
        session = anchor_client.sessions.create(browser={
            "profile": {
                "name": "new-profile",
                "persist": True
            }
        })

        session_id = session["data"]["id"]

        # Navigate to the login page
        anchor_client.sessions.goto(session_id, url="https://example.com/login")

        # Fill in your login credentials
        anchor_client.sessions.mouse.click(session_id, x=100, y=200)
        anchor_client.sessions.keyboard.type(session_id, text="your-username")

        anchor_client.sessions.mouse.click(session_id, x=100, y=250)
        anchor_client.sessions.keyboard.type(session_id, text="your-password")

        # Submit the login form
        anchor_client.sessions.mouse.click(session_id, x=100, y=300)

        print("Authentication completed. Profile will be saved when session ends.")
        ```
      </CodeGroup>
    </Step>

    <Step title="Save Profile">
      End the session. The profile will be automatically saved since you set `persist: true` when creating the session.

      <CodeGroup>
        ```JavaScript node.js theme={null}
        import Anchorbrowser from "anchorbrowser";

        (async () => {
         const anchorClient = new Anchorbrowser()

         // After completing authentication, end the session to save the profile
         await anchorClient.sessions.delete(sessionId)

         console.log('Session ended. Profile "new-profile" has been saved.')
        })();
        ```

        ```python python theme={null}
        from anchorbrowser import Anchorbrowser
        import os

        anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

        # After completing authentication, end the session to save the profile
        anchor_client.sessions.delete(session_id)

        print('Session ended. Profile "new-profile" has been saved.')
        ```
      </CodeGroup>
    </Step>

    <Step title="Use the profile in other sessions">
      Now, when creating a new session pass the `profile` parameter with the name of the profile you created to load the saved browser context.

      <CodeGroup>
        ```JavaScript node.js theme={null}
        import Anchorbrowser from "anchorbrowser";

        (async () => {
         const anchorClient = new Anchorbrowser()
         const session = await anchorClient.sessions.create({
            browser: {
                profile: {
                    name: 'new-profile'
                }
            }
            })
         console.log(session)
        })();
        ```

        ```python python theme={null}
        from anchorbrowser import Anchorbrowser
        import os

        anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
        session = anchor_client.sessions.create(browser={
            "profile": {
                "name": "new-profile"
            }
        })
        print(session)
        ```
      </CodeGroup>
    </Step>
  </Steps>
</Expandable>

<Expandable title="Via UI" defaultOpen>
  <Steps>
    <Step title="Start a session with a new profile">
      Through the Anchor playground, create a profile on the configuration area. Then, click to start a session.

      <img src="https://mintcdn.com/anchor-b3ec2715/gNwz9f2wKiBAjmbK/images/profile-create.png?fit=max&auto=format&n=gNwz9f2wKiBAjmbK&q=85&s=ba567b5ede7d85d69a465d727b6793cf" alt="Create profile in playground" data-og-width="848" width="848" data-og-height="692" height="692" data-path="images/profile-create.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anchor-b3ec2715/gNwz9f2wKiBAjmbK/images/profile-create.png?w=280&fit=max&auto=format&n=gNwz9f2wKiBAjmbK&q=85&s=6588b9f06bf34183b74ab4d2df0f2b1d 280w, https://mintcdn.com/anchor-b3ec2715/gNwz9f2wKiBAjmbK/images/profile-create.png?w=560&fit=max&auto=format&n=gNwz9f2wKiBAjmbK&q=85&s=253c8033f42cb35319e507f16c8637b5 560w, https://mintcdn.com/anchor-b3ec2715/gNwz9f2wKiBAjmbK/images/profile-create.png?w=840&fit=max&auto=format&n=gNwz9f2wKiBAjmbK&q=85&s=6c4ac0b9bcd85a57b47e103c3981f4df 840w, https://mintcdn.com/anchor-b3ec2715/gNwz9f2wKiBAjmbK/images/profile-create.png?w=1100&fit=max&auto=format&n=gNwz9f2wKiBAjmbK&q=85&s=18dcf1a0098c0bd979f802cdd469f986 1100w, https://mintcdn.com/anchor-b3ec2715/gNwz9f2wKiBAjmbK/images/profile-create.png?w=1650&fit=max&auto=format&n=gNwz9f2wKiBAjmbK&q=85&s=9beac8d27ee4256120853639e9b3dc47 1650w, https://mintcdn.com/anchor-b3ec2715/gNwz9f2wKiBAjmbK/images/profile-create.png?w=2500&fit=max&auto=format&n=gNwz9f2wKiBAjmbK&q=85&s=bf988345d1448fca3a2e00d64062f733 2500w" />
    </Step>

    <Step title="Authenticate Once">
      Authenticate to the target service using the playground to create a browser context with the required cookies and session data.
    </Step>

    <Step title="Save Profile">
      Save the profile using the 'Save Profile' button in the Anchor Browser Playground.
      <Note>This operation will end the current playground browser session</Note>

      <img src="https://mintcdn.com/anchor-b3ec2715/gNwz9f2wKiBAjmbK/images/profile-save.png?fit=max&auto=format&n=gNwz9f2wKiBAjmbK&q=85&s=d8ffb3b7d286d0f96fb0e52787f6458e" alt="Save profile in playground" data-og-width="624" width="624" data-og-height="188" height="188" data-path="images/profile-save.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anchor-b3ec2715/gNwz9f2wKiBAjmbK/images/profile-save.png?w=280&fit=max&auto=format&n=gNwz9f2wKiBAjmbK&q=85&s=21499a1a7e89195e28d06a8c17c24d19 280w, https://mintcdn.com/anchor-b3ec2715/gNwz9f2wKiBAjmbK/images/profile-save.png?w=560&fit=max&auto=format&n=gNwz9f2wKiBAjmbK&q=85&s=40bb58135dafbe0818db43d842fdebe4 560w, https://mintcdn.com/anchor-b3ec2715/gNwz9f2wKiBAjmbK/images/profile-save.png?w=840&fit=max&auto=format&n=gNwz9f2wKiBAjmbK&q=85&s=aa655f1cdb5e843abd0b1d1531ddc511 840w, https://mintcdn.com/anchor-b3ec2715/gNwz9f2wKiBAjmbK/images/profile-save.png?w=1100&fit=max&auto=format&n=gNwz9f2wKiBAjmbK&q=85&s=ad3506904c5f9c804423b402d41f37b4 1100w, https://mintcdn.com/anchor-b3ec2715/gNwz9f2wKiBAjmbK/images/profile-save.png?w=1650&fit=max&auto=format&n=gNwz9f2wKiBAjmbK&q=85&s=8ad71b63014b649bdf365cd4199746d7 1650w, https://mintcdn.com/anchor-b3ec2715/gNwz9f2wKiBAjmbK/images/profile-save.png?w=2500&fit=max&auto=format&n=gNwz9f2wKiBAjmbK&q=85&s=4556fc858758e7fdbb3904ee4598fcad 2500w" />

      Then approve it in the popup window 'Yes, Save and Terminate'

      <img src="https://mintcdn.com/anchor-b3ec2715/gNwz9f2wKiBAjmbK/images/profile-confirm.png?fit=max&auto=format&n=gNwz9f2wKiBAjmbK&q=85&s=cf881132cfe21e46430f42af6096cbef" alt="Confirm profile save" data-og-width="1128" width="1128" data-og-height="364" height="364" data-path="images/profile-confirm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anchor-b3ec2715/gNwz9f2wKiBAjmbK/images/profile-confirm.png?w=280&fit=max&auto=format&n=gNwz9f2wKiBAjmbK&q=85&s=3381963e33a467191992cecaf7fb3e36 280w, https://mintcdn.com/anchor-b3ec2715/gNwz9f2wKiBAjmbK/images/profile-confirm.png?w=560&fit=max&auto=format&n=gNwz9f2wKiBAjmbK&q=85&s=e565f397c48a94d9470107adc639da39 560w, https://mintcdn.com/anchor-b3ec2715/gNwz9f2wKiBAjmbK/images/profile-confirm.png?w=840&fit=max&auto=format&n=gNwz9f2wKiBAjmbK&q=85&s=5012d3d96ffa834d35c807cda269dd32 840w, https://mintcdn.com/anchor-b3ec2715/gNwz9f2wKiBAjmbK/images/profile-confirm.png?w=1100&fit=max&auto=format&n=gNwz9f2wKiBAjmbK&q=85&s=a24ac054c186218c096c8fd019237a48 1100w, https://mintcdn.com/anchor-b3ec2715/gNwz9f2wKiBAjmbK/images/profile-confirm.png?w=1650&fit=max&auto=format&n=gNwz9f2wKiBAjmbK&q=85&s=ace5599dbc198f265fa84e5c05927575 1650w, https://mintcdn.com/anchor-b3ec2715/gNwz9f2wKiBAjmbK/images/profile-confirm.png?w=2500&fit=max&auto=format&n=gNwz9f2wKiBAjmbK&q=85&s=a60df27d31fb2870f8603a32bcb399a5 2500w" />
    </Step>

    <Step title="Use the profile in other sessions">
      Select the saved profile from the dropdown in the playground configuration area when starting a new session.

      <img src="https://mintcdn.com/anchor-b3ec2715/gNwz9f2wKiBAjmbK/images/profile-reuse.png?fit=max&auto=format&n=gNwz9f2wKiBAjmbK&q=85&s=328c09eda74988b1c2523a70c8222bb6" alt="Reuse saved profile" data-og-width="814" width="814" data-og-height="606" height="606" data-path="images/profile-reuse.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anchor-b3ec2715/gNwz9f2wKiBAjmbK/images/profile-reuse.png?w=280&fit=max&auto=format&n=gNwz9f2wKiBAjmbK&q=85&s=4a97928d72444823fe9ccf0f818bf2c6 280w, https://mintcdn.com/anchor-b3ec2715/gNwz9f2wKiBAjmbK/images/profile-reuse.png?w=560&fit=max&auto=format&n=gNwz9f2wKiBAjmbK&q=85&s=9636dd11441a35651b4684412ce215ac 560w, https://mintcdn.com/anchor-b3ec2715/gNwz9f2wKiBAjmbK/images/profile-reuse.png?w=840&fit=max&auto=format&n=gNwz9f2wKiBAjmbK&q=85&s=a1fbd4add893479082e43d3049c6f086 840w, https://mintcdn.com/anchor-b3ec2715/gNwz9f2wKiBAjmbK/images/profile-reuse.png?w=1100&fit=max&auto=format&n=gNwz9f2wKiBAjmbK&q=85&s=18c75651bc923ebcfba73330b686463b 1100w, https://mintcdn.com/anchor-b3ec2715/gNwz9f2wKiBAjmbK/images/profile-reuse.png?w=1650&fit=max&auto=format&n=gNwz9f2wKiBAjmbK&q=85&s=d31a31a62a61d3ce598bc22623499b1e 1650w, https://mintcdn.com/anchor-b3ec2715/gNwz9f2wKiBAjmbK/images/profile-reuse.png?w=2500&fit=max&auto=format&n=gNwz9f2wKiBAjmbK&q=85&s=aaf09a7f38ac9c4f1a8c17448f91ddc5 2500w" />
    </Step>
  </Steps>
</Expandable>

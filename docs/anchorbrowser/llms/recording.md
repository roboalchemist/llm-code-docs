# Source: https://docs.anchorbrowser.io/essentials/recording.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Session Recording

> Record browser sessions for debugging, analysis, and documentation

## Overview

Anchor Browser provides built-in session recording that allows you to capture and review browser sessions. This feature is invaluable for debugging automation workflows, analyzing user behavior, and creating documentation.

## How It Works

Anchor Browser automatically records browser sessions and creates an MP4 video file that captures the complete visual experience.
Recordings are accessible both through our API and the web UI (see below).

<Expandable title="SDK Usage">
  # SDK Usage

  ## Record a Session

  Recording is enabled by default when creating a session.
  Start a session using the [SDK](/quickstart/use-via-sdk), you can enable recording by setting:
  `recording` -> `active` -> `true` in the request body.

  <CodeGroup>
    ```javascript node.js theme={null}
    import AnchorBrowser from 'anchorbrowser';

    (async () => {
      const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
      
      const response = await anchorClient.sessions.create({
        session: {
          recording: {
            active: true   // Enable recording (default)
          }
        }
      });
      
      const sessionId = response.data.id
      console.log("Session created:", response.data);
    })().catch(console.error);
    ```

    ```python python theme={null}
    import os
    from anchorbrowser import Anchorbrowser

    anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

    response = anchor_client.sessions.create(
        session={
            "recording": {
                "active": True  # Enable recording (default)
            }
        }
    )

    session_id = response.data.id
    print("Session created:", session_id)
    ```
  </CodeGroup>

  ## Get Session Recordings

  Retrieve recordings for a specific session:

  <CodeGroup>
    ```javascript node.js theme={null}
    import AnchorBrowser from 'anchorbrowser';

    (async () => {
      const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
      
      const recordings = await anchorClient.sessions.recordings.list(sessionId);
      console.log("Recordings:", recordings.data);
    })().catch(console.error);
    ```

    ```python python theme={null}
    import os
    from anchorbrowser import Anchorbrowser

    anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

    recordings = anchor_client.sessions.recordings.list(session_id)
    print("Recordings:", recordings.data)
    ```
  </CodeGroup>

  ## Download Recording

  Download a specific recording file:

  <CodeGroup>
    ```javascript node.js theme={null}
      import AnchorBrowser from 'anchorbrowser';
      import { writeFile } from 'node:fs/promises';
      
      (async () => {
        const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
        // const sessionId = 'your-session-id'; // Replace with actual session ID
        
        const recording = await anchorClient.sessions.recordings.primary.get(sessionId);
        
        // Save to file
        const buffer = await recording.arrayBuffer();
        await writeFile(`recording-${sessionId}.mp4`, Buffer.from(buffer));
        
        console.log(`Recording saved as recording-${sessionId}.mp4`);
      })().catch(console.error);
    ```

    ```python python theme={null}
      import os
      from anchorbrowser import Anchorbrowser

      anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
      session_id = "your-session-id"  # Replace with actual session ID

      recording = anchor_client.sessions.recordings.primary.get(session_id)

      # Save to file
      with open(f"recording-{session_id}.mp4", "wb") as f:
          for chunk in recording.iter_bytes(chunk_size=8192):
              f.write(chunk)

      print(f"Recording saved as recording-{session_id}.mp4")
    ```
  </CodeGroup>
</Expandable>

<Expandable title="Web UI Usage">
  # Web UI Usage

  ## Create a Session

  In order to create a session through the UI with recording enabled use the [playground](https://app.anchorbrowser.io/playground), it will be recorded by default.

  <img className="mx-auto" src="https://mintcdn.com/anchor-b3ec2715/Fx9t9aj1txSbvvH0/images/recording-ui-start-session.png?fit=max&auto=format&n=Fx9t9aj1txSbvvH0&q=85&s=283f14ef3a6948ccee4b9194851beb2c" alt="Starting a session to be recorded in the playground" width="700" data-og-width="3678" data-og-height="1250" data-path="images/recording-ui-start-session.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anchor-b3ec2715/Fx9t9aj1txSbvvH0/images/recording-ui-start-session.png?w=280&fit=max&auto=format&n=Fx9t9aj1txSbvvH0&q=85&s=e42185db96b105a25fcbf83d1123dc62 280w, https://mintcdn.com/anchor-b3ec2715/Fx9t9aj1txSbvvH0/images/recording-ui-start-session.png?w=560&fit=max&auto=format&n=Fx9t9aj1txSbvvH0&q=85&s=1da30b3e0075a8957ca7214d9b5a8a38 560w, https://mintcdn.com/anchor-b3ec2715/Fx9t9aj1txSbvvH0/images/recording-ui-start-session.png?w=840&fit=max&auto=format&n=Fx9t9aj1txSbvvH0&q=85&s=aaeffb38ba44be49c7052976c6792a92 840w, https://mintcdn.com/anchor-b3ec2715/Fx9t9aj1txSbvvH0/images/recording-ui-start-session.png?w=1100&fit=max&auto=format&n=Fx9t9aj1txSbvvH0&q=85&s=dae7a0f792a768e6bc5da970c3f46c51 1100w, https://mintcdn.com/anchor-b3ec2715/Fx9t9aj1txSbvvH0/images/recording-ui-start-session.png?w=1650&fit=max&auto=format&n=Fx9t9aj1txSbvvH0&q=85&s=c8db8e3e8c88076b129bb639f4937841 1650w, https://mintcdn.com/anchor-b3ec2715/Fx9t9aj1txSbvvH0/images/recording-ui-start-session.png?w=2500&fit=max&auto=format&n=Fx9t9aj1txSbvvH0&q=85&s=a5c55a0f68a04a3513393383bdab2dd7 2500w" />

  ## Session Recordings

  The Session History dashboard shows all sessions. Each session has a link to its recording.

  <Warning>
    If a session is still running, the link in the session history page will take you to the session's live view instead of the recording. Once the session ends, the link will point to the recording.
  </Warning>

  <img className="mx-auto" src="https://mintcdn.com/anchor-b3ec2715/Fx9t9aj1txSbvvH0/images/recording-ui-session-history.png?fit=max&auto=format&n=Fx9t9aj1txSbvvH0&q=85&s=0c9dbea9a2d36c8464678bdfc9d47bc7" alt="Session history dashboard showing list of sessions" data-og-width="3346" width="3346" data-og-height="832" height="832" data-path="images/recording-ui-session-history.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anchor-b3ec2715/Fx9t9aj1txSbvvH0/images/recording-ui-session-history.png?w=280&fit=max&auto=format&n=Fx9t9aj1txSbvvH0&q=85&s=6b0c406064ea72da7d436427032be429 280w, https://mintcdn.com/anchor-b3ec2715/Fx9t9aj1txSbvvH0/images/recording-ui-session-history.png?w=560&fit=max&auto=format&n=Fx9t9aj1txSbvvH0&q=85&s=17c22d02134427ad9d674b782b38bfc1 560w, https://mintcdn.com/anchor-b3ec2715/Fx9t9aj1txSbvvH0/images/recording-ui-session-history.png?w=840&fit=max&auto=format&n=Fx9t9aj1txSbvvH0&q=85&s=745af978c9b3c2cdd66966e2981108c0 840w, https://mintcdn.com/anchor-b3ec2715/Fx9t9aj1txSbvvH0/images/recording-ui-session-history.png?w=1100&fit=max&auto=format&n=Fx9t9aj1txSbvvH0&q=85&s=300e4abe7c7b707b109a7adf0a2fa34b 1100w, https://mintcdn.com/anchor-b3ec2715/Fx9t9aj1txSbvvH0/images/recording-ui-session-history.png?w=1650&fit=max&auto=format&n=Fx9t9aj1txSbvvH0&q=85&s=647e621174a1141302580fae54641dfc 1650w, https://mintcdn.com/anchor-b3ec2715/Fx9t9aj1txSbvvH0/images/recording-ui-session-history.png?w=2500&fit=max&auto=format&n=Fx9t9aj1txSbvvH0&q=85&s=ab03169a008eec5b47f8727dfd5db7d6 2500w" />

  ## Recording Playback

  When you click on a session recording, the playback interface will be opened.
  You can use it to view the recording, navigate through it, and download it as MP4 file.

  <img className="mx-auto" src="https://mintcdn.com/anchor-b3ec2715/Fx9t9aj1txSbvvH0/images/recording-ui-session-history-download.png?fit=max&auto=format&n=Fx9t9aj1txSbvvH0&q=85&s=34752c0c995dd14c0bce7339156b5435" alt="Recording playback interface with video controls" width="800" data-og-width="3470" data-og-height="1710" data-path="images/recording-ui-session-history-download.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anchor-b3ec2715/Fx9t9aj1txSbvvH0/images/recording-ui-session-history-download.png?w=280&fit=max&auto=format&n=Fx9t9aj1txSbvvH0&q=85&s=6ee49cd051fde3fc372b5b7a230e06f8 280w, https://mintcdn.com/anchor-b3ec2715/Fx9t9aj1txSbvvH0/images/recording-ui-session-history-download.png?w=560&fit=max&auto=format&n=Fx9t9aj1txSbvvH0&q=85&s=08821fb3bb16337e1bce7551d0c2e56a 560w, https://mintcdn.com/anchor-b3ec2715/Fx9t9aj1txSbvvH0/images/recording-ui-session-history-download.png?w=840&fit=max&auto=format&n=Fx9t9aj1txSbvvH0&q=85&s=80c1551ce2e36dcbc7fe273b1503df85 840w, https://mintcdn.com/anchor-b3ec2715/Fx9t9aj1txSbvvH0/images/recording-ui-session-history-download.png?w=1100&fit=max&auto=format&n=Fx9t9aj1txSbvvH0&q=85&s=fd0e35092af137db0a83e2b5c060ed9b 1100w, https://mintcdn.com/anchor-b3ec2715/Fx9t9aj1txSbvvH0/images/recording-ui-session-history-download.png?w=1650&fit=max&auto=format&n=Fx9t9aj1txSbvvH0&q=85&s=ce0d3ca2bf6a23730f11e169544e1530 1650w, https://mintcdn.com/anchor-b3ec2715/Fx9t9aj1txSbvvH0/images/recording-ui-session-history-download.png?w=2500&fit=max&auto=format&n=Fx9t9aj1txSbvvH0&q=85&s=30ed67282de00d1c3deec661b02ed684 2500w" />
</Expandable>

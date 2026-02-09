# Source: https://docs.anchorbrowser.io/integrations/browseruse-deployment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Browser-use

<Note>This guide is dedicated to running your own browser-use agent while connecting to an Anchor browser. To use the embedded browser use capability, refer to [AI task completion](/agentic-browser-control/ai-task-completion)</Note>

<Steps>
  <Step title="Step one - Create an Anchor Browser session">
    ```python python theme={null}
    from anchorbrowser import Anchorbrowser
    import os

    anchor_client = Anchorbrowser(
        api_key=os.getenv("ANCHOR_API_KEY")
    )

    session = anchor_client.sessions.create()
    cdp_url = session.data.cdp_url
    print("Session's CDP_URL for later use\n", cdp_url)
    ```
  </Step>

  <Step title="Initialize browser-use with Anchor browser">
    ```python python theme={null}
    from browser_use import Agent, Controller
    from browser_use.browser import BrowserProfile, BrowserSession
    from browser_use.llm import ChatOpenAI
    import os

    # Configure your LLM (example with OpenAI)
    llm = ChatOpenAI(
        model='gpt-4o',
        api_key=os.getenv('OPENAI_API_KEY'),
    )

    # Initialize browser session with Anchor
    profile = BrowserProfile(keep_alive=True)
    browser_session = BrowserSession(
        headless=False, 
        cdp_url=cdp_url, 
        browser_profile=profile
    )

    # Create controller and agent
    controller = Controller()
    agent = Agent(
        task="Your task description here",
        llm=llm,
        enable_memory=False,
        use_vision=False,
        controller=controller,
        browser_session=browser_session,
    )

    # Run the agent
    result = await agent.run(max_steps=40)
    ```
  </Step>

  <Step title="Optional - Live view the browser">
    Use the `live_view_url` returned on the first step to view the browser session in real-time, or to embed it as a UI component

    ```html  theme={null}
    <!-- Make sure to replace <session_id> with the 
        actual session ID from the first step -->
    <iframe src="https://live.anchorbrowser.io?sessionId=<session_id>" 
        sandbox="allow-same-origin allow-scripts" 
        allow="clipboard-read; clipboard-write" 
        style="border: 0px; display: block; width: 100%; height: 100%;
        position: absolute; top: 0px; left: 0px;">
    </iframe>
    ```
  </Step>
</Steps>

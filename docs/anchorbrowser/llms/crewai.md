# Source: https://docs.anchorbrowser.io/agent-frameworks/crewai.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# CrewAI

AI agents can leverage browser sessions to complete tasks in the web. The ways to use the browser in CrewAI agent platform are:

* **As a Flexible Browser Tool**: Enable the CrewAI agent to explore the web freely using a general-purpose browser tool.
* **As a Specific-Flow Tool Defined in CrewAI**: Create custom tools by writing CrewAI code to define specific workflows tailored to your needs.
* **As a Specific-Flow Tool Defined in Anchor Browser**: Define tools using the Anchor platform, which CrewAI agents can then use through the Official Anchor Tool.

## Quick start - Use Anchor Browser as a flexible browser tool

You can connect your CrewAI agent directly to Anchor Browser, allowing it to use browser sessions for various tasks, leveraging the power of browser automation without the need for complex integration code. Below is a quick guide to setting up and using Anchor Browser as a tool for your CrewAI agent.

<Accordion title="Code example - Use Anchor Browser as a flexible browser tool">
  <CodeGroup>
    ```python python theme={null}
    import os
    from anchorbrowser import Anchorbrowser
    from crewai import Agent, Task, Crew

    ANCHOR_API_KEY = os.getenv("ANCHOR_API_KEY")

    # Create an Anchor Browser tool for CrewAI
    class AnchorBrowserTool:
        def __init__(self):
            self.anchor_client = Anchorbrowser(api_key=ANCHOR_API_KEY)
        
        def browse_and_extract(self, url, task_description):
            # Create a browser session
            session = self.anchor_client.sessions.create(
                session={
                    "max_duration": 30,
                    "idle_timeout": 10
                }
            )
            
            try:
                # Use the agent to perform the task
                result = self.anchor_client.agent.task(
                    task_description,
                    task_options={
                        "url": url,
                        "session_id": session.id
                    }
                )
                return result
            finally:
                # Clean up
                self.anchor_client.sessions.terminate(session.id)

    # Initialize the tool
    browser_tool = AnchorBrowserTool()

    # Create a CrewAI agent that uses Anchor Browser
    researcher = Agent(
        role='Web Researcher',
        goal='Research and extract information from websites',
        backstory='Expert at gathering information from web sources',
        tools=[browser_tool.browse_and_extract],
        verbose=True
    )

    # Create a task
    research_task = Task(
        description='Go to news.ycombinator.com and extract the title of the first story',
        agent=researcher
    )

    # Create and run the crew
    crew = Crew(
        agents=[researcher],
        tasks=[research_task],
        verbose=True
    )

    result = crew.kickoff()
    print(result)
    ```

    ```javascript node.js theme={null}
    const { AnchorClient } = require("anchorbrowser");
    const { Agent, Task, Crew } = require("crewai");

    class AnchorBrowserTool {
        constructor() {
            this.anchorClient = new AnchorClient({
                apiKey: process.env.ANCHOR_API_KEY,
            });
        }
        
        async browseAndExtract(url, taskDescription) {
            // Create a browser session
            const session = await this.anchorClient.sessions.create({
                session: {
                    max_duration: 30,
                    idle_timeout: 10
                }
            });
            
            try {
                // Use the agent to perform the task
                const result = await this.anchorClient.agent.task(
                    taskDescription,
                    { sessionId: session.id }
                );
                return result;
            } finally {
                // Clean up
                await this.anchorClient.sessions.terminate(session.id);
            }
        }
    }

    // Initialize the tool
    const browserTool = new AnchorBrowserTool();

    // Create a CrewAI agent that uses Anchor Browser
    const researcher = new Agent({
        role: 'Web Researcher',
        goal: 'Research and extract information from websites',
        backstory: 'Expert at gathering information from web sources',
        tools: [browserTool.browseAndExtract.bind(browserTool)],
        verbose: true
    });

    // Create a task
    const researchTask = new Task({
        description: 'Go to news.ycombinator.com and extract the title of the first story',
        agent: researcher
    });

    // Create and run the crew
    const crew = new Crew({
        agents: [researcher],
        tasks: [researchTask],
        verbose: true
    });

    const result = await crew.kickoff();
    console.log(result);
    ```
  </CodeGroup>
</Accordion>

## Use Anchor Browser as a specific-flow tool defined in CrewAI

CrewAI can integrate closely with Anchor Browser to define tools for particular workflows. For example, if you need a customized process to interact with an authenticated application, you can create that flow as a reusable tool that CrewAI agents can use for automation.

Here is an example of creating a specific workflow tool using Anchor Browser that can be utilized by CrewAI to automate targeted tasks.

<Accordion title="Code example - Use Anchor Browser as a specific-flow tool defined in CrewAI">
  <CodeGroup>
    ```python python theme={null}

    import crewai
    from playwright.sync_api import sync_playwright

    ANCHOR_API_KEY = "YOUR_ANCHOR_API_KEY"  # Replace with your actual API key

    # Register Anchor Browser as a specific application tool in CrewAI
    class AnchorSpecificTool(crewai.Tool):
        name = "SpecificAnchorTool"
        description = "Custom tool for interacting with a specific application."

        def __init__(self):
            super().__init__()

            anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
            with sync_playwright() as p:
                # Create a browser session
                session = anchor_client.sessions.create()
                cdp_url = session.data.cdp_url
            
                # Connect to Anchor Browser session
                browser = p.chromium.connect_over_cdp(cdp_url)
                page = browser.new_page()
                page.goto(command['url'])

                # Perform specific actions based on command
                if command.get('action') == 'extract':
                    result = page.text_content(command['selector'])
                    browser.close()
                    return result

                browser.close()

    # Add custom AnchorBrowserTool to CrewAI agent
    my_agent = crewai.Agent(name="Web Automation Agent")
    my_agent.add_tool(AnchorSpecificTool())

    # Use the agent to perform a specific task
    result = my_agent.act({
        'tool': 'SpecificAnchorTool',
        'command': {
            'url': 'https://example.com',
            'action': 'extract',
            'selector': 'body'
        }
    })

    print(result)
    ```

    ```jsx node.js theme={null}
    const { chromium } = require('playwright-core');
    const AnchorClient = require('anchorbrowser');
    const crewai = require('crewai');

    // Define a custom specific-flow tool in CrewAI that uses Anchor Browser
    class AnchorSpecificTool {
      name = "SpecificAnchorTool";
      description = "Custom tool for interacting with a specific application.";

      async run(command) {
        const anchorClient = new AnchorClient({
            apiKey: process.env.ANCHOR_API_KEY,
        });

        // Create a browser session
        const session = await anchorClient.sessions.create();
        const cdp_url = session.data.cdp_url;

        // Connect to Anchor Browser session
        const browser = await chromium.connectOverCDP(cdp_url);

        const page = await browser.newPage();
        await page.goto(command.url);

        // Perform specific actions based on the command
        if (command.action === 'extract') {
          const result = await page.textContent(command.selector);
          await browser.close();
          return result;
        }

        await browser.close();
      }
    }

    // Create a CrewAI agent and add the custom specific-flow Anchor Browser tool
    const agent = new crewai.Agent({ name: "Web Automation Agent" });
    const anchorSpecificTool = new AnchorSpecificTool();
    agent.addTool(anchorSpecificTool);

    // Use the tool through the CrewAI agent
    const result = await agent.act({
      tool: 'SpecificAnchorTool',
      command: {
        url: 'https://example.com',
        action: 'extract',
        selector: 'body'
      }
    });

    console.log(result);
    ```
  </CodeGroup>
</Accordion>

# Source: https://docs.brightdata.com/ai/mcp-server/integrations/agent-builder.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI's Agent Builder MCP Server Integration

> How to integrate Agent Builder with Bright Data's MCP server to create AI Agents.

<Card title="Building an AI startup?" cta="Learn more" href="https://brightdata.com/ai/ai-startups-program" icon="rocket-launch" iconType="duotone" arrow="true">
  You might be eligible for our Startup Program. Get fully funded access to the infrastructure you're reading about right now (up to \$20K value).
</Card>

**Requirements:**

* [Bright Data account](https://brightdata.com/?hs_signup=1\&utm_source=docs)
* OpenAI Account with a [verified organization](https://help.openai.com/en/articles/10910291-api-organization-verification)

<Steps>
  <Step title="Create a new flow">
    Go to [Agent Builder](https://platform.openai.com/agent-builder) and create a new flow

        <img src="https://mintcdn.com/brightdata/fFraBjMeOL_w74GS/images/Screenshot2025-10-10at10.27.55.png?fit=max&auto=format&n=fFraBjMeOL_w74GS&q=85&s=bf25f8712081d6ac13a3cf09549da5ff" alt="Screenshot 2025-10-10 at 10.27.55.png" width="1431" height="510" data-path="images/Screenshot2025-10-10at10.27.55.png" />
  </Step>

  <Step title="Click on the agent node">
        <img src="https://mintcdn.com/brightdata/fFraBjMeOL_w74GS/images/Screenshot2025-10-10at10.30.51.png?fit=max&auto=format&n=fFraBjMeOL_w74GS&q=85&s=2540abed9918e39d3de60b62be3c9e9c" alt="Screenshot 2025-10-10 at 10.30.51.png" width="1339" height="618" data-path="images/Screenshot2025-10-10at10.30.51.png" />

    After clicking the agent node, the agent configuration panel will appear on the left side of the screen.
  </Step>

  <Step title="Click on Tools to add the MCP">
        <img src="https://mintcdn.com/brightdata/fFraBjMeOL_w74GS/images/Screenshot2025-10-10at10.32.45.png?fit=max&auto=format&n=fFraBjMeOL_w74GS&q=85&s=8b0d7fa9fd19e153ee4c974395b15ed2" alt="Screenshot 2025-10-10 at 10.32.45.png" width="375" height="529" data-path="images/Screenshot2025-10-10at10.32.45.png" />
  </Step>

  <Step title="Choose MCP and add the Web MCP server">
    Copy and paste the following URL into the URL section:

    ```
    https://mcp.brightdata.com/mcp?token=YOUR_API_KEY
    ```

    Replace `YOUR_API_KEY` with your actual Bright Data API key.

    <Note>
      You can copy this URL with a pre-filled API key from your [control panel](https://brightdata.com/cp/mcp)
    </Note>

    Then click the Connect button.

        <img src="https://mintcdn.com/brightdata/fFraBjMeOL_w74GS/images/Screenshot2025-10-10at10.40.55.png?fit=max&auto=format&n=fFraBjMeOL_w74GS&q=85&s=ffcb3638097163f372023019c9f8aad1" alt="Screenshot 2025-10-10 at 10.40.55.png" width="524" height="668" data-path="images/Screenshot2025-10-10at10.40.55.png" />
  </Step>

  <Step title="Choose your preferred tools and add them">
    Here you can choose the relevant tools you want to expose to the agent, or add all of them by clicking the Add button.

        <img src="https://mintcdn.com/brightdata/fFraBjMeOL_w74GS/images/Screenshot2025-10-10at10.44.46.png?fit=max&auto=format&n=fFraBjMeOL_w74GS&q=85&s=815f30c45e4c6b8cd35b90ece1b47277" alt="Screenshot 2025-10-10 at 10.44.46.png" width="522" height="566" data-path="images/Screenshot2025-10-10at10.44.46.png" />
  </Step>

  <Step title="Configure your agent with a name and instructions">
    Give your agent a name, provide an instruction set, choose the reasoning effort level, and click the Preview button to test it.

        <img src="https://mintcdn.com/brightdata/fFraBjMeOL_w74GS/images/Screenshot2025-10-10at10.48.31.png?fit=max&auto=format&n=fFraBjMeOL_w74GS&q=85&s=0a170e98701f8a9d9d3a8ad92ea3008c" alt="Screenshot 2025-10-10 at 10.48.31.png" width="356" height="556" data-path="images/Screenshot2025-10-10at10.48.31.png" />
  </Step>

  <Step title="Test your agent">
    Ask your agent any question that requires real-time web data and get an instant answer.

    <img src="https://mintcdn.com/brightdata/fFraBjMeOL_w74GS/images/Screenshot2025-10-10at10.52.31.png?fit=max&auto=format&n=fFraBjMeOL_w74GS&q=85&s=395ead6d155bf53a2e72537c9d01ddc8" alt="Screenshot 2025-10-10 at 10.52.31.png" width="1672" height="746" data-path="images/Screenshot2025-10-10at10.52.31.png" />
  </Step>
</Steps>

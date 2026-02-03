# Source: https://dev.writer.com/connectors/pitchbook.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# PitchBook connector

> Connect WRITER Agent to PitchBook to access private market data and investment analytics

This guide shows you how to configure the [PitchBook](https://pitchbook.com/) connector for WRITER Agent. After setting up this connector, WRITER Agent can perform operations like exploring private market data including company profiles, funding rounds, valuations, investor information, and deal histories.

## Set up the PitchBook connector

Configure the PitchBook connector in [AI Studio](https://app.writer.com/aistudio) under **Connectors & Tools**. The PitchBook connector uses API key authentication.

### Obtain a PitchBook API key

Create an API key in PitchBook:

1. Log in to your PitchBook account
2. Navigate to API settings or contact PitchBook support for API access
3. Generate a new API key
4. Copy the API key for use in AI Studio

For detailed instructions, see [PitchBook's API documentation](https://pitchbook.com/help/PitchBook-api).

### Configure the connector in AI Studio

After obtaining your PitchBook API key:

1. Navigate to **Connectors & Tools** in [AI Studio](https://app.writer.com/aistudio)
2. Select the PitchBook connector
3. Select who has access by default (all users or specific teams)
4. Select which tools to enable for your agents
5. Enter your PitchBook API key

## Next steps

* [Set up connectors](https://support.writer.com/article/299-setting-up-connectors): Learn how to configure and enable connectors in AI Studio
* [Tool calling guide](/home/tool-calling): Understand how AI agents use tools in conversations
* [Action Agent guide](https://support.writer.com/article/293-how-to-use-action-agent): Learn how to use Action Agent with connected tools
* [MCP gateway overview](/home/mcp-gateway): Learn about Writer's MCP gateway architecture

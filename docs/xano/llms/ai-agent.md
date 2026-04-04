# Source: https://docs.xano.com/building/logic/triggers/ai-agent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# AI Agent Trigger

<Steps>
  <Step title="AI Agent Triggers">
    AI Agent triggers can be created to run any time an agent is called. This is useful for things like logging agent calls, dynamically updating tool instructions, or for modifying the agent's toolset based on certain conditions.

    You can find AI Agent triggers by clicking the settings icon in the top-right corner of your agent and choosing **Triggers**.

    Agent Triggers offer the following inputs:

    `toolset`\
    Contains the toolset information, such as the name and instructions.

    ```json  theme={null}
    {
      "id": 1,
      "name": "Agent Name",
      "instructions": "Agent Instructions"
    }
    ```

    `tools[]`\
    An array that contains each tool included in the toolset.

    ```json  theme={null}
      {
        "id": 1,
        "name": "Log Records",
        "instructions": "Logs action taken by the agent"
    }
    ```

    You can modify the tools or toolset by building logic in the trigger to do so.
  </Step>
</Steps>


Built with [Mintlify](https://mintlify.com).
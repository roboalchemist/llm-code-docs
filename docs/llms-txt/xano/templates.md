# Source: https://docs.xano.com/ai-tools/agents/templates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Templates

> Agent Templates

<CardGroup cols={2}>
  <Card title="Agent History & Debugging Mode" icon="rectangle-history-circle-plus" img="/images/YT1.png" href="/ai-tools/agents/templates#agent-history-%26-debugging-mode">
    Install this snippet to monitor, analyze, and debug your agent’s behavior.
    Gain critical insight into every agent run.
  </Card>

  <Card title="Conversation History" icon="comments" img="/images/YT3.png" href="/ai-tools/agents/templates#conversation-history">
    Install this snippet to manage and persist user interactions. The perfect
    starting point for any chatbot or conversational agent.
  </Card>
</CardGroup>

## Agent History & Debugging Mode

Install this snippet to monitor, analyze, and debug your agent's behavior. Gain critical insight into every agent run.

* **Logging Database Tables**: Includes agents and agent\_runs, agent\_steps, agent\_tool\_calls tables to store detailed execution history.
* **Automated Logging Function**: A dedicated function to easily log the inputs, outputs, and steps of each agent run.
* **Monitoring Dashboard**: A utility API endpoint that provides a simple dashboard to review agent performance statistics and debug individual runs.

<Steps>
  <Step title="Install the Snippet" icon="scissors">
    <Card title="Agent History & Debugging Mode" icon="scissors" horizontal href="https://www.xano.com/snippet/LyKzUNP9/" cta="Install Snippet">
      Monitors, analyzes, and debugs your agent’s behavior by logging every run, step, and tool call. Includes a dashboard for performance stats and run details, plus automated logging to capture inputs, outputs, and execution history.
    </Card>
  </Step>

  <Step title="Get the Base URL from the Agent History API group" icon="folder-open">
    Navigate to your APIs from the left-hand menu. Find **Agent History** and click the copy button as shown below.

        <img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/agents-templates-agenthistoryAPIgroup.png?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=5a5575598fbb5aeeea269af8a4edd2bd" alt="Agents Templates Agenthistory AP Igroup Pn" width="1265" height="143" data-path="images/agents-templates-agenthistoryAPIgroup.png" />
  </Step>

  <Step title="Replace the Base URL in the /dashboard API" icon="paste">
    Click on the **Agent History** API group to enter it.

    Click on the \*\*/dashboard \*\*API.

    Click on the first step inside of that function stack, and replace the value with the base URL you copied in the previous step.

        <img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/agents-templates-agenthistoryreplacevariable.png?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=281c56d31d365d26e73d62783f85946a" alt="Agents Templates Agenthistoryreplacevariable Pn" width="2464" height="1157" data-path="images/agents-templates-agenthistoryreplacevariable.png" />
  </Step>

  <Step title="Add a new record to the Agents table" icon="table">
    Navigate to your Database from the left-hand menu.

    Click on the **Agents** table.

    Add a new record with the details of the agent you'd like to monitor using the dashboard.

        <img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/agents-templates-agenthistory-agentstable.png?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=387acebafd38d71a378c17360aabfff0" alt="agents-templates-agenthistory-agentstable.png" width="1194" height="277" data-path="images/agents-templates-agenthistory-agentstable.png" />
  </Step>

  <Step title="Add a new Agents user to the agent_user table" icon="lock">
    We use a separate table for authentication of the agent monitoring dashboard.

    Navigate back to your Database, and click on the **agent\_user** table.

    Add a record. This is what you will use to access the Agent dashboard.

        <img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/agents-templates-agenthistory-agentusertable.png?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=d015a35267d6738725877ae6cce8bc26" alt="agents-templates-agenthistory-agentusertable.png" width="1034" height="223" data-path="images/agents-templates-agenthistory-agentusertable.png" />
  </Step>

  <Step title="Add monitoring to your Agent usage" icon="eye">
    In any function stack where you're calling your agent using the **Call Agent** function, add the new **log\_agent** custom function to capture the agent's response and other run information.

        <img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/agents-templates-agenthistory-customfunction.png?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=4ce9a1a47524e42f8a8db7ea71fa9faa" alt="agents-templates-agenthistory-customfunction.png" width="463" height="83" data-path="images/agents-templates-agenthistory-customfunction.png" />
  </Step>

  <Step title="Access your Agent Monitoring dashboard" icon="window">
    From the /dashboard API, copy the endpoint URL using the button at the top of the page.

    Paste that URL into a new tab.

    Log in using the credentials you stored in the **agent\_user** table.
  </Step>
</Steps>

## Conversation History

<img src="https://mintcdn.com/xano-997cb9ee/GzDS96R__du_4MXp/images/templates-20250826-111349.png?fit=max&auto=format&n=GzDS96R__du_4MXp&q=85&s=f29b356f8adef84637898eb6ef8b637b" alt="An image showing the chatbot provided in this snippet" width="1536" height="880" data-path="images/templates-20250826-111349.png" />

Install this snippet to manage and persist user interactions. It's the perfect starting point for any chatbot or conversational agent.

This snippet includes:

* Authentication endpoints (auth/login and auth/me)
* Database tables (conversations and messages, agent\_user)
* Chatbot API group
* A chatbot UI that you can use to test your agents.\\

**Prerequisites**

* Agent must be configured with prompt type set to "Messages"
* Agent messages value must be set to: `{{ $args.messages|json_encode() }}`

<img src="https://mintcdn.com/xano-997cb9ee/GzDS96R__du_4MXp/images/templates-20250826-111914.png?fit=max&auto=format&n=GzDS96R__du_4MXp&q=85&s=f3768bf7992158a0622bfd63f262d0dd" alt="Setting the prompt type to Messages and the agent messages value" width="1382" height="392" data-path="images/templates-20250826-111914.png" />

<Steps>
  <Step title="Install the Snippet" icon="scissors">
    <Card title="Conversation History" icon="scissors" horizontal href="https://www.xano.com/snippet/rmFsF785" cta="Install Snippet">
      Install this snippet to manage and persist user interactions. It's the perfect starting point for any chatbot or conversational agent.
    </Card>
  </Step>

  <Step title="Get the Base URL from the Chatbot API group" icon="folder-open">
    Navigate to your APIs from the left-hand menu. Find *Chatbot*\* and click the copy button as shown below.

        <img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/agents-templates-agenthistoryAPIgroup.png?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=5a5575598fbb5aeeea269af8a4edd2bd" alt="Agents Templates Agenthistory AP Igroup Pn" width="1265" height="143" data-path="images/agents-templates-agenthistoryAPIgroup.png" />
  </Step>

  <Step title="Replace the Base URL in the /conversation API" icon="paste">
    Click on the **Agent History** API group to enter it.

    Click on the \*\*/dashboard \*\*API.

    Click on the first step inside of that function stack, and replace the value with the base URL you copied in the previous step.

        <img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/agents-templates-agenthistoryreplacevariable.png?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=281c56d31d365d26e73d62783f85946a" alt="Agents Templates Agenthistoryreplacevariable Pn" width="2464" height="1157" data-path="images/agents-templates-agenthistoryreplacevariable.png" />
  </Step>

  <Step title="Call your agent inside of a function stack" icon="table">
    Navigate to your APIs from the left-hand menu.

    Click on the **Conversation** API group, and then select the /conversation API.

    In the group called "Add your Agent statement here", add a Call Agent function, and select your agent from the list

    In step 5, update the **agent\_response** variable to use the Call AI Agent function's output.

        <img src="https://mintcdn.com/xano-997cb9ee/GzDS96R__du_4MXp/images/templates-20250826-114643.png?fit=max&auto=format&n=GzDS96R__du_4MXp&q=85&s=38c4b5703477991688bfa4822696faaa" alt="Modifying your function stack to add agent monitoring" width="1536" height="740" data-path="images/templates-20250826-114643.png" />
  </Step>

  <Step title="Access the Chatbot example and observe conversation history in action" icon="window">
    From the /chatbot API, copy the endpoint URL using the button at the top of the page.

    Paste that URL into a new tab.
  </Step>
</Steps>


Built with [Mintlify](https://mintlify.com).
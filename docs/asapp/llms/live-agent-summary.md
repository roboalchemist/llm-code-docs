# Source: https://docs.asapp.com/agent-desk/digital-agent-desk/live-agent-summary.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Live Agent Summary - GenAgent

> Learn how to receive summaries from GenerativeAgent conversations.

When using GenerativeAgent (GA), conversations may escalate to human agents. **Live Agent Summary** automatically generates concise summaries of these conversations, giving your agents the key context they need without requiring them to read through lengthy chat transcripts.

Live Agent Summary helps improve Average Handling Time (AHT) by generating concise, structured summaries that present key information to agents at handoff. The summary highlights:

* Customer intent
* Key actions taken
* Unresolved issues

<Frame>
  <img src="https://mintcdn.com/asapp/Ve91OvW2QLqQ2_fD/images/messaging-platform/digital-agent-desk/live-agent-summary.png?fit=max&auto=format&n=Ve91OvW2QLqQ2_fD&q=85&s=49c918b3f79b2c698ddf55712951deae" alt="Live Agent Summary Interface" data-og-width="1600" width="1600" data-og-height="958" height="958" data-path="images/messaging-platform/digital-agent-desk/live-agent-summary.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/Ve91OvW2QLqQ2_fD/images/messaging-platform/digital-agent-desk/live-agent-summary.png?w=280&fit=max&auto=format&n=Ve91OvW2QLqQ2_fD&q=85&s=b97feb705af646e40812c3b21973a9c3 280w, https://mintcdn.com/asapp/Ve91OvW2QLqQ2_fD/images/messaging-platform/digital-agent-desk/live-agent-summary.png?w=560&fit=max&auto=format&n=Ve91OvW2QLqQ2_fD&q=85&s=80dee0619c8352496fce236c024ddf00 560w, https://mintcdn.com/asapp/Ve91OvW2QLqQ2_fD/images/messaging-platform/digital-agent-desk/live-agent-summary.png?w=840&fit=max&auto=format&n=Ve91OvW2QLqQ2_fD&q=85&s=135476acb6eda677e539019e3a8d48b9 840w, https://mintcdn.com/asapp/Ve91OvW2QLqQ2_fD/images/messaging-platform/digital-agent-desk/live-agent-summary.png?w=1100&fit=max&auto=format&n=Ve91OvW2QLqQ2_fD&q=85&s=cd35be066d4eee6a429b0e6aae6d91cf 1100w, https://mintcdn.com/asapp/Ve91OvW2QLqQ2_fD/images/messaging-platform/digital-agent-desk/live-agent-summary.png?w=1650&fit=max&auto=format&n=Ve91OvW2QLqQ2_fD&q=85&s=1676401919d345aadd3671f6799c3551 1650w, https://mintcdn.com/asapp/Ve91OvW2QLqQ2_fD/images/messaging-platform/digital-agent-desk/live-agent-summary.png?w=2500&fit=max&auto=format&n=Ve91OvW2QLqQ2_fD&q=85&s=38d5c54784c9ff3998237b7a689e172f 2500w" />
</Frame>

## How Live Agent Summary Works

Live Agent Summary enhances your existing Digital Agent Desk by automatically generating context during escalations:

* **Smart Context Generation**: The system analyzes GA conversations and creates concise summaries when escalations occur
* **Inline Integration**: The system displays summaries directly in the transcript panel with highlight styling, so agents don't need to switch between views
* **Complete Context**: Agents maintain access to all standard transcript information (customer profile, conversation history) plus the generated insights inline
* **Immediate Understanding**: No need to read through entire conversations - the system highlights key information and makes it easily accessible

## Set Up Live Agent Summary

To set up Live Agent Summary, you need to work with ASAPP to enable the feature in your environment and configure the summary generation parameters:

<Steps>
  <Step title="Enable Summaries in Your Environment">
    Contact your ASAPP Implementation Manager to enable GenAgent summaries in your Digital Agent Desk environment.

    This involves configuring the summary generation parameters, setting up handoff trigger conditions, and testing the summary output quality.

    <Note>
      Live Agent Summary requires GenerativeAgent to be configured and operational in your environment.
    </Note>
  </Step>

  <Step title="Validate Summary Output">
    Conduct pilot testing with a small group of agents to validate the effectiveness of summaries:

    * Review summaries with agents to confirm accuracy and usefulness
    * Gather feedback on summary clarity and completeness
    * Adjust summary parameters based on agent input and preferences
  </Step>

  <Step title="Roll Out to Production">
    Once validation is complete, roll out Live Agent Summary to your full agent team:

    * Train agents on how to interpret and use summary information effectively
    * Establish best practices for leveraging summary context in customer interactions
    * Monitor AHT and CSAT metrics to measure improvements and identify optimization opportunities
  </Step>
</Steps>

## Next Steps

After setting up Live Agent Summary, you're ready to improve agent efficiency and enhance customer experience during handoffs.

You may find the following sections helpful in advancing your Digital Agent Desk capabilities:

<CardGroup>
  <Card href="/agent-desk/digital-agent-desk/knowledge-base" title="Knowledge Base">
    Learn how to configure and optimize your knowledge base for better agent support.
  </Card>

  <Card href="/agent-desk/digital-agent-desk/user-management" title="User Management">
    Configure user roles and permissions to optimize agent access and capabilities.
  </Card>

  <Card href="/agent-desk/digital-agent-desk/queues-and-routing" title="Queues and Routing">
    Set up efficient queue management and routing to complement summary capabilities.
  </Card>

  <Card href="/generativeagent" title="GenerativeAgent">
    Learn more about GenerativeAgent capabilities that power Live Agent Summary.
  </Card>
</CardGroup>

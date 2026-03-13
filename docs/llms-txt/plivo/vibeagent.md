# Source: https://plivo.com/docs/aiagent/aistudio/vibeagent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Vibe Agent

> Generate agent flows from natural language — AI-powered flow builder

Vibe Agent is an AI-powered assistant that enables you to create agent flows using simple, natural language descriptions. Whether you're building simple workflows or complex automation, Vibe Agent quickly generates a flow tailored to your use case, saving time while ensuring accuracy.

<Info>
  The vibe agent can quickly get you to a 70% agentic flow. However, for a very effective and production-ready agent, it's recommended to make the refine and perfect the agentic flow manually
</Info>

What You Can Do with Vibe Agent

* Create the first draft of an Agent Flow by describing your use case in simple, clear language.
* Automatically generate all required nodes, paths, and logic based on your input.
* Quickly test, refine, and publish the generated flow—all from one interface.
* Save time by skipping manual setup—Vibe Agent understands context, integrations, and flow logic.

## Building with Vibe Agent

<Steps>
  <Step title="Describe Your Use Case and Launch the Agent">
    * Enter your workflow description in the text box.
    * Be clear and specific about **channels**, **integrations**, and **key values**.
    * Use concise, structured sentences. The clearer and more detailed you are, the better the result.

    <Frame>
            <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/aiagent/images/vibeagent.jpg?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=317b4bc7df245e2e55d8311ea039800b" alt="" width="2880" height="1760" data-path="aiagent/images/vibeagent.jpg" />
    </Frame>
  </Step>

  <Step title="Analyze and Receive a Plan">
    * Vibe Agent analyzes your prompt to assess feasibility.
    * If the task is not feasible, it will **suggest alternatives**.
    * If feasible, it will create a **detailed plan** outlining:
      * Trigger
      * Channel configuration
      * Node settings
      * Edge cases to be covered
      * Call closure criteria and details
    * The plan will serve as a blueprint for your agent flow.

    <Frame>
            <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/aiagent/images/vibeagent2.png?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=9c082187092dd81c6269003bcb34d07e" alt="" width="1844" height="1372" data-path="aiagent/images/vibeagent2.png" />
    </Frame>
  </Step>

  <Step title="Review the Plan">
    * **Review the detailed plan** Vibe Agent provides. It’s critical to ensure all tasks and edge cases are covered.
    * If you find any gaps or missed scenarios, provide feedback and ask for adjustments.
    * **Reviewing the plan properly** is faster and more effective than modifying the flow later.
    * **Clarification questions** may be asked by Vibe Agent before finalizing the plan.

    <Frame>
            <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/aiagent/images/vibeagent3.png?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=759aa7bb33d1815001cc422860767b7e" alt="" width="2760" height="1378" data-path="aiagent/images/vibeagent3.png" />
    </Frame>
  </Step>

  <Step title="Confirm the Plan">
    * Once you confirm that the plan is correct, Vibe Agent will **begin building the agent flow** by adding nodes, configuring each node in the flow and connecting the pathways based on the plan
    * Occasionally, you might need to manually intervene, especially for nodes like **App Actions** and **HTTP** nodes, where authentication or field mapping is required.
  </Step>

  <Step title="Review the flow">
    * **Manual review is required** for each node, even though Vibe Agent automatically generates them. Ensure the node is configured as per your use case.
    * If Vibe Agent pauses or encounters issues during the process, simply **ask it to resume**.

    <Frame>
            <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/aiagent/images/vibeagent4.png?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=9dd496ad79a7de6d873b412cc91cedbf" alt="" width="2202" height="1386" data-path="aiagent/images/vibeagent4.png" />
    </Frame>
  </Step>

  <Step title="Test and Deploy the Agent">
    * Test the agent using the **Playground** to simulate real-world scenarios.
    * Start with simple scenarios and expand gradually to ensure all edge cases are handled.
    * Once satisfied with the flow, **deploy** the agent to your desired channel (e.g., voice, chat, WhatsApp).
  </Step>
</Steps>

Important Note

For use cases where any action needs to be performed on a third-party service (e.g., Zendesk, Hubspot, Notion), make sure you set up the required integration and complete authentication in the Integrations section first.

Vibe Agent cannot handle integration setup or authentication steps.

## Tips for Better Results

* Be Clear: "Send a WhatsApp alert when a new Zendesk ticket is created" works better than vague prompts.
* Mention Integrations: Include the tools you're using (e.g., Hubspot, Google Sheets).
* Define Outcomes: Say what the agent should accomplish—like booking appointments or updating records.

Vibe Agent isn’t just a text-to-flow generator—it’s a collaborative builder that understands the full picture of your automation goals.

# Source: https://docs.unifygtm.com/reference/agents/building-an-agent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unifygtm.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Building an Agent

> Learn the fundamentals of building Agents in Unify.

## Agent configuration

Every Agent has three components:

1. **Record Type**: Specify whether this agent will run on Company records or Person records.
2. **Questions**: Define research questions for the agent to answer.
3. (Optional) **Guidance**: Provide additional context or advice to the agent to improve the results.

Once you've configured your Agent, test it by running it on example Companies or People.

<Frame caption="An empty Agent modal.">
  <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/empty-agent-modal.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=99616e9820e84ac8aec22ee50ecd986c" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/agents/empty-agent-modal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/empty-agent-modal.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=69b80e50f625afbd330c6b2a14873b88 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/empty-agent-modal.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=0f8f2db3383ce2a6588b9ccdba967521 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/empty-agent-modal.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=bfa69ea70d5b84d00b33f2d422e60335 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/empty-agent-modal.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=1f3de99ea6cf98d64fd34e29925dad4a 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/empty-agent-modal.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=48f14d50d7dee050f7ed99838555d3b3 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/empty-agent-modal.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=2a761d0d5d423f6a48128cad800addfd 2500w" />
</Frame>

### Record type

Agents can run on Companies or People. Data from Unify for the underlying records will be made
available to the Agent as it performs research to answer your questions.

For example, an agent intended to perform account qualification will run on company records.
On the other hand, an agent that researches individual people for lead qualification will run on person records.

<Warning>Once you save an Agent, you cannot change its record type.</Warning>

### Questions

Define a set of questions that the Agent will answer for you.
Every question has an expected response type. The available response types are:

* **True / False**
* **Number**
* **Select**

View the [response types documentation](/reference/agents/response-types) for more details and examples.
Try to keep your questions straightforward and concise.
Use a [guidance prompt](#guidance-prompt) to guide define any special
terms or concepts that the Agent should know.

### Guidance prompt

Optionally, you may provide a prompt to help guide your Agent's thought process.
If there is any context the Agent needs to answer your question, this is the place to include it.

In most cases, providing guidance for the Agent is unnecessary.
The Agent already knows that it will be answering questions about a company or person,
so you do not need to include that information in the prompt.

Examples of things to include in a guidance prompt:

* What your company does
* Where to find specific information about the Person or Company to research
* Definitions for specialized terms and concepts

<Tip>
  Unify provides deep customization of and visibility into Agents' thought processes.
  You can take advantage of this to tweak questions or guidance and dial in the accuracy.
</Tip>

## Testing your Agent

Unify gives you best-in-class visibility into an AI's chain-of-thought.
Leverage this to test your Agent, diagnose any issues, and iterate on your
questions and guidance prompts.

Upon providing a valid Agent configuration, an extension will appear and prompt
you to test your Agent. Use the search bar to find a specific Company or Person to test your Agent on,
or use the shuffle button to randomly select a Company or Person. The Agent will run,
explain its reasoning, and provide responses to your questions.

<Tip>
  Generate multiple examples simultaneously to speed up your workflow.
  Navigate through these examples using the arrows at the top of the screen.
</Tip>

<Frame caption="Run the Agent on multiple records concurrently and navigate using the arrows.">
  <video autoPlay muted loop playsInline src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/navigate-agent-examples.mp4?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=5dc6a82150a1c52fbf980dede6513a1a" data-path="images/reference/agents/navigate-agent-examples.mp4" />
</Frame>

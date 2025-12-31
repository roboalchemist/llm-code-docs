# Source: https://docs.asapp.com/generativeagent/human-in-the-loop/approver-mode.md

# Approver Mode

> Learn how human agents review and refine generated responses to ensure safe, accurate, and on-brand customer interactions.

Human-in-the-Loop Agent (HILA) **Approver Mode** is a powerful capability that enables human agents to supervise and refine GenerativeAgent responses in real time before they are delivered to customers. This information is used to **fine-tune GenerativeAgent** over time.

This approach ensures safe, on-brand interactions and accelerates the training of AI systems to sound like your best support agents, making it ideal for piloting new intents and achieving high-quality automated support.

Approver Mode works similarly to regular HILA: GenerativeAgent creates a ticket for a HILA queue, where a HILA can review the ticket. However, instead of providing guidance and information, the HILA approves or modifies GenerativeAgent's messages.

## Set Up Approver Mode

<Steps>
  <Step title="Integrate HILA with your Agent Desk Platform">
    ASAPP offers seamless integration into your existing agent desk through an iframe-based HILA application.

    HILAs operate from dedicated queues within your platform, receiving GenerativeAgent consultation requests directly. This ensures they work within a familiar interface, while you retain full control over routing and assignment.

    <Note>
      To set up HILA in your environment, contact your ASAPP Implementation Manager.
    </Note>
  </Step>

  <Step title="Configure Ticket Assignment and Routing">
    HILAs are assigned tickets based on the routing and assignment configurations in your support platform.

    If no HILA is assigned within the configurable threshold (default: 60 seconds), the case is automatically escalated to a live agent.
  </Step>

  <Step title="Enable Approver Mode">
    Reach out to your ASAPP account team to enable Approver Mode for your account and configure the Administator
  </Step>
</Steps>

<Note>
  HILA in Approver Mode can not be tried out in Previewer.
</Note>

### Administrator Controls

There are several settings that can be configured, particularly to ensure end customers receive quick responses:

* **Auto-accept Timeout:** Responses are automatically approved after a configurable timeout (default: 30 seconds) to ensure the customer remains engaged if the HILA is inactive
* **Agent Assignment Timeout:** If no HILA is assigned within a configurable timeout (default: 60 seconds), the conversation escalates to a live agent
* **Task-level Control:** Define which tasks require complete supervision through Approver Mode
* **Escalation Message:** When HILA initiates an escalation, a configurable message is sent to the customer, informing them that their conversation will be handed over to a live agent

<Warning>
  These safeguards ensure that customers never wait long and always receive a human-verified message.
</Warning>

## Approver Mode Workflow

The Approver Mode workflow follows the same process as regular HILA, with one key difference: instead of providing guidance and information to GenerativeAgent, agents approve or modify the messages that GenerativeAgent has already generated.

<Steps>
  <Step title="Ticket Assignment">
    HILAs are assigned tickets based on the routing and assignment configurations in your support platform. If no HILA is assigned within the configurable threshold (default: 60 seconds), the case is escalated to a live agent automatically.
  </Step>

  <Step title="Ticket Review">
    HILAs are presented with key information to help them answer the GenerativeAgent query:

    <Frame>
      <img src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/hila/ApproverMode.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=e47021fe80c98e638ac7a20bc93cf91e" alt="Approver Mode Interface" data-og-width="2536" width="2536" data-og-height="1582" height="1582" data-path="images/generativeagent/hila/ApproverMode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/hila/ApproverMode.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=9efd782616f5da5388663af800bf240a 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/hila/ApproverMode.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=ae428b01b8525347fea3eceed2766b29 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/hila/ApproverMode.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=b5adbdf482e517a8a65b91d17f4e68fe 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/hila/ApproverMode.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=db98953bbbdd92b5a4d608da1f345e24 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/hila/ApproverMode.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=3d657596785e6e0fb5f89fff10b15012 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/hila/ApproverMode.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=94824f31f0fa8bf6fdf5862fe875450c 2500w" />
    </Frame>

    The HILA application includes:

    * **Transcript:** Complete history of the customer interaction before the ticket was raised
    * **Context:** Summarized view of key customer intents and topics for quick understanding
    * **Customer information:** Details such as customer name and account data if authenticated
    * **Conversation thread:** Real-time view of the approver phase showing all approved messages, edits, and system messages
    * **Assignment timer:** Tracks how long the ticket has been with the assigned HILA
  </Step>

  <Step title="HILA Approval">
    Unlike regular HILA, where agents provide guidance, in Approver Mode, HILA can do one of four things when a GenerativeAgent utterance comes for approval:

    1. **Accept** the utterance as the most appropriate next response to the customer
    2. **Review** the utterance and make necessary changes before sending it to the customer
    3. **Transfer** if the situation requires escalation to a live agent for deeper support
    4. **End** the ticket if the conversation is resolved or GenerativeAgent escalates
  </Step>

  <Step title="GenerativeAgent Continues the Conversation">
    Based on the HILA's action, GenerativeAgent will continue the conversation and reach out to HILA (Approver Mode) for subsequent messages.

    HILA and GenerativeAgent conversations need to be quick since there is a customer waiting for resolution on the other side. To support this, there are **real-time notifications** to ensure that HILA doesn't miss any new messages from GenerativeAgent.
  </Step>
</Steps>

## What Can Be Fine-Tuned?

Using Approver Mode, every agent correction becomes valuable feedback to improve GenerativeAgent over time. Today, we primarily use these edits to align GenerativeAgent's responses with your brand voice and the communication style of your best agents.

Additionally, agent interactions generate insights that inform future improvements, such as:

* **Knowledge Access:** Identify which APIs, knowledge base articles, or system data agents reference, helping refine task instructions
* **Content Gaps & Escalation Patterns:** Spot where agents frequently intervene or escalate, highlighting areas where task instructions or fallback behavior can be improved

<Tip>
  These signals help build toward more confident, autonomous operation over time.
</Tip>

## Next Steps

After setting up Approver Mode, you can enhance your human-in-the-loop capabilities:

<CardGroup cols={2}>
  <Card href="/generativeagent/human-in-the-loop" title="Human-in-the-Loop">
    Learn about the core HILA capabilities and how to incorporate it into your use cases.
  </Card>

  <Card href="/generativeagent/configuring/tasks-and-functions/improving" title="Task and Function Improvements">
    Learn how to improve GenerativeAgent's tasks and functions.
  </Card>

  <Card href="/generativeagent/configuring" title="Configure GenerativeAgent">
    Learn how to configure GenerativeAgent tasks for your use case.
  </Card>

  <Card href="/generativeagent/go-live" title="Go Live">
    Follow steps and best practices to launch your GenerativeAgent deployment in production.
  </Card>
</CardGroup>

# Source: https://dev.writer.com/agent-builder/demo-agent.md

# Agent Builder Demo Application

> Explore the Agent Builder demo agent that analyzes customer reviews and drafts responses. Learn how UI, blueprints, and state variables work together.

<Warning>
  Agent Builder is in beta. Some features are still in development and are subject to change.
</Warning>

When you create a new agent with Agent Builder, it comes with a demo agent that analyzes customer reviews and drafts personalized responses. This walkthrough shows you how the demo agent works and how to modify it to understand Agent Builder's core concepts.

<img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/demo-agent.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=6a0d38372c2d7cff242a3457a46c019a" alt="" data-og-width="3456" width="3456" data-og-height="1814" height="1814" data-path="images/agent-builder/demo-agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/demo-agent.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=1a64409aab0dff73b54117e08f42e455 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/demo-agent.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=cebd1417ee1d0d2afe47aca29f786d9c 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/demo-agent.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=da63201c6ab4ef7c4ec801cdb2733f49 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/demo-agent.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=5109985216f24095fb26a575ec57ec62 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/demo-agent.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=029c2382c84e5255376b1831fa487665 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/demo-agent.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=56a5a0dd544ec6e2956e3185e0d70c6d 2500w" />

This walkthrough covers the following topics:

* How to navigate the Agent Builder interface
* How the UI and blueprint work together through state variables
* How to use the **Classification** block to route workflows
* How to connect blocks using `@{result}`
* How to modify an existing agent to add new behavior

<Tip>
  If you are unfamiliar with Agent Builder, review the [Agent Builder Overview](/agent-builder/overview) to learn more about the different components of an agent.
</Tip>

## Start an Agent Builder project

To create an agent with Agent Builder, log in to [AI Studio](https://app.writer.com/aistudio) and follow these steps:

<Steps>
  <Step title="Click the Build an agent button">
    Click the **Build an agent** button in the top right corner of the page.

        <img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/build-agent-button.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=cc6bdc545119bcd97319a71850cf7d5a" alt="Build an agent button" data-og-width="590" width="590" data-og-height="198" height="198" data-path="images/agent-builder/build-agent-button.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/build-agent-button.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=929c05fa19f02fd96d9c40398950e4bc 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/build-agent-button.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=2fdd754b4a5342b91906b353300ec77c 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/build-agent-button.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=9f9b4bde8acb4e44aaddf6f83a24f00a 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/build-agent-button.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=da1ef54b5c7f7235e5218e063fbaca62 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/build-agent-button.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=b383319378a3e1d8b599bfa21b38efe1 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/build-agent-button.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=2a038c483d5fcd8755c33af77b067631 2500w" />
  </Step>

  <Step title="Create a new agent">
    In the modal that appears, select **New Agent** to create a new agent from scratch.

    <Tip>
      For common use cases, prebuilt agent templates are available. These include both general-purpose and industry-specific options, all customizable to your specific requirements.
    </Tip>

        <img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/get-started-agent-builder.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=035990e1925e3c575f3d4966ae57ea10" alt="Agent creation options" data-og-width="2778" width="2778" data-og-height="1606" height="1606" data-path="images/agent-builder/get-started-agent-builder.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/get-started-agent-builder.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=8fba199fd65a3da92c6909a2eb07d749 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/get-started-agent-builder.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=d909dab372cb2721833f33202b980c6b 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/get-started-agent-builder.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=2b94eb2c112853f0cc6ae11860a58f83 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/get-started-agent-builder.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=e84b5f0849480ded8f8cbd44093b96f3 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/get-started-agent-builder.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=5c0d754d551628ee2b0e732575666716 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/get-started-agent-builder.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=650a29916a2c295f13ac724c8e63b554 2500w" />

    Once the agent is created, a new tab will open in your browser with the Agent Builder interface.
  </Step>

  <Step title="Return to the Agent Builder interface">
    You can get to the Agent Builder interface any time by going to the [AI Studio homepage](https://app.writer.com/aistudio) and selecting the agent you created.

    You'll see the Configure Deployment page when you select the agent. To get to the edit interface, click the **Edit** button in the top right corner.

        <img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/edit-button.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=293915f43f6e0e45aa67b6cfac784403" alt="Edit agent" data-og-width="581" width="581" data-og-height="163" height="163" data-path="images/agent-builder/edit-button.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/edit-button.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=2082b3e16cd438f17b79cd8b26c97944 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/edit-button.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=9338001cc20185c05c8d1e2762f3b8d2 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/edit-button.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=0e78b548c604e91540dc88caf00dc302 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/edit-button.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=d1c3512c824ee46c2a503661e992aa18 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/edit-button.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=8eab76b5bba0baf3efd589fc530833b3 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/edit-button.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=89357ffd387c198c992a2c064ebe0cd9 2500w" />
  </Step>
</Steps>

## Preview the demo agent

Writer initializes the new agent with a demo workflow that you can use to get started. The demo agent takes a customer review and uses a series of tools to analyze the review and draft a response to the customer.

### Agent Builder views

The Agent Builder interface contains four views:
<img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/view-switching.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=f2e6eaf0cce2d5c10b9c2f5cc35c332b" alt="" data-og-width="1048" width="1048" data-og-height="138" height="138" data-path="images/agent-builder/view-switching.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/view-switching.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=1202fb830eeb69c4b6c33c501a958634 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/view-switching.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=736266518a7f896fa552c76f1fe3e1c1 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/view-switching.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=1e76c868c119086e495c36af429e5c47 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/view-switching.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=749ae4255f81531621aa66bd00da0de8 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/view-switching.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=b82945b59cc5f615ac657a3f435fd04f 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/view-switching.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=e2de61db111903896ddb547c66ebecaf 2500w" />

* **Interface**: The agent's UI, where you can edit the agent's appearance.
* **Blueprints**: The agent's blueprint, where you can edit the agent's behavior.
* **Vault**: The agent's secrets, where you can add secrets like API keys or passwords.
* **Preview**: Test the agent's behavior and preview what the user sees.

You can switch between views by clicking the tabs at the top of the page.

### Preview the agent's behavior

Before you start editing, preview the agent to see how it works:

<Steps>
  <Step title="Click the Preview tab">
    Click the **Preview** tab to see the agent in action.
    <img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-preview.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=5518823879655e3523bf3ab475fe4052" alt="" data-og-width="3456" width="3456" data-og-height="1814" height="1814" data-path="images/agent-builder/agent-preview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-preview.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=437f73907e5cd744131f6c14b74bd707 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-preview.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=01074314fb1b6a71e7fd574d742d0c10 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-preview.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=ca0fab4be6d86d534640b816fa489b87 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-preview.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=214dd8c4ba06e62eeb3ac2b04436d2ad 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-preview.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=499b2f5ea52a61a8d51a401181e88b0c 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-preview.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=ed7ea1a98f317f42e0dd36f08c6aaacb 2500w" />
  </Step>

  <Step title="Copy and paste the example customer review">
    Copy the example customer review under **1. Copy Review** and paste it into the **2.Paste Review** text input.
  </Step>

  <Step title="Click Draft response">
    Click **Draft response**. You'll see a status message in the UI that the agent is generating a response. Once the agent has finished, you'll see the response in the UI.
  </Step>

  <Step title="Inspect the agent's blueprint">
    Click the **Blueprints** tab to see the agent's blueprint. You'll see green boxes highlighting the path that the agent took through the blueprint. You'll learn more about the blueprint in the next section.

        <img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-path.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=ae025688c6e18eeb322758556a42f761" alt="" data-og-width="3456" width="3456" data-og-height="1814" height="1814" data-path="images/agent-builder/agent-path.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-path.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=f1da279c5773b0613a51bdbdbf6bff97 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-path.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=32ffae7be0d7a16f5d94d56b81fc48ed 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-path.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=7bab99fc7c9e571df2af0e62f7bf08c6 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-path.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=5028866807576fca11cda037b79c2917 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-path.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=bb1e21a19f69358d107cb4861d0d6208 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-path.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=46347e36c59b35df762f73b1094b4aaf 2500w" />
  </Step>
</Steps>

## Tour of the demo agent architecture

The demo agent consists of an interface and a blueprint. The interface and blueprint are connected through the agent's state and UI triggers.

<img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/demo-agent-architecture.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=35154169be3557ced366471ee8d79f1c" alt="Demo agent blueprint structure showing the flow from UI trigger to text generation" data-og-width="3992" width="3992" data-og-height="1108" height="1108" data-path="images/agent-builder/demo-agent-architecture.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/demo-agent-architecture.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=a71d0176610fd21adec609d68a202725 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/demo-agent-architecture.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=7507b00a3e821ca78b9f3914a50d00a8 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/demo-agent-architecture.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=d9cdc46a4e60a9f4eab76620fe33d647 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/demo-agent-architecture.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=4c2c8100345ef45ccfd25e972c3bee04 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/demo-agent-architecture.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=d20b310c2216ff7eacb0275b018ae977 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/demo-agent-architecture.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=592487bd21fedcd005afea4d51651446 2500w" />

* [**Interface**](#interface-view): What the user sees and interacts with.
* [**Blueprint**](#blueprints-view): A flowchart-like interface where you connect blocks of logic.
* [**Agent state**](#agent-state): A set of values that's shared between the UI and the blueprint. Both the UI and the blueprint can reference and update the state.
* **UI trigger**: A trigger from the UI that starts the agent's blueprint. In this case, the UI trigger is attached to click events on the **Draft response** button.

### Agent state

The [agent's state](/agent-builder/state) is a core component of the agent's behavior. It contains values that the UI and blueprint can access and update.

You can view the agent's state from any view by clicking the **State explorer** icon in the top right of the page.

<img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/state-explorer-icon.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=dc9b3e4865094cbb8ab1c1b016b1393d" alt="" data-og-width="830" width="830" data-og-height="183" height="183" data-path="images/agent-builder/state-explorer-icon.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/state-explorer-icon.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=c879c37cc482564a6d147017903e4783 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/state-explorer-icon.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=3f059d1a8f0aef068d333aab62ac3eee 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/state-explorer-icon.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=9fc574243187e6eddf1fbd838e21c0d8 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/state-explorer-icon.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=b6244e617a09a9b798cedf1d021f946a 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/state-explorer-icon.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=3a2844ff0e041c4880ddb3f7306038b4 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/state-explorer-icon.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=f31a2f62a7a3b151be20e9c1901f1f42 2500w" />

The section [Connecting the UI and the blueprint](#connecting-the-ui-and-the-blueprint) describes how the UI and blueprint interact with the state to perform the agent's tasks.

### Blueprints view

The Blueprints view is where you define the agent's logic and behavior. It's a flowchart-like interface where you connect blocks of logic.

If you previewed the agent, you'll see green boxes highlighting the path that the agent took through the blueprint. For the sample review, the agent takes the following steps:

<img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-path.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=ae025688c6e18eeb322758556a42f761" alt="" data-og-width="3456" width="3456" data-og-height="1814" height="1814" data-path="images/agent-builder/agent-path.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-path.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=f1da279c5773b0613a51bdbdbf6bff97 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-path.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=32ffae7be0d7a16f5d94d56b81fc48ed 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-path.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=7bab99fc7c9e571df2af0e62f7bf08c6 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-path.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=5028866807576fca11cda037b79c2917 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-path.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=bb1e21a19f69358d107cb4861d0d6208 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-path.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=46347e36c59b35df762f73b1094b4aaf 2500w" />

<Steps>
  <Step title="UI Trigger">
    The blueprint started with the **UI Trigger** element. In this case, the UI Trigger is configured to run when the user clicks the **Draft response** button in the UI.
  </Step>

  <Step title="Set state to show the progress message">
    The agent used the **Set state** block to set the `progress_message` value for the agent state to show that it is generating a response.
  </Step>

  <Step title="Classification">
    The agent uses the **Classification** block to analyze the review to determine the primary focus of the review, from the following: `Packaging`, `Pricing`, `Quality`, `Delivery`, or `Empty`.

    The agent determined the review fit into the `Quality` category. Classification blocks are built-in blocks that use a Palmyra model to classify the input based on a set of user-defined categories.
  </Step>

  <Step title="Text generation">
    The agent used the **Text generation** block to have a Palmyra model draft a response to the customer specifically focused on quality.
  </Step>

  <Step title="Set state for the response">
    The agent stored the drafted response using the `@{result}` environment variable so it could use it in the UI.
  </Step>

  <Step title="Set state to clear the progress message">
    The agent cleared the `progress_message` value in the state to remove the loading message from the UI.
  </Step>
</Steps>

#### View another path through the blueprint

To view another path through the blueprint, go back to the **Preview** view and paste the following:

`I like the style but it's a lot more expensive than other brands without any difference in quality.`

Click **Draft response**, and navigate back to the **Blueprint** view. You'll see that the agent took a different path through the blueprint, this time selecting the `Pricing` category and drafting a response using a pricing-related prompt.

### Interface view

The Interface view is where you define the agent's appearance. You build the interface with components that you can customize and reference in the blueprint.

This agent's UI has the following components:

* A welcome image in a sidebar
* A section for the review:
  * A **Text area Input** for the customer review
  * A button to **Draft response**
* A section for the response:
  * A **Message** component to display the in progress status message
  * A section with **Text** components to display the response

The Interface uses **Column container** components to layout the Review section in a two-column format.

<img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-ui.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=6ac3c04756349ac695633f34f1c617d6" alt="" data-og-width="3456" width="3456" data-og-height="1812" height="1812" data-path="images/agent-builder/agent-ui.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-ui.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=f62260322574ce3824950d2492891045 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-ui.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=9ab00f13da9423be5cc3bf86650bf1eb 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-ui.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=f5ab0d5a3e9359de457ef917288f68f2 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-ui.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=f39d0274fd6c55b3b7a059c3595b786d 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-ui.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=404b163258203cab853e53cd2891b596 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-ui.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=a780de261e5be94f4466c1c7987d73a3 2500w" />

#### Hidden sections

You won't see the hidden section for the results in the UI when you first load the agent. You can see that the section is in the UI from the **Interface Layers** view, which shows all the components in the UI. The hidden section has an icon next to it indicating that it's not visible.

<img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/hidden-components.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=f7dd2e3509d7dd19fbe1b90b6f18b30f" alt="" data-og-width="424" width="424" data-og-height="116" height="116" data-path="images/agent-builder/hidden-components.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/hidden-components.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=fb369ba90ed96062983f609fdb5ff280 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/hidden-components.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=59f5caacba229d31590f19a8abe47823 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/hidden-components.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=26d9651d45d27e0e7ef15da254fa4754 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/hidden-components.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=80086c82dd0d8108fce7272abfef417b 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/hidden-components.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=c8bd17c0d1cb843b817809c163358b85 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/hidden-components.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=84a928a1ca238ce29e25771cabcd4abf 2500w" />

Click that element in the Component tree to see its settings. Under **Visibility**, it's set to only show up once there is a value in the `review_response` state variable.

<img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/review-response-visibility.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=ed68e3df92d501351b8369ce65e27b5b" alt="" data-og-width="752" width="752" data-og-height="258" height="258" data-path="images/agent-builder/review-response-visibility.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/review-response-visibility.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=acf0626e4bd876be1c93d34dc5bc0f93 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/review-response-visibility.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=a37b5ab1fc0595a860f1cc8a64ecffab 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/review-response-visibility.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=f48f6ab4f4f84f255874373599356710 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/review-response-visibility.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=a3ef016784ad453b170f21974ce9b520 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/review-response-visibility.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=5375d6a9fa837ecfdefa31a449d10834 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/review-response-visibility.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=358ca51a608cc731f03c872a6b057504 2500w" />

### Connecting the UI and the blueprint with state variables

To build full-featured agents, you must be able to connect the UI to the blueprint.

The agent's state is the main way to pass data between the UI and the blueprint. The state contains a set of values that the UI and blueprint can both reference and set. You can also use triggers to connect the UI to the blueprint.

Here are the places where the demo agent connects the UI to the blueprint and passes data between them:

<Steps>
  <Step title="UI Trigger">
    The **Draft response** button in the UI is connected to the **UI Trigger** element in the blueprint. Click events trigger the blueprint to run.
  </Step>

  <Step title="Customer review input">
    The **Text area Input** component in the UI binds the user's input to the `customer_review` state variable. The blueprint uses this value in the **Classification** block.
  </Step>

  <Step title="Progress message">
    The **Message** component in the UI displays the value of the `progress_message` state variable to the user. The blueprint sets this value after the user clicks **Generate response**.
  </Step>

  <Step title="Review response">
    The two sections in the response with **Text** components in the UI depend on the value of the `review_response` state variable.

    1. The blueprint sets this value after the **Text generation** block runs.
    2. Once `review_response` contains a value, the section that had the message "The response will be shown here" disappears.
    3. The section that displays the response appears. The text area in that section contains the value of `review_response`.

    See [Hidden sections](#hidden-sections) for more information about the review response sections and conditionally showing and hiding them.
  </Step>

  <Step title="Clear progress message">
    Once the review response is generated, the final **Set state** block in the blueprint sets the `progress_message` state variable to an empty string to clear the loading message from the UI.
  </Step>
</Steps>

### Passing data between blocks

The demo agent also shows how to pass data between blocks with the `@{result}` variable. Once the text generation block has finished, it passes its result to the next block in the blueprint, which is the **Set state** block. The **Set state** block sets the `review_response` state variable with the `@{result}` from the text generation block.

Learn more about all available variables in [Using Data from Previous Blocks](/agent-builder/execution-environment).

## Modify the demo agent

Now that you've toured the Agent Builder interface, try editing the agent's behavior.

### Add a new category to the classification block

This example shows how to add a new category to the classification block to look for and respond to reviews that focus on sizing issues.

First, add another category to the **Classification** block in the blueprint so that the agent can also classify reviews that are about sizing.

<Steps>
  <Step title="Open the Classification block">
    Navigate to the **Blueprints** view and click the **Classification** block in the blueprint to open the block settings.
  </Step>

  <Step title="Add a new category">
    In the **Categories** section, add a new category called `Sizing` with the value:

    ```
    The review relates to sizing issues or satisfaction with sizing.
    ```

        <img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-category.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=ed7994ab24346faecf62107cdbcb4c2f" alt="" data-og-width="1850" width="1850" data-og-height="1144" height="1144" data-path="images/agent-builder/add-category.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-category.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=c4ed5f3c1d9d2055aec2279fc91e88d3 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-category.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=5db2a0555d6f7de60cc0510904a890b8 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-category.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=1cfdb455ec4046e88a06fe9a45ced12b 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-category.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=c16cd4b5850a87ec43ee39232ad8f246 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-category.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=b58e3900d056c79cfa5728efdf883374 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-category.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=d0e426890f0590c120ad5e258c6ef696 2500w" />
  </Step>

  <Step title="Add a new text generation block">
    Add a new **Text generation** block to the blueprint to generate a response to sizing-related reviews:

    1. Click one of the existing **Text generation** blocks in the blueprint.
    2. Type `Command + c` (on Mac) or `Ctrl + c` (on Windows) to copy the block.
    3. Click onto the blueprint canvas and type `Command + v` (on Mac) or `Ctrl + v` (on Windows) to paste the block.
  </Step>

  <Step title="Edit the new text generation block">
    Click on the new text generation block you pasted to edit it. Update the following settings:

    * **Alias**: `Draft sizing response`
    * **Prompt**: update the prompt to focus on sizing issues:

    ```
    Take the role of a customer success rep and draft an email response to the customer review below that mentions sizing: @{customer_review}

    Address the customer's sizing experience. Thank them if the sizing was accurate, or address their concerns if there were problems with sizing.
    ```
  </Step>

  <Step title="Connect the new text generation block to the rest of the blueprint">
    Connect the new text generation block to the rest of the blueprint:

    * Drag a line from the purple dot next to **Sizing** on the **Classification** block to connect it to the new **Text generation** block.
    * Drag a line from the **Success** connection point on the **Text generation** block to the **Set state** block.

        <img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/new-sizing-path.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=a80a3def505f72b0e80230449b320bdf" alt="" data-og-width="3456" width="3456" data-og-height="1808" height="1808" data-path="images/agent-builder/new-sizing-path.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/new-sizing-path.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=dfbf1b27d91598b67ad0c1c0a60106fc 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/new-sizing-path.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=ca0a0e99c4687e550c769677e23394f5 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/new-sizing-path.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=73741a3ce5237d3e86b85e8e1c00ac04 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/new-sizing-path.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=10432091589beebff04008f75e62d6f2 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/new-sizing-path.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=0bc199abb051b8d866156e3a0c3b480c 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/new-sizing-path.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=913e73ded2139dff74ed52869892b37e 2500w" />
  </Step>
</Steps>

Now, preview the agent to see the new behavior. Paste the following review into the input field and click **Draft response**:

```
The sizing felt off, I'm normally a small and even the XS was too big.
```

You should see the agent take a different path through the blueprint and generate a sizing-related response.

### Add a new UI component

This next example shows how to add a new UI component that you can incorporate into the agent's blueprint.

The steps show how to prompt the agent to add a discount of a certain percentage when generating a response to the customer review. You will:

* Add a **Select input** component to the UI that lists different discount percentages
* Edit the prompt for one of the **Text generation** blocks to add the selected discount percentage to the response if there is one

**From the UI view:**

<Steps>
  <Step title="Add a new Select input component">
    Add a new **Select input** component to the UI. Drag it into the section that contains the area for pasting the review text and the **Draft response** button.

    Update the following settings in the Select input component's settings:

    * **Label**: `Discount %`
    * **Options**: `0`, `5`, `10`, `15` (the keys and values should be the same)
    * **Link variable** under **Binding**: `discount`
  </Step>

  <Step title="Move the component above the Draft response button">
    Move the component above the **Draft response** button by clicking the three vertical dots on the component's settings menu and selecting **Move up**. You can also drag the component up in the UI.

        <img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/move-component-up.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=986d926c6f5916133530919c192e6f27" alt="" data-og-width="678" width="678" data-og-height="278" height="278" data-path="images/agent-builder/move-component-up.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/move-component-up.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=ac1fde8e5244b79dd3582939d274b4ff 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/move-component-up.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=1cd6156eee19510b5e6aec7b5cfacb94 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/move-component-up.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=3b5fdce7d4019e53b903b2236621d46f 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/move-component-up.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=c4e7088359349cb25138ef11af418ce4 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/move-component-up.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=4bd79e769ef5ca8a3382d2f69e3d7ea6 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/move-component-up.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=f82ca631a8b70efa14a39c501b76d449 2500w" />

    The UI should now look like this:
    <img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dropdown-input-settings.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=44782af75624ccd310c9d2c0b80fc271" alt="" data-og-width="3456" width="3456" data-og-height="1808" height="1808" data-path="images/agent-builder/dropdown-input-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dropdown-input-settings.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=dc385bfa33f0db5cc40855a67b5002fd 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dropdown-input-settings.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=b371a8784a4e329e5f3c744e90c0e542 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dropdown-input-settings.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=9138ca7a609e756c2ec3e142a17515df 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dropdown-input-settings.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=403fcb2906f65986fafc17c5bc05e14a 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dropdown-input-settings.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=a12bc9bfe6b25244751245aa157aacbf 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dropdown-input-settings.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=6ffa239d7e4d44a443be23c46c34ffa1 2500w" />
  </Step>
</Steps>

**From the blueprint view:**

<Steps>
  <Step title="Edit the Draft packaging response text generation block">
    Click the **Draft packaging response** text generation block to open its settings.

    Edit the block's prompt to read the `discount` state variable and add a discount to the response if there is one. For example, add the following to the prompt:

    ```
    Offer a discount of @{discount} percent on their next purchase.

    Do not offer a discount if the value of @{discount} is 0.
    ```

        <img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-discount.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=fdae7550de665470de4d5d80fe72b268" alt="" data-og-width="3456" width="3456" data-og-height="1804" height="1804" data-path="images/agent-builder/add-discount.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-discount.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=5ded7ee088cfffabd6f30c3ce479dd65 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-discount.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=e036132034baf5f18dae55720618ffd0 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-discount.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=e3cd7f7cfa0bac951c77bb726ee589c4 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-discount.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=0e11018fa261f21cf5f2bed0633ed26d 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-discount.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=653cc8d1c4119d69df2c0fab3fdf9541 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-discount.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=4ecea2dee901b329ba9f8745b6da2a14 2500w" />
  </Step>
</Steps>

Now, preview the agent to see the new behavior. Paste the following review into the input field:

```
The packaging was awful.
```

Then, choose a discount amount from the select input and click **Draft response**.

You should see the agent take a different path through the blueprint and generate a response that offers a discount if you set it above 0.

You can update the prompts for the other text generation blocks to have the agent offer a discount for the other categories.

## Next steps

Now that you've interacted with and modified an agent in Agent Builder, you can build your own. Check out the [Agent Builder Quickstart](/agent-builder/quickstart) to learn how to build a new agent from scratch.

<feedback />

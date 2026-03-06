# Source: https://io.net/docs/guides/intelligence/agentic-workflow.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Agentic Workflow Editor

> Build, connect, and execute powerful AI workflows using a visual, no-code interface. From simple task chains to full-blown multi-agent orchestration - without writing a single line of code.

## What is Agentic Workflow?

**Agentic Workflow Editor** is a visual builder that lets you create and manage AI workflows composed of models, agents, tools, and task logic — like a modular intelligence engine.

Instead of scripting interactions between various models or APIs, you can drag components onto a canvas, configure them, connect them visually, and run the flow to see the outcome — all from your browser.

### Who is this for?

* **AI Engineers & Researchers** – Quickly prototype multi-agent systems
* **Data Scientists & Analysts** – Automate complex logic chains without coding
* **Product / Ops Teams** – Connect AI models to business logic visually
* **Consultants & Agencies** – Package workflows as reusable templates

## Getting Started

To begin using the Agentic Workflow Editor :

1. **Go to your io.net Dashboard.**
2. Navigate to the [**Agentic Workflow Editor**](https://id.io.net/ai/agentic-workflow-editor) under **IO Intelligence** section.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8bd89ada3ee0343160527832b53ea3a26e84268fa63c2b463a4e6ea1ba98d4d5-AFW-1.jpg?fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=377af89fe869060b6f9347885f9a97b3" alt="" className="mx-auto" style={{ width:"76%" }} data-og-width="2448" width="2448" data-og-height="480" height="480" data-path="images/docs/8bd89ada3ee0343160527832b53ea3a26e84268fa63c2b463a4e6ea1ba98d4d5-AFW-1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8bd89ada3ee0343160527832b53ea3a26e84268fa63c2b463a4e6ea1ba98d4d5-AFW-1.jpg?w=280&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=c14d325e24f9ba40b93785605afb356d 280w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8bd89ada3ee0343160527832b53ea3a26e84268fa63c2b463a4e6ea1ba98d4d5-AFW-1.jpg?w=560&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=fcdde5fddb812eef46174cc161535766 560w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8bd89ada3ee0343160527832b53ea3a26e84268fa63c2b463a4e6ea1ba98d4d5-AFW-1.jpg?w=840&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=40f20f19fc983abae573e4ce1cf43e4b 840w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8bd89ada3ee0343160527832b53ea3a26e84268fa63c2b463a4e6ea1ba98d4d5-AFW-1.jpg?w=1100&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=d6bee1222fd14542cf8c51095fc725c0 1100w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8bd89ada3ee0343160527832b53ea3a26e84268fa63c2b463a4e6ea1ba98d4d5-AFW-1.jpg?w=1650&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=f9072d6b386df49658e7c3dce582e660 1650w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8bd89ada3ee0343160527832b53ea3a26e84268fa63c2b463a4e6ea1ba98d4d5-AFW-1.jpg?w=2500&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=d4b3c821a6d4c32e0d6fb2038c0c3c7b 2500w" />
</Frame>

3. Create a new workflow and start interacting with AI models.

### Interface Overview

| Section           | Description                                             |
| ----------------- | ------------------------------------------------------- |
| **Left Sidebar**  | Workflows list: folders, create new flow, rename/delete |
| **Center Editor** | Visual flow builder: drag & drop components             |
| **Right Sidebar** | Settings for selected components                        |
| **Bottom Panel**  | Flow Outcome result: logs and execution steps           |

## Import your flow before starting:

* Click **Import From YAML** button when you just created new flow in the center of the flow editor

  <Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/12bcdad467779bd3a3a3f4cac1b75161a47188df7d18f934008110e6746561a8-Artboard.jpg?fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=b235042b66d41941d1231e8591233caf" alt="" className="mx-auto" style={{ width:"55%" }} data-og-width="662" width="662" data-og-height="484" height="484" data-path="images/docs/12bcdad467779bd3a3a3f4cac1b75161a47188df7d18f934008110e6746561a8-Artboard.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/12bcdad467779bd3a3a3f4cac1b75161a47188df7d18f934008110e6746561a8-Artboard.jpg?w=280&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=b71d957b60e4afd915811eadb2b6aaa7 280w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/12bcdad467779bd3a3a3f4cac1b75161a47188df7d18f934008110e6746561a8-Artboard.jpg?w=560&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=11d8883a0c266abad51c8b2b8804ef68 560w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/12bcdad467779bd3a3a3f4cac1b75161a47188df7d18f934008110e6746561a8-Artboard.jpg?w=840&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=fdd97cbf25e8d4791f1c1c6e91fc7882 840w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/12bcdad467779bd3a3a3f4cac1b75161a47188df7d18f934008110e6746561a8-Artboard.jpg?w=1100&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=67e0a5844547b67e36c0eb5f46fbf568 1100w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/12bcdad467779bd3a3a3f4cac1b75161a47188df7d18f934008110e6746561a8-Artboard.jpg?w=1650&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=0d08fcea5c3d3deb90e8879d35b8b78c 1650w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/12bcdad467779bd3a3a3f4cac1b75161a47188df7d18f934008110e6746561a8-Artboard.jpg?w=2500&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=a763f76f48f29c7f3e47325977f471ef 2500w" />
  </Frame>
* Upload `.yaml` file (max 1MB)
* Click **Generate Flow**

  <Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0d5c4eb8771956ce49db919e89ef2d08bba4fe3b2388d79bd8f74beccfc4260e-Artboard3.jpeg?fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=e1ab674d35f490a66d563d5dc3afb03e" alt="" className="mx-auto" style={{ width:"66%" }} data-og-width="1042" width="1042" data-og-height="656" height="656" data-path="images/docs/0d5c4eb8771956ce49db919e89ef2d08bba4fe3b2388d79bd8f74beccfc4260e-Artboard3.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0d5c4eb8771956ce49db919e89ef2d08bba4fe3b2388d79bd8f74beccfc4260e-Artboard3.jpeg?w=280&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=2d60db7c0ae9c6aa5086a6c1ab53bf30 280w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0d5c4eb8771956ce49db919e89ef2d08bba4fe3b2388d79bd8f74beccfc4260e-Artboard3.jpeg?w=560&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=1b962dc80bcb60eb11066d54a500709e 560w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0d5c4eb8771956ce49db919e89ef2d08bba4fe3b2388d79bd8f74beccfc4260e-Artboard3.jpeg?w=840&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=1dd06072fe0545e116724958bcaf0d49 840w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0d5c4eb8771956ce49db919e89ef2d08bba4fe3b2388d79bd8f74beccfc4260e-Artboard3.jpeg?w=1100&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=c44a9475316cbded9975a5e4e3237c98 1100w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0d5c4eb8771956ce49db919e89ef2d08bba4fe3b2388d79bd8f74beccfc4260e-Artboard3.jpeg?w=1650&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=94c2acb9fac391dea39f1092bc225834 1650w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0d5c4eb8771956ce49db919e89ef2d08bba4fe3b2388d79bd8f74beccfc4260e-Artboard3.jpeg?w=2500&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=3891d5e9c364b2f24d8798088f2f3384 2500w" />
  </Frame>

## How the flow working

To design an effective agentic workflow, we recommend the following order:

### 1. Create an Agent

Start by adding an Agent component to represent your core logic and behavior. In the right sidebar, configure: `Agent Name`, `Instructions` (what it should do), `Swarm Name `(for group coordination if applicable)

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/30edbb4345858afb1ecf950a90376b52d1e18ac3f315b346b55ae35888acfbb0-AFW-7.jpg?fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=b3d4b831c95d0104adfca420bc14ea92" alt="" className="mx-auto" style={{ width:"46%" }} data-og-width="572" width="572" data-og-height="826" height="826" data-path="images/docs/30edbb4345858afb1ecf950a90376b52d1e18ac3f315b346b55ae35888acfbb0-AFW-7.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/30edbb4345858afb1ecf950a90376b52d1e18ac3f315b346b55ae35888acfbb0-AFW-7.jpg?w=280&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=37ae601c448db6c1d0d3d73368bc16c6 280w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/30edbb4345858afb1ecf950a90376b52d1e18ac3f315b346b55ae35888acfbb0-AFW-7.jpg?w=560&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=da57bcf468ad2641a4f075a5f958b30e 560w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/30edbb4345858afb1ecf950a90376b52d1e18ac3f315b346b55ae35888acfbb0-AFW-7.jpg?w=840&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=5f6a3922261366ccdab4781ce9cd4b58 840w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/30edbb4345858afb1ecf950a90376b52d1e18ac3f315b346b55ae35888acfbb0-AFW-7.jpg?w=1100&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=47e0c9c7fb4329bec9fb753561baabfc 1100w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/30edbb4345858afb1ecf950a90376b52d1e18ac3f315b346b55ae35888acfbb0-AFW-7.jpg?w=1650&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=e5028c8aba32e6dfcdcadd9fbe0ab3e0 1650w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/30edbb4345858afb1ecf950a90376b52d1e18ac3f315b346b55ae35888acfbb0-AFW-7.jpg?w=2500&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=97a47024c729847b9529e332d4e640ab 2500w" />
</Frame>

<Warning>
  First, insert an Agent component. Then connect it to a Model, followed by Tasks or Tools.
</Warning>

### 2. Pick an AI Model

Attach an AI Model to the Agent by clicking into the component and choosing from the available models in the right sidebar. This defines the core reasoning engine your agent will use.

1. Click **Add Component** → Select **AI Model**
2. Select the Component block → use right sidebar to:

   * Search and select an AI model
   * Click **Save**

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/403d89dd39ff32b32c650752cf39315fb12b192ab97e925df020b539b13fe4d5-AFW-3.jpg?fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=f819b7aa92035f2cfd8b700298286205" alt="" className="mx-auto" style={{ width:"76%" }} data-og-width="1350" width="1350" data-og-height="1458" height="1458" data-path="images/docs/403d89dd39ff32b32c650752cf39315fb12b192ab97e925df020b539b13fe4d5-AFW-3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/403d89dd39ff32b32c650752cf39315fb12b192ab97e925df020b539b13fe4d5-AFW-3.jpg?w=280&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=e69ec96a58b9bd6cfa7bf770f933d3cb 280w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/403d89dd39ff32b32c650752cf39315fb12b192ab97e925df020b539b13fe4d5-AFW-3.jpg?w=560&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=68c788a674c9876b47201444ba7954ba 560w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/403d89dd39ff32b32c650752cf39315fb12b192ab97e925df020b539b13fe4d5-AFW-3.jpg?w=840&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=d1abff946a6c9c1f522f33a6ae50ad3e 840w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/403d89dd39ff32b32c650752cf39315fb12b192ab97e925df020b539b13fe4d5-AFW-3.jpg?w=1100&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=776d348b5dd7c8bb7da85904b58cbd28 1100w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/403d89dd39ff32b32c650752cf39315fb12b192ab97e925df020b539b13fe4d5-AFW-3.jpg?w=1650&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=60894f238f3ebc864814dd359c3f37e5 1650w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/403d89dd39ff32b32c650752cf39315fb12b192ab97e925df020b539b13fe4d5-AFW-3.jpg?w=2500&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=6023f36a35538fd1d8e14e5a7e79da2b 2500w" />
   </Frame>
3. The block updates with the model name

### 3. Define Tasks

Add Task components for specific steps your Agent will perform. Configure each task with: `Task ID`, `Name`, `Text`, `Client Mode (on/off)`

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5e275657c27e6e04000163741885596d014b515e5c49b1c2213b810513377461-AFW-8.jpg?fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=16c7cdda95fb746f3b147374194e85b3" alt="" className="mx-auto" style={{ width:"44%" }} data-og-width="562" width="562" data-og-height="982" height="982" data-path="images/docs/5e275657c27e6e04000163741885596d014b515e5c49b1c2213b810513377461-AFW-8.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5e275657c27e6e04000163741885596d014b515e5c49b1c2213b810513377461-AFW-8.jpg?w=280&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=12547ba2b97190a328f2cab0a0c581ca 280w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5e275657c27e6e04000163741885596d014b515e5c49b1c2213b810513377461-AFW-8.jpg?w=560&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=20fd812ebb0d0f59dee701ab3c3f0162 560w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5e275657c27e6e04000163741885596d014b515e5c49b1c2213b810513377461-AFW-8.jpg?w=840&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=a4cb25b6a20cdc6ec2dc522212de2402 840w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5e275657c27e6e04000163741885596d014b515e5c49b1c2213b810513377461-AFW-8.jpg?w=1100&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=c32bf5a566685c402874a616882b3393 1100w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5e275657c27e6e04000163741885596d014b515e5c49b1c2213b810513377461-AFW-8.jpg?w=1650&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=31a4111f8540ced6fe3580340d94d753 1650w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5e275657c27e6e04000163741885596d014b515e5c49b1c2213b810513377461-AFW-8.jpg?w=2500&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=efb208b7851f2e0af48e0b81d0a99d28 2500w" />
</Frame>

### 4. Connect Tools

Use Tool components to integrate external capabilities — such as RAG search, cryptocurrency data, or web search. Tools allow **Agents** or **Tasks** to interact with these systems.

To use a Tool:

* Add the **Tool** component to your flow.
* Select one from the built-in list — no manual configuration is required.

| Tool Name                    | Description                                                             |
| ---------------------------- | ----------------------------------------------------------------------- |
| `r2r.list documents`         | Lists documents with pagination.                                        |
| `r2r.rag search`             | Performs a Retrieval-Augmented Generation (RAG) search.                 |
| `listing coins`              | Retrieves a paginated list of active cryptocurrencies.                  |
| `get coin info`              | Returns coin metadata like logo, description, links, and documentation. |
| `get coin quotes`            | Provides real-time price quotes for cryptocurrencies.                   |
| `get coin quotes historical` | Returns historical price quotes.                                        |
| `search the web`             | Performs a web search. Requires `text` input.                           |
| `search the web async`       | Performs a web search asynchronously. Requires `text` input.            |

<Info>
  Note: When connecting components, remember — arrow always points from Agent or Task → Tool. Tools never initiate.
</Info>

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/19aa01d29c0c4fee1049b44dd46dab134da9aec9281a7af4da0fac3a0a0f2ee1-AFW-9.jpg?fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=4d04327d176a66a762993c92dd41b932" alt="" className="mx-auto" style={{ width:"39%" }} data-og-width="578" width="578" data-og-height="1220" height="1220" data-path="images/docs/19aa01d29c0c4fee1049b44dd46dab134da9aec9281a7af4da0fac3a0a0f2ee1-AFW-9.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/19aa01d29c0c4fee1049b44dd46dab134da9aec9281a7af4da0fac3a0a0f2ee1-AFW-9.jpg?w=280&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=9d32827a1d3c49a57cee3b72901a0f7e 280w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/19aa01d29c0c4fee1049b44dd46dab134da9aec9281a7af4da0fac3a0a0f2ee1-AFW-9.jpg?w=560&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=c3d130d20f3a62a149af37fc5a38cb32 560w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/19aa01d29c0c4fee1049b44dd46dab134da9aec9281a7af4da0fac3a0a0f2ee1-AFW-9.jpg?w=840&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=202b57a787b8078ee4b7453e8b9a3187 840w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/19aa01d29c0c4fee1049b44dd46dab134da9aec9281a7af4da0fac3a0a0f2ee1-AFW-9.jpg?w=1100&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=8f62360f64cbb3a114b56a08948ecc20 1100w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/19aa01d29c0c4fee1049b44dd46dab134da9aec9281a7af4da0fac3a0a0f2ee1-AFW-9.jpg?w=1650&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=06d11af229c92ddd1110d1a751095b18 1650w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/19aa01d29c0c4fee1049b44dd46dab134da9aec9281a7af4da0fac3a0a0f2ee1-AFW-9.jpg?w=2500&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=8c140858d2f0baea5904fbfa89c9d5f7 2500w" />
</Frame>

### 5. Add Stages (Optional)

Add Stage components to organize your workflow into sequential or parallel stages, each with defined objectives and context. Configure each Stage with: `Type`, `Objective`, `Result Type`, `Context`

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8e99b2e453e4346c015613084865cf33d9f936cb58fe07bd157e20c1ce9aa75a-AFW-10.jpg?fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=b4828b1f03456d83aababba0c75a9163" alt="" className="mx-auto" style={{ width:"50%" }} data-og-width="590" width="590" data-og-height="1014" height="1014" data-path="images/docs/8e99b2e453e4346c015613084865cf33d9f936cb58fe07bd157e20c1ce9aa75a-AFW-10.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8e99b2e453e4346c015613084865cf33d9f936cb58fe07bd157e20c1ce9aa75a-AFW-10.jpg?w=280&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=7a497ce7d39c6ae22b88f5fa2acba8c7 280w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8e99b2e453e4346c015613084865cf33d9f936cb58fe07bd157e20c1ce9aa75a-AFW-10.jpg?w=560&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=5bc4619dfc8f9cc24f6a2ca6435938b1 560w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8e99b2e453e4346c015613084865cf33d9f936cb58fe07bd157e20c1ce9aa75a-AFW-10.jpg?w=840&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=3ff2835e0b88b66cbc79d94d1002e1e4 840w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8e99b2e453e4346c015613084865cf33d9f936cb58fe07bd157e20c1ce9aa75a-AFW-10.jpg?w=1100&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=275f2fdb8b797e42fb7a1558464f68b5 1100w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8e99b2e453e4346c015613084865cf33d9f936cb58fe07bd157e20c1ce9aa75a-AFW-10.jpg?w=1650&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=f9cc12c9c8a5f0f9b31ac1be5c2252cc 1650w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8e99b2e453e4346c015613084865cf33d9f936cb58fe07bd157e20c1ce9aa75a-AFW-10.jpg?w=2500&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=62e7d31c97e9b1fecc3640c30e7314f0 2500w" />
</Frame>

### 6. Connect Everything

In the Agentic Workflow Editor, components are connected to define how data and logic flow between them.

* **Agents** and **Tasks** are active components — they **initiate** actions.
* **Tools** and **Models** are passive — they are **called** by Agents or Tasks.

#### Valid Connection Examples:

* Agent → Tool
* Agent → Model
* Task → Tool

#### Invalid:

* Tool → Agent
* Tool → Task

<Info>
  Tools don’t initiate logic — they return results when triggered by another component.
</Info>

**To create a connection:** Drag from the top-right circle of one block to another. This sets execution order and data flow

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/081f4fee39c6cf3694d865314e6a9ffe774687164ce4f58eb955a7a78d7836af-Group_20.jpg?fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=384d02ce4a7f534db11d92b9a706151c" alt="" className="mx-auto" style={{ width:"62%" }} data-og-width="882" width="882" data-og-height="770" height="770" data-path="images/docs/081f4fee39c6cf3694d865314e6a9ffe774687164ce4f58eb955a7a78d7836af-Group_20.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/081f4fee39c6cf3694d865314e6a9ffe774687164ce4f58eb955a7a78d7836af-Group_20.jpg?w=280&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=3e3600b15682548f0c608759f17a4299 280w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/081f4fee39c6cf3694d865314e6a9ffe774687164ce4f58eb955a7a78d7836af-Group_20.jpg?w=560&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=e11724d388203dfe97ccc6bf3dbc9b00 560w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/081f4fee39c6cf3694d865314e6a9ffe774687164ce4f58eb955a7a78d7836af-Group_20.jpg?w=840&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=8310ba7e0542a99331fb74cb2dd29fc8 840w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/081f4fee39c6cf3694d865314e6a9ffe774687164ce4f58eb955a7a78d7836af-Group_20.jpg?w=1100&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=1fa670c7b30c502f268f150f771e9662 1100w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/081f4fee39c6cf3694d865314e6a9ffe774687164ce4f58eb955a7a78d7836af-Group_20.jpg?w=1650&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=00691c890e12511da5b09d93dda9b70a 1650w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/081f4fee39c6cf3694d865314e6a9ffe774687164ce4f58eb955a7a78d7836af-Group_20.jpg?w=2500&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=b6cc82d8942ba91cb1860985dad5d129 2500w" />
</Frame>

**To remove a connection**: Hover over the connecting line, then click the cross icon to remove it.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c21c8645c4654b9cef7e248900cbaa382d8064527e66f66b1ce130ba0ab97f31-Group_21.jpg?fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=12728456ffee5f3dd10064fd0ee0ce0f" alt="" className="mx-auto" style={{ width:"52%" }} data-og-width="880" width="880" data-og-height="790" height="790" data-path="images/docs/c21c8645c4654b9cef7e248900cbaa382d8064527e66f66b1ce130ba0ab97f31-Group_21.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c21c8645c4654b9cef7e248900cbaa382d8064527e66f66b1ce130ba0ab97f31-Group_21.jpg?w=280&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=6b1b0f675d4c4c37254545a7552c4ac0 280w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c21c8645c4654b9cef7e248900cbaa382d8064527e66f66b1ce130ba0ab97f31-Group_21.jpg?w=560&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=bbf46c9d8b74f3eb1d0cb0aa0448f402 560w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c21c8645c4654b9cef7e248900cbaa382d8064527e66f66b1ce130ba0ab97f31-Group_21.jpg?w=840&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=d97776f0f0e6b04827ef0a42ebcd9a1e 840w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c21c8645c4654b9cef7e248900cbaa382d8064527e66f66b1ce130ba0ab97f31-Group_21.jpg?w=1100&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=3bddf2aae1fb0c25bc201f81ab7c1cc2 1100w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c21c8645c4654b9cef7e248900cbaa382d8064527e66f66b1ce130ba0ab97f31-Group_21.jpg?w=1650&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=41d04acc886d47926d4c2379db689af9 1650w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c21c8645c4654b9cef7e248900cbaa382d8064527e66f66b1ce130ba0ab97f31-Group_21.jpg?w=2500&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=0dc01e743e2a4e6331a3c80e959dcd1f 2500w" />
</Frame>

### 7. Run and Review

Hit Run to execute your flow and see step-by-step output in the Flow Outcome panel.

* **Successful** real-time execution steps in **Flow Outcome**

  <Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/17d2edd51ab0997dc39affbc1ec606b97e5a2eea8bd7224abfdd469dce045203-AFW-4.jpg?fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=523fa9b025adb42acb6917cd97a5a0e4" alt="" className="mx-auto" style={{ width:"56%" }} data-og-width="790" width="790" data-og-height="480" height="480" data-path="images/docs/17d2edd51ab0997dc39affbc1ec606b97e5a2eea8bd7224abfdd469dce045203-AFW-4.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/17d2edd51ab0997dc39affbc1ec606b97e5a2eea8bd7224abfdd469dce045203-AFW-4.jpg?w=280&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=c3e9527ff52e0ed9a56fcddf8af3690a 280w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/17d2edd51ab0997dc39affbc1ec606b97e5a2eea8bd7224abfdd469dce045203-AFW-4.jpg?w=560&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=e48e776052e6568ba65fd1ad3251a0b2 560w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/17d2edd51ab0997dc39affbc1ec606b97e5a2eea8bd7224abfdd469dce045203-AFW-4.jpg?w=840&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=f5e5ff3c731229c1ffa7b19449ee8389 840w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/17d2edd51ab0997dc39affbc1ec606b97e5a2eea8bd7224abfdd469dce045203-AFW-4.jpg?w=1100&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=9dbd835479f5dcd56000f86c3ef391c0 1100w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/17d2edd51ab0997dc39affbc1ec606b97e5a2eea8bd7224abfdd469dce045203-AFW-4.jpg?w=1650&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=32573aad774737e4ebe54c1f365c7fa8 1650w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/17d2edd51ab0997dc39affbc1ec606b97e5a2eea8bd7224abfdd469dce045203-AFW-4.jpg?w=2500&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=7a50c32f3b7becd62f12f891c4610fad 2500w" />
  </Frame>
* **Errors** (e.g., logic issues or invalid config) will be displayed clearly

  <Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d4ace2ddeea2c660998a2f3c11752b2fe467217ad5e912a3c85b4c175547417e-AFW-5.jpeg?fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=c3b0f9ea45e33afa490d5d112972f898" alt="" className="mx-auto" style={{ width:"50%" }} data-og-width="662" width="662" data-og-height="302" height="302" data-path="images/docs/d4ace2ddeea2c660998a2f3c11752b2fe467217ad5e912a3c85b4c175547417e-AFW-5.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d4ace2ddeea2c660998a2f3c11752b2fe467217ad5e912a3c85b4c175547417e-AFW-5.jpeg?w=280&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=5870efd8d054d9285ec1db30384bd137 280w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d4ace2ddeea2c660998a2f3c11752b2fe467217ad5e912a3c85b4c175547417e-AFW-5.jpeg?w=560&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=753f4b93807a45b1d83be5f0d3b56a23 560w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d4ace2ddeea2c660998a2f3c11752b2fe467217ad5e912a3c85b4c175547417e-AFW-5.jpeg?w=840&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=e62b09400fd79f49f6ce77d6cf5ceaae 840w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d4ace2ddeea2c660998a2f3c11752b2fe467217ad5e912a3c85b4c175547417e-AFW-5.jpeg?w=1100&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=313e4f4c6d2d4ac9507ba8f8a7fca874 1100w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d4ace2ddeea2c660998a2f3c11752b2fe467217ad5e912a3c85b4c175547417e-AFW-5.jpeg?w=1650&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=f648900339bc6bcecb35e4ce35e19054 1650w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d4ace2ddeea2c660998a2f3c11752b2fe467217ad5e912a3c85b4c175547417e-AFW-5.jpeg?w=2500&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=17c279021b04da14785cc254693ee4f6 2500w" />
  </Frame>

### 8. Reposition or Delete

* Drag components freely to organize your flow
* **To delete a component:** Select the block in the editor, then click the **trash icon** in the right sidebar

  <Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7a36f8ce885e5c453bfa79a7680228094d9950ca3cb9cc04a140fb8da4f5e80c-Artboard.jpg?fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=fddce446dde88c3a6c59d2e78a315dba" alt="" className="mx-auto" style={{ width:"88%" }} data-og-width="1406" width="1406" data-og-height="730" height="730" data-path="images/docs/7a36f8ce885e5c453bfa79a7680228094d9950ca3cb9cc04a140fb8da4f5e80c-Artboard.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7a36f8ce885e5c453bfa79a7680228094d9950ca3cb9cc04a140fb8da4f5e80c-Artboard.jpg?w=280&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=42eb5a5c9b8f738befeb95474a3a1723 280w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7a36f8ce885e5c453bfa79a7680228094d9950ca3cb9cc04a140fb8da4f5e80c-Artboard.jpg?w=560&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=52ec572327671dc76471b5d9064140c4 560w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7a36f8ce885e5c453bfa79a7680228094d9950ca3cb9cc04a140fb8da4f5e80c-Artboard.jpg?w=840&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=f6492c4906579cf76a93b64ca9aea838 840w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7a36f8ce885e5c453bfa79a7680228094d9950ca3cb9cc04a140fb8da4f5e80c-Artboard.jpg?w=1100&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=4667e75b948f414686b64f7ec2de9c7e 1100w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7a36f8ce885e5c453bfa79a7680228094d9950ca3cb9cc04a140fb8da4f5e80c-Artboard.jpg?w=1650&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=8beacbf74c4d72f50208ddadd3394071 1650w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7a36f8ce885e5c453bfa79a7680228094d9950ca3cb9cc04a140fb8da4f5e80c-Artboard.jpg?w=2500&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=602cd9377096cb81a54ad115873f731c 2500w" />
  </Frame>

## Saving, Exporting

* Your work is **autosaved**, no need to click Save (see timestamp near Run).
* Click **⋮** three dots (top-right) to :

  * **Download as .yaml** your Flow
  * **Delete flow** from your account

  <Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3547ad69bee77cf429fe5599adb669f2c8b5754587b4ab33c574118ed5c75d53-AWF-10.jpg?fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=5926bbc84555f338f7cc4ee1c05ede8f" alt="" className="mx-auto" style={{ width:"49%" }} data-og-width="516" width="516" data-og-height="430" height="430" data-path="images/docs/3547ad69bee77cf429fe5599adb669f2c8b5754587b4ab33c574118ed5c75d53-AWF-10.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3547ad69bee77cf429fe5599adb669f2c8b5754587b4ab33c574118ed5c75d53-AWF-10.jpg?w=280&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=2a0a9d7366f5d0991ad679243533571d 280w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3547ad69bee77cf429fe5599adb669f2c8b5754587b4ab33c574118ed5c75d53-AWF-10.jpg?w=560&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=767616da963cd031dcbcb0d48e02b173 560w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3547ad69bee77cf429fe5599adb669f2c8b5754587b4ab33c574118ed5c75d53-AWF-10.jpg?w=840&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=8f27870ce8c4e099744179a7c2aecede 840w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3547ad69bee77cf429fe5599adb669f2c8b5754587b4ab33c574118ed5c75d53-AWF-10.jpg?w=1100&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=af0734af36b90c19a16b164862a45c5e 1100w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3547ad69bee77cf429fe5599adb669f2c8b5754587b4ab33c574118ed5c75d53-AWF-10.jpg?w=1650&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=554418e9cb053d9b9ffccdeb4a3d5345 1650w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3547ad69bee77cf429fe5599adb669f2c8b5754587b4ab33c574118ed5c75d53-AWF-10.jpg?w=2500&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=73fc52a38beda706b2254ea98c9e3511 2500w" />
  </Frame>

## Left Sidebar: Workflows

The left sidebar helps you organize and manage your workflows efficiently. Here's how it works:

* **Search Bar** Quickly find any existing workflow by typing its name.
* **Add New Flow** Use the “+ Flow” button to start a new workflow inside the selected folder.
* **Flow List** Displays all your existing workflows, grouped by folders. Each flow entry shows the number of components inside it, e.g. (2).
* **Flow Actions** (Hover Options) When you hover over a flow in the list, additional options appear:

  * **Edit** – Open the flow in the editor.
  * **Rename** – Update the flow name.
  * **Delete** – Permanently remove the flow (confirmation required).

  <Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/55601102ee1b143f9339f94f5988562c919625813549306a34628a9297d0befd-afw18.jpeg?fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=cf2a0ad9e72b51cd85138a1f97150673" alt="" className="mx-auto" style={{ width:"62%" }} data-og-width="878" width="878" data-og-height="736" height="736" data-path="images/docs/55601102ee1b143f9339f94f5988562c919625813549306a34628a9297d0befd-afw18.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/55601102ee1b143f9339f94f5988562c919625813549306a34628a9297d0befd-afw18.jpeg?w=280&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=6869987c4477189764930be6ecb74e5e 280w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/55601102ee1b143f9339f94f5988562c919625813549306a34628a9297d0befd-afw18.jpeg?w=560&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=5e57d5e7f75885ad1ef24767709330e7 560w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/55601102ee1b143f9339f94f5988562c919625813549306a34628a9297d0befd-afw18.jpeg?w=840&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=855f31b6f1d9fedfae02d92fa78ee963 840w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/55601102ee1b143f9339f94f5988562c919625813549306a34628a9297d0befd-afw18.jpeg?w=1100&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=1bd9085ac89d89d480c3f420fd59c70b 1100w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/55601102ee1b143f9339f94f5988562c919625813549306a34628a9297d0befd-afw18.jpeg?w=1650&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=4689d8cb782b79ebb20a83e92ba4bf28 1650w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/55601102ee1b143f9339f94f5988562c919625813549306a34628a9297d0befd-afw18.jpeg?w=2500&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=e1b7e1b9c6afb7c9e0a4878d68f78f7b 2500w" />
  </Frame>

You can also collapse the left sidebar to maximize the workspace. Click the collapse arrow icon to hide or show the sidebar.

## Canvas Tools

* Zoom In / Out using **+ / -** buttons
* Use **Lock icon** to freeze layout
* Use **Fit to View** to focus on working area
* Collapse **Left / Bottom Panels** for full-screen editing

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d532e9ae63a970e884b53ae5408c79f55fb7d4f7f4173ccfad1be21a980c1739-AWF-14.jpeg?fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=74cd3a0b95c16ab5abeef1de5a61773a" alt="" className="mx-auto" style={{ width:"62%" }} data-og-width="374" width="374" data-og-height="322" height="322" data-path="images/docs/d532e9ae63a970e884b53ae5408c79f55fb7d4f7f4173ccfad1be21a980c1739-AWF-14.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d532e9ae63a970e884b53ae5408c79f55fb7d4f7f4173ccfad1be21a980c1739-AWF-14.jpeg?w=280&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=1b3b9932a2ac3783f5a18852ed8b0ab5 280w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d532e9ae63a970e884b53ae5408c79f55fb7d4f7f4173ccfad1be21a980c1739-AWF-14.jpeg?w=560&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=b4af0c802f4d4f98b1bde94a1f3613ab 560w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d532e9ae63a970e884b53ae5408c79f55fb7d4f7f4173ccfad1be21a980c1739-AWF-14.jpeg?w=840&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=6967df93dd871a62ab3a800cac14ecd2 840w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d532e9ae63a970e884b53ae5408c79f55fb7d4f7f4173ccfad1be21a980c1739-AWF-14.jpeg?w=1100&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=9ee1f5a41888e0def03a2f28c7444cec 1100w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d532e9ae63a970e884b53ae5408c79f55fb7d4f7f4173ccfad1be21a980c1739-AWF-14.jpeg?w=1650&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=126f14722286f232eb9e57e20b50d114 1650w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d532e9ae63a970e884b53ae5408c79f55fb7d4f7f4173ccfad1be21a980c1739-AWF-14.jpeg?w=2500&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=006e735859e05c9c278d1b0b8820cb4b 2500w" />
</Frame>

## What Happens Under the Hood?

Each flow is executed as an agentic graph:

* Components are orchestrated via context-passing protocol
* Execution supports branching, parallelism, and tool chaining
* Flow outcome shows step-by-step logs, results, and failures

<Info>
  Note: execution is managed by IO’s internal orchestration engine, ensuring retry logic, state management, and observability.
</Info>

## Tips

* Start with an Agent → Connect an AI Model → Add Tasks and Tools
* Keep blocks modular and reusable
* Use Flow Outcome to debug before scaling
* YAML export lets you version-control or share flows

## Shortcuts & Extras

| Action          | How                                                        |
| --------------- | ---------------------------------------------------------- |
| Upload Flow     | Click **Import From YAML**, select `.yaml`, click Generate |
| Delete Flow     | Click `⋮`, choose **Delete Flow** (confirmation popup)     |
| Export Flow     | Click `⋮`, choose **Download YAML**                        |
| Collapse Panels | Click arrows on **Left** or **Bottom** bars                |
| Fit View        | Use **Zoom to Fit** icon                                   |

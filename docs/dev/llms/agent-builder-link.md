# Source: https://dev.writer.com/home/agent-builder-link.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Learn about Agent Builder

> Build AI agents with a low-code visual editor. Collaborate with drag-and-drop blocks for tool calling, RAG, and custom workflows.

<Warning>
  Agent Builder is in beta. Some features are still in development and are subject to change.
</Warning>

<iframe className="w-full aspect-video rounded-xl" src="https://fast.wistia.com/embed/iframe/7g9zhwwyrt?version=v1x&playerColor=aae3d8" title="Your Video Title" frameBorder="0" allow="autoplay; fullscreen" allowFullScreen />

Agent Builder is a low-code tool for building AI agents with Writer. It enables technical and business builders to collaborate in a shared development environment, where they can assemble an agent using a visual editor and a library of drag-and-drop blocks.

<img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-builder-overview.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=5bd011b4940537f0ba1f85db2dfa6b40" alt="Agent Builder" data-og-width="2362" width="2362" data-og-height="1880" height="1880" data-path="images/agent-builder/agent-builder-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-builder-overview.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=781c0a014bcc1e113400246fba102cc8 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-builder-overview.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=858859dba044d8e7c5b6ac91db33f432 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-builder-overview.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=bf916234792a1d6a69b6850da4c6a8a3 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-builder-overview.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=0a388ba834ee282508d01f9274e82b94 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-builder-overview.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=1c32dda973867f0626f80aa6647fc5c4 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-builder-overview.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=dd479eb457c9c82e28a2d11f5b44177a 2500w" />

Agents created in Agent Builder are fully composable and reusable—from the backend logic to frontend experience—making them faster to build and easier to maintain. Each agent consists of two core components: a blueprint and a UI.

* **Blueprint**: a visual map of the agent's business logic and behavior.
  * Blueprints are created using a library of configurable blocks for tool calling, built-in RAG, text generation, classification, state management, persistent key-value storage, and more.
  * They define how the agent processes input, makes decisions, and takes action—enabling it to reliably orchestrate work across people, data, systems, and even other agents built in Writer.
* **UI**: the interface that users interact with.
  * UIs are designed using elements like input fields, buttons, and embeds, including support for guided workflows with pagination.
  * They give users a structured, intuitive way to engage with agents, from simple chat interfaces to rich, interactive tools.

Agent Builder includes other features to help you build and deploy agents:

* **Custom code**: add custom Python code to the agent to extend its capabilities with more complex logic.
* **Deploy and supervise**: deploy the agent to the Writer cloud, grant access to specific teams, and monitor the agent's performance.

<CardGroup>
  <Card title="Blueprint">
    Define the agent's business logic and behavior.
    <img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-path.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=ae025688c6e18eeb322758556a42f761" alt="Blueprint" data-og-width="3456" width="3456" data-og-height="1814" height="1814" data-path="images/agent-builder/agent-path.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-path.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=f1da279c5773b0613a51bdbdbf6bff97 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-path.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=32ffae7be0d7a16f5d94d56b81fc48ed 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-path.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=7bab99fc7c9e571df2af0e62f7bf08c6 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-path.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=5028866807576fca11cda037b79c2917 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-path.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=bb1e21a19f69358d107cb4861d0d6208 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-path.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=46347e36c59b35df762f73b1094b4aaf 2500w" />
  </Card>

  <Card title="UI">
    Design the agent's interface.
    <img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/demo-agent.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=6a0d38372c2d7cff242a3457a46c019a" alt="UI" data-og-width="3456" width="3456" data-og-height="1814" height="1814" data-path="images/agent-builder/demo-agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/demo-agent.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=1a64409aab0dff73b54117e08f42e455 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/demo-agent.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=cebd1417ee1d0d2afe47aca29f786d9c 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/demo-agent.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=da63201c6ab4ef7c4ec801cdb2733f49 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/demo-agent.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=5109985216f24095fb26a575ec57ec62 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/demo-agent.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=029c2382c84e5255376b1831fa487665 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/demo-agent.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=56a5a0dd544ec6e2956e3185e0d70c6d 2500w" />
  </Card>

  <Card title="Custom code">
    Add custom Python code to the agent to extend its capabilities.
    <img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-custom-code.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=b67251c8abfa5acf37f0918a4985f484" alt="Custom code" data-og-width="2244" width="2244" data-og-height="1106" height="1106" data-path="images/agent-builder/agent-custom-code.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-custom-code.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=61fe889150e69a8c383a3491043b9daa 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-custom-code.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=bad4f3ba011d689556966a74abf4658e 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-custom-code.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=363d492b2b00f1cf78b3a32aa4045d3f 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-custom-code.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=0519577159a816e493440830b23938f3 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-custom-code.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=4225e22d546ad42436625d9a47b092e0 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-custom-code.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=1a62e3dba946a1addae54dee04f6743b 2500w" />
  </Card>

  <Card title="Deploy and supervise">
    Deploy the agent to the Writer cloud and monitor its performance.
    <img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/deploy-and-monitor.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=5a9f82e4e9dc8eaac24c9751bbbd11d5" alt="Deploy and monitor" data-og-width="3454" width="3454" data-og-height="1804" height="1804" data-path="images/agent-builder/deploy-and-monitor.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/deploy-and-monitor.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=5bfc0dd96ceb9776d647dfb67eaaae0d 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/deploy-and-monitor.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=591ee52c32f4c86b0e9b2e31ffcdbcb5 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/deploy-and-monitor.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=3ba8f7f9fa72d4254ce2e7dce9996407 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/deploy-and-monitor.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=019ddf962c31256b7f1c3c06cfe15e41 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/deploy-and-monitor.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=cd592ee511fade2f95a3d68e19730c50 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/deploy-and-monitor.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=01a0521a7a0c83a657cd9448ee4a4c21 2500w" />
  </Card>
</CardGroup>

## Choose your development approach

Agent Builder supports two development approaches:

* **Cloud development**: Build agents directly in the web editor with immediate deployment
* **Local development**: Develop agents locally with your preferred editor, then sync to cloud when ready or [deploy with Docker](/agent-builder/deploy-with-docker)

Get started with Agent Builder with the following guides:

* [Tour the Agent Builder interface and interact with the demo agent](/agent-builder/demo-agent)
* [Build your first agent](/agent-builder/quickstart)
* [Develop agents locally](/agent-builder/local-development)

<feedback />

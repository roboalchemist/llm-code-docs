# Source: https://io.net/docs/guides/intelligence/exploring-ai-agents.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Exploring AI Agents

> Learn about AI Agents on io.net and how to use, configure, and deploy them to build autonomous AI systems.

Agents on [io.net](http://io.net) are packaged, executable components that encapsulate task logic, tool interactions, and external integrations. This section documents the agents provided by [io.net](http://io.net), including core agents and agents that integrate with third-party services such as *GitHub*, *Linear*, and other external tools. It describes how to deploy agents programmatically or via `curl`, configure runtime parameters, and manage secrets required for authenticated access to external APIs. These capabilities support repeatable, secure operation of AI agents within automated workflows.

## Getting Started

<Steps>
  <Step title="Navigate to the Agents tab">
    Open [io.net Intelligence](https://ai.io.net/) and navigate to the Agents tab in the navigation bar.

    <Frame>
            <img src="https://mintcdn.com/ionet-cca8037f/0yoW7mbPwygcy17a/images/docs/io-intelligence/Agents/IOIntel_Agents_NavBar.png?fit=max&auto=format&n=0yoW7mbPwygcy17a&q=85&s=567e679fb1b683b7c15d5e7582bebd5e" alt="Agents Tab in the Navigation Bar" data-og-width="1154" width="1154" data-og-height="212" height="212" data-path="images/docs/io-intelligence/Agents/IOIntel_Agents_NavBar.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/0yoW7mbPwygcy17a/images/docs/io-intelligence/Agents/IOIntel_Agents_NavBar.png?w=280&fit=max&auto=format&n=0yoW7mbPwygcy17a&q=85&s=884cdd313e73ba0cb98207f0b25efaa0 280w, https://mintcdn.com/ionet-cca8037f/0yoW7mbPwygcy17a/images/docs/io-intelligence/Agents/IOIntel_Agents_NavBar.png?w=560&fit=max&auto=format&n=0yoW7mbPwygcy17a&q=85&s=8a409c236ee6849387c12ac04bbc1fe4 560w, https://mintcdn.com/ionet-cca8037f/0yoW7mbPwygcy17a/images/docs/io-intelligence/Agents/IOIntel_Agents_NavBar.png?w=840&fit=max&auto=format&n=0yoW7mbPwygcy17a&q=85&s=90eba24552ddadeef9e23ec94f3ac791 840w, https://mintcdn.com/ionet-cca8037f/0yoW7mbPwygcy17a/images/docs/io-intelligence/Agents/IOIntel_Agents_NavBar.png?w=1100&fit=max&auto=format&n=0yoW7mbPwygcy17a&q=85&s=4c4d429c0610ea3c5f14532579ef25f4 1100w, https://mintcdn.com/ionet-cca8037f/0yoW7mbPwygcy17a/images/docs/io-intelligence/Agents/IOIntel_Agents_NavBar.png?w=1650&fit=max&auto=format&n=0yoW7mbPwygcy17a&q=85&s=3e05198146eef5e6e40212c8c59124ad 1650w, https://mintcdn.com/ionet-cca8037f/0yoW7mbPwygcy17a/images/docs/io-intelligence/Agents/IOIntel_Agents_NavBar.png?w=2500&fit=max&auto=format&n=0yoW7mbPwygcy17a&q=85&s=d93550b0608aa8c809dbe94f2278cdf1 2500w" />
    </Frame>
  </Step>

  <Step title="Select an Agent">
    Browse the list of available agents, or use the search bar to quickly locate a specific agent, then click on your chosen agent to view its details.

    <Frame>
            <img src="https://mintcdn.com/ionet-cca8037f/Mhl052ZVUG1_ajIf/images/docs/io-intelligence/Agents/IOIntel_Agents_MainView.png?fit=max&auto=format&n=Mhl052ZVUG1_ajIf&q=85&s=8058761344db12503f17c7ff1f83e026" alt="Agents Selection and Search Bar" data-og-width="2488" width="2488" data-og-height="1620" height="1620" data-path="images/docs/io-intelligence/Agents/IOIntel_Agents_MainView.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/Mhl052ZVUG1_ajIf/images/docs/io-intelligence/Agents/IOIntel_Agents_MainView.png?w=280&fit=max&auto=format&n=Mhl052ZVUG1_ajIf&q=85&s=2dcdc67e588ee2e97ebb5d7f5b4d1466 280w, https://mintcdn.com/ionet-cca8037f/Mhl052ZVUG1_ajIf/images/docs/io-intelligence/Agents/IOIntel_Agents_MainView.png?w=560&fit=max&auto=format&n=Mhl052ZVUG1_ajIf&q=85&s=240a8483e80f0ebffaaad00d9afa402d 560w, https://mintcdn.com/ionet-cca8037f/Mhl052ZVUG1_ajIf/images/docs/io-intelligence/Agents/IOIntel_Agents_MainView.png?w=840&fit=max&auto=format&n=Mhl052ZVUG1_ajIf&q=85&s=6a9314f3ca9e962090413282cc24eee4 840w, https://mintcdn.com/ionet-cca8037f/Mhl052ZVUG1_ajIf/images/docs/io-intelligence/Agents/IOIntel_Agents_MainView.png?w=1100&fit=max&auto=format&n=Mhl052ZVUG1_ajIf&q=85&s=617a3984a664dad291c8a2357789b460 1100w, https://mintcdn.com/ionet-cca8037f/Mhl052ZVUG1_ajIf/images/docs/io-intelligence/Agents/IOIntel_Agents_MainView.png?w=1650&fit=max&auto=format&n=Mhl052ZVUG1_ajIf&q=85&s=f779214e6ba56ec2011f7ff55fb6b2bf 1650w, https://mintcdn.com/ionet-cca8037f/Mhl052ZVUG1_ajIf/images/docs/io-intelligence/Agents/IOIntel_Agents_MainView.png?w=2500&fit=max&auto=format&n=Mhl052ZVUG1_ajIf&q=85&s=1003823aad48e74c3b48f7e0358faca7 2500w" />
    </Frame>
  </Step>
</Steps>

## **Deploying and Configuring Agents**

When an agent is selected, the *Agent Details* view provides everything needed to evaluate, install, and configure your chosen agent.

### Agent Details and Installation

The *Agent Details* view displays information about your selected agent, along with installation options. Agents can be installed using either Python (via `pip`) or `cURL`, depending on your preferred workflow.

If you do not already have an existing API key, the *Agent Details* view provides an option to generate and inject a new API key directly into the provided `pip` or `curl` installation commands, allowing installation to proceed without leaving the page.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/Mhl052ZVUG1_ajIf/images/docs/io-intelligence/Agents/IOIntel_Agents_InjectAPIKey.png?fit=max&auto=format&n=Mhl052ZVUG1_ajIf&q=85&s=03c4017fa856afed5c660c6818383cbf" alt="IO Intel Agents Inject API Key" data-og-width="2338" width="2338" data-og-height="1064" height="1064" data-path="images/docs/io-intelligence/Agents/IOIntel_Agents_InjectAPIKey.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/Mhl052ZVUG1_ajIf/images/docs/io-intelligence/Agents/IOIntel_Agents_InjectAPIKey.png?w=280&fit=max&auto=format&n=Mhl052ZVUG1_ajIf&q=85&s=b112d5d150a8a27f81dd7854e51cb6e8 280w, https://mintcdn.com/ionet-cca8037f/Mhl052ZVUG1_ajIf/images/docs/io-intelligence/Agents/IOIntel_Agents_InjectAPIKey.png?w=560&fit=max&auto=format&n=Mhl052ZVUG1_ajIf&q=85&s=e91a935389c72e1f26afeaf986ad5bb4 560w, https://mintcdn.com/ionet-cca8037f/Mhl052ZVUG1_ajIf/images/docs/io-intelligence/Agents/IOIntel_Agents_InjectAPIKey.png?w=840&fit=max&auto=format&n=Mhl052ZVUG1_ajIf&q=85&s=702224ed725b35686d110e8edabc978a 840w, https://mintcdn.com/ionet-cca8037f/Mhl052ZVUG1_ajIf/images/docs/io-intelligence/Agents/IOIntel_Agents_InjectAPIKey.png?w=1100&fit=max&auto=format&n=Mhl052ZVUG1_ajIf&q=85&s=4cda204bef321022de4f77b880e79742 1100w, https://mintcdn.com/ionet-cca8037f/Mhl052ZVUG1_ajIf/images/docs/io-intelligence/Agents/IOIntel_Agents_InjectAPIKey.png?w=1650&fit=max&auto=format&n=Mhl052ZVUG1_ajIf&q=85&s=2c31eaa51c7b1bcb7c5f1331633b5c81 1650w, https://mintcdn.com/ionet-cca8037f/Mhl052ZVUG1_ajIf/images/docs/io-intelligence/Agents/IOIntel_Agents_InjectAPIKey.png?w=2500&fit=max&auto=format&n=Mhl052ZVUG1_ajIf&q=85&s=22bda57adae7cb5ef9ae376fc4941ec5 2500w" />
</Frame>

### Trying an Agent before Installation

Before installing, an agent can be tested directly from the interface. Click the **Try Agent** button and it opens the *Playground* where you can be provide input for the agent.

After clicking the **Run Agent** button, the **Result** tab displays the agent’s output, making it possible to quickly validate behavior and responses before deployment.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/WZEfOjHvxZSqrWOL/images/docs/io-intelligence/Agents/IOIntel_Agents_Playground.png?fit=max&auto=format&n=WZEfOjHvxZSqrWOL&q=85&s=09aa251bf60f915a6a5291742816ad95" alt="IO Intel Agents Playground" data-og-width="2464" width="2464" data-og-height="1366" height="1366" data-path="images/docs/io-intelligence/Agents/IOIntel_Agents_Playground.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/WZEfOjHvxZSqrWOL/images/docs/io-intelligence/Agents/IOIntel_Agents_Playground.png?w=280&fit=max&auto=format&n=WZEfOjHvxZSqrWOL&q=85&s=5d16c40d150b7dde1dd9519ea78fa46a 280w, https://mintcdn.com/ionet-cca8037f/WZEfOjHvxZSqrWOL/images/docs/io-intelligence/Agents/IOIntel_Agents_Playground.png?w=560&fit=max&auto=format&n=WZEfOjHvxZSqrWOL&q=85&s=f52a8fe3180f33ea339775ac2d7a485c 560w, https://mintcdn.com/ionet-cca8037f/WZEfOjHvxZSqrWOL/images/docs/io-intelligence/Agents/IOIntel_Agents_Playground.png?w=840&fit=max&auto=format&n=WZEfOjHvxZSqrWOL&q=85&s=1399f52a61d1f1f832fec4954b33b6d9 840w, https://mintcdn.com/ionet-cca8037f/WZEfOjHvxZSqrWOL/images/docs/io-intelligence/Agents/IOIntel_Agents_Playground.png?w=1100&fit=max&auto=format&n=WZEfOjHvxZSqrWOL&q=85&s=4329e6e28b5d1c4c11c93130a2214cf6 1100w, https://mintcdn.com/ionet-cca8037f/WZEfOjHvxZSqrWOL/images/docs/io-intelligence/Agents/IOIntel_Agents_Playground.png?w=1650&fit=max&auto=format&n=WZEfOjHvxZSqrWOL&q=85&s=c4c0d28a63aaaaa318a62468703f640a 1650w, https://mintcdn.com/ionet-cca8037f/WZEfOjHvxZSqrWOL/images/docs/io-intelligence/Agents/IOIntel_Agents_Playground.png?w=2500&fit=max&auto=format&n=WZEfOjHvxZSqrWOL&q=85&s=b0387858b414e8f1038906317785a739 2500w" />
</Frame>

### Configuring Secrets

Agents that integrate with third-party applications require secrets for authenticated access, for example, GitHub, Linear, Jira and many more.

To configure secrets, navigate to the **Secret Management** tab within the *Agent Details* view.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/WZEfOjHvxZSqrWOL/images/docs/io-intelligence/Agents/IOIntel_Agents_SecretManagement.png?fit=max&auto=format&n=WZEfOjHvxZSqrWOL&q=85&s=33a8a166156ecd0741ef48730ed67ab2" alt="IO Intel Agents Secret Management" data-og-width="2380" width="2380" data-og-height="708" height="708" data-path="images/docs/io-intelligence/Agents/IOIntel_Agents_SecretManagement.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/WZEfOjHvxZSqrWOL/images/docs/io-intelligence/Agents/IOIntel_Agents_SecretManagement.png?w=280&fit=max&auto=format&n=WZEfOjHvxZSqrWOL&q=85&s=bad1df4a43171b8e1fd603b4813bd234 280w, https://mintcdn.com/ionet-cca8037f/WZEfOjHvxZSqrWOL/images/docs/io-intelligence/Agents/IOIntel_Agents_SecretManagement.png?w=560&fit=max&auto=format&n=WZEfOjHvxZSqrWOL&q=85&s=89e579a6364fe8aa80bb9f140862be55 560w, https://mintcdn.com/ionet-cca8037f/WZEfOjHvxZSqrWOL/images/docs/io-intelligence/Agents/IOIntel_Agents_SecretManagement.png?w=840&fit=max&auto=format&n=WZEfOjHvxZSqrWOL&q=85&s=d6ae15a43b38c60fc374ef0d4939f92c 840w, https://mintcdn.com/ionet-cca8037f/WZEfOjHvxZSqrWOL/images/docs/io-intelligence/Agents/IOIntel_Agents_SecretManagement.png?w=1100&fit=max&auto=format&n=WZEfOjHvxZSqrWOL&q=85&s=1b00e9ee91c131fa6d79aa98ce983000 1100w, https://mintcdn.com/ionet-cca8037f/WZEfOjHvxZSqrWOL/images/docs/io-intelligence/Agents/IOIntel_Agents_SecretManagement.png?w=1650&fit=max&auto=format&n=WZEfOjHvxZSqrWOL&q=85&s=ff46e7b7f02febb4548347c1a5aceb14 1650w, https://mintcdn.com/ionet-cca8037f/WZEfOjHvxZSqrWOL/images/docs/io-intelligence/Agents/IOIntel_Agents_SecretManagement.png?w=2500&fit=max&auto=format&n=WZEfOjHvxZSqrWOL&q=85&s=eec267a2e9cbf6a7eb83ed2075b0e5e8 2500w" />
</Frame>

On this tab:

* Clicking the **Manage Secrets** button redirects you to the *API Keys and Secrets* page.
* On the *API Keys and Secrets* page, a new secret can be added here by clicking **Add Secret** and providing the following details:
  * *Secret Name*
  * *Secret Value*
  * *Associated Agent*

Alternatively, secrets can be created or selected directly within the **Secret Management** section of the *Agent Details* view:

* An existing secret can be selected from the list.
* A new secret can be created by entering a secret name and value.
* Secrets created here are automatically saved and will also appear in the *API Keys and Secrets* page.

Once the required secrets are configured, the agent is fully set up and ready to be interacted with.

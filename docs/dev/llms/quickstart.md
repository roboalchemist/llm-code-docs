# Source: https://dev.writer.com/home/quickstart.md

# Source: https://dev.writer.com/agent-builder/quickstart.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Agent Builder Quickstart

> Build your first agent in Agent Builder. Create a meeting notes summarizer with a visual interface and blueprint in this step-by-step tutorial.

<Warning>
  Agent Builder is in beta. Some features are still in development and are subject to change.
</Warning>

This quickstart walks through building a new agent that summarizes meeting notes in different formats for various stakeholders.

<CardGroup>
  <Card title="Interface">
        <img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/quickstart-interface.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=5b037297a0523ccd9f956942e028cd3b" alt="Agent Builder interface showing text input for meeting notes and dropdown for summary format" data-og-width="3456" width="3456" data-og-height="1802" height="1802" data-path="images/agent-builder/quickstart-interface.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/quickstart-interface.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=2ca9b8e58d016568be86eb3ea5ff4333 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/quickstart-interface.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=da52ae76cb5d5d7570a8c66d73410255 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/quickstart-interface.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=d227d2a8b948029e6d9101549f336090 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/quickstart-interface.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=c9c9de6c1cbfc23970fdb40537fbc72e 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/quickstart-interface.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=fcaf3e629d12e5923bc45380e51d1dd6 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/quickstart-interface.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=51de4c64c23a3e465f6f03e8dc6e651b 2500w" />
  </Card>

  <Card title="Blueprint">
        <img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/quickstart-blueprint.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=a929fdee047f656e931625698dc839b9" alt="Agent Builder blueprint with blocks for processing meeting notes and generating summaries" data-og-width="3456" width="3456" data-og-height="1812" height="1812" data-path="images/agent-builder/quickstart-blueprint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/quickstart-blueprint.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=dc956610c3341f494f5b92208fede78b 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/quickstart-blueprint.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=ce91971cf2adbe38d74916b299e0709c 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/quickstart-blueprint.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=efe0bdfa3fc88fcbae8b758ecba67a74 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/quickstart-blueprint.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=1bdc9d1e199c0e2b2065b5d4023cf26e 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/quickstart-blueprint.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=f54886444ec593899867043d2857cdbd 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/quickstart-blueprint.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=d7ad7f4fed75977d0e9a17272ecf9913 2500w" />
  </Card>
</CardGroup>

This quickstart covers how to:

* [Create a new Agent Builder project](#create-a-new-agent-builder-project)
* [Clear the demo agent that's automatically created](#clear-the-demo-agent)
* [Build the agent's UI to accept meeting notes and select a summary format](#build-the-ui)
* [Build the agent's blueprint to summarize the meeting notes and display the result in the UI](#build-the-blueprint)
* [Preview the agent](#preview-the-agent)
* [Deploy the agent](#deploy-the-agent)

<Tip>
  If you are unfamiliar with Agent Builder:

  * Review the [Agent Builder overview](/agent-builder/overview) to learn more about the different components of an agent.
  * Follow the [Demo agent walkthrough](/agent-builder/demo-agent) to see how to modify an existing agent.
</Tip>

## Choose your development approach

This quickstart shows the cloud development workflow. If you prefer to develop locally with your editor of choice, see [Develop agents locally](/agent-builder/local-development) for the local development workflow.

You can follow the same steps here to build and deploy the quickstart agent locally once you've initialized a local project.

## Create a new Agent Builder project

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

## Clear the demo agent

When you create a new Agent Builder project, a demo agent is automatically created for you. You can remove the demo agent's components and blueprints to start building your own agent.

### Clear the UI

<Steps>
  <Step title="Delete the top-level Page component from the Component Tree">
    Navigate to the **Interface** view. Then select the **Interface Layers** section in the left sidebar.

    Click the top **Page** component from the UI component tree.

        <img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/select-page-element.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=ec50052a28934c909c68b518885f26da" alt="" data-og-width="624" width="624" data-og-height="380" height="380" data-path="images/agent-builder/select-page-element.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/select-page-element.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=c8efb2c8fbcff521352dc260dbfe0bee 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/select-page-element.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=027a85d1b0f7555aa05500735ad8e5e4 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/select-page-element.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=41bc2b9d47712c977ab85ebb3004af93 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/select-page-element.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=3e770042e90a6bd569800e22e5abfe4e 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/select-page-element.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=9ec38938e957b7aeea0e974ce6ed35d0 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/select-page-element.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=8e072193b7c317d15aa97cfb5621b7b5 2500w" />

    Then click the three vertical dots on the Page's settings menu to find the **Delete** option.

        <img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/delete-page.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=d0671ed7e5bac4841af791de261db67e" alt="" data-og-width="660" width="660" data-og-height="674" height="674" data-path="images/agent-builder/delete-page.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/delete-page.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=94e24475c6d5fc629fc808d27f415ecc 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/delete-page.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=a99c05f36272d69cfc94fc65354284b9 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/delete-page.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=63b603068c46ffb283634dbd96899943 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/delete-page.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=385d5bd94fd11634f46314544009da86 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/delete-page.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=e995b99f35d71e20d8cf7f7c9d3f7e2a 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/delete-page.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=b98f217eb08241e1e97689d9d6a8daa0 2500w" />
  </Step>

  <Step title="Add a new Page">
    Your Component Tree should now contain a single **Root** component.

    Click **Add page** at the bottom of the component tree to create a new blank page.

        <img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-new-page.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=0f2230acf1920193b55b0956540c03f5" alt="" data-og-width="438" width="438" data-og-height="80" height="80" data-path="images/agent-builder/add-new-page.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-new-page.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=f2b9c03fe7a8e31f7ce97ee668c0ba8d 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-new-page.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=dd77edf68152c4d777e15ece497466da 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-new-page.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=11815b76be3918ff0d3c9820778057c5 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-new-page.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=fde7cd3fa8c6f0483763d7501b9f75a1 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-new-page.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=dfa36412fd7709e0d187c963b7cc0281 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-new-page.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=d3eb4707a21f333741ba209e5a9e22af 2500w" />
  </Step>
</Steps>

### Clear the blueprint

<Steps>
  <Step title="Delete the first component under Blueprints Root">
    Navigate to the **Blueprints** view. Then select the **Blueprints Layers** section in the left sidebar.

    Click the first component under **Blueprints Root**. Here, the component is a blueprint called `BUTTON@CLICK_1`.

        <img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprint-component-tree.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=e2afa8a10d7dd95c9946d394f8332a55" alt="" data-og-width="600" width="600" data-og-height="368" height="368" data-path="images/agent-builder/blueprint-component-tree.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprint-component-tree.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=203f295519300e12a9a7613ff3fb8cbd 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprint-component-tree.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=7f6ab819165711a25fc44b6a48b3194e 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprint-component-tree.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=704b70a5f957853d0252f2adb39fa61e 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprint-component-tree.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=caf1a4c090e2e12201d9da606c76d257 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprint-component-tree.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=b30a449eca6292d4c6f4ec6361bdd24a 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprint-component-tree.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=add7145ddf39f7a068ce95397f34db3c 2500w" />

    Then click the three vertical dots on the blueprint's settings menu to find the **Delete** option.

        <img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/delete-blueprint.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=a9cbe340c9a4681bc533717d83e7658f" alt="" data-og-width="652" width="652" data-og-height="684" height="684" data-path="images/agent-builder/delete-blueprint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/delete-blueprint.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=1d758d2fb62bfe0d2493f972ae1e4c7d 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/delete-blueprint.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=9d1a07f713fddea9077c59026debbcb9 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/delete-blueprint.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=61d5b55fb7c06a6b5441e0600f3e11a5 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/delete-blueprint.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=6b756483439d177f2bbfcabd48be7895 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/delete-blueprint.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=9900defc83a698f9706aa069f242d81a 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/delete-blueprint.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=76966d92a1283cba265790b6a1c8a7f2 2500w" />
  </Step>

  <Step title="Add a new Blueprint">
    Your blueprint's component tree should now be empty.

    Click **Add blueprint** at the bottom of the component tree to create a new blank blueprint.

        <img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-blueprint.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=ad77596bd30a5ec50453fd1dccb5fefc" alt="" data-og-width="440" width="440" data-og-height="78" height="78" data-path="images/agent-builder/add-blueprint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-blueprint.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=673622b583b78df18d7140c284f45846 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-blueprint.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=3fe0f420023282e8006ca06c7bd4ab9c 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-blueprint.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=7cd5edf407745e241a59cb303c390c10 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-blueprint.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=cf29545e9756d364ebc877f690971b05 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-blueprint.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=674e831ee7ae79b8282431ce4a4f21d7 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-blueprint.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=f93d3be64f51eabac5aa0d6888273954 2500w" />
  </Step>
</Steps>

## Build the UI

Now that you have an empty page, build the UI for the new agent. This agent has the following components:

* A **Text area** for users to paste their meeting notes
* A **Select input** for users to select the summary format they want
* A **Button** to start the summarization process
* A **Message** component to display a loading message while summarization is in progress
* A **Text** component to display the summary

Navigate to the **Interface** view to build the UI.

### Add the Text area Input

The [**Text area Input** component](/components/textareainput) is where users can paste their meeting notes.

<Steps>
  <Step title="Add the Text area Input component to the canvas">
    Make sure you are in the **Interface** view. Then open the **Add block** section in the left sidebar and search for the **Text area Input** component in the component library.

    Click and drag the **Text area Input** component onto the canvas.
  </Step>

  <Step title="Edit the Text area Input component settings">
    Click the **Text area Input** component you just added to edit its settings. Update the following settings:

    * **Label**: `Meeting notes`
    * **Placeholder**: `Paste your meeting notes here.`
    * **Link variable** under **Binding**: `meeting_notes`. This allows the blueprint to access the meeting notes content whenever the user updates it.

    <Tip>
      The "link variable" is stored in the agent's state. The state is a set of variables that both the blueprint and the UI can access and update. You can learn more about the agent's state in [Agent state](/agent-builder/state).
    </Tip>

        <img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/meeting-notes-textarea.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=092065f0671c8c6b3eb42fb554274609" alt="" data-og-width="3456" width="3456" data-og-height="1810" height="1810" data-path="images/agent-builder/meeting-notes-textarea.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/meeting-notes-textarea.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=ac0d07785d02f3715a965c8dbacff374 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/meeting-notes-textarea.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=07d894d84145b0341433f43361eca4e6 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/meeting-notes-textarea.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=ca50e98d8a81fa987330d9489e7505aa 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/meeting-notes-textarea.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=7d258f7fbedbf86709b18d3555b1e737 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/meeting-notes-textarea.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=77a39ea2ae9d8561060fea999fde307b 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/meeting-notes-textarea.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=6a14c06bf9b7ed90be2c1580c4e034fa 2500w" />
  </Step>
</Steps>

### Add the select input

The [**Select input** component](/components/selectinput) is where users can choose what type of summary they want via a dropdown.

<Steps>
  <Step title="Add the select input component to the canvas">
    Search for the **Select input** component in the component library on the left side of the page.

    Click and drag the **Select input** component onto the canvas.
  </Step>

  <Step title="Edit the select input component settings">
    Click the **Select input** component you just added to edit its settings. Update the following settings:

    * **Label**: `Summary format`
    * **Options**: Add the options you want to display in the dropdown. For this example, add the following options, with the key and the value both set to the option name.
      * `Executive brief`
      * `Action items only`
      * `Full summary`
      * `Key decisions`
    * **Link variable** under **Binding**: `summary_format`. This allows the blueprint to access the selected format whenever the user changes it.

        <img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/summary-format-dropdown.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=b646a7aba2f804026cfc1c2eef36c42b" alt="" data-og-width="3454" width="3454" data-og-height="1806" height="1806" data-path="images/agent-builder/summary-format-dropdown.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/summary-format-dropdown.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=bf8e5e6bb77241f03aa2ae6c87a5d14a 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/summary-format-dropdown.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=7dbbe796d76fffda728a1f0d120ca9fd 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/summary-format-dropdown.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=d6cf4e6e9719c3e666b0c7fbbcf5fd31 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/summary-format-dropdown.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=64ce75cd350f6adcae3b768b1b0ce64c 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/summary-format-dropdown.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=5b1e002d8781063c491d498e360afce7 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/summary-format-dropdown.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=956be04efcf27fe37029f8022ace3ab2 2500w" />
  </Step>
</Steps>

### Add the summarize button

Next, add a [**Button** component](/components/button) to the UI. In a later step, you'll connect this button to the blueprint that triggers the summarization process.

<Steps>
  <Step title="Add the button component to the canvas">
    Search for the **Button** component in the block library on the left side of the page. Then click and drag the **Button** component onto the canvas.
  </Step>

  <Step title="Edit the button component settings">
    Click the **Button** component you just added to open its settings. Update the following settings:

    * **Text**: `Generate summary`

        <img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/generate-summary-button.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=460b1b1c51b1d86265d3aaddf8af25e8" alt="" data-og-width="3454" width="3454" data-og-height="1806" height="1806" data-path="images/agent-builder/generate-summary-button.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/generate-summary-button.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=c7857feabc3a9deed7903a7e36bca5ae 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/generate-summary-button.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=bf7f4153790809ebbc1e197fe6901776 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/generate-summary-button.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=dcf1954bd29f4a4995059cf12ad1cfec 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/generate-summary-button.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=022dc36128048c6663f7050db0bf59bf 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/generate-summary-button.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=c78c1457c5fa330ce2f7c519e55e7681 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/generate-summary-button.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=72aed2a02b33067c4873cd51902d47a6 2500w" />
  </Step>
</Steps>

### Add the progress message component

The [**Message** component](/components/message) displays messages to users. Here, you use it to display a loading message while summarization is in progress.

<Steps>
  <Step title="Add the message component to the canvas">
    Search for the **Message** component in the block library. Then click and drag the **Message** component onto the canvas.
  </Step>

  <Step title="Edit the message component settings">
    Click the **Message** component you just added to edit its settings. Update the following settings:

    * **Message**: `@{status}`. This reads from the `status` state variable, which the blueprint will set to indicate the progress of the summarization.

        <img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/status-message-component.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=1b8cdf69f044398c452b5957617ebcd7" alt="" data-og-width="3456" width="3456" data-og-height="1810" height="1810" data-path="images/agent-builder/status-message-component.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/status-message-component.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=b3e47cd616d121232b57ffee3dfe3d01 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/status-message-component.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=7ab6b7ec17870ccb5c27a56e0ce47cf7 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/status-message-component.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=ac897b9535c36a7e44db09ae791c64f8 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/status-message-component.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=2a52f6a348f387fa8a38b7a83722d47b 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/status-message-component.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=da4bfcaadfc445b9bbb339f8fcdb7b9b 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/status-message-component.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=a8620dd0dd3fc4bc84b81734d519075a 2500w" />
  </Step>
</Steps>

### Add the summary text component

The [**Text** component](/components/text) is where the blueprint displays the meeting summary when it's complete.

<Steps>
  <Step title="Add the text component to the canvas">
    Search for the **Text** component in the block library on the left side of the page. Then click and drag the **Text** component onto the canvas.

    <Tip>
      There are multiple components with the name **Text** in them. Make sure you select the **Text** component under the **Content** section of the component library.
    </Tip>
  </Step>

  <Step title="Edit the text component settings">
    Click the **Text** component you just added to edit its settings. Update the following settings:

    * **Text**: `@{summary}`. This displays the value of the `summary` state variable, which the blueprint sets to the meeting summary.
    * **Use Markdown**: Select **Yes**. This allows you to use markdown formatting in the text.

        <img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/summary-text-component.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=b4b7c9b86cf25f99093aff624cc556a2" alt="" data-og-width="3456" width="3456" data-og-height="1814" height="1814" data-path="images/agent-builder/summary-text-component.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/summary-text-component.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=f36ecd005568a0d80802e039f69d59f3 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/summary-text-component.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=72b39eee4c92b8d34629d03e23290721 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/summary-text-component.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=e910441cd7c8afc59efce1764fbfb583 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/summary-text-component.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=96484941c13c4712101678633a11be98 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/summary-text-component.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=5c4eba3bbd46bf298538bb806dc87355 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/summary-text-component.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=30b5f8e1f2491c2e690ed05dbb51da54 2500w" />
  </Step>
</Steps>

## Build the blueprint

With the UI built, you can now build the blueprint for the new agent.

The blueprint has the following logic:

1. The **UI trigger** block triggers the blueprint when the user clicks the **Generate summary** button in the UI.
2. The **Set state** block sets the `status` state variable to `Summarizing` so that the `Message` component in the UI can display it.
3. The **Text generation** block generates a summary of the meeting notes based on the selected format.
4. The **Set state** block sets the `summary` state variable to the generated summary so that the `Text` component in the UI can display it.
5. The **Set state** block sets the `status` state variable back to an empty string to clear the loading message from the UI.

Navigate to the **Blueprints** view to build the blueprint.

### Add the UI trigger

The [**UI trigger** block](/blueprints/uitrigger) triggers the blueprint when the user clicks the **Generate summary** button in the UI.

<Steps>
  <Step title="Add the UI trigger block to the canvas">
    Make sure you are in the **Blueprints** view. Then open the **Add block** section in the left sidebar and search for the **UI trigger** block in the blueprints toolkit.

    Click and drag the **UI trigger** block onto the canvas.
  </Step>

  <Step title="Edit the UI trigger block settings">
    Click the **UI trigger** block you just added to edit its settings. Update the following settings:

    * **Component ID**: Select the button component (it should show as `Generate summary`)
    * **Event type**: `wf-click`. This triggers the blueprint when the user clicks the **Generate summary** button in the UI.

        <img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/ui-trigger-meeting-notes.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=339e6e6e8942e0582d0c82c28fab3bf0" alt="" data-og-width="3456" width="3456" data-og-height="1816" height="1816" data-path="images/agent-builder/ui-trigger-meeting-notes.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/ui-trigger-meeting-notes.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=999e8e5ba97d4ab89c5d99d754182d5f 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/ui-trigger-meeting-notes.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=46c1b395a2df0cb3889300d4f85deb36 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/ui-trigger-meeting-notes.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=63cf87cd1951d61a61ad4fabbd4a1c50 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/ui-trigger-meeting-notes.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=171015edfd79c4608eb276664eda852c 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/ui-trigger-meeting-notes.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=3746f06f28d4654f332c9bec2d8f717c 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/ui-trigger-meeting-notes.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=60c483552bd53e228bd97082ddcab7de 2500w" />
  </Step>
</Steps>

### Add the set state block for the progress message

The [**Set state** block](/blueprints/setstate) sets the `status` state variable to `Summarizing` so that the `Message` component in the UI can display it.

<Steps>
  <Step title="Add the set state block to the canvas">
    Search for the **Set state** block. Then click and drag the **Set state** block onto the canvas.

    Connect the **Set state** block to the **UI trigger** block by dragging a line from the green dot on the **UI trigger** block to the **Set state** block. This tells the blueprint to execute the **Set state** block after the UI Trigger completes.
  </Step>

  <Step title="Edit the set state block settings">
    Click the **Set state** block you just added to edit its settings. Update the following settings:

    * **Link variable**: `status`
    * **Value**: `% Generating summary`. The `%` symbol indicates that the message should display a dynamic loading symbol.

    The **Message** component in the UI displays the loading message when this block is executed.

        <img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/set-status-summarizing.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=86bf9a51363ac3c6e91922c3b276ada2" alt="" data-og-width="3456" width="3456" data-og-height="1810" height="1810" data-path="images/agent-builder/set-status-summarizing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/set-status-summarizing.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=b80a2cf70c955dd1466d80e442a6d302 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/set-status-summarizing.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=e3eedee998d37eee9ebbff398b7b699b 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/set-status-summarizing.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=6ee9ed720aaa730a4dc427edc8f51dda 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/set-status-summarizing.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=7e9f37e574ae7aa265637dd31d7f386f 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/set-status-summarizing.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=2ed56057940eae2d374dbfee1ca0dc35 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/set-status-summarizing.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=31a63d173cbbaf3b6060bc060afafef5 2500w" />
  </Step>
</Steps>

At this point, you can preview the agent to see the new behavior. When you click the **Generate summary** button, the `Message` component displays the loading message that you set in the **Set state** block.

<img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/preview-agent-summarizing.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=8a22735e4ab67c553b087862b3383e4b" alt="" data-og-width="3456" width="3456" data-og-height="922" height="922" data-path="images/agent-builder/preview-agent-summarizing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/preview-agent-summarizing.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=e866253afea975296e484cca2f3639ea 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/preview-agent-summarizing.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=0823dbc0901dbbf92cb692561c67f663 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/preview-agent-summarizing.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=0f255e6a017bf287129e76fbd9bbcda3 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/preview-agent-summarizing.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=2caa7f6cd6fdd1c0d2400623deb5dd26 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/preview-agent-summarizing.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=c88d0bd2be969cc46fa752f300121c15 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/preview-agent-summarizing.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=9f56287ffef87281e972b37fdfe9fc55 2500w" />

### Add the text generation block

The [**Text generation** block](/blueprints/textgeneration) generates a summary of the meeting notes based on the selected format using Palmyra LLMs.

<Steps>
  <Step title="Add the text generation block to the canvas">
    Search for the **Text generation** block in the block library. Then click and drag the **Text generation** block onto the canvas.

    Connect the previous **Set state** block to this **Text generation** block. Drag a line from the green dot on the **Set state** block to the **Text generation** block. This tells the blueprint to execute the **Text generation** block after the **Set state** block completes successfully.
  </Step>

  <Step title="Edit the text generation block settings">
    Click the **Text generation** block you just added to edit its settings. Update the following settings:

    * **Prompt**: Enter the following prompt. This prompt references the `meeting_notes` and `summary_format` state variables, which you set up in the UI. It instructs the agent to summarize the meeting notes and defines the different formats.

    ```
    Summarize these meeting notes based on the requested format:

    Meeting Notes: @{meeting_notes}
    Format: @{summary_format}

    Guidelines for each format:
    - Executive brief: Create a concise 2-3 sentence overview focusing on high-level outcomes and decisions for leadership
    - Action items only: List only the specific action items, who is responsible, and deadlines
    - Full summary: Provide a comprehensive summary including discussion points, decisions, action items, and next steps
    - Key decisions: Focus specifically on decisions made during the meeting and their implications

    Format the output appropriately for the selected format type.
    ```

        <img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/meeting-notes-text-generation.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=3fcf16dd570ca0395db4434084a79374" alt="" data-og-width="3456" width="3456" data-og-height="1812" height="1812" data-path="images/agent-builder/meeting-notes-text-generation.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/meeting-notes-text-generation.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=ada6665f6b715084c6a23615bf2cacb2 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/meeting-notes-text-generation.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=330297e8b70062e78d5d3673aee651a5 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/meeting-notes-text-generation.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=b2fffbd79a6fbffa0672ee7250f3f6c7 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/meeting-notes-text-generation.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=ccb0265d4921493d88250ac659b7eb43 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/meeting-notes-text-generation.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=4460bbeceaefc8f0ac85eecc5954a0a4 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/meeting-notes-text-generation.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=5920e2341deea931a57e7e301cdafbe6 2500w" />
  </Step>
</Steps>

### Add the set state block for the summary result

This [**Set state** block](/blueprints/setstate) sets the `summary` state variable to the generated summary so that the Text component in the UI can display it.

<Steps>
  <Step title="Add the set state block to the canvas">
    Search for the **Set state** block in the block library. Then click and drag the **Set state** block onto the canvas.

    Connect the new **Set state** block to the **Text generation** block. Drag a line from the green dot on the **Text generation** block to the new **Set state** block. This tells the blueprint to execute the new block after the **Text generation** block completes successfully.
  </Step>

  <Step title="Edit the set state block settings">
    Click the **Set state** block you just added to edit its settings. Update the following settings:

    * **Link variable**: `summary`
    * **Value**: `@{result}`. The `result` environment variable is the output of the previous **Text generation** block.

    <Tip>
      The `@{result}` syntax is how you reference the output of previous blocks. Learn more about what data and variables are available to reference in [Using data from previous blocks](/agent-builder/execution-environment).
    </Tip>

        <img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/set-summary-result.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=226c53cb4fb6e248d636b4ec4f5a2599" alt="" data-og-width="3456" width="3456" data-og-height="1812" height="1812" data-path="images/agent-builder/set-summary-result.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/set-summary-result.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=946d7af0e4ad6d4042aeffa3ee8e36c9 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/set-summary-result.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=3ccca2d70893415829b84c8b342face6 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/set-summary-result.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=87e9636a213418dd02c8343f79829df1 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/set-summary-result.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=f8dc740606fc43c1b719d76e4c09d384 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/set-summary-result.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=2276dc7bc6fe05c0ae55a516e4f93ede 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/set-summary-result.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=c10c8099347c9fc257a4a68606b36e35 2500w" />
  </Step>
</Steps>

### Add the set state block to clear the status message

This [**Set state** block](/blueprints/setstate) clears the `status` state variable to remove the status message from the UI.

<Steps>
  <Step title="Add the set state block to the canvas">
    Search for the **Set state** block in the block library. Then click and drag the **Set state** block onto the canvas.

    Connect the new **Set state** block to the previous **Set state** block. Drag a line from the green dot on the previous **Set state** block to the new **Set state** block. This tells the blueprint to execute the new block after the previous block completes successfully.
  </Step>

  <Step title="Edit the set state block settings">
    Click the **Set state** block you just added to edit its settings. Update the following settings:

    * **Link variable**: `status`
    * **Value**: Leave the **Value** blank. This clears the `status` state variable.

        <img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/clear-status-message.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=12817ab9201bbd4de4467b3bea58bb0c" alt="" data-og-width="3456" width="3456" data-og-height="1810" height="1810" data-path="images/agent-builder/clear-status-message.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/clear-status-message.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=0880d823b3aff4e2bb7190860a0e9744 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/clear-status-message.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=d01e5711a434ed9a69c0e74504d2ef89 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/clear-status-message.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=b4672bc7e63fe7574ca556323b4603af 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/clear-status-message.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=2121b3060ce31187a5679d28b334977d 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/clear-status-message.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=03c3ab398faf7d2c919183c08297c11f 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/clear-status-message.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=56f2c2e293e991d995843e43b1540e4e 2500w" />
  </Step>
</Steps>

### Data connection patterns

Notice how the blueprint connects blocks and passes data using variables:

* `@{meeting_notes}` and `@{summary_format}`: the blueprint blocks read from UI inputs via state
* `@{result}`: the blueprint blocks read the output from the Text generation block
* `@{summary}`: the blueprint blocks write the summary to the state, which the UI displays
* `@{status}`: the blueprint blocks set progress messages that the UI displays

This pattern of using `@{variable_name}` is how all Agent Builder components communicate.

## Preview the agent

You've now built the UI and blueprint for the new agent. Go to the **Preview** view to test the agent.

Paste meeting notes into the **Meeting notes** text area and select a summary format from the **Summary format** select input. Then click the **Generate summary** button to see the agent create a summary in your selected format.

Here's a sample transcript that you can use to test if you don't have your own meeting notes:

<Expandable title="Sample transcript">
  ```text  theme={null}
  1
  00:00:00,000 --> 00:00:03,500
  Sarah: Alright everyone, let's start with our Q1 campaign performance.

  2
  00:00:03,500 --> 00:00:07,000
  Sarah: Mike, how are we tracking on the content calendar?

  3
  00:00:07,000 --> 00:00:12,500
  Mike: We're slightly behind on blog posts - only published 8 out of 12 planned for January.

  4
  00:00:12,500 --> 00:00:18,000
  Mike: The SEO-focused pieces are taking longer than expected because we're doing more keyword research.

  5
  00:00:18,000 --> 00:00:22,500
  Mike: The good news is organic traffic is up 18% month-over-month.

  6
  00:00:22,500 --> 00:00:28,000
  Mike: I think we can catch up by end of month if we get approval for two freelance writers at $150 per article.

  7
  00:00:28,000 --> 00:00:32,500
  Sarah: Approved. That's within our content budget. Alex, what's the budget looking like for paid campaigns?

  8
  00:00:32,500 --> 00:00:37,000
  Alex: We've spent 60% of Q1 budget already, but conversion rates are 23% higher than last quarter.

  9
  00:00:37,000 --> 00:00:42,500
  Alex: The LinkedIn campaign is performing especially well for enterprise leads.

  10
  00:00:42,500 --> 00:00:47,000
  Alex: We're seeing a 4.2% CTR compared to 2.8% industry average.

  11
  00:00:47,000 --> 00:00:53,500
  Alex: I'd like to shift $15K from the underperforming Google Display campaign to LinkedIn and maybe test some YouTube ads.

  12
  00:00:53,500 --> 00:00:57,000
  Sarah: Let's do the LinkedIn shift but hold off on YouTube until we see February numbers.

  13
  00:00:57,000 --> 00:01:02,500
  Sarah: We need to be more conservative with spend until we understand the pricing impact.

  14
  00:01:02,500 --> 00:01:06,000
  Sarah: Lisa, any updates on the product launch messaging?

  15
  00:01:06,000 --> 00:01:10,500
  Lisa: The beta feedback is mostly positive. Users love the new dashboard interface and automation features.

  16
  00:01:10,500 --> 00:01:16,000
  Lisa: Main concern is pricing - 40% of beta users said our current model is too high for small businesses.

  17
  00:01:16,000 --> 00:01:20,500
  Lisa: They're comparing us to competitors who start at $39/month.

  18
  00:01:20,500 --> 00:01:25,000
  Lisa: I recommend we create a basic tier at $29/month instead of starting at $79.

  19
  00:01:25,000 --> 00:01:30,500
  Lisa: All marketing materials are ready but we'll need to update pricing pages, sales decks, and comparison charts.

  20
  00:01:30,500 --> 00:01:35,000
  Sarah: That's a significant pricing change that could impact our revenue projections by 30-40%.

  21
  00:01:35,000 --> 00:01:39,500
  Sarah: I need to discuss with leadership before we commit.

  22
  00:01:39,500 --> 00:01:45,000
  Sarah: Can you prepare a comprehensive business case by Friday? Include competitive analysis and revenue projections.

  23
  00:01:45,000 --> 00:01:49,500
  Lisa: Absolutely. I'll also coordinate with the sales team to get their input on customer feedback.

  24
  00:01:49,500 --> 00:01:53,000
  Mike: Quick question - should we hold off on publishing the pricing comparison blog post?

  25
  00:01:53,000 --> 00:01:57,500
  Sarah: Good catch. Yes, hold that one back. Focus on the feature-focused content instead.

  26
  00:01:57,500 --> 00:02:02,000
  Alex: Should we pause the Google Display campaign completely or just reduce spend?

  27
  00:02:02,000 --> 00:02:07,500
  Alex: It's eating budget but only generating 12 leads per month at $89 cost per lead.

  28
  00:02:07,500 --> 00:02:12,000
  Sarah: Reduce to minimum viable spend for now - maybe $2K monthly.

  29
  00:02:12,000 --> 00:02:17,500
  Sarah: We might be able to optimize it later once we have more conversion data.

  30
  00:02:17,500 --> 00:02:22,000
  Alex: Got it. I'll also run some A/B tests on our LinkedIn ad creative while we're scaling that up.

  31
  00:02:22,000 --> 00:02:26,500
  Sarah: Let me summarize our action items: Mike to hire freelancers and catch up on content calendar.

  32
  00:02:26,500 --> 00:02:31,000
  Sarah: Alex to reallocate $15K from Display to LinkedIn and reduce Display to $2K monthly.

  33
  00:02:31,000 --> 00:02:36,500
  Sarah: Lisa to prepare pricing analysis by Friday. I'll schedule leadership review for next Tuesday.

  34
  00:02:36,500 --> 00:02:40,000
  Lisa: Should I invite sales leadership to that pricing review?

  35
  00:02:40,000 --> 00:02:44,500
  Sarah: Yes, definitely include Tom from sales. His team will need to adjust their pitch if we change pricing.

  36
  00:02:44,500 --> 00:02:49,000
  Mike: If pricing changes, how much time do we need to update all marketing materials?

  37
  00:02:49,000 --> 00:02:54,500
  Lisa: About two weeks if we prioritize the sales decks and website first. The brochures can follow.

  38
  00:02:54,500 --> 00:02:59,000
  Sarah: That might push our launch timeline back slightly, but better to get pricing right.

  39
  00:02:59,000 --> 00:03:02,500
  Alex: All good on my end. I'll send the campaign performance report by tomorrow.

  40
  00:03:02,500 --> 00:03:05,000
  Sarah: Perfect. Thanks everyone. See you next week.
  ```
</Expandable>

Try different summary formats with the same meeting notes to see how the output changes based on your selection. You can also experiment with leaving the summary format blank to see how the agent handles it.

If you encounter any issues, refer to the [Troubleshooting](/agent-builder/troubleshooting) guide for debugging information.

## Deploy the agent

When you're ready to deploy the agent, click **Configure deployment** in the top right corner of the Agent Builder interface. You can also access the deployment configuration by going to the [AI Studio homepage](https://app.writer.com/aistudio) and selecting the agent you created.

If the agent isn't deployed, you see a toggle bar that says **Draft**.

<img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/not-deployed.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=d5bb311eb3357a77ba67a5268a79b711" alt="" data-og-width="1280" width="1280" data-og-height="266" height="266" data-path="images/agent-builder/not-deployed.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/not-deployed.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=81fbd0401e689b9f764c3deb4eaae769 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/not-deployed.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=aa9351ab6eee77f041bae7926c231c16 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/not-deployed.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=edcebe62cdb6c3de4c0630789fc25dd4 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/not-deployed.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=c38132de7e6a8ae3f37002ceab6dd42c 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/not-deployed.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=773cedd074e71f6663243e2187cc3283 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/not-deployed.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=bab6ed2f764bae8a1f102a49a1b2e2b1 2500w" />

To deploy the agent, toggle the bar. Writer deploys the agent to the Writer cloud, which takes a moment to complete.

When the deployment is complete, the toggle bar shows **Deployed**. It also shows a list of the teams in your organization, which you can use to grant access to the agent. You must select at least one team before you can view the URL for the deployed agent.

<img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/deployed-agent.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=dcc802273d31cde4ef8bda3e73775508" alt="" data-og-width="3452" width="3452" data-og-height="1804" height="1804" data-path="images/agent-builder/deployed-agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/deployed-agent.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=8fac010e854abdb5e9274e214d5e0cbc 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/deployed-agent.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=6e007c89168f959865c731a81dbe6023 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/deployed-agent.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=543b99a4cfd9cefaabfa440a37cbc4a0 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/deployed-agent.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=170ff3fa7a31a7c4a3161e49384fd1cc 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/deployed-agent.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=c412f40d430ff90144607d6e7e204b6c 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/deployed-agent.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=e8d6151072d595bca4cebb132e4eec57 2500w" />

You can also choose to deploy the agent to the Writer Agent Library for the teams you've granted access to. These teams can see the agent you've created in the main [Ask Writer app](https://app.writer.com).

To help teams find the agent, select **Edit the agent guide**, where you can add a description and other information to help teams use the agent.

<img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-instructions.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=02ab1a120689b63528cbe9e698d39875" alt="" data-og-width="1992" width="1992" data-og-height="1636" height="1636" data-path="images/agent-builder/agent-instructions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-instructions.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=7577219ac8e96a37a6ad19f64853f9cf 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-instructions.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=1032e8b2f1df18ae6ed8f730d35fd7f7 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-instructions.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=af88bfd12f13fae388128683d46dabd7 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-instructions.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=be2e33961fe259a9de0edb2965c4b333 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-instructions.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=ac978dedb83d543ebed96ac4234f6735 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/agent-instructions.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=10a2f0c7e62165ce98640ddce76336ea 2500w" />

## Agentic enhancements

This tutorial shows outcome-driven design in action: you define what kind of summary you want, and the agent adapts. To make this agent even more versatile, consider adding:

* [Send summaries to Slack](/agent-builder/invoice-processing): Automatically post to relevant channels
* [HTTP request blocks](/blueprints/httprequest) and [tool calling](/agent-builder/tool-calling) to integrate with third party APIs to perform actions like:
  * **Emailing participants**: Send summaries via your email API such as SendGrid or Mailgun
  * **Calendar integrations**: Schedule follow-up meetings and block time for tasks
  * **CRM updates**: Log meeting outcomes in your customer database
  * **Task automation**: Create Jira tickets or Asana tasks for each action item

These integrations transform a summarizer into a true meeting assistant that takes action on your behalf.

## Next steps

* Learn how to [add file inputs and parse PDFs](/agent-builder/summarize-pdfs)
* Learn how to [style the agent's UI](/agent-builder/component-styles)
* Learn how to [send messages to Slack](/agent-builder/invoice-processing)
* Add [tool calling for intelligent integrations with external tools](/agent-builder/tool-calling)

<feedback />

# Source: https://dev.writer.com/no-code/deploying-an-agent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy an agent

<Tip> Full-access users can deploy any agent in their organization. Individual builders can deploy agents they create.</Tip>
To deploy a no-code agent, first click on the **Deploy** tab at the top of the page. Depending on your organization's status, you'll have up to four deployment options:

* [**Playground**](#playground): Receive a URL to share with others to test the agent.
* [**Embed agent**](#embed-agent): Embed the agent on your own website or portal.
* [**Deploy to Slack**](#deploy-to-slack): Enable the agent for use within Slack.
* [**Deploy to Writer**](#deploy-to-writer): Enable the agent for use within Writer.

## Playground

Playground is the easiest way to share and test your agent. Just go to **Deploy** and turn on the Playground toggle. You can either copy the Playground URL to share with others, or open the agent in **Playground** in a new tab.

<img src="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/playground.png?fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=c29dc8d98b38428bff8eab3e3b2b66b6" alt="Deploying an agent to the playground" data-og-width="1478" width="1478" data-og-height="492" height="492" data-path="images/no-code/playground.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/playground.png?w=280&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=15023fb8fc9abeb500bb361a699441b5 280w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/playground.png?w=560&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=380bc5890bc613ce60eea0dcc2f03ec0 560w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/playground.png?w=840&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=99ded7376ff7c56fe078a776e4850f28 840w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/playground.png?w=1100&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=dade2e767964eeb6a67794af435fb97b 1100w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/playground.png?w=1650&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=46b5ebf700d197991eace9781afdf663 1650w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/playground.png?w=2500&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=7c6b5e70e6dad394355c93917ce7a501 2500w" />

The **Open** button will take you directly to this agent through the Playground, while the **Copy link** option will generate a shareable link that you can send to any tester or end user to get feedback on your agent.

<Warning>
  Links to the Playground view of an agent don't require authentication. This can be useful for providing external users access to test an agent (they won't be able to navigate elsewhere within your AI Studio).
</Warning>

## Embed agent

Embedding an agent allows you to embed the agent on your own website or portal.

<Steps>
  <Step title="Toggle embed option">
    First, go to the **Deploy** tab and toggle the **Embed Agent** option.
    <img src="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/embed-agent.png?fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=96ce68123d0c83abda968cbc359b9d5c" alt="Embedding an agent" data-og-width="1498" width="1498" data-og-height="696" height="696" data-path="images/no-code/embed-agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/embed-agent.png?w=280&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=a9c5e3cf7f7a79c5420ed00c10cb3ded 280w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/embed-agent.png?w=560&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=e9a18100dbdc65f6721e99c962753210 560w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/embed-agent.png?w=840&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=ac7a10131c9d1257496e6acbe8726b60 840w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/embed-agent.png?w=1100&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=914c70e5ba696ac9042605b6d76d7648 1100w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/embed-agent.png?w=1650&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=38ca95576fe198dc0bd6ea2882f4ed66 1650w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/embed-agent.png?w=2500&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=cd3dc273b4cb92c122285363b4870987 2500w" />
  </Step>

  <Step title="Add domains to allowlist">
    Prevent unauthorized use of this agent by adding domains to the allowlist
    <img src="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/embed-allowlist.png?fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=73a564dfc47a41b3b765848d018ff094" alt="Add domains to allowlist" data-og-width="1482" width="1482" data-og-height="266" height="266" data-path="images/no-code/embed-allowlist.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/embed-allowlist.png?w=280&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=c0fec9867fd3a54b13d5631698f1be4c 280w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/embed-allowlist.png?w=560&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=bc3802ff79ea46b2c3ff717c42ad6a4a 560w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/embed-allowlist.png?w=840&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=a9766835d76051df5960cf901e601192 840w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/embed-allowlist.png?w=1100&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=947f3bfa34b2ec8064a047e104d10134 1100w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/embed-allowlist.png?w=1650&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=542ad3dd102f22d394c26357c33cfe52 1650w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/embed-allowlist.png?w=2500&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=1e452a90a3157752fa22eb23dbb991ce 2500w" />
  </Step>

  <Step title="Select embed style">
    After enabling embed, select your preferred style: centered or widget.
    <img src="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/embed-style.png?fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=e26f0d3c823abb020e72b96fbaca0e13" alt="Embedding styles" data-og-width="1486" width="1486" data-og-height="704" height="704" data-path="images/no-code/embed-style.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/embed-style.png?w=280&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=91d7996c615140fb9ada957c8ce89024 280w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/embed-style.png?w=560&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=4957b9293561c74f697e2b0a0f553568 560w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/embed-style.png?w=840&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=7e7d9b2eeee8874f31d673eaeb9d49f3 840w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/embed-style.png?w=1100&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=0b98b0331294e2db2a196c8536491195 1100w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/embed-style.png?w=1650&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=fa7e01d13f0362af292471e3f4e1b559 1650w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/embed-style.png?w=2500&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=2c5ff1517c5ed448d7bf5108bf674679 2500w" />
  </Step>

  <Step title="Copy the snippet">
    You'll see a block of code that contains the snippet you need to include wherever you want, such as on your own website or portal. Copy the iFrame snippet and share it with your engineering team to embed this agent. You can disable the embed snippet at any time in AI Studio, and any changes you push will immediately update the embeds.
    <img src="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/embed-iframe.png?fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=96e20b081f040c853e7e13bbd9fb5275" alt="Copy the iFrame snippet" data-og-width="1480" width="1480" data-og-height="330" height="330" data-path="images/no-code/embed-iframe.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/embed-iframe.png?w=280&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=c292b08585c16cd30e20ec9916573f37 280w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/embed-iframe.png?w=560&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=f36a9218ff82a276fd08400d27376249 560w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/embed-iframe.png?w=840&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=1b44aa71b8ba65511f88f8305bb40c1e 840w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/embed-iframe.png?w=1100&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=1a536e433758f01ecfbaf0646067ff23 1100w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/embed-iframe.png?w=1650&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=8df78ee1bdae6fee9089c69869075fb7 1650w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/embed-iframe.png?w=2500&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=0b649e16161301bbeea8231847e20896 2500w" />
  </Step>
</Steps>

## Deploy to Slack

If your organization uses chat agents with General chat mode or Knowledge Graph mode with AI Studio graphs, you'll see a Deploy to Slack option. This allows you to enable the agent for use within Slack. Once deployed, the agent will be available in Slack, and you'll be able to access it directly from within your workspace.

<Warning>Deployed agents in Slack will charge token usage. Please refer to our [pricing page](/home/pricing) for more details.</Warning>
<Note>You'll have access to this deployment option if your organization uses agents with chat capabilities using General chat mode or Knowledge Graph mode.</Note>

<Steps>
  <Step title="Toggle Slack option">
    First, go to the **Deploy** tab and click the **Connect to Slack** link.
    <img src="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/deploy-slack.png?fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=b823e742dd60284a06b34ed59865e53c" alt="Deploying an agent to Slack" data-og-width="1472" width="1472" data-og-height="320" height="320" data-path="images/no-code/deploy-slack.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/deploy-slack.png?w=280&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=be7995177ee1f2d7f54db8f59dda651d 280w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/deploy-slack.png?w=560&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=91793d59250af69ea5dd587fdbd21a8e 560w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/deploy-slack.png?w=840&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=901ca86769c74110f35d0fe920672830 840w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/deploy-slack.png?w=1100&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=c40d118f45dd5bb0e045c25aad246cfa 1100w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/deploy-slack.png?w=1650&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=88739e59545e6b939baebac08e017637 1650w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/deploy-slack.png?w=2500&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=93bef674bcab16a038b401d26be45577 2500w" />
  </Step>

  <Step title="Go through the OAuth flow">
    Next, you'll need to go through the OAuth flow to allow Writer to access your Slack workspace.
    <img src="https://mintcdn.com/writer/kYaX1Myslb-BtXRR/images/no-code/slack-2.png?fit=max&auto=format&n=kYaX1Myslb-BtXRR&q=85&s=62b8eee2c9d574ad1de3b4b6c2f9ee1c" alt="Go through the OAuth flow" data-og-width="2048" width="2048" data-og-height="1536" height="1536" data-path="images/no-code/slack-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/kYaX1Myslb-BtXRR/images/no-code/slack-2.png?w=280&fit=max&auto=format&n=kYaX1Myslb-BtXRR&q=85&s=bcdfbfe69a550dbdcfaa8dd6db33e814 280w, https://mintcdn.com/writer/kYaX1Myslb-BtXRR/images/no-code/slack-2.png?w=560&fit=max&auto=format&n=kYaX1Myslb-BtXRR&q=85&s=619453469fb5fba903d8cda80a50f725 560w, https://mintcdn.com/writer/kYaX1Myslb-BtXRR/images/no-code/slack-2.png?w=840&fit=max&auto=format&n=kYaX1Myslb-BtXRR&q=85&s=07897156ff82c6ce44f98d2e6182bc7f 840w, https://mintcdn.com/writer/kYaX1Myslb-BtXRR/images/no-code/slack-2.png?w=1100&fit=max&auto=format&n=kYaX1Myslb-BtXRR&q=85&s=3ec73621a83918f675aa7dfa1cd2b93e 1100w, https://mintcdn.com/writer/kYaX1Myslb-BtXRR/images/no-code/slack-2.png?w=1650&fit=max&auto=format&n=kYaX1Myslb-BtXRR&q=85&s=c818da335f433885f5c034a7c210ba35 1650w, https://mintcdn.com/writer/kYaX1Myslb-BtXRR/images/no-code/slack-2.png?w=2500&fit=max&auto=format&n=kYaX1Myslb-BtXRR&q=85&s=87c83b994657258885f1f3954df348c5 2500w" />
  </Step>

  <Step title="Toggle Slack option">
    You can now toggle the **Deploy to Slack** option to enable the agent for use within Slack.
  </Step>

  <Step title="Connect to Writer">
    Once the agent is Slack-enabled, you can start interacting with it by clicking the Writer button in Slack and selecting "Connect to Writer."
    <img src="https://mintcdn.com/writer/kYaX1Myslb-BtXRR/images/no-code/slack-1.png?fit=max&auto=format&n=kYaX1Myslb-BtXRR&q=85&s=2f27881230b6ee87a9943fe4fa6dfe52" alt="Connect to Writer" data-og-width="2244" width="2244" data-og-height="1732" height="1732" data-path="images/no-code/slack-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/kYaX1Myslb-BtXRR/images/no-code/slack-1.png?w=280&fit=max&auto=format&n=kYaX1Myslb-BtXRR&q=85&s=29c85b4ae8cc2d5d5392cb33f3d15956 280w, https://mintcdn.com/writer/kYaX1Myslb-BtXRR/images/no-code/slack-1.png?w=560&fit=max&auto=format&n=kYaX1Myslb-BtXRR&q=85&s=c331b226796b0885a01ca3af966f481b 560w, https://mintcdn.com/writer/kYaX1Myslb-BtXRR/images/no-code/slack-1.png?w=840&fit=max&auto=format&n=kYaX1Myslb-BtXRR&q=85&s=ad94eb608ca97341f0ff40c9ef52367c 840w, https://mintcdn.com/writer/kYaX1Myslb-BtXRR/images/no-code/slack-1.png?w=1100&fit=max&auto=format&n=kYaX1Myslb-BtXRR&q=85&s=c981191df7705532878132d35d00802a 1100w, https://mintcdn.com/writer/kYaX1Myslb-BtXRR/images/no-code/slack-1.png?w=1650&fit=max&auto=format&n=kYaX1Myslb-BtXRR&q=85&s=49b20a8b0d9f7b32857e67a2111d03cb 1650w, https://mintcdn.com/writer/kYaX1Myslb-BtXRR/images/no-code/slack-1.png?w=2500&fit=max&auto=format&n=kYaX1Myslb-BtXRR&q=85&s=2da2b23204af59f8cdde9e97c1bae838 2500w" />
  </Step>

  <Step title="Return to Slack">
    When you return to Slack, the agent will be available for use. You'll see that the Q\&A functionality is now integrated within Slack.
    <img src="https://mintcdn.com/writer/kYaX1Myslb-BtXRR/images/no-code/slack-3.png?fit=max&auto=format&n=kYaX1Myslb-BtXRR&q=85&s=9fa1edeb44c3394624f35c12a7ae2a27" alt="Return to Slack" data-og-width="2240" width="2240" data-og-height="1728" height="1728" data-path="images/no-code/slack-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/kYaX1Myslb-BtXRR/images/no-code/slack-3.png?w=280&fit=max&auto=format&n=kYaX1Myslb-BtXRR&q=85&s=333a39eb78a309abd813d6ce7a64e774 280w, https://mintcdn.com/writer/kYaX1Myslb-BtXRR/images/no-code/slack-3.png?w=560&fit=max&auto=format&n=kYaX1Myslb-BtXRR&q=85&s=73ce121dba8449c88688c8ed4c2e9fbd 560w, https://mintcdn.com/writer/kYaX1Myslb-BtXRR/images/no-code/slack-3.png?w=840&fit=max&auto=format&n=kYaX1Myslb-BtXRR&q=85&s=b72c67f1599b77a652c0ff773ed7405b 840w, https://mintcdn.com/writer/kYaX1Myslb-BtXRR/images/no-code/slack-3.png?w=1100&fit=max&auto=format&n=kYaX1Myslb-BtXRR&q=85&s=10f6efd78564654eb3b7814be0f0952e 1100w, https://mintcdn.com/writer/kYaX1Myslb-BtXRR/images/no-code/slack-3.png?w=1650&fit=max&auto=format&n=kYaX1Myslb-BtXRR&q=85&s=02399569715c26c8d0518f17a86df2ac 1650w, https://mintcdn.com/writer/kYaX1Myslb-BtXRR/images/no-code/slack-3.png?w=2500&fit=max&auto=format&n=kYaX1Myslb-BtXRR&q=85&s=fcbdb2cd1da713d5b53bf961faf87392 2500w" />
  </Step>

  <Step title="Select interaction mode">
    When using the agent in Slack, you'll have two interaction modes:

    * **General mode:** If the agent uses General mode and doesn't include a Knowledge Graph mode, simply select it and start chatting.
    * **Knowledge Graph mode:** If the agent includes a Knowledge Graph, select the interaction mode—either Knowledge Graph mode or General mode.
      * In General mode, it'll function like a non-graph-enabled agent.
      * In Knowledge Graph mode, you'll be prompted to connect the relevant graphs. Once connected, you can start chatting with the agent.

    If the agent is built with specific data constraints (e.g., a sales Q\&A agent linked only to Salesforce data), you'll select the Knowledge Graph, and the setup will be complete without needing to choose different graphs. This deployment mode leverages the configurations set in the agent builder, ensuring the agent behaves as expected in Slack
    <img src="https://mintcdn.com/writer/kYaX1Myslb-BtXRR/images/no-code/slack-4.png?fit=max&auto=format&n=kYaX1Myslb-BtXRR&q=85&s=1805d6373d412037084a95a930b23ab5" alt="Select interaction mode" data-og-width="2240" width="2240" data-og-height="1728" height="1728" data-path="images/no-code/slack-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/kYaX1Myslb-BtXRR/images/no-code/slack-4.png?w=280&fit=max&auto=format&n=kYaX1Myslb-BtXRR&q=85&s=2547f4489301214fcfeb24b902e3284e 280w, https://mintcdn.com/writer/kYaX1Myslb-BtXRR/images/no-code/slack-4.png?w=560&fit=max&auto=format&n=kYaX1Myslb-BtXRR&q=85&s=6b4a82127016e2f10b0ae9883eb8358d 560w, https://mintcdn.com/writer/kYaX1Myslb-BtXRR/images/no-code/slack-4.png?w=840&fit=max&auto=format&n=kYaX1Myslb-BtXRR&q=85&s=7e5f65397561cc1ea9cf9e69f321e56c 840w, https://mintcdn.com/writer/kYaX1Myslb-BtXRR/images/no-code/slack-4.png?w=1100&fit=max&auto=format&n=kYaX1Myslb-BtXRR&q=85&s=6e9124efc4c91c22974de220a3c28e3e 1100w, https://mintcdn.com/writer/kYaX1Myslb-BtXRR/images/no-code/slack-4.png?w=1650&fit=max&auto=format&n=kYaX1Myslb-BtXRR&q=85&s=0416d054e008e80c4c5a407041f897d7 1650w, https://mintcdn.com/writer/kYaX1Myslb-BtXRR/images/no-code/slack-4.png?w=2500&fit=max&auto=format&n=kYaX1Myslb-BtXRR&q=85&s=13cacb2df6a4b17f4832b61010935874 2500w" />
  </Step>
</Steps>

## Deploy to Writer

If your organization uses the Writer App in addition to AI Studio, you'll see a **Deploy to Writer** option. This allows you to select specific teams in Writer where you want to deploy the agent.
<Note>You'll have access to this option if you have access to the Writer App.</Note>

<Steps>
  <Step title="Update Agent Info">
    Before deploying to Writer, update the **Agent Info** under the **Agent Guide** tab to provide helpful information about the agent to users.
    <img src="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/agent-info.png?fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=02662579b7a8926cab7528f2039bf12b" alt="Agent Info" data-og-width="1758" width="1758" data-og-height="1066" height="1066" data-path="images/no-code/agent-info.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/agent-info.png?w=280&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=9793f653412e2e68006c09aa1789ce35 280w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/agent-info.png?w=560&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=b800a3f89fa1bdb3f41475052d01b625 560w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/agent-info.png?w=840&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=323b1966e6f91666a163aceae67de8c2 840w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/agent-info.png?w=1100&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=6d7ffbb4df14b6ad0cf7e074ff72c4fe 1100w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/agent-info.png?w=1650&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=722ca044e8590923995d1dc592c797ce 1650w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/agent-info.png?w=2500&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=dca2462ecc1b24d2b3c03ccd57fded98 2500w" />
  </Step>

  <Step title="Deploy to Writer">
    Click the deploy button. Once deployed, the agent will be available to those teams within the app library. You can choose to deploy the agent to all teams or select specific teams.
    <img src="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/deploy-writer.png?fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=390de889221d2cffee03f880a1bf8c7c" alt="Deploy to Writer" data-og-width="1476" width="1476" data-og-height="396" height="396" data-path="images/no-code/deploy-writer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/deploy-writer.png?w=280&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=4ee7896b13a4e73120cf9155aaa3fd0f 280w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/deploy-writer.png?w=560&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=58044e1ffb4962c906b350e8bed95c0d 560w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/deploy-writer.png?w=840&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=0ac7ef63adeae7a6ed2bac5e62b6801e 840w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/deploy-writer.png?w=1100&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=39701abd801c02281b4c72a690d66d88 1100w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/deploy-writer.png?w=1650&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=9a5f87581d75a24f020c70435d904765 1650w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/deploy-writer.png?w=2500&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=c6a3d74bd199f5fc49b0d2c7a1eff9e2 2500w" />
  </Step>
</Steps>

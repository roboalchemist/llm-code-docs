# Source: https://docs.tavily.com/documentation/partnerships/IBM.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavily.com/llms.txt
> Use this file to discover all available pages before exploring further.

# IBM watsonx Orchestrate

> Integrate Tavily's AI-powered research capabilities with IBM watsonx Orchestrate

## Overview

Tavily offers two services on IBM watsonx Orchestrate:

* **Tavily Research Agent** — An AI-powered research agent that conducts comprehensive web research using coordinated parallel sub-agents to deliver detailed, citation-backed reports on complex topics.
* **Tavily Search API** — Real-time web search optimized for AI agents and LLMs.

Both services are available through the IBM Cloud catalog and can be procured using IBM credits.

## Setup Guide

### Step 1: Create a Tavily Instance on IBM Cloud

1. Navigate to [IBM Cloud](https://cloud.ibm.com/)
2. In the search bar, type "Tavily" to find the available services

<Frame>
  <img src="https://mintcdn.com/tavilyai/mMnPoAJLztM_oyJe/images/ibm-cloud-search.png?fit=max&auto=format&n=mMnPoAJLztM_oyJe&q=85&s=d93abe6a9991e7b1866db11a044d6b69" alt="Search for Tavily in IBM Cloud" data-og-width="3006" width="3006" data-og-height="1692" height="1692" data-path="images/ibm-cloud-search.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavilyai/mMnPoAJLztM_oyJe/images/ibm-cloud-search.png?w=280&fit=max&auto=format&n=mMnPoAJLztM_oyJe&q=85&s=66bb3c8ace5f9d7d64caa68a8f9bfcf1 280w, https://mintcdn.com/tavilyai/mMnPoAJLztM_oyJe/images/ibm-cloud-search.png?w=560&fit=max&auto=format&n=mMnPoAJLztM_oyJe&q=85&s=09155234b890a142b39526b732e3b8ad 560w, https://mintcdn.com/tavilyai/mMnPoAJLztM_oyJe/images/ibm-cloud-search.png?w=840&fit=max&auto=format&n=mMnPoAJLztM_oyJe&q=85&s=5cbe6c47bf5e911a6cdf1f583e1de7a8 840w, https://mintcdn.com/tavilyai/mMnPoAJLztM_oyJe/images/ibm-cloud-search.png?w=1100&fit=max&auto=format&n=mMnPoAJLztM_oyJe&q=85&s=2a0b6b40225635b89defa1999610109e 1100w, https://mintcdn.com/tavilyai/mMnPoAJLztM_oyJe/images/ibm-cloud-search.png?w=1650&fit=max&auto=format&n=mMnPoAJLztM_oyJe&q=85&s=20e7c1568c4e4c9a25f6f91e5889c49e 1650w, https://mintcdn.com/tavilyai/mMnPoAJLztM_oyJe/images/ibm-cloud-search.png?w=2500&fit=max&auto=format&n=mMnPoAJLztM_oyJe&q=85&s=7dfc4d9f2b862d718959cc05fa6bdee5 2500w" />
</Frame>

3. Select either **Tavily Search API** or **Tavily Research Agent** depending on your needs
4. Click **Create** to provision a new instance

<Frame>
  <img src="https://mintcdn.com/tavilyai/mMnPoAJLztM_oyJe/images/ibm-create-agent.png?fit=max&auto=format&n=mMnPoAJLztM_oyJe&q=85&s=cd49a442c3765a4ff8d88ab56552290c" alt="Create Tavily instance" data-og-width="3018" width="3018" data-og-height="1616" height="1616" data-path="images/ibm-create-agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavilyai/mMnPoAJLztM_oyJe/images/ibm-create-agent.png?w=280&fit=max&auto=format&n=mMnPoAJLztM_oyJe&q=85&s=1179fb2250966942bb1ac167bcef216e 280w, https://mintcdn.com/tavilyai/mMnPoAJLztM_oyJe/images/ibm-create-agent.png?w=560&fit=max&auto=format&n=mMnPoAJLztM_oyJe&q=85&s=93c7f6420b17c70aaba98c03d507bdef 560w, https://mintcdn.com/tavilyai/mMnPoAJLztM_oyJe/images/ibm-create-agent.png?w=840&fit=max&auto=format&n=mMnPoAJLztM_oyJe&q=85&s=16bd5366eaa6d973fb2acce65454ccb3 840w, https://mintcdn.com/tavilyai/mMnPoAJLztM_oyJe/images/ibm-create-agent.png?w=1100&fit=max&auto=format&n=mMnPoAJLztM_oyJe&q=85&s=c5947547fd2937c61fe85b169627ee9a 1100w, https://mintcdn.com/tavilyai/mMnPoAJLztM_oyJe/images/ibm-create-agent.png?w=1650&fit=max&auto=format&n=mMnPoAJLztM_oyJe&q=85&s=8e42bcc3a8cf964fd85fac2a32876d31 1650w, https://mintcdn.com/tavilyai/mMnPoAJLztM_oyJe/images/ibm-create-agent.png?w=2500&fit=max&auto=format&n=mMnPoAJLztM_oyJe&q=85&s=58ca552f949ffad812f2de174ce7fab0 2500w" />
</Frame>

### Step 2: Copy Your Bearer Token

Once your instance is created, copy the bearer token from the credentials section. You'll need this to connect the agent in watsonx Orchestrate.

<Frame>
  <img src="https://mintcdn.com/tavilyai/mMnPoAJLztM_oyJe/images/ibm-agent-bearer-token.png?fit=max&auto=format&n=mMnPoAJLztM_oyJe&q=85&s=8f60155aaf55eb62c48f4164526fd10c" alt="Copy bearer token" data-og-width="2954" width="2954" data-og-height="1504" height="1504" data-path="images/ibm-agent-bearer-token.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavilyai/mMnPoAJLztM_oyJe/images/ibm-agent-bearer-token.png?w=280&fit=max&auto=format&n=mMnPoAJLztM_oyJe&q=85&s=06fa8d689e3b7e90cac08331a164cf8c 280w, https://mintcdn.com/tavilyai/mMnPoAJLztM_oyJe/images/ibm-agent-bearer-token.png?w=560&fit=max&auto=format&n=mMnPoAJLztM_oyJe&q=85&s=859667c7031f5335b8a02e1cd3e20a87 560w, https://mintcdn.com/tavilyai/mMnPoAJLztM_oyJe/images/ibm-agent-bearer-token.png?w=840&fit=max&auto=format&n=mMnPoAJLztM_oyJe&q=85&s=0c71f4fd1924ebc26cf7662cf6133be0 840w, https://mintcdn.com/tavilyai/mMnPoAJLztM_oyJe/images/ibm-agent-bearer-token.png?w=1100&fit=max&auto=format&n=mMnPoAJLztM_oyJe&q=85&s=2bc466ae12ac195600f486c035941ed5 1100w, https://mintcdn.com/tavilyai/mMnPoAJLztM_oyJe/images/ibm-agent-bearer-token.png?w=1650&fit=max&auto=format&n=mMnPoAJLztM_oyJe&q=85&s=e93048264850ae4cebb78a4ba510b0c2 1650w, https://mintcdn.com/tavilyai/mMnPoAJLztM_oyJe/images/ibm-agent-bearer-token.png?w=2500&fit=max&auto=format&n=mMnPoAJLztM_oyJe&q=85&s=bda2f5bf3efef01e0943b9b48cd3003e 2500w" />
</Frame>

### Step 3: Add Tavily to watsonx Orchestrate

1. Navigate to [watsonx Orchestrate](https://dl.watson-orchestrate.ibm.com/chat)
2. Create a new agent

<Frame>
  <img src="https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-create-agent.png?fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=eb4f4ff6f45709cc8895a2aa2a1ea627" alt="Create agent in watsonx Orchestrate" data-og-width="3016" width="3016" data-og-height="1600" height="1600" data-path="images/wxo-create-agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-create-agent.png?w=280&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=5e4f58f5f273e0e2c527a9326a5798ab 280w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-create-agent.png?w=560&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=08e415d86284e6a1cab6e98493b8be82 560w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-create-agent.png?w=840&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=a9bed3c6b8b89db2b4757b1e5c030aef 840w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-create-agent.png?w=1100&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=c195b722b27b2b3576f673ed1447bd11 1100w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-create-agent.png?w=1650&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=7e1de1132aa8f7bd47f4594d22d5d8a0 1650w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-create-agent.png?w=2500&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=f2ac03abdef68208a771cf505f95a848 2500w" />
</Frame>

3. Name your agent

<Frame>
  <img src="https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-name-agent.png?fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=4d3d20fa3a2d5374ec7ba3d94af0944b" alt="Name your agent" data-og-width="2992" width="2992" data-og-height="1600" height="1600" data-path="images/wxo-name-agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-name-agent.png?w=280&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=3a0ce6ee4bb1007d098183f636e1e4f0 280w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-name-agent.png?w=560&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=09a25a1b66bc949726f12058c5a12057 560w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-name-agent.png?w=840&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=b30ca097e522d951947e6c34e7cda39e 840w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-name-agent.png?w=1100&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=ea39a7ceda12b90946800c752ee7ba5f 1100w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-name-agent.png?w=1650&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=74f6c982721d6bff585aadeb7680f34b 1650w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-name-agent.png?w=2500&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=a474a58787f5af2ae89d10509c61e5a3 2500w" />
</Frame>

4. Add a collaborator agent

<Frame>
  <img src="https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-add-agent.png?fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=0aae16eb9c909bd9aed0c60db51ce39a" alt="Add collaborator agent" data-og-width="2998" width="2998" data-og-height="1602" height="1602" data-path="images/wxo-add-agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-add-agent.png?w=280&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=ee09665c3fb8889df3014852fed5aa62 280w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-add-agent.png?w=560&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=7c6ed2f5bf757c6727556012e9694c55 560w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-add-agent.png?w=840&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=d9e3a113bb92bccd72fcff59d0972c7d 840w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-add-agent.png?w=1100&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=28d75b9f012be880f067595cb943ca52 1100w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-add-agent.png?w=1650&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=9d47fcdcd79cae14152730dfef7257e4 1650w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-add-agent.png?w=2500&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=b4dae0af6169984e19268406708e7eeb 2500w" />
</Frame>

5. Select **Tavily Research Agent** from the partner agents list

<Frame>
  <img src="https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-select-tavily-agent.png?fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=8f7e26add4edcbaea7ddd8314c9a87bb" alt="Select Tavily agent" data-og-width="3002" width="3002" data-og-height="1598" height="1598" data-path="images/wxo-select-tavily-agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-select-tavily-agent.png?w=280&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=698bab83e6cf7da165d6aed17c3c66ac 280w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-select-tavily-agent.png?w=560&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=588b9c193f09c7d7a56294a4b110c6ee 560w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-select-tavily-agent.png?w=840&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=6bda31c6c3df85cd93c395e6e8b5b459 840w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-select-tavily-agent.png?w=1100&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=561db9aeb50f25988687cdd0e1653357 1100w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-select-tavily-agent.png?w=1650&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=d1eacccf5563561bed8135c8601b79e1 1650w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-select-tavily-agent.png?w=2500&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=6514016e0109882783e6370a6b973adb 2500w" />
</Frame>

6. Review the agent details and click **Add as collaborator**

<Frame>
  <img src="https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-add-collaborator.png?fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=ab168b3f2b974c5d1c97598f190ff41e" alt="Add Tavily as collaborator" data-og-width="3016" width="3016" data-og-height="1602" height="1602" data-path="images/wxo-add-collaborator.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-add-collaborator.png?w=280&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=254bef6f797dc64c1e4a34cc7a9c0cc7 280w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-add-collaborator.png?w=560&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=71cffb0480bb95abbf85cfcca33953ae 560w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-add-collaborator.png?w=840&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=b4c21b686665fdc2e1929d0b7d4dbe76 840w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-add-collaborator.png?w=1100&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=ef755117da825fb164fef9801bdf8066 1100w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-add-collaborator.png?w=1650&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=80d2e68192ee946c7507bd29de9b3594 1650w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-add-collaborator.png?w=2500&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=53bd1687f71a62a16fa1dd25cada4cb5 2500w" />
</Frame>

7. Enter your bearer token (from Step 2) in the **Bearer token** field and click **Register and add**

<Frame>
  <img src="https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-register-token.png?fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=9577b14c50e386b6b556fd8af23481af" alt="Register agent with bearer token" data-og-width="2990" width="2990" data-og-height="1608" height="1608" data-path="images/wxo-register-token.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-register-token.png?w=280&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=4339bec7acef3439222b410fea727839 280w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-register-token.png?w=560&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=4ba3432910d0d45ad57607e24027a77a 560w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-register-token.png?w=840&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=ddf6c2dc379e6ff453d92a4ca91e45ab 840w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-register-token.png?w=1100&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=4b377893acb1ca81266bf8af1d4199cf 1100w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-register-token.png?w=1650&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=e0feadf454a8993a848055308a1aeea7 1650w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-register-token.png?w=2500&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=84c0a9a1bf83121b46da2d4d788e9a47 2500w" />
</Frame>

8. The Tavily Research Agent will now appear in your agent's **Toolset** under the Agents section

<Frame>
  <img src="https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-agent-loaded.png?fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=7b655e46129563eceb73a61e39c4e9cf" alt="Tavily agent loaded in toolset" data-og-width="3016" width="3016" data-og-height="1614" height="1614" data-path="images/wxo-agent-loaded.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-agent-loaded.png?w=280&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=edfa6720f9ce1086c6c261b2613eea62 280w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-agent-loaded.png?w=560&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=746488acf3c1095519d57a360b9f6265 560w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-agent-loaded.png?w=840&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=aa8d30d0e91b5ff5efb9bdf6cfd0552f 840w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-agent-loaded.png?w=1100&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=db82652e20840df23d7b8f4b87a17773 1100w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-agent-loaded.png?w=1650&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=17e2bcf7a7e3d622bf5120396b7c48a8 1650w, https://mintcdn.com/tavilyai/Wr9BDR90tDFYHmP_/images/wxo-agent-loaded.png?w=2500&fit=max&auto=format&n=Wr9BDR90tDFYHmP_&q=85&s=f21e148943c80119a3184fb317d356e4 2500w" />
</Frame>

### Step 4: Try It Out

Ask a question in the chat that requires real-time web research, and watsonx Orchestrate will automatically hand off to the Tavily Research Agent.

<Frame>
  <img src="https://mintcdn.com/tavilyai/mMnPoAJLztM_oyJe/images/agent-handoff.png?fit=max&auto=format&n=mMnPoAJLztM_oyJe&q=85&s=7e4219aa980df17699d697922c052863" alt="Tavily Research Agent handoff example" data-og-width="2992" width="2992" data-og-height="1600" height="1600" data-path="images/agent-handoff.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavilyai/mMnPoAJLztM_oyJe/images/agent-handoff.png?w=280&fit=max&auto=format&n=mMnPoAJLztM_oyJe&q=85&s=46bbb49c988479792456b4c308710875 280w, https://mintcdn.com/tavilyai/mMnPoAJLztM_oyJe/images/agent-handoff.png?w=560&fit=max&auto=format&n=mMnPoAJLztM_oyJe&q=85&s=2bfcb3aba0f01f76f909abb791cdaee2 560w, https://mintcdn.com/tavilyai/mMnPoAJLztM_oyJe/images/agent-handoff.png?w=840&fit=max&auto=format&n=mMnPoAJLztM_oyJe&q=85&s=1eab5237e9fc05fc27cd296b567bd243 840w, https://mintcdn.com/tavilyai/mMnPoAJLztM_oyJe/images/agent-handoff.png?w=1100&fit=max&auto=format&n=mMnPoAJLztM_oyJe&q=85&s=70549a45c138f2fcf9fe17d2dab97d7e 1100w, https://mintcdn.com/tavilyai/mMnPoAJLztM_oyJe/images/agent-handoff.png?w=1650&fit=max&auto=format&n=mMnPoAJLztM_oyJe&q=85&s=c443905cf7d7fc26a33c626d52f6be1c 1650w, https://mintcdn.com/tavilyai/mMnPoAJLztM_oyJe/images/agent-handoff.png?w=2500&fit=max&auto=format&n=mMnPoAJLztM_oyJe&q=85&s=ccec58e3ddd6379f0bf8642f2bcfc928 2500w" />
</Frame>

Your Tavily Research Agent is now ready to use within watsonx Orchestrate.

## Resources

* [IBM watsonx Orchestrate Documentation](https://www.ibm.com/docs/en/watsonx/watson-orchestrate/base?topic=agents-adding-orchestration#adding-a-collaborator-agent)
* [Partner Agents Catalog](https://www.ibm.com/docs/en/watsonx/watson-orchestrate/base?topic=catalog-partner-agents)

# Source: https://docs.asapp.com/agent-desk/virtual-agent/flows.md

# Flows

> Learn how to build flows to define how the virtual agent interacts with the customer.

Flows define how the virtual agent interacts with the customer. They can be as simple as an answer to an FAQ, or as complex as a multi-turn dialog used to offer self-service recommendations.

Flows are built through a series of [nodes](getting-started#flow-nodes "Flow Nodes") that dictate the flow of the conversation as well as any business logic it needs to perform. Once built, flows can be reached from intents, or redirected to from other flows.

## Flows List

In the flows page, you will find a list of existing flows for your business. The following information displays in table format:

* **Flow Name**
  A unique flow name, with letters and numbers only.
* **Flow Description**
  A brief description that describes the objective of the flow.
* **Traffic from Intent**
  Intents can be routed to specific flows through [intent routing](/agent-desk/virtual-agent/intent-routing "Intent Routing"). In this column, you will see which intents route to the respective flow.
  You can click the intent to navigate to the specific [intent routing detail page](/agent-desk/virtual-agent/intent-routing#intent-routing-detail-page "Intent Routing Detail Page") to view routing behavior details.
* **Traffic from Redirect**
  Flows have the ability to link to one another through the use of [redirect nodes](#redirect-node "Redirect Node"). In this column, you will be able to see which existing flows redirect to the respective flow. You can click the flow to navigate to the specific [flow builder page](#flow-builder "Flow Builder") to view flow details.

## Flow Builder

The flow builder consists of three major parts:

1. Flow Graph
2. Node Configuration Panel
3. Toolbar

<Frame>
  <img src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2e31ab13-f4ee-ceee-c22a-f245d0af9f7c.jpg?fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=6e6c0273a7368fdf04098e617a664e65" data-og-width="1624" width="1624" data-og-height="994" height="994" data-path="image/uuid-2e31ab13-f4ee-ceee-c22a-f245d0af9f7c.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2e31ab13-f4ee-ceee-c22a-f245d0af9f7c.jpg?w=280&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=78c8e967ed7d6a5bbc5137405e161c09 280w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2e31ab13-f4ee-ceee-c22a-f245d0af9f7c.jpg?w=560&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=d093b09da1ed370cd77ca6869ce1aff2 560w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2e31ab13-f4ee-ceee-c22a-f245d0af9f7c.jpg?w=840&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=0cd0bf54dd5f40d0524f1bb9680752e2 840w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2e31ab13-f4ee-ceee-c22a-f245d0af9f7c.jpg?w=1100&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=c64c0fbdb1fd4d3e7dd18fdfd06217d8 1100w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2e31ab13-f4ee-ceee-c22a-f245d0af9f7c.jpg?w=1650&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=468628867ad96ec1ea4952bcbb684db3 1650w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2e31ab13-f4ee-ceee-c22a-f245d0af9f7c.jpg?w=2500&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=469589d5bf6bd22cdd5a3c1ade7bc0da 2500w" />
</Frame>

### Flow Graph

The Flow Graph is a visual representation of the conversation flow you're designing, and displays all possible paths of dialog as you create them.

<Frame>
  <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-61217916-747e-69d4-fc86-34b2e2708503.jpg?fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=4900198dca74ba08894c786f5109869b" data-og-width="1440" width="1440" data-og-height="900" height="900" data-path="image/uuid-61217916-747e-69d4-fc86-34b2e2708503.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-61217916-747e-69d4-fc86-34b2e2708503.jpg?w=280&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=bc5661c166e9047aaf534664aa68eb52 280w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-61217916-747e-69d4-fc86-34b2e2708503.jpg?w=560&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=eb6f91101f9e9496554d8ee739b782d7 560w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-61217916-747e-69d4-fc86-34b2e2708503.jpg?w=840&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=fe5a8a0731b62e14790f9e119e41c4ea 840w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-61217916-747e-69d4-fc86-34b2e2708503.jpg?w=1100&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=de63b2082c020cd0104611b83642795f 1100w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-61217916-747e-69d4-fc86-34b2e2708503.jpg?w=1650&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=3ccd1a26e826c97b8293f9459e2ffb6d 1650w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-61217916-747e-69d4-fc86-34b2e2708503.jpg?w=2500&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=39afa38581b8d8d0e0864e87b922747e 2500w" />
</Frame>

#### Select Nodes

Each node in the graph can be selected by clicking anywhere on the node. Upon selection, the node configuration panel will automatically expand on the right.

#### Flow Graph Zoom

You can zoom in on particular parts of the flow by using the zoom percentage bar at the bottom right or using your computer trackpad or mouse.

### Node Configuration Panel

The node configuration panel allows you to manage settings and configure routing rules for the following [node types](#node-types "Node Types"):

* [Response Node](#node-types "Node Types"): configure virtual agent responses, send deeplinks, and classify what customers say in return.
* [Login Node](#login-node "Login Node"): direct the customer to authenticate before proceeding in the flow.
* [Redirect Node](#redirect-node "Redirect Node"): redirect customer to another flow.
* [Agent Node](#agent-node "Agent Node"): direct the customer to an agent queue.
* [End Node](#end-node "End Node"): wrap up the conversation by confirming whether the customer needs additional help.
* [API Node](#api-node): use API fields dynamically in your flows.

### Toolbar

The toolbar displays the flow name and allows to you perform a number of different functions:

1. [Version Dropdown:](#navigate-flow-versions "Navigate Flow Versions") view and toggle through multiple versions of the flow.
2. [Version Indicators](#version-indicators "Version Indicators"): keep track of flow version deployment to Test or Production environments
3. [Manage Versions](#manage-versions "Manage Versions"): manage flow version deployment to Test or Production environments
4. [Preview](#preview-flow "Preview Flow"): click to preview your current flow version in real-time
5. More Actions:
   * Copy link to test: Navigate to your demo environment to test a flow.
   * Flow Settings: View flow information such as name, description, and flow shortcut.

Learn more: [Save, Deploy, and Test](#save-new-flow "Save New Flow")

<Frame>
  <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9948b1a1-3bf0-5c6c-b7b4-b5108a168b53.jpg?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=eaf00326e7d9433b4bcb56289591ff9a" data-og-width="1999" width="1999" data-og-height="332" height="332" data-path="image/uuid-9948b1a1-3bf0-5c6c-b7b4-b5108a168b53.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9948b1a1-3bf0-5c6c-b7b4-b5108a168b53.jpg?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=ce02aae3ad2922bfd0247402618e0b89 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9948b1a1-3bf0-5c6c-b7b4-b5108a168b53.jpg?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=328817b5090bc5a400f1762d0ffc0d4f 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9948b1a1-3bf0-5c6c-b7b4-b5108a168b53.jpg?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=2903c82ad43fd52ee24ce2504e730dd3 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9948b1a1-3bf0-5c6c-b7b4-b5108a168b53.jpg?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=ddcab6acdea1a0ae8f421d61100190a6 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9948b1a1-3bf0-5c6c-b7b4-b5108a168b53.jpg?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=6e62240fc9059ed7d0644d46204ea4ea 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9948b1a1-3bf0-5c6c-b7b4-b5108a168b53.jpg?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=500be5e8c5f487b71f7f4bfd48c722af 2500w" />
</Frame>

## Node Types

### Response Node

<Frame>
  <img src="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/NodeResponse.png?fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=881ae5661362c68f03a5a0b942bf1b08" data-og-width="392" width="392" data-og-height="440" height="440" data-path="images/messaging-platform/NodeResponse.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/NodeResponse.png?w=280&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=65b57fda4f43590d760f3532c4223beb 280w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/NodeResponse.png?w=560&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=448be84ab153919fd870370fb5c503c3 560w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/NodeResponse.png?w=840&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=f710aa2fe1d463f31476f1ddd6717a6f 840w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/NodeResponse.png?w=1100&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=7ec3c29b42efd5871b03eacdb23a2dc4 1100w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/NodeResponse.png?w=1650&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=e241d44d5b155189c4d65f203c83cc74 1650w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/NodeResponse.png?w=2500&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=4c50e6f0be5447cbe486c13faecbd6af 2500w" />
</Frame>

The **Response** node allows you to configure virtual agent responses, send deeplinks, and classify what customers say in return. It consists of three sections:

1. **Content**
2. **Routing**
3. **Advanced Settings**

### Content

The **Content** section allows you to specify the responses and deeplinks that will be sent to the customer. You can add as many of either as you like by clicking **Add Content** and selecting from the menu.

Once added, this content can be easily reordered by dragging, or deleted by hovering over the content block and clicking the trash icon. In the flow graph, you will be able to preview how the content will be displayed to the customer.

<Frame>
  <img src="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-14590ffb-dd26-1a48-5ebe-05db63fb8363.jpg?fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=68ee53c3bfcc7857ef86dec8ad88a890" data-og-width="1200" width="1200" data-og-height="1240" height="1240" data-path="image/uuid-14590ffb-dd26-1a48-5ebe-05db63fb8363.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-14590ffb-dd26-1a48-5ebe-05db63fb8363.jpg?w=280&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=70372fe4f7557dceee3bad4547bf6411 280w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-14590ffb-dd26-1a48-5ebe-05db63fb8363.jpg?w=560&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=95fbd862f31f30c9a3f221dc457b6c7a 560w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-14590ffb-dd26-1a48-5ebe-05db63fb8363.jpg?w=840&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=a6b0bc8101779985f184f94280683891 840w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-14590ffb-dd26-1a48-5ebe-05db63fb8363.jpg?w=1100&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=d59b2ab7abab0a8713b8fa5b99bfc33f 1100w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-14590ffb-dd26-1a48-5ebe-05db63fb8363.jpg?w=1650&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=b69909bb6317d0bd6dd84044da919fa1 1650w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-14590ffb-dd26-1a48-5ebe-05db63fb8363.jpg?w=2500&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=2dcf202a67359154a09440e8942214c5 2500w" />
</Frame>

#### Responses

Any response text you specify will be sent to the customer when they reach the node.

<Frame>
  <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-84c5c765-de30-25c9-c32b-5de3ab523672.jpg?fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=5d9123f9ec60e34567a91e6e8f440438" data-og-width="1200" width="1200" data-og-height="1020" height="1020" data-path="image/uuid-84c5c765-de30-25c9-c32b-5de3ab523672.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-84c5c765-de30-25c9-c32b-5de3ab523672.jpg?w=280&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=39ed2c6f4f6ff48c78ba9eddc233819b 280w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-84c5c765-de30-25c9-c32b-5de3ab523672.jpg?w=560&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=0f2e28f15c1a79e1c18b98fc6bb0f3ea 560w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-84c5c765-de30-25c9-c32b-5de3ab523672.jpg?w=840&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=ae235a1efa613887472ebd36c49036f4 840w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-84c5c765-de30-25c9-c32b-5de3ab523672.jpg?w=1100&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=70d7c8f4f164718f9566911bdb2d5d01 1100w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-84c5c765-de30-25c9-c32b-5de3ab523672.jpg?w=1650&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=5d05aac762b6919df163b99e62049bdb 1650w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-84c5c765-de30-25c9-c32b-5de3ab523672.jpg?w=2500&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=2c8d78a2fe69d5edf758ee2da0313965 2500w" />
</Frame>

#### Deeplinks

<Frame>
  <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-38b352a6-f2d5-0ae0-d93d-c5ae1d9e923d.jpg?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=fb20b2b8e82593de64864ef72401ed8a" data-og-width="982" width="982" data-og-height="753" height="753" data-path="image/uuid-38b352a6-f2d5-0ae0-d93d-c5ae1d9e923d.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-38b352a6-f2d5-0ae0-d93d-c5ae1d9e923d.jpg?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=52d289c824d75ba86554753a98aee9ca 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-38b352a6-f2d5-0ae0-d93d-c5ae1d9e923d.jpg?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=4be623b068f911e3a1e01c63620a2004 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-38b352a6-f2d5-0ae0-d93d-c5ae1d9e923d.jpg?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=fb4ab0633e619dec22061e05069fd2f0 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-38b352a6-f2d5-0ae0-d93d-c5ae1d9e923d.jpg?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=52801b6dbccf1f6c89dd732aa8e8ce8a 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-38b352a6-f2d5-0ae0-d93d-c5ae1d9e923d.jpg?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=0edf4393c3acf758a03bcbec52fb8216 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-38b352a6-f2d5-0ae0-d93d-c5ae1d9e923d.jpg?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=e1c6fa6eb82a3a76e32eaed3d37531eb 2500w" />
</Frame>

After selecting **Deeplink** from the **Add Content** menu, the following additional fields will appear:

* **Link to**: select an existing link from the dropdown or directly [create a new link](/agent-desk/virtual-agent/links#create-a-link "Create a Link").
  If you select an existing link, you can click **View link definition** to open the specific [link details](/agent-desk/virtual-agent/links#edit-a-link "Edit a Link") in a new tab.
* **Call to action**: define the accompanying text that the customer will click on in order to navigate to the link.
* **Hide button after new message**: choose to remove the deeplink after a new response appears to prevent users from navigating to the link past this node.

### Routing

The **Routing** section is where you will configure what happens after the content is sent.

You have two options:

* **Jump to node**
  Choosing to **Jump to node** allows you to define a default routing rule that will execute immediately after the node content has been delivered to the user.

<Frame>
  <img src="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-f74dc1d8-2dee-eee0-bea5-c75cd13dcb06.jpg?fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=e3160348a87c4f62797f41e60e3de808" data-og-width="1999" width="1999" data-og-height="662" height="662" data-path="image/uuid-f74dc1d8-2dee-eee0-bea5-c75cd13dcb06.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-f74dc1d8-2dee-eee0-bea5-c75cd13dcb06.jpg?w=280&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=fb6e693c915a84e31a068f3ef603ea1a 280w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-f74dc1d8-2dee-eee0-bea5-c75cd13dcb06.jpg?w=560&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=e56d9b4173ccb5b086332a41ecc97f1b 560w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-f74dc1d8-2dee-eee0-bea5-c75cd13dcb06.jpg?w=840&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=7e61fc52db94414d9e0219228240243a 840w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-f74dc1d8-2dee-eee0-bea5-c75cd13dcb06.jpg?w=1100&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=2382241472f41693063cec58c8469bee 1100w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-f74dc1d8-2dee-eee0-bea5-c75cd13dcb06.jpg?w=1650&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=02f361efe4963110a29614582b07bc7b 1650w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-f74dc1d8-2dee-eee0-bea5-c75cd13dcb06.jpg?w=2500&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=d98ed1eef2dd995351479c392b7a1d44 2500w" />
</Frame>

* **Wait for response**

  Choosing to **Wait for response** means that the virtual agent will pause until the customer responds, then attempt to classify their response and branch accordingly. When this option is selected, you'll need to specify the branches and [quick reply text](#quick-replies "Quick Replies") for each type of response you wish the virtual agent to classify. See [Branch Classifiers](#branch-classifiers "Branch Classifiers") section for more detailed information.

  <Frame>
    <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-de9b034a-8962-3900-0949-21b147a981f7.jpg?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=64f1a3f15c69d88de677670f95abc765" data-og-width="1402" width="1402" data-og-height="494" height="494" data-path="image/uuid-de9b034a-8962-3900-0949-21b147a981f7.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-de9b034a-8962-3900-0949-21b147a981f7.jpg?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=81470898bfaf7a6e602e0bfdea2bd601 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-de9b034a-8962-3900-0949-21b147a981f7.jpg?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=2e2aac834618a172303aa28d03afbf88 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-de9b034a-8962-3900-0949-21b147a981f7.jpg?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=9c143b165ccfb1b278cb8600107cbb29 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-de9b034a-8962-3900-0949-21b147a981f7.jpg?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=4054e0c0d6d73d80ef783a58e0b0d260 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-de9b034a-8962-3900-0949-21b147a981f7.jpg?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=8d29f70084a57a2b05d07296f6180635 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-de9b034a-8962-3900-0949-21b147a981f7.jpg?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=7e2fa76df4204daeb6ed2995d18a39f0 2500w" />
  </Frame>

Flows cannot end on a response node. To appropriately end a flow after a response node, please route to an [End node](#end-node "End Node").

#### Branch Classifiers

When **Wait for response** is selected for routing, you can define the branches for each type of response you wish the virtual agent to classify.

There are two types of branch classifiers that you can use:

* **System classifiers**
  ASAPP supports pre-trained system templates to classify free text user input. You can use branches like `CONFIRM` or `DENY` that are already trained by our system and are readily available for use for polar (yes/no) questions. You do not need to supply training utterances for system classifiers.

  <Frame>
    <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c020323d-4882-3db7-a342-d892c0cdbf46.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=9638e77574bb21821eabb8489f9dc9eb" data-og-width="762" width="762" data-og-height="820" height="820" data-path="image/uuid-c020323d-4882-3db7-a342-d892c0cdbf46.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c020323d-4882-3db7-a342-d892c0cdbf46.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=279a5410b4075fa39643596e52fc6643 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c020323d-4882-3db7-a342-d892c0cdbf46.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=7d17c7934afdc72f04161ffe0414b8e0 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c020323d-4882-3db7-a342-d892c0cdbf46.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=5db7fad8bf4837c67f4cd50f7b0d5783 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c020323d-4882-3db7-a342-d892c0cdbf46.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=3f8299d11c14c280618faec1ac75484c 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c020323d-4882-3db7-a342-d892c0cdbf46.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=5089afe98e55b6e5114207a36aa2540b 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c020323d-4882-3db7-a342-d892c0cdbf46.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=eef4e29d5cc85b344301793654610501 2500w" />
  </Frame>

* **Custom classifiers**
  If pre-trained classifiers do not meet your needs, define your own custom branches and supply training utterances. You must give your branch classifier a **Display Name** and supply at least five training utterances to train this custom classification. Learn more about how to best train your custom branches in the [Training response route](/agent-desk/virtual-agent/best-practices#2-training-response-routes "2. Training Response Routes") section.

<Frame>
  <img src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-1cff1b12-002a-49ee-254d-1a0a13a0faa2.gif?s=0715120cf8969daddfd3b89a453526b9" data-og-width="1039" width="1039" data-og-height="677" height="677" data-path="image/uuid-1cff1b12-002a-49ee-254d-1a0a13a0faa2.gif" data-optimize="true" data-opv="3" />
</Frame>

#### Quick Replies

For each branch classifier, you should define the corresponding **Quick Reply text**. These will appear in our SDKs (web, mobile) and third-party channels as tapable options.

<Frame>
  <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-f4cd3e23-d37a-355f-7005-60d313f6f8ac.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=b209ef8c0902453ff529bb434810849e" data-og-width="1878" width="1878" data-og-height="866" height="866" data-path="image/uuid-f4cd3e23-d37a-355f-7005-60d313f6f8ac.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-f4cd3e23-d37a-355f-7005-60d313f6f8ac.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=154fe5dfc278e19d544841a0d05db38b 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-f4cd3e23-d37a-355f-7005-60d313f6f8ac.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=a4aee86cff57ab9f3fbbcb5974df3c7e 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-f4cd3e23-d37a-355f-7005-60d313f6f8ac.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=c088469098c5832308ff61f01b9b2c4b 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-f4cd3e23-d37a-355f-7005-60d313f6f8ac.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=9342c9190ae05a05ea6c3a85fdf521b2 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-f4cd3e23-d37a-355f-7005-60d313f6f8ac.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=6f401cb256428af08c29af04a896b049 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-f4cd3e23-d37a-355f-7005-60d313f6f8ac.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=6da4c09af782f7e98402a0b7df137b56 2500w" />
</Frame>

### Advanced Settings

In the **Advanced Settings** section, you can set flow success reporting for the response node.

#### Flow Success

Flow success attempts to accurately measure whether a customer has successfully self-served through the virtual agent. You measure this by setting the appropriate flow reporting status on certain nodes within a flow. Learn more: [How do I determine flow success?](/agent-desk/virtual-agent/best-practices#measuring-virtual-agents "Measuring Virtual Agents")

To set flow reporting status for response nodes:

1. Toggle **Set flow reporting status** on.
2. By default, **Success** is selected for response nodes but this can be modified for your particular flow.

<Frame>
  <img src="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0f71f580-39ab-009d-9a6a-8fcc3dffbd8d.jpg?fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=977c08d85c5040ccc27e05ed1dca1788" data-og-width="1024" width="1024" data-og-height="287" height="287" data-path="image/uuid-0f71f580-39ab-009d-9a6a-8fcc3dffbd8d.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0f71f580-39ab-009d-9a6a-8fcc3dffbd8d.jpg?w=280&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=0433e9ce3734f0f1916621cbbea1b87a 280w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0f71f580-39ab-009d-9a6a-8fcc3dffbd8d.jpg?w=560&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=e53245f5ae17b9a64a24a536220c0f2b 560w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0f71f580-39ab-009d-9a6a-8fcc3dffbd8d.jpg?w=840&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=f730434910e1598f93257f1ee40d7606 840w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0f71f580-39ab-009d-9a6a-8fcc3dffbd8d.jpg?w=1100&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=6ad5bd2d928091c566533af1c83a8e2b 1100w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0f71f580-39ab-009d-9a6a-8fcc3dffbd8d.jpg?w=1650&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=0913c32de549f58d2c2be8b7c2ce4245 1650w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0f71f580-39ab-009d-9a6a-8fcc3dffbd8d.jpg?w=2500&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=1cc48546b66bbcc78f70c4f8261d2bd4 2500w" />
</Frame>

### Login Node

The **Login Node** enables customer authentication within a flow. In this node, you can define the following:

* **Content**
* **Routing**
* **Advanced Settings**

<Frame>
  <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d6a3bc59-4453-bb6d-5eb7-3ad75343e33f.jpg?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=54f911a82a3f64027d2d3f08b2a8a24d" data-og-width="775" width="775" data-og-height="718" height="718" data-path="image/uuid-d6a3bc59-4453-bb6d-5eb7-3ad75343e33f.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d6a3bc59-4453-bb6d-5eb7-3ad75343e33f.jpg?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=28b7f6b43acbc6444d0a05689e9d04ae 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d6a3bc59-4453-bb6d-5eb7-3ad75343e33f.jpg?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=aa74127114814eba2d2ffe21ce7c69bd 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d6a3bc59-4453-bb6d-5eb7-3ad75343e33f.jpg?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=bc2dc2b9ebb5968f60d0384f60c047ad 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d6a3bc59-4453-bb6d-5eb7-3ad75343e33f.jpg?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=327637f4f712c72fa79a7ca1bf7a908d 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d6a3bc59-4453-bb6d-5eb7-3ad75343e33f.jpg?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=90af97845fa5c7d48d80abf9ab7fe3f4 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d6a3bc59-4453-bb6d-5eb7-3ad75343e33f.jpg?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=447534e335a3950ea70272e09b79f68f 2500w" />
</Frame>

#### Content

The **Content** section allows you to define the text to be shown to the customer to accompany the login action. All login nodes will have default text which you can modify to suit your particular flow needs.

* **Message text**: Define the main text that will prompt the customer to login
* **Call to action**: Define the accompanying text that the customer will click on in order to login
* **Text sent to indicate that a login is in process**: customize the text that is sent after the customer has tried to log in.

In the flow graph, you can preview how the content will be displayed to the customer.

#### Routing

Flows cannot end on a login node. The **Routing** section is where you can configure what happens after a customer successfully logs in or optionally configure branches for exceptional conditions.

##### On login

In the **On login** section, you must define the default routing rule that will execute after the customer successfully logs in.

<Frame>
  <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4f888e5e-6173-307c-8153-6e6267fad35e.png?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=ce50c797f7a87f4b6d1cd3950dafe67e" data-og-width="1600" width="1600" data-og-height="426" height="426" data-path="image/uuid-4f888e5e-6173-307c-8153-6e6267fad35e.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4f888e5e-6173-307c-8153-6e6267fad35e.png?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=55dc433566e0f38382382dc940ed7557 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4f888e5e-6173-307c-8153-6e6267fad35e.png?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=71241e044cbaaa6406d0fb0f3fcaa8f6 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4f888e5e-6173-307c-8153-6e6267fad35e.png?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=9a4214ea722b1b4f10f82765990bc59d 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4f888e5e-6173-307c-8153-6e6267fad35e.png?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=1a363d630024fb898331d98d9cc16ab3 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4f888e5e-6173-307c-8153-6e6267fad35e.png?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=1efdef4c6565f379e1209fdf6b2cf473 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4f888e5e-6173-307c-8153-6e6267fad35e.png?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=167873d172776a96afb4442a1c0d4c88 2500w" />
</Frame>

##### On response

Similar to response nodes, you can optionally add response branches in the **On response** section to account for exceptional conditions that may occur when a customer is trying to authenticate, such as login errors or retries and refreshes.

Please see [Branch Classifiers](#branch-classifiers "Branch Classifiers") on the response node for more information on how to configure these routing rules.

<Frame>
  <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-dd1d24fc-c9d3-eb94-551f-0f484dfdfc7a.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=a5d602af063cb384ab96d92323d76dc8" data-og-width="1600" width="1600" data-og-height="675" height="675" data-path="image/uuid-dd1d24fc-c9d3-eb94-551f-0f484dfdfc7a.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-dd1d24fc-c9d3-eb94-551f-0f484dfdfc7a.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=e9e19ecc407e0c3857db20400ef1060a 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-dd1d24fc-c9d3-eb94-551f-0f484dfdfc7a.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=c66d9de13413a5285c56139229b58f08 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-dd1d24fc-c9d3-eb94-551f-0f484dfdfc7a.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=007869e4780465e48f3012c305275d3a 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-dd1d24fc-c9d3-eb94-551f-0f484dfdfc7a.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=4d326055084a4bb762b3c94addfaca7a 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-dd1d24fc-c9d3-eb94-551f-0f484dfdfc7a.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=993ffe950c1870eeb9c6cee015177c22 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-dd1d24fc-c9d3-eb94-551f-0f484dfdfc7a.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=351f32d90f60ad3cd25a03d26f58770f 2500w" />
</Frame>

##### Else

In the **Else** section, you can define what happens if login is unsuccessful and we do not recognize customer responses.

#### Advanced Settings

In **Advanced Settings**, you have the option to **Force reauthentication** which will prompt all customers to log in again, regardless of current authentication state.

### API Node

The API node allows you to use API fields dynamically in your flows. The data you retrieve on an API node can be used for two things:

1. **Displaying the data** on subsequent nodes.
2. **Routing to different nodes** based on the data.

#### Data Request

The **Data Request** section allows you to add data fields from an existing API integration.

<Frame>
  <img src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-1afa3ec6-da35-0ba0-403d-abcd778b2055.png?fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=b216702fb3a900f30062cc3c540a842a" data-og-width="383" width="383" data-og-height="417" height="417" data-path="image/uuid-1afa3ec6-da35-0ba0-403d-abcd778b2055.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-1afa3ec6-da35-0ba0-403d-abcd778b2055.png?w=280&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=0b99ff216f9e117d3d78acd4e69c2203 280w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-1afa3ec6-da35-0ba0-403d-abcd778b2055.png?w=560&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=28ab5ace3877f9c712503aec436c96f1 560w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-1afa3ec6-da35-0ba0-403d-abcd778b2055.png?w=840&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=63fc89f263bd72745e3768e03b46601b 840w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-1afa3ec6-da35-0ba0-403d-abcd778b2055.png?w=1100&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=9badb25b0468bc7cad2fb9e83bd53337 1100w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-1afa3ec6-da35-0ba0-403d-abcd778b2055.png?w=1650&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=d415744966455d3c218f3be11214c3e8 1650w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-1afa3ec6-da35-0ba0-403d-abcd778b2055.png?w=2500&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=7babc5e50ed8515834da30716a139c76 2500w" />
</Frame>

Select **Add data fields** to choose objects from existing integrations, which will allow you to add collections of data fields to the node. There is a search bar that allows you to easily search through the available fields.

<Frame>
  <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6bd04609-3365-b170-5abd-10e137481de3.png?fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=10cdb783b64d87f0c71a16ad6f672eff" data-og-width="1595" width="1595" data-og-height="927" height="927" data-path="image/uuid-6bd04609-3365-b170-5abd-10e137481de3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6bd04609-3365-b170-5abd-10e137481de3.png?w=280&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=7a5430df969e1cd99d9ff270e5d820dc 280w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6bd04609-3365-b170-5abd-10e137481de3.png?w=560&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=5fee7470624d75192cb6de385df3ad2e 560w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6bd04609-3365-b170-5abd-10e137481de3.png?w=840&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=71b7e7245f910272e82a87d41c4aa546 840w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6bd04609-3365-b170-5abd-10e137481de3.png?w=1100&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=ebfceb1d23a7b4f68c1a0f5625e2a0de 1100w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6bd04609-3365-b170-5abd-10e137481de3.png?w=1650&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=ba56f6d1d8dbd29b9f9571e17c799eff 1650w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6bd04609-3365-b170-5abd-10e137481de3.png?w=2500&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=c2d8244dc5f939a84774f11455c543f4 2500w" />
</Frame>

After you select objects, all of the referenced fields will automatically populate in the API node.

In addition to objects and arrays, you can request actions.

<Note>
  You can only select one action per node; selecting an action will automatically disable the selection of additional objects, actions, and arrays.
</Note>

#### Input Parameters

Some actions require input parameters for the API call, which you can define in AI-Console. In the node edit panel, you can see a field for defining parameters that will be passed as part of the API call. This field leverages curly brackets: click the **curly bracket** icon or select the **shift>\{** or **}** keys to choose the API value to pass as an input parameter.

<Note>
  Only valid data can be used for input parameters; objects or arrays will not be surfaced through curly brackets.
</Note>

<Frame>
  <img src="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-02e0a722-3e1c-4c35-bffd-3c9a83368472.png?fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=09f1d549d236959d232ea97a72ba34b8" data-og-width="1999" width="1999" data-og-height="1250" height="1250" data-path="image/uuid-02e0a722-3e1c-4c35-bffd-3c9a83368472.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-02e0a722-3e1c-4c35-bffd-3c9a83368472.png?w=280&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=cf765f9cd2a06e51b9e3f33f62e38448 280w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-02e0a722-3e1c-4c35-bffd-3c9a83368472.png?w=560&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=cf2c856e77f828045fa426687bd54662 560w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-02e0a722-3e1c-4c35-bffd-3c9a83368472.png?w=840&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=a671dff3e7e897f997f3ae6b6bcbaa27 840w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-02e0a722-3e1c-4c35-bffd-3c9a83368472.png?w=1100&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=4a4b8645a75cb995f40de12f12b745c6 1100w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-02e0a722-3e1c-4c35-bffd-3c9a83368472.png?w=1650&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=4859206f6a60c3e1c9f40120ddb1f5d8 1650w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-02e0a722-3e1c-4c35-bffd-3c9a83368472.png?w=2500&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=6aa8c186229c20a445d2aeffb4e6d9c8 2500w" />
</Frame>

#### Displaying Data

You are easily able to display API fields from an API node in subsequent response nodes. This field leverages curly brackets: click the **curly bracket** icon or select the **shift>\{** or **}** keys in the Response Node Content section to choose API values to display, which will render as a dynamic API field in the flow graph.

<Frame>
  <img src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-269410d7-d017-6c4b-df6f-f4a8ec743a8f.png?fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=8b641aba44c2c9129af4c0de2a6079e4" data-og-width="1782" width="1782" data-og-height="884" height="884" data-path="image/uuid-269410d7-d017-6c4b-df6f-f4a8ec743a8f.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-269410d7-d017-6c4b-df6f-f4a8ec743a8f.png?w=280&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=bd1a424f1342e1eea004fcdfedafa728 280w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-269410d7-d017-6c4b-df6f-f4a8ec743a8f.png?w=560&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=bc507a8dc169da8ba05b2fb50ecb418b 560w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-269410d7-d017-6c4b-df6f-f4a8ec743a8f.png?w=840&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=074651793eb1d76666572ea56ec51d94 840w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-269410d7-d017-6c4b-df6f-f4a8ec743a8f.png?w=1100&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=785a1aba9da90fbad56675e6a892102b 1100w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-269410d7-d017-6c4b-df6f-f4a8ec743a8f.png?w=1650&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=cc61fd07d756db53fbccb221482d0bce 1650w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-269410d7-d017-6c4b-df6f-f4a8ec743a8f.png?w=2500&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=cfe98e9e32499cc52021d9c4caadf58a 2500w" />
</Frame>

When you click on the API field itself, data format options appear that will allow you to specify exactly what format to display to the end user.

<Frame>
  <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e456368d-92a6-a6ee-0df0-6df089265ac0.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=cc07a29fcdfde6724123dabb0c381e51" data-og-width="384" width="384" data-og-height="388" height="388" data-path="image/uuid-e456368d-92a6-a6ee-0df0-6df089265ac0.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e456368d-92a6-a6ee-0df0-6df089265ac0.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=2ceee270a85f2eba9266436983599845 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e456368d-92a6-a6ee-0df0-6df089265ac0.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=752941e6fd03d8cceef4cfb5f437ce31 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e456368d-92a6-a6ee-0df0-6df089265ac0.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=9b834401cabdbe037815c127037b78e1 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e456368d-92a6-a6ee-0df0-6df089265ac0.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=81235fc09c97aaf515c3be9e47d733b3 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e456368d-92a6-a6ee-0df0-6df089265ac0.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=f1e8e070adaef65a14fc06077059f0af 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e456368d-92a6-a6ee-0df0-6df089265ac0.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=3df472200c260c701bf1fc4a3e924af0 2500w" />
</Frame>

#### Routing to Different Nodes

Routing and data operators allow you to specify different flow branching based on what is returned from an API. This leverages the same framework as routing on other nodes, but provides additional functionality around operators to give you flexibility in configuring routing conditions.

<Frame>
  <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-859bd96a-74c6-3435-abfd-d39baf90ffa0.png?fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=88d4b78b211f8ef705d5affb29b57bdf" data-og-width="461" width="461" data-og-height="580" height="580" data-path="image/uuid-859bd96a-74c6-3435-abfd-d39baf90ffa0.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-859bd96a-74c6-3435-abfd-d39baf90ffa0.png?w=280&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=4133dff5a398d5bbcb031c77d62c2ae6 280w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-859bd96a-74c6-3435-abfd-d39baf90ffa0.png?w=560&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=d482a6d989ef68df1631dbc2d6ba00d5 560w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-859bd96a-74c6-3435-abfd-d39baf90ffa0.png?w=840&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=18eb202a941cdb8d51393c519f97ae11 840w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-859bd96a-74c6-3435-abfd-d39baf90ffa0.png?w=1100&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=0ac8331770f00ff179cd0541dd4014b2 1100w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-859bd96a-74c6-3435-abfd-d39baf90ffa0.png?w=1650&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=dc9289a36eae2561489db44716de0924 1650w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-859bd96a-74c6-3435-abfd-d39baf90ffa0.png?w=2500&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=bd47a7db0871fd2d02c0e4fe69f5653e 2500w" />
</Frame>

Operators allow you to contextually define conditions to route on.

#### Error Handling

API nodes provide default error handling, but you are able to create custom error handling on the node itself if desired. You can specify where a user should be directed in the event of an error with the API call.

<Frame>
  <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9bbe352a-b20c-b737-ee22-76aa11d6bc6e.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=e34c17eb8975bd2d55f9e1461bd60b4c" data-og-width="382" width="382" data-og-height="367" height="367" data-path="image/uuid-9bbe352a-b20c-b737-ee22-76aa11d6bc6e.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9bbe352a-b20c-b737-ee22-76aa11d6bc6e.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=61ca48d905f8c611466346d3f87db9b0 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9bbe352a-b20c-b737-ee22-76aa11d6bc6e.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=6caf0c68a5177ef0e4cb8b0fec7fb38d 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9bbe352a-b20c-b737-ee22-76aa11d6bc6e.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=6da79538fb627d49754d62b8dcbd1117 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9bbe352a-b20c-b737-ee22-76aa11d6bc6e.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=2bba817813171fbfd9c30f07ce6bc158 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9bbe352a-b20c-b737-ee22-76aa11d6bc6e.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=5d15bd17727d218ccea020b55c147b75 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9bbe352a-b20c-b737-ee22-76aa11d6bc6e.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=f7599f1a4eb9152adf8344a4d98a6bc0 2500w" />
</Frame>

#### API Library

API fields are available under the integrations menu. In this page, you can view and search through all available objects and associated data fields.

### Redirect Node

The **Redirect Node** serves to link flows with one another by directing the customer to a separate flow. A Redirect Node does not display content to the customer.

In this node, you can define the following:

* **Destination**
* **Routing**
* **Advanced Settings**

<Frame>
  <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7cd585e4-f3dc-f4f5-7f0d-959444c1e7d7.jpg?fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=44f4a9fb18124c0b56b3bc21f001a096" data-og-width="775" width="775" data-og-height="676" height="676" data-path="image/uuid-7cd585e4-f3dc-f4f5-7f0d-959444c1e7d7.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7cd585e4-f3dc-f4f5-7f0d-959444c1e7d7.jpg?w=280&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=e81f43627b2b1d50c3dfc6f5d570acee 280w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7cd585e4-f3dc-f4f5-7f0d-959444c1e7d7.jpg?w=560&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=45087602346f6253aedc51aeb2fe1ac0 560w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7cd585e4-f3dc-f4f5-7f0d-959444c1e7d7.jpg?w=840&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=23406e813a625aab16e3f17513882f38 840w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7cd585e4-f3dc-f4f5-7f0d-959444c1e7d7.jpg?w=1100&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=e7621c6ee2bc2f582d737f82f7c3536a 1100w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7cd585e4-f3dc-f4f5-7f0d-959444c1e7d7.jpg?w=1650&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=86b7a1b325a3f518a3e7bf3b4bf4a1d0 1650w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7cd585e4-f3dc-f4f5-7f0d-959444c1e7d7.jpg?w=2500&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=32390128a24470ff669727f606ba089b 2500w" />
</Frame>

#### Destination

The **Destination** section allows you to define where to redirect the customer. You can redirect to an existing **flow** or an **intent**.

* Select **Flow** to redirect to an individual flow destination.
* Select **Intent** to redirect the customer to solve for a broader issue intent that may route them to different flows depending on the [intent routing rules](/agent-desk/virtual-agent/intent-routing "Intent Routing").

Depending on the option you select, you will be able to select the destination flow or intent from the dropdown.

#### Routing (Return Upon Completion)

Redirect nodes can end your flow or you can choose to have the customer return your flow after the destination flow has completed. To do so, toggle on **Return upon completion**. After doing so, you can define the default routing rule that will execute upon customer return.

### Agent Node

The **Agent Node** enables you to direct the customer to an agent queue in order to help resolve their issue. The data associated with this customer will be used to determine the live agent queue to put them in.

#### Advanced Settings

In the Advanced Settings section, you can set flow success reporting for the agent node.

##### Flow Success

Flow success attempts to accurately measure whether a customer has successfully self-served through the virtual agent. This is measured by setting the appropriate flow reporting status on certain nodes within a flow. Learn more: [How do I determine flow success?](/agent-desk/virtual-agent/best-practices#measuring-virtual-agents "Measuring Virtual Agents")

For agent nodes, this is always considered a failure.

To set flow reporting status for agent nodes:

1. Toggle **Set flow reporting status** on.
2. By default, **Failure** will be selected for agent nodes

<Frame>
  <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-59f2fa3b-2f13-9a04-9e50-9145adfe99ff.jpg?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=5a1dc00f12640f4057c0be316345903e" data-og-width="841" width="841" data-og-height="494" height="494" data-path="image/uuid-59f2fa3b-2f13-9a04-9e50-9145adfe99ff.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-59f2fa3b-2f13-9a04-9e50-9145adfe99ff.jpg?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=2bcefe460524e127881720adf776043b 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-59f2fa3b-2f13-9a04-9e50-9145adfe99ff.jpg?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=087dcc652dd64aa39fe9dc062b8fc370 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-59f2fa3b-2f13-9a04-9e50-9145adfe99ff.jpg?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=4cd088cbb7e79497b7ca9008c72f1e22 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-59f2fa3b-2f13-9a04-9e50-9145adfe99ff.jpg?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=d31612ca7daabb58a930c3f0b9fb5282 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-59f2fa3b-2f13-9a04-9e50-9145adfe99ff.jpg?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=eb20da5913c0d9dab393e406ddc4fd62 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-59f2fa3b-2f13-9a04-9e50-9145adfe99ff.jpg?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=e261fea7465a3c66c35ce6e44010b068 2500w" />
</Frame>

### End Node

The **End Node** wraps up the conversation by confirming whether the customer needs additional help.

#### Advanced Settings

In the **Advanced Settings** section, you can select the end Semantic Response Score (SRS) options (see below) for your flow.

By default, all three options will be selected when an end node is added, thus presenting all three options for the customer to select from. You can expand the section to modify these options to present to the customer.

##### End SRS Options

At the end of a flow, the virtual agent will ask the customer: "Is there anything else we can help you with today?"\*

After the above message is sent, there are three options available for the customer to select from:

* **"Thanks, I'm all set"**
  A customer selecting this **positive** option will prompt the virtual agent to wrap up and resolve the issue.
* **"I have another question"**
  A customer selecting this **neutral** option will prompt the virtual agent to ask the customer what their question is.
* **"My question has not been answered"**
  A customer selecting this **negative** option will prompt the virtual agent to escalate the customer into agent chat to help resolve their issue.
  \*Exact end SRS options and text may vary. Please contact your ASAPP team for more details.

<Frame>
  <img src="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-015c83bb-4604-d342-9502-495ecdfe6b53.jpg?fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=930d0504c352ca9a9980cd450c61ad29" data-og-width="1762" width="1762" data-og-height="1110" height="1110" data-path="image/uuid-015c83bb-4604-d342-9502-495ecdfe6b53.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-015c83bb-4604-d342-9502-495ecdfe6b53.jpg?w=280&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=bbd86837b0cea5dd5d7c40aee300c9bb 280w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-015c83bb-4604-d342-9502-495ecdfe6b53.jpg?w=560&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=be162b0590a4d82067eb08702b89dbb9 560w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-015c83bb-4604-d342-9502-495ecdfe6b53.jpg?w=840&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=afd000c3e857711025434b666bb16847 840w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-015c83bb-4604-d342-9502-495ecdfe6b53.jpg?w=1100&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=ff81f28f9c50dd8579e75cb399eab72f 1100w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-015c83bb-4604-d342-9502-495ecdfe6b53.jpg?w=1650&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=ebe278fb2d30eff2161946db9670345a 1650w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-015c83bb-4604-d342-9502-495ecdfe6b53.jpg?w=2500&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=9362e69ba2fe26891d48a844f8ac96cd 2500w" />
</Frame>

### Logic Nodes

The **Logic Node** enables you to define a “rule” or “logic” by which a flow should branch off based on different conditions. This gives you the ability to create more dynamic flows that can adapt to different customer inputs or other conversational context.

For example, a Logic Node can evaluate if a user's `zipcode` equals `New York`:

* If true, the flow continues to Message Node 1 ("Area is eligible for discount")
* Otherwise, it goes to Message Node 2 ("Area is not eligible for a discount")

<Frame>
  <img src="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/logic-nodes.png?fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=c1f703b3fb799c6e0af2a5dfde135a7f" data-og-width="1290" width="1290" data-og-height="914" height="914" data-path="images/messaging-platform/logic-nodes.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/logic-nodes.png?w=280&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=6a4d4ba04284b8129987f59466460db9 280w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/logic-nodes.png?w=560&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=9ca1b0b36d03865350f5b63c61291660 560w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/logic-nodes.png?w=840&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=d8c56e5d654d5caa9e1f64dcbc31a26e 840w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/logic-nodes.png?w=1100&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=a41c9945903446a8f6d5099157cd5885 1100w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/logic-nodes.png?w=1650&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=a10c5b244f931c857d8cef480ef71586 1650w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/logic-nodes.png?w=2500&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=2eb0fb84825c79a438cb037f0e8b0818 2500w" />
</Frame>

## Quick Start: Flows

### Create Flow

<Frame>
  <img src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-23846669-6400-d259-9dd6-c05a934628c4.png?fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=c0742ee5cfa528d32deec5fb67ca7a79" data-og-width="1104" width="1104" data-og-height="744" height="744" data-path="image/uuid-23846669-6400-d259-9dd6-c05a934628c4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-23846669-6400-d259-9dd6-c05a934628c4.png?w=280&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=cc018970bc991d0c7b45ce521f2f95b1 280w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-23846669-6400-d259-9dd6-c05a934628c4.png?w=560&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=0ecdf04d24fbe411b465413f2fedd76a 560w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-23846669-6400-d259-9dd6-c05a934628c4.png?w=840&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=d99a5df5cfc7fa23561e46a140a2c64a 840w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-23846669-6400-d259-9dd6-c05a934628c4.png?w=1100&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=96d5e75e3e83f96a8b3c6ea2869123e2 1100w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-23846669-6400-d259-9dd6-c05a934628c4.png?w=1650&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=dd455bb3fd11e496313b7366087984f1 1650w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-23846669-6400-d259-9dd6-c05a934628c4.png?w=2500&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=700f1e4eec0a809eb7269a4274806a53 2500w" />
</Frame>

Click **Create** to trigger a dialog for creating a new flow. The following data must be provided:

* **Name:** Give a unique name for your flow, using letters and numbers only.
* **Description:** Give a brief description of the purpose of the flow.

<Tip>
  Avoid vague flow names. Using clear names & descriptions allow others to quickly distinguish the purpose of your flow. We recommend following an "Objective +**Topic**" naming convention, such as: Find **Food** or Pay **Bill**.
</Tip>

Click **Next** to go to the flow builder where you will design and build your flow using the various [node types](#node-types "Node Types").

### Preview Flow

You can preview your flow as you are building it!

In the toolbar, select the **eye** icon to open the in-line preview. This panel will then allow you to preview the version of the flow that is currently displayed. As you are actively editing a flow, select this icon at any time to preview your progress.

<Frame>
  <img src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2b6a0023-418f-349a-12de-97db59756c41.gif?s=e07935d1f2cfb56e026f84ac90bfc470" data-og-width="1224" width="1224" data-og-height="702" height="702" data-path="image/uuid-2b6a0023-418f-349a-12de-97db59756c41.gif" data-optimize="true" data-opv="3" />
</Frame>

To preview a previously saved version of the flow, navigate to the flow version in the [version dropdown](#version-indicators "Version Indicators"), then click the **eye** icon to preview.

#### Preview Capabilities

There are a few capabilities to leverage in preview:

* **Re-setting:** puts you back to the first node of the flow and allows you to test it again.
* **Debug information:** opens a panel that provides more detailed insights into where you are in a flow and the associated metadata with your preview.
* **Close:** close the in-line preview.

<Frame>
  <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-dec4da7d-9bec-9a29-7db9-6c4753edefd4.gif?s=9ec5359c9662601c0c1471e8d34c48cc" data-og-width="1354" width="1354" data-og-height="703" height="703" data-path="image/uuid-dec4da7d-9bec-9a29-7db9-6c4753edefd4.gif" data-optimize="true" data-opv="3" />
</Frame>

#### Preview with Mocked Data

The real time preview also has the ability to preview integrated flows using mocked data. By mocking data directly in the preview, you can test different flow paths based on the different values an API can return.

1. Define Request
   * You can define if the request is a success or failure when previewing. Each API node is treated as a separate call in the preview experience.
   <Frame>
     <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-cc121ffe-4697-fdb1-03b1-2980bac31e27.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=eeb528ecd0173f84f7bbd3023603d513" data-og-width="930" width="930" data-og-height="1730" height="1730" data-path="image/uuid-cc121ffe-4697-fdb1-03b1-2980bac31e27.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-cc121ffe-4697-fdb1-03b1-2980bac31e27.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=8fbf745e03d0ba61591eef29a03be808 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-cc121ffe-4697-fdb1-03b1-2980bac31e27.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=466dbb0e47fd114cf87465580dda5d9f 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-cc121ffe-4697-fdb1-03b1-2980bac31e27.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=c6047afbc4afd8e78b9b799b2be597f3 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-cc121ffe-4697-fdb1-03b1-2980bac31e27.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=f870754bb18919be0f77b7a69747acb0 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-cc121ffe-4697-fdb1-03b1-2980bac31e27.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=3015cb8b484e34449efdc2009ef728ff 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-cc121ffe-4697-fdb1-03b1-2980bac31e27.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=a225933aa221a96610a01f264b217bc2 2500w" />
   </Frame>
2. View and Edit Mock Data Fields

   * For a successful API call, you can view and edit mock data fields, which will inform the subsequent flow path in the preview.
   * By default, all returned values are selected and pre-filled. Values set in the preview will be cached until you leave the flow builder, to prevent the need to re-enter each mock data form.

   <Frame>
     <img src="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-fe3f5af7-9ac8-9360-a9a3-e60a0df2dd16.png?fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=7155fcf2560bb5b9288320538052c287" data-og-width="930" width="930" data-og-height="1730" height="1730" data-path="image/uuid-fe3f5af7-9ac8-9360-a9a3-e60a0df2dd16.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-fe3f5af7-9ac8-9360-a9a3-e60a0df2dd16.png?w=280&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=3919d47dccd02f5217355bc3829a9871 280w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-fe3f5af7-9ac8-9360-a9a3-e60a0df2dd16.png?w=560&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=7d5840092882b35c0a4477bde3b40e82 560w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-fe3f5af7-9ac8-9360-a9a3-e60a0df2dd16.png?w=840&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=e1dece52b7a944f9910c75728352eeef 840w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-fe3f5af7-9ac8-9360-a9a3-e60a0df2dd16.png?w=1100&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=412bafff76b8ddf76626c6ff64eefbe3 1100w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-fe3f5af7-9ac8-9360-a9a3-e60a0df2dd16.png?w=1650&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=3f710783d689cb1bd76e4f2e65d3377b 1650w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-fe3f5af7-9ac8-9360-a9a3-e60a0df2dd16.png?w=2500&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=57cf4d40a81c4182f070f1f771be43c4 2500w" />
   </Frame>

### Save New Flow

When you are building a new flow, the following buttons will display in the toolbar:

* **Discard changes:** remove all unsaved changes made to the flow.
* **Save:** save changes to the flow as a new version or override an existing version.

<Frame>
  <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a6181873-136b-6d04-a38a-242e99e922e0.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=88377fba64cf8b0378976437074de9a6" data-og-width="1999" width="1999" data-og-height="87" height="87" data-path="image/uuid-a6181873-136b-6d04-a38a-242e99e922e0.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a6181873-136b-6d04-a38a-242e99e922e0.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=361ad90b1ddad224085dc95841b8c251 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a6181873-136b-6d04-a38a-242e99e922e0.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=4bea58cf64863d75f7807b0cb8176066 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a6181873-136b-6d04-a38a-242e99e922e0.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=18e1cdf86c77edd24c0bd1deaa791d19 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a6181873-136b-6d04-a38a-242e99e922e0.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=0b15d1c6f57e1ce7e04b4dd8f03a2721 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a6181873-136b-6d04-a38a-242e99e922e0.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=101d8918856b8eb302de051178a9f794 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a6181873-136b-6d04-a38a-242e99e922e0.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=0ce360030136983949303c4df9b7b395 2500w" />
</Frame>

To save your new flow, select **Save**.

### Deploy New Flow

Newly created flows (i.e. the initial version) will **immediately deploy to test environments and production**. These new flows can be deployed without harm since customers will not be able to invoke the flow unless there are incoming routes due to [intent routing](/agent-desk/virtual-agent/intent-routing "Intent Routing").

<Frame>
  <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8b66727a-30bd-703f-b094-cbd7ead452eb.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=b9ee9361edb6f3fd8ba0d08847ff375e" data-og-width="946" width="946" data-og-height="750" height="750" data-path="image/uuid-8b66727a-30bd-703f-b094-cbd7ead452eb.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8b66727a-30bd-703f-b094-cbd7ead452eb.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=5e1813d45e03d0282e6b039f1d668075 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8b66727a-30bd-703f-b094-cbd7ead452eb.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=bccb7b08058abd01676167896b0d6246 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8b66727a-30bd-703f-b094-cbd7ead452eb.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=310858554d9340f4f92080bb5b201893 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8b66727a-30bd-703f-b094-cbd7ead452eb.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=2463b8cdddd458d687274effb8f1b502 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8b66727a-30bd-703f-b094-cbd7ead452eb.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=e36416467468b551da0fa51c22d3d921 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8b66727a-30bd-703f-b094-cbd7ead452eb.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=3cdced370940fdb5c876a4597db21dd7 2500w" />
</Frame>

### Test New Flow

After deploying your flow to test, navigate to your respective test environment in order to verify your flow changes:

1. In the upper right corner of the toolbar, click the icon for **More actions**.
2. Select **Copy link to demo**.
3. Copy the **Flow Shortcut**.
4. Choose to **Go to demo env.**
5. Once there, select the chat bubble and paste the flow shortcut into the text entry to start testing your flow.

<Frame>
  <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-816ae3d2-cfd5-ee62-9836-a9cda9b906e0.gif?s=ffac4b0dfc5f6135d410b84a510eadb0" data-og-width="1224" width="1224" data-og-height="702" height="702" data-path="image/uuid-816ae3d2-cfd5-ee62-9836-a9cda9b906e0.gif" data-optimize="true" data-opv="3" />
</Frame>

### Edit & Save New Version

You can make changes to your new flow by selecting a node and making edits in the [Node Configuration Panel](#node-configuration-panel "Node Configuration Panel").

Once you are ready to save your changes, select **Save**. Since the current version of the flow is already deployed to production, you will **NOT** be able to save over the current version and **MUST** save as a new version to prevent unintentional changes to flows in production.

<Frame>
  <img src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-3111bc91-7f92-b557-7111-4b8dd2be242b.png?fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=7bc951c249b746fe0fd9e9b523a56225" data-og-width="946" width="946" data-og-height="548" height="548" data-path="image/uuid-3111bc91-7f92-b557-7111-4b8dd2be242b.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-3111bc91-7f92-b557-7111-4b8dd2be242b.png?w=280&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=3341cf06ab6a8df995eaee98233fa81c 280w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-3111bc91-7f92-b557-7111-4b8dd2be242b.png?w=560&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=abe59e4f20c5b22df56099bf1f96fc3c 560w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-3111bc91-7f92-b557-7111-4b8dd2be242b.png?w=840&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=e7052dbeeb62c4235ab363897b9c2425 840w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-3111bc91-7f92-b557-7111-4b8dd2be242b.png?w=1100&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=39033d720792a8a5f767984b5f8a9341 1100w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-3111bc91-7f92-b557-7111-4b8dd2be242b.png?w=1650&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=d5d654693fa06752cdea59b537a27d94 1650w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-3111bc91-7f92-b557-7111-4b8dd2be242b.png?w=2500&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=7a798e8a0de86af816a0835033ae23d0 2500w" />
</Frame>

For future flow versions that are not deployed to production, you will be able to save your changes as a **new flow version** or to overwrite the **current flow version**.

<Frame>
  <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-515f5f10-8a76-5910-5f97-2dc89d381378.png?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=6a8a7eedca5208f743cf0ed5472c7582" data-og-width="950" width="950" data-og-height="562" height="562" data-path="image/uuid-515f5f10-8a76-5910-5f97-2dc89d381378.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-515f5f10-8a76-5910-5f97-2dc89d381378.png?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=fda5bf657505ebecad2be1dfad2e77a1 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-515f5f10-8a76-5910-5f97-2dc89d381378.png?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=55f20508f57c568a664b2f178b0f8dd9 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-515f5f10-8a76-5910-5f97-2dc89d381378.png?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=dfe747d8b76003cb7869aae685e0c7e8 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-515f5f10-8a76-5910-5f97-2dc89d381378.png?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=b8cf36997e9274aa605031cae10b0661 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-515f5f10-8a76-5910-5f97-2dc89d381378.png?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=4ea358359b7df866fbbf3eff439abcc3 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-515f5f10-8a76-5910-5f97-2dc89d381378.png?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=1c098cc586cbc560f8edab0a715e6ee6 2500w" />
</Frame>

### Deploy Version to Test

After saving, you will be directed to **Manage Versions** where you will manage which flow version is deployed to test environments and to production..

<Caution>
  All flows should be verified in test environments, such as demo or pre-production environments before production. Therefore, new flow versions **MUST** be deployed to test **PRIOR** to [deployment in production](#deploy-version-to-prod "Deploy Version to Prod").
</Caution>

To deploy a flow version to test environments:

1. Select the new version you want to deploy in the version dropdown for **Test**.
2. After selection, click **Save**.
3. Flow version will deploy to all lower test environments within 5-10 minutes.

<Frame>
  <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-75491e14-8dfe-c56c-c837-a68c6e2c37e8.png?fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=140138e8797d462a2dbedaa4ea771068" data-og-width="950" width="950" data-og-height="750" height="750" data-path="image/uuid-75491e14-8dfe-c56c-c837-a68c6e2c37e8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-75491e14-8dfe-c56c-c837-a68c6e2c37e8.png?w=280&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=6d23f53de3104033e7ac05089bcb2ab1 280w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-75491e14-8dfe-c56c-c837-a68c6e2c37e8.png?w=560&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=ef52f82ecedd69e5e710975e05feaac9 560w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-75491e14-8dfe-c56c-c837-a68c6e2c37e8.png?w=840&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=75fec0127fdefeff8221edfed0e1fc47 840w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-75491e14-8dfe-c56c-c837-a68c6e2c37e8.png?w=1100&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=8017cfd3cf9e11b529fcca6f5fb72564 1100w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-75491e14-8dfe-c56c-c837-a68c6e2c37e8.png?w=1650&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=e13cef138ad446328b8b22af82de7111 1650w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-75491e14-8dfe-c56c-c837-a68c6e2c37e8.png?w=2500&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=8dde3776718290be54303adceb90284b 2500w" />
</Frame>

### Test Version

After deploying your flow to test, navigate to your respective test environment in order to verify your flow changes:

1. In the upper right corner of the toolbar, click the icon for **More actions**.
2. Select **Copy link to demo**.
3. Copy the **Flow Shortcut**.
4. Choose to **Go to demo env**.
5. Once there, select the chat bubble and paste the flow shortcut into the text entry to start testing your flow.

<Frame>
  <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bd6031aa-5804-3dbe-9039-33c57496abd3.gif?s=c6553f9f5c561e1e075dc9350685d5c2" data-og-width="1224" width="1224" data-og-height="702" height="702" data-path="image/uuid-bd6031aa-5804-3dbe-9039-33c57496abd3.gif" data-optimize="true" data-opv="3" />
</Frame>

### Deploy Version to Prod

After verifying the expected flow behavior in **Test**, you can deploy the flow version to production, which will impact customers if there the [flow is routed from an intent](/agent-desk/virtual-agent/intent-routing "Intent Routing"):

1. Select the version you want to deploy in the version dropdown for **Prod**.
2. After selection, click **Save**.
3. Flow version will deploy to Production within 5-10 minutes.

<Frame>
  <img src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-26bbd80b-9cc8-e943-f1b4-b71f99d1a049.png?fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=d90abc06d39ca7c693557ecd00af4759" data-og-width="942" width="942" data-og-height="754" height="754" data-path="image/uuid-26bbd80b-9cc8-e943-f1b4-b71f99d1a049.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-26bbd80b-9cc8-e943-f1b4-b71f99d1a049.png?w=280&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=34f20906fd0463ea441f296967226376 280w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-26bbd80b-9cc8-e943-f1b4-b71f99d1a049.png?w=560&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=5b048867220cc4b82b88247be20e6ffd 560w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-26bbd80b-9cc8-e943-f1b4-b71f99d1a049.png?w=840&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=9df2a78b6f95280b7407802d6c88bc86 840w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-26bbd80b-9cc8-e943-f1b4-b71f99d1a049.png?w=1100&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=c7fed5dd5608d0e6e4b26bd23ba2939d 1100w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-26bbd80b-9cc8-e943-f1b4-b71f99d1a049.png?w=1650&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=918d890dc1893c5c79a9654edb911b47 1650w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-26bbd80b-9cc8-e943-f1b4-b71f99d1a049.png?w=2500&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=528ab44612dca414d1c9084276c405de 2500w" />
</Frame>

### Manage Versions

When you are simply viewing a flow without making any changes, **Manage Versions** will always be at the top of the toolbar for you to manage flow version deployments. Upon selection, the versions that are currently deployed to Test and Prod environments will display, which you can edit as appropriate.

<Frame>
  <img src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-259c265c-031d-8f63-ee2f-aadc8e9760a9.png?fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=8cc1b060e2052c2c5a9b1e6dd163c736" data-og-width="946" width="946" data-og-height="762" height="762" data-path="image/uuid-259c265c-031d-8f63-ee2f-aadc8e9760a9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-259c265c-031d-8f63-ee2f-aadc8e9760a9.png?w=280&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=e2c7062e61deefdabc218a0c033c13b4 280w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-259c265c-031d-8f63-ee2f-aadc8e9760a9.png?w=560&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=3ab1fde913292699ac52ffce6b0b0df1 560w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-259c265c-031d-8f63-ee2f-aadc8e9760a9.png?w=840&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=6d3ddbedd9946e8802882616123501aa 840w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-259c265c-031d-8f63-ee2f-aadc8e9760a9.png?w=1100&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=16720aa7fabc6e8c6af285c7e32d2e5f 1100w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-259c265c-031d-8f63-ee2f-aadc8e9760a9.png?w=1650&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=a3a3d9ed4fc22f15b60d85e8e433806d 1650w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-259c265c-031d-8f63-ee2f-aadc8e9760a9.png?w=2500&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=0930f2f545a3a3c3b17437c72ef2b3e9 2500w" />
</Frame>

In addition to version deployments, you can view any existing [intents that route to this flow](/agent-desk/virtual-agent/intent-routing "Intent Routing") in **Incoming Routes**. Upon selection, you will be directed to the specific [intent detail](/agent-desk/virtual-agent/intent-routing#intent-routing-detail-page "Intent Routing Detail Page") page where you can view the intent routing rules.

<Frame>
  <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d955ad2e-56f9-1792-02cc-85b016188de7.gif?s=ab950a3e5adfc8e2c0b5dff3b981613e" data-og-width="1224" width="1224" data-og-height="702" height="702" data-path="image/uuid-d955ad2e-56f9-1792-02cc-85b016188de7.gif" data-optimize="true" data-opv="3" />
</Frame>

### Navigate Flow Versions

Many flows may iterate through multiple versions. You can toggle to view previous flow versions using the version dropdown:

1. Next to the flow name, click the version dropdown in the toolbar.
2. Selecting the version you want to view.
3. Once selected, the version details will display in the flow graph.
4. You can click any node to start editing that specific flow version.

<Frame>
  <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-ca2f1cdb-930a-b714-013b-9ae194266186.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=d155979dd214f1b470cf6b89a76daa44" data-og-width="682" width="682" data-og-height="478" height="478" data-path="image/uuid-ca2f1cdb-930a-b714-013b-9ae194266186.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-ca2f1cdb-930a-b714-013b-9ae194266186.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=a92165947775c89b31e265f37ef74c47 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-ca2f1cdb-930a-b714-013b-9ae194266186.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=02d068f83f2953497b9f6b4e9dc77f07 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-ca2f1cdb-930a-b714-013b-9ae194266186.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=ad59c5dbaecbe15a79af4b556aabdc0b 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-ca2f1cdb-930a-b714-013b-9ae194266186.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=1df59b72a354d5c9ffbfc30074f60543 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-ca2f1cdb-930a-b714-013b-9ae194266186.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=5911f12cbd97f253f04aec1779a6dfad 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-ca2f1cdb-930a-b714-013b-9ae194266186.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=c761f6078c73b802e35b1e174dbdf247 2500w" />
</Frame>

#### Version Indicators

As flow versions are iteratively edited and deployed to Test and Prod, there are a few indicators in the toolbar to help the you quickly understand which version is being edited and which versions have been deployed to an environment:

* **Unsaved changes**
  If the version is denoted with an asterisk along with a filled gray indicator of "Unsaved Changes", the flow version is currently being edited and must be saved before navigating away from the page.

<Frame>
  <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b95f0c45-4c6e-96b8-6c0c-d2b15793d74c.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=d2416dda5ab3f51ec229891e3463a7ec" data-og-width="436" width="436" data-og-height="68" height="68" data-path="image/uuid-b95f0c45-4c6e-96b8-6c0c-d2b15793d74c.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b95f0c45-4c6e-96b8-6c0c-d2b15793d74c.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=c190ba0e6db1970c2aeb2e04ab8242c7 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b95f0c45-4c6e-96b8-6c0c-d2b15793d74c.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=e79c0fd94f6b8df326cdd3865f8f89e1 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b95f0c45-4c6e-96b8-6c0c-d2b15793d74c.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=1e80495d025f4a0fb032200febe8df05 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b95f0c45-4c6e-96b8-6c0c-d2b15793d74c.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=79a8359f7ba5c35f993e9e663472cbed 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b95f0c45-4c6e-96b8-6c0c-d2b15793d74c.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=fe98fb2a8be4683af90933055c236dcf 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b95f0c45-4c6e-96b8-6c0c-d2b15793d74c.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=1ec6958d52552963922051c11c9cac74 2500w" />
</Frame>

* **Unreleased version**
  If a version is denoted with a hollow *gray* indicator *Unreleased version* , the flow version is saved but not deployed to any environment.

<Frame>
  <img src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2db8fb16-cfde-04b6-400e-f92ec9bcb40f.png?fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=68a55c99c15fc98bcca00947e374a5ad" data-og-width="440" width="440" data-og-height="62" height="62" data-path="image/uuid-2db8fb16-cfde-04b6-400e-f92ec9bcb40f.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2db8fb16-cfde-04b6-400e-f92ec9bcb40f.png?w=280&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=8b0f541ef90b2d3480c483ecc8f24e43 280w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2db8fb16-cfde-04b6-400e-f92ec9bcb40f.png?w=560&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=c01a09ab42e283d5e7b409cf72157fe0 560w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2db8fb16-cfde-04b6-400e-f92ec9bcb40f.png?w=840&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=c7e2eb8b8f8e8b2149ea8b8eb95c1ae6 840w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2db8fb16-cfde-04b6-400e-f92ec9bcb40f.png?w=1100&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=58bf3136fe6f060f4259e7bdc3d17bac 1100w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2db8fb16-cfde-04b6-400e-f92ec9bcb40f.png?w=1650&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=926b52c1ed3f0a29c481b619b4af44f5 1650w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2db8fb16-cfde-04b6-400e-f92ec9bcb40f.png?w=2500&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=59e0c9ddbeab8d7e7b7747601ae96fba 2500w" />
</Frame>

* **Available in test**
  If a version is denoted with a hollow *orange* indicator of *Available in test*, the flow version is deployed to test environments (e.g. demo) but it is **not routed** from an intent.

<Frame>
  <img src="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-093b439c-2133-7dee-faa1-610f7f5ecda7.png?fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=7419f4229ebf412919f494ce13fd602f" data-og-width="400" width="400" data-og-height="68" height="68" data-path="image/uuid-093b439c-2133-7dee-faa1-610f7f5ecda7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-093b439c-2133-7dee-faa1-610f7f5ecda7.png?w=280&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=ee43566bc34b04fce583760418ff4412 280w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-093b439c-2133-7dee-faa1-610f7f5ecda7.png?w=560&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=f74f8ebd47f4cb4bd4e1f11fcc8240c5 560w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-093b439c-2133-7dee-faa1-610f7f5ecda7.png?w=840&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=e457b681da3c2ef3b418534c650a8ac9 840w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-093b439c-2133-7dee-faa1-610f7f5ecda7.png?w=1100&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=4f5c62ee0e2b3d6df5f580d7baf8283c 1100w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-093b439c-2133-7dee-faa1-610f7f5ecda7.png?w=1650&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=1293d9ab8782d612d1562792630edcb2 1650w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-093b439c-2133-7dee-faa1-610f7f5ecda7.png?w=2500&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=baede7e82665e0a47f5a2c4d56172bf5 2500w" />
</Frame>

* **Live in test**
  If a version is denoted with a filled *orange* indicator of *Live in test*, the flow version is deployed to test environments (e.g. demo) and it is **routed from an intent**.

<Frame>
  <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-988c703d-5e62-c8ea-e50d-273c003cd99b.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=30dbded69cd7c7934d3b65c255788bc9" data-og-width="354" width="354" data-og-height="58" height="58" data-path="image/uuid-988c703d-5e62-c8ea-e50d-273c003cd99b.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-988c703d-5e62-c8ea-e50d-273c003cd99b.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=3e1113bb5672621af11d85d23f2fa2dc 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-988c703d-5e62-c8ea-e50d-273c003cd99b.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=13ce0ab53774045ad49a41c68f25a96a 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-988c703d-5e62-c8ea-e50d-273c003cd99b.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=ac71fce50fb8996e3318886c9a0fe4ba 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-988c703d-5e62-c8ea-e50d-273c003cd99b.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=755e1080373867ff00b19a770a46ab7d 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-988c703d-5e62-c8ea-e50d-273c003cd99b.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=d15c0f1791d4f4933f22260138629b4f 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-988c703d-5e62-c8ea-e50d-273c003cd99b.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=3dc530fb1012af28863da16e54f767d7 2500w" />
</Frame>

* **Available in prod**
  If a version is denoted with a hollow *green* indicator of *Available in prod*, the flow version is deployed to the production environment but it is **not routed** from an intent.

<Frame>
  <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b619f575-64b7-c3f6-afd2-ad76bd2a4691.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=d097940d25fd5aef6b7c1235e4059a4d" data-og-width="400" width="400" data-og-height="62" height="62" data-path="image/uuid-b619f575-64b7-c3f6-afd2-ad76bd2a4691.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b619f575-64b7-c3f6-afd2-ad76bd2a4691.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=36f9893c6f56233e8a0f3112c8165e4d 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b619f575-64b7-c3f6-afd2-ad76bd2a4691.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=ba070344d8cc72ec37781c504f9762b6 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b619f575-64b7-c3f6-afd2-ad76bd2a4691.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=1f06d514c0b0e66c99c418d0fd7d3ae5 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b619f575-64b7-c3f6-afd2-ad76bd2a4691.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=0640e9247deb250234ef907e3ea6566a 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b619f575-64b7-c3f6-afd2-ad76bd2a4691.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=28215feaf80656ff6ed0a2bd5dff8696 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b619f575-64b7-c3f6-afd2-ad76bd2a4691.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=1d5ae25954d29bf22f9159d5ad67c11a 2500w" />
</Frame>

* **Live in prod**
  If a version is denoted with a filled *green* indicator of *Live in prod*, the flow version is deployed to the production environment and it **is routed from an intent which can be reached by customers**.

<Frame>
  <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8f2ad53d-9de5-1270-5a4a-6edeeb115f68.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=80f299cd2c6c1b50b0f944e36e697ef6" data-og-width="368" width="368" data-og-height="66" height="66" data-path="image/uuid-8f2ad53d-9de5-1270-5a4a-6edeeb115f68.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8f2ad53d-9de5-1270-5a4a-6edeeb115f68.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=3dc4b94c2a63209211668621d8cb48e2 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8f2ad53d-9de5-1270-5a4a-6edeeb115f68.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=7c923284b13f360bb63c4d36445248fd 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8f2ad53d-9de5-1270-5a4a-6edeeb115f68.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=45a81356802a2522867dbd1e373b2701 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8f2ad53d-9de5-1270-5a4a-6edeeb115f68.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=77d961cd0f2f430be5b5069954332ff9 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8f2ad53d-9de5-1270-5a4a-6edeeb115f68.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=185ada297e24fa1c5fc30a263d615f39 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8f2ad53d-9de5-1270-5a4a-6edeeb115f68.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=4883d002c763e1005639804bc8576641 2500w" />
</Frame>

* **Available in test and prod**
  If a version is denoted with a hollow *green* indicator of *Available in test and prod*, the flow version is deployed to test environments (e.g. demo) but it is **not routed** from an intent.

<Frame>
  <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a2a4d66c-428f-7424-e856-f4c681fc63d9.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=4e110ae32f09310f562a08c205909ba9" data-og-width="470" width="470" data-og-height="68" height="68" data-path="image/uuid-a2a4d66c-428f-7424-e856-f4c681fc63d9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a2a4d66c-428f-7424-e856-f4c681fc63d9.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=3f6b87c08206d0939aa3fb6aa2eb4533 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a2a4d66c-428f-7424-e856-f4c681fc63d9.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=778df03d71bc80c114c76c00d56f1ef2 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a2a4d66c-428f-7424-e856-f4c681fc63d9.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=f9c7be64295050de9b19ce0dc4524475 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a2a4d66c-428f-7424-e856-f4c681fc63d9.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=236c5d8ce303dcad7e853cb478928043 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a2a4d66c-428f-7424-e856-f4c681fc63d9.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=a1f6b16b0bedba74e06b6e28ce875b02 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a2a4d66c-428f-7424-e856-f4c681fc63d9.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=757915b66bcfd8d8e8e975e09af780c9 2500w" />
</Frame>

* **Live in test and prod**
  If a version is denoted with a filled *green* indicator of *Live in test and prod*, the flow version is deployed to all environments and it **is routed from an intent which can be reached by customers**.

<Frame>
  <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3e9419cd-0a3e-5fba-ba93-58bc786f6e27.png?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=2946de86a86f756d5ccfab1b03b74d59" data-og-width="424" width="424" data-og-height="60" height="60" data-path="image/uuid-3e9419cd-0a3e-5fba-ba93-58bc786f6e27.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3e9419cd-0a3e-5fba-ba93-58bc786f6e27.png?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=3854176c2c5ee8da7f7cd53c576168f1 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3e9419cd-0a3e-5fba-ba93-58bc786f6e27.png?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=58c3168ace431974d236b1b4dea56427 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3e9419cd-0a3e-5fba-ba93-58bc786f6e27.png?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=422b80b9c7ab195c9383abca1e1f83e0 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3e9419cd-0a3e-5fba-ba93-58bc786f6e27.png?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=0276fc8f5f1c3d8e2edb7e17f2ef1d90 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3e9419cd-0a3e-5fba-ba93-58bc786f6e27.png?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=2646f8c5bee033490fad924aaa6d799e 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3e9419cd-0a3e-5fba-ba93-58bc786f6e27.png?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=5f39489e1c06a04f16267dd5d0757095 2500w" />
</Frame>

#### View Intent Routing

If a flow is **routed from an intent** (e.g. Live in...), you can hover over these indicators to view and navigate to the respective intent routing page.

<Frame>
  <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d021a99f-b1fa-82d0-7629-7425bfebac9b.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=fd872ded5cf2c7044f86d58e2f250137" data-og-width="472" width="472" data-og-height="186" height="186" data-path="image/uuid-d021a99f-b1fa-82d0-7629-7425bfebac9b.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d021a99f-b1fa-82d0-7629-7425bfebac9b.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=9796bf1875fc71dc93ae8ce90742c6b7 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d021a99f-b1fa-82d0-7629-7425bfebac9b.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=b23b9f9a09f4941f50b2ff307a7941b2 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d021a99f-b1fa-82d0-7629-7425bfebac9b.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=f3b4d26f4af25178ba77557676bde9fd 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d021a99f-b1fa-82d0-7629-7425bfebac9b.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=c9a76e60ca53455ababc67850b5bb80f 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d021a99f-b1fa-82d0-7629-7425bfebac9b.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=eb54d20f3b1b1158b19c39ea1684344f 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d021a99f-b1fa-82d0-7629-7425bfebac9b.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=7ad88b9e7e5496255b7c9e85808695f7 2500w" />
</Frame>

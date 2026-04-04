# Source: https://docs.asapp.com/agent-desk/integrations/voice.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Voice

The ASAPP Voice Agent Desk includes web-based agent-assist services, which provide telephone agents with a machine learning and natural-language processing powered desktop. Voice Agent Desk augments the agent's ability to respond to inbound telephone calls from end customers.

Voice Agent Desk augments the agents by allowing quick access to relevant customer information and provides actionable suggestions that ASAPP infers from analyzing the ongoing conversation. The content, actions, and responses ASAPP provides to agents augment the agent's ability to respond quickly and more effectively to end customers.

Voice Agent Desk interfaces with relevant customer applications to enable desired features.

The ASAPP Voice Agent Desk is not in the call-path but is more of an active listener, and uses two different integrations to provide the real-time augmentation:

* [SIPREC](#glossary "Glossary") - you enable SIP RECording on the customer [Session Border Controllers (SBC)](#glossary "Glossary") and route a copy of the media stream, call information, and metadata per session to ASAPP.
* [CTI](#glossary "Glossary") Events - ASAPP subscribes to telephony events of the voice agents via the CTI server (login, logout, on-hook, off-hook, etc.)

ASAPP associates and aggregates the media sessions and CTI events within the ASAPP solution and uses them to power the agent augmentation features presented in Voice Agent Desk to the agents.

The ASAPP Voice Agent Desk solution provides agents with the real-time features that automate many of their repeatable tasks. Agents can use Voice Agent Desk for:

* The real-time transcript
* Conversation Summary - where agents add notes and structured data tags that ASAPP suggests as well as disposition the call during the interaction and once it is complete.
* Agents login to Voice Agent Desk via the customer's SSO.
* Customer information (optional)
* Knowledge Base integration (optional)

## Customer Current State Solution

ASAPP works with you to understand your current telephony infrastructure and ecosystem, including the type of voice work assignment platform/s and other capabilities available, such as SIPREC.

<Frame>
  <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8e1bdfb9-6cc8-a396-f02b-54b6e9034baa.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=e9e2d7c40b167a3e5827a4e0dd432944" data-og-width="1680" width="1680" data-og-height="1060" height="1060" data-path="image/uuid-8e1bdfb9-6cc8-a396-f02b-54b6e9034baa.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8e1bdfb9-6cc8-a396-f02b-54b6e9034baa.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=cce964ac24501299d8ab29602c33fa1d 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8e1bdfb9-6cc8-a396-f02b-54b6e9034baa.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=2bd0c47e88a4fa81d8e2c2fa476ae99f 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8e1bdfb9-6cc8-a396-f02b-54b6e9034baa.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=838ba850daaccdb0ed4ecf22b49e9905 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8e1bdfb9-6cc8-a396-f02b-54b6e9034baa.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=ee072604fbb62bba2c71cbf33bcf1193 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8e1bdfb9-6cc8-a396-f02b-54b6e9034baa.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=7768ff8b9c3fc0eac6b23113aa7a3c41 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8e1bdfb9-6cc8-a396-f02b-54b6e9034baa.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=c13119d77c93e37fba028d597eda1a06 2500w" />
</Frame>

## Solution Architecture

After ASAPP completes the discovery of the customer's current state, ASAPP completes the architecture definition, including integration points into the existing infrastructure. You can deploy the ASAPP [media gateways and media gateway proxies](#glossary "Glossary") within your existing AWS instance or within ASAPP's, providing additional flexibility and control.

<Frame>
  <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-839c65f3-0236-c4c9-1573-b166e65e3b88.png?fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=4d97177a8095c68db1ec24b9a97666c3" data-og-width="1799" width="1799" data-og-height="1300" height="1300" data-path="image/uuid-839c65f3-0236-c4c9-1573-b166e65e3b88.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-839c65f3-0236-c4c9-1573-b166e65e3b88.png?w=280&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=9367aec9599bc2b4df4c0264c3495c66 280w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-839c65f3-0236-c4c9-1573-b166e65e3b88.png?w=560&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=8dd7c13c5ca84cc664896d3ff51ace86 560w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-839c65f3-0236-c4c9-1573-b166e65e3b88.png?w=840&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=8878482b128859ee553b9d6d4470648a 840w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-839c65f3-0236-c4c9-1573-b166e65e3b88.png?w=1100&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=c6169d3c97a2e2b821d6b69ec4bbdf92 1100w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-839c65f3-0236-c4c9-1573-b166e65e3b88.png?w=1650&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=c791a9e281087396bbdea591a6f1980e 1650w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-839c65f3-0236-c4c9-1573-b166e65e3b88.png?w=2500&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=2e863904019ec7d74acb3d6a1ed1116a 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0ff10b1d-7e06-7319-9c26-21e4d1695d6e.png?fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=67d2a800d26dae5d210e7ed2a07d7a15" data-og-width="1799" width="1799" data-og-height="1300" height="1300" data-path="image/uuid-0ff10b1d-7e06-7319-9c26-21e4d1695d6e.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0ff10b1d-7e06-7319-9c26-21e4d1695d6e.png?w=280&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=9c3dc5bd52692b7648c9aab083b80207 280w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0ff10b1d-7e06-7319-9c26-21e4d1695d6e.png?w=560&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=d115b53e3f8c0ced10a996a0521d2cd4 560w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0ff10b1d-7e06-7319-9c26-21e4d1695d6e.png?w=840&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=f350fa2b8d1f83c0c20b21f35198d565 840w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0ff10b1d-7e06-7319-9c26-21e4d1695d6e.png?w=1100&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=25ddbfab4f3f273d05dd091f67445bb0 1100w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0ff10b1d-7e06-7319-9c26-21e4d1695d6e.png?w=1650&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=c27ff17dfc6bce1a8c7df9410c67dbc8 1650w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-0ff10b1d-7e06-7319-9c26-21e4d1695d6e.png?w=2500&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=a39d463e9380bbcf9a2b6e4622c15020 2500w" />
</Frame>

### Network Connectivity

ASAPP will determine the network connectivity between your infrastructure and the ASAPP AWS Virtual Private Cloud (VPC) based on the architecture, however, ASAPP will deploy secure connections between your data centers and the ASAPP VPC.

<Frame>
  <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4f069eaa-5575-b8bc-bff8-ff581945295c.png?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=341b5bc4aa5c918ec40d09170f1f823e" data-og-width="1799" width="1799" data-og-height="1300" height="1300" data-path="image/uuid-4f069eaa-5575-b8bc-bff8-ff581945295c.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4f069eaa-5575-b8bc-bff8-ff581945295c.png?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=76b7de642378a4a29fa5401252937e65 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4f069eaa-5575-b8bc-bff8-ff581945295c.png?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=dbcddc41149c33ea0ded40aea8db9779 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4f069eaa-5575-b8bc-bff8-ff581945295c.png?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=5e260ef23882a2dd36716304ef904c2c 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4f069eaa-5575-b8bc-bff8-ff581945295c.png?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=6bbc92f1245641104fe245c253acfc40 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4f069eaa-5575-b8bc-bff8-ff581945295c.png?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=87311382190f8e3cf2950c22bf3a172b 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4f069eaa-5575-b8bc-bff8-ff581945295c.png?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=6009d76e26f55df657c6dde03c684e43 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-5faecace-de88-de02-cfa4-66cb7cbd1e3e.png?fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=9d378ff3c9f2e5a5d317ce84d7d6c8dd" data-og-width="1799" width="1799" data-og-height="1300" height="1300" data-path="image/uuid-5faecace-de88-de02-cfa4-66cb7cbd1e3e.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-5faecace-de88-de02-cfa4-66cb7cbd1e3e.png?w=280&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=a11c0a1c1dc660e0de508af2cfeef065 280w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-5faecace-de88-de02-cfa4-66cb7cbd1e3e.png?w=560&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=664bdbf2931f58b2b042f9d6c5c07074 560w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-5faecace-de88-de02-cfa4-66cb7cbd1e3e.png?w=840&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=1e67693bd8356fda215a22a7c738d036 840w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-5faecace-de88-de02-cfa4-66cb7cbd1e3e.png?w=1100&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=c1c9dfdede6ec312fe2d5f06553d475b 1100w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-5faecace-de88-de02-cfa4-66cb7cbd1e3e.png?w=1650&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=5b3dbaa39954c914f5df2b4c21421ee7 1650w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-5faecace-de88-de02-cfa4-66cb7cbd1e3e.png?w=2500&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=88140dda4f002f94e5745b202f020044 2500w" />
</Frame>

### Port Details

You can see ports and protocols in use for the Voice implementation depicted in the following diagram. These definitions provide visibility to your security teams for the provisioning of firewalls and ACL's.

* SIP/SIPREC - TCP (5060, 5070-5072)
  * SBC to Media Gateway Proxies
  * SBC to Media Gateway/s
* Audio Streams - UDP \<RTP/RTCP port range>
* CTI Event Feed - TCP \<vendor specific>
* API Endpoints - TCP 443
  In customer firewalls, disable the [SIP Application Layer Gateway (ALG)](#glossary "Glossary") and any 'Threat Detection' features, as they typically interfere with the SIP dialogs and the re-INVITE process.

<Frame>
  <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-5afeb63d-6712-0cea-b0df-04adf439353d.png?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=1944e0fc92bae4a048feff5c5e54f605" data-og-width="1799" width="1799" data-og-height="1300" height="1300" data-path="image/uuid-5afeb63d-6712-0cea-b0df-04adf439353d.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-5afeb63d-6712-0cea-b0df-04adf439353d.png?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=46326b14b1e3ecc25f599e8f45075148 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-5afeb63d-6712-0cea-b0df-04adf439353d.png?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=1896bc44ce57974e3b8ddd6282bdea1f 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-5afeb63d-6712-0cea-b0df-04adf439353d.png?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=ff0089993f413d3fbf5992e5458bb0fa 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-5afeb63d-6712-0cea-b0df-04adf439353d.png?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=1869d78a2eeba589aba6277293a008e0 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-5afeb63d-6712-0cea-b0df-04adf439353d.png?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=01477e1484cf015bf6d2d14048ea9298 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-5afeb63d-6712-0cea-b0df-04adf439353d.png?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=784b5def46032a52c4d0c1a9f565bd8d 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8a91dd1c-f0d5-8378-61e9-a858bb05d416.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=1d41a4ff7f8cd68829029116e270078b" data-og-width="1799" width="1799" data-og-height="1300" height="1300" data-path="image/uuid-8a91dd1c-f0d5-8378-61e9-a858bb05d416.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8a91dd1c-f0d5-8378-61e9-a858bb05d416.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=53d665c844c251dc5af139a56a2988a4 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8a91dd1c-f0d5-8378-61e9-a858bb05d416.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=1781c62b43eaf9d466aa12204002eaa1 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8a91dd1c-f0d5-8378-61e9-a858bb05d416.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=c376109a893e242601544ccc1917064d 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8a91dd1c-f0d5-8378-61e9-a858bb05d416.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=f7b45916155476db65f46046765299c3 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8a91dd1c-f0d5-8378-61e9-a858bb05d416.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=f8e5e4c1a21a82db55a54bbb581ca31f 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8a91dd1c-f0d5-8378-61e9-a858bb05d416.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=05aca2282ad6ecb0a3169bb2b7970a35 2500w" />
</Frame>

### Data Flow

The Voice Agent Desk Data Flow diagram illustrates the [PCI Zone](#glossary "Glossary") within the ASAPP solution. The customer SBC originates the SIPREC sessions and the media streams and sends them to ASAPP media gateways, which repackage the streams into secure WebSockets and send them to the [Voice Streamer](#glossary "Glossary") within the PCI zone. ASAPP encrypts the data in transit and at rest.

The SBC does not typically encrypt the SIPREC sessions and associated media streams from the SBC to the ASAPP media gateways, but usually encapsulates them within a secure connection. You are responsible for the compliance/security of the network path between the SBC and the media gateways, in accordance with applicable customer policies.

<Frame>
  <img src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-3190e31d-1fc7-fcc3-57f6-aff9dee85513.png?fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=22060e262c98f3ba8eaf703320576946" data-og-width="1220" width="1220" data-og-height="550" height="550" data-path="image/uuid-3190e31d-1fc7-fcc3-57f6-aff9dee85513.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-3190e31d-1fc7-fcc3-57f6-aff9dee85513.png?w=280&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=83343eb09bb3f2b1c4c6e25dc9e4d074 280w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-3190e31d-1fc7-fcc3-57f6-aff9dee85513.png?w=560&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=73a6aaa7ef64669bbdde8e88a75c3c51 560w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-3190e31d-1fc7-fcc3-57f6-aff9dee85513.png?w=840&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=0943080b353601bc35df0f66137a251a 840w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-3190e31d-1fc7-fcc3-57f6-aff9dee85513.png?w=1100&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=f4367f3cc348c8b87b145b16561ddc28 1100w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-3190e31d-1fc7-fcc3-57f6-aff9dee85513.png?w=1650&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=9e6f1e08437ceec021e82ea2ce700582 1650w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-3190e31d-1fc7-fcc3-57f6-aff9dee85513.png?w=2500&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=bfaae86317f42b551de6ee98bdbb177f 2500w" />
</Frame>

## SIPREC and CTI Correlation and Association

In order to be able to associate the correct audio stream and the correct agent and agent desktop, ASAPP must associate the audio session and the CTI events of the particular agent.

ASAPP assigns voice agents a unique Agent ID and adds it to the SSO profile as a custom attribute. ASAPP will then map this to the Agent ID within ASAPP.

You configure the SBCs to set a unique call identifier, such as [UCID](#glossary "Glossary") (Avaya) or [GUID](#glossary "Glossary")/GUCID (Cisco), etc. on inbound calls, which provides ASAPP the means to correlate the individual SIPREC stream with the CTI events of the correct agent.

The SBCs will initiate a SIPREC session INVITE for each new call. With SIPREC, the customer SBC and the ASAPP media gateway negotiate the media attributes via the [SDP](#glossary "Glossary") offer/answer exchange during the establishment of the session. The codec/s in use today are:

1. G.711
2. G.729

Traffic and load considerations:

* Total number of voice agents using ASAPP -\<total agent count>
* Maximum concurrently logged in agents \<max concurrent agent count>
* Maximum concurrent calls at each SBC pair -\<max number of current offered calls to SBC/s>
* Maximum calls per second at each SBC pair -\<max calls per second offered to the SBC>

### Load Balancing for ASAPP Media Gateway Proxies

In order to distribute traffic across all of the media gateway proxies, the SBCs load balance the SIPREC dialogs to the ASAPP MG Proxies. To facilitate this, you configure the SBCs with a proxy list that provides business continuity and enables fail-over to the next available proxy if one of the proxies becomes unavailable.

Session Recording Group Example:

The customer data center SBCs use different orders for the media gateway proxy list.

Data Center 1:

1. MG Proxy #1
2. MG Proxy #2
3. MG Proxy #3

Data Center 2:

1. MG Proxy #3
2. MG Proxy #2
3. MG Proxy #1

## Media Failover and Survivability

### Session Border Controller (SBC) to Media Gateways (MG) and Proxies

* Typically unencrypted signaling and audio through a secure connection/private tunnel
  * You can encrypt the traffic in theory, but the SBC has costs and scale limitations associated with encrypting traffic, as well as cost increases to MGs as you will need more instances.
* ASAPP accepts SIPREC dialogs, but initially sets SDP media to "inactive," which pauses the audio while in the IVR and in queue.
  * The ASAPP media gateway will re-invite the session and re-negotiate the media parameters to resume the audio stream when the agent answers the call.

<Frame>
  <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d5da0e97-893d-32e0-3686-ab027d3132cf.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=3baa324bd7ad2d6b603bec61c5ba95af" data-og-width="1780" width="1780" data-og-height="1370" height="1370" data-path="image/uuid-d5da0e97-893d-32e0-3686-ab027d3132cf.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d5da0e97-893d-32e0-3686-ab027d3132cf.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=e41a8e72b1868332df9b8175b14b9ead 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d5da0e97-893d-32e0-3686-ab027d3132cf.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=f1a8f69cf397af561e1f87355fb65ff7 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d5da0e97-893d-32e0-3686-ab027d3132cf.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=d97cd7cafc9c5f6361cac196b8681579 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d5da0e97-893d-32e0-3686-ab027d3132cf.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=1e555fe87f2d4680af583c0f990f9c53 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d5da0e97-893d-32e0-3686-ab027d3132cf.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=d19d21fd9940601db825e6da69edfac3 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d5da0e97-893d-32e0-3686-ab027d3132cf.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=8cbcad3b2848c453837da7bc391eeb3b 2500w" />
</Frame>

* SIP RFC handles some level of packet loss and re-transmissions but if the SIP signal is lost, the SIPREC dialog will be torn down and the media will no longer be sent.
* Media is sent via UDP.
  * No retransmissions so packet loss or disconnects result in permanent loss of the audio.
* Proxies are transactionally stateless.
* No audio is ever sent to/through proxies, all audio goes directly to media gateways.
  * Proxies are no longer in the signal path after the first transaction.
* If a proxy fails or is disconnected, SBCs can "hunt" or failover to the next proxy in it's configuration.
  * No existing calls are impacted.
* If media gateways fail or are disconnected, the next SIP transaction will fail and the existing media stream (if resumed) will send via UDP to nothing (media is lost).
* Media gateways use regular SIP OPTIONS sent to static proxies that indicate if they are available and their current number of calls.
* Proxies use this active call load to evenly load balance to the least used media gateway.
  * As well as dynamically pick up when a media gateway is no longer available or new ones come online.
* Any inbound calls coming in over ISDN-PRI/TDM trunk facilities will not have associated SIPREC sessions, as these calls do not traverse the SBC.

### Media Gateways to ASAPP Voice Streamers

* Secure websocket initiated per stream (2 per call) to the ASAPP Voice Streamer
* Media gateways do not store media, all processing is done in memory.
* Packet loss can be tolerated a little with TCP retransmissions.
* Buffer overrun audio data in the media gateway is purged instantly (per stream).
* If a secure websocket connection is lost, the media gateway will attempt a limited number of reconnections and then fail.
* If a voice streamer fails, a media gateway will reconnect to a new streamer.
* If a media gateway fails, the SIPREC stream is lost and the SBC can no longer send audio for that group of calls.

## Integration

### API Integration

Integration to existing customer systems enable ASAPP to call for information from those systems to present to the agent, such as:

* customer profile information
* billing history/statements
* customer product purchases
* Knowledge Base

Integration also enables ASAPP to push information to those systems, such as disposition notes and account changes/updates.

ASAPP will work with you to determine use cases for each integration that will add value to the agent and customer experience.

### Custom Call Data from CTI Information

In many instances, CTI will carry end customer specific information about the end customer and the call. This may be in the form of [User-to-User Information (UUI)](#glossary "Glossary"), `Call Variables`, Custom `NamedVariables`, or Custom `KVList UserData`. ASAPP uses this data to provide more information to agents and admins. It may contain information that provides customer identity information, route codes, queue information, customer authentication status, IVR interactions/ outputs, or simply unique identifiers for further data lookup from APIs. ASAPP extracts the custom fields and leverages the data in real-time to provide agents as much information as possible as part of the initial part of the interaction.

Each environment is uniquely different and ASAPP needs to understand what data is available from the CTI events to maximize relevant data to the agent and for voice intelligence processing.

Examples:

**Avaya**

```json  theme={null}
UserToUserInfo: “10000002321489708161;verify=T;english;2012134581”
```

**Cisco**

```json  theme={null}
CallVariable1:10000002321489708161
CallVariable7:en-us
user.AuthDetect:87
```

**Genesys**

```json  theme={null}
userAccount:10000002321489708161
userLanguage:en
userFirstName:John
```

**Twilio**

```json  theme={null}
<Parameter name=”FirstName” value=”John”/>
<Parameter name=”AccountNum” value=”10000002321489708161”/>
<Parameter name=”Language” value=”English”/>
<Parameter name=”VerficationStatus” value=”True”/>
```

### SSO Integration

[Single Sign-On (SSO)](#glossary "Glossary") allows users to sign in to ASAPP using their existing corporate credentials. ASAPP supports [Security Assertion Markup Language](#glossary "Glossary") (SAML) 2.0 Identity Provider (IdP) based authentication. ASAPP requires SSO integration to support implementation.

To enable the SSO integration, the customer must populate and pass the Agent Login ID as a custom attribute in the SAML payload. Then, when a user logs in to ASAPP and authenticates via the existing SSO mechanism, the Agent Login ID value is then passed to ASAPP via SAML assertion for subsequent CTI event correlation.

The ASAPP Voice Agent Desk supports role-based access. You can define a specific role for each user that will determine their permissions within the ASAPP platform. For example, you can define the "app-asappagentprod" role in the Active Directory to send to ASAPP via SAML for those specific users that should have access to ASAPP Voice Agent Desk only. You can define multiple roles for an agent, such as access to Voice Agent Desk, Digital Agent Desk, and Admin Desk. You must define roles for voice agents and supervisors and include them in the SAML payload as a custom attribute.

The table below provides examples of SAML user attributes.

<table class="informaltable frame-void rules-rows">
  <tbody>
    <tr>
      <td class="td"><p><strong>SAML Attribute Values</strong></p></td>
      <td class="td"><p><strong>ASAPP Usage</strong></p></td>
      <td class="td"><p><strong>Examples</strong></p></td>
    </tr>

    <tr>
      <td class="td"><p>Agent Login ID</p></td>
      <td class="td"><p>Provides mapping of the customer telephony agent ID to ASAPP’s internal user ID.</p></td>

      <td class="td">
        <p><code class="code">user.extensionattribute1</code></p>
        <p>or</p>
        <p><code class="code">cti\_agent\_id</code></p>
      </td>
    </tr>

    <tr>
      <td class="td"><p>Givenname</p></td>
      <td class="td"><p>Given name</p></td>
      <td class="td"><p><code class="code">user.givenname</code></p></td>
    </tr>

    <tr>
      <td class="td"><p>Surname</p></td>
      <td class="td"><p>Surname</p></td>
      <td class="td"><p><code class="code">user.surname</code></p></td>
    </tr>

    <tr>
      <td class="td"><p>Mail</p></td>
      <td class="td"><p>Email address</p></td>
      <td class="td"><p><code class="code">user.mail</code></p></td>
    </tr>

    <tr>
      <td class="td"><p>Unique User Identifier</p></td>
      <td class="td"><p>The User ID (authRepId); can be represented as an employee ID or email address.</p></td>
      <td class="td"><p><code class="code">user.employeeid</code> or <code class="code">user.userprincipalname</code></p></td>
    </tr>

    <tr>
      <td class="td"><p>PhysicalDeliveryOfficeName</p></td>
      <td class="td"><p>Physical delivery office name</p></td>
      <td class="td"><p><code class="code">user.physicaldeliveryofficename</code></p></td>
    </tr>

    <tr>
      <td class="td"><p>HireDate</p></td>
      <td class="td"><p>Hire date attribute used by reporting.</p></td>
      <td class="td"><p><code class="code">HireDate</code></p></td>
    </tr>

    <tr>
      <td class="td"><p>Title</p></td>
      <td class="td"><p>Can be used for reporting.</p></td>
      <td class="td"><p><code class="code">Title</code></p></td>
    </tr>

    <tr>
      <td class="td"><p>Role</p></td>
      <td class="td"><p>The roles define what agents can see in the UI and have access to when they login.</p></td>
      <td class="td"><p><code class="code">user.role app-asappadminprod app-asappagentprod</code></p></td>
    </tr>

    <tr>
      <td class="td"><p>Group</p></td>
      <td class="td"><p>For Voice, this is only for reporting purposes. For digital chat this also can be used for queue management.</p></td>
      <td class="td"><p><code class="code">user.groups</code></p></td>
    </tr>
  </tbody>
</table>

## Call Flows

Once an inbound [Automatic Call Distribution (ACD)](#glossary "Glossary") call is connected to an agent, the agent may need to transfer or conference the customer in with another agent/skill group. It is important to identify and document these types of call flows, when the transcript and customer data needs to be provided to another agent due to a change in call state. Then ASAPP will test these call scenarios as part of the QA and UAT testing process.

These scenarios include:

* Cold Transfers
  * The agent transfers the call to a queue (or similar) but does not stay on the call.
* Warm Transfers
  * The agent talks to the receiving agent prior to completing the transfer, in order to prepare the agent with the context of the call/customer issue.
* Conferences
  * The agent conferences in another agent or supervisor and remains on the call.
* Other
  * Customer call back applications or other unique call flows.

## Speech Files for Model Training

To prepare for a production launch, ASAPP will train the speech models on the customer language and vocabulary, which will provide better transcription accuracy. ASAPP will use a set of customer call recordings from previous interactions.

You will need to provide ASAPP with a minimum of 1,000 hours of agent/customer dual-channel/speech separated media files in .wav format with a sample rate of 8000 and signed 16-bit [Pulse-Code Modulation (PCM)](#glossary "Glossary") in order for ASAPP to train the speech recognition models.

* ASAPP will set up an SFTP site in our PCI zone to receive voice media files from you. You will provide an SSH public key and ASAPP will configure the SFTP location within S3.
  * ASAPP prefers that you redact the PCI data from the provided voice recordings. Regardless, ASAPP will use its media redaction technology to remove sensitive customer data (Credit Card Numbers and Social Security Numbers) from the recordings to the extent possible. In addition to the default redaction noted above, ASAPP can customize redaction criteria per your requirements and feature considerations.
* The unredacted voice media files will remain within the [PCI Zone](#glossary "Glossary").
* ASAPP will use a combination of automated and manual transcription to refine our speech models. Data that ASAPP shares with vendors goes through the redaction process described above and is transferred via secured mechanisms such as SFTP.

## Non-Production Lower Environments

As part of our implementation strategy, ASAPP will implement two lower environments for testing (UAT and QA) by both ASAPP and customer resources. It is important that the lower environments do not use production data, including the audio data, as it may contain PCI information or other customer information that you should not expose to the lower environments.

You can implement lower environments using a lab environment, or a production environment.

When using the production infrastructure to support the lower environments, ASAPP separates production traffic from the lower environment traffic. The lower environments will have dedicated inbound numbers and routing that will allow them to be isolated and provide the ability for ASAPP and the customer teams to fully test using non-production traffic.

As part of the environment's buildout, ASAPP will need a way to initiate and terminate test calls. The ASAPP team will use the same soft-client and tools used by agents to login as a voice agent, answer inbound test calls, and simulate the various call flows used within the customer contact center.

ASAPP proposes customers allocate two [Direct Inward Dialing](#glossary "Glossary") (DID)/ [Toll Free Number](#glossary "Glossary") (TFN) numbers, one for each of the two different test environments.

* Demo Environment - A lower environment used by both ASAPP and customers.
* Preprod Environment - A lower environment used by ASAPP QA for testing.

At the SBC level, you should configure the Demo and Preprod DID numbers with their own Session Recording Server (SRS), unique from the production SRS configuration. This will allow the test environments to always have SIPREC turned on, but not send excess/production traffic to ASAPP. This also allows the test environments to operate independently of production. With Oracle/Acme, you can accomplish this with session agents. For Avaya SBCE, you can accomplish this with End Point Flows.

ASAPP will have a separate set of media gateways and media gateway proxies for each environment to ensure traffic and data separation.

The lower environments (not PCI compliant) are for testing only and will not receive actual customer audio. The production environment is where ASAPP transcribes and redacts the audio in a PCI zone.

<Frame>
  <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9b1f3ae3-1ee4-9930-3cd6-7ca15a0d2501.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=941ee7b159d084f6afdb587fc0ff26ce" data-og-width="1799" width="1799" data-og-height="1400" height="1400" data-path="image/uuid-9b1f3ae3-1ee4-9930-3cd6-7ca15a0d2501.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9b1f3ae3-1ee4-9930-3cd6-7ca15a0d2501.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=27b9815f8362211274bd4b7062f55726 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9b1f3ae3-1ee4-9930-3cd6-7ca15a0d2501.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=9a315d3dc616d94c45ee408773e69dff 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9b1f3ae3-1ee4-9930-3cd6-7ca15a0d2501.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=0914b8e5678a588ac5413ad555e221f6 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9b1f3ae3-1ee4-9930-3cd6-7ca15a0d2501.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=bf931ea0c1ee39b76a4b584bf4478f77 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9b1f3ae3-1ee4-9930-3cd6-7ca15a0d2501.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=3f1c7f742b2ca47a575cf37645fc6fa1 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9b1f3ae3-1ee4-9930-3cd6-7ca15a0d2501.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=2a907b7468f9bef4b4c47c72992e9e53 2500w" />
</Frame>

## Appendix A - Avaya Configuration Details

This section provides specific configuration details for the solution that leverages Avaya telephony infrastructure.

**Avaya Communication Manager**

* Set Avaya [Internet Protocol - Private Branch Exchange (IP-PBX)](#glossary "Glossary") SIP trunks to 'shared' to ensure the UCID is not reset by the PBX.
  * Change trunk-group x -> page 3 -> UUI Treatment:shared
* Set `SendtoASAI` parameter to 'yes.'
  * Change system-parameters features -> page 13 -> Send UCID to ASAI? Y
  * Add ASAPP voice agents to a new skill, one that is not used for queuing or routing.
  * Configure AES to monitor the new skill.
    * ASAPP will use the `cstaMonitorDevice` service to monitor the ACD skill.
    * ASAPP may also call `cstaMonitorCallsViaDevice` if more call data is needed.

**Avaya AES [TSAPI](#glossary "Glossary") configuration**

* Networking -> Ports -> TSAPI Ports
  * Enabled
  * TSAPI Service Port (450)
    * Firewalls will also need to allow these ports.

| **Connection Type** | **TCP Min Port** | **TCP Max Port** |
| :------------------ | :--------------- | :--------------- |
| unencrypted/TCP     | 1050             | 1065             |
| encrypted/TLS       | 1066             | 1081             |

* AES link to ASAPP connection provisioning
  * Provisioning of new ASAPP Voice skill for monitoring.

## Appendix B - Cisco Configuration Details

This section provides specific configuration details for the solution that leverages Cisco telephony infrastructure.

**Cisco CTI Server configuration**

* ASAPP will connect with the `CTI_SERVICE_ALL_EVENTS`
  * You will need the Preferred `ClientID` (identifier for ASAPP) and `ClientPassword` (if not null) to send the `OPEN_REQ` message.
* Ports 42027 (side A) and 43027 (side B)
  * Instance number if not 0 will increase these ports
  * Firewalls will also need to allow these ports
* `CallVariable`1-10 Definitions/usages
* Custom `NamedVariables` and `NamedArrays` Definitions/usages
* Events currently used by ASAPP:
  * `OPEN_REQ`
  * `OPEN_CONF`
  * `SYSTEM`
  * `AGENT_STATE`
  * `AGENT_PRE_CALL`
  * `BEGIN_CALL`
  * `CALL_DATA_UPDATE`
  * `CALL_CLEARED`
  * `END_CALL`

## Appendix C - Oracle (Acme) Session Border Controller

In order to provide the correlation between the SIPREC session and specific CTI events, ASAPP will use the following approach:

* Session Border Controller
  * Configure the SBC to create an Avaya UCID (universal call identifier) in the SIP header.
    * UCID generation is a native feature for Oracle/Acme Packet session border controller platforms.
      * [Oracle SBC UCID Admin](https://docs.oracle.com/en/industries/communications/enterprise-session-border-controller/8.4.0/configuration/universal-call-identifier-spl#GUID-97456BB9-264F-4290-AB92-8C60F64B9734)
* In the Oracle (Acme Packet) SBCs, load balancing across the ASAPP Media Gateway Proxies requires the use of static IP addresses versus the use of dynamic hostnames.
  * SBC Settings for Media Gateway Proxies - Production and Lower Environments:
    * Transport = TCP
    * SIP OPTIONS = disabled
    * Load Balancing strategy = "hunt"
    * Session-recording-required = disabled
    * Port = 5070

## Glossary

| **Term**                                                  | **Acronym** | **Definition**                                                                                                                                                                                                                 |
| :-------------------------------------------------------- | :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Automated Speech Recognition**                          | ASR         | The service that converts speech (audio) to text.                                                                                                                                                                              |
| **Automatic Call Distributor**                            | ACD         | A telephony system that automatically receives incoming calls and distributes them to available agents. Its purpose is to help inbound contact centers sort and manage large volumes of calls to avoid overwhelming the team.  |
| **Computer Telephony Integration**                        | CTI         | The means of linking a call center's telephone systems to a business application. In this case, ASAPP monitors agents and receives call state event data via CTI.                                                              |
| **Direct Inward Dialing**                                 | DID         | A service that allows a company to provide individual phone numbers for each employee without a separate physical line.                                                                                                        |
| **Globally Unique IDentifier**                            | GUID        | A numeric label used for information in communications systems. When generated according to the standard methods, GUIDs are, for practical purposes, unique. Also known as Universally Unique IDentifier (UUID)                |
| **Internet Protocol Private Branch Exchange**             | IP-PBX      | A system that connects phone extensions to the Public Switched Telephone Network (PSTN) and provides internal business communication.                                                                                          |
| **Media Gateway**                                         | MG          | Entry point for all calls from Customer. Receives and forwards SIP and audio data.                                                                                                                                             |
| **Media Gateway Proxy**                                   | MGP         | SIP Proxy, used for SIP signaling to/from customer SBC.                                                                                                                                                                        |
| **Payment Card Industry Data Security Standard**          | PCI DSS     | Payment card industry compliance refers to the technical and operational standards that businesses follow to secure and protect credit card data provided by cardholders and transmitted through card processing transactions. |
| **Payment Card Industry Zone**                            | PCI Zone    | PCI Level I Certified environment for cardholder data and other sensitive customer data storage (Transport layer security for encryption in transit, encryption at rest, access tightly restricted and monitored).             |
| **Pulse-Code Modulation**                                 | PCM         | Pulse-code modulation is a method used to digitally represent sampled analog signals. It is the standard form of digital audio in digital telephony.                                                                           |
| **Security Assertion Markup Language**                    | SAML        | An open standard for exchanging authentication and authorization data between an identity provider and a service provider.                                                                                                     |
| **Session Border Controller**                             | SBC         | SIP-based voice security platform; source of the SIPREC sessions to ASAPP.                                                                                                                                                     |
| **Session Description Protocol**                          | SDP         | Used between endpoints for negotiation of network metrics, media types, and other associated properties, such as codec and sample size.                                                                                        |
| **Session Initiation Protocol Application-Level Gateway** | SIP ALG     | A firewall function that enables the firewall to inspect the SIP dialog/s. This function should be disabled to prevent SIP dialog interruption.                                                                                |
| **Session Initiation Protocol Recording**                 | SIPREC      | IETF standard used for establishing recording sessions and reporting of the metadata of the communication sessions.                                                                                                            |
| **Single Sign On**                                        | SSO         | Single sign-on is an authentication scheme that allows a user to log in with a single ID and password to any of several related, yet independent, software systems.                                                            |
| **Toll-Free Number**                                      | TFN         | A service that allows callers to reach businesses without being charged for the call. The called person is charged for the toll-free number.                                                                                   |
| **Telephony Services API**                                | TSAPI       | Telephony server application programming interface (TSAPI) is a computer telephony integration standard that enables telephony and computer telephony integration (CTI) application programming.                               |
| **Universal Call IDentifier**                             | UCID        | UCID assigns a unique number to a call when it enters that call center network. The single UCID can be passed among platforms, and can be used to compile call-related information across platforms and sites.                 |
| **User to User Information**                              | UUI         | The SIP UUI header allows the IVR to insert information about the call/caller and pass it to downstream elements, in this case, Communication Manager. The UUI information is then available via CTI.                          |
| **Voice Streamer**                                        | VS          | Receives SIP and audio data from MG. Gets the audio transcribed into text through the ASR and sends that downstream.                                                                                                           |

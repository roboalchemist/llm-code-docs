# Source: https://docs.asapp.com/ai-productivity/ai-compose/deploying-ai-compose-for-salesforce.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploying AI Compose for Salesforce

> Use AI Compose on Salesforce Lightning Experience.

## Overview

This page describes how to integrate AI Compose into your Salesforce application.

### Integration Steps

There are three parts to the AI Compose setup process. Use the links below to skip to information about a specific part of the process:

1. [Configure the Salesforce organization](#1-configure-the-salesforce-organization-centrally) centrally using an administrator account
2. [Setup agent/user authentication](#2-set-up-single-sign-on) through the existing single sign-on (SSO) service
3. [Work with your ASAPP contact to configure Auto-Pilot Greetings](#3-configure-auto-pilot-greetings), if desired

<Tip>
  Expected effort for each part of the setup process:

  * 1 hour for installation and configuration of the ASAPP chat components
  * 1-2 hours to enable user authentication, depending on SSO system complexity
</Tip>

## Requirements

**Browser Support**

ASAPP AI Compose is supported in Google Chrome and Microsoft Edge

<Tip>
  NOTE: This support covers the latest version of each browser and extends to the previous two versions

  Please consult your ASAPP account contact if your installation requires support for other browsers
</Tip>

**Salesforce**

ASAPP supports Lightning-based chat (cf. classic)

<Frame>
  <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c6a319ef-4846-1c14-7ea5-5294ed44e8e2.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=197eb06f56ad435844c348f0f301942a" data-og-width="191" width="191" data-og-height="32" height="32" data-path="image/uuid-c6a319ef-4846-1c14-7ea5-5294ed44e8e2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c6a319ef-4846-1c14-7ea5-5294ed44e8e2.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=812a40db36e9f8390b18c15f3b7977ad 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c6a319ef-4846-1c14-7ea5-5294ed44e8e2.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=24c7f94e3483a28349f0cefb3601218a 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c6a319ef-4846-1c14-7ea5-5294ed44e8e2.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=167ea98803418b1011579b66cffc2a72 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c6a319ef-4846-1c14-7ea5-5294ed44e8e2.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=68126a671b731ee790a310b14433900a 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c6a319ef-4846-1c14-7ea5-5294ed44e8e2.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=8fb760ccec36b09b563199e3c240fe16 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c6a319ef-4846-1c14-7ea5-5294ed44e8e2.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=46751a028f4e0f539ce6e15d31647ac0 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e66b3aab-d17a-a7dc-f607-4f8a9504db87.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=7a6329c3b8870b0efed7b970de0a601f" data-og-width="181" width="181" data-og-height="44" height="44" data-path="image/uuid-e66b3aab-d17a-a7dc-f607-4f8a9504db87.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e66b3aab-d17a-a7dc-f607-4f8a9504db87.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=2cdf631676264c6a0cd28c33d19f8fd9 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e66b3aab-d17a-a7dc-f607-4f8a9504db87.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=af8e4ca52570fb2dbfddb30bb4ef8071 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e66b3aab-d17a-a7dc-f607-4f8a9504db87.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=c223e60d25e0de5aa669e789eb6fc875 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e66b3aab-d17a-a7dc-f607-4f8a9504db87.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=921f044f140d97d019935bb6d30f3a85 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e66b3aab-d17a-a7dc-f607-4f8a9504db87.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=b8c50ccb0bb793d0b128c5737fc41950 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e66b3aab-d17a-a7dc-f607-4f8a9504db87.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=94b449d86bfc8684bd8a72504433b5a5 2500w" />
</Frame>

**SSO Support**

The AI Compose widget supports SP-initiated SSO with either OIDC (preferred method) or SAML.

**Domain Whitelisting**

In order for AI Compose to interact with ASAPP's backend and third-party support services, the following domains need to be accessible from end-user environments:

| Domain                                     | Description                                                        |
| :----------------------------------------- | :----------------------------------------------------------------- |
| \*.asapp.com                               | ASAPP service URLs                                                 |
| \*.ingest.sentry.io                        | Application performance monitoring tool                            |
| fonts.googleapis.com                       | Fonts                                                              |
| google-analytics.com                       | Page analytics                                                     |
| asapp-chat-sdk-production.s3.amazonaws.com | Static ASAPP AWS URL for desktop network connectivity health check |

## Integrate with Salesforce

### 1. Configure the Salesforce Organization Centrally

**Before You Begin**

You will need the following information to configure ASAPP for Salesforce:

* Administrator credentials to login to your Salesforce organization account.
  * **NOTE:** Organization and Administrator should be enabled for 'chat'.
* A URL for the ASAPP installation package, which will be provided by ASAPP.

  <Note>
    ASAPP provides the same install package for implementing both AI Compose and AI Summary in Salesforce. Use this guide to configure AI Compose.

    If you're looking to implement AI Summary, [use this guide](/ai-productivity/ai-summary/salesforce-plugin).
  </Note>
* API Id and API URL values, which can be found in your ASAPP Developer Portal account (developer.asapp.com) in the **Apps** section.

**Configuration Steps**

**1. Install the ASAPP Package**

* Open the package installation URL from ASAPP.
* Login with your Salesforce organization administrator credentials. The package installation page appears:
  <Frame>
    <img src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2e51b4cf-646c-4e67-42b2-4df188321f5f.png?fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=3b3453f446e56ddb5ff72e61eb376229" data-og-width="1048" width="1048" data-og-height="668" height="668" data-path="image/uuid-2e51b4cf-646c-4e67-42b2-4df188321f5f.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2e51b4cf-646c-4e67-42b2-4df188321f5f.png?w=280&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=ee00dc343ebe618c5e343aefe0659e9c 280w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2e51b4cf-646c-4e67-42b2-4df188321f5f.png?w=560&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=7bdcdc206dccace685967a6f87b5bfe1 560w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2e51b4cf-646c-4e67-42b2-4df188321f5f.png?w=840&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=a105b462b6a091ed4b336edff575825a 840w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2e51b4cf-646c-4e67-42b2-4df188321f5f.png?w=1100&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=8173e208a61d35a88a588b9ead7b8dff 1100w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2e51b4cf-646c-4e67-42b2-4df188321f5f.png?w=1650&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=b7f90eacd387ec82d077fa5aa5f665c9 1650w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2e51b4cf-646c-4e67-42b2-4df188321f5f.png?w=2500&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=1ce32a401725ccc87718532eee22c397 2500w" />
  </Frame>
* Choose **Install for All Users** (as shown above).
* Check the acknowledgment statement and click the **Install** button:
  <Frame>
    <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-efdaa3e5-109a-a6f1-46d9-fbc0777d7340.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=ac6e51a8691b073a193dc8e7ccc00f93" data-og-width="993" width="993" data-og-height="52" height="52" data-path="image/uuid-efdaa3e5-109a-a6f1-46d9-fbc0777d7340.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-efdaa3e5-109a-a6f1-46d9-fbc0777d7340.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=f60086d953b9233d91ef96fe955ecae1 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-efdaa3e5-109a-a6f1-46d9-fbc0777d7340.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=a9f598a88fa4166fe984108eb858f699 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-efdaa3e5-109a-a6f1-46d9-fbc0777d7340.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=3ebadd88f8dad52c7deead4557728e66 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-efdaa3e5-109a-a6f1-46d9-fbc0777d7340.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=9033c27fc2c859b09853c6890c96e3e3 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-efdaa3e5-109a-a6f1-46d9-fbc0777d7340.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=63b3985924d98ca5c3f37a0d4df9fcb0 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-efdaa3e5-109a-a6f1-46d9-fbc0777d7340.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=738fab3a61137016728453ae0949bfcc 2500w" />
  </Frame>
  <Frame>
    <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d6534373-fa62-f370-e790-fee74118bd80.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=e52dca54a2f61a7bb4c4449ad45d5ba6" data-og-width="101" width="101" data-og-height="57" height="57" data-path="image/uuid-d6534373-fa62-f370-e790-fee74118bd80.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d6534373-fa62-f370-e790-fee74118bd80.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=a9cc1ee976e72567a946265d0f966425 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d6534373-fa62-f370-e790-fee74118bd80.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=0fac8fb49a5a1dc352099d5f39e26c23 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d6534373-fa62-f370-e790-fee74118bd80.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=db234e38cd00bcd1d7058ffa50288a85 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d6534373-fa62-f370-e790-fee74118bd80.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=f81a126b7c3cd7bd96c191269a053424 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d6534373-fa62-f370-e790-fee74118bd80.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=5ad81f179a643934cee81ca6bcb28ffe 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d6534373-fa62-f370-e790-fee74118bd80.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=93c33a13e037bdc028fdc1495e1ca6cb 2500w" />
  </Frame>
* The Installation runs. An **Installation Complete!** message appears:
  <Frame>
    <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6c4df35c-6c3f-a1d2-b0cc-64b5d0aac3d9.png?fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=30b848a1afa7994b62afd9e4d5709c68" data-og-width="941" width="941" data-og-height="225" height="225" data-path="image/uuid-6c4df35c-6c3f-a1d2-b0cc-64b5d0aac3d9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6c4df35c-6c3f-a1d2-b0cc-64b5d0aac3d9.png?w=280&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=5b07db7a950980c6fa2075e7a51e0d06 280w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6c4df35c-6c3f-a1d2-b0cc-64b5d0aac3d9.png?w=560&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=07cd4ddd732110b5167550b31b566126 560w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6c4df35c-6c3f-a1d2-b0cc-64b5d0aac3d9.png?w=840&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=e5bf50f2d819a03d845a307ca6f3e3a3 840w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6c4df35c-6c3f-a1d2-b0cc-64b5d0aac3d9.png?w=1100&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=a73dbff25a1bfab56c8667df6165a5ef 1100w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6c4df35c-6c3f-a1d2-b0cc-64b5d0aac3d9.png?w=1650&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=9597bb87df097b59b96f54ef0201b29d 1650w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6c4df35c-6c3f-a1d2-b0cc-64b5d0aac3d9.png?w=2500&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=a4536c7577a0999d1f2e329697c15cb6 2500w" />
  </Frame>
  <Frame>
    <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-8229e206-9c06-70e3-af08-2a5c9b4373c3.png?fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=128008375db731bea3d9e24380e211c3" data-og-width="954" width="954" data-og-height="178" height="178" data-path="image/uuid-8229e206-9c06-70e3-af08-2a5c9b4373c3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-8229e206-9c06-70e3-af08-2a5c9b4373c3.png?w=280&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=7366ad5a52f7c945865d9775250c806a 280w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-8229e206-9c06-70e3-af08-2a5c9b4373c3.png?w=560&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=3e9054853b9266fb6089b7d6cdd389ed 560w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-8229e206-9c06-70e3-af08-2a5c9b4373c3.png?w=840&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=20213fe08a18dd0dd0b04112fc103323 840w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-8229e206-9c06-70e3-af08-2a5c9b4373c3.png?w=1100&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=e0014206d63056d06d8acf8816753dde 1100w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-8229e206-9c06-70e3-af08-2a5c9b4373c3.png?w=1650&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=b083e42e58b8f91dda72a56deed619a0 1650w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-8229e206-9c06-70e3-af08-2a5c9b4373c3.png?w=2500&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=b6f8c6b4af4b78ea1a3b13d26ea72dd6 2500w" />
  </Frame>
* Click the **Done** button.

**2. Add ASAPP to the Chat Transcript Page**

* Open the 'Service Console' page (or your chat page).
* Choose an existing chat session or start a new chat session so that the chat transcript page appears (the exact mechanism is organization-specific).
* In the top-right, click the **gear** icon, then right-click **Edit Page**, and **Open Link in a New Tab**.
  <Frame>
    <img src="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-16a63275-b025-59fc-3aa5-154a5ca10db6.png?fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=25c46727857f80c804b5420fc05e7532" data-og-width="381" width="381" data-og-height="492" height="492" data-path="image/uuid-16a63275-b025-59fc-3aa5-154a5ca10db6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-16a63275-b025-59fc-3aa5-154a5ca10db6.png?w=280&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=1742f2e2d551024b81d3f048683573b8 280w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-16a63275-b025-59fc-3aa5-154a5ca10db6.png?w=560&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=69dc7aefef2a43c3a4771ef61020cdae 560w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-16a63275-b025-59fc-3aa5-154a5ca10db6.png?w=840&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=3013226a4d76f3fed2b8561c61fd981c 840w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-16a63275-b025-59fc-3aa5-154a5ca10db6.png?w=1100&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=4b4269ae492aa9b5b863a0c33a9a6336 1100w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-16a63275-b025-59fc-3aa5-154a5ca10db6.png?w=1650&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=7d4bde5ecd421fe406e9921d3195db7e 1650w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-16a63275-b025-59fc-3aa5-154a5ca10db6.png?w=2500&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=e8e5c231066edade800a5a61e4052412 2500w" />
  </Frame>
* Navigate to the new tab to see the chat transcript edit page:
  <Frame>
    <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-412d4636-2ddf-33fd-04bb-598df2851636.png?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=6763ed8b39daad3645ef7becd83d0f46" data-og-width="1916" width="1916" data-og-height="975" height="975" data-path="image/uuid-412d4636-2ddf-33fd-04bb-598df2851636.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-412d4636-2ddf-33fd-04bb-598df2851636.png?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=47b47b4627df1d99e26b6976f926b9c8 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-412d4636-2ddf-33fd-04bb-598df2851636.png?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=118192043f9415cf5f15687f79fde365 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-412d4636-2ddf-33fd-04bb-598df2851636.png?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=ef0640d8670af5ffa581f32da1f1eca9 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-412d4636-2ddf-33fd-04bb-598df2851636.png?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=3b06a1383aa7807195effb7d56e6b40c 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-412d4636-2ddf-33fd-04bb-598df2851636.png?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=7ecf6ba64035bb324c5c06116e9cd8fb 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-412d4636-2ddf-33fd-04bb-598df2851636.png?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=596c39de7fde1620a370b84ce0027e91 2500w" />
  </Frame>
* Select the conversation panel (middle) and delete it.
  <Frame>
    <img src="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-082909fc-339c-417c-2ba6-af6de29ef281.png?fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=7ec2b11ed0c1bcbf01216c8118c3d9f9" data-og-width="873" width="873" data-og-height="575" height="575" data-path="image/uuid-082909fc-339c-417c-2ba6-af6de29ef281.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-082909fc-339c-417c-2ba6-af6de29ef281.png?w=280&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=b9a751e99f70869e9adb3be74e344d96 280w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-082909fc-339c-417c-2ba6-af6de29ef281.png?w=560&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=831a5fd2825273ec7023b42ed6627d02 560w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-082909fc-339c-417c-2ba6-af6de29ef281.png?w=840&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=41417ecfbd48b192c544612b11a78afc 840w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-082909fc-339c-417c-2ba6-af6de29ef281.png?w=1100&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=4c31a03d1db2d960e5d0b80ba80c4749 1100w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-082909fc-339c-417c-2ba6-af6de29ef281.png?w=1650&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=62630d9850a32662a8464d6daa1de30f 1650w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-082909fc-339c-417c-2ba6-af6de29ef281.png?w=2500&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=2c6add90cf9d931ece511abfd2bd635e 2500w" />
  </Frame>
* Drag the **chatAsapp** component (left), inside the conversation panel:
  <Frame>
    <img src="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-03d5534d-9513-e847-f942-8c11291b8806.png?fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=b8ea52284cb0cd4118857b3bf043d096" data-og-width="3584" width="3584" data-og-height="1780" height="1780" data-path="image/uuid-03d5534d-9513-e847-f942-8c11291b8806.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-03d5534d-9513-e847-f942-8c11291b8806.png?w=280&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=b10a555125cd6b9ed83e0876d84ef674 280w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-03d5534d-9513-e847-f942-8c11291b8806.png?w=560&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=3963ceb3e40a25632c5318d37a66c5f0 560w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-03d5534d-9513-e847-f942-8c11291b8806.png?w=840&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=f418a522023f61cccf2a611a6ee640e5 840w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-03d5534d-9513-e847-f942-8c11291b8806.png?w=1100&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=507a52d5d7c8ef3c7325c406bed50dd4 1100w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-03d5534d-9513-e847-f942-8c11291b8806.png?w=1650&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=208cfc129a5a4910b8f40237399a040d 1650w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-03d5534d-9513-e847-f942-8c11291b8806.png?w=2500&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=febe282162f7933273f6a1a44eca763c 2500w" />
  </Frame>
* Drag the **exploreAsapp** component (left), to the right column. Next, add your organization's **API key** and **API URL** (found in the ASAPP Developer Portal) in the rightmost panel:

  <Note>
    The API key is labeled as **API Id** in the ASAPP Developer Portal.

    The API URL should be listed as `https://api.sandbox.asapp.com` for lower environments and `https://api.asapp.com` for production.
  </Note>

  <Frame>
    <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-cba02769-7bfd-4046-7b89-f6e99d6e26da.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=5c7d7727374f04d8fa5c347bcf40e2c3" data-og-width="1916" width="1916" data-og-height="974" height="974" data-path="image/uuid-cba02769-7bfd-4046-7b89-f6e99d6e26da.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-cba02769-7bfd-4046-7b89-f6e99d6e26da.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=dd31ad6ea6acc2cd63da9e52a5053f14 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-cba02769-7bfd-4046-7b89-f6e99d6e26da.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=0bd5bde0cf623d7dda5a3792fa30cfd0 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-cba02769-7bfd-4046-7b89-f6e99d6e26da.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=e3ae59fdccd9f3f0afe12b24f88e0671 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-cba02769-7bfd-4046-7b89-f6e99d6e26da.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=c4a99801a6f0009a6bbdf9234c1d2bcd 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-cba02769-7bfd-4046-7b89-f6e99d6e26da.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=dd2c8f9e066b26472d69393263715f9a 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-cba02769-7bfd-4046-7b89-f6e99d6e26da.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=922f0562a5cb239b54d16a92e6586c2b 2500w" />
  </Frame>

  <Frame>
    <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b9a621e7-75d9-7dfe-7e62-08dd68fc00b2.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=ff25795d9228e39195dbf9c5b9237d57" data-og-width="841" width="841" data-og-height="623" height="623" data-path="image/uuid-b9a621e7-75d9-7dfe-7e62-08dd68fc00b2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b9a621e7-75d9-7dfe-7e62-08dd68fc00b2.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=08669c111bc13985da33c6b592d310e5 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b9a621e7-75d9-7dfe-7e62-08dd68fc00b2.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=6f0dd48d8bb9e3b86ff06db8b4ec743e 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b9a621e7-75d9-7dfe-7e62-08dd68fc00b2.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=be0e6c0092cbbe69c12f533489502591 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b9a621e7-75d9-7dfe-7e62-08dd68fc00b2.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=71b3fc2b65b3e7f6ccb3f757fd991f02 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b9a621e7-75d9-7dfe-7e62-08dd68fc00b2.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=3818055913c5b4b279ca8f3d7f2c2d3b 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-b9a621e7-75d9-7dfe-7e62-08dd68fc00b2.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=81da2d8428a86521a916f30f8cdab125 2500w" />
  </Frame>
* Click **Save**, then click **Activate**
  <Frame>
    <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8d13377b-ee60-0196-c713-224ee04d65cc.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=90c6adbf461d6e286c22fdc2b291521e" data-og-width="639" width="639" data-og-height="289" height="289" data-path="image/uuid-8d13377b-ee60-0196-c713-224ee04d65cc.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8d13377b-ee60-0196-c713-224ee04d65cc.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=3df65585d44e03a2e4e93bf961c0f653 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8d13377b-ee60-0196-c713-224ee04d65cc.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=b68db2f28b176f78db17f288e69b65f5 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8d13377b-ee60-0196-c713-224ee04d65cc.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=c97b1f2150a36a4e0bf08952123d100a 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8d13377b-ee60-0196-c713-224ee04d65cc.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=d0fab91d5f23fa63c18447c0aba7c41d 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8d13377b-ee60-0196-c713-224ee04d65cc.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=344ca936f8a50066d6c72dda8f170f53 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8d13377b-ee60-0196-c713-224ee04d65cc.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=87b31690976fd7f847c68befc3bd4383 2500w" />
  </Frame>
* Click **Assign as org default**.
  <Frame>
    <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e2227892-55f8-1c17-16c7-61a1895bf19c.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=a8afc23ad01706158397d073750e5fd2" data-og-width="961" width="961" data-og-height="525" height="525" data-path="image/uuid-e2227892-55f8-1c17-16c7-61a1895bf19c.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e2227892-55f8-1c17-16c7-61a1895bf19c.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=769ddaf716801a57c6dab9ddd4c35d1b 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e2227892-55f8-1c17-16c7-61a1895bf19c.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=f4976bf06c8d1d4deb39407627c18164 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e2227892-55f8-1c17-16c7-61a1895bf19c.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=195a06632129edc20e939ff64b877a8f 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e2227892-55f8-1c17-16c7-61a1895bf19c.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=dd8ac6c40c09299e02796eaf4f0f039e 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e2227892-55f8-1c17-16c7-61a1895bf19c.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=8de4d5a833e7dee04bd137e405e8ce05 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e2227892-55f8-1c17-16c7-61a1895bf19c.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=d19d4657e22a6bb63073416e7c6d77cd 2500w" />
  </Frame>
* Choose the **Desktop** form factor, then click **Save**.
  <Frame>
    <img src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-25a3c7b0-9a58-97be-28a4-799e4de6f3f3.png?fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=896ff7c3620357aa1344554a8be3a597" data-og-width="649" width="649" data-og-height="187" height="187" data-path="image/uuid-25a3c7b0-9a58-97be-28a4-799e4de6f3f3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-25a3c7b0-9a58-97be-28a4-799e4de6f3f3.png?w=280&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=70307c8fdbea17186274b84dcc6c3099 280w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-25a3c7b0-9a58-97be-28a4-799e4de6f3f3.png?w=560&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=50c9bbe471bc45564b832947a34987bd 560w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-25a3c7b0-9a58-97be-28a4-799e4de6f3f3.png?w=840&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=90203eba34107d8681284872f93f0151 840w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-25a3c7b0-9a58-97be-28a4-799e4de6f3f3.png?w=1100&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=d8e621f5e3883d46b51805bd815d0fb4 1100w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-25a3c7b0-9a58-97be-28a4-799e4de6f3f3.png?w=1650&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=4f0ce6f6b2fcda2f3c5e001de9915363 1650w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-25a3c7b0-9a58-97be-28a4-799e4de6f3f3.png?w=2500&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=d9bc0545c1266f03a22095168386f62e 2500w" />
  </Frame>
* Return to the chat transcript page and refresh - the ASAPP composer should appear.
  <Frame>
    <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-419161db-4848-c498-a3b7-60faa0d0df6d.png?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=54389209b9d389168ef13571c6303701" data-og-width="1916" width="1916" data-og-height="974" height="974" data-path="image/uuid-419161db-4848-c498-a3b7-60faa0d0df6d.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-419161db-4848-c498-a3b7-60faa0d0df6d.png?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=4f2ef3f9c309abe1b0a3d7c68dd7d110 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-419161db-4848-c498-a3b7-60faa0d0df6d.png?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=66b8f050d1458b76bf33736ea0bc75ee 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-419161db-4848-c498-a3b7-60faa0d0df6d.png?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=28104196bcb19593d0d33eaf2337eeaf 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-419161db-4848-c498-a3b7-60faa0d0df6d.png?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=032488b1d123f2bc2159a85229e44c3f 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-419161db-4848-c498-a3b7-60faa0d0df6d.png?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=3524028b6645b30ae9d7a2b8f4769d50 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-419161db-4848-c498-a3b7-60faa0d0df6d.png?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=ff4bb692cd5a10ed5331980143f8d560 2500w" />
  </Frame>

### 2. Set Up Single Sign-On

ASAPP handles authentication through the customer's SSO service to confirm the identity of the agent.

ASAPP acts as the Service Provider (SP), with the customer acting as the Identity Provider (IDP). The customer's authentication system performs user authentication using their existing user credentials.

ASAPP supports SP-initiated SSO with either OIDC (preferred method) and SAML. Once the user initiates sign-in, ASAPP detects that the user is authenticated and requests an assertion from the customer's SSO service.

**Configuration Steps for OIDC (preferred method)**

1. Create a new IDP OIDC application with type `Web`

2. Set the following attributes for the app:
   <table class="informaltable frame-void rules-rows">
     <thead>
       <tr>
         <th class="th"><p>Attribute</p></th>
         <th class="th"><p>Value\*</p></th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td class="td"><p>Grant Type</p></td>
         <td class="td"><p>authorization code</p></td>
       </tr>

       <tr>
         <td class="td"><p>Sign-in Redirect URIs</p></td>

         <td class="td">
           <p>Production: `https://api.asapp.com/auth/v1/callback/\{company_marker\}`</p>
           <p>Sandbox: `https://api.sandbox.asapp.com/auth/v1/callback/\{company_marker\}-sandbox`</p>
         </td>
       </tr>
     </tbody>
   </table>
   **\*NOTE:** ASAPP to provide `company_marker` value

3. Save the application and send ASAPP the `Client ID` and `Client Secret` from the app through a secure communication channel

4. Set scopes for the OIDC application:
   * Required: `openid`
   * Preferred: `email`, `profile`

5. Tell ASAPP which end-user attribute should be used a unique identifier

6. Tell ASAPP your IDP domain name

**Configuration Steps for SAML**

1. Create a new IDP SAML application.
2. Set the following attributes for the app:

   | Attribute            | Value\*                                                                                                                                                                                                                                                                     |
   | :------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Single Sign On URL   | Production: `https://sso.asapp.com/auth/realms/standalone-{company_marker}-auth/broker/saml/endpoint/clients/asapp-sam`l <br /><br /> Sandbox: `https://sso.asapp.com/auth/realms/standalone-{company_marker}-auth/broker/saml-sandbox/endpoint/clients/asapp-saml-sandbox` |
   | Recipient URL        | Production: `https://sso.asapp.com/auth/realms/standalone-{company_marker}-auth/broker/saml/endpoint/clients/asapp-saml` <br /><br /> Sandbox: `https://sso.asapp.com/auth/realms/standalone-{company_marker}-auth/broker/saml-sandbox/endpoint/clients/asapp-saml-sandbox` |
   | Destination URL      | Production: `https://sso.asapp.com/auth/realms/standalone-{company_marker}-auth/broker/saml/endpoint/clients/asapp-saml` <br /><br /> Sandbox: `https://sso.asapp.com/auth/realms/standalone-{company_marker}-auth/broker/saml-sandbox/endpoint/clients/asapp-saml-sandbox` |
   | Audience Restriction | Production: `https://sso.asapp.com/auth/realms/standalone-{company_marker}-auth/broker/saml/endpoint/clients/asapp-saml` <br /><br /> Sandbox: `https://sso.asapp.com/auth/realms/standalone-{company_marker}-auth/broker/saml-sandbox/endpoint/clients/asapp-saml-sandbox` |
   | Response             | Signed                                                                                                                                                                                                                                                                      |
   | Assertion            | Signed                                                                                                                                                                                                                                                                      |
   | Signature Algorithm  | RSA\_SHA256                                                                                                                                                                                                                                                                 |
   | Digest Algorithm     | SHA256                                                                                                                                                                                                                                                                      |
   | Attribute Statements | externalUserId: `{unique_id_to_identify_the_user}`                                                                                                                                                                                                                          |

   **\*NOTE:** ASAPP to provide `company_marker` value
3. Save the application and send the Public Certificate to validate Signature for this app SAML payload to ASAPP team
4. Send ASAPP team the URL of the SAML application

### 3. Configure Auto-Pilot Greetings

If you so choose, you can work with your ASAPP contact to enable Auto-Pilot Greetings in your AI Compose installation.
Auto-Pilot Greetings automatically generates a greeting at the beginning of a conversation, and that greeting can be automatically sent to a customer on your agent's behalf after a configurable timer elapses.

Your ASAPP contact can:

* Turn Auto-Pilot Greetings on or off for your organization
* Set a countdown timer value after which the Auto-Pilot Greeting is sent if an agent does not cancel Auto-Pilot by typing or clicking a "cancel" button
* Set the global default messages that will be provided for Auto-Pilot Greetings across your organization (note that agents can optionally customize their Auto-Pilot Greetings messages within the Auto-Pilot tab of the AI Compose panel)

## Usage

### Customization

#### Conversation Attributes

Once the ASAPP AI Compose widget is embedded, Salesforce shares the following conversation attributes with ASAPP: customer name, agent name and skill.

ASAPP can use name attributes to populate values into templated responses (e.g. "Hi \[customer name], how can I help you today?") and to selectively filter response lists based on the skill of the conversation.

#### Conversation Redaction

When message text in the conversation transcript is sent to ASAPP, ASAPP applies redaction to the message text to prevent transmission of sensitive information. Reach out to your ASAPP account contact for information on available redaction capabilities to configure for your implementation.

#### Composer Placement

ASAPP currently targets Lightning desktops. Within Lightning-based desktops, you are free to place our composer wherever you choose. However, we suggest placing it immediately below the Salesforce conversation widget, such that the chat log appears above the ASAPP composer.

### Data Security

ASAPP's security protocols protect data at each point of transmission from first user authentication, to secure communications, to our auditing and logging system, all the way to securing the environment when data is at rest in the data logging system. Access to data by ASAPP teams is tightly constrained and monitored. Strict security protocols protect both ASAPP and our customers.

The following security controls are particularly relevant to AI Compose:

1. Client sessions are controlled using a time-limited authorization token. Privileges for each active session are controlled server-side to mitigate potential elevation-of-privilege and information disclosure risks.
2. To avoid unauthorized disclosure of information, unique, non-guessable IDs are used to identify conversations. These conversations can only be accessed using a valid client session.
3. Requests to API endpoints that can potentially receive sensitive data are put through a round of redaction to strip the request of sensitive data (like SSNs and phone numbers).

### Additional Considerations

#### Historical Conversation Data for Generating a Response List

ASAPP uses past agent conversations to generate a customized response list tailored to a given use case. In order to create an accurate and relevant list, ASAPP requires a minimum of 200,000 historical transcripts to be supplied ahead of implementing AI Compose.

For more information on how to transmit the conversation data, reach out to your ASAPP account contact.

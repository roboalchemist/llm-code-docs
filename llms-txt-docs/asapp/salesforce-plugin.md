# Source: https://docs.asapp.com/autosummary/salesforce-plugin.md

# Deploying AutoSummary for Salesforce

> Learn how to use the AutoSummary Salesforce plugin.

## Using This Guide

**Deployment Guides** describe the technical components of ASAPP services and provide information about how to interact with and implement these components in your organization.

## Overview

ASAPP AutoSummary generates a summary of each voice or messaging (chat) interaction between a customer and an agent. AutoSummary also generates Structured Data and intent outputs.

With automated interaction summaries, organizations reduce agent time and effort both during and after calls, and gain high-coverage summary data for future reference by agents, supervisors and quality teams.

<Note>
  AutoSummary currently supports English-language conversations only.
</Note>

### Technology

ASAPP AutoSummary has the following technical components:

* An AutoSummary model that ASAPP uses to generate summary text
* An ASAPP component that interfaces between ASAPP's AutoSummary and

Conversation APIs to generate summaries for each conversation.

<Frame>
  <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e7d605d0-27c4-490c-c4d7-88e9e44f2ee1.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=00818b92162b5fd47a8fcb1d0e33667a" data-og-width="1731" width="1731" data-og-height="1020" height="1020" data-path="image/uuid-e7d605d0-27c4-490c-c4d7-88e9e44f2ee1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e7d605d0-27c4-490c-c4d7-88e9e44f2ee1.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=f98719b4fbd9dbd81c0a6922dd366fa1 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e7d605d0-27c4-490c-c4d7-88e9e44f2ee1.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=8001c33f3d90e323135408e997ef4947 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e7d605d0-27c4-490c-c4d7-88e9e44f2ee1.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=15b73d4c2f33727ee43fc571417de047 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e7d605d0-27c4-490c-c4d7-88e9e44f2ee1.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=207b1eafcd4bd22036d594c3336bb5ea 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e7d605d0-27c4-490c-c4d7-88e9e44f2ee1.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=4639e55739d1f71ea23c10f19409aca8 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e7d605d0-27c4-490c-c4d7-88e9e44f2ee1.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=3b896f423370c21171aca43498249005 2500w" />
</Frame>

## Setup

### Requirements

**Browser Support**
ASAPP AutoSummary is supported in Google Chrome and Microsoft Edge
<Note>This support covers the latest version of each browser and extends to the previous two versions</Note>

Please consult your ASAPP account contact if your installation requires support for other browsers

**Salesforce**
ASAPP supports Lightning-based chat (cf. classic)

<Frame>
  <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c6a319ef-4846-1c14-7ea5-5294ed44e8e2.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=197eb06f56ad435844c348f0f301942a" data-og-width="191" width="191" data-og-height="32" height="32" data-path="image/uuid-c6a319ef-4846-1c14-7ea5-5294ed44e8e2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c6a319ef-4846-1c14-7ea5-5294ed44e8e2.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=812a40db36e9f8390b18c15f3b7977ad 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c6a319ef-4846-1c14-7ea5-5294ed44e8e2.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=24c7f94e3483a28349f0cefb3601218a 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c6a319ef-4846-1c14-7ea5-5294ed44e8e2.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=167ea98803418b1011579b66cffc2a72 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c6a319ef-4846-1c14-7ea5-5294ed44e8e2.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=68126a671b731ee790a310b14433900a 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c6a319ef-4846-1c14-7ea5-5294ed44e8e2.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=8fb760ccec36b09b563199e3c240fe16 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c6a319ef-4846-1c14-7ea5-5294ed44e8e2.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=46751a028f4e0f539ce6e15d31647ac0 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e66b3aab-d17a-a7dc-f607-4f8a9504db87.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=7a6329c3b8870b0efed7b970de0a601f" data-og-width="181" width="181" data-og-height="44" height="44" data-path="image/uuid-e66b3aab-d17a-a7dc-f607-4f8a9504db87.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e66b3aab-d17a-a7dc-f607-4f8a9504db87.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=2cdf631676264c6a0cd28c33d19f8fd9 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e66b3aab-d17a-a7dc-f607-4f8a9504db87.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=af8e4ca52570fb2dbfddb30bb4ef8071 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e66b3aab-d17a-a7dc-f607-4f8a9504db87.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=c223e60d25e0de5aa669e789eb6fc875 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e66b3aab-d17a-a7dc-f607-4f8a9504db87.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=921f044f140d97d019935bb6d30f3a85 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e66b3aab-d17a-a7dc-f607-4f8a9504db87.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=b8c50ccb0bb793d0b128c5737fc41950 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e66b3aab-d17a-a7dc-f607-4f8a9504db87.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=94b449d86bfc8684bd8a72504433b5a5 2500w" />
</Frame>

**SSO Support**
AutoSummary supports SP-initiated SSO with either OIDC (preferred method) or SAML.
**Domain Whitelisting**

In order for AutoSummary to interact with ASAPP's backend and third-party support services, the following domains need to be accessible from end-user environments:

| Domain                                       | Description                                                        |
| :------------------------------------------- | :----------------------------------------------------------------- |
| `*.asapp.com`                                | ASAPP service URLs                                                 |
| `*.ingest.sentry.io`                         | Application performance monitoring tool                            |
| `fonts.googleapis.com`                       | Fonts                                                              |
| `google-analytics.com`                       | Page analytics                                                     |
| `asapp-chat-sdk-production.s3.amazonaws.com` | Static ASAPP AWS URL for desktop network connectivity health check |

### Procedure

There are two parts to the AutoSummary setup process. Use the links below to skip to information about a specific part of the process:

1. [Configure the Salesforce organization](#1-configure-the-salesforce-organization-centrally-35766 "1. Configure the Salesforce Organization Centrally") centrally using an administrator account
2. [Setup agent/user authentication](#2-set-up-single-sign-on-sso-user-authentication-35766 "2. Set Up Single Sign-On (SSO) User Authentication") through the existing single sign-on (SSO) service

<Tip>
  Expected effort for each part of the setup process:

  * 1 hour for installation and configuration of the ASAPP chat components
  * 1-2 hours to enable user authentication, depending on SSO system complexity
</Tip>

#### 1. Configure the Salesforce Organization Centrally

**Before You Begin**
You will need the following information to configure ASAPP for Salesforce:

* Administrator credentials to login to your Salesforce organization account.
  * **NOTE:** Organization and Administrator should be enabled for 'chat'.
* A URL for the ASAPP installation package, which will be provided by ASAPP.

<Note>
  ASAPP provides the same install package for implementing both AutoCompose and AutoSummary in Salesforce. Use this guide to configure AutoSummary.

  If you're looking to implement AutoCompose, [use this guide](/autocompose/deploying-autocompose-for-salesforce).
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
  The API key is labeled as **API Id** in the ASAPP Developer Portal. The API URL should be listed as `https://api.sandbox.asapp.com` for lower environments and `https://api.asapp.com` for production.
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
* Choose **Desktop** form factor, then click **Save**.
  <Frame>
    <img src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-25a3c7b0-9a58-97be-28a4-799e4de6f3f3.png?fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=896ff7c3620357aa1344554a8be3a597" data-og-width="649" width="649" data-og-height="187" height="187" data-path="image/uuid-25a3c7b0-9a58-97be-28a4-799e4de6f3f3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-25a3c7b0-9a58-97be-28a4-799e4de6f3f3.png?w=280&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=70307c8fdbea17186274b84dcc6c3099 280w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-25a3c7b0-9a58-97be-28a4-799e4de6f3f3.png?w=560&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=50c9bbe471bc45564b832947a34987bd 560w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-25a3c7b0-9a58-97be-28a4-799e4de6f3f3.png?w=840&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=90203eba34107d8681284872f93f0151 840w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-25a3c7b0-9a58-97be-28a4-799e4de6f3f3.png?w=1100&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=d8e621f5e3883d46b51805bd815d0fb4 1100w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-25a3c7b0-9a58-97be-28a4-799e4de6f3f3.png?w=1650&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=4f0ce6f6b2fcda2f3c5e001de9915363 1650w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-25a3c7b0-9a58-97be-28a4-799e4de6f3f3.png?w=2500&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=d9bc0545c1266f03a22095168386f62e 2500w" />
  </Frame>
* Return to the chat transcript page and refresh - the ASAPP composer should appear.
  <Frame>
    <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-419161db-4848-c498-a3b7-60faa0d0df6d.png?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=54389209b9d389168ef13571c6303701" data-og-width="1916" width="1916" data-og-height="974" height="974" data-path="image/uuid-419161db-4848-c498-a3b7-60faa0d0df6d.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-419161db-4848-c498-a3b7-60faa0d0df6d.png?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=4f2ef3f9c309abe1b0a3d7c68dd7d110 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-419161db-4848-c498-a3b7-60faa0d0df6d.png?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=66b8f050d1458b76bf33736ea0bc75ee 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-419161db-4848-c498-a3b7-60faa0d0df6d.png?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=28104196bcb19593d0d33eaf2337eeaf 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-419161db-4848-c498-a3b7-60faa0d0df6d.png?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=032488b1d123f2bc2159a85229e44c3f 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-419161db-4848-c498-a3b7-60faa0d0df6d.png?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=3524028b6645b30ae9d7a2b8f4769d50 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-419161db-4848-c498-a3b7-60faa0d0df6d.png?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=ff4bb692cd5a10ed5331980143f8d560 2500w" />
  </Frame>

**3. Add a new Salesforce field to populate AutoSummary results**
AutoSummary writes only to the **Chat Transcript** object. You need to create a new field on the Chat Transcript object that will be used by the ASAPP component.

* Go to **Setup** > **Object Manager** > **Chat Transcript** > **Fields & Relationships** page (in this specific example, we choose to add the field for summarization on the Chat Transcript page).
* Click on the **New** button.
  <Frame>
    <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a74eb43e-d0b8-3fdd-6c19-b7fe2b380301.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=96e43b0e10add0745b11bec48c4b8d08" data-og-width="1600" width="1600" data-og-height="466" height="466" data-path="image/uuid-a74eb43e-d0b8-3fdd-6c19-b7fe2b380301.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a74eb43e-d0b8-3fdd-6c19-b7fe2b380301.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=2f13e7ef4d727038ed42f6ec38b45f7b 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a74eb43e-d0b8-3fdd-6c19-b7fe2b380301.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=20d14a5e06112ee47c194d7375557f6e 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a74eb43e-d0b8-3fdd-6c19-b7fe2b380301.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=2d7e7569071951d3237615c6742a3a25 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a74eb43e-d0b8-3fdd-6c19-b7fe2b380301.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=e715807011289b5bff67365e48b5a30e 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a74eb43e-d0b8-3fdd-6c19-b7fe2b380301.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=e53aa8deb03fb106408b77ad9759edfa 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a74eb43e-d0b8-3fdd-6c19-b7fe2b380301.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=091ec6ff027fb762164e1b0b498d6ad3 2500w" />
  </Frame>
* **Choose the field type (Step 1)**: we suggest setting this field as **Text Area (Long)**. Once this radio button is selected, click on the **Next** button.
* **Enter the field details (Step 2)**: Add a **Field Label** and a **Field Name**. Click **Next**.

<Note>
  Take note of this **Field Name**, as it will be needed when setting up the AutoSummary widget.
</Note>

<Frame>
  <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-85e7878d-743e-852a-fdff-13534d84864c.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=b12357512d69402f3d9c376b9195f8da" data-og-width="1600" width="1600" data-og-height="795" height="795" data-path="image/uuid-85e7878d-743e-852a-fdff-13534d84864c.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-85e7878d-743e-852a-fdff-13534d84864c.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=74a70219a57933280e129342bb500387 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-85e7878d-743e-852a-fdff-13534d84864c.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=c3b85e7aca5e1c6adb077c216042f6fb 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-85e7878d-743e-852a-fdff-13534d84864c.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=d198d624419e115bdb38043d62c273e4 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-85e7878d-743e-852a-fdff-13534d84864c.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=5a5d7517635d8d1eec0bb3586444eaea 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-85e7878d-743e-852a-fdff-13534d84864c.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=17921b1dad468c93b46ffccc73630f00 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-85e7878d-743e-852a-fdff-13534d84864c.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=e82c2e04d3a336d7e530ca7fae883914 2500w" />
</Frame>

* **Establish field-level security (Step 3)**: no need to modify anything. Click on **Next**.
* **Add to page layouts (Step 4)**: ensure to add the new field to page layouts for this implementation and then click **Save**.
* Once created, you will be able to see the field on the following page:
  <Frame>
    <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3a15836c-3204-4032-82fc-1cf486a1532f.png?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=8f73c918c5be01c9067b38639fbd715b" data-og-width="1600" width="1600" data-og-height="521" height="521" data-path="image/uuid-3a15836c-3204-4032-82fc-1cf486a1532f.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3a15836c-3204-4032-82fc-1cf486a1532f.png?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=ef8e0826d88e1833b90bf14d5601babd 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3a15836c-3204-4032-82fc-1cf486a1532f.png?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=3ad90232381134eb1a6313c92b300211 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3a15836c-3204-4032-82fc-1cf486a1532f.png?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=0d4a6443ed8429d50843ac7c65d8a905 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3a15836c-3204-4032-82fc-1cf486a1532f.png?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=9f0e9eb44260ced7a9af2f87f1a6281a 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3a15836c-3204-4032-82fc-1cf486a1532f.png?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=1c651b6ce84c78bf882dce1caec7c1ec 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-3a15836c-3204-4032-82fc-1cf486a1532f.png?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=2595885a1bd1597f441e81b00669e34e 2500w" />
  </Frame>

**4. Configure AutoSummary Widget**

* On the Service Console page, click on **Configuration** (gear icon) and then click **Edit Page**.
  <Frame>
    <img src="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-156e16ea-d143-b711-53ea-9da9667357fd.png?fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=533089be02c29a2b76d4ed5adb0a1a70" data-og-width="1600" width="1600" data-og-height="848" height="848" data-path="image/uuid-156e16ea-d143-b711-53ea-9da9667357fd.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-156e16ea-d143-b711-53ea-9da9667357fd.png?w=280&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=1683097fb296a026e2471caf41ad20b9 280w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-156e16ea-d143-b711-53ea-9da9667357fd.png?w=560&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=210828ce9482d459e6a0a2cad466d733 560w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-156e16ea-d143-b711-53ea-9da9667357fd.png?w=840&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=5c7abe4e96ec4b01cc95eff14f3fd4bf 840w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-156e16ea-d143-b711-53ea-9da9667357fd.png?w=1100&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=33f6fa53c10950fff9f86dda3812eba9 1100w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-156e16ea-d143-b711-53ea-9da9667357fd.png?w=1650&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=4ac5f9ff4078e5807d6adc02e034f2a1 1650w, https://mintcdn.com/asapp/9jlDT2iVQhMOPce8/image/uuid-156e16ea-d143-b711-53ea-9da9667357fd.png?w=2500&fit=max&auto=format&n=9jlDT2iVQhMOPce8&q=85&s=c3461854ef15553e154e644fd14a7316 2500w" />
  </Frame>
* Click the **ASAPP** panel. Then the configuration panel will appear on the right of the page. Enter the following information into the fields:
  * **API key**: this is the **API Id** found in the ASAPP Developer Portal.
  * **API URL**: this is found in the ASAPP Developer Portal; use `https://api.sandbox.asapp.com` in lower environments and `https://api.asapp.com`in production.
  * Select the checkbox for **ASAPP AutoSummary**.
  * **ASAPP AutoSummary field**: enter the **Field Name** created as part of Step 3. This is the field where the ASAPP-generated summary will appear.
  <Frame>
    <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8b35fadc-df1f-2b55-8428-d1918d2a4f3b.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=60ea6e6f6d35f50399f17700bd49951e" data-og-width="1599" width="1599" data-og-height="936" height="936" data-path="image/uuid-8b35fadc-df1f-2b55-8428-d1918d2a4f3b.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8b35fadc-df1f-2b55-8428-d1918d2a4f3b.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=7895e1b85a773de0d201dec2d5255d88 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8b35fadc-df1f-2b55-8428-d1918d2a4f3b.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=77cd9e9398efd4eb6006ed8a6ce042d4 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8b35fadc-df1f-2b55-8428-d1918d2a4f3b.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=5537610d5bab9ed985816157773d60ea 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8b35fadc-df1f-2b55-8428-d1918d2a4f3b.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=409737410f58485022a05fcbcfb86bbf 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8b35fadc-df1f-2b55-8428-d1918d2a4f3b.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=2c926f3499331331f07c8a4ac65c21e4 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8b35fadc-df1f-2b55-8428-d1918d2a4f3b.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=384c8eb3807ea72de051b44a3390e624 2500w" />
  </Frame>
  <Frame>
    <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-96d8db8f-687d-5672-2a44-28c8021f4ef7.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=f56609585aaa9b7f190543665486c806" data-og-width="695" width="695" data-og-height="520" height="520" data-path="image/uuid-96d8db8f-687d-5672-2a44-28c8021f4ef7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-96d8db8f-687d-5672-2a44-28c8021f4ef7.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=88b2674298d70f687c52ffc0631c99a0 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-96d8db8f-687d-5672-2a44-28c8021f4ef7.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=2061d79c286f4d698eb1a70e4ae01486 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-96d8db8f-687d-5672-2a44-28c8021f4ef7.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=c208f57717733e9f40c010edc177ee8b 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-96d8db8f-687d-5672-2a44-28c8021f4ef7.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=f3eb3bc9316519a8133f7fd7de64cdab 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-96d8db8f-687d-5672-2a44-28c8021f4ef7.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=c3d612336f57ff01ca94636294c982cf 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-96d8db8f-687d-5672-2a44-28c8021f4ef7.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=6491b319f44205dc0e258849fccbecd2 2500w" />
  </Frame>
* Click on the **Save** button to apply the changes.
  These configuration steps add the AutoSummary field to the Chat Transcript object. From this point forward, you may use this summary field as part of your agent-facing or internal summary data use case. A common use case is to display this field to the agent in the Record Detail widget.
  **5. Add Record Detail Widget (OPTIONAL)**
* If the Record Detail widget is not already on the Chat Transcript page, drag the **Record Detail** widget from the left panel and place it on the page.
* Click on the **Save** button to apply the changes.
* Refresh the page to see the changes applied to the page.
  The AutoSummary field should now be visible under the **Transcription** section of the Record Detail widget. Once the conversation is ended, summarization will be displayed in this newly configured field in the Record Detail widget.

#### 2. Set Up Single Sign-On (SSO) User Authentication

ASAPP handles authentication through the customer's SSO service to confirm the identity of the agent.

ASAPP acts as the Service Provider (SP) with the customer acting as the Identity Provider (IDP). The customer's authentication system performs user authentication using their existing user credentials.

ASAPP supports SP-initiated SSO with either OIDC (preferred method) and SAML. Once the user initiates sign-in, ASAPP detects that the user is authenticated and requests an assertion from the customer's SSO service.

**Configuration Steps for OIDC (preferred method)**

1. Create a new IDP OIDC application with type `Web`
2. Set the following attributes for the app:

   | Attribute             | Value\*                                                                                                                                                                            |
   | :-------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Grant Type            | authorization code                                                                                                                                                                 |
   | Sign-in Redirect URIs | <ul><li>Production: `https://api.asapp.com/auth/v1/callback/{company_marker}`</li><li>Sandbox: `https://api.sandbox.asapp.com/auth/v1/callback/{company_marker}-sandbox`</li></ul> |

   <Note> ASAPP to provide `company_marker` value</Note>
3. Save the application and send ASAPP the `Client ID` and `Client Secret` from the app through a secure communication channel
4. Set scopes for the OIDC application:
   * Required: `openid`
   * Preferred: `email`, `profile`
5. Tell ASAPP which end-user attribute should be used a unique identifier
6. Tell ASAPP your IDP domain name
   **Configuration Steps for SAML**
7. Create a new IDP SAML application.
8. Set the following attributes for the app:

   | Attribute            | Value\*                                                                                                                                                                                                                                                                                  |
   | :------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Single Sign On URL   | <ul><li>Production: `https://sso.asapp.com/auth/realms/standalone-{company_marker}-auth/broker/saml/endpoint/clients/asapp-saml`</li><li>Sandbox: `https://sso.asapp.com/auth/realms/standalone-{company_marker}-auth/broker/saml-sandbox/endpoint/clients/asapp-saml-sandbox`</li></ul> |
   | Recipient URL        | <ul><li>Production: `https://sso.asapp.com/auth/realms/standalone-{company_marker}-auth/broker/saml/endpoint/clients/asapp-saml`</li><li>Sandbox: `https://sso.asapp.com/auth/realms/standalone-{company_marker}-auth/broker/saml-sandbox/endpoint/clients/asapp-saml-sandbox`</li></ul> |
   | Destination URL      | <ul><li>Production: `https://sso.asapp.com/auth/realms/standalone-{company_marker}-auth/broker/saml/endpoint/clients/asapp-saml`</li><li>Sandbox: `https://sso.asapp.com/auth/realms/standalone-{company_marker}-auth/broker/saml-sandbox/endpoint/clients/asapp-saml-sandbox`</li></ul> |
   | Audience Restriction | <ul><li>Production: `https://sso.asapp.com/auth/realms/standalone-{company_marker}-auth/broker/saml/endpoint/clients/asapp-saml`</li><li>Sandbox: `https://sso.asapp.com/auth/realms/standalone-{company_marker}-auth/broker/saml-sandbox/endpoint/clients/asapp-saml-sandbox`</li></ul> |
   | Response             | Signed                                                                                                                                                                                                                                                                                   |
   | Assertion            | Signed                                                                                                                                                                                                                                                                                   |
   | Signature Algorithm  | RSA\_SHA256                                                                                                                                                                                                                                                                              |
   | Digest Algorithm     | SHA256                                                                                                                                                                                                                                                                                   |
   | Attribute Statements | externalUserId: {unique_id_to_identify_the_user}                                                                                                                                                                                                                                         |

   <Note> ASAPP to provide `company_marker` value</Note>
9. Save the application and send the Public Certificate to validate Signature for this app SAML payload to ASAPP team
10. Send ASAPP team the URL of the SAML application

## Usage

### Customization

#### Historical Transcripts for Summary Model Customization

ASAPP uses past agent conversations to generate a customized summary model that is tailored to a given use case. In order to create a customized summary model, ASAPP requires a minimum of 500 representative historical transcripts to generate free-text summaries. Transcripts should identify both the agent and customer messages.

<Note>
  Proper transcript formatting and sampling ensures data is usable for model training. Please ensure transcripts conform to the following:
  **Formatting**

  * Each utterance is clearly demarcated and sent by one identified sender
  * Utterances are in chronological order and complete, from beginning to very end of the conversation
  * Where possible, transcripts include the full content of the conversation rather than an abbreviated version. For example, in a digital messaging conversation:
    <table class="informaltable frame-void rules-rows">
      <thead>
        <tr>
          <th class="th"><p>Full</p></th>
          <th class="th"><p>Abbreviated</p></th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td class="td">
            <p><strong>Agent</strong>: Choose an option from the list below</p>
            <p><strong>Agent</strong>: (A) 1-way ticket (B) 2-way ticket (C) None of the above</p>
            <p><strong>Customer</strong>: (A) 1-way ticket</p>
          </td>

          <td class="td">
            <p><strong>Agent</strong>: Choose an option from the list below</p>
            <p><strong>Customer</strong>: (A)</p>
          </td>
        </tr>
      </tbody>
    </table>

  **Sampling**

  * Transcripts are from a wide range of dates to avoid seasonality effects; random sampling over a 12-month period is recommended
  * Transcripts mimic the production conversations on which models will be used - same types of participants, same channel (voice, messaging), same business unit
  * There are no duplicate transcripts
</Note>

For more information on how to transmit the conversation data, reach out to your ASAPP account contact.
Visit [Transmitting Data to SFTP](/reporting/send-sftp) for instructions on how to send historical transcripts to ASAPP.

#### Conversation Redaction

When message text in the conversation transcript is sent to ASAPP, ASAPP applies redaction to the message text to prevent transmission of sensitive information. Reach out to your ASAPP account contact for information on available redaction capabilities to configure for your implementation.

### Data Security

ASAPP's security protocols protect data at each point of transmission from first user authentication, to secure communications, to our auditing and logging system, all the way to securing the environment when data is at rest in the data logging system. Access to data by ASAPP teams is tightly constrained and monitored. Strict security protocols protect both ASAPP and our customers.
The following security controls are particularly relevant to AutoCompose:

1. Client sessions are controlled using a time-limited authorization token. Privileges for each active session are controlled server-side to mitigate potential elevation-of-privilege and information disclosure risks.
2. To avoid unauthorized disclosure of information, unique, non-guessable IDs are used to identify conversations. These conversations can only be accessed using a valid client session.
3. Requests to API endpoints that can potentially receive sensitive data are put through a round of redaction to strip the request of sensitive data (like SSNs and phone numbers).

# Source: https://www.aptible.com/docs/getting-started/deploy-starter-template/node-js.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Node.js + Express - Starter Template

> Deploy a starter template Node.js app using the Express framework on Aptible

<CardGroup cols={3}>
  <Card title="Deploy Now" icon="rocket" href="https://app.aptible.com/create" />

  <Card title="GitHub Repo" icon="github" href="https://github.com/aptible/template-express" />

  <Card title="View Example" icon="browser" href="https://app-52737.on-aptible.com/" />
</CardGroup>

# Overview

The following guide is designed to help you deploy a sample [Node.js](https://nodejs.org/) app using the [Express framework](https://expressjs.com/) from the Aptible Dashboard.

# Deploying the template

<Info> Prerequisite: Ensure you have [Git](https://git-scm.com/downloads) installed. </Info>

Using the [Deploy Code](https://app.aptible.com/create) tool in the Aptible Dashboard, you can deploy the **Express Template**. The tool will guide you through the following:

<Steps>
  <Step title="Deploy with Git Push">
        <img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node1.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=d2515d892b7f9567751f8a4c6d08955f" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/node1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node1.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=2a401f5771cf355d7021f77f50a6739a 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node1.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=b743683b59ee1e24b4863dbdabd2266e 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node1.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=a39956623b0d9be157e0d718eb6f3545 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node1.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=e042384b702b403ae5629d4d1159526d 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node1.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=e73b73ae634d31199317f33c9f87c68d 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node1.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=75bf8761266c5babffeed9812fbafbf6 2500w" />
  </Step>

  <Step title="Add an SSH key">
    <img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node2.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=f6317e159d372b927e2f6fe776c3ee7a" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/node2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node2.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=6b040e96cddb850be3fac3cd9b99e70a 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node2.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=008521d1fba94cf9aba0445889713283 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node2.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=9339b404627c518a77eaa61cdbdb31a8 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node2.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=8113bb5151bd05afee387aea2fd02068 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node2.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=6a2fca1eccdde3e0e58036da05d05517 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node2.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=56455a5296e00e013d5bcbe618a75f4e 2500w" />
    If you have not done so already, you will be prompted to set up an [SSH key](/core-concepts/security-compliance/authentication/ssh-keys#ssh-keys).
  </Step>

  <Step title="Environment Setup">
        <img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node3.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=be3bfb9b4c3a3f6ba39adde4ed70085d" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/node3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node3.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=53e92535701a434f26c06d3277fcddab 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node3.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=67cea008d4161c7452a5122b26c94e94 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node3.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=386980ac21e5ab342195e3cc9e03fb99 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node3.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=fb2ce9499b01636087b7811f339b90d8 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node3.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=002fb394003403ea14b386d6d88a1604 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node3.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=b18084d018f80039e116ddf6eb942fd8 2500w" />\
    Select your [Stack](/core-concepts/architecture/stacks) to deploy your resources. This will determine what region your resources are deployed to. Then, name the [Environment](/core-concepts/architecture/environments) your resources will be grouped into.
  </Step>

  <Step title="Prepare the template">
    <img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node4.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=d5fd4b9033690c9daad39d9159a94ec1" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/node4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node4.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=f1032f6f78c968bbd4ade14dcec03110 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node4.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=36532c32d33472df17e5d9c07185574f 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node4.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=16f613df12b63c8a030ffe5526f7d25f 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node4.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=0d90a76741861a56874c46875af52b4c 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node4.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=9d2214d9635dc78b3acef0572b38b62d 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node4.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=cb95d07914b98e968307b474b15d2f9a 2500w" />
    Select **Express Template** for deployment, and follow command-line instructions.
  </Step>

  <Step title="Fill environment variables and deploy">
        <img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node5.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=71400219e31addf9b926b1dc04683cb3" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/node5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node5.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=6f1ab398bb55bac09d3c9f381f232ea4 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node5.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=ae83f4a44790dcca8d81fbd6acbec9b3 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node5.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=fdd1bfdf97e18952411b7cdcf2ba1f08 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node5.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=fc3266ee9e7f8dcac91167f09d53bfac 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node5.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=051ae7478d14700333a519be741f1c4e 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node5.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=5cc2588f7de3e2f8caa93b5ef90c743a 2500w" />

    Aptible will automatically fill this template's required databases, services, and app's configuration with environment variable keys for you to fill with values. Once complete, save and deploy the code!

    Aptible will stream logs to you in live time:
    <img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node6.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=1361b40e7b55dce2ce872e0fe12b7ae6" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/node6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node6.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=33085246283a46c29c0c1d7512c3a683 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node6.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=1714b2613ea018dfc42ec8acb0b2541c 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node6.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=d2496fbeb91e2457dfd6be25e2257a54 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node6.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=55fd9727cdd214ac411770e829375e83 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node6.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=5582f7c4f08d85f43060ca3b6a3b4ff0 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node6.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=ef9c585a1e920d89f78306d1729da771 2500w" />
  </Step>

  <Step title="Expose your app to the internet">
    <img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node7.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=656b0e1c2e7987dc335538b3d70d598d" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/node7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node7.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=c062d04c143ad4b871dc49f50fe29318 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node7.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=7379a79d1024742177e57cc8ad419d32 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node7.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=ab4ea40b5d986a205575bff1ad11228a 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node7.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=191247ee12cf933c6a8e969705aa6aab 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node7.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=f9deeeb4218cf2fd53d69deb3ad3221e 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node7.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=9cb8eb29a590c2437fac4fcb3b97b97a 2500w" />
    Now that your code is deployed, it's time to expose your app to the internet. Select the service that needs an [endpoint](/core-concepts/apps/connecting-to-apps/app-endpoints/overview), and Aptible will automatically provision a managed endpoint.
  </Step>

  <Step title="View your deployed app" icon="party-horn">
        <img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node8.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=78ef220e736fb8e4cf8083a1db202db3" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/node8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node8.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=eb51fa064e35a81b6c40b6c9541face8 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node8.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=0d3db0a59f4013ce7bdca549d182a841 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node8.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=c885b19b038edad3ddc9280284890eea 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node8.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=22165897fe59a1c5d69c4bedab746b82 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node8.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=0aacd7cfce8d690a2d5e399ed6bc41f4 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/node8.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=bab597866ddae202eb7b06e395efebce 2500w" />
  </Step>
</Steps>

# Continue your journey

<Card title="Deploy custom code" icon="books" iconType="duotone" href="https://www.aptible.com/docs/custom-code-quickstart">
  Read our guide for deploying custom code on Aptible.
</Card>

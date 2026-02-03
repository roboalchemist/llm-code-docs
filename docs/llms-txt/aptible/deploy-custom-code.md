# Source: https://www.aptible.com/docs/getting-started/deploy-custom-code.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy your custom code

> Learn how to deploy your custom code on Aptible

## Overview

The following guide is designed to help you deploy custom code on Aptible. During this process, Aptible will launch containers to run your custom app and Managed Databases for any data stores, like PostgreSQL, Redis, etc., that your app requires to run.

## Compatibility

Aptible supports many frameworks; you can deploy any code that meets the following requirements:

* **Apps must run on Linux in Docker containers**

  * To run an app on Aptible, you must provide Aptible with a Dockerfile. To that extent, all apps on Aptible must be able to run Linux in Docker containers.
    <Tip> New to Docker? [Check out Docker’s getting started guide](https://docs.docker.com/get-started/).</Tip>

* **Apps may only receive traffic over HTTP or TCP.**

  * App endpoints (load balancers) are how you expose your Aptible app to the Internet. These endpoints only support traffic received over HTTP or TCP. While you cannot serve UDP services from Aptible, you may still connect to UDP services (such as DNS, SNMP, etc.) from apps hosted on Aptible.

* **Apps must not depend on persistent storage.**

  * App containers on Aptible are ephemeral and cannot be used for data persistence. To store your data with persistence, we recommend using a [Database](http://aptible.com/docs/databases) or third-party storage solution, such as AWS S3. Apps that rely on persistent local storage or a volume shared between multiple containers must be re-architected to run on Aptible. If you have questions about doing so, contact [Aptible Support](/how-to-guides/troubleshooting/aptible-support) for assistance.

# Deploy Code

<Info>Prerequisites: Ensure you have [Git](https://git-scm.com/downloads) installed, a Git repository with your application code, and a [Dockerfile](/core-concepts/apps/deploying-apps/image/deploying-with-git/overview) ready to deploy.</Info>

Using the Deploy Code tool in the Aptible Dashboard, you can deploy Custom Code. The tool will guide you through the following:

<Steps>
  <Step title="Deploy with Git Push">
        <img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code1.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=e05a3f6c5952e32364be7ad30092a51d" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/custom-code1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code1.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=ffc5eb4200fa5fb9acb20d0212f8f01a 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code1.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=49ffb07a036801cbd59268822610b3e0 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code1.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=21ddf7b1061c4b7dc84ede2369b0faf1 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code1.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=00e247c9a3cf99681725ccd3862e10df 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code1.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=c6cdadd5d731e7687af9f877cd5fe531 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code1.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=e4c993fe2a870cf3b876635b912cc61a 2500w" />
  </Step>

  <Step title="Add an SSH key">
    <img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code2.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=a6203ba1bb8d2992ea129a4e53a63f83" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/custom-code2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code2.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=b0cef4ae9f082c0cda66fc36ca769fe0 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code2.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=4d692307d6e2bf7f506956a7c5fb104b 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code2.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=0b440558a5bfef1cac0ffd6820107941 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code2.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=1126c4fd35e6414a6893ed82ec8d9048 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code2.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=13ccffa65d3f58a704ac5d7c39332fa9 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code2.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=7c3b3c9d1ef05232adcc52d7df07361a 2500w" />
    If you have not done so already, you will be prompted to set up an [SSH key](/core-concepts/security-compliance/authentication/ssh-keys#ssh-keys).
  </Step>

  <Step title="Environment Setup">
    <img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code3.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=482bd8b4ad7900c8590f6a014963d110" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/custom-code3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code3.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=ae0406e974caf43969986c358bd53623 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code3.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=ae01e7950b1df27c3ad979111f03a3b8 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code3.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=262043e89523121cd322294253c33e52 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code3.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=0b1464327c6a19684af68c34e33f3dfd 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code3.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=a052d552eebc21b2bad35122b0deb5b2 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code3.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=ee58aa2711fd3e2f5c365631756a9661 2500w" />
    Select your [stack](/core-concepts/architecture/stacks) to deploy your resources. This will determine what region your resources are deployed to. Then, name the [environment](/core-concepts/architecture/environments) your resources will be grouped into.
  </Step>

  <Step title="Push your code to Aptible">
    <img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code4.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=8444bf4b0fd18982a776ed6cc5bf4cef" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/custom-code4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code4.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=c40cdc919f5ef480ddfed953795e6f54 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code4.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=3262f0b74ee620408eca37b29ed5b277 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code4.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=183c944d3e870c504d1ecd34ef89071b 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code4.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=5204bfbe428b92a076cbd5eac7156a1e 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code4.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=6eddfe817baaa0fe33f445ad55dc860a 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code4.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=56b0a7cc7bcb5e300f65449f9e75b6c8 2500w" />
    Select **Custom Code** deployment, and from your command-line interface, add Aptible’s Git Server and push your code to our scan branch using the commands in the Aptible Dashboard
  </Step>

  <Step title="Provision a database and configure your app">
    <img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code5.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=33fa6e8e398d9e9eb9c07afd516c3d55" alt="" data-og-width="2000" width="2000" data-og-height="2000" height="2000" data-path="images/custom-code5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code5.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=94892ebaccf5a9f9c75384aa9c6ab1e7 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code5.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=339f44d415df8b7a9fcef90ef1289bdc 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code5.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=aced248575e0f9b88ef77226a6d4be42 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code5.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=bbfcabeda6804cfef82cccaa5dd28d76 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code5.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=a21fb993fdd74c5ae7bbc5dc7d2d38e3 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code5.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=2937558d696be335c0ffa66702386004 2500w" />
    Optionally, provision a database, configure your app with [environment variables](/core-concepts/apps/deploying-apps/configuration#configuration-variables), or add additional [services](/core-concepts/apps/deploying-apps/services) and commands.
  </Step>

  <Step title="Deploy your code and view logs">
    <img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code6.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=482c422d89425642f6c8028ebec5b5f0" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/custom-code6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code6.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=947dd7090945a4c15bcd15dd3ad6587c 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code6.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=1934419257a8420b5e8d20c9984fba03 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code6.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=766d371a4a1ab2e4c44c6903f889a2e0 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code6.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=736e712cb5cc741434a7f99a78f245ea 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code6.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=ee4340c04101cd2dd386ad26fae0b549 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code6.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=52291daaed610bf7745f4bf41991d9f1 2500w" />
    Deploy your code and view [logs](/core-concepts/observability/logs/overview) in real time
  </Step>

  <Step title="Expose your app to the internet">
    <img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code7.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=0a086642589af4f75d61ff01424c4cac" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/custom-code7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code7.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=74586b1e02af7c2fc872ec2dd24125fd 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code7.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=1b50f5c0b76330fabbba86cb2ab64cfe 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code7.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=c3fd450c02667f9da49fbd063a438974 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code7.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=68d9412ae12f303ab2fdbd3446f01fd7 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code7.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=d7bdcd757419b272210aad0ed6a9e1a5 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/custom-code7.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=67082da4370c6996280175619ec6b7e4 2500w" />
    Now that your code is deployed, it's time to expose your app to the internet. Select the service that needs an [endpoint](/core-concepts/apps/connecting-to-apps/app-endpoints/overview), and Aptible will automatically provision a managed endpoint.
  </Step>

  <Step title="View your deployed app 🎉" icon="party-horn" />
</Steps>

# Source: https://www.aptible.com/docs/getting-started/deploy-starter-template/php-laravel.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# PHP + Laravel - Starter Template

> Deploy a starter template PHP app using the Laravel framework on Aptible

<CardGroup cols={3}>
  <Card title="Deploy Now" icon="rocket" href="https://app.aptible.com/create" />

  <Card title="GitHub Repo" icon="github" href="https://github.com/aptible/template-laravel" />

  <Card title="View Live Example" icon="browser" href="https://app-52756.on-aptible.com/" />
</CardGroup>

# Overview

This guide will walk you through the process of launching a PHP app using the [Laravel framework](https://laravel.com/).

# Deploy Template

<Info> Prerequisite: Ensure you have [Git](https://git-scm.com/downloads) installed. </Info>

Using the [Deploy Code](https://app.aptible.com/create) tool in the Aptible Dashboard, you can deploy the **Laravel Template**. The tool will guide you through the following:

<Steps>
  <Step title="Deploy with Git Push">
        <img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php1.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=7fb890d33645401e160132ba972cadab" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/php1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php1.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=c77db93d15ba0c98f3586d038194d431 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php1.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=41b5fc6159cb77913261c2839c6de9e8 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php1.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=0fb9503232b8d7044af366d3dfbc4ec2 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php1.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=17a988feaf6719554f1233315783133d 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php1.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=98e94d54d2797b7f43d24974902ca1dc 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php1.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=f367897cd61d2e98956ce14e6ffd9f81 2500w" />
  </Step>

  <Step title="Add an SSH key">
    <img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php2.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=5d4290f259189b704b68718174bc1055" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/php2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php2.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=4f0c46e1fe97c29d20059c73035358a7 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php2.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=2a904c42f7f09c233f53c6bf505ccc88 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php2.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=5b6362b8c43594eec920d388b9f1f9c6 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php2.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=839a8b4b62c74c521f84246326f8dacc 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php2.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=c214fd2630cd74704d680e8c6feaf800 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php2.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=d0a4b59e7e7b148992c8d5dd47e2d3c8 2500w" />
    If you have not done so already, you will be prompted to set up an [SSH key](/core-concepts/security-compliance/authentication/ssh-keys#ssh-keys).
  </Step>

  <Step title="Environment Setup">
    <img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php3.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=e55f9a60b747aae8f6ed523eea3c218b" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/php3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php3.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=4a43ae2f98ff07903cb735b92b982edf 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php3.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=337e3b10fef30fb11b7a35966955948e 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php3.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=c7cea86e6f8a61861678d59cbf14059d 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php3.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=fa37eff98ff4051dd259e73064be8e94 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php3.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=b5600fce00267cae6b87774d6ea03a89 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php3.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=dc844a600658bbeee8c1c4c57228b888 2500w" />
    Select your [stack](/core-concepts/architecture/stacks) to deploy your resources. This will determine what region your resources are deployed to. Then, name the [environment](/core-concepts/architecture/environments) your resources will be grouped into.
  </Step>

  <Step title="Prepare the template">
    <img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php4.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=265a454c862588b957124e7334eaeac5" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/php4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php4.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=2182dcea60d95bdeeaf10dc9cd4bc290 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php4.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=fc98add810a80e1a2b9155d0de6a5030 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php4.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=10ba955afc7ca892a1e7f9f0b8bdfe02 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php4.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=bea65e31a616a9b124833fb25c19cbb7 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php4.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=71ebf643e7441dfc15ad71c6690132ed 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php4.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=98141333d61c21b39ad72803404d25ed 2500w" />
    Select **Laravel Template** for deployment, and follow command-line instructions.
  </Step>

  <Step title="Fill environment variables and deploy!">
    <img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php5.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=e2fefd126f15f6937e4057f401f0ac67" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/php5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php5.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=97e9fca34cd2f03d3e065c9a00dc490e 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php5.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=7a09c22c0aa9016aa038641f118f9fc7 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php5.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=ed3ec259bc2f6adc46c2767344bc2352 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php5.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=a825fa17d6ab3e5bf91c0578f0a48e8d 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php5.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=6f5abedb0bf1d8ace0e291e82a5e7436 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/php5.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=9dcc5206f0c133d6f322d4ed1009d443 2500w" />
    Aptible will automatically fill this template's required databases, services, and app's configuration with environment variable keys for you to fill with values. Once complete, save and deploy the code!

    Aptible will stream the logs to you in live time:
    <img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/php6.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=a336e3ac17d3d4b542379776db455642" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/php6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/php6.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=925c08dbdc980b7df6e3f6747fe8f3c4 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/php6.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=8a038ca210aaa6fd5c9cddcfd1514503 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/php6.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=6266f9ea3a5f85f4c6e09bec79ad48cc 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/php6.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=daa50f45212af9d6700ecd1d0e19205e 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/php6.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=3016c3f5f3c748a04ed8fce0a1456515 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/php6.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=dcc42ff6939ba779c0164469a597a71a 2500w" />
  </Step>

  <Step title="Expose your app to the internet">
    <img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/php7.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=c9123bc641b82d9e045943c066c4c74c" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/php7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/php7.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=50e2d019f3b0373e7326e042a34eb58b 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/php7.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=8a5805d52e1e86b14aeb06992c86b6f6 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/php7.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=3ea24a610702a11c27e77470bbe41ac9 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/php7.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=6c51060480af0acbfaff4f32abff85d4 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/php7.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=4648ef41a029bbebf8cd6e2b6f4bf0d6 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/php7.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=da74f7fb3a341d89933203c1a91004a3 2500w" />
    Now that your code is deployed, it's time to expose your app to the internet. Select the service that needs an [endpoint](/core-concepts/apps/connecting-to-apps/app-endpoints/overview), and Aptible will automatically provision a managed endpoint.
  </Step>

  <Step title="View your deployed app" icon="party-horn">
        <img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/php8.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=a0ce83d45b5c30d87d69c02e95693cd0" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/php8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/php8.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=2165810e3d8ccff041cb66574ec5079e 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/php8.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=1bb3d5dd1ebfa78d78c2ee90be467126 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/php8.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=8798e54673d2327df92d65ac1c2ded3f 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/php8.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=e0bdf7aff8f6b0d8c214280e19df7509 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/php8.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=3d04e4dd82bd9b99ff99ac9c97b67491 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/php8.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=7d724c5c8f2fc76790c6cfaa4c31deee 2500w" />
  </Step>
</Steps>

# Continue your journey

<Card title="Deploy custom code" icon="books" iconType="duotone" href="https://www.aptible.com/docs/custom-code-quickstart">
  Read our guide for deploying custom code on Aptible.
</Card>

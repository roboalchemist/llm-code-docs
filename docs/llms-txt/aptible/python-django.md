# Source: https://www.aptible.com/docs/getting-started/deploy-starter-template/python-django.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Python + Django - Starter Template

> Deploy a starter template Python app using the Django framework on Aptible

<CardGroup cols={3}>
  <Card title="Deploy Now" icon="rocket" href="https://app.aptible.com/create" />

  <Card title="GitHub Repo" icon="github" href="https://github.com/aptible/template-django" />

  <Card title="View Example" icon="browser" href="https://app-52709.on-aptible.com/" />
</CardGroup>

# Overview

This guide will walk you through the process of launching a [Python](https://www.python.org/) app using the [Django](https://www.djangoproject.com/) framework.

# Deploy Template

<Info> Prerequisite: Ensure you have [Git](https://git-scm.com/downloads) installed.</Info>

Using the [Deploy Code](https://app.aptible.com/create) tool in the Aptible Dashboard, you can deploy the **Django Template**. The tool will guide you through the following:

<Steps>
  <Step title="Deploy with Git Push">
        <img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django1.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=0e18c03c0590c5f184cfa9065828e978" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/django1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django1.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=67fbeb45818f8e497a499325ac136cc9 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django1.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=44b5b2e4a810467e78346cb9d49448d8 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django1.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=a5792bdda5208b609168ee0080c9f3dd 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django1.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=d137ebae4e1c329c9c97fa0d70e03b2c 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django1.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=0faea048055774774400b7aadc4fe3bd 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django1.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=12b7912b0e56c1b29c24a89dd9a2a0f9 2500w" />
  </Step>

  <Step title="Add an SSH key">
    <img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django2.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=dded35dce07acbc81b922f4e2792662b" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/django2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django2.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=f168b81a0b6a695f3814704c5fb193e6 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django2.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=fca324f0e5735c3e70d28d9ccb6a5599 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django2.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=5c8eab8802b18b0a1b30165bcfa1926a 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django2.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=ca85a35737f2ca76f80d13d9c4956e13 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django2.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=ad7173e258aa77d1c11fd1d8ceb235a2 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django2.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=11be364b335887c606bd8f381c42e498 2500w" />
    If you have not done so already, you will be prompted to set up an [SSH key](/core-concepts/security-compliance/authentication/ssh-keys#ssh-keys).
  </Step>

  <Step title="Environment Setup">
    <img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django3.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=805399b4dc39e1380ee75cc3cc1c729f" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/django3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django3.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=a3f48385d38f46c0c5903f7ac630d003 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django3.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=444e5121ac9fd06bbde42e73c07a39ea 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django3.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=ca477782078a73a406f2dc4b3ffb77a4 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django3.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=c172c4189e344ae4e3bf66422d346561 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django3.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=20fd56f832c39735bf3d8e827313d422 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django3.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=98faa63a0b178ccd8c6fca9f3ab04c16 2500w" />
    Select your [stack](/core-concepts/architecture/stacks) to deploy your resources. This will determine what region your resources are deployed to. Then, the name the [environment](/core-concepts/architecture/environments) your resources will be grouped into.
  </Step>

  <Step title="Prepare the template">
    <img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django4.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=af86bae61187b7b4fff5036daace7dfd" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/django4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django4.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=d0b6faa554d822e4c3966656ea91c69e 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django4.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=33fd850f1975a25904e14e68102f0a90 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django4.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=f0fe54bc0af5ff8b01ffef318c9b1a93 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django4.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=83538560be3e3c98bfda33b83e5c550c 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django4.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=ed75014e44b0e00a7624d571e3c79d8d 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django4.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=b6d8270a3ad27842fccddf7e25064269 2500w" />
    Select **Django Template** for deployment, and follow command-line instructions.
  </Step>

  <Step title="Fill environment variables and deploy!">
    <img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django5.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=2f3e10f543ef01d7eeeca62429e26755" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/django5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django5.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=8e45a3c255f881761b6d9943861b0d49 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django5.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=f103328102f1c4f580a26aa860b62413 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django5.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=3aa7f4f8f26815432896318b707013a9 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django5.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=cbeba8854d48f0d9af49fb1741dc0dd2 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django5.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=b8205d620a841f725eddc70f6729726b 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django5.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=f112d3dd016307de77dee605dd309dfe 2500w" />
    Aptible will automatically fill this template's required databases, services, and app's configuration with environment variable keys for you to fill with values. Once complete, save and deploy the code!

    Aptible will stream the logs to you in live time:
    <img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django6.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=66d30a7afbd6ac1184fb365bbcf7465a" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/django6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django6.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=6780429b8b6b7003ba1f058218e13dd3 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django6.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=e9da1adbdb3dc505b964aa80dc40649b 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django6.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=f867bd85a0cf6cd71b32868a39fbdc18 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django6.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=f30c9359655c3039f99c8b9f2b940eb4 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django6.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=c8999af7d3c9e141d788d5f3712e9905 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django6.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=5435c11fa949fbb310d212a80e1601db 2500w" />
  </Step>

  <Step title="Expose your app to the internet">
    <img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django7.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=ab2ff50e4cf3501be1046d294dca3b28" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/django7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django7.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=9ea95b19e7c2f74370d43aa901c361d0 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django7.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=ddbc672bb25fa76c9ebfb96cd2645c40 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django7.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=d1803fc8ab2b0db9df8cf5da39571eaf 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django7.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=06d536c78c8c01a8cbd45a158500acff 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django7.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=0484c7903b9254481932b50ef46793be 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django7.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=81a505066a00c5b2fbcd9b0b9504b6cb 2500w" />
    Now that your code is deployed, it's time to expose your app to the internet. Select the service that needs an [endpoint](/core-concepts/apps/connecting-to-apps/app-endpoints/overview), and Aptible will automatically provision a managed endpoint.
  </Step>

  <Step title="View your deployed app" icon="party-horn">
        <img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django8.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=ad5683908065e1d28b20bf1fd9abf54c" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/django8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django8.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=f313d36fa30df100b2240b42530e017f 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django8.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=1daa3b5398440a4cc51cf1635e914efe 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django8.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=c7b21eebfa9b28e815e6eb82dddfee36 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django8.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=387d42384b970c44869a835cd4e834ea 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django8.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=b21316e1cd19fe4342f17970db1d7d3b 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/django8.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=e8441dd28208a26092de799cc4968ba7 2500w" />
  </Step>
</Steps>

# Continue your journey

<Card title="Deploy custom code" icon="books" iconType="duotone" href="https://www.aptible.com/docs/custom-code-quickstart">
  Read our guide for deploying custom code on Aptible.
</Card>

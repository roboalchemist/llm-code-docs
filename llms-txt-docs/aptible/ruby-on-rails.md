# Source: https://www.aptible.com/docs/getting-started/deploy-starter-template/ruby-on-rails.md

# Ruby on Rails - Starter Template

> Deploy a starter template Ruby on Rails app on Aptible

<CardGroup cols={3}>
  <Card title="Deploy Now" icon="rocket" href="https://app.aptible.com/create" />

  <Card title="GitHub Repo" icon="github" href="https://github.com/aptible/template-rails" />

  <Card title="View Example" icon="browser" href="https://app-52710.on-aptible.com/" />
</CardGroup>

# Overview

This guide will walk you through the process of launching the [Rails Getting Started example](https://guides.rubyonrails.org/v4.2.7/getting_started.html) from the Aptible Dashboard.

# Deploying the template

<Info>
  Prerequisite: Ensure you have [Git](https://git-scm.com/downloads) installed.
</Info>

Using the [Deploy Code](https://app.aptible.com/create) tool in the Aptible Dashboard, you can deploy the **Ruby on Rails Template**. The tool will guide you through the following:

<Steps>
  <Step title="Deploy with Git Push">
        <img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby1.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=96256d53258cc6e13216dbc8e89a66ae" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/ruby1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby1.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=6952d457098f0824bb316c23d01b1862 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby1.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=279fa711fc1eefb5ae9df16f6bd725a7 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby1.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=dbd03af3c2047b5e1be079af25b08f8c 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby1.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=daa547850d181cd31f2e6355cb3dec3d 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby1.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=963e63c86e9a1f64b2874992d04c0b3e 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby1.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=45e14464322d6db51f54a6213371892c 2500w" />
  </Step>

  <Step title="Add an SSH key">
        <img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby2.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=e207be0a7eb863176c65af7906f09f5d" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/ruby2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby2.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=4f4a0f30d9d478542ce70336c58dbed4 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby2.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=04cb334ddb9504fab11ddc04df3f8605 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby2.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=9c94e6217d4c68150822bda9d8ba7517 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby2.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=93d082c3acbe8f654f73ba719dfdf15e 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby2.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=60e699e7c9754af0cc0dec9416f93201 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby2.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=3f6796ccf9de036c61fb31e11a0e18ab 2500w" />

    If you have not done so already, you will be prompted to set up an [SSH key](/core-concepts/security-compliance/authentication/ssh-keys#ssh-keys).
  </Step>

  <Step title="Environment Setup">
        <img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby3.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=3f1c2f75f944a64f613a5b2e73bd040e" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/ruby3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby3.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=75eb457c3d2a4632f28260ada078d1de 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby3.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=eacacac85b026e4e31980cb685ab17f9 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby3.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=5685c30ec3830c8622d0b0553ab6c0c4 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby3.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=53d5561ea8f2cfa26513cfbe7fda1025 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby3.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=49dc1d92f0d8af8367e4ea44ba22a9af 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby3.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=f777706ab406e1a59f2cc2352a492558 2500w" />

    Select your [stack](/core-concepts/architecture/stacks) to deploy your resources. This will determine what region your resources are deployed to. Then, name the [environment](/core-concepts/architecture/environments) your resources will be grouped into.
  </Step>

  <Step title="Prepare the template">
        <img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby4.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=d903342f3d08fc201483957abccef969" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/ruby4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby4.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=03c579a513da8b71c92f71fb66e95512 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby4.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=752dbe9b3695404fc3577058f7cb5901 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby4.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=e6885578ea81c637ee473c21e0f7636c 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby4.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=1de8287e511fd56f53303ea061165a69 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby4.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=7a937711cfa1852525355d3d715b89ee 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby4.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=427db204ea338dcb37b9eb16621f220a 2500w" />

    Select `Ruby on Rails Template` for deployment, and follow the command-line instructions.
  </Step>

  <Step title="Fill environment variables and deploy!">
        <img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby5.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=249b7e4498403168cac4953860df1062" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/ruby5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby5.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=2b9b4020cf56e8bc8566e622e0842f00 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby5.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=cec7500cac6d752f54fcaba1327c04ea 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby5.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=af9b1f2e9e63224db87e4e020d182e8a 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby5.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=5b7e24cfb4fb73934b293b39b693a4e4 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby5.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=5b1a6219160675de504b93b9a225639d 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby5.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=59b3bf9e8d58c1ab9b0fb37d661fee87 2500w" />

    Aptible will automatically fill this template's required databases, services, and app's configuration with environment variable keys for you to fill with values. Once complete, save and deploy the code!
  </Step>

  <Step title="View logs in real time">
        <img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby6.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=f978f55674e2f3b3b402c919fb2f38d5" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/ruby6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby6.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=51e9399978f4a91893163750ae765be6 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby6.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=744387d6da125ec8b748cb113e24a70d 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby6.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=fef1b8e7a486e855699f3e88e95719f1 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby6.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=cac5130ae5fe693f25ee745912f53491 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby6.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=029cf70e13a04d16328fbf44282b88ce 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby6.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=e0b0dc53cc2fcadfab7cf04fe3bd0cd1 2500w" />
  </Step>

  <Step title="Expose your app to the internet">
        <img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby7.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=0e1dae20dbf4e1357ff608032a80b439" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/ruby7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby7.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=e13ecec33e221679998433e269874d9e 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby7.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=231b184e7790f3995fa6a0874e3a9d86 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby7.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=52ad815b583db75eb1f716402dcdb288 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby7.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=3bb2fad80f3b3b6ab2d094106c7dd0f2 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby7.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=a3bf184780d87d6f38127ef3fcf3791b 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby7.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=63c257b9059d1ff65f602a2758ec74fa 2500w" />

    Now that your code is deployed, it's time to expose your app to the internet. Select the service that needs an [endpoint](/core-concepts/apps/connecting-to-apps/app-endpoints/overview), and Aptible will automatically provision a managed endpoint.
  </Step>

  <Step title="View your deployed app 🎉" icon="party-horn">
        <img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby8.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=50dab00f12fa2b4ed94524a909ff8431" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/ruby8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby8.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=21d90ff6e42763178db2afcd765fae4a 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby8.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=6aecffc6aedd37a177fe951d1edf802a 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby8.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=47fcf9bd0e3348f34e0b3c31e5f53959 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby8.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=0b99804bec85a2f41c4bbbbdf0254295 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby8.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=8f4d421d7aed43e580fd6e386a56aa53 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/ruby8.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=e78526a6c3d7e447eb3b328eecc9747f 2500w" />
  </Step>
</Steps>

# Continue your journey

<Card title="Deploy custom code" icon="books" iconType="duotone" href="https://www.aptible.com/docs/custom-code-quickstart">
  Read our guide for deploying custom code on Aptible.
</Card>

# Source: https://www.aptible.com/docs/getting-started/deploy-starter-template/python-flask.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Python + Flask - Demo App

> Deploy our Python demo app using the Flask framework with Managed PostgreSQL Database and Redis instance

<CardGroup cols={3}>
  <Card title="Deploy Now" icon="rocket" href="https://app.aptible.com/create" />

  <Card title="GitHub Repo" icon="github" href="https://github.com/aptible/deploy-demo-app" />

  <Card title="View Example" icon="browser" href="https://app-60388.on-aptible.com/" />
</CardGroup>

# Overview

The following guide is designed to help you deploy an example app on Aptible. During this process, Aptible will launch containers to run a Python app with a web server, a background worker, a Managed PostgreSQL Database, and a Redis instance.

<Frame>
    <img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/flask1.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=0627d26b6502fbfb650fc62e2ec920c6" alt="" data-og-width="3200" width="3200" data-og-height="1600" height="1600" data-path="images/flask1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/flask1.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=84785db267e4dd30e81a8e58615dc72e 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/flask1.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=8ddb6b597cd1ea74d807688f1ce50de2 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/flask1.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=60fe864452ee40b135925cab4e6e09b9 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/flask1.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=255564d24fbde7968b1842911d2c4512 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/flask1.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=9e2efc0f9f8dfbdcd96b4e31f4f95ada 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/flask1.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=35b8395d2e36c3069b086c5c9eeace6f 2500w" />
</Frame>

The demo app displays the last 20 messages of the database, including any additional messages you record via the "message board." The application was designed to guide new users through a "Setup Checklist" which showcases various features of the Aptible platform (such as database migration, scaling, etc.) using both the dashboard and Aptible CLI.

# Deploy App

<Info> Prerequisite: Ensure you have [Git](https://git-scm.com/downloads) installed. </Info>

Using the [Deploy Code](https://app.aptible.com/create) tool in the Aptible Dashboard, you can deploy the **Deploy Demo App**. The tool will guide you through the following:

<Steps>
  <Step title="Deploy with Git Push">
        <img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/flask2.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=fca1202761392674e0e50f2afa05cc8a" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/flask2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/flask2.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=e31af01853eebf7bf97c1e06e65f067e 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/flask2.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=6bcd9ffd9787e8392967bfc4f1e0842f 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/flask2.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=c0764d1a2d18d67dff5701ca39fc95d6 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/flask2.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=6cfe082a2fa1bf449ed616472a428b12 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/flask2.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=89f159a272c3db5fe7d660dc33e68485 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/flask2.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=a58f48026825770a8cee56a2ae166a6a 2500w" />
  </Step>

  <Step title="Add an SSH key">
    <img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/flask3.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=230ae34d856b5b3fe8c476c6fe3454c9" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/flask3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/flask3.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=268056f9bb657b48789b759ade65b9b0 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/flask3.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=4483d4b8f6114b14fdbccc40a1905ff0 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/flask3.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=fbcd180ca1a883ca395cb328d3c43961 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/flask3.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=92c9aed1493406517fd2112b4045ed6d 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/flask3.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=4d5ebfc0e580b08e2cebbd43738d2f36 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/flask3.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=5acf5fd5d7f526c7613d481f76293d24 2500w" />
    If you have not done so already, you will be prompted to set up an [SSH key](/core-concepts/security-compliance/authentication/ssh-keys#ssh-keys).
  </Step>

  <Step title="Environment Setup">
    <img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/flask4.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=c1644981d2945b756b24845227c23c8a" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/flask4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/flask4.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=7e18050736966ff9aa6e5f6807c49348 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/flask4.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=a4267dd5314a8bf77d8eb9f0d0c75175 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/flask4.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=73d9469cb460a96167f5bf5874b72381 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/flask4.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=4c15822a02b956da2f00638235796bc2 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/flask4.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=203459d77da357904134003f60f2bc03 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/flask4.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=3bf20ee91ec4683dd3be155945d138bb 2500w" />
    Select your [stack](/core-concepts/architecture/stacks) to deploy your resources. This will determine what region your resources are deployed to. Then, name the [environment](/core-concepts/architecture/environments) your resources will be grouped into.
  </Step>

  <Step title="Prepare the template">
    <img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask5.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=30672f0cb0672b43d9dd556722399f8d" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/flask5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask5.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=b3c19125129ef336e075dc74746f2014 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask5.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=7173a3ea935fdcf42b375a3e67204c13 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask5.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=6e28aed8450d5a33e2821c9612f51317 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask5.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=6bff9933c16c7f76bc89e1490ee3d784 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask5.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=537ac49cd543d25cd540d928b6c78082 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask5.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=3a4b228eec0387e216815ee6f53e4d04 2500w" />
    Select **Deploy Demo App** for deployment, and follow command-line instructions.
  </Step>

  <Step title="Fill environment variables and deploy">
    <img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask6.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=0d8f624eb8ff7e0914bc352aa9839a37" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/flask6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask6.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=d22e7df9a25b824128b8deca3e593c17 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask6.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=5d53268067eb80a811b35e43736e5b54 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask6.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=03af40225d905c6bc4141b4ebb8a9b45 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask6.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=7912fb67a23c9fa32b79501b5d309a47 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask6.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=a72029931b87b46bb526be520364698f 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask6.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=4c327a259bd99e815839adaf98024b30 2500w" />
    Aptible will automatically fill this template's app configuration, services, and required databases. This includes: a web server, a background worker, a Managed PostgreSQL Database, and a Redis instance. All you have to do is fill the complete the environment variables save and deploy the code!

    Aptible will show you the logs in live time:
    <img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask7.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=a9ba3734bd9f2ef4c7941d088e7e31ea" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/flask7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask7.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=767e4f7ca876d98b36a6f6c8c00d680c 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask7.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=50019d7c958f70960bfb56efe061f2ee 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask7.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=9a443b9655ad986dc5ac47d3afd4e665 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask7.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=0022e027fc3c844d6c2f9afc7be31393 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask7.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=51a19229631731e0e6fe57cdbf210068 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask7.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=a69c94108054e9ecbf44e69e43711cf9 2500w" />
  </Step>

  <Step title="Expose your app to the internet">
    <img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask8.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=4c34014ede13d2d1448c0654cd975a1d" alt="" data-og-width="2000" width="2000" data-og-height="1000" height="1000" data-path="images/flask8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask8.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=729a576506ce5dec3912b2c31c03c7de 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask8.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=5db4c745eca1d4c006b8e023c8454c33 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask8.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=1411ab9487b3f37cadc7f85381964f19 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask8.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=1d08efdd4f697087c703098287baee40 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask8.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=235e9c8f9280441a75d26d07f24624ba 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask8.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=13ac7c57d4bd646a9414696efc6eeb62 2500w" />
    Now that your code is deployed, it's time to expose your app to the internet. Select the service that needs an [endpoint](/core-concepts/apps/connecting-to-apps/app-endpoints/overview), and Aptible will automatically provision a managed endpoint.
  </Step>

  <Step title="View your deployed app" icon="party-horn">
    <Frame>
            <img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask9.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=541d675b0169b77deef70b1f6ae57ee7" alt="" data-og-width="3080" width="3080" data-og-height="1924" height="1924" data-path="images/flask9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask9.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=fd7b6fb730e5eb056e9e17c1d41a7962 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask9.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=306d5ab5e255aa22a849af058b10cab0 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask9.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=d1aaf94b9f8391c98fb14ade1e5b23af 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask9.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=e8cdb49d654db243da972bd66028e9c8 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask9.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=c3e6c99abda2bf54dfe38f785cf5ab35 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/flask9.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=e5e83767010a83f3479908252c66fa47 2500w" />
    </Frame>

    From here, you can optionally test the application's message board and/or "Setup Checklist."
  </Step>
</Steps>

# Continue your journey

<Card title="Deploy custom code" icon="books" iconType="duotone" href="https://www.aptible.com/docs/custom-code-quickstart">
  Read our guide for deploying custom code on Aptible.
</Card>
